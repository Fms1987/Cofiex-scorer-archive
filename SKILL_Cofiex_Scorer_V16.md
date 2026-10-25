---
name: cofiex-scorer
description: Simulates COFIEX technical evaluation of a carta-consulta under Res.
  Normativa 1/2024 (amended by Res. 32/2025, 142/2026, 150/2026, 151/2026). Outputs
  score range (Annex II rubric), eliminatory check (Art. 28), sublimit viability gate,
  senior MDB review, GTEC questions, iteration/persistence analysis, and correction
  plan. 

metadata:
  version: '16.1'
  language: en
  author: Fabricio Martins
  updated: '2026-07-02'
---
## BLIND-JUDGMENT PRINCIPLE (MANDATORY — READ BEFORE ANY UPDATE)
This skill is a **blind evaluator**. It must score any incoming carta-consulta on its
intrinsic merits and on the regulatory/empirical calibration encoded here — **never** by
recognizing or matching a specific real project, proponent, CC number, or meeting outcome.

**Calibration is preserved as anonymized empirical anchors only:** numeric ranges,
score thresholds, modality discounts, bonus criteria, and profile-based references
(e.g. "investment op, 4 strategic areas, profile B → AE ~6,5"). Identifying metadata
(proponent name, municipality/state, CC/PFE number, meeting number tied to a named case)
is deliberately stripped so the evaluator cannot reverse-engineer a known verdict.

**MAINTENANCE RULE (applies to every future version):**
1. New empirical findings must be folded in as **anonymized anchors** (profile + numbers),
   never as named cases or "this project was approved" precedents.
2. When a new blind test or corpus session is added, strip the identity before storing
   the calibration value it imparts. Keep the *what it teaches*, drop the *who it was*.
3. Do not reintroduce named-precedent tables, per-meeting CC rosters, or session-by-session
   changelogs. Consolidate findings into the calibration sections below.
4. The output must never cite a real project as a comparator. Use anonymized profiles.

Violating these rules destroys the blind character of the skill and biases scoring.

### Update discipline (4 blind-judgment update sub-rules)
Whenever new evidence/calibration is incorporated, apply ALL of the following:
1. **Empirical anchor required.** Every parameter change ships with an anchor (number of
   blind tests / date) and a one-line rationale. No change without an anchor.
2. **Ranges over exceptions.** New information is translated into ranges/probabilities,
   never into ad-hoc named exceptions.
3. **Official tables are not user-overridable.** User-supplied values for regulated inputs
   (CAPAG, sublimit caps) never overwrite official tables without verifiable metadata.
4. **Anonymous changelog only.** Record only: parameter changed, new value/range, empirical
   reason (e.g. "n blind tests = k"). Never cite an identifiable carta-consulta.

## About this skill
Simulates the COFIEX technical evaluation of a carta-consulta (external financing proposal)
under **Resolução Normativa nº 1/2024**, consolidated 18/05/2026 (amended by COFIEX
Res. 32/2025, 142/2026, 150/2026, 151/2026).

On receiving a carta-consulta, briefly state what the skill does before analyzing: it
simulates the technical review (Art. 9–23), the eliminatory gate (Art. 28), the sublimit
(Art. 25), the objective scoring (Art. 10, Annexes II–III), the calibrated GTEC questions,
and the final technical opinion with section-by-section improvement suggestions.

**SMART quality (corpus-wide):** Formula 100%, Unit 100% are universal; **Verification is
the weakest field** (~40–53%); baseline presence varies by sector (digital/justice defer it;
fiscal/environment/water include it). Avg ≈ 3.7/5.

**Regulation reading confirmations (NR 1/2024 consolidated).**
- Annex II weights A=5 / B=3 / C=2 / D=1 / E=0.5; IDH formula per Art. 18 (relative to meeting).
- Two distinct +1 bonuses, **jointly capped at AE=10**: PPA-priority bonus (Art. 15 §3º) and
  Frontier-Zone bonus (Art. 15 §4º).
- Strategic-Areas catalogue uses numbering **101–307** (PPA 2024–2027). The old 1.1–1.15
  numbering (Res. 17/2021, SIGS, discontinued per Art. 50) is structural reference only.
- Official Annex I (PFE) structure: I. Project (Identification, Justification, Objectives,
  Indicators, Components, Beneficiaries) · II. Strategic Areas · III. Management · IV. Risks
  · V. Financing · VI. Preparatory Actions · VII. Contacts.

**Score-component ceilings (confirmed against the regulation):** AE max 10 · IDH max 2 ·
CAPAG max 2 · Debt max 1 · **Total max 15** (subnational). Federal = AE only (max 10).
Bonuses are absorbed inside the AE=10 ceiling; they do not push total above 15 by default
(see PHASE 9, cap_extensível).

## Cross-cutting Empirical Findings (anonymized anchors)
These are the calibration lessons distilled from all corpus sessions and blind tests, stored
as patterns rather than named cases.

**Delivery model dominates sector label.** On-lending / pass-through operations
(development banks lending onward to subnationals/subprojects) score low on AE
(≈3.3–5.5) **only when indicators are genuinely deferred** to undefined subprojects (baseline
and/or target undefined at CC stage). The discount attaches to *deferred indicators*, not to
the typology label. A sovereign-fund or financial-intermediation operation that presents a
full set of well-structured, SMART, baselined OEs is scored on the merit of those indicators
(anchor: fund/intermediation op with ~10 well-structured OEs → AE ~9.0). Worst-case
on-lending anti-pattern: all indicators with baseline=0 **and** target=0 simultaneously
(does not correlate with ticket size — the largest on-lending tickets often show the least
indicator development).

**Modality must be identified before penalizing indicator sparsity.**
- PBL/DPL/guarantee-fund operations structurally carry only 2–3 indicators (prior actions /
  policy triggers replace a project logframe). Not a preparation gap. (GTEC Q19.)
- DLI (Disbursement-Linked Indicator) / SDL / PBR is a distinct logic: score against
  disbursement-trigger adequacy, not raw indicator count. Dominant for development-bank
  climate finance.
- DPL indicator *richness* varies: a DPL tying 12 named objectives to 12 trackable indicators
  is materially stronger than a 2–3-indicator fiscal DPL — do not apply the "thin = normal"
  exemption uncritically.

**Institutional-preparation uplift (anchor: blind-test batch).** Well-prepared social or
program operations — approved enabling law, named impact-evaluation partner (e.g. a recognized
evaluation institute), real measured baselines, field prototype — earn an AE uplift into the
A/B band even without large physical infrastructure. Preparation maturity (legal marco +
evaluation design + baselines) is a substantive AE driver, not narrative. Flag these inputs
explicitly when present and map to uplift.

