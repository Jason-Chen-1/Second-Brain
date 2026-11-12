# S08 Multiagent Debate Extraction Notes

- Source metadata checked in `raw/source_manifest.md`: S08 is `Improving Factuality and Reasoning through Multiagent Debate - Du et al.`, dated 2023-05-23, public, paper/PDF, medium quality, with intended use as the positive claim that debate improves factuality.
- PDF extraction used bundled Python with `pdfplumber`; the PDF has 27 pages.
- Core protocol checked from Sections 1-2: multiple LLM instances answer independently, then receive other agents' answers in a consensus prompt and update answers over repeated rounds.
- Experimental defaults checked from Section 3 and appendix: most evaluations use three agents and two rounds because of compute cost; experiments use `gpt-3.5-turbo-0301`; zero-shot chain-of-thought is applied in evaluations.
- Reasoning results checked from Table 1: debate scores 81.8 +/- 2.3 on arithmetic, 85.0 +/- 3.5 on GSM8K, and 122.9 +/- 7.6 on chess pawn score.
- Factuality results checked from Table 2: debate scores 73.8 +/- 2.3 on biographies, 71.1 +/- 4.6 on MMLU, and 45.2 +/- 2.9 on chess move validity.
- Dataset sizes checked from Appendix A.2: arithmetic 100 generated tasks, GSM8K 100 problems, chess move prediction 300 selected games, MMLU 100 selected questions, chess validity 100 selected tasks.
- Mixed-model result checked from Figure 11/prose: on 20 GSM8K problems with ChatGPT and Bard, Bard solves 11, ChatGPT solves 14, and joint debate solves 17.
- Limitations checked from Section 5 and Appendix A.2: debate is computationally expensive, long debate input can exceed model attention/usefulness, consensus can be confidently wrong, and biography evaluation can miss unsupported generated facts not represented in the ground-truth bullets.
- Evidentiary boundary: medium-quality preprint; it is positive evidence for debate but not final consensus, especially because S09 is explicitly listed in the manifest as a future counterpoint source.
