# SWZA — Proveniencia dát

> Odkiaľ pochádzajú fakty v BRAND.md, čo je lokálne, čo je len na Google Drive a ako si to dožiadať.
> Aktualizované: 2026-07-03

## Master zdroj

**Google Drive — zdieľaný SWZA priečinok** (prístup: operátor). Lokálna kópia bola stiahnutá 2026-07-02 ako Drive-export zipy (`<Folder>-20260702T*Z-3-00N.zip`), rozbalená do `~/projects/SWZA/extracted/`, znalosti destilované do `BRAND.md` a potom raw dáta lokálne zmazané (2026-07-03). **Nič sa nestratilo — všetko je na Drive.**

## Drive štruktúra ↔ čo z nej vzniklo

| Drive priečinok | Veľkosť (zip) | Čo obsahuje | Destilát / lokálne ponechané |
|---|---|---|---|
| Data Exports | 3.5 G (2 zipy: 1809+5564 súborov) | FB export `facebook-export-StartupWeekendZilina-28_05_2026-LiYLtUaq.zip` (7304 súborov, celá história stránky: posty, komentáre, médiá) + Discord export + analýzy 00–05 | Analýzy `extracted/Data Exports/0*.md` (FB: sumár, 1132 postov, komentáre, timeline, content plan; Discord: harmonogram, checklisty, roly, automatizácia, sponzori) — **hlavný zdroj BRAND.md**. Discord export ponechaný (7 M). Raw FB export ZMAZANÝ lokálne. |
| Grafika | 2.5 G (3 zipy) | PSD zdrojáky (postery, reels ending), logá, farby, hotové posty | Ponechané: `Grafika/{Logo,Colors,Posty siete,Pictures,Ilustration,Flyer kids}` (~20 M). PSD priečinok `Grafika/Grafika` (3.5 G) ZMAZANÝ lokálne. |
| Content | 1.1 G (2 zipy) | REELS videá (995 M), tlačové správy, web texty, forbes, warmup carusel, KIDS posty, follow-up emaily | Ponechané všetko okrem `Content/REELS` (videá len na Drive). |
| Komunikačné materiály | 113 M (2 zipy) | Media Kit SWZA + KIDS, email šablóny, FAQ, 2025 základná grafika, newslettre | Ponechané celé (~115 M) — priamy assets zdroj. |
| Content ideas | 12 K | 30 tém content ideas (docx) | Ponechané celé; zoznam premietnutý do BRAND.md §Content pillars. |

## Lokálny stav po cleanupe (2026-07-03)

- `~/projects/SWZA/extracted/` = **192 M** (z pôvodných ~17 G vrátane zipov a duplikátov).
- Zmazané: Drive zipy (7 G), duplicitná extrakcia FB exportu + vnorený zip (3.6 G), raw FB export `facebook-export-full` (1.8 G), PSD `Grafika/Grafika` (3.5 G), `Content/REELS` (995 M), `(1)` duplikáty.
- Overenie pred mazaním: dve FB extrakcie identické na file-liste (7304 vs 7307 — len `.DS_Store` + escaping apostrofov).

## Ako dožiadať raw dáta

1. **Fotky/videá z FB histórie** (reálne event fotky do postov): Drive → `Data Exports` → stiahnuť `facebook-export-...-LiYLtUaq.zip` → média sú v `posts/media/`.
2. **PSD zdrojáky na nové postery**: Drive → `Grafika` (podpriečinok Grafika).
3. **Reels ako referencia formátu**: Drive → `Content/REELS`.
4. Čerstvý FB export (nové posty od 28.5.2026): FB Page → Settings → Download Page Information.

## Ostatné lokálne SWZA zdroje (mimo Drive)

- `~/projects/SWZA/SWZA/` — 2026 partner-email drafty, ticketing guide, 2019 archív (promo poznámky, rozhovor zilinak.sk).
- `~/projects/SWZA/Ticketing_Research/` — prieskum ticketing platforiem (tootoot zvolený).
- `~/projects/SWZA/Startup Weekend Žilina 2025.pdf` — event prezentácia.
