from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEMO_ROOT = PROJECT_ROOT / "second_brain_demo"
RAW = DEMO_ROOT / "raw"
MANIFEST = RAW / "source_manifest.md"
WIKI = DEMO_ROOT / "wiki"
TESTS = PROJECT_ROOT / "experiments" / "ingest_tests.md"

EXPECTED_TESTS = {f"T{i:02d}" for i in range(1, 11)}
REQUIRED_FRONTMATTER = {"title", "page_type", "status", "updated", "sources", "confidence"}
FRONTMATTER_ENUMS = {
    "page_type": {"concept", "comparison", "entity", "register", "overview"},
    "status": {"draft", "reviewed"},
    "confidence": {"high", "medium", "low", "mixed"},
}
VERDICT_RE = re.compile(
    r"^- Verdict:\s+(?:\*\*)?(pass|partial|fail)(?:\*\*)?\s*$",
    flags=re.IGNORECASE | re.MULTILINE,
)


def manifest_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        if re.match(r"^\| S\d{2} \|", line):
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def frontmatter_fields(text: str) -> dict[str, str] | None:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, flags=re.DOTALL)
    if not match:
        return None

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if field:
            fields[field.group(1)] = field.group(2).strip()
    return fields


def source_list(value: str) -> tuple[set[str], bool]:
    if not (value.startswith("[") and value.endswith("]")):
        return set(), False
    body = value[1:-1].strip()
    if not body:
        return set(), True
    values = {item.strip() for item in body.split(",")}
    return values, all(re.fullmatch(r"S\d{2}", item) for item in values)


def test_sections(text: str) -> tuple[dict[str, str], list[str]]:
    headings = list(re.finditer(r"^## (T\d{2})\b[^\n]*$", text, flags=re.MULTILINE))
    sections: dict[str, str] = {}
    ids: list[str] = []
    for index, heading in enumerate(headings):
        test_id = heading.group(1)
        ids.append(test_id)
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        sections.setdefault(test_id, text[heading.end() : end])
    return sections, ids


