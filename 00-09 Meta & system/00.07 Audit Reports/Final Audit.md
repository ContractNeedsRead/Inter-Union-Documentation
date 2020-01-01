---
jd: "00.07"
type: audit
title: Final Audit
---

# 00.07 Final Audit — Phases 1–5 Complete

**Date:** 2026-10-26 · **Audit scope:** the entire vault
**Reader's guide:** this is the Phase 5 final audit from the build prompt. It reports the mechanical gates, the graph checks, the deferred items, and the verdict against the Definition of Done.

## 1. Build inventory

| Layer | Count |
|---|---|
| Article hubs | 163 (NALC 43, APWU 43, NRLCA 38, NPMHU 39) |
| Contract section notes | ~667 (every section of every article, incl. no-section articles as single notes) |
| Topic hubs | 19 (21.01–29.02, every one with a hand-written comparison table) |
| ELM notes | 11 (31.01–31.11) |
| Handbook notes | 1 transcribed (ASM) + 10 missing-source stubs |
| Arbitration awards | 2 (full text) |
| Statute notes | 17 (34.01–34.17, official USCODE-2022 texts) |
| Meta/build/audit | 00.00–00.09 layer |
| **Vault total** | **914 markdown files** |
| Archive | 46 PDFs in `_sources/` (4 agreements, 3 guides, ELM 14 chapters, ASM, POM, 2 awards, 21 statute files) |

## 2. Mechanical gates — PASS

- **890/890 notes pass** `tools/phase1_verify.py`: frontmatter completeness, `source_file` resolution, tags ⊆ approved taxonomy, no body-prose provenance, markers present, `status: complete` ⇒ `## Full text`.
- **6,177/6,177 wikilinks resolve** (`tools/link_check.py`; Phase-4 stub-hub targets whitelisted as deferred).
- **903 counterpart edges; 0 asymmetric; 0 unverified; 0 prohibited `same` relations** (`tools/phase5_checks.py`).
- Transcription spot-checks: every note ≥10 verbatim passage checks vs fresh poppler/PyMuPDF extraction (thousands of checks across Phases 1–3; scribe reports logged in [[00.06 Build Log]]).
- Engine discipline: poppler primary for clean files; PyMuPDF coordinate-ordered for NPMHU; cross-engine audits caught PyMuPDF's silent text loss (NALC §8.4.E–G, ELM exhibits) before it entered the vault.

## 3. Definition of Done — verdict per clause

| Clause | Status |
|---|---|
| Every article is a hub with linked section notes | ✓ 163 hubs, complete section coverage |
| Every section note `status: complete` + provenance + in-vault full text | ✓ with **two documented exceptions**: NPMHU §9.1 (`partial` — wage tables are raster images; numbers deliberately not OCR-guessed, gap G11) and NPMHU §29.2 (`partial` — the printed source ends mid-sentence; source defect verified by OCR) |
| Every 20-29 hub has a hand-written comparison table + populated legal layer | ✓ 19/19 (23.02 Attendance honestly scoped: attendance control lives in ELM 510, core-transcribed, remainder flagged) |
| Authorities needed are present, transcribed, or `missing-source`-flagged | ✓ 17 statutes + 11 ELM + ASM transcribed; 10 handbook stubs; case law and agency decisions absent from `_sources/` (G3/G4 — no sources supplied) |
| Walkable chain from any contract section to law/arbitration in-vault | ✓ verified in the Phase 1 audit and strengthened by the citation-link conversion (every contract cite now wikilinks its authority) |
| No broken references / unresolved source_file / unverified counterparts / missing transcribed dates / orphan hubs | ✓ 6,177 links resolve; 890/890 source_files resolve; 0 unverified counterparts; all transcribed dates present; 0 orphan hubs |
| 00.09 shows every `_sources/` file cited | ✓ 33 of 46 cited by notes; **13 deferred with reasons** (POM + 12 ELM front-matter/chapter holdings for future phases — recorded in [[00.09 Source archive index]]) |

## 4. Divergence findings (the vault's substance — hub tables)

Every hub's comparison table states material differences; the headline set:

1. **NPMHU has no penalty overtime** (1.5× ceiling; ELM Exhibit 434.141c confirms) — [[21.05 Penalty Pay]]
2. **NALC-only 2.5× beyond 12/60 and Work Assignment list** — [[21.03 Overtime]]
3. **NRLCA's whole pay system is FLSA §7(b)(2)-shaped** (2,080/2,240 guarantee, no OTDL) — [[21.03 Overtime]], [[21.01 Compensation]]
4. **NPMHU's expired term pays 1.3% × 3** against 1.3/1.4/1.5 ladders elsewhere — the §1207 arbitration stakes — [[21.01 Compensation]]
5. **NRLCA has no safety committee and one-sentence no-layoff protection** — [[26.01 Safety & Health]], [[29.01 Job Security & Layoffs]]
6. **Discipline machinery splits:** NRLCA's day of reflection and 1-year LOW; APWU's grievance-stalled suspensions; the three-way veterans'-preference election — [[24.01 Discipline]]
7. **Arbitration costs split:** loser-pays (NRLCA) vs shared (hourly crafts); NRLCA's 30-day award deadline — [[28.02 Arbitration]]
8. **Union rights data duties:** NRLCA's six named reports vs biweekly files — [[27.01 Union Rights]]
9. **Bid budgets 6/5/9/none; rural mutual exchanges; NPMHU's paid transfer leave** — [[25.01 Seniority]]
10. **NRLCA's CDS renewal cost comparison is the only subcontracting conversion right** — [[29.02 Subcontracting]]

## 5. Deferred items (explicit, with reasons)

1. **NPMHU wage tables** (G11): raster; needs an image-capable reviewer or user-supplied table data.
2. **JCAM OCR flags + Das award reconstruction**: pending render confirmation by an image-capable reviewer (this model family has no image input; all flagged passages are marked inline per conventions).
3. **ELM 510 full subchapter** (attendance control) and ELM chapters 1/2/3/6/7: future phases; the cited cores are transcribed.
4. **POM** archived but uncited: Phase-3+ candidate.
5. **Handbooks** (M-39, M-41, EL-312, F-15, F-21, P-1, MS-47/MS-1, Publication 52, EL-304, SF 95): 10 missing-source stubs — sources not supplied.
6. **Case law (G3) and agency decisions (G4)**: no sources supplied; no stubs fabricated.
7. **MOUs/LOIs (area 15)**: back matter excluded by design from Phases 1–3; next ingestion project.
8. **NPMHU 29.2B**: source defect in the printed agreement; documented, not invented around.
9. **Effective dates** on hubs remain empty where the PDFs don't print them (never invented).

## 6. Verdict

The vault meets the Definition of Done within the supplied corpus, with every deviation explicitly deferred and reasoned. The measure from the build prompt — a mail handler, a clerk, a city carrier, and a rural carrier opening the same topic note and seeing what unites and divides them, with the source language one click away in the same note — is met: 19 hubs, 163 article hubs, 903 typed counterpart edges, 6,177 resolving links, zero invented text.

## 7. Addendum — Steward Library integration (2026-10-26, after final audit)

The user supplied a personal maintenance-craft steward library (`C:\Users\JR\Documents\A Tale of Blood and Stone\2 Union Steward Topics\`, 65 files, 2.64 MB). It was archived to `_sources/Steward Library/` (originals untouched) and woven in:

- **Handbooks resolved from stubs:** 32.08 MS-47 (byte-exact), 32.12 EL-307 (excerpt, partial), 32.13 MS-63, 32.14 MI AS-530-90-5, 32.15 Maintenance MMOs (26-MMO staffing catalog).
- **Regional interpretive material:** 17.04 Northeast Q&A Compendium (3,192 lines verbatim).
- **User's working materials:** 16.01 LMOU Brockton MA (full 22-item LMOU + agenda), 41.01–41.05 five maintenance sample grievances, 42.01–42.06 steward tooling (labor checklist, eMARS, WebEOR, training manual, staffing strategy, RFI), 44.01–44.07 election materials + APWU Constitution, 36.01 FLRA overview.
- **Statute gap filled:** 34.18 39 CFR §266.6 (official text; the user's archived note described §266.5 — discrepancy flagged).
- **Schema extension:** `grievance-note` and `explainer` types added (templates in 00.04) for areas 41–44; adapted born-digital notes carry `<!-- source: … -->` markers instead of page markers; URLs inside verbatim transcriptions are no longer flagged as body-prose provenance.
- **Verification after integration: 916/916 mechanical gates; 6,361 links, 0 unresolved** (14 source-internal verbatim links informational).

The maintenance weave is complete: APWU Article 38 ↔ MS-47/MS-63/MMOs ↔ the staffing grievance guide ↔ the five sample grievances form one walkable chain, and the user's steward tooling now sits beside the contract text it operates on.
