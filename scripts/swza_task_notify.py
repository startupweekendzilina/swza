#!/usr/bin/env python3
"""
SWZA Task Notification Script — v3 (opraveny)
----------------------------------------------
Číta TASKS_v2 sheet, detekuje zmeny owner emailu / statusu,
zoskupuje úlohy na osobu a posiela 1 email / osoba / typ udalosti.
Owner stĺpec môže obsahovať viac emailov oddelených čiarkou.

Reminder logika: úloha stale > 4 dni → posiela sa reminder.
Uloha sa považuje za stale ak je v stĺpci J prázdne ALEBO ak od
posledného reminderu (stĺpec J) uplynulo > 4 dni.

Použitie:
    python3 swza_task_notify.py          # normálny beh (+ emaily)
    python3 swza_task_notify.py --dry-run # bez odosielania emailov
"""

import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

# === CONFIG ===
SPREADSHEET_ID = "14wTR5XREjKxSXi6B4R81x669ITJ9fPYDl9vrNwM435s"
SHEET_NAME    = "TASKS"
REMINDER_DAYS = 4
SYSTEM_NAME   = "SWZA Robot"
FROM_EMAIL    = "startupweekend.zilina@gmail.com"

# Stĺpce
COL_ID       = "A"
COL_TASK     = "B"
COL_OWNER    = "E"
COL_STATUS   = "F"
COL_DEADLINE = "H"
COL_J        = "J"          # Last_reminder_sent

# Statusy znamenajúce "úloha je uzavretá"
CLOSED_STATUSES = {"done", "cancelled", "postponed"}

STATE_DIR = Path.home() / ".hermes"
STATE_FILE = STATE_DIR / "swza_task_state.json"


# ── GWS helpers ──────────────────────────────────────────────────────────────

def run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["gws"] + args, capture_output=True, text=True)


def run_json(args: list[str]) -> dict:
    r = run(args)
    if r.returncode != 0:
        raise RuntimeError(f"gws error: {r.stderr.strip()}")
    return json.loads(r.stdout)


def read_rows() -> tuple[list[dict], list[list], list[int]]:
    """
    Prečíta všetky riadky TASKS_v2.
    Returns (rows_as_dicts, raw_values, row_numbers)
    row_numbers[i] = číslo riadku v sheet (1-indexed, pre zápis J stĺpca)
    """
    data = run_json([
        "sheets", "spreadsheets", "values", "get",
        "--params", json.dumps({
            "spreadsheetId": SPREADSHEET_ID,
            "range": f"{SHEET_NAME}!A1:J1000"
        })
    ])
    values: list[list] = data.get("values", [])
    if len(values) < 2:
        return [], values, []

    headers = values[0]
    rows = []
    row_nums = []
    for i, row in enumerate(values[1:], start=2):
        d = {headers[j]: (row[j] if j < len(row) else "")
             for j in range(len(headers))}
        rows.append(d)
        row_nums.append(i + 1)
    return rows, values, row_nums


def write_j_cell(sheet_row: int, date_str: str) -> None:
    """Zapíše dátum do stĺpca J (Last_reminder_sent) pre daný riadok."""
    rng = f"{SHEET_NAME}!{COL_J}{sheet_row}"
    r = run([
        "sheets", "spreadsheets", "values", "update",
        "--params", json.dumps({
            "spreadsheetId": SPREADSHEET_ID,
            "range": rng,
            "valueInputOption": "USER_ENTERED"
        }),
        "--json", json.dumps({"values": [[date_str]]})
    ])
    ok = r.returncode == 0
    print(f"    {'[OK]' if ok else '[ERR]'} J{sheet_row} ← {date_str}")


def send_email(to: str, subject: str, body: str) -> bool:
    r = run(["gmail", "+send", "--to", to, "--subject", subject, "--body", body])
    if r.returncode != 0:
        print(f"    [EMAIL ERR] {to}: {r.stderr.strip()}", file=sys.stderr)
        return False
    print(f"    [SENT] {to}")
    return True


# ── Čistenie dát z bunky ────────────────────────────────────────────────────

def clean(v: str) -> str:
    return v.strip() if v else ""


