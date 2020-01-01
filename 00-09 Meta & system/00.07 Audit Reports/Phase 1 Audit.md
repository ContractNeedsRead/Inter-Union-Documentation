---
jd: "00.07"
type: audit
title: Phase 1 Audit
---

# 00.07 Phase 1 Audit — Overtime Vertical Slice

**Date:** 2026-10-26 · **Phase:** 1 · **Gate status:** awaiting user review
**Reader's guide:** this audit lets someone unfamiliar with the session judge whether the vertical slice proved the schema. It reports provision counts, divergence findings, spot-check results, the in-vault walk-through, and open items.

## 1. Provision count

| Layer | Notes | Status |
|---|---|---|
| NALC (11.08) | hub + §8.1, §8.4, §8.5 | complete |
| APWU (12.08) | hub + §8.1, §8.4, §8.5 | complete |
| NRLCA (13.08, 13.09) | 2 hubs + §8.1, §8.3, §8.5, §9.2.A.1 | complete |
| NPMHU (14.08) | hub + §8.1, §8.4, §8.5 | complete |
| ELM (31) | §432.3, §434.1, §434.141 (+exhibits a–c), §443/§443.1 | complete |
| Guides (17) | JCAM 8.4–8.5 (commentary), JCIM 31 overtime Q&As, CIM 8.4–8.5 Q&As | complete |
| Arbitration (33) | 33.01 Das 2013, 33.02 Mittenthal 1987 | complete |
| Statutes (34) | 34.01 FLSA §207(a)(1)/(b)(2), 34.02 PRA §§101(a)/1206/1207 | complete |
| Hub | [[21.03 Overtime]] with hand-written comparison table | complete |

**33 notes total; 33/33 pass the mechanical quality gates** (`tools/phase1_verify.py`), and **349/349 wikilinks resolve** (`tools/link_check.py`; Phase-2 stub targets whitelisted).

## 2. Verification performed

- **Mechanical gates:** frontmatter completeness (type/status/transcribed/source_checked/source_file/topics/provision_type), `source_file` resolution, tags ⊆ taxonomy, no body-prose provenance ("see the original"/"available at [URL]"/http links in body), page/section/sheet markers present, `status: complete` implies `## Full text`. 33/33 pass.
- **Link resolution:** every wikilink target in the slice resolves to a filename or alias; 0 unresolved.
- **Transcription spot-checks (≥10 passages per note, vs fresh extraction):** NALC 10/10 per note (nalc-scribe); APWU 10/10 per note (apwu-scribe); NRLCA 10–21/10–21 with one false negative adjudicated (rural-scribe); NPMHU/CIM/ELM 10/10 per note (mh-scribe). Award PDFs were re-OCR'd independently (rapidocr) and reconciled against the embedded layer and poppler.
- **Cross-engine extraction discipline:** poppler primary for all clean files; PyMuPDF coordinate-ordered for NPMHU; every engine gap flagged (NALC §8.4.E–G was invisible to PyMuPDF — caught and recovered).
- **Counterpart edges:** every edge was written only after both ends were read (the lead read all four contracts' Article 8 text plus the ELM exhibits before writing any edge). **Unverified counterparts: none.**

## 3. Divergence findings (the slice's substance)

1. **NPMHU has no penalty overtime** — 1.5× is the ceiling for mail handlers; NALC/APWU carry 2× (ELM Exhibit 434.141c confirms Mail Handlers: No).
2. **NALC-only 2.5×** beyond 12/60 (§8.4.G) and NALC-only **Work Assignment list** (§8.5.A).
3. **Distribution philosophy differs:** NALC equitable distribution with weekly posting; APWU/NPMHU seniority rotation; NRLCA twice-yearly relief-day list.
4. **NRLCA is a different species:** FLSA §7(b)(2) annual guarantee (2,080/2,240), no OTDL — overtime as a rate, not a queue.
5. **No universal 60-hour ceiling:** NALC/APWU 12/60; NPMHU 12/day only; NRLCA none.
6. **Non-OTDL shields differ:** 4-of-5/10/8/6 (NALC/APWU) vs 10/6 only (NPMHU); NALC alone adds 11.5/60 + no-discipline-for-leaving.
7. **ELM papers over the NPMHU carve-out** if read without Exhibit 434.141c — recorded as `diverges` edges with one-line notes.
8. **December means different things** in each book (penalty exclusion, limits exclusion, Christmas-OT accounting).

## 4. The walk-through (a steward's path, entirely in-vault)

1. Open [[21.03 Overtime]] → comparison table, row "Penalty overtime" → NPMHU cell links [[8.4 Overtime Work]] → `## Full text` shows §8.4 verbatim with `<!-- p.18 -->` markers.
2. From there, `## Related` → [[31.02 ELM 434.1 Overtime]] → frontmatter `interprets:` carries the `diverges` edge back to NPMHU §8.4 with the one-line note; `## Full text` shows §434.133 verbatim.
3. → [[31.03 ELM 434.141 Eligibility and Exhibit]] → Exhibit 434.141c table (Mail Handlers: No) with source footnotes.
4. Back up to the hub → "Legal layer" → [[33.01 Das 2013 — OTDL priority includes penalty overtime]] → `## Full text` is the complete award; its `interprets:` edge (clarifies) leads to [[APWU §8.5]], whose `counterparts:` lead to [[NALC §8.5]] and [[8.4 Overtime Work]].
5. → [[34.01 FLSA 207 Maximum Hours]] (`implements:` edges back to all four contracts) → [[34.02 Postal Reorganization Act Labor Framework]] (the §1207 arbitration machinery now governing the expired NPMHU agreement).
6. Every hop is a resolved in-vault wikilink; no reader ever leaves the vault or waits for a download. **The walk-through is clean — the schema works.**

## 5. Open items (not blockers)

1. **JCAM OCR flags + Das award reconstruction** await render confirmation by an image-capable reviewer (this model family has no image input). All flagged passages are marked inline per conventions.
2. **ELM §434.142–143, §443.2, §444** (rural compensation) referenced but not yet transcribed — Phase 3 candidates.
3. **Third arbitration award:** the APWU database has no further downloadable Article 8 overtime awards; two awards transcribed. User may supply more (G1).
4. **Effective dates:** hubs carry `effective: ""` where the agreement's effective date isn't printed in the supplied PDF — never invented; to be filled when verified.
5. **Schema amendment during the slice:** `status` added to all non-section leaf templates (quality gates require it on every note); JCAM/JCIM leaf notes renamed to unique filenames (`Art 8 Overtime — JCAM/JCIM`) to avoid duplicate-basename wikilink ambiguity; hub aliases extended. All logged in [[00.06 Build Log]].

## 6. Gate checklist

- [x] 21.03 Overtime hub with hand-written comparison table
- [x] All four contracts' overtime provisions transcribed at section granularity
- [x] ELM sections transcribed with restates/diverges edges and one-line divergence notes
- [x] Two arbitration awards + FLSA + PRA transcribed with correct edge types
- [x] Every counterpart edge read at both ends; 0 unverified
- [x] Every source_file resolves; source_pages plausible (printed-page maps verified)
- [x] ≥10 spot-checks per note (scribes' reports; summarized in §2)
- [x] Walk-through contract → ELM → arbitration → statute → back, fully in-vault
- [x] 33/33 mechanical quality gates; 349/349 links resolve
- [ ] **User review** — schema proven; Phase 2 (full contract ingestion) ready to start on approval

**Verdict:** the slice is done and the schema is proven. Phase 2 — batch ingestion of all remaining articles of all four contracts — can begin.
