# S23 Evidence Notes - Latent Agents

Source ID: S23

Manifest metadata checked: `Latent Agents - Yi, Mueller & Lee`, dated 2026-04-27, file `raw/S23.pdf`, arXiv URL `https://arxiv.org/abs/2604.24881`, type `paper/PDF`, public, quality `medium`, project use `internalized multi-agent debate, token cost, and agent-specific subspaces`.

PDF extraction:

- `raw/S23.pdf` exists and has 34 pages.
- PDF metadata title: `Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate`.
- PDF metadata authors: John Seon Keun Yi, Aaron Mueller, and Dokyun Lee.
- PDF metadata DOI: `https://doi.org/10.48550/arXiv.2604.24881`.
- PDF metadata arXiv ID: `https://arxiv.org/abs/2604.24881v1`.

Core extracted claims used:

- S23 proposes Internalized Multi-Agent Debate (IMAD), a two-stage fine-tuning method that distills multi-agent debate into a single LLM.
- IMAD first uses supervised fine-tuning to replicate debate structure, then uses reinforcement learning with dynamic reward scheduling and length clipping to internalize debate into latent space.
- The training debate dataset contains 944 debate traces from three GPT-3.5-turbo agents over two rounds on arithmetic expressions with six randomly generated two-digit numbers.
- The RL stage uses GRPO, anneals the length limit from 2000 to 500 tokens, decays the structure reward weight from 1.0 to 0.05, and uses LoRA adapters.
- S23 evaluates GSM8K, MMLU-Pro, and Big-Bench Hard with 1000 sampled problems per dataset and mean accuracy with standard error across three runs.
- Table 1 reports LLaMA-3.1 8B IMAD at 85.20% +/- 0.46 on GSM8K, 62.00% +/- 0.93 on MMLU-Pro, and 58.53% +/- 0.76 on BBH, with average token counts 644.33, 728.07, and 562.76.
- Table 1 reports LLaMA-3.1 8B explicit debate at 83.03% +/- 0.55 on GSM8K, 64.60% +/- 0.95 on MMLU-Pro, and 51.06% +/- 1.73 on BBH, with average token counts 5757.78, 8705.32, and 8887.94.
- S23 says IMAD uses 6.3% to 21.1% of explicit debate's tokens across tested models, described as a 5-16x inference-efficiency improvement.
- S23 reports that activation steering finds agent-specific subspaces and gives an average 15.41% steering-alignment improvement across tested conditions for the internalized model.
- S23 reports malicious-trait steering experiments for evil and hallucination traits, with cleaner evil-trait suppression and better GSM8K performance preservation for IMAD than base steering.

Evidentiary boundary:

- S23 is medium-quality paper/PDF evidence for IMAD and latent-agent claims, not production evidence for enterprise auditability or tool-use safety.
- The main debate dataset is arithmetic-only with a fixed three-agent, two-round format.
- The behavioral-control experiment uses LLM-judge trait scores, though S23 reports a human-LLM judge agreement check.
- S23 states that benefits are strongest for models with at least 7B parameters and that smaller models showed limited gains.
