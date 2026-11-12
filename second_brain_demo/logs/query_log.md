# Query Log

This log records substantive questions asked against the wiki and whether the answer should be written back.

## Q01 | RAG vs LLM Wiki

- Question: How does RAG differ from an LLM-maintained wiki?
- Sources/pages: S01 and LLM Wiki-related sources.
- Answer summary: RAG retrieves raw evidence at query time, while an LLM Wiki compiles knowledge into persistent, linked pages during ingest.
- Write-back decision: write back only if the answer becomes a reusable comparison page.

## Q02 | MCP Reliability

- Question: Does MCP by itself make enterprise agents reliable?
- Sources/pages: S11-S17.
- Answer summary: MCP improves interoperability, but reliability also needs authorization, least privilege, tool-output validation, provenance, evaluation, and human escalation.
- Write-back decision: suitable for a tool-boundary or enterprise-agent reliability page.

## Q03 | Multi-Agent Debate

- Question: Does multi-agent debate improve reliability?
- Sources/pages: S07-S09 and S23.
- Answer summary: Some sources report benefits, while later work questions whether agents truly debate or simply amplify correlated behavior.
- Write-back decision: should preserve both positive and skeptical evidence.

## Q04 | Insufficient Evidence and Outdated Claims

- Question: Which claims should be treated as uncertain or outdated?
- Sources/pages: S06, S09, S12-S14.
- Answer summary: insufficient-information tool tasks, debate limitations, and protocol-version updates should be represented as uncertainty or supersession rather than erased.

## Q05 | Tool-Calling Numbers

- Question: Which numerical claims require exact citation?
- Sources/pages: S04, S05, S10.
- Answer summary: benchmark counts, pass rates, dates, and scale claims require direct citation and should not be paraphrased loosely.

## Q06 | MCP Architecture vs Authorization

- Question: What is the difference between MCP architecture and MCP authorization?
- Pages read: `wiki/index.md`, `wiki/model-context-protocol-architecture.md`, `wiki/model-context-protocol-authorization.md`, `wiki/model-context-protocol-security-best-practices.md`, `raw/source_manifest.md`, `logs/query_log.md`.
- Source IDs: S11, S12, S13, S14, S19, S22.
- Answer summary: MCP architecture describes the protocol and integration structure for hosts, clients, servers, tools, resources, prompts, and capability negotiation; MCP authorization describes the access-control boundary for MCP deployments, with S12 as the stable authorization specification for OAuth 2.1, PKCE, audience binding, and token handling.
- Direct support vs synthesis: direct support comes from S11 for architecture vocabulary and S12 for authorization boundaries; synthesis distinguishes the architecture layer from production authorization and security controls using S11, S12, and S13.
- Write-back decision: no write-back; the existing architecture and authorization pages already contain the reusable comparison and links.
- Modified files: `logs/query_log.md`.
- Unresolved issues: detailed implementation checklists for OAuth 2.1 requirements, audience binding across multiple servers, and mandatory S13 security controls remain `source-needed`.
- Diff saved: No file diff produced.

## Q07 | Enterprise Agent Reliability Stack

- Question: How do MCP, RAG, LLM Wiki, and multi-agent systems form an enterprise agent reliability stack?
- Pages read: `wiki/index.md`, `wiki/project-scope-and-research-hypotheses.md`, `wiki/model-context-protocol-architecture.md`, `wiki/retrieval-augmented-generation.md`, `wiki/llm-wiki.md`, `wiki/autogen-multi-agent-conversation-framework.md`, `wiki/multiagent-debate-for-factuality-and-reasoning.md`, `raw/source_manifest.md`, `logs/query_log.md`.
- Source IDs: S01, S07, S08, S09, S10, S11, S12, S13, S15, S17, S20, S21, S23, S24.
- Answer summary: MCP supplies the tool/context exchange and authorization/security boundary; RAG supplies query-time raw evidence retrieval; LLM Wiki supplies persistent compiled memory with provenance, conflicts, and maintenance history; multi-agent systems supply task decomposition, verification, debate, and human/tool orchestration when justified. Together they form a layered reliability stack, but none independently guarantees reliability.
- Direct support vs synthesis: direct support comes from S21 for the four-layer stack, S11/S12/S13 for MCP boundaries, S01 for RAG, S10/S21 for LLM Wiki, and S07/S08/S09/S23 for multi-agent patterns and limits; synthesis connects those layers into an operational reliability stack.
- Write-back decision: no write-back; `wiki/project-scope-and-research-hypotheses.md` already contains the reusable stack framing and cross-links.
- Modified files: `logs/query_log.md`.
- Unresolved issues: experiments are still needed for pressure-point testing, authorization/state/rollback evidence artifacts, RAG-vs-LLM-Wiki division of labor, and when multi-agent topology improves reliability rather than adding cost or correlated errors.
- Diff saved: No file diff produced.

## Q08 | Multi-Agent Debate Reliability

- Question: I think multi-agent debate can enhance reliability, is that true?
- Pages read: `wiki/index.md`, `wiki/multiagent-debate-for-factuality-and-reasoning.md`, `wiki/autogen-multi-agent-conversation-framework.md`, `wiki/latent-agents-internalized-debate.md`, `wiki/contradiction-register.md`, `wiki/project-scope-and-research-hypotheses.md`, `raw/source_manifest.md`, `logs/query_log.md`.
- Source IDs: S07, S08, S09, S17, S21, S23.
- Answer summary: Yes, multi-agent debate can enhance reliability in some benchmark and structured-reasoning settings, but it does not automatically do so. S08 reports gains over single-agent, reflection, and majority-vote baselines across several tasks, while S09 qualifies the claim by showing that gains depend on initial reasoning strength, diversity, and resistance to majority pressure. S17 and S21 further caution that multi-agent topology should be justified by task needs and can add cost, delay, and correlated errors.
- Direct support vs synthesis: direct support comes from S08 for positive debate results, S09 for limits and majority pressure, S07 for multi-agent orchestration patterns, S17 for practical single-vs-multi-agent tradeoffs, and S23 for internalized debate cost tradeoffs; synthesis is the conditional reliability judgment.
- Write-back decision: no write-back; `wiki/multiagent-debate-for-factuality-and-reasoning.md` and `wiki/contradiction-register.md` already preserve both positive and skeptical evidence.
- Modified files: `logs/query_log.md`.
- Unresolved issues: transfer from S09's Knight-Knave-Spy setting to S08's broader factuality/math/chess/MMLU tasks remains open; production thresholds for when debate justifies cost, latency, and audit complexity remain `source-needed`.
- Diff saved: No file diff produced.
