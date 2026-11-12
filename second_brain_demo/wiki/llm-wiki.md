---
title: LLM Wiki
page_type: concept
status: draft
updated: 2026-07-11
sources: [S01, S10, S18, S19, S20, S21, S24]
confidence: mixed
---

# LLM Wiki

## Core Definition

An LLM Wiki is a persistent Markdown knowledge-base pattern in which an LLM helps maintain derived wiki pages from raw source materials under a schema or maintenance contract [S10].

S10 is the original concept source for the LLM Wiki pattern used in this project and says the pattern motivates the idea that an LLM can maintain a persistent Markdown knowledge base [S10].

S18 adds a public Obsidian second-brain repository as an implementation-reference comparison point for file organization, commands, maintenance, and search, but it should not be copied blindly because it is shaped by its author's workflow [S18].

S19 adds a public `llmwiki` repository capture for comparing document ingestion, generated Markdown pages, and MCP-style connection patterns in LLM Wiki workflows [S19].

S20 adds a low-quality critique/opinion capture that frames LLM Wiki as a possible complement to RAG rather than a replacement; this source should be used only as a low-confidence critique and not as independent support for key LLM Wiki conclusions [S20].

S21 treats LLM Wiki as the compiled-knowledge channel in the project stack, where ingest converts sources into persistent, linked Markdown pages rather than retrieving raw chunks at every query [S21].

S24 is a synthetic screenshot source that visibly shows this project folder containing `.obsidian`, `evidence`, `logs`, `raw`, `schema`, and `wiki` folders, but it does not prove folder contents, completeness, or workflow correctness beyond what is visible in the screenshot [S24].

## Key Claims

- S10 defines a project structure that distinguishes raw sources, generated wiki pages, and schema files [S10].
- S10 identifies ingest, query, and lint workflows as part of the LLM Wiki pattern [S10].
- S10 is used in this project as the baseline for the LLM Wiki architecture [S10].
- S10 supports the claim that a medium-sized source set can be maintained through an index-like wiki structure [S10].
- S10 is a public source capture of Andrej Karpathy's `LLM Wiki`, dated 2026-04-04 in the capture and manifest [S10].
- S18 is a public open-source repository capture for `obsidian-second-brain`, active in 2026, and is useful for implementation comparison rather than reliability evidence [S18].
- S19 is a public open-source repository capture for `llmwiki` by Lucas Astorian, active in 2026, and is useful for comparing source ingestion, wiki generation, and MCP-style connection patterns [S19].
- S20 is a low-quality critique/opinion capture from Artificial Ideas, dated 2026 in the manifest, and is useful for stress-testing overconfident claims about LLM Wiki replacing RAG [S20].
- S21 says LLM Wiki's strength is accumulated synthesis but its risks include hardened ingest errors, summary drift, and over-trust in derived pages [S21].
- S24 visibly supports that this local project has the expected top-level audit and wiki folders `evidence`, `logs`, `raw`, `schema`, and `wiki`, plus an `.obsidian` folder [S24].

## Evidence and Sources

The captured S10 source states that it is included because it is the original concept source for the LLM Wiki pattern used in this project [S10].

The captured S10 source says the LLM Wiki pattern defines the `raw`/`wiki`/`schema` structure and motivates maintaining a persistent Markdown knowledge base with an LLM [S10].

Synthesis: S10's LLM Wiki pattern is a knowledge-base maintenance workflow, while [[retrieval-augmented-generation|Retrieval-Augmented Generation]] in S01 is a model architecture that retrieves external passages during generation [S01] [S10].

Synthesis: [[second-brain-implementation-patterns|Second-Brain Implementation Patterns]] compare public second-brain repositories such as S18 against the schema-governed LLM Wiki architecture in S10, while preserving S18's evidentiary boundary as an implementation reference [S10] [S18].

Synthesis: S19 is closer to the LLM Wiki pattern than S18 because its capture is explicitly about LLM Wiki workflows, document ingestion, generated Markdown pages, and MCP-style connection patterns; however, both S18 and S19 remain implementation examples rather than reliability evidence [S18] [S19].

Synthesis: S20 should be treated as a challenge prompt for the design question of whether synthesis belongs at ingest time or query time, while S10 remains the concept source for LLM Wiki and S01 remains the primary source for RAG architecture [S01] [S10] [S20].

Synthesis: S21's dual-channel research question preserves both RAG and LLM Wiki: RAG keeps query-time raw evidence available, while LLM Wiki preserves compiled knowledge, conflicts, entity relations, research questions, and maintenance history [S01] [S10] [S21].

Synthesis: S24 provides a screenshot-level check that the project folder layout resembles the raw/wiki/schema/logs/evidence maintenance pattern described by S10 and S21, but the screenshot itself should remain lower-confidence evidence than source files or logs [S10] [S21] [S24].

## Limitations and Counter-Evidence

S10 should be treated as an original design proposal and concept source, not as a controlled empirical evaluation [S10].

S10's reliability claims should be tested through project stress tests rather than accepted as benchmark evidence [S10].

S10 is a medium-quality source capture in the manifest, so it can define project vocabulary and architecture but should not independently settle reliability, accuracy, or enterprise-readiness claims [S10].

S18 is also medium-quality and repository-shaped, so implementation ideas from it require local evaluation before being treated as best practices for this wiki [S18].

S19 is also medium-quality and repository-shaped, so public implementation features from it should be treated as comparison material until fuller repository extraction or local testing supports adoption [S19].

S20 is low quality and opinion-shaped, so it can record skepticism about LLM Wiki replacing RAG but must not independently support a key conclusion about retrieval, reliability, or enterprise suitability [S20].

S21 is project framing rather than empirical validation, so its LLM Wiki risk list should be tested through lint checks, stress tests, and evidence logs [S21].

S24 is a synthetic screenshot and only supports visible UI-level folder names; it should not be used to infer file contents, source counts, successful ingestion, or whether the repository is complete or reproducible [S24].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[second-brain-implementation-patterns|Second-Brain Implementation Patterns]]
- [[contradiction-register|Contradiction Register]]
- [[project-scope-and-research-hypotheses|Project Scope and Research Hypotheses]]

## Open Questions

- What lint checks best predict whether an LLM-maintained wiki remains faithful to raw sources over many ingests source-needed?
- When should an LLM Wiki use retrieval over raw sources instead of relying on derived wiki pages source-needed?
- How large can a medium-sized source set become before the index-like wiki structure needs additional hierarchy or automation source-needed?