**Sector-label contamination.** Files tagged by keyword, not by dominant strategic area.
Contamination is high in health (~62%) and education (~50%) — driven by boilerplate strategic
items (e.g. generic "improve health/education conditions") and by multi-theme public-management
("Progestão"-style) operations whose indicators are 100% HR/payroll/procurement/pension.
Contamination is low (~5–15%) in water/sanitation and environment/climate (specialized
single-sector institutions). **Verify a CC's dominant strategic area against its actual
indicator set before applying any sector template** (GTEC Q23).

**Ready-made sectoral SMART scaffolds** (pre-existing national regulatory benchmarks any CC
in the subsector should reference): CID-10/DATASUS (health epidemiology), IDEB/SAEB-INEP
(education), iRAP (road safety), DEC/FEC-ANEEL (power distribution), SNIS-style indices
(water/sanitation: IAA, IAE, índice de perdas). CCs using these score highest on SMART.
Wait-time-by-procedure is a strong, low-cost citizen-facing access indicator (health).

**Financial modalities and their AE expectation profiles:**
1. Standard investment loan → project logframe.
2. PBL/DPL → prior-action triggers (2–3 indicators normal).
3. DLI/SDL/PBR → disbursement-linked result indicators.
4. **Guarantee on a third-party concession** (sovereign guarantee for a concessionaire;
   credit does not finance works) → indicators measure concession/contract performance
   (e.g. carbon sequestered, area restored, milestones), not direct delivery (GTEC Q24).
5. **Guarantee on recurring PPP counter-payments** (Art. 25 IV; contrapartida waiver Art. 36
   VI) → service-level indicators (uptime, MKBF, accessibility, wait time), not works delivery;
   cite the applicable PPP sublimit resolution (GTEC Q28).

**Other recurring patterns to flag (not eliminatory):**
- **Multi-tranche megaproject:** one physical project financed via several CCs/creditors.
  Indicator overlap is by design — check sibling tranches before flagging duplication (Q26).
- **Climate-disaster submission cluster:** many CCs from one event across several creditors,
  with no declared coordination — flag duplication/coordination risk (Q25).
- **Dual-creditor operations:** can inflate apparent indicator quality through repetition;
  flag overlapping indicators across related CCs from the same borrower.
- **Self-referential indicator:** using the entity's own CAPAG (or analogous recalibrated
  rating) as an outcome target risks loss of comparability mid-project (Q22).
- **GBV/GRM safeguard indicator:** driven by the **financing vehicle** (World Bank ESF, or
  Climate Investment Funds/CIF), not by creditor identity. Expected for ESF/CIF operations
  with civil works in vulnerable areas (Q27).
- **Racial/gender quotas as formal contract subcomponents** appear across all government
  levels (municipal/state/federal) — a substantive AE element, not mere narrative.
- **Documented zero-baseline** (explained: "territories selected later by criteria") scores
  materially better than an undocumented baseline=0.
- **Debt-restructuring** operations are exempt from the Art. 28 counterpart minimum
  (Art. 3º, II, Res. COFIEX 03/2019) and from PPA inclusion (Art. 7º §7º Res. Senado 43/2001,
  debt service already in LOA/LDO). Exemption attaches to the **modality, not the sector** (Q21).

**Strongest exemplar profiles (anonymized, for drafting reference):**
- *A.1 Theory of Change — STRONG:* explicit quantified causal chain with a counterfactual
  ("with-vs-without network" scenario) monetizing several externality categories per indicator.
- *A.5 Financial Sustainability — STRONG:* multiple post-project OPEX streams quantified, each
  with a named funding source; or counterpart explicitly earmarked to a named post-project
  program with PPA/legislative backing. (Corpus baseline: 0/14 of the original set rated STRONG
  on A.5 — this is the single highest-value differentiator available.)
- *Rural ToC scaffolding:* named M&E systems with "(P)" output vs "(R)" outcome tagging and a
  3-stage evaluation design (baseline → intermediate → final) rate STRONG/ADEQUATE even without
  a narrative diagram; a Multidimensional Poverty Index composite is the clearest causal chain.
- *Justice/modernization with innovative outcome indicators:* SMART outcome indicators with
  measured baselines (e.g. asset-recovery / patrimonial-persecution outcomes) anchor AE in the
  upper band (anchor: such a profile → AE ~8.0, up from a generic-modernization ~6.5).

## Behavioral Rules
- Clinical language. Deficiencies first.
- Score: AE (max 10) + IDH (max 2) + CAPAG (max 2) + Debt (max 1) = max 15.
- CAPAG D = hard eliminatory (Art. 28, I, c). CAPAG C = 0 pts, non-competitive but **not**
  eliminatory. CAPAG 0.000 for unclassified entities (most municipalities) = 0 pts, not eliminatory.
- Federal entities: CAPAG/IDH/Debt do NOT apply; AE only (max 10); no AE floor.
- Subnational AE floor: 3.0 pts (Art. 28, I, b).
- Score as a RANGE (min/expected/max), ±1 level uncertainty.
- **Sublimit positioning ≥ score maximization in a supply-constrained market.**
- **Ticket size ≤ estimated meeting cap is a necessary condition for approval, independent of score.**
- **Scores are stable across resubmissions of identical CC text → identical score.** Iteration
  strategy = timing + ticket + sublimit, not CC revision.
- **Persistence has diminishing returns:** 2nd attempt ~60% success, 3rd ~17%, 4th+ ~0%.
  Recommend max 2 cycles before fundamental restructuring.
- "Withdrawn" (Res. 17/2021, proponent self-removed pre-scoring) ≠ "Not approved" (Res. 1/2024,
  scored but cap-blocked or eliminatory) — different strategic signals.
- All inputs echoed verbatim. Every output carries the version stamp.
- **Input integrity precedes scoring** (see PHASE 1.6): regulated inputs are not auto-trusted.

## PHASE 0 — Regulatory Live Check
At session start, search:
- `"Resolução Normativa COFIEX" site:mpo.gov.br OR site:gov.br 2025 2026`
- `COFIEX reunião aprovados resultados 2025 2026`
- Newer resolution detected → flag REGULATORY UPDATE. Unavailable → flag Live check unavailable.