def evidence_paths(section: str) -> list[str]:
    lines = section.splitlines()
    paths: list[str] = []
    in_evidence = False
    for line in lines:
        if line.strip() == "- Evidence file(s):":
            in_evidence = True
            continue
        if not in_evidence:
            continue
        item = re.match(r"^\d+\.\s+(.+?)\s*$", line)
        if item:
            candidate = item.group(1).strip().strip("`")
            if candidate.startswith(("second_brain_demo/", "evidence/", "experiments/")):
                paths.append(candidate)
            continue
        if line.strip():
            break
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Second Brain artifact")
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    required = [
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "AI_USE.md",
        PROJECT_ROOT / "memo.docx",
        MANIFEST,
        DEMO_ROOT / "schema" / "AGENTS.md",
        DEMO_ROOT / "schema" / "page_template.md",
        DEMO_ROOT / "schema" / "prompts.md",
        WIKI / "index.md",
        DEMO_ROOT / "logs" / "ingest_log.md",
        DEMO_ROOT / "logs" / "query_log.md",
        DEMO_ROOT / "logs" / "lint_log.md",
        TESTS,
        PROJECT_ROOT / "evidence",
        DEMO_ROOT / "evidence",
        DEMO_ROOT / "evidence" / "diffs",
    ]
    missing_required = [str(path.relative_to(PROJECT_ROOT)) for path in required if not path.exists()]

    manifest_text = MANIFEST.read_text(encoding="utf-8")
    rows = manifest_rows(manifest_text)
    source_ids = {row[0] for row in rows}
    source_types = {row[4] for row in rows if len(row) >= 5}

    missing_raw_files: list[str] = []
    for row in rows:
        if len(row) < 4:
            continue
        for filename in re.findall(r"`([^`]+)`", row[3]):
            if not (RAW / filename).exists():
                missing_raw_files.append(f"{row[0]} -> {filename}")

    wiki_files = sorted(WIKI.glob("*.md"))
    wiki_stems = {path.stem for path in wiki_files}
    citation_occurrences: list[str] = []
    links: list[tuple[str, str]] = []
    missing_frontmatter: list[str] = []
    invalid_frontmatter: list[str] = []
    unknown_frontmatter_sources: list[str] = []
    citations_missing_from_frontmatter: list[str] = []

    for path in wiki_files:
        text = path.read_text(encoding="utf-8")
        frontmatter_match = re.match(
            r"\A---\r?\n.*?\r?\n---(?:\r?\n|\Z)", text, flags=re.DOTALL
        )
        page_body = text[frontmatter_match.end() :] if frontmatter_match else text
        page_citations = re.findall(r"\[(S\d{2})\]", page_body)
        citation_occurrences.extend(page_citations)
        links.extend((path.name, target.strip()) for target in re.findall(r"\[\[([^\]|#]+)", text))

        fields = frontmatter_fields(text)
        if fields is None:
            missing_frontmatter.append(path.name)
            continue

        missing_fields = sorted(REQUIRED_FRONTMATTER - fields.keys())
        if missing_fields:
            invalid_frontmatter.append(f"{path.name}: missing {', '.join(missing_fields)}")

        for field, allowed in FRONTMATTER_ENUMS.items():
            if field in fields and fields[field] not in allowed:
                invalid_frontmatter.append(f"{path.name}: invalid {field}={fields[field]}")

        if "updated" in fields:
            try:
                valid_date = bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", fields["updated"]))
                date.fromisoformat(fields["updated"])
            except ValueError:
                valid_date = False
            if not valid_date:
                invalid_frontmatter.append(f"{path.name}: invalid updated={fields['updated']}")

        declared_sources, valid_source_syntax = source_list(fields.get("sources", ""))
        if "sources" in fields and not valid_source_syntax:
            invalid_frontmatter.append(f"{path.name}: sources must be [Sxx, ...]")

        for source_id in sorted(declared_sources - source_ids):
            unknown_frontmatter_sources.append(f"{path.name} -> {source_id}")
        for source_id in sorted(set(page_citations) - declared_sources):
            citations_missing_from_frontmatter.append(f"{path.name} -> {source_id}")

    citations = set(citation_occurrences)
    unknown_citations = sorted(citations - source_ids)
    broken_links = sorted(
        {f"{source} -> {target}" for source, target in links if target not in wiki_stems}
    )

    index_path = WIKI / "index.md"
    index_targets = set()
    if index_path.exists():
        index_text = index_path.read_text(encoding="utf-8")
        index_targets = {target.strip() for target in re.findall(r"\[\[([^\]|#]+)", index_text)}
    pages_missing_from_index = sorted((wiki_stems - {"index"}) - index_targets)

    tests_text = TESTS.read_text(encoding="utf-8")
    sections, test_ids = test_sections(tests_text)
    test_id_counts = Counter(test_ids)
    duplicate_tests = sorted(test_id for test_id, count in test_id_counts.items() if count > 1)
    found_tests = set(test_ids)
    missing_tests = sorted(EXPECTED_TESTS - found_tests)
    unexpected_tests = sorted(found_tests - EXPECTED_TESTS)
    missing_test_verdicts: list[str] = []
    multiple_test_verdicts: list[str] = []
    invalid_test_verdicts: list[str] = []
    parsed_verdicts: dict[str, str] = {}
    missing_evidence_paths: list[str] = []

    for test_id in sorted(EXPECTED_TESTS & found_tests):
        section = sections[test_id]
        verdicts = VERDICT_RE.findall(section)
        raw_verdict_lines = re.findall(r"^- Verdict:\s*(.*?)\s*$", section, flags=re.MULTILINE)
        if not verdicts:
            missing_test_verdicts.append(test_id)
            if raw_verdict_lines:
                invalid_test_verdicts.append(f"{test_id} -> {raw_verdict_lines[0]}")
        elif len(verdicts) > 1:
            multiple_test_verdicts.append(test_id)
        else:
            parsed_verdicts[test_id] = verdicts[0].lower()

        for artifact in evidence_paths(section):
            if not (PROJECT_ROOT / Path(artifact)).exists():
                missing_evidence_paths.append(f"{test_id} -> {artifact}")

    verdict_summary = Counter(parsed_verdicts.values())
    checks = {
        "at_least_12_sources": len(rows) >= 12,
        "at_least_3_source_types": len(source_types) >= 3,
        "all_manifest_raw_files_present": not missing_raw_files,
        "wiki_pages_present": bool(wiki_files),
        "citations_present": bool(citations),
        "no_unknown_citations": not unknown_citations,
        "no_broken_wikilinks": not broken_links,
        "wiki_frontmatter_complete": not missing_frontmatter and not invalid_frontmatter,
        "frontmatter_sources_valid": not unknown_frontmatter_sources,
        "citations_declared_in_frontmatter": not citations_missing_from_frontmatter,
        "all_wiki_pages_indexed": not pages_missing_from_index,
        "ten_test_sections": not missing_tests and not unexpected_tests and not duplicate_tests,
        "one_valid_verdict_per_test": (
            len(parsed_verdicts) == len(EXPECTED_TESTS)
            and not missing_test_verdicts
            and not multiple_test_verdicts
            and not invalid_test_verdicts
        ),
        "all_test_evidence_paths_present": not missing_evidence_paths,
        "required_files_present": not missing_required,
    }
    report = {
        "source_count": len(rows),
        "source_type_count": len(source_types),
        "source_types": sorted(source_types),
        "missing_raw_files": sorted(set(missing_raw_files)),
        "wiki_page_count": len(wiki_files),
        "citation_count": len(citation_occurrences),
        "unique_cited_source_count": len(citations),
        "unknown_citations": unknown_citations,
        "broken_wikilinks": broken_links,
        "missing_frontmatter": missing_frontmatter,
        "invalid_frontmatter": invalid_frontmatter,
        "unknown_frontmatter_sources": unknown_frontmatter_sources,
        "citations_missing_from_frontmatter": citations_missing_from_frontmatter,
        "pages_missing_from_index": pages_missing_from_index,
        "test_count": len(found_tests),
        "missing_tests": missing_tests,
        "unexpected_tests": unexpected_tests,
        "duplicate_tests": duplicate_tests,
        "verdict_count": len(parsed_verdicts),
        "verdict_summary": dict(sorted(verdict_summary.items())),
        "missing_test_verdicts": missing_test_verdicts,
        "multiple_test_verdicts": multiple_test_verdicts,
        "invalid_test_verdicts": invalid_test_verdicts,
        "missing_evidence_paths": sorted(set(missing_evidence_paths)),
        "missing_required_files": missing_required,
        "checks": checks,
        "overall": "pass" if all(checks.values()) else "fail",
    }

    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["overall"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
