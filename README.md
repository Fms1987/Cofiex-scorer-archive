# Cofiex-scorer-archive

Private reference archive backing the [cofiex-scorer](https://github.com/Fms1987/Cofiex-scorer-BETA)
skill. Raw source material — not anonymized, not meant to be queried by the skill's own
retrieval protocol (that corpus is the fichas in `Cofiex-scorer-BETA`, kept anonymized so the
skill cannot cite or self-lookup a case). This archive exists so a human (or an agent, when a
score or a ficha looks wrong) can go back to the original document.

- `Cartas-Consultas/` — raw carta-consulta texts (PDF/MD/TXT) and NT (Nota Técnica) texts, 2023–2026.
  `Resultados_Cofiex/` holds the original PDFs; `Resultados_Cofiex_md/` holds only their Markdown
  conversions (the PDF copies that used to sit alongside them there were removed as duplicates —
  same bytes already in `Resultados_Cofiex/`, see CHANGELOG below).
- `Atas Cofiex_2023_2026/` — published meeting results (PDFs) and the scoring workbook
- `External_Credit_Operations_Database_September_2026.xlsx` — compiled external-debt/COFIEX
  dataset (Senate resolutions, STN/SADIPEM, World Bank, IBGE, COFIEX/MPO): CAPAG ratings, IDH(M),
  borrowing capacity, loan history. Used by the skill's PHASE 1.6 as a local, pre-reconciled
  CAPAG/IDH/debt cross-check (see `official-data-sources.md` in the skill repo).

**Contains real proponent names, SEI process numbers, exact financial figures and exact
quantities.** Private by design; never merge into or sync from `Cofiex-scorer-BETA`.
