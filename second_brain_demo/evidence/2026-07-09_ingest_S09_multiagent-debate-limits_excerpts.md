# S09 Multiagent Debate Limits Extraction Notes

- Source metadata checked in `raw/source_manifest.md`: S09 is `Can LLM Agents Really Debate? - Wu, Li & Li`, dated 2025-11-11, public, paper/PDF, medium quality, with intended use as a counterpoint to S08 about debate limits and majority pressure.
- PDF extraction used bundled Python with `pdfplumber`; the PDF has 20 pages.
- Title and metadata checked from the PDF: `Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning`; authors Haolun Wu, Zhenkun Li, and Lingyao Li; arXiv ID `2511.07784v1`.
- Core task checked from Sections 3-4: S09 uses Knight-Knave-Spy logic puzzles with knights, knaves, and spies; the debate protocol includes initial proposals, player-by-player debate, self-adjustment, and final decision.
- Controlled factors checked from Table 1: agent team size, team composition, confidence visibility, debate order, debate depth, and task difficulty.
- Anchor configuration checked from Section 5.2: team size 3, Het-MixA composition, hidden confidence, fixed debate order, depth 1, and all task-difficulty levels.
- Experiment size checked from Section 5.2: all controlled experiments use 100 puzzles per configuration across easy, medium, and hard conditions.
- Table 3 checked: strict instance accuracy improves from 17.33% to 69.33% on size-4 puzzles, 6.00% to 46.67% on size-6 puzzles, and 3.33% to 36.00% on size-8 puzzles.
- Table 3 checked: agent-level accuracy improves from 35.33% to 77.11% on size-4 puzzles, 27.11% to 55.56% on size-6 puzzles, and 22.66% to 44.89% on size-8 puzzles.
- Table 4 checked: final smooth accuracy regression has R2 = 0.393 and 745 observations; initial smooth accuracy beta = 0.600 with p < 0.001; number of agents beta = 0.066 with p < 0.001; game size beta = -0.030 with p < 0.001.
- Process findings checked from Section 6.2: majority pressure suppresses independent correction; `gemini-2.5-flash` and `gpt-5-mini` correct incorrect majorities 34.4% and 30.0% of the time, while `gemini-2.5-flash-lite` in Mix A corrects itself only 3.6% of the time.
- Figure 6/prose checked: rational behavior yields correction rates above 90%, while irrational behavior yields rates below 55% despite a noted `gemini-2.5-flash-lite` exception.
- Limitations checked from Section 8: results are limited to Knight-Knave-Spy puzzles, available models, narrow team compositions and protocols, criteria tailored to verifiable logic tasks, and limited analysis of linguistic or rhetorical mechanisms.
- Evidentiary boundary: medium-quality 2025 preprint; useful as a counterpoint to S08, but it qualifies rather than fully supersedes S08 because the task domain and experimental design differ.
