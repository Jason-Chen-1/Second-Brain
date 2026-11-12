# 2026-07-11 Lint Check Notes

## Files Read

- `schema/AGENTS.md`
- `raw/source_manifest.md`
- `wiki/*.md`
- `logs/ingest_log.md`
- `logs/query_log.md`
- `logs/lint_log.md`

## Automated Checks

- Manifest source IDs: S01-S24 found.
- Missing raw files referenced by manifest: 0.
- Wiki frontmatter structural issues: 0 after fix.
- Unknown source IDs in wiki pages: 0.
- Source IDs cited in page bodies but omitted from frontmatter: 13 before fix, 0 after fix.
- Broken wikilinks: 0.
- Missing `wiki/index.md` entries: 0.
- Duplicate wiki page titles: 0.

## Automatic Fixes

Added missing body-cited source IDs to frontmatter and updated `updated` dates to 2026-07-11 in:

- `wiki/autogen-multi-agent-conversation-framework.md`
- `wiki/llm-wiki.md`
- `wiki/model-context-protocol-architecture.md`
- `wiki/model-context-protocol-authorization.md`
- `wiki/multiagent-debate-for-factuality-and-reasoning.md`
- `wiki/tau-bench-agent-consistency-benchmark.md`
- `wiki/toolformer-self-supervised-tool-use.md`
- `wiki/toolsandbox-stateful-tool-use-benchmark.md`

## Semantic Spot Checks

- S20 low-quality/opinion boundary is preserved on `wiki/llm-wiki.md`, `wiki/retrieval-augmented-generation.md`, and `wiki/contradiction-register.md`.
- S24 synthetic screenshot boundary is preserved on `wiki/llm-wiki.md` and `wiki/project-scope-and-research-hypotheses.md`.
- Contradictions remain preserved in `wiki/contradiction-register.md`.
- MCP historical, stable authorization, and current security-practice claims include dated or access-date framing.

## Git Diff Result

`git diff -- wiki\autogen-multi-agent-conversation-framework.md wiki\llm-wiki.md wiki\model-context-protocol-architecture.md wiki\model-context-protocol-authorization.md wiki\multiagent-debate-for-factuality-and-reasoning.md wiki\tau-bench-agent-consistency-benchmark.md wiki\toolformer-self-supervised-tool-use.md wiki\toolsandbox-stateful-tool-use-benchmark.md` produced no output because the affected wiki files are currently untracked in Git.

