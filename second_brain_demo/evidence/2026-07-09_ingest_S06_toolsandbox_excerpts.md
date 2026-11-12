# S06 ToolSandbox Extraction Notes

- Source metadata checked in `raw/source_manifest.md`: S06 is `ToolSandbox - Lu et al.`, dated 2024-08-08, public, paper/PDF, high quality, with intended use for stateful, multi-turn, insufficient-information tool evaluation.
- PDF extraction used bundled Python with `pdfplumber`; the PDF has 24 pages.
- Core definition checked from abstract and Section 2: ToolSandbox includes stateful tool execution, implicit state dependencies, a built-in user simulator for on-policy conversational evaluation, and dynamic milestone/minefield evaluation.
- Stateful claims checked from Section 2.1: stateful tools inspect, depend on, or manipulate world states including cellular service, Wi-Fi, location service, and low-battery mode; stateful tools cover 44% of the toolbox.
- User simulator claims checked from Section 2.2 and Tables 2-3: Knowledge Boundary and Demonstration reduce GPT-4o user-simulator hallucination to 6.97% and instruction-following error to 0.77%; simulator error rates across GPT-4o, Claude-3-Opus, and Gemini-1.5-Pro agents are reported around 7.78%-8.07% total error.
- Benchmark statistics checked from Table 4: ToolSandbox has 13.9 average turns, 3.80 average tool calls, 1,032 test cases, and 34 tools.
- Scenario counts checked from Table 6: 152 Single Tool Call, 656 Multiple Tool Call, 584 Single User Turn, 224 Multiple User Turn, 192 State Dependency, 472 Canonicalization, and 224 Insufficient Information scenarios.
- Main results checked from Table 5: GPT-4o-2024-05-13 scores 73.0 average similarity; Claude-3-Opus-20240229 scores 69.2; GPT-3.5-Turbo-0125 scores 65.6; GPT-4-0125-Preview scores 64.3; Claude-3-Sonnet-20240229 scores 63.8; Hermes-2-Pro-Mistral-7B scores 31.4.
- ReAct appendix checked from Table 9: GPT-4o changes 73.0 to 73.6; Claude-3-Opus 69.2 to 69.3; GPT-4-0125-Preview 64.3 to 65.2; Claude-3-Sonnet 63.8 to 63.7.
- Conflict noted: S06 says tau-bench requires action matching to a single predetermined sequence, while S05 describes final database-state comparison with room for stochastic conversational variation; this was recorded in `wiki/contradiction-register.md`.
- Evidentiary boundary: high-quality public paper, but it is a benchmark paper from Apple authors and its comparisons to prior benchmarks are secondary with respect to those benchmark authors' own descriptions.
