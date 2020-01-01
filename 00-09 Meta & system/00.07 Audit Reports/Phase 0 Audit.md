---
jd: "00.07"
type: audit
title: Phase 0 Audit
---

# 00.07 Phase 0 Audit — Scaffold and Schema

**Date:** 2026-10-26 · **Phase:** 0 · **Gate status:** awaiting user approval
**Reader's guide:** this audit lets someone unfamiliar with the session judge whether Phase 0 is done. It summarizes the schema, taxonomy, and conventions produced, states the deviations from the build prompt, and lists what must be decided at the gate.

## 1. What was produced

| Artifact | File | Contents |
|---|---|---|
| Area structure | `Vault/` folder tree | All ten areas (00–09 … 40–49), all categories, no notes beyond meta. |
| Source archive | `_sources/` (outside vault) | 9 top-level PDFs + ELM folder (14 chapter PDFs), exactly as supplied; vault is markdown-only. |
| JD index | [[00.00 JD Index]] | Area/category numbering, article-hub numbering rule, planned topic-hub map. |
| Design doc | [[00.01 Conventions & Design]] | The build prompt's non-negotiable principles + every Phase 0 decision. |
| Taxonomy | [[00.02 Taxonomy]] | 52 hierarchical `topic/…` tags, each with a one-line definition and parent. |
| Edge vocabulary | [[00.03 Relationship types]] | The three vocabularies verbatim, with direction conventions and required `note:` fields. |
| Templates | `00.04 Templates/` (14 files) | Article hub, section, subsection, topic hub, ELM, handbook, arbitration, statute, case, agency decision, MOU, interpretive guide, LMOU, missing-source stub. |
| Inventory | [[00.05 Workspace Inventory]] | Per-file assessment, coverage matrix, gap report G1–G10, first-slice scope. |
| Transcription rules | [[00.08 Transcription conventions]] | Fidelity, markers, OCR regime, tables, footnotes, amendments, non-prose translation. |
| Build log | [[00.06 Build Log]] | Session 1 entry with all decisions. |
| Archive index | [[00.09 Source archive index]] | `_sources/` → canonical IDs, ready for citing-note tracking. |

## 2. Schema summary (frozen pending approval)

- **Frontmatter property names are fixed.** Every transcribed note carries the provenance block: `source_file`, `source_url`, `source_pages`, `source_locator`, `source_checked`, `transcribed`, `transcription_notes`. No body-prose provenance; no `## Source` section.
- **Enums:** `type` (14 values), `status` (complete/partial/missing-source/superseded), `provision_type` (definition/rate/procedure/remedy/right/obligation/timeline), counterpart `relation` (analogous/parallel/divergent/supersedes/unverified; `same` prohibited).
- **Bodies:** section notes are `## Full text` → `## Summary` → `## Cross-union comparison` → `## References` → `## Related`. Hubs are `## Why this matters across crafts` → `## Provisions by contract` (Dataview) → `## Comparison table` (hand-written) → `## Legal layer` → `## Divergences worth noting` → `## Related topics` (+ optional `## Primary sources`).
- **JD discipline:** JD numbers on containers only; section/subsection notes are un-numbered leaves inside `<JD> Article <N> — <Title>` folders.

## 3. Scan-quality findings (drives the extraction strategy)

- **14 of 16 source units are born-digital with clean text.** No OCR needed (contracts other than NPMHU, JCIM, CIM, all ELM chapters, ASM, POM).
- **NPMHU 2022–2025 agreement:** text layer scrambled at the run level (not OCR-broken). Strategy: coordinate-ordered extraction with PyMuPDF + deduplication + render verification.
- **2025 JCAM:** Paper-Capture scan + OCR layer (17/457 pages image-only). Strategy: OCR regime — spot-check every transcribed passage against the rendered page.

## 4. Deviations from the build prompt (all deliberate, all documented)

1. Vault root is `Vault/` with `_sources/` as its sibling at workspace root (the prompt's relative-path example assumed different nesting; resolution rule simplified to "relative to vault root, `../_sources/…`").
2. Original source filenames kept — they encode term years the prompt's example names lose.
3. `16 LMOU — local agreements` (en dash) instead of the literal `/`, which Obsidian wikilinks would parse as a path separator.
4. Web-born/manual sources (ELM, ASM, POM) get **section markers**, not page markers; `source_pages` left empty for them.
5. Planned hub JD map proposed in the JD index (the prompt fixed only 21.03 and 21.05 by example).

## 5. Open questions for the gate (see [[00.05 Workspace Inventory]] §4/§6)

- **G1/G2 — the legal layer is empty.** No arbitration awards, no FLSA text, no cases in `_sources/`. Phase 1's legal layer (2–3 awards + FLSA §207) cannot be transcribed until the user supplies files or authorizes download-and-archive of the official public-domain FLSA text.
- **G10 — NPMHU 2022–2025 has lapsed** (term ended September 2025). Is there a newer edition?
- **G5 — no NRLCA interpretive guide.** Rural parity in every hub will be thinner until supplied.
- **Tooling:** approve installing PyMuPDF (Python) for NPMHU coordinate-ordered extraction?
- **JCAM regime:** spot-check-everything (slow, safe) vs. extraction + sample verification?

## 6. Gate checklist

- [x] Area structure matches the prompt (ten areas; LMOU folder name deviation documented)
- [x] `_sources/` created at workspace root; vault contains no binaries
- [x] 00.00–00.09 exist; templates cover every note type the prompt names
- [x] Taxonomy and relationship catalog proposed; no notes created against them yet
- [x] Workspace inventory covers every file with type, edition, format, pages, coverage
- [x] Coverage matrix complete for all four agreements
- [x] Gap report and first-slice scope present
- [x] All decisions logged in the build log
- [ ] **User approval** — do not mass-create notes before sign-off

**Verdict:** Phase 0 is complete except for the user's gate decisions above. No Phase 1 work should start before approval.
