# Lint Log

This log records maintenance and audit checks on the knowledge base.

## 2026-07-09 | Language Normalization

- Action: began replacing Chinese and mojibake text in Markdown project documents with clear English while preserving source IDs, file roles, and intended effects.
- Files checked: root documentation, schema files, raw manifest, logs, wiki pages, and source explanations.
- Open issue: verify after completion that no Chinese or mojibake text remains in Markdown files.

## Future Lint Items

- Check missing frontmatter in wiki pages.
- Check unknown source IDs and broken wikilinks.
- Check that low-quality sources are not over-promoted.
- Check that dates, versions, and numerical claims are cited.
- Check that evidence paths and logs remain consistent after future operations.

## 2026-07-11 | Knowledge Base Lint

- Check time: 2026-07-11.
- Files read: `schema/AGENTS.md`, `raw/source_manifest.md`, `wiki/*.md`, `logs/ingest_log.md`, `logs/query_log.md`, `logs/lint_log.md`.
- Issues found:
  - Medium: 13 cited source IDs appeared in wiki page bodies but were omitted from the same pages' frontmatter `sources` lists.
  - No missing raw files, unknown source IDs, missing required frontmatter fields, bad frontmatter enum values, duplicate titles, broken wikilinks, or missing index entries were detected after the automatic fixes.
  - No automatic rewrite was made for judgment-heavy research conclusions.
- Automatic fixes:
  - Added missing source IDs to frontmatter and updated `updated: 2026-07-11` in `wiki/autogen-multi-agent-conversation-framework.md`, `wiki/llm-wiki.md`, `wiki/model-context-protocol-architecture.md`, `wiki/model-context-protocol-authorization.md`, `wiki/multiagent-debate-for-factuality-and-reasoning.md`, `wiki/tau-bench-agent-consistency-benchmark.md`, `wiki/toolformer-self-supervised-tool-use.md`, and `wiki/toolsandbox-stateful-tool-use-benchmark.md`.
- Verification:
  - Re-ran checks for manifest source IDs, missing raw files, wiki frontmatter, body citations versus frontmatter sources, unknown source IDs, broken wikilinks, duplicate titles, and missing index entries; all returned zero errors after the fixes.
  - Spot-checked source-quality handling for S20 and S24, temporal/version framing for MCP pages, and contradiction preservation in `wiki/contradiction-register.md`.
- Evidence saved: `evidence/2026-07-11_lint_check_notes.md`.
- Diff saved: No file diff produced. `git diff -- [changed wiki files]` returned no output because the affected wiki files are currently untracked in Git.
- Unresolved recommendations:
  - Human review can decide whether draft pages should be promoted to `reviewed`; this was not changed automatically.
  - Because many knowledge-base files are untracked in Git, future diff capture would be stronger after the current KB state is added to version control.
