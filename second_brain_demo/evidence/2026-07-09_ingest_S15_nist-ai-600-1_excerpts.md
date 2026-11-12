# S15 Ingest Evidence - NIST AI 600-1

Source: `raw/S15.pdf` and `raw/S15_nist_ai_600_1.source.md`.

Access boundary: S15 is a public, high-quality official NIST report/PDF plus local source capture, accessed 2026-07-06 per the source capture and manifest [S15].

Checked PDF facts:

- PDF title metadata: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" [S15].
- PDF page count from `pdfplumber`: 64 pages [S15].
- Publication line in PDF: July 2024; approval line: approved by the NIST Editorial Review Board on 2024-07-25 [S15].
- Manifest date: 2024-07-26; DOI: `https://doi.org/10.6028/NIST.AI.600-1` [S15].
- Introduction says the document is a cross-sectoral profile of and companion resource for AI RMF 1.0 for Generative AI, pursuant to EO 14110 [S15].
- Introduction says AI RMF 1.0 was released in January 2023 and is intended for voluntary use [S15].
- The Generative AI Public Working Group focus was limited to four primary considerations: Governance, Content Provenance, Pre-deployment Testing, and Incident Disclosure [S15].
- Risk overview lists 12 GAI risks: CBRN Information or Capabilities; Confabulation; Dangerous, Violent, or Hateful Content; Data Privacy; Environmental Impacts; Harmful Bias or Homogenization; Human-AI Configuration; Information Integrity; Information Security; Intellectual Property; Obscene, Degrading, and/or Abusive Content; Value Chain and Component Integration [S15].
- Suggested-action tables use AI RMF function tags `GV`, `MP`, `MS`, and `MG` for Govern, Map, Measure, and Manage [S15].
- Suggested-action section states not every AI RMF subcategory is included and not every suggested action applies to every AI actor or AI actor task [S15].
- Checked examples include GV-1.5 incident monitoring and TEVV retention, GV-1.6 GAI inventory, GV-4.2 downstream third-party plugin impact documentation, GV-4.3 incident-reporting criteria, MS-1.1 provenance and unmeasured-risk tracking, MS-2.3 empirical capability validation, and MS-3.2 emergent-risk identification [S15].

Evidentiary boundary:

- S15 is governance guidance, not an agent implementation guide or benchmark; task-performance claims should continue to cite S04, S05, or S06 as appropriate [S04] [S05] [S06] [S15].
- S15 includes uncertainty and future-revision language; the page preserves this as a limitation rather than turning suggested actions into universal requirements [S15].