Active regulatory base:
- Res. Normativa COFIEX nº 1 (22 Nov 2024) — main framework
- Res. 32/2025 — amends Res. 1/2024
- Res. 142/2026 (24 Mar 2026) — amends Res. 2/2025 and Res. 1/2024
- Res. 150/2026 (26 Mar 2026) — technical/financial modifications
- Res. 151/2026 (26 Mar 2026) — BRL restructuring restrictions
- Portaria MF/STN 857/2026 (27 Mar 2026) — Adjustment Factor 0.78, CAPAG consolidation
- CMN 5.282/2026 (26 Feb 2026) — subnational sublimit share → 29.7%

## PHASE 1 — Mandatory Intake
**First ask:** "Do you have a pre-filled file (draft CC, intake form, or prior scoring sheet)
to attach? If yes, upload it now."
- File attached → read fully, pre-populate every inferable field, ask only for blanks/ambiguities.
- No file → run the full sequential Q&A (use `references/protocolo-preenchimento.md` v2.0 as
  the structured guide; Part I = scoring inputs Blocks 0–8, Part II = PFE form Blocks 9–15).

**Operation value is the mandatory first-line input.**

Block I — Identity & Financials (PRIORITY): I.1 Full name | I.2 Abbreviated | I.3 Type
(investment/restructuring/on-lending) | I.4 Proponent | I.5 Entity type (federal/state/DF/
municipality/federal statal/subnational statal/IF) | **I.6 Creditor** | **I.7 Currency** |
**I.8 Total value USD-eq ←MANDATORY** | **I.9 Loan amount USD-eq ←MANDATORY** | I.10
Counterpart % (flag if <20% without waiver) | I.11 Target sublimit (General/PPP/Env-Climate/
Fiscal/Debt-Restr/BRL-Ops/Federal).

Block II — Strategic Areas: Annex II codes + narrative per area.

Block III — Entity Profile: CAPAG (A+/A/B+/B/C/D/unclassified) + **CAPAG consultation date and
source (mandatory metadata)** | Basel (IFs) | GAF/ROI (statals) | DC/RCL | Debt trend (5 levels)
| IDH/IDHM (3 dec.) | Region | Frontier zone Y/N | PPA priority integral Y/N | Fiscal Recovery
Plan Y/N | Art. 28 d–h each Y/N | **IBGE code (for cross-check)**.

## PHASE 1.6 — Input Integrity Gate (mandatory pre-scorer)
Regulated inputs are not auto-trusted. Run BEFORE classification:
- **CAPAG metadata.** Reject a CAPAG value with no consultation date/source. Verify the rating
  belongs to the STN cycle in force at the target-meeting date (Portaria 857/2026 recalculations
  may have shifted a borderline-B entity). Missing metadata → `input_flag`, do not assign CAPAG
  points until validated.
- **IBGE-code × UF cross-check.** Confirm the entity's IBGE code matches its declared name/UF.
  Discrepancy → `input_flag`; do not auto-use dataset CAPAG/IDH for that entity until resolved.
- **Fiscal-capacity consistency.** Sanity-check declared values/projections against entity type
  and ticket. Outliers → `input_flag`.
- **No silent override.** A flagged input blocks automatic use of the corresponding dataset value;
  surface the flag in the output and request correction.

## PHASE 2 — Entity Classification
| Entity | AE floor | CAPAG | IDH | Debt | Main gate |
|---|---|---|---|---|---|
| Federal organ | None | N/A | N/A | N/A | SOF adequacy Art. 23 |
| Federal non-dep. statal | None | GAF/ROI or Basel | N/A | Own matrix | — |
| Subnational State/DF/Muni | 3.0 | STN if classified | Yes | 5-level | Art. 28, I, a–h |
| Subnational non-dep. statal | None | GAF/ROI | N/A | Exigível/PL | — |
| Financial institution/agency | None | Basel | N/A | Basel cat. | — |

> **Municipal SEM (sociedade de economia mista):** treated under subnational-statal rules
> (no AE floor, GAF/ROI-based CAPAG, Exigível/PL debt). A SEM with strong own-revenue (e.g. water
> tariff) may qualify for waiver of the Art. 28 counterpart minimum (anomaly — confirm regime).

SEAID coordination axes: State Modernization | Infrastructure | Social & Sustainability.

## PHASE 3 — Technical Screening (Annex I)
Mark COMPLETE / INCOMPLETE / MISSING / N.A. per section: I Project | II Strategic Areas |
III Management | IV Risks | V Financing | VI Preparatory | VII Contacts | CAPAG docs |
STN opinion (conditional) | SOF adequacy (federal). Binary gate: failed = no scoring.
Overall: APPROVED / CONDITIONAL / REJECTED.

Common Annex I weaknesses (anonymized corpus patterns):
- Missing/vague risk matrices (esp. environmental licensing for infrastructure).
- Incomplete post-project sustainability/maintenance plans — near-universal; few quantify costs.
- Counterpart sources "to be secured during preparation", not legislatively secured.
- Indicators declared without baseline or verification mechanism.
- Indicators with excessively wide target ranges (e.g. "1,000–10,000 jobs") — request point
  target with baseline (GTEC; lowers AE if uncorrected).
- Justice ops: governance ambiguity between judicial independence and executive UGP control.
- On-lending ops: generic Section II because subprojects are undefined at CC stage (SEAID
  historically accepts this for federal statal intermediaries).
- Dual-creditor ops: stronger Section IV (dual scrutiny) but weaker Section I coherence
  (component fragmentation).

## PHASE 4 — Eliminatory Checks (Art. 28)
Subnational Art. 28, I: (a) Annex I rejected · (b) AE < 3.0 · (c) CAPAG D [C = 0 pts, NOT
eliminatory] · (d) judicial block · (e) no STN opinion · (f) delays/guarantee honors ·
(g) contract violation · (h) unanswered revision.
Federal: SOF inadequacy (Art. 23).
Also check: PRF/RRF incompatibility | counterpart <20% without waiver | incomplete docs |
environmental-licensing gap.

Anonymized precedents: CAPAG D confirmed eliminatory under NR 1/2024; dual constraint possible
(sublimit exhausted AND absence from an active Fiscal Recovery Plan).

## PHASE 5 — Strategic Areas Scoring (AE)
### PPA 2024–2027 Objectives (35)
Axis 1 — Social: 101 Poverty · 102 Health/SUS · 103 Early childhood/edu · 104 Secondary/technical
· 105 Creative economy · 106 Human rights · 107 Women · 108 Indigenous/quilombola · 109 Anti-racism
· 110 Social security · 111 Sustainable cities · 112 Safety · 113 Sport.
Axis 2 — Economic: 201 Environment · 202 Disaster/climate · 203 Family farming · 204 Decarbonization
· 205 Competitiveness · 206 ST&I · 207 Labor · 208 Clean energy · 209 Digital · 210 Logistics
· 211 Trade · 212 Water · 213 Tourism · 214 Regional equity · 215 Mining.
Axis 3 — Democracy: 301 Transparency · 302 State capacity · 303 Digital govt · 304 Defense
· 305 Int'l cooperation · 306 Fiscal · 307 Justice.
*Art. 15 §3º priorities (bonus-eligible): 101, 102, 103, 111, 201, 210, 212.*

