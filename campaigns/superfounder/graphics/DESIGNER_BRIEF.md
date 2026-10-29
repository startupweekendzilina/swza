# Grafika — špecifikácia pre grafika (fallback zadanie)

Ak by si chcel dať tieto assety profesionálne prepracovať, tu je presné zadanie.

## Brand (overené pre SWZA #13)
- **Primárna:** žltá `#F5C518` (akcent — CTA, hashtag, badge)
- **Sekundárna:** oranžová `#FF6B35` (CTA, dôraz)
- **Text:** čierna `#0A0A0A`
- **Pozadie:** biela (master square) / tmavá `#0A0A0A` (IG stories)
- **Logo:** SWZA #13 typografické (text-based), corner badge s hashtagom

## Všetkých 6 assetov
Všetky PNG sú vygenerované v `/home/node/swza/campaigns/superfounder/graphics/`. Ak ich dáš grafikovi:

### (a) `a_ig_story_frame1_mas_to_v_sebe_1080x1920.png`
- **Formát:** 1080×1920 (IG story)
- **Pozadie:** tmavá (gradient #0A0A0A → #1A1A1A)
- **Top brand strip:** žltý `#F5C518`, text „SWZA #13" vľavo, „9.–11. 10. 2026" vpravo
- **Hero text:** „Máš to v sebe?" veľký biely + žltý, dve časti na dva riadky
- **Subline:** „Superfounder lístok sa nedá kúpiť. Dá sa len získať."
- **Dátum:** „9.–11. október 2026 · Žilinská univerzita · AT Park"
- **Hashtag:** #UkazCoMasVSebe (žltý)
- **CTA strip dole:** oranžový, „SWIPE UP · VYPLŇ FORMULÁR"

### (b) `b_ig_story_frame2_10_listkov_1080x1920.png`
- **Formát:** 1080×1920
- **Pozadie:** tmavá
- **Veľké číslo:** „10" žlté, nadpis „lístkov. Nedajú sa kúpiť."
- **Stred:** „5 otázok." biely + „90 sekúnd." žltý
- **Pod ním:** „Za 54 hodín ukážeš, čo máš v sebe." (sivý)
- **CTA box:** žltý 60–80 px od stredu, text „PRESVEDČ NÁS" + „a jeden z 10 lístkov je tvoj"
- **Spodná zóna (200 px):** prázdna pre link sticker
- **Hashtag:** #UkazCoMasVSebe · #StartupWeekendZilina

### (c) `c_master_square_claim_1080x1080.png`
- **Formát:** 1080×1080 (master pre IG/FB/LinkedIn)
- **Pozadie:** biela
- **Top strip:** žltý s textom „SWZA #13 · OPERATION FOXBAT" + dátum
- **Hero claim (3 riadky):** „Nápady má kadekto. / Dotiahne ich málokto. / Ukáž, že ty áno." — prvé dva riadky čierne, tretí oranžový (akcent)
- **Akcent bar:** oranžový pod claimom
- **Subline:** „Za 54 hodín na Startup Weekende Žilina / ukážeš, čo máš v sebe."
- **Badge (privilege línia):** čierny box so žltým textom „Superfounder lístok sa nedá kúpiť. Dá sa len získať."
- **Footer:** žltý s textom „5 otázok · 90 sekúnd · 10 lístkov · #UkazCoMasVSebe"

### (d) `d_formulár_hlavička_1600x400.png`
- **Formát:** 1600×400 (Google Forms header)
- **Pozadie:** čierna
- **Vľavo:** logo SWZA #13 + OPERATION FOXBAT subtitle, veľká privilege línia (biela + žltá)
- **Vpravo:** žltý badge s „10" + „lístkov" + „5 otázok" + „90 sekúnd" + dátum

### (e1) `e1_superfounder_listok_square_1080x1080.png`
- **Formát:** 1080×1080 (štýl „vstupenka")
- **Pozadie:** tmavý gradient
- **Lístok (rotated -4°):** žltý obdĺžnik s perforáciou v strede, čierny header s textom „SUPERFOUNDER LÍSTOK", veľký čierny box s textom „NEDÁ SA / KÚPIŤ" (žltý + biely)
- **Info dole:** „5 otázok · 90 sekúnd" + dátum + hashtag
- **Corner badge:** oranžový kruh s „LEN 10 KS"

### (e2) `e2_superfounder_listok_story_1080x1920.png`
- **Formát:** 1080×1920 (IG story verzia lístka)
- Rovnaká kompozícia ako e1, ale formát na výšku, badge „LEN 10 LÍSTKOV", CTA strip dole

## Písmo
- Sans-serif, geometric, výrazné (nie Helvetica — skôr Inter, Poppins, Montserrat, alebo bold grotesk)
- Hierarchia: claim 64–86 px bold, subline 30–34 px semibold, detaily 24–28 px

## Čo grafik môže zlepšiť oproti SVG renderu
1. **Logo** — teraz je typografické „SWZA #13". Ak existuje ostré logo (SVG/PNG v Drive), nahraď.
2. **Fotka alebo ilustrácia** — momentálne je to čisto typografické. Mohol by pridať jemný vzor/štruktúru v pozadí (napr. noise, jemné línie) pre vizuálnu hĺbku.
3. **Animácia** — pre stories by sa dali 2 fram-y animovať (slide-in text). V IG sticker link to funguje.
4. **Brand knižnica** — ak máte v Canva/Creative Cloud existujúci brand kit, použi tie farby (overené fallbacky `#F5C518`, `#FF6B35`, `#0A0A0A`).
5. **Výstupné formáty** — ideálne aj PDF pre tlač (ak by sa niečo malo tlačiť na event), PNG pre social.

## Finálna kontrola pred zverejnením
- [ ] Žltá nie je príliš bledo na tmavom pozadí (kontrast OK)
- [ ] Všetok text je čitateľný na mobile (min. 24 px)
- [ ] Dátum 9.–11. 10. 2026 je všade rovnaký
- [ ] Žiadne emoji (podľa tónu kampane)
- [ ] Hashtag je #UkazCoMasVSebe (nie #UkazCoMasVSebe bez diakritiky v social)
