# Wiki Maintainer Contract

## 1. Scope

Maintain a knowledge base about reliable knowledge and tool use for enterprise AI agents, with emphasis on MCP, multi-agent systems, RAG, LLM Wiki, security, evaluation, and auditability.

## 2. Directory Ownership

- `raw/`: read-only sources and manifest. Do not modify captured source materials.
- `wiki/`: derived knowledge pages that the AI may create and update.
- `schema/`: human/AI maintained rules, templates, and prompts. Significant changes must be explainable.
- `logs/`: append-only event logs.
- `experiments/`: test designs and results, maintained separately from ordinary knowledge-base prompts.
- `evidence/`: diffs, screenshots, terminal outputs, excerpts, and other audit materials.

Adding files to `raw/` does not automatically update the wiki. A source must be explicitly ingested, and related wiki pages, index pages, logs, and evidence should be updated as appropriate.

## 3. Naming

- Markdown filenames use lowercase kebab-case English names.
- Concept pages should use stable concept names rather than dates or model versions.
- Ambiguous entities must use qualifiers, such as `atlas-crm-synthetic.md` and `atlas-pay-synthetic.md`.

## 4. Required Page Metadata

Every wiki page must begin with YAML frontmatter:

```yaml
---
title: Human-readable title
page_type: concept|comparison|entity|register|overview
status: draft|reviewed
updated: YYYY-MM-DD
sources: [S01, S02]
confidence: high|medium|low|mixed
---
```

## 5. Claims and Provenance

- Every nontrivial factual claim must cite a source ID in the same sentence or paragraph, for example `[S05]`.
- Numbers, dates, units, protocol versions, and normative terms such as `MUST`, `SHOULD`, and `MAY` must be checked against the source.
- Secondary sources must not override primary sources.
- Low-quality sources must not independently support key conclusions.
- Inferences must be labeled as synthesis and should name the supporting sources.
- If no source is available, write `source-needed` rather than inventing a citation.

## 6. Internal Links

- Use Obsidian wikilinks: `[[page-name]]` or `[[page-name|display text]]`.
- New pages must be linked from `index.md` and from at least one relevant topic page.
- Link targets use filenames without `.md`.

## 7. Create vs Update

- Create a new page when there is a stable new concept or entity supported by at least two sources or one high-quality primary source.
- Update an existing page when the new material changes evidence, scope, time, or confidence for a covered concept.
- Do not create a page for one-off answers, duplicated content, or material with no reusable value.

## 8. Contradictions

- Do not silently merge conflicts or create false consensus.
- Record claim A, claim B, conditions, source quality, and applicability.
- Use `contradiction-register.md` for persistent contradiction records.
- Mark a contradiction as leaning resolved only when newer, higher-quality, directly comparable evidence exists; otherwise keep it open.

## 9. Supersession and Time

- New versions must not erase old historical claims; mark older claims as superseded and link to the updating source.
- Protocol and product claims must include version and access date when relevant.
- Words like current or latest must be tied to a concrete date.

## 10. Ingest Workflow

1. Confirm source ID, shareability, and quality in the manifest.
2. Read the source and extract claims, numbers, entities, limitations, negative results, and uncertainty.
3. Read `wiki/index.md` and identify pages to update.
4. Update source-related topic pages first, then overview or register pages.
5. Check numbers, dates, citations, and wikilinks.
6. Append to `logs/ingest_log.md`: source, prompt/action, created or modified files, verification, and exceptions.
7. Save relevant audit material in `evidence/` when the operation changes important files.

## 11. Query and Write-back

- Read `index.md` first, then the smallest necessary set of wiki pages.
- Answers must list source IDs and uncertainty.
- Write back only when the answer spans at least three sources, is reusable, creates a new comparison/connection/framework, and is not a temporary guess.
- Record write-back decisions in `logs/query_log.md`.

## 12. Tool Calls and Enterprise Safety

- Distinguish read tools from write tools; write tools require a higher approval threshold.
- Pause and clarify when tool names, entities, parameters, or side effects are ambiguous.
- Use least privilege; prohibit token passthrough; do not treat a session ID as authentication.
- For high-risk actions, display the tool, target, key parameters, side effects, and rollback plan, then require human confirmation.
- Preserve summaries of tool inputs, outputs, authorization context, time, and errors without recording secrets.

## 13. Lint

Check for missing frontmatter, unknown sources, broken links, orphan pages, duplicate pages, unsourced claims, unresolved contradictions, stale versions, low-quality source overuse, uncited numbers, sensitive information, and unsafe write-tool assumptions.