### Rubric — Annex II + operational checklist
| Grade | Score | Description | Checklist (all YES) |
|---|---|---|---|
| A | 5 | Direct + SMART + structural + majority resources + innovative | Direct PPA link · SMART w/baseline · >50% budget · feasible timeline · innovation |
| B | 3 | Direct + SMART + high impact + significant resources | Direct PPA link · SMART w/baseline · >30% budget · feasible timeline |
| C | 2 | Relevant + SMART + moderate impact | PPA relevance · indicators (not fully SMART) · some budget |
| D | 1 | Specific + indicators + low impact | PPA mention · basic indicators · minimal budget |
| E | 0.5 | Low relevance | tangential PPA · no indicators/targets |

**SMART (per indicator):** 1. Specific (single defined outcome) · 2. Measurable (formula + unit)
· 3. Achievable (realistic vs. baseline/timeframe) · 4. Relevant (measures the objective) ·
5. Time-bound (baseline year + target year).

**AE score drivers (anonymized):**
- ISO-standard / ready-made benchmark indicators (ISO 37120/22/23; CID-10; IDEB; iRAP; DEC/FEC;
  SNIS) satisfy SMART by design → strongest predictor of AE ≥ 8.0.
- A **national-benchmark anchor indicator** present in a multi-sector CC adds a systematic
  ~+0.5 to the AE estimate (anchor: multi-sector CC, 7 OEs mix 3B + 4C/D, with a national
  anchor indicator → AE ~8.0).
- "Indicators to be defined during preparation" / baseline=0 by design → tier D–E (typical of
  genuinely deferred on-lending; NOT applied to funds with fully specified indicators).
- Physical baselines with year-over-year targets → tier B–A.
- Output-only indicators ("X systems deployed") without outcome measurement → tier C–D.
- Technical exhaustiveness ≠ SMART compliance (a highly detailed CC with output-level indicators
  is still mid-tier AE).
- The +1 "100% PPA integral" bonus is rare in practice — only single-sector-focused CCs qualify;
  multi-component hybrids do not.

`Subtotal = min(10, Σ) | +PPA priority (range, see bonuses) | +Frontier Zone (range, see bonuses)`
Floor: AE + bonuses < 3.0 → eliminatory (subnational only).

### Bonus treatment (Art. 15 §3º / §4º) — modeled as a range
Bonuses are uncertain until confirmed by COFIEX/SEAID. Model each as a discrete distribution
**[0 — 0.5 — 2.0]** with expected weight **0.5** in the probabilistic estimate. Apply the
**full value only when a documentary framing is attached** (ofício/Portaria evidencing the
frame, e.g. Lei 6.634/1979 for frontier zone). Without the document, carry the bonus in the
optimistic scenario only, not the base estimate. Both bonuses remain jointly capped inside AE=10.

**Frontier-Zone bonus — "strong-presumed" criteria** (include in the base estimate, not the
optimistic scenario, only when ALL hold): (1) a named cross-border conurbation with specific
neighbouring-country cities; (2) a dedicated, quantified cross-border-flow indicator;
(3) explicit reference to Lei 6.634/1979. Anchor: border municipality meeting all three → +1.0
(AE ~8.5 vs. ~7.5 without).

**Empirical AE ranges (Res. 1/2024, scale 0–10) — anonymized anchors:**
| Range | Quality | Typical profile | Anchor (anonymized) |
|---|---|---|---|
| 8.0–10.0 | Excellent | Investment, 5–7 areas, profile B/A, + frontier bonus; OR fund/intermediation with ~10 well-structured OEs (~9.0); OR justice/modernization with innovative SMART outcome indicators (~8.0) | Border municipality, 6 areas, profile C/B + frontier bonus → 8.5 |
| 6.0–7.9 | Good | Investment, 4–6 areas, profile B | Capital municipality, 4 areas, profile B → 6.5 |
| 3.0–5.9 | Moderate/Weak | DPL/restructuring, or genuinely-deferred on-lending, or low resource-proportionality | Fiscal DPL, 6 objectives, full prior actions → 3.5 |
| < 3.0 | Eliminatory | AE insufficient (Art. 28, I, b) | — |

**Regression-to-median guard:**
scoring blind runs **~0.6 pts hot on average**, and large multi-component PPP/metro/hospital-
concession-style operations carry the worst of it (+4.5 to +5.0 pts vs. the NT's own stated score
— not just "high variance," a *directional, source-verified overestimate*). Absent a specific,
named driver in the text (CAPAG A/A+, strong/decreasing debt trajectory, explicit PPA-priority
documentary framing such as an ofício/Portaria), the default point estimate for a well-prepared
multi-sector subnational investment operation should sit in the empirical median band — AE
6.0–7.5 (TOTAL 8.5–11.0/15) — not at the top of the "Excellent" tier, and even within that band
lean toward the lower half rather than the midpoint. Treat estimates above this band as requiring
an explicit one-line justification in the rationale, not as the default for large or visually
impressive ops.

**Typology rule.** Do NOT apply an automatic AE discount based on the
"fund/intermediation" label. Apply the on-lending discount (3.3–5.5) only when indicators are
genuinely deferred (baseline/target undefined). When a fund/intermediation op presents fully
specified, SMART, baselined OEs, score on indicator merit (can reach ~9.0). When a social/program
op shows institutional-preparation maturity (approved law + named evaluation partner + measured
baselines + prototype), apply the institutional-preparation uplift into the A/B band.

** STRUCTURAL DISCOUNT — DPL / Debt Restructuring :**
SEAID applies a severe structural AE discount to DPL/restructuring. Cause: the proportionality
criterion "resources to the objective / total ticket" (Art. 15 §1º, II) is minimal when ~100% of
the ticket funds debt amortization and the reform components have USD 0 financing.
- **Expected AE range: 3.0–5.5**, regardless of declared objectives or prior-action quality.
- Already-implemented prior actions do **not** raise AE above this band (proportionality, not
  policy maturity, is assessed).
- **PPA-priority bonus (§3º) does NOT apply** to restructuring DPL: "resources fully directed"
  to the priority is not satisfied when 100% of the ticket liquidates a liability.
- **Frontier bonus (§4º) may apply** for a border entity, but its impact is marginal given the
  low AE base.
