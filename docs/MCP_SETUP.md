# MCP_SETUP.md — N8N MCP Server Configuration

## Quick Setup (pre nového agenta)

Ak potrebuješ aktivovať N8N MCP server:

1. **Skontroluj či existuje `.env` v projekte**
   ```bash
   ls -la .env
   ```
   Ak neexistuje, skopíruj z `.env.example`:
   ```bash
   cp .env.example .env
   ```

2. **Pridaj API key do `.env`**
   ```
   N8N_MCP_API_KEY=your_actual_n8n_api_key
   ```

3. **Restartni opencode** (config sa načítava len pri štarte)

## Konfigurácia (opencode.json)

```json
{
  "mcp": {
    "n8n": {
      "type": "remote",
      "url": "https://api.n8n-mcp.com",
      "env": {
        "API_KEY": "${N8N_MCP_API_KEY}"
      }
    }
  }
}
```

- `${N8N_MCP_API_KEY}` — placeholder ktorý opencode nahradí hodnotou z `.env`
- `.env` je v `.gitignore` — nikdy sa necommituje

## Verifikácia

Po restarte over či MCP funguje:
```
/help alebo skús pripojiť n8n server
```

Ak MCP nejde:
1. Skontroluj `.env` — správny formát `N8N_MCP_API_KEY=...`
2. Skontroluj či opencode načítava projekt z spravneho adresara
3. Skús `export N8N_MCP_API_KEY=your_key` pred spustením

## Bezpečnostné pravidlo

`.env` súbory sa **NIKDY** nečítajú cez tools.
- API key musí byť len v `.env`
- `opencode.json` obsahuje len placeholder