# S21 Ingest Evidence - Project Scope and Research Hypotheses

Source: `raw/S21_project_scope_note.md`.

Access boundary: S21 is a shareable, medium-quality project note dated 2026-07-06 and marked as an AI-assisted draft requiring student review before being treated as a personal project statement [S21].

Checked source facts:

- Title: "Project Scope and Research Hypotheses" [S21].
- Research object: reliable knowledge and tool use for enterprise AI agents [S21].
- Reliability scope: traceable knowledge, explicit permissions, correct tool selection, verifiable state changes, and appropriate human oversight [S21].
- Four stack layers: MCP as tools/context exchange boundary; multi-agent systems as task decomposition and verification topology; RAG as query-time retrieval from raw evidence; LLM Wiki as pre-compilation of multi-source knowledge into a maintainable persistent structure [S21].
- MCP boundary: interoperability value but no automatic guarantee of business correctness, correct tool choice, authorization, truthful tool output, or whether a write action should execute [S21].
- RAG boundary: strong for high-risk facts, current information, and direct citations, with risks from retrieval misses, fragmented evidence, and repeated query-time synthesis [S21].
- LLM Wiki boundary: accumulated synthesis can preserve conflicts, relations, questions, and maintenance history, but ingest errors can harden and summaries can drift [S21].
- Multi-agent boundary: multi-agent systems do not automatically increase reliability and can amplify correlated errors if agents share model, context, and false assumptions [S21].
- Evidence workflow: project evidence should come from reproducible files, logs, and artifacts including `source_manifest.md`, `wiki/`, `schema/`, `logs/`, and `evidence/` [S21].
- Six research questions cover LLM Wiki as research memory, RAG plus LLM Wiki dual-channel architecture, MCP boundaries, multi-agent reliability conditions, lab-grade second-brain records, and pressure points such as conflict merging, entity confusion, numerical drift, low-quality source contamination, and over-synthesis [S21].

Evidentiary boundary:

- S21 is project framing and hypothesis material, not empirical validation or a formal specification [S21].
- S21 should be reviewed by the student before being treated as a personal project statement [S21].