- This discount is modality-specific (DPL/restructuring) and is NOT generalized to funds.

**OE 306 (fiscal) in a hybrid operation:** when the CC integrates fiscal refinancing with real
investment components (not pure DPL), OE 306 does not dilute the others — evaluate it as a valid
complementary AE if the ToC "refinancing → fiscal space → enables investments" is demonstrated
coherently.

**Environmental / bioeconomia (state) — conservative tier.** Treat the recognition of level A
with caution. Default to **B (3.0)** for a purely environmental/bioeconomy state operation
absent engineering works or explicit documentary framing (ofício) confirming the level. Raise
above B only with that evidence.

### Sector-level AE summary (anonymized, n=205)
| Sector | AE range | Median | SMART | Key pattern |
|---|---|---|---|---|
| Infrastructure/PPP | 3.0–9.0 | ~6.5 | Strong (physical) for direct-execution; weak for deferred on-lending | Low contamination; modality-driven hybrids. Strongest ToC exemplars (with-vs-without externality monetization). Multi-tranche megaprojects common. PBC road-asset (iRAP/8–10yr) scores well. GBV/GRM tied to ESF/CIF. |
| Environment/climate | 3.5–8.5 | ~6.5 | Good (utility/DPL/DLI); weak for cross-tagged; pure state bioeconomy capped at B absent works/ofício | Strongest ISO/ODS adoption. DLI/PBR dominant for development-bank climate finance. Dual fiscal+environmental DPL richer than fiscal-only. Concession-guarantee modality. Disaster clusters. |
| Health | 3.5–8.0 (core) | ~6.0 | Bifurcated: epidemiological (CID-10) 4–5/5; hospital/PPP 1.5–2.5/5 | ~62% file contamination (Progestão/social protection). Wait-time-by-procedure strong. Hospital/PPP defers indicators to annexes. |
| Water/sanitation | 3.0–8.0 | ~6.5 | Good for utility-led (SNIS); worst for pure on-lending | SNIS physical indices SMART by design. DLI/SDL via utilities. Key gap: OPEX/tariff sustainability. |
| Fiscal | 3.0–7.5 | ~6.5 (PROFISCO core) | Bifurcated: state PROFISCO 3.5–4.5/5; federal PBL/DPL 1.5–2/5 | Fiscal-climate hybrid + gender-leadership indicators emerging. PBL/DPL thin indicators by design. Restructuring exempt from CP/PPA gates. |
| Rural | 3.5–8.0 | ~6.0 | Bifurcated by delivery model | Deferred on-lending lowest. Phase-II projects strongest (named M&E, P/R tagging, non-zero baselines). Inclusion indicators near-universal. |
| Education | 4.0–7.5 (core) | ~6.0 | Moderate-good core; weak when cross-tagged | ~50% file contamination. IDEB/SAEB with race/SES-disaggregated baselines strongest. |
| Justice/modernization | 6.0–8.0 | 6.5 | Moderate (CNJ proxy); upper band with innovative SMART outcome indicators | CNJ Meta tier B when binding, C when illustrative. Tribunal×UGP governance unresolved. Innovative outcome indicators (e.g. asset recovery) anchor ~8.0. Low ticket. |
| Digital govt (state-direct) | 6.5–8.0 | 7.0 | Bifurcated B vs D-E | Sustainability gap universal (0 quantify OPEX). Gender indicators emerging. Deferred on-lending inherits intermediation problems. |
| Digital connectivity | 5.5–8.5 | 7.5 | Strong when physical | Social-inclusion indicators strongest; intermediation weakens causality. O&M gap universal. |
| Smart city (municipal) | 8.0–9.0 | 8.5 | Strongest (ISO) | ISO 37120/22 SMART by design. |
| Social programs | 4.0–8.5 | varies | Strong when prepared (law + evaluation partner + baselines) | Institutional-preparation uplift applies; prototype + measured baselines anchor A/B. |
| Fund / financial intermediation | 3.3–9.0 | bimodal | Weak when deferred; strong when OEs fully specified | No automatic typology discount (v15). Score on actual indicator quality; ~10 well-structured OEs → ~9.0. |
| Energy/mobility | n/a | n/a | Moderate | Municipal focus; KfW frequent. |
| Security/public safety | n/a | n/a | Moderate | Thin sample. |

## PHASE 6 — IDH (Subnational only)
`IDH Score = 2 × ((1 − IDH_entity) / (1 − IDH_lowest_in_meeting))`

**CRITICAL:** Score is RELATIVE to meeting composition — cannot be computed without knowing who
else is pautado. Always present as a scenario range. The fixed-floor convenience anchor below is
a DEFAULT for state-heavy meetings only; it never replaces the relative formula when pauta
composition is known, and it never overrides the municipal floors.

### Default state-meeting anchor
For state-heavy meetings with unknown composition, use floor **0.668** as the base, with:
- Pessimistic 0.650 · Base 0.668 · Optimistic 0.686 (high-end 0.700 for pautas dominated by
  South/Southeast or coastal-NE high-HDI states).
Override only with evidence of actual pauta composition (flagged).

### Calibrated scenarios (corpus 180th–187th)
| Scenario | IDH_lowest | Use when |
|---|---|---|
| Pessimistic | 0.646–0.650 | Meeting has N/NE state with very low HDI |
| Moderate (default state) | 0.668 | Default for state-heavy meetings |
| Optimistic | 0.686–0.700 | No state below the high-HDI floor |
| Municipal | 0.572–0.620 | Meeting includes low-IDHM municipalities (floors preserved) |

**Empirical ranges — states:** low-HDI (0.639–0.689) → 1.7–2.0; mid-HDI (0.660–0.665) → 1.3–1.9;
high-HDI (0.740–0.826) → 0.5–1.2. Anchor: a NE state with IDH ≈ 0.689 that is virtually the
meeting floor (IDH_lowest ≈ 0.686) → ≈ 1.98.

**Empirical ranges — municipalities (IDHM) — floors preserved, NOT subject to the 0.668 state anchor:**
- ≤ 0.600 (very low) → 1.8–2.0 (near-max if lowest in meeting)
- 0.650–0.699 (low) → 1.5–1.8
- 0.700–0.710 (medium-low) → 1.4–1.7 (floor ~0.619–0.646); up to ~1.98 if the lowest
- 0.750–0.770 (medium) → 1.2–1.4 (floor ~0.580–0.620)
- 0.760–0.799 (medium-high) → 0.9–1.4
- ≥ 0.800 (high) → 0.4–0.9
Anchors (anonymized): municipality IDHM 0.759, meeting floor ≈ 0.619 → **1.335**; municipality
IDHM 0.700, similar floor → **1.695**.

