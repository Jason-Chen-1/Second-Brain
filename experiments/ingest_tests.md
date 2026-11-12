# Ingest Stress Test Matrix

## T01 Contradiction

- Edge case: Two sources make incompatible claims. Does the wiki flag, preserve, resolve, or blur the conflict?
- Suggested sources: S08 and S09
- Hypothesis: The second brain can identify and report the contradiction while preserving both sides of the conflict.
- Input: 
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. S08 and S09
6. the existing wiki pages most relevant to the source topic
- Action:
Use prompt for Single-source Ingest to ingest the suggested sources.
- Expected behavior: S08's positive debate findings and S09's limiting findings should both remain visible; the wiki should create or update a contradiction record.
- Observed behavior: S09 updated the multiagent debate page and added an open contradiction/qualification entry: S08 reports broad benefits from debate, while S09 narrows that claim by showing dependence on reasoning strength, diversity, and resistance to majority pressure.
- Evidence file(s):
1. second_brain_demo/evidence/2026-07-09_ingest_S08_multiagent-debate_excerpts.md
2. second_brain_demo/evidence/2026-07-09_ingest_S09_multiagent-debate-limits_excerpts.md
3. second_brain_demo/evidence/diffs/2026-07-09_ingest_S09_multiagent-debate-limits.diff
4. second_brain_demo/wiki/contradiction-register.md
- Verdict: Pass
- Why it matters: This shows that the wiki can handle conflicting sources instead of silently choosing one side.

## T02 Supersession

- Edge case: A newer source updates an older fact. Does the old claim become archived, annotated, or silently overwritten?
- Suggested sources: S14 and S12/S13
- Hypothesis: The second brain can identify the updates on the same topic.
- Input:
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. S14, S12 and S13 in the given order
6. the existing wiki pages most relevant to the source topic
- Action: 
Use prompt for Single-source Ingest to ingest the suggested sources.
- Expected behavior: S14 should remain visible as historical MCP positioning, while S12 and S13 should update the wiki with newer production authorization and security boundaries instead of silently overwriting the older source.
- Observed behavior: S14 was preserved as the historical launch/positioning source. S12 created the MCP authorization page and superseded S14 for production authorization claims, while S13 added security best-practice guidance as a complement to S12.
- Evidence file(s):
1. second_brain_demo/evidence/2026-07-09_ingest_S14_mcp-positioning_excerpts.md
2. second_brain_demo/evidence/2026-07-09_ingest_S12_mcp-authorization_excerpts.md
3. second_brain_demo/evidence/2026-07-09_ingest_S13_mcp-security-best-practices_excerpts.md
4. second_brain_demo/evidence/diffs/2026-07-09_ingest_S12_mcp-authorization.diff
5. second_brain_demo/wiki/model-context-protocol-architecture.md
6. second_brain_demo/wiki/model-context-protocol-authorization.md
- Verdict: Pass
- Why it matters: This shows whether the wiki can preserve older context while preferring newer or more specific sources for current claims.

## T03 Near Duplicate

- Edge case: Two sources say almost the same thing with slight differences. Does the wiki deduplicate without losing nuance?
- Suggested sources: S11 and S12
- Hypothesis: The second brain can separate adjacent MCP concepts without duplicating or blurring their claims.
- Input:
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. second_brain_demo/wiki/model-context-protocol-architecture.md
6. second_brain_demo/wiki/model-context-protocol-authorization.md
7. second_brain_demo/wiki/model-context-protocol-security-best-practices.md
8. second_brain_demo/logs/query_log.md
9. S11 and S12
- Action:
Use prompt for Query to ask the question: What is the difference between MCP architecture and MCP authorization?
- Expected behavior: S11 and S12 should not be merged into one vague MCP page. The wiki should keep S11's architecture vocabulary separate from S12's authorization requirements while linking the two pages.
- Observed behavior: S11 created the MCP architecture page, and S12 created the MCP authorization page. Query Q06 confirmed that the system can answer the difference between architecture and authorization without losing the relationship between them.
- Evidence file(s):
1. second_brain_demo/evidence/2026-07-09_ingest_S11_mcp-architecture_excerpts.md
2. second_brain_demo/evidence/2026-07-09_ingest_S12_mcp-authorization_excerpts.md
3. second_brain_demo/evidence/diffs/2026-07-09_ingest_S12_mcp-authorization.diff
4. second_brain_demo/wiki/model-context-protocol-architecture.md
5. second_brain_demo/wiki/model-context-protocol-authorization.md
6. second_brain_demo/logs/query_log.md
- Verdict: Pass
- Why it matters: Near-duplicate or adjacent sources are common in a growing second brain; the system needs to deduplicate while preserving conceptual nuance.

