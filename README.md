# Inter-Union-Documentation

> **Four unions, one employer, four contracts that were never meant to be read together.**
> This vault makes them legible to each other — so a rank-and-file member of any craft can
> see, in one place, what we share and what still divides us. The goal is not just knowledge:
> it is the structural groundwork for going from **four unions to one**.

**Repository:** https://github.com/ContractNeedsRead/Inter-Union-Documentation

---

## What this vault is

A complete, verbatim archive of the four national agreements — NALC, APWU, NRLCA, NPMHU —
layered with the authorities that govern them (ELM, handbooks, arbitration awards, statutes),
the interpretive material each side has produced (JCAM, JCIM, CIM, Q&A compendia, the
Discipline Book, Step 4 settlements), and the working tools stewards actually use.

Every note obeys the same discipline:

- **Verbatim text** — every provision's full text is in the note, with printed-page markers and provenance frontmatter. Nothing is invented.
- **Typed links mean something** — `modifies`, `implements`, `clarifies`, `divergent`, `parallel` — the edge says what the relationship is, not just that one exists.
- **Hand-written comparison tables** — the topic hubs are written, not generated, because the differences are findings, not data.
- **Two documented exceptions only** — the NPMHU wage tables (raster images in the printed contract) and one source defect (§29.2B ends mid-sentence) are flagged, not guessed around.

## Get the vault onto your computer (no command line needed)

This is a folder of Markdown files plus a PDF library. You do not need Git, and the only
software you need to install is Obsidian. The steps below are written for Windows; Mac and
Linux are the same except for the extraction step.

**Step 1 — Download the repository**

1. Go to https://github.com/ContractNeedsRead/Inter-Union-Documentation
2. Click the green **Code** button.
3. Click **Download ZIP**.

The archive is roughly **1.4 GB** — it contains the full PDF library — so give it time.

If the download stalls or fails partway (GitHub sometimes times out on archives this large),
use **GitHub Desktop** instead: download it free from https://desktop.github.com, install it,
sign in with a free GitHub account (or skip sign-in if it lets you), then
**File → Clone repository → URL**, paste the repository URL above, and choose a local path
such as `C:\Vault`.

**Step 2 — Extract it**

1. Open your Downloads folder.
2. Right-click the `.zip` file → **Extract All…**
3. Choose a short, simple destination such as `C:\Vault`.

Do **not** double-click into the ZIP and open files from there. Obsidian needs real files on
disk, not files inside an archive.