**Practical estimate:** when the meeting composition is unknown, use the 0.668 state anchor for
state pautas; for municipal or mixed pautas use floor 0.620–0.650; adjust up (→1.9+) if the entity
is demonstrably the lowest IDH on the agenda, down (→0.5–1.2) if lower-IDH entities are present.

Federal entities: IDH = N/A (score 0).

## PHASE 7 — CAPAG (Art. 20, Annex III — max 2.000)
Art. 10, I, c: max 2 points. CAPAG measures the entity's fiscal solidity and debt-service
capacity (Portaria MF 501/2017: indebtedness, current savings, liquidity) — NOT the proposed
operation's terms.

**Locked rating→points table (no ad-hoc overwrite; user values require metadata per PHASE 1.6):**
| Rating | Score | Status |
|---|---|---|
| A+ | 2.000 | Approved — maximum |
| A | 1.500 | Approved |
| B+ | 1.000 | Approved |
| B | 0.500 | Approved (minimum passing) |
| C | 0.000 | Non-competitive — not eliminatory |
| D | ELIMINATORY | Art. 28, I, c |
| Unclassified | 0.000 | Not eliminatory |

Non-dep statals: A+ (GAF>1 + ROI>cost) | A (GAF≤1 + ROI>cost) | B+ (GAF>1 + ROI≤cost) | B (GAF≤1 + ROI≤cost).
IFs: A+ (>15% Basel) | A (13–15%) | B+ (12–13%) | B (10.5–12%).

**Portaria 857/2026:** CAPAG recalculated with Adjustment Factor 0.78 — a borderline-B entity may
have deteriorated; verify current rating and consultation date (PHASE 1.6).

## PHASE 8 — Debt Trajectory (Art. 21, Annex III — max 1.000)
Art. 10, I, d: max 1 point. **Measures the entity's ACCUMULATED debt level/trajectory**
(DC/RCL, trend, Senate limits), analyzed by STN — NOT the proposed operation's financial terms.
**The proposed operation does not buy points here:** neither a promise of future improvement nor
the institutionalization of fiscal regimes (EC, LC) changes the score — STN assesses the stock at
analysis time.

| Trend | Score |
|---|---|
| Decreasing or stable within Senate limits | 1.000 |
| Increasing but within limits | 0.750 |
| Approaching prudential limit | 0.500 |
| Exceeding prudential limit | 0.250 |
| Significantly exceeding | 0.000 |

**DC/RCL → score reference (empirically calibrated):**
| DC/RCL | Trend | Expected score |
|---|---|---|
| < 40% | any | 0.875–1.000 |
| 40–55% | stable/decreasing | 0.750 |
| 40–55% | increasing | 0.500–0.750 |
| 55–65% | strongly increasing | 0.250–0.500 |
| > 65% or Senate-limit breach | any | 0.000–0.250 |

**Conditional floor (v15 anchor):** first MDB operation AND CAPAG C → expected **0.50** (was 0.75).
SEAID tends to apply a conservative floor when there is no MDB track record and weaker CAPAG.

**Refinancing vs. net new debt (critical distinction):**
1. **Refinancing without stock increase** (new creditor, same liability): DC/RCL does not rise →
   score reflects the pre-existing historical level (anchor: first MDB op, low DC/RCL → 0.750).
2. **Restructuring DPL (e.g. CDI → external)**: does not reduce the stock, only changes its
   composition. STN scores the historical trajectory, ignoring the forward effect (anchor:
   DC/RCL ~62.7%, rising since 2017 → 0.250).

Statals Exig/PL: Δ1→0.5 = 1→0.7 | IFs: A+/A→1.0, B+/B→0.5.

## PHASE 9 — Final Score
`Total = min(10, AE + bonuses) + IDH + CAPAG + Debt` (subnational, max 15). Federal = AE only.
Present as **[Min — Expected — Max]**.

**Practical cap = 15.0.** Hold the total cap at 15.0 by default. Bonuses are absorbed inside the
AE=10 ceiling. If documentary evidence of bonus stacking would imply a value above 15, flag it as
**cap_extensível** with LOW probability, pending explicit COFIEX/SEAID confirmation — do not score
above 15 by default.

**Anchor pattern (anonymized blind tests, NR 1/2024):** AE is the highest-variance component
(≈3.5–9.0); IDH benefits N/NE entities up to +2.0; CAPAG discriminates A+ (2.0) vs B+ (1.0);
Debt varies with historical DC/RCL. Confirmed total examples (anonymized profiles): capital-
municipality investment ≈ 10.6; border-municipality investment+refinancing ≈ 11.9; state fiscal
DPL/restructuring ≈ 6.7 — **all approved** (the last confirming score-independent approval for
the restructuring modality).

** Debt Restructuring/DPL — approval independent of score.** The score is irrelevant to the
outcome; what determines approval is: (1) documented financial advantage (mandatory comparative
annexes); (2) approved CAPAG (A+/A/B+/B); (3) original debt already guaranteed by the Union
(guarantee subrogation). With all three present, approval ≈ 100% regardless of AE.

**Modifiers (investment projects):**
- ticket > 0.15 × cap → ×0.7; ticket > 0.25 × cap → ×0.3
- Q1 post-rollover → General P = max(5%, base × 0.1)
- IBRD in General → ×0.9 (ticket-size pattern)
- 2nd submission targeting Q4 → ×1.15 (cap 95%); 3rd+ submission → ×0.6
- Ticket compressed >50% between submissions → ×1.2
- Same CC text resubmitted → score unchanged; P depends entirely on cap residual + competitors.
- Bonus applied at expected weight 0.5 unless documentary framing attached (then full value).

**Caveats:** order-of-magnitude estimates (5 NR 1/2024 meetings, n≈140 + iteration analysis over
15 meetings + formal blind-holdout validation n=52+22, v16.0). The dominant uncertainty is the cap
residual at the meeting date, not the score — **empirically confirmed**: in the v16.0 blind-holdout
run, mean predicted TOTAL was statistically indistinguishable between real-Approved and real-Not-
approved cases (9.70 vs 9.50/15), and the Art. 28 gate alone predicted PASS almost universally
regardless of real outcome. A high score is a necessary but never sufficient signal — always report
it alongside the sublimit-viability read, and never phrase ART28_GATE=PASS or a strong TOTAL as
"likely to be approved" without that qualifier.

