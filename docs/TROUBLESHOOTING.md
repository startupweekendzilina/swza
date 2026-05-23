# TROUBLESHOOTING.md — Archív chýb a riešení

## Formát záznamu

Každá chyba má:
- **Dátum:** Kedy sa vyskytla
- **Problém:** Čo sa stalo
- **Príčina:** Prečo sa to stalo
- **Riešenie:** Ako sme to opravili
- **Osoba:** Kto to vyriešil

---

## [2026-05-18] Google OAuth 414 URI Too Long

**Problém:** Pri OAuth prihlásení cez Google v n8n self-hosted:
```
OAuth Authorization Error
Request failed with status code 414
```

**Príčina:** Nesúlad redirect URI medzi n8n a Google Cloud Console, alebo príliš dlhá URL.

**Riešenie:** Skontrolovať či redirect URI v n8n presne zodpovedá Authorized redirect URI v Google Cloud Console — znak po znaku (bez/s koncom slash, https/http, www).

---

## [2026-05-18] Google OAuth 403 access_denied

**Problém:** Pri OAuth prihlásení:
```
Access blocked: webup.sk has not completed the Google verification process
Error 403: access_denied
```

**Príčina:** OAuth app bola v stave "Testing" — prístup mali len schválení testovací useri.

**Riešenie:** Zmeniť Publishing status z "Testing" na "Production" v Google Cloud Console → OAuth consent screen.

---

## [2026-05-18] n8n MCP tool JSON parsing error

**Problém:** Pri volaní `n8n_create_workflow` alebo `n8n_update_partial_workflow`:
```
JSON parsing failed: Expected ',' or '}' after property value
```

**Príčina:** Tool niekedy zlyhá pri zložitých JSON štruktúrach (viacriadkové reťazce, špeciálne znaky).

**Prevencia:**
1. Používať jednoduchšie štruktúry
2. Použiť `intent` parameter vždy
3. Pre komplexné kódy použiť `patchNodeField` s `__patch_find_replace` namiesto celého bloku
4. V prípade zlyhania: manuálna editácia v n8n UI

---

## [2026-05-18] Code node čítal nesprávne stĺpce zo Sheet

**Problém:** Code node nemal žiadny output — stĺpce A, C neexistovali.

**Príčina:** Google Sheets vracia dáta s hlavičkami z prvého riadku, nie s písmenami stĺpcov:
- `row.A` → neexistuje
- Správne: `row['OWNERSHIP OBLASTI']` (názov stĺpca z hlavičky)
- `row.C` → neexistuje
- Správne: `row.col_3` (pre 3. stĺpec) alebo `row['col_3']`

**Prevencia:**
1. Pred písaním Code nodu si pozrieť SKUTOČNÚ štruktúru dát z Google Sheets
2. Použiť `console.log($input.all())` alebo pozrieť output node pred Code node
3. Stĺpce bez hlavičiek majú formát `col_0`, `col_1`, `col_2`...
4. Premenovať hlavičky v Google Sheets na jednoduché názvy bez medzier

**Riešenie:** Opraviť Code node kód:
```javascript
const items = $input.all();
let output = '';
for (const item of items) {
  const row = item.json;
  if (!row['OWNERSHIP OBLASTI']) continue;
  const task = row['OWNERSHIP OBLASTI'] || 'N/A';
  const owner = row.col_3 || 'N/A';
  output += `Task: ${task}, Owner: ${owner}\n`;
}
return [{json: {message: output || 'No tasks found'}}];
``` Toto umožní prístup bez nutnosti full Google verification processu (pre self-hosted n8n s obmedzeným počtom userov).

**Varianta:** Alternatívne mohlo byť pridanie `startupweekend.zilina@gmail.com` do testovacích userov.