## T04 Ambiguous Entity

- Edge case: Same name, different person, organization, or concept. Does linking stay precise?
- Suggested sources: S11 and S22
- Hypothesis: The second brain can disambiguate the MCP acronym and avoid linking unrelated concepts.
- Input:
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. S11 and S22
6. the existing wiki pages most relevant to the source topic
- Action:
Use prompt for Single-source Ingest to ingest the suggested sources.
- Expected behavior: S22 should not be linked as Model Context Protocol evidence even though it uses the acronym MCP. The wiki should separate Maximum Clique Problem from Model Context Protocol and preserve precise linking.
- Observed behavior: S22 was ingested as MCP acronym disambiguation. The wiki created a separate disambiguation page and updated the MCP architecture page to state that S22 is about Maximum Clique Problem, not Model Context Protocol.
- Evidence file(s):
1. second_brain_demo/evidence/2026-07-09_ingest_S22_mcp-acronym-disambiguation_excerpts.md
2. second_brain_demo/evidence/diffs/2026-07-09_ingest_S22_mcp-acronym-disambiguation.diff
3. second_brain_demo/wiki/mcp-acronym-disambiguation.md
4. second_brain_demo/wiki/model-context-protocol-architecture.md
- Verdict: Pass
- Why it matters: This tests whether the wiki avoids false links when different domains share the same abbreviation.

## T05 Numerical Precision

- Edge case: Tables, percentages, dates, or units. Does the wiki preserve exact values and source them?
- Suggested sources: S04, S05 and S10
- Hypothesis: The second brain can preserve the exact values.
- Input:
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. S04, S05 and S10
6. the existing wiki pages most relevant to the source topic
- Action:
Cross-check the numbers in raw sources and wikis.
- Expected behavior: Dates, benchmark counts, pass rates, scale claims, and other numbers should be preserved accurately.
- Observed behavior: The checked numbers in the wiki pages match the corresponding raw sources.
- Evidence file(s):
1. second_brain_demo/raw/S04.pdf
2. second_brain_demo/wiki/api-bank-tool-augmented-llm-benchmark.md
3. second_brain_demo/raw/S05.pdf
4. second_brain_demo/wiki/tau-bench-agent-consistency-benchmark.md
5. second_brain_demo/raw/S10_llm_wiki.source.md
6. second_brain_demo/wiki/llm-wiki.md
- Verdict: Pass
- Why it matters: Numeric drift can make a knowledge base unreliable even when the qualitative summary is correct.

## T06 Images / Figures