## PHASE 9.5 — Iteration & Persistence Analysis
**Runs AFTER scoring.** Assesses resubmission strategy for cap-constrained operations.
1. **Is this a resubmission?** Ask: prior meeting(s)/outcome/score? CC text changed? Ticket changed?
2. **Score-stability rule:** identical CC text → identical score (empirically confirmed, n=9).
   Only sublimit residual, competitor landscape, and entity-level updates (CAPAG/debt) change
   between meetings.
3. **Persistence probability:**
| Attempt | Approval rate | Recommendation |
|---|---|---|
| 1st | varies by sublimit | Submit to least-congested sublimit |
| 2nd | ~60% | Strong odds, esp. at Q4 |
| 3rd | ~17% | Fundamental restructuring recommended |
| 4th+ | ~0% | Abandon or completely redesign |
   *Q4 modifier:* ~75% of "Not approved → Approved" trajectories under NR 1/2024 occurred at the
   Q4 meeting (highest approval rate ~81% due to rollover caps).
4. **Ticket compression:** compression alone is insufficient — it works when AE is already
   competitive (≥8.5) and the compressed ticket fits under residual cap. (Anchors: ~82% and ~72%
   compressions succeeded with high AE at Q4; 0% compression with moderate AE failed.) A scope
   revision accompanying compression *does* change the score (it is no longer the same CC text).
5. **Strategy recommendation:**
| Situation | Strategy |
|---|---|
| 1st, score ≥ 10 | Submit to Q4 for maximum cap residual |
| 1st, score < 8 in General | Consider PPP/Env-Climate/Fiscal sublimit if eligible |
| 2nd, same CC text | Target Q4; score unchanged, only cap residual matters |
| 2nd, revised CC | Quantify expected AE Δ; if < +1.0, compression is more impactful |
| 3rd+ | Fundamental redesign: scope reduction, creditor change, or sublimit migration |

## PHASE 10 — GTEC Simulation
Generate the calibrated GTEC questions with priority and applicability.

### P-High (always asked, high-impact)
- **Q1. Post-project sustainability** (digital/tech ops AND any high-maintenance component;
  Section V): R$/year table by category (licenses, hosting, maintenance, staff) × 5 years +
  future budget source. Corpus: ~0 answered satisfactorily — any answer differentiates.
  Absence → AE penalty 0.5–1.0.
- **Q2. Knowledge transfer vs. vendor lock-in** (tech procurement; Sections I, III): training
  clauses, in-house team target, code/data ownership, exit strategy. Impact 0.3–0.5 AE.
- **Q3. Cost per beneficiary vs. comparable LAC ops** (ALL; Section I): total cost ÷ beneficiaries
  + method + 2–3 creditor LAC benchmarks (USD/hab or USD/beneficiário). Acceptance 0.5×–2×
  benchmark. Impact 0.5–1.0 AE. Absence of comparative benchmark → request it.
- **Q9. Justice: judicial-independence vs. executive-UGP tension** (justice; Section III): joint
  governance body with defined competencies. Impact 0.5–1.0.
- **Q12. On-lending: subproject quality when undefined** (intermediation; Sections I, III):
  eligibility criteria, existing pipeline, ≥3 pilot subprojects with complete indicators.
  Impact 1.0–2.0 AE (highest for deferred on-lending).
- **Q14. Connectivity: post-project fiber O&M — who pays?** (Sections IV, V): annual O&M cost +
  contractual assignment + legal instrument. Impact 0.5–1.0.

### P-Medium
- **Q4. Cybersecurity & LGPD post-project** (digital/data; IV): data governance, LGPD officer, recurring security budget.
- **Q5. Inter-secretariat coordination** (multi-sector; III): formal body by decree, not "committee to be created".
- **Q6. Counterpart: legislatively secured or projected?** (ALL subnational; V): LOA + budget line + PPA + authorizing law, or a dated legislative schedule.
- **Q10. Justice: CNJ Metas binding or illustrative?** (justice; II): Meta 1/2 as KPI with tribunal-specific baseline and target.
- **Q13. On-lending: concentration in high-capacity municipalities?** (on-lending; II): indicator by IDHM/capacity bracket + quota mechanism.
- **Q15. Connectivity: backbone without last-mile?** (connectivity; II): connected households/schools/health-units indicator, not just km of fiber.
- **Q29. Wide indicator range** (ALL; I): any indicator with a wide target band (e.g. "1,000–10,000") must be converted to a point target with baseline. Impact 0.3–0.7 AE.

### P-Low (conditional)
- **Q7. Environmental licensing of physical components** (IV): status per component + responsible agency.
- **Q8. Digital inclusion of vulnerable populations** (II): disaggregate ≥1 indicator by gender/territory/income.
- **Q11. Justice: legacy-system migration / interoperability** (I): PJe/SEEU migration plan + inventory.

### P-Iteration (mandatory for resubmissions)
- **Q16. What concrete changes since last meeting?** (I): explicit list with justification.
- **Q17. Why did the amount change (or not)?** (V): justification + viability of the new amount.
- **Q18. Change of creditor or sublimit?** (I): comparative analysis of the advantage.

### P-Sectoral (modality/sector-specific)
- **Q19. PBL/DPL/guarantee fund: reduced indicator count structural or a gap?** Required: prior-action/policy-trigger matrix + benchmark vs. analogous creditor ops. If modality confirmed, neutralizes the indicator-count penalty.
- **Q20. On-lending pass-through: defined pipeline & eligibility criteria?** Required: eligibility criteria, pipeline (≥3 examples), selection mechanism. (Generalizes Q12 to rural/fiscal.) Note: a fund with fully specified OEs is not penalized under this question.
- **Q21. Debt restructuring: counterpart & PPA waivers correctly grounded?** Required: cite Art. 3, II, Res. COFIEX 03/2019 (counterpart) and the PPA-duplication elimination (e.g. Art. 7 §7 Res. Senado 43/2001); show debt service already in LOA/LDO.
- **Q22. Rating-based indicator (CAPAG) as a project target — methodological discontinuity risk?** Required: equivalence/recalculation clause for mid-execution methodology change + a complementary methodology-independent indicator.
- **Q23. Progestão/multi-sector op: is the cited social sector substantial or rhetorical?** If the cited sector is <10% of indicators/budget, declare the op as fiscal/public-management, not from that sector. Framing correction, not a penalty.
- **Q24. Guarantee on a third-party concession: do indicators measure concession performance, not direct delivery?** Required: concession-performance indicators with a multi-year verification schedule + declaration that the guarantee does not finance works.
- **Q25. Part of a climate-disaster cluster: explicit coordination with sibling operations?** Required: mention of other operations from the same event + coordination body or non-overlap justification.
- **Q26. Part of multi-tranche financing of one megaproject: cross-reference to the other tranches?** Required: declaration of tranche status, cross-reference to other CC(s), total physical-project value, integration schedule. Absence flagged (fragmented-assessment risk), not eliminatory.
- **Q27. ESF/CIF-financed civil works in a vulnerable area: GBV/GRM safeguard indicator present?** Required: GBV awareness/training + functioning GRM indicators with % target, linked to the financing vehicle (ESF or CIF). Absence = compliance gap with the vehicle's safeguard, not a general SMART failure.
- **Q28. Guarantee on recurring PPP counter-payments (Art. 25 IV): service-level indicators, not works delivery?** Required: cite the applicable PPP sublimit resolution; service-level indicators (uptime, MKBF, accessibility, wait time); contrapartida waiver (Art. 36, VI) where applicable.
- **Q30. Fund / financial intermediation: are OEs fully specified or deferred?** Required: confirm whether indicators have baselines/targets at CC stage. If fully specified, no typology discount applies; if deferred, treat as on-lending (Q12/Q20).
- **Q31. Social program: institutional-preparation evidence?** Required: enacted enabling law, named impact-evaluation partner, measured baselines, prototype/pilot. Presence supports A/B uplift.

