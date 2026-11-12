# S03 Ingest Evidence Notes

Source: S03, `raw/S03.pdf`, "Toolformer: Language Models Can Teach Themselves to Use Tools" by Schick et al., manifest date 2023-02-09.

Verification notes:

- PDF extraction reported 17 pages.
- Manifest labels S03 as a public, high-quality paper/PDF intended for when and how models choose tools.
- Method checked: sample candidate API calls, execute calls, filter by future-token loss reduction, and fine-tune GPT-J on API-augmented CCNet text.
- Tool inventory checked: question answering with Atlas, BM25 Wikipedia search over KILT Wikipedia, calculator with four arithmetic operations and two-decimal rounding, NLLB 600M machine translation into English, and calendar returning current date.
- Dataset/counts checked from Table 2 for `tau_f = 1.0`: QA 18,526; Wikipedia Search 60,974; Calculator 994; Calendar 20,587; Machine Translation 1,034.
- Training details checked from main text and Appendix B: GPT-J 6.7B base, batch size 128, learning rate `1e-5`, 10% warmup, up to 25,000 examples per API, max sequence length 1,024, DeepSpeed ZeRO-3, 8 NVIDIA A100 40GB GPUs, BF16.
- Benchmark numbers checked from Tables 3-8: LAMA, math, QA, MLQA, temporal datasets, and language-modeling perplexity.
- Limitations checked from Section 7: no chained tool use, no interactive search/query refinement, input-wording sensitivity, sample inefficiency, and no tool-cost awareness.
- Relationship checked against existing S02 ReAct page: Toolformer and ReAct both concern tool use, but S03 uses self-supervised fine-tuning for API insertion while S02 uses prompted thought/action/observation trajectories.

No contradiction with existing S01 or S02 pages was detected; S03 adds a distinct self-supervised tool-use learning mechanism.