# ── Email parsing ─────────────────────────────────────────────────────────────

def parse_emails(owner_str: str) -> list[str]:
    """
    Parsuje owner string a vráti list emailov.
    Podporuje oddel'ovače: čiarka, bodkočiarka, newline.
    Filtrované prázdne položky a neplatné emaily.
    """
    if not owner_str:
        return []
    # Normalizuj: nahraď ; a \n za ,
    normalized = re.sub(r'[\n;]', ',', owner_str)
    emails = [e.strip() for e in normalized.split(',')]
    result = []
    for e in emails:
        if e and re.match(r'^[^@]+@[^@]+\.[^@]+$', e):
            result.append(e)
    return result


# ── State management ─────────────────────────────────────────────────────────

def load_state() -> dict:
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}

def save_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def load_task_state(t_id: str) -> dict:
    return load_state().get(t_id, {})

def save_task_state(t_id: str, owner_email: str, status: str) -> None:
    state = load_state()
    now = datetime.now().isoformat()
    prev = state.get(t_id, {})
    if prev.get("owner_email") != owner_email or prev.get("status") != status:
        state[t_id] = {
            "owner_email": owner_email,
            "status": status,
            "changed_at": now
        }
        save_state(state)

def persist_state() -> None:
    """Uloží changed_at times pre všetky úlohy (beží po úspešnom behu)."""
    pass  #状态的保存发生在每次 save_task_state 调用时


