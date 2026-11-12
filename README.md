# Second Brain Demo

This README documents the setup in enough detail that another RA can recreate it.

## 1. Operating System, App Versions, Model/Tool Used, Subscription/API Constraints, Plugins/Extensions, and Installed Packages

| Item | Setup used |
|---|---|
| Operating system | Windows. Registry values on the build machine: `Windows 10 Home China`, version `25H2`, build `26200.8655`. |
| Model/tool | OpenAI Codex was used to inspect local files and build and maintain the Markdown wiki. The exact Codex app version and model version were not recorded. |
| Knowledge-base app | The artifact is plain Markdown and can optionally be opened as an Obsidian vault. The Obsidian version was not recorded. |
| Subscription/API constraints | The Python validator requires no API key or subscription. Replaying an LLM ingest requires Codex access or a comparable tool that can read and edit local files. The original subscription plan and API limits were not recorded. |
| Plugins/extensions | No Obsidian community-plugin folder is included. The `.obsidian/core-plugins.json` file records the enabled Obsidian core plugins. |
| Python | Current command-line Python: `3.12.7`. Current bundled Python: `3.12.13`. |
| Installed packages | `pdfplumber 0.11.9` is available in the current bundled environment. `experiments/reproduce.py` uses only the Python standard library. |
| Other tools | Git `2.53.0.windows.1`; ripgrep `15.1.0`. |

## 2. Directory Tree, Naming Conventions, Schema File, Key Prompts/Commands, and Model Settings That Matter

```text
.
|-- memo.docx
|-- README.md
|-- AI_USE.md
|-- second_brain_demo/
|   |-- .obsidian/            # optional Obsidian configuration
|   |-- raw/                  # source files/captures and source_manifest.md
|   |-- wiki/                 # generated Markdown pages and index.md
|   |-- schema/               # AGENTS.md, page_template.md, prompts.md
|   |-- logs/                 # ingest, query, and lint logs
|   `-- evidence/             # per-source notes, diffs, and lint evidence
|-- experiments/
|   |-- ingest_tests.md       # T01-T10 test definitions and verdicts
|   `-- reproduce.py          # structural validator
`-- evidence/                 # project-level reproduction output
```

**Naming conventions**

- Sources use IDs such as `S01` and `S24`; their metadata and shareability are recorded in `second_brain_demo/raw/source_manifest.md`.
- Wiki filenames use lowercase English kebab-case.
- Nontrivial claims use `[Sxx]` citations.
- Internal links use Obsidian `[[wikilinks]]`.
- Evidence and diff filenames begin with the operation date and source ID or topic.

**Schema files**

- `second_brain_demo/schema/AGENTS.md` is the operating contract for folder ownership, frontmatter, citations, page creation/update, contradictions, ingest, query write-back, and lint.
- `second_brain_demo/schema/page_template.md` defines the standard wiki-page structure.
- `second_brain_demo/schema/prompts.md` contains the single-source ingest, multi-source ingest, screenshot ingest, query, and lint prompts.

For LLM operations, use the complete relevant prompt from `second_brain_demo/schema/prompts.md` and require the model to follow `second_brain_demo/schema/AGENTS.md`.

## 3. How to Run or Replay the Demo Artifact

**Inspect the demo**

1. Open `second_brain_demo/wiki/index.md` in a Markdown editor, or open `second_brain_demo/` as an Obsidian vault.
2. Follow the index links to inspect wiki pages.
3. Trace any `[Sxx]` citation through `second_brain_demo/raw/source_manifest.md` to the corresponding raw file or capture note.
4. Inspect `second_brain_demo/logs/` for ingest, query, and lint records.
5. Inspect `experiments/ingest_tests.md` and follow its evidence paths into `second_brain_demo/evidence/`.

**Run the validator**

From the project root:

```powershell
python experiments/reproduce.py
```