> **Tip:** Windows' built-in extractor can fail on archives this large, or on deep folder
> paths. If it errors out, install **7-Zip** (free, https://7-zip.org), then right-click the
> ZIP → **7-Zip → Extract to "C:\Vault\"**.

When extraction finishes you should have one folder containing `README.md` and the numbered
areas (`00-09 Meta & system`, `10-19 Contracts`, `20-29 Cross-union topics`,
`30-39 External authorities`, `40-49 Organizing materials`, `Sources`).

**Step 3 — Install Obsidian**

1. Go to https://obsidian.md/download
2. Download the Windows installer and run it. No administrator rights are needed.
3. On first launch you can skip the account and pricing prompts — Obsidian is free for
   personal use and does not require an account.

**Step 4 — Open the vault**

1. On Obsidian's start screen, click **Open folder as vault**.
2. Navigate to the folder that directly contains `README.md` — for example
   `C:\Vault\Inter-Union-Documentation-main` — and click **Select Folder**.

Pick the folder that *contains* `README.md`, not the folder above it.

Obsidian may ask whether you trust the author and want to enable plugins. This vault ships
no plugins, so either choice is fine. Obsidian will create a hidden `.obsidian` folder for
your personal settings — that is normal and stays on your machine.

**Step 5 — Find your way around**

- You are reading the front door. Everything else is one click or one search away.
- **Ctrl+O** opens the quick switcher — type `21.03` or `Overtime` to jump straight to a note.
- **Ctrl+G** opens the graph view. That is the view shown in the time-lapse GIF.
- `[[Double-bracket links]]` in the text are clickable. Notes that do not exist yet are the
  gaps listed at the bottom of this file — they are honest placeholders, not broken links.

**Keeping it up to date**

Each drop is published as a single fresh snapshot rather than an incremental history, so
updating means downloading the new ZIP and replacing the folder. **Keep your own notes
outside the vault**, or back them up separately, so replacing a snapshot never costs you work.

**Troubleshooting**

| Problem | Fix |
|---|---|
| "Windows protected your PC" when running the Obsidian installer | Click **More info → Run anyway**. Standard for small independent installers. |
| ZIP extraction fails, hangs, or reports path-length errors | Use 7-Zip and extract to a short path like `C:\Vault`. |
| Obsidian opens and shows nothing | You selected an empty folder or a folder above the vault root. Re-open and choose the folder that directly contains `README.md`. |
| Graph view is sluggish at first | It is indexing ~3,800 files and 1.4 GB of PDFs. Give it a minute; it settles. |
| A link does not resolve | Note names must match exactly. Report mismatches as an issue on the repository. |
| Download ZIP fails | Use GitHub Desktop (Step 1) or retry at a quieter time of day. |

## Start here: the 19 topic hubs

The `20-29 Cross-union topics` area is the vault's answer to "what unites us, what divides us."
Every hub is a hand-written table comparing all four contracts on one subject, followed by the
legal layer and the primary sources.

| If you care about | Open |
|---|---|
| Overtime, penalty pay, the OTDL | [[21.03 Overtime]], [[21.05 Penalty Pay]] |
| Pay and COLAs | [[21.01 Compensation]] |
| Schedules and hours | [[22.01 Hours of Work]], [[22.02 Work Schedules & Limits]] |
| Leave and attendance | [[23.01 Leave]], [[23.02 Attendance]] |
| Discipline and due process | [[24.01 Discipline]], [[24.02 Due Process]] |
| Seniority, bidding, transfers | [[25.01 Seniority]], [[25.02 Posting & Bidding]], [[25.03 Reassignment & Transfer]] |
| Safety and health | [[26.01 Safety & Health]] |
| Union rights and representation | [[27.01 Union Rights]], [[27.02 Representation]] |
| Grievances and arbitration | [[28.01 Grievance Procedure]], [[28.02 Arbitration]] |
| Job security and subcontracting | [[29.01 Job Security & Layoffs]], [[29.02 Subcontracting]] |

Each hub's **Divergences** section is, in effect, the negotiation list for one contract:
the concrete differences a merged union would have to reconcile. The headline set, collected
in the [[Final Audit]]:

1. **Mail handlers have no penalty overtime** — a 1.5× ceiling where city carriers reach 2.5× ([[21.05 Penalty Pay]]).
2. **The rural craft's whole pay system is FLSA §7(b)(2)-shaped** — an evaluated annual guarantee instead of an OTDL ([[21.03 Overtime]]).
3. **Job security splits two ways** — the eight-section Healy framework for city carriers, clerks, and handlers, versus the rural contract's single sentence ([[29.01 Job Security & Layoffs]]).
4. **Discipline machinery diverges** — the rural day-of-reflection and one-year LOW; the APWU grievance-stalled suspensions; the three-way veterans'-preference election ([[24.01 Discipline]]).
5. **Arbitration costs differ** — loser-pays in the rural system, shared costs in the hourly crafts, plus the rural 30-day award deadline ([[28.02 Arbitration]]).
6. **Seniority and bidding mechanics** — bid budgets of 6/5/9/none and different tie-breakers ([[25.01 Seniority]]).
7. **Safety architecture** — three crafts have contract committees; the rural craft has none ([[26.01 Safety & Health]]).
8. **Union data rights** — the rural union's six named reports versus the hourly crafts' biweekly files ([[27.01 Union Rights]]).
9. **Subcontracting conversion rights** — only the rural contract has a CDS renewal-cost comparison ([[29.02 Subcontracting]]).

The commonalities are just as visible: the shared 40-hour week, the shared just-cause
discipline principle, the shared grievance-ladder concept, the shared ELM that governs
everyone — the material a single contract could ratify almost as-is.

## The documents, as ways to tackle things

| Document type | What it is | What it helps you tackle |
|---|---|---|
| **Contract section notes** (areas 11–14) | Every article and section, verbatim, with provenance | "What does my contract actually say?" — the ground truth for every argument |
| **MOUs and LOIs** ([[15.01 NALC MOUs]], [[15.02 APWU MOUs]], [[15.03 NRLCA MOUs]], [[15.04 NPMHU MOUs]]) | The 352 side agreements that modify the articles, each linked to the clause it changes | "The article says one thing, but there's a deal" — the most-missed material |
| **LMOU** (16) | Local agreements | Local variation on top of the national language |
| **Interpretive guides** (17) | JCAM/JCIM/CIM, the [[17.04 Northeast Q&A Compendium]], the [[17.05 Discipline Book (APWU, Revised 2023)]], [[17.06 Step 4 Settlements (APWU)]] | "How does the union read this?" — the agreed and contested meanings |
| **ELM** (31) | The manual that sets wages, hours, and working conditions across all crafts — including [[31.12 ELM 666.3 Whistleblower Protection]] | The common ground all four contracts adopt by reference |
| **Handbooks** (32) | MS-47, MS-63, EL-307, EL-809, EL-603, EL-804/814, MS-1, the [[32.15 Maintenance MMOs]] staffing catalog, the [[32.17 MMO Rubric Library — Index]], the [[32.24 Postal Bulletin Archive — Index]] | Staffing arithmetic, safety rules, EEO and injury processes |
| **Arbitration awards** (33) | National awards that settle what the words mean — [[33.03 Das 2020 Art 37.3.A.1]], Goldberg, Mittenthal, Bloch, and more | Precedent — the answers arbitrators have already given |
| **Statutes** (34) | FLSA, the [[34.02 Postal Reorganization Act Labor Framework]], FMLA, FECA, OSH Act, USERRA, and the rest | The legal floor beneath all four contracts — including the PRA §1207 machine that currently shapes bargaining |
| **Grievance notes** (41) | Worked sample grievances for maintenance staffing cases | "How do I actually write it?" |
| **Explainers** (42) | Steward tooling: [[42.01 Labor Checklist]], eMARS, WebEOR, the [[42.09 Challenge eWHEP Staffing Package]], the [[42.05 Maintenance Staffing Strategy and Grievance Guide]], [[42.06 Requests for Information]], the anonymized [[42.07 OSHA Complaint — Citation Map]] and [[42.08 Harassment, EEO & OWCP — Procedure Kit]], [[42.13 FMLA — Steward Guide]], [[42.18 Labor Law Fundamentals]], [[42.19 Workplace Harassment Training]], [[42.20 PSE Issues]] | "How do I run the case, end to end?" |
| **Campaign materials** (44) | Election letters, legal outlines, the APWU Constitution | "How do we run the union?" |

## The maintenance section (longer for now — that's on purpose)

The vault's deepest coverage is the **Maintenance Craft** — the steward who built this
project work there. The maintenance weave runs end to end:

- **The contract basis:** [[APWU Article 38 — Maintenance Craft]] — staffing, seniority, and posting rules for maintenance positions.
- **The staffing arithmetic:** the [[32.17 MMO Rubric Library — Index]] (177 official MMOs, one per machine) and the compiled [[32.15 Maintenance MMOs]] tables — the hours management is supposed to staff to.
- **The decoder:** [[42.11 Machine & MMO Labor Mapping Tables]] — machine name → acronym → MMO → staffing hours.
- **The challenge method:** [[42.09 Challenge eWHEP Staffing Package]] (the Balogun column) and the [[42.05 Maintenance Staffing Strategy and Grievance Guide]] — how to attack the staffing package, with the eWHEP program order at [[32.16 MMO-125-20 eWHEP Program]].
- **The evidence pipeline:** [[42.01 Labor Checklist]] → [[42.10 How to Collect WebEOR Data]] → the eMARS/WebEOR references in area 42.
- **The worked examples:** [[41.01]]–[[41.05]] — bypassing, staffing packages, posting, coverage, understaffing — each linked to the clause and the awards that back it.
- **The handbooks:** [[32.08 MS-47 Housekeeping]] and [[32.23 MS-1 Operation and Maintenance of Real Property (TL-6)]] (custodial staffing), [[32.13 MS-63 Maintenance Management]] (the eMARS framework), [[32.12 EL-307 Reasonable Accommodation]].
- **The safety side:** [[42.07 OSHA Complaint — Citation Map]] (incident → citation → quoted standard), [[31.12 ELM 666.3 Whistleblower Protection]], [[31.13 ELM 814.1 Safety Rights]].
- **The injury side:** [[42.08 Harassment, EEO & OWCP — Procedure Kit]] (the full claim checklist), [[32.20 EL-505 Injury Compensation]], [[34.13 FECA 5 USC 8102]], [[34.17 OWCP Regulations 20 CFR 10]].
- **The DOT/MVS side:** the Step 4 and Q&A corpus in [[17.06 Step 4 Settlements (APWU)]].

As stewards from the other crafts add their material, their sections will grow the same way.

## How the vault is organized

```
Vault/
├── README.md                  ← you are here
├── 00-09 Meta & system/       ← the design docs, taxonomy, build log, audits
├── 10-19 Contracts/
│   ├── 11 NALC / 12 APWU / 13 NRLCA / 14 NPMHU   ← every article, verbatim
│   ├── 15 MOUs & side letters/                    ← 352 MOUs/LOIs, linked to their articles
│   ├── 16 LMOU — local agreements/                ← local agreements
│   └── 17 Interpretive guides/                    ← JCAM/JCIM/CIM, Q&As, Discipline Book, Step 4s
├── 20-29 Cross-union topics/  ← the 19 hubs — the comparison layer
├── 30-39 External authorities/
│   ├── 31 ELM / 32 Handbooks / 33 Arbitration / 34 Statutes / 35 Courts / 36 Agencies
├── 40-49 Organizing materials/
│   ├── 41 Grievance notes / 42 Explainers / 44 Campaign materials
└── Sources/                   ← raw copies of everything provided, for browsing (not crosslinked)
```

Addresses are Johnny Decimal (`21.03` = the Overtime hub). Tags are controlled by the
[[00.02 Taxonomy]]; link types by the [[00.03 Relationship types]]; the rules of
transcription by [[00.08 Transcription conventions]]; the design decisions by
[[00.01 Conventions & Design]]. Every step of the build is logged in the [[00.06 Build Log]],
and the quality gates (provenance, verbatim markers, link resolution) are described in the
[[Final Audit]].

## Trust, but verify

- Every transcription note carries `source_file`, printed-page markers, and a `status`
  (`complete` / `partial` / `missing-source`). Two notes are `partial` for documented
  reasons; nothing is silently missing.
- Where a newer edition exists in the vault, older archive copies were never allowed to
  overwrite it (CBA 2024–2027, JCIM Nov 2025, newer EL-307/MS-47/MS-63).
- Image-only scans (two awards, four Step 4s, the NPMHU wage tables, the Richardson-Brooks
  Q&A) are flagged in-notes pending an OCR/visual pass — their holdings are never guessed.

## What's still missing — and how to help

- **M-39 and M-41** (delivery handbooks) — the last two handbook stubs; the PDFs are welcome.
- **Non-APWU local material** — LMOUs, steward guides, and workshop kits from NALC, NRLCA,
  and NPMHU would balance the vault the way the maintenance section is balanced now.
- **Case law and agency decisions** (areas 35–36) — seeded, waiting for sources.
- **Per-machine MMO transcription** — the rubric library is fully archived; machines get
  their own transcribed notes as grievances demand them.

The vault is a living instrument. Add to it the way it was built: source first, verbatim,
never invented, linked by meaning — toward one contract for four crafts.
