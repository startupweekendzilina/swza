# MEMORY.md — Context Preservation & Communication

## Core Principle: Context Preservation

**Pravidlo:** Po KAŽDOM turn (user prompt + assistant response) agent uloží do projektovej pamäte cokolvek dôležité.

### Čo ukladať po každom turn:
- Aktuálny stav úloh
- Rozhodnutia a dohody
- Zmeny v plánoch
- Čo bolo dokončené / čo zostáva
- Blokeri a problémy

### Ako ukladať:
Použi skill `para-memory-files`:

```
Skill: para-memory-files
```

### Kde nájsť informácie:
1. `docs/STAV.md` — aktuálny stav (vždy aktuálny)
2. `docs/ROLES.md` — kto vlastní čo
3. `docs/PHASES.md` — čo sa deje kedy
4. `docs/TOOLS.md` — nástroje a platformy

---

## Self-Contained Documentation Rule

**Kľúčové pravidlo:** Projekt musí byť zdokumentovaný tak, aby **akykolvek agent mohol prist bez ziadneho kontextu a pamäte a zo stavu ktory je v adresári, vediet všetko pochopit a ozivit.**

Preto:
- Všetky dôležité informácie sú v `/docs/` adresári
- `STAV.md` je vždy aktuálny — žiadne "tajné" znalosti mimo súborov
- Rozhodnutia sa dokumentujú ihneď, nie retroaktivne
- Nový agent má prečítať: STAV.md → ROLES.md → PHASES.md → TOOLS.md

---

## Communication & Handoff

### Pred začiatkom novej práce:
1. Prečítaj `docs/STAV.md`
2. Skontroluj či task nie je už dokončený
3. Over či nie sú nové blokéry

### Po dokončení tasku:
1. Aktualizuj `docs/STAV.md`
2. Ulož kontext do pamäte (para-memory-files)
3. Informuj vlastníka role ak relevantné

### Pri nejasnostiach:
- Prvý zdroj: `docs/STAV.md`
- Druhý zdroj: `docs/ROLES.md` (vlastník role)
- Eskalácia: Hlavný organizátor (Baška)

---

## Error Handling

Pri problémoch:
1. Zaloguj chybu do `docs/STAV.md`
2. Informuj vlastníka role
3. Ak je kritické: eskaluj na hlavného organizátora
4. Dokumentuj riešenie do `docs/TROUBLESHOOTING.md`

---

## Memory Files Location

Pre para-memory-files skill sa používajú tieto lokácie:
- Projekt: `/Users/danielharcek/Projects/swza-opencode-project/`
- PARA folders: v `docs/PARA/` adresári
- Daily notes: v `docs/PARA/0_DAILY/`
- Knowledge: v `docs/PARA/1_KNOWLEDGE/`