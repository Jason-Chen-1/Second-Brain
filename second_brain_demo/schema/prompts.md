# Reusable Prompts

This file is only for building, querying, and maintaining the knowledge base. Audit materials from each operation are saved in `evidence/` so later readers can inspect what changed.

Project directories:

- `second_brain_demo/raw/`: raw sources and `source_manifest.md`
- `second_brain_demo/wiki/`: generated and maintained wiki pages
- `second_brain_demo/schema/`: rules, templates, and prompts
- `second_brain_demo/logs/`: append-only ingest, query, and lint logs
- `evidence/`: audit materials such as diffs, page excerpts, terminal output, or screenshot notes
- `evidence/diffs/`: minimal relevant diffs for operations that modify files

## Single-source Ingest

```text
Follow `second_brain_demo/schema/AGENTS.md` to ingest [Sxx]. The goal is to update the knowledge base.

Read first:
1. `second_brain_demo/raw/source_manifest.md`
2. `second_brain_demo/schema/AGENTS.md`
3. `second_brain_demo/schema/page_template.md`
4. `second_brain_demo/wiki/index.md`, creating it if missing
5. the raw file, PDF, screenshot, or `.source.md` for [Sxx]
6. the existing wiki pages most relevant to the source topic

Tasks:
- Do not modify raw source files.
- Extract core claims, entities, concepts, numbers, dates, versions, limits, negative results, and uncertainty.
- Decide whether to update existing wiki pages or create a new page.
- If creating a new page, use `page_template.md` and link it from `wiki/index.md`.
- Cite every nontrivial factual claim with a source ID such as `[Sxx]`.
- Check numbers, dates, protocol versions, normative terms, and benchmark results against the source.
- If the source conflicts with existing sources, update or create `wiki/contradiction-register.md` and preserve both sides.
- If the source updates an old fact, preserve the historical claim and mark the supersession relationship.
- If the source is low-quality, synthetic, a screenshot, an opinion piece, or secondary material, state its evidentiary boundary.
- Check wikilinks, frontmatter, sources, confidence, and index entry for all changed pages.

After completion:
1. Update `second_brain_demo/logs/ingest_log.md` with source ID, files read, actions, created/modified files, verification, exceptions, and unresolved issues.
2. If files changed, run `git diff -- [changed files]` and save the minimal relevant diff to `evidence/diffs/YYYY-MM-DD_ingest_[Sxx-or-topic].diff`.
3. Record the diff path in `ingest_log.md`; if no diff was produced, write `No file diff produced`.
4. Save page excerpts, terminal output, or screenshot notes in `evidence/` when useful, and record their paths in `ingest_log.md`.
5. In the final response, state which wiki pages changed, whether a new page was created, whether conflicts or uncertainty remain, whether the log was updated, and where diff/evidence was saved.
```

## Multi-source Ingest

```text
Follow `second_brain_demo/schema/AGENTS.md` to ingest [Sxx-Syy] one source at a time. The goal is to update the knowledge base, not to merge all sources into a single summary.

Read first:
1. `second_brain_demo/raw/source_manifest.md`
2. `second_brain_demo/schema/AGENTS.md`
3. `second_brain_demo/schema/page_template.md`
4. `second_brain_demo/wiki/index.md`
5. the raw file for each source
6. relevant wiki pages

For each source:
- Check ID, type, quality, shareability, and intended use in the manifest.
- Extract claims, entities, numbers, dates, limits, negative results, and uncertainty.
- Decide whether the source supplements, conflicts with, updates, duplicates, qualifies, or disambiguates existing knowledge.
- Update necessary wiki pages and cite source IDs for all nontrivial factual claims.
- Record page changes and exceptions for that source.

After all sources:
- Update `wiki/index.md`.
- Check and update `wiki/contradiction-register.md`.
- Check frontmatter, sources, confidence, wikilinks, and index entries for all changed pages.
- Update `logs/ingest_log.md` by source or source group.
- If files changed, run `git diff -- [changed files]` and save the minimal relevant diff to `evidence/diffs/YYYY-MM-DD_ingest_[source-range-or-topic].diff`.
- Record the diff path in `ingest_log.md`; if no diff was produced, write `No file diff produced`.
- Save page excerpts, terminal output, or screenshot notes in `evidence/` when useful.
- Final response: report each source result, created/modified wiki pages, conflicts or uncertainty, log update, and diff/evidence location.
```

## Screenshot Ingest