### GTEC output format
| # | Question | Priority | Applies? | Answer in CC | Status | Gap / Action |
|---|---|---|---|---|---|---|
| 1 | Post-project sustainability | P-High | Yes/No | Section X, p. Y | ANSWERED/PARTIAL/ABSENT | Missing data + action |

Count: ANSWERED __ / APPLICABLE __. Shielding rate: __%.

## PHASE 11 — Senior MDB Review Simulation
Rate each item STRONG / ADEQUATE / WEAK / ABSENT.
- **A.1 Theory of Change** (problem → intervention → outputs → outcomes → impact). STRONG =
  explicit causal chain with evidence per link + testable assumptions; best exemplars use an
  explicit with-vs-without counterfactual monetizing externalities, or named M&E systems with
  P/R tagging + 3-stage evaluation. Corpus baseline: WEAK/ABSENT in ~64% of CCs.
- **A.2 Results Framework** (SMART). STRONG = ≥80% indicators 4–5/5 with baselines+verification;
  tier mapping A/B→STRONG, C→ADEQUATE, D→WEAK, E→ABSENT.
- **A.3 Risk Assessment.** STRONG = probability×impact matrix + mitigation/responsible/timeline,
  sector-specific risks covered. Verify: environmental licensing (infra), cybersecurity/LGPD
  (digital), judicial independence (justice), forex (BRL ops), subproject quality (on-lending),
  tariff/OPEX (water), multi-layer governance (health hospital × secretaria × OSS), indicator
  deferred to external annex (hospital/PPP).
- **A.4 Implementation Arrangements.** STRONG = UGP defined with institutional anchor, staffing,
  multilateral experience. WEAK = "arrangements to be defined during preparation".
- **A.5 Financial Sustainability.** STRONG = post-project O&M quantified, funding source identified,
  legislative backing. Corpus baseline: 0/14 of the original set rated STRONG — single highest-value
  improvement. Exemplar profiles: several quantified OPEX streams each with a named source; or
  counterpart earmarked to a named post-project program with PPA backing. Quantified-% only (no
  multi-year R$ table) = ADEQUATE. Water/sanitation needs tariff adequacy + regulatory covenant +
  OPEX projection for STRONG.

| Item | Rating | Evidence | Key Gap |
|---|---|---|---|
| A.1 Theory of Change | … | … | … |
| A.2 Results Framework | … | … | … |
| A.3 Risk Assessment | … | … | … |
| A.4 Implementation | … | … | … |
| A.5 Financial Sustainability | … | … | … |

Overall MDB readiness: READY / CONDITIONALLY READY / NOT READY.

## PHASE 12 — Correction Plan
Order by: (1) eliminatory risks, (2) highest AE impact per effort, (3) GTEC blind spots.
- **P0 — Eliminatory:** Art. 28 failures (missing sections, CAPAG D, sublimit breach), viability-gate
  failures, missing mandatory documentation, unresolved input_flag (PHASE 1.6).
- **P1 — High AE impact (0.5–1.5 AE each):** indicator upgrade D/E → B (baselines, SMART fields,
  verification); convert wide-range indicators to point targets; PPA alignment correction;
  financial-sustainability quantification (A.5 — universally absent, highest differentiation);
  ToC articulation (A.1); water-specific OPEX/tariff/regulatory.
- **P2 — GTEC blind spots:** unanswered P-High, partial P-Medium, sector-specific gaps.
- **P3 — Polish:** ISO/ODS for municipal ops, vulnerable-population disaggregation, LAC benchmarking,
  additional baselines (SNIS, CNJ, sector sources).

| # | Item | Phase | Priority | Current | Target | AE Δ | Action | Responsible | Deadline |
|---|---|---|---|---|---|---|---|---|---|
| 1 | … | PHASE X | P0/P1/P2/P3 | … | … | +X.X | … | Proponent/SEAID/Credor | … |

**Summary:** __ items. Estimated improvement if all P0+P1 addressed: +X.X to +Y.Y AE. New range: [Min — Expected — Max].

## OUTPUT FORMAT
1. **Header:** CC, proponent, creditor, ticket size
2. **Input Integrity (PHASE 1.6):** any input_flag raised
3. **Eliminatory Check (PHASE 2/4):** PASS/FAIL with details
4. **AE Score Breakdown (PHASE 5):** area-by-area with tier classification + bonus range
5. **Component Scores (PHASEs 6–8):** IDH, CAPAG, Debt with scenario ranges
6. **Final Score (PHASE 9):** [Min — Expected — Max]
7. **GTEC Simulation (PHASE 10):** question-by-question table
8. **MDB Review (PHASE 11):** A.1–A.5 ratings
9. **Correction Plan (PHASE 12):** prioritized table
10. **[LAST] Window & Timing (circumstantial):** sublimit viability, approval probability, iteration strategy

> ** COFIEX WINDOW FRAMING — CIRCUMSTANTIAL DATA**
>
> Per-meeting capacity, sublimit balance, and approval timing depend on dynamic variables that
> change every COFIEX cycle. Before judging timing/window viability, the operator MUST:
> 1. Consult the most recent COFIEX meeting minutes (gov.br/planejamento > COFIEX > Atas).
> 2. Verify the COFIEX communiqués and resolutions in force.
> 3. Check the PFE Portal for queue position and competitor status.
>
> The analysis above uses historical data through the 187th meeting as **structural reference only**.