- Edge case: Charts, screenshots, diagrams, or inline images. What information survives ingest?
- Suggested sources: S24
- Hypothesis: The second brain can preserve visible image evidence without adding unsupported interpretation.
- Input:
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. S24
6. the existing wiki pages most relevant to the source topic
- Action:
Use prompt for Single-source Ingest to ingest the suggested sources.
- Expected behavior: The topic-related information should be preserved, and the wiki should preserve only information visible in the screenshot without inferring file contents, workflow completeness, or project reliability from the image alone.
- Observed behavior: S24 was used only for screenshot-level visible folder-structure evidence. The ingest log records visible folder names and explicitly separates visible facts from inferred claims about completeness, file contents, or reliability.
- Evidence file(s):
1. second_brain_demo/evidence/2026-07-09_ingest_S24_project-folder-screenshot_notes.md
2. second_brain_demo/evidence/diffs/2026-07-09_ingest_S24_project-folder-screenshot.diff
3. second_brain_demo/wiki/llm-wiki.md
4. second_brain_demo/wiki/project-scope-and-research-hypotheses.md
- Verdict: Pass
- Why it matters: Image sources can be hard to interpret and easy to over-interpret; this test checks whether the wiki keeps visual evidence within its real evidentiary boundary.
- Notes: This result is based on ingest artifact inspection.

## T07 Low-quality Source

- Edge case: A low-quality, secondary, or opinion-based source makes a useful claim. Does the wiki preserve it as a low-confidence viewpoint without letting it independently support a key conclusion?
- Suggested sources: S20
- Hypothesis: The second brain can retain a low-quality viewpoint while preventing it from becoming decisive evidence.
- Input:
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. S20
6. the existing wiki pages most relevant to the source topic
- Action:
Use prompt for Single-source Ingest to ingest the suggested sources.
- Expected behavior: S20 should be kept as a low-quality critique or viewpoint. It should not independently support a key conclusion or override higher-quality RAG and LLM Wiki sources.
- Observed behavior: S20 was labeled low quality and used to add a low-confidence critique boundary and design tension around LLM Wiki versus RAG.
- Evidence file(s):
1. second_brain_demo/evidence/2026-07-09_ingest_S20_llm-wiki-critique_excerpts.md
2. second_brain_demo/evidence/diffs/2026-07-09_ingest_S20_llm-wiki-critique.diff
3. second_brain_demo/wiki/llm-wiki.md
4. second_brain_demo/wiki/retrieval-augmented-generation.md
5. second_brain_demo/wiki/contradiction-register.md
- Verdict: Pass
- Why it matters: Low-quality sources can still be useful for stress-testing claims, but only if the wiki prevents them from being over-promoted.

## T08 Non-obvious Connection

- Edge case: Two sources imply a useful cross-source synthesis neither states explicitly. Does the wiki surface it?
- Suggested sources: S11, S13 and S21
- Hypothesis: The second brain can synthesize a useful reliability-stack claim across architecture, security, and project-scope sources.
- Input:
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. second_brain_demo/wiki/project-scope-and-research-hypotheses.md
6. second_brain_demo/wiki/model-context-protocol-architecture.md
7. second_brain_demo/wiki/retrieval-augmented-generation.md
8. second_brain_demo/wiki/llm-wiki.md
9. second_brain_demo/wiki/autogen-multi-agent-conversation-framework.md
10. second_brain_demo/wiki/multiagent-debate-for-factuality-and-reasoning.md
11. second_brain_demo/logs/query_log.md
12. S11, S13 and S21
- Action:
Use prompt for Query to ask the question: How do MCP, RAG, LLM Wiki, and multi-agent systems form an enterprise agent reliability stack?
- Expected behavior: The wiki should surface a cross-source synthesis that is not stated by any single source alone.
- Observed behavior: Query Q07 synthesized MCP, RAG, LLM Wiki, and multi-agent systems into a layered enterprise-agent reliability stack. MCP supplies tool/context and authorization/security boundaries, RAG supplies query-time evidence retrieval, LLM Wiki supplies persistent compiled memory, and multi-agent systems support decomposition and verification when justified.
- Evidence file(s):
1. second_brain_demo/evidence/2026-07-09_ingest_S11_mcp-architecture_excerpts.md
2. second_brain_demo/evidence/2026-07-09_ingest_S13_mcp-security-best-practices_excerpts.md
3. second_brain_demo/evidence/2026-07-09_ingest_S21_project-scope_excerpts.md
4. second_brain_demo/wiki/project-scope-and-research-hypotheses.md
5. second_brain_demo/wiki/model-context-protocol-architecture.md
6. second_brain_demo/wiki/model-context-protocol-security-best-practices.md
7. second_brain_demo/wiki/retrieval-augmented-generation.md
8. second_brain_demo/wiki/llm-wiki.md
9. second_brain_demo/wiki/autogen-multi-agent-conversation-framework.md
10. second_brain_demo/wiki/multiagent-debate-for-factuality-and-reasoning.md
11. second_brain_demo/logs/query_log.md
- Verdict: Pass
- Why it matters: The second brain should do more than store summaries; it should support reusable synthesis across related sources.