```text
Follow `second_brain_demo/schema/AGENTS.md` to ingest screenshot source [Sxx]. The goal is to add only confirmable screenshot information to the knowledge base.

Read first:
1. `second_brain_demo/raw/source_manifest.md`
2. `second_brain_demo/schema/AGENTS.md`
3. `second_brain_demo/schema/page_template.md`
4. `second_brain_demo/raw/[Sxx_xxx.png]`
5. relevant wiki pages

Tasks:
- Describe clearly visible text, interface elements, chart structure, and context.
- Separate directly visible information from inference.
- Do not treat unclear, hidden, or unverifiable content as fact.
- If OCR or visual recognition is used, state that it may be wrong and preserve uncertainty.
- Update necessary wiki pages and `wiki/index.md`.
- Cite screenshot-derived information with `[Sxx]`.

After completion:
1. Update `logs/ingest_log.md`.
2. If files changed, run `git diff -- [changed files]` and save the minimal relevant diff to `evidence/diffs/YYYY-MM-DD_ingest_[Sxx-screenshot].diff`.
3. Record the diff path in `ingest_log.md`; if no diff was produced, write `No file diff produced`.
4. Save screenshot notes or page excerpts in `evidence/` when useful.
5. Final response: state what was written, what was omitted as uncertain, whether the log was updated, and where diff/evidence was saved.
```

## Query

```text
Follow the Query and Write-back rules in `second_brain_demo/schema/AGENTS.md` to answer this question:

[question]

Read first:
1. `second_brain_demo/wiki/index.md`
2. the smallest necessary set of relevant wiki pages
3. `second_brain_demo/raw/source_manifest.md`
4. relevant raw sources only when needed
5. `second_brain_demo/logs/query_log.md`

Consider:
- Is this a factual query, comparison, mechanism explanation, evidence audit, research hypothesis, or write-back decision?
- Which statements are directly supported by sources, and which are synthesis?
- Are there conflicts, version updates, low-quality sources, negative results, uncertainty, or `source-needed` gaps?
- Does the answer depend on dates, protocol versions, benchmark numbers, or other unstable information?
- Is there enough evidence to answer?
- Should the answer be written back to the wiki? Write back only if it is reusable, supported by at least three sources, and creates a useful comparison, connection, or framework.

Output:
1. Direct answer.
2. Supporting source IDs.
3. Distinction between direct support and synthesis.
4. Uncertainty, conflicts, or evidence gaps.
5. Write-back decision and affected page, if any.

After completion:
- Update `logs/query_log.md` with the question, pages read, answer summary, source IDs, write-back decision, modified files, and unresolved issues.
- If writing back, update the relevant wiki pages and `wiki/index.md`.
- If files changed, run `git diff -- [changed files]` and save the minimal relevant diff to `evidence/diffs/YYYY-MM-DD_query_[short-name].diff`.
- Record the diff path in `query_log.md`; if no diff was produced, write `No file diff produced`.
- Save answer excerpts or write-back notes in `evidence/` when useful.
- Final response: state what was read, whether write-back happened, whether the log was updated, and where diff/evidence was saved.
```

## Lint

```text
Follow the Lint rules in `second_brain_demo/schema/AGENTS.md` to check the knowledge base.

Read first:
1. `second_brain_demo/schema/AGENTS.md`
2. `second_brain_demo/raw/source_manifest.md`
3. `second_brain_demo/wiki/`
4. `second_brain_demo/logs/ingest_log.md`
5. `second_brain_demo/logs/query_log.md`
6. `second_brain_demo/logs/lint_log.md`

Check:
- directory integrity for raw, wiki, schema, and logs;
- manifest consistency and missing raw files;
- wiki frontmatter fields;
- provenance and unknown source IDs;
- broken links, orphan pages, duplicate pages, and missing index entries;
- source-quality handling;
- temporal/version claims;
- contradiction preservation;

Fix rules:
- Automatically fix deterministic issues such as missing index links, obvious broken links, missing log entries, and formatting errors.
- Do not rewrite judgment-heavy research conclusions automatically; list recommendations first.
- Do not modify raw source files.

After completion:
1. Update `logs/lint_log.md` with check time, files read, issues found, automatic fixes, and unresolved recommendations.
2. If files changed, run `git diff -- [changed files]` and save the minimal relevant diff to `evidence/diffs/YYYY-MM-DD_lint_[short-name].diff`.
3. Record the diff path in `lint_log.md`; if no diff was produced, write `No file diff produced`.
4. Save terminal output, issue lists, or page excerpts in `evidence/` when useful.
5. Final response: list issues by severity, say what was fixed, what needs human judgment, and where diff/evidence was saved.
```