# ── Hlavná logika ────────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv

    # Test mode: preposle vsetky emaily na jednu adresu (--force-all)
    test_email = None
    force_all = False
    for arg in sys.argv:
        if arg.startswith("--test-email="):
            test_email = arg.split("=", 1)[1]
        if arg == "--force-all":
            force_all = True
    if test_email:
        print(f"*** TEST MODE — vsetky emaily idu na: {test_email} ***\n")
        if force_all:
            print(f"*** FORCE ALL — posielam vsetkych 23 úloh ako keby boli nove ***\n")

    print("=" * 60)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SWZA Task Notify v3")
    if dry_run:
        print("*** DRY RUN — emaily sa nepošlú ***\n")

    # ── 1. Načítanie sheetu ──────────────────────────────────────────────
    try:
        rows, raw_values, row_nums = read_rows()
    except Exception as e:
        print(f"[FATAL] Nemôžem čítať sheet: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"  Načítaných {len(rows)} úloh z {SHEET_NAME}")

    # ── 2. Detekcia zmien ─────────────────────────────────────────────────
    # Rozdelíme udalosti podľa typu a osoby
    # assign_events:   email → list of task dicts (nové / priradené úlohy)
    # status_events:   email → list of (task_dict, prev_status) (zmeny statusu)

    assign_events = defaultdict(list)   # {email: [task, ...]}
    status_events = defaultdict(list)    # {email: [(task, prev_status), ...]}

    for row_idx, task in zip(row_nums, rows):
        t_id     = clean(task.get("ID", ""))
        t_owner  = clean(task.get("Owner (email)", ""))
        t_stat   = clean(task.get("Status", ""))
        if not t_id:
            continue

        # Parsujeme všetky emaily z owner stĺpca
        t_emails = parse_emails(t_owner)

        prev_state = load_task_state(t_id)
        prev_emails_raw = prev_state.get("owner_email", "")
        prev_emails = parse_emails(prev_emails_raw) if prev_emails_raw else []
        prev_status = prev_state.get("status", "")

        # ── Owner change ──
        if t_emails:
            if not prev_emails:
                # Prvé priradenie — posielame email ihneď
                for email in t_emails:
                    assign_events[email].append(task)
            else:
                # Zmena owner-a: nájdi rozdiely a pošli email iba pri zmene
                new_emails = set(t_emails) - set(prev_emails)
                for email in new_emails:
                    assign_events[email].append(task)

        # ── Status change (posielame VŠETKÝM aktuálnym ownerom) ──
        if t_stat and prev_status and t_stat != prev_status:
            for email in t_emails:
                status_events[email].append((task, prev_status))

        # Uložíme aktuálny stav
        save_task_state(t_id, t_owner, t_stat)

    # ── 3. ZOSKUPENÉ EMAILY — Assignment ───────────────────────────────
    if assign_events:
        print(f"\n  Nové / zmenené priradenia ({len(assign_events)} osôb):")
        for email, task_list in assign_events.items():
            task_lines = ""
            for t in task_list:
                task_lines += f"  • {t.get('ID','')}: {t.get('Úloha','')} (deadline: {t.get('Deadline','')})\n"
            subject = (
                f"[SWZA] Priradené nové úlohy — {len(task_list)}ks"
                if len(task_list) > 1
                else f"[SWZA] Nova uloha priradena: {task_list[0].get('Úloha','')}"
            )
            body = f"""Ahoj!

Bol ti priradený nový task v SWZA organizácii:

{task_lines}
Prosím, aktualizuj status priamo v Sheete tu:
👉 https://docs.google.com/spreadsheets/d/14wTR5XREjKxSXi6B4R81x669ITJ9fPYDl9vrNwM435s/edit?gid=2099318786#gid=2099318786

--
{SYSTEM_NAME}"""

            print(f"    {email} ({len(task_list)} úloh)")
            if dry_run:
                print(f"    [DRY RUN] Subject: {subject}")
            else:
                recipient = test_email if test_email else email
                send_email(recipient, subject, body)

    # ── 4. ZOSKUPENÉ EMAILY — Status change ─────────────────────────────
    if status_events:
        print(f"\n  Zmeny statusu ({len(status_events)} osôb):")
        for email, events in status_events.items():
            task_lines = ""
            for t, prev_status in events:
                task_lines += (
                    f"  • {t.get('ID','')}: {t.get('Úloha','')} "
                    f"({prev_status} → {t.get('Status','')})\n"
                )
            subject = f"[SWZA] Status ulohy aktualizovany"
            body = f"""Ahoj!

Niektoré z tvojich úloh boli aktualizované:

{task_lines}
Pozri si zmeny a prípadne ďalej reaguj v Sheete:
👉 https://docs.google.com/spreadsheets/d/14wTR5XREjKxSXi6B4R81x669ITJ9fPYDl9vrNwM435s/edit?gid=2099318786#gid=2099318786

--
{SYSTEM_NAME}"""

            print(f"    {email} ({len(events)} zmien)")
            if dry_run:
                print(f"    [DRY RUN] Subject: {subject}")
            else:
                recipient = test_email if test_email else email
                send_email(recipient, subject, body)

    if not assign_events and not status_events:
        print("\n  Žiadne nové udalosti.")

    # ── 5. REMINDER LOGIKA (4 dni) — ZOSKUPOVANÁ PO OSOBE ───────────────
    # Pravidlo Zuzky 25.6.2026: 1 email / osoba / beh — všetky stale úlohy
    # daného vlastníka idú do jedného emailu ako odrážky. 2+ úloh = 1 email.
    # (Netreba spamovať ľudí.)
    print(f"\n  Kontrola stale úloh (> {REMINDER_DAYS} dní bez reminderu):")
    now = datetime.now()

    # Fáza 1: nazbieraj remindre zoskupené podľa emailu
    # reminder_events[email] = list of (row_idx, task)
    reminder_events: dict[str, list[tuple[int, dict]]] = defaultdict(list)
    reminder_rows: list[tuple[int, str]] = []  # (row_idx, date_str) pre J stĺpec

    for row_idx, task in zip(row_nums, rows):
        t_id     = clean(task.get("ID", ""))
        t_owner  = clean(task.get("Owner (email)", ""))
        t_stat   = clean(task.get("Status", ""))
        if not t_id:
            continue

        # Preskoč uzavreté
        if t_stat in CLOSED_STATUSES:
            continue

        # Preskoč úlohy bez ownera — nemá koho pingnúť
        t_emails = parse_emails(t_owner)
        if not t_emails:
            continue

        # last_reminder_sent je v stĺpci J
        raw_row_idx = row_idx - 1
        last_reminder_str = ""
        if raw_row_idx < len(raw_values):
            raw_row = raw_values[raw_row_idx]
            if len(raw_row) > 9:
                last_reminder_str = clean(raw_row[9])

        should_remind = False

        if last_reminder_str:
            try:
                lr_dt = datetime.strptime(last_reminder_str, "%Y-%m-%d")
                should_remind = (now - lr_dt) > timedelta(days=REMINDER_DAYS)
            except ValueError:
                should_remind = True
        else:
            prev = load_task_state(t_id)
            changed_at_str = prev.get("changed_at", "")
            if changed_at_str:
                try:
                    ch_dt = datetime.fromisoformat(changed_at_str)
                    should_remind = (now - ch_dt) > timedelta(days=REMINDER_DAYS)
                except ValueError:
                    should_remind = False
            else:
                # Prvýkrát vidím túto úlohu — len si zapamätám a skipnem
                state = load_state()
                state.setdefault(t_id, {})["changed_at"] = now.isoformat()
                save_state(state)
                print(f"    {t_id}: prvá detekcia, sledujem odteraz")
                continue

        if should_remind:
            for email in t_emails:
                reminder_events[email].append((row_idx, task))

    # Fáza 2: pošli JEDEN email / osoba so všetkými jej stale úlohami
    if reminder_events:
        print(f"\n  Remindre — 1 email / osoba ({len(reminder_events)} osôb):")
        for email, entries in reminder_events.items():
            task_lines = ""
            row_idxs_to_update: list[int] = []
            for row_idx, t in entries:
                task_lines += (
                    f"  • {t.get('ID','')}: {t.get('Úloha','')}\n"
                    f"      Deadline: {t.get('Deadline','') or '—'} | "
                    f"Stav: {t.get('Status','') or '—'}\n"
                )
                row_idxs_to_update.append(row_idx)

            n = len(entries)
            if n > 1:
                subject = f"[SWZA] Pripomienka: {n}× úloha čaká na aktualizáciu"
            else:
                e0 = entries[0][1]
                subject = (
                    f"[SWZA] Pripomienka: v#{e0.get('ID','')} — "
                    f"{e0.get('Úloha','')} (uz {REMINDER_DAYS}+ dní)"
                )

            body = f"""Ahoj!

Automatická pripomienka — tvoje úlohy nemali {REMINDER_DAYS}+ dní aktualizovaný status:

{task_lines}
Prosím, aktualizuj status priamo v Sheete (alebo daj vedieť, ak potrebuješ pomoc):
👉 https://docs.google.com/spreadsheets/d/14wTR5XREjKxSXi6B4R81x669ITJ9fPYDl9vrNwM435s/edit?gid=2099318786#gid=2099318786

--
{SYSTEM_NAME}"""

            print(f"    {email} → {n} úloh (1 email)")
            if dry_run:
                print(f"    [DRY RUN] Subject: {subject}")
            else:
                recipient = test_email if test_email else email
                if send_email(recipient, subject, body):
                    for row_idx in row_idxs_to_update:
                        reminder_rows.append((row_idx, now.strftime("%Y-%m-%d")))

    # ── 6. Update J stĺpca ───────────────────────────────────────────────
    if reminder_rows:
        print(f"\n  Ukladám Last_reminder_sent do stĺpca J:")
        for row_idx, date_str in reminder_rows:
            if dry_run:
                print(f"    [DRY RUN] J{row_idx} = {date_str}")
            elif not test_email:
                # V test modeu nezapisujeme do sheetu
                write_j_cell(row_idx, date_str)

    # ── 7. Summary ──────────────────────────────────────────────────────
    total_events = len(assign_events) + len(status_events)
    total_reminder_tasks = sum(len(v) for v in reminder_events.values())
    print(f"\n{'='*60}")
    print(f"  Úloh: {len(rows)}")
    print(f"  Assignmentov: {len(assign_events)} osôb / {sum(len(v) for v in assign_events.values())} úloh")
    print(f"  Status zmien: {len(status_events)} osôb")
    print(f"  Remindere: {len(reminder_events)} emailov / {total_reminder_tasks} úloh")
    print(f"  {'[DRY RUN — nič nebolo odoslané]' if dry_run else '[HOTOVO]'}")

    if not dry_run:
        persist_state()


if __name__ == "__main__":
    main()