## T09 Negative Evidence

- Edge case: A source omits an expected claim or reports a null result. Does the wiki retain absence or uncertainty?
- Suggested sources: S06 and S09
- Hypothesis: The second brain can preserve negative evidence, limitations, and uncertainty instead of forcing a positive conclusion.
- Input:
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. second_brain_demo/wiki/toolsandbox-stateful-tool-use-benchmark.md
6. second_brain_demo/wiki/multiagent-debate-for-factuality-and-reasoning.md
7. second_brain_demo/wiki/autogen-multi-agent-conversation-framework.md
8. second_brain_demo/wiki/latent-agents-internalized-debate.md
9. second_brain_demo/wiki/contradiction-register.md
10. second_brain_demo/wiki/project-scope-and-research-hypotheses.md
11. second_brain_demo/logs/query_log.md
12. S06 and S09
- Action:
Use prompt for Query to ask the question: I think multi-agent debate can enhance reliability, is that true?
- Expected behavior: The wiki should retain absence, limits, and uncertainty instead of forcing a positive conclusion. S06's insufficient-information/stateful-tool concerns and S09's debate-limit evidence should remain visible.
- Observed behavior: The reply was "Yes, but only conditionally." It did not simply support the positive view from S08, but also illustrated uncertainty through S09.
- Evidence file(s):
1. second_brain_demo/evidence/2026-07-09_ingest_S06_toolsandbox_excerpts.md
2. second_brain_demo/evidence/2026-07-09_ingest_S09_multiagent-debate-limits_excerpts.md
3. second_brain_demo/evidence/diffs/2026-07-09_ingest_S06_toolsandbox.diff
4. second_brain_demo/evidence/diffs/2026-07-09_ingest_S09_multiagent-debate-limits.diff
5. second_brain_demo/wiki/toolsandbox-stateful-tool-use-benchmark.md
6. second_brain_demo/wiki/multiagent-debate-for-factuality-and-reasoning.md
7. second_brain_demo/wiki/contradiction-register.md
8. second_brain_demo/logs/query_log.md
- Verdict: Pass
- Why it matters: A reliable knowledge base should remember limitations and null or negative evidence, not only positive results.

## T10 Scale

- Edge case: Move from 5 to 20+ sources. What breaks first: index, links, context, consistency, or latency?
- Suggested sources: all sources
- Hypothesis: The second brain can support ingesting more than 20 sources without structural errors and with only a reasonable increase in latency.
- Input:
1. second_brain_demo/raw/source_manifest.md
2. second_brain_demo/schema/AGENTS.md
3. second_brain_demo/schema/page_template.md
4. second_brain_demo/wiki/index.md
5. all sources
6. the existing wiki pages most relevant to the source topic
- Action:
Use prompt for Single-source Ingest to ingest the suggested sources.
- Expected behavior: The index and links should be preserved, the context should be handled appropriately, the output should remain consistent with the sources, and latency should increase only within a reasonable range.
- Observed behavior: No errors occurred in the index, links, context, or consistency checks. The latency growth was acceptable.
- Evidence file(s):
1. second_brain_demo/evidence
2. second_brain_demo/wiki
3. second_brain_demo/logs
- Verdict: Pass
- Why it matters: A reliable knowledge base should be able to support a relatively large number of sources and wiki pages. How the second brain behaves as ingests increase should be considered.
