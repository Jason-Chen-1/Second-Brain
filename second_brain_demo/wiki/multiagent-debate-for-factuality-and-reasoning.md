---
title: Multiagent Debate for Factuality and Reasoning
page_type: concept
status: draft
updated: 2026-07-11
sources: [S07, S08, S09, S21, S23]
confidence: mixed
---

# Multiagent Debate for Factuality and Reasoning

## Core Definition

Multiagent debate is a language-generation procedure in which multiple LLM instances independently propose answers, read the other agents' answers, update their own answers over multiple rounds, and converge toward a shared final answer [S08].

Du et al. present multiagent debate as a black-box method: it requires only access to model generations, not model likelihoods, gradients, or internal state [S08].

S09 studies multi-agent debate in a controlled Knight-Knave-Spy logic-puzzle environment, where agents make initial proposals, debate one player at a time, self-adjust, and then output final role assignments that are aggregated by majority vote with a supervisor tie-breaker if needed [S09].

S23 studies Internalized Multi-Agent Debate, which distills multi-agent debate traces into a single LLM to reduce inference-time token cost while trying to preserve debate-like reasoning behavior [S23].

## Key Claims

- S08 positions debate as complementary to single-model prompting methods such as chain-of-thought, verification, self-consistency, and scratchpads [S08].
- In the S08 protocol, each agent first answers a query independently; then each agent receives the other agents' responses in a consensus prompt and is asked to update its answer, with this process repeated for multiple debate rounds [S08].
- S08 reports that language-model agents empirically converge to a single shared answer after multiple debate rounds, but it explicitly states that convergence is not guaranteed because debate can be viewed as a multi-agent game [S08].
- The paper says prompts that make agents more "stubborn" about their own solutions can induce longer debates and better final solutions, while agents are often relatively agreeable, possibly because of instruction tuning or RLHF [S08].
- Most S08 benchmark experiments use three agents and two debate rounds because of computational expense, though the paper reports additional gains from more agents and rounds in Figure 10 [S08].
- The main experiments use `gpt-3.5-turbo-0301`, and S08 combines debate with zero-shot chain-of-thought prompting in its evaluations [S08].
- In Table 1, multiagent debate scores 81.8% +/- 2.3 on arithmetic, compared with 67.0% +/- 4.7 for a single agent, 72.1% +/- 4.5 for single-agent reflection, and 69.0% +/- 4.6 for multi-agent majority voting [S08].
- In Table 1, multiagent debate scores 85.0% +/- 3.5 on GSM8K grade-school math, compared with 77.0% +/- 4.2 for a single agent, 75.0% +/- 4.3 for single-agent reflection, and 81.0% +/- 3.9 for multi-agent majority voting [S08].
- In Table 1, multiagent debate scores 122.9 +/- 7.6 on chess move prediction measured by Stockfish pawn score, compared with 91.4 +/- 10.6 for a single agent, 102.1 +/- 11.9 for single-agent reflection, and 102.2 +/- 6.2 for multi-agent majority voting [S08].
- In Table 2, multiagent debate scores 73.8% +/- 2.3 on the biography factuality benchmark, 71.1% +/- 4.6 on MMLU, and 45.2% +/- 2.9 on chess move validity [S08].
- In Table 2, single-agent baselines score 66.0% +/- 2.2 on biographies, 63.9% +/- 4.8 on MMLU, and 29.3% +/- 2.6 on chess move validity, while single-agent reflection scores 68.3% +/- 2.9, 57.7% +/- 5.0, and 38.8% +/- 2.9 respectively [S08].
- S08 introduces a biography factuality benchmark for famous computer scientists and says contemporary language models often hallucinate institutions and dates in generated biographies [S08].
- The paper reports that, on 20 GSM8K problems debated between ChatGPT and Bard, Bard solves 11, ChatGPT solves 14, and joint multiagent debate solves 17 [S08].
- The appendix says the arithmetic evaluation uses 100 generated arithmetic tasks, GSM8K uses 100 grade-school math problems, chess move prediction uses 300 selected chess games, MMLU uses 100 selected questions, and chess validity uses 100 selected BIG-Bench chess-state-tracking tasks [S08].
- S09 frames the open question as whether multi-agent debate gains reflect genuine deliberative reasoning rather than ensembling or majority voting, and it evaluates both debate outcomes and debate process quality [S09].
- S09 varies six factors: agent team size, agent team composition, confidence visibility, debate order, debate depth, and task difficulty [S09].
- In S09's default anchor configuration, agent team size is 3, composition is Het-MixA, confidence visibility is hidden, debate order is fixed, debate depth is 1, and task difficulty spans all levels [S09].
- S09 says all controlled experiments use 100 puzzles per configuration across easy, medium, and hard conditions [S09].
- In S09 Table 3, debate improves strict instance accuracy from 17.33% to 69.33% on size-4 puzzles, from 6.00% to 46.67% on size-6 puzzles, and from 3.33% to 36.00% on size-8 puzzles [S09].
- In S09 Table 3, debate improves agent-level accuracy from 35.33% to 77.11% on size-4 puzzles, from 27.11% to 55.56% on size-6 puzzles, and from 22.66% to 44.89% on size-8 puzzles [S09].
- S09 reports that initial smooth accuracy is the strongest predictor of final smooth accuracy in its regression, with beta = 0.600, p < 0.001, R2 = 0.393, and 745 observations [S09].
- S09 reports that number of agents positively predicts final smooth accuracy with beta = 0.066 and p < 0.001, while game size negatively predicts final smooth accuracy with beta = -0.030 and p < 0.001 [S09].
- S09 reports that debate depth, confidence visibility, and debate order are not significant predictors in its final-output-accuracy regression [S09].
- S09 finds that majority pressure can suppress independent correction: stronger models such as `gemini-2.5-flash` and `gpt-5-mini` corrected an incorrect majority 34.4% and 30.0% of the time, while `gemini-2.5-flash-lite` in Mix A corrected itself only 3.6% of the time in such cases [S09].
- S09 reports that rational, validity-aligned behavior produced correction rates above 90%, while irrational behavior produced correction rates below 55% despite the `gemini-2.5-flash-lite` exception noted in the paper [S09].
- S23 reports that IMAD uses between 6.3% and 21.1% of explicit debate's tokens across tested models while matching or improving debate performance on several model/benchmark combinations [S23].
- S23 reports that LLaMA-3.1 8B IMAD scores 85.20% +/- 0.46 on GSM8K and consumes 644.33 average tokens, compared with 83.03% +/- 0.55 and 5757.78 average tokens for explicit debate [S23].

## Evidence and Sources

S08 is a medium-quality public paper/PDF in the manifest, dated 2023-05-23, with intended use as the positive claim that debate improves factuality [S08].

S09 is a medium-quality public paper/PDF in the manifest, dated 2025-11-11, with intended use as a counterpoint to S08 about debate limits and majority pressure [S09].

The paper evaluates debate on six task families: arithmetic, GSM8K grade-school math, chess move prediction, biographies, MMLU, and chess move validity [S08].

The biography factuality metric compares generated biography bullets against Wikipedia-derived ground-truth facts by prompting ChatGPT to judge consistency as `yes`, `no`, or `uncertain`, and the authors ignore ground-truth bullets labeled `uncertain` [S08].

S09 uses Knight-Knave-Spy puzzles because they provide structured logical reasoning tasks with verifiable ground truth and stepwise intermediate debate decisions [S09].

Synthesis: Multiagent debate is a specific multi-agent inference pattern, while [[autogen-multi-agent-conversation-framework|AutoGen]] is a general framework that can implement many multi-agent conversation patterns, including debate-like interactions [S07] [S08].

Synthesis: S08 supports multiagent debate as a useful black-box inference procedure, while S09 narrows that claim by showing that controlled logic-task gains are strongly bounded by participant reasoning strength, diversity, and ability to resist incorrect majorities [S08] [S09].

Synthesis: [[latent-agents-internalized-debate|Latent Agents and Internalized Multi-Agent Debate]] reframes debate as a training signal that may be internalized into one model, while S08 and S09 evaluate explicit multi-agent interaction at inference time [S08] [S09] [S23].

## Limitations and Counter-Evidence

S08 states that multiagent debate is more computationally expensive than other prompting techniques because it requires multiple language generations and multiple debate rounds [S08].

S08 reports that, as debates become longer, current language models sometimes struggle to process the full debate input and focus mostly on recent generations [S08].

The paper states that debate consensus can still be wrong: agents may converge to a single incorrect answer and confidently affirm that it is correct and consistent with other agents' responses [S08].

S08's biography evaluation can miss incorrect generated facts if those facts are not covered by the ground-truth bullet set, so the authors describe the metric as estimating relative accuracy rather than fully validating biographies [S08].

S08 is a preprint/framework-style empirical paper rather than a peer-reviewed benchmark standard in the manifest, so its results should be treated as medium-confidence positive evidence pending later counter-evidence [S08].

S09 is also medium-quality preprint evidence in the manifest, so its negative and qualifying claims should update confidence but not be treated as final consensus [S09].

S09 limits its study to Knight-Knave-Spy logic puzzles, and the authors state that this structured domain may not capture open-ended reasoning, creative problem-solving, commonsense tasks, or tasks with multiple valid solutions [S09].

S09 says its analysis is limited to the LLMs available at the time of study, a narrow range of team compositions and debate protocols, and criteria tailored to logical reasoning with verifiable ground truth [S09].

S09 reports that weaker teams can converge prematurely or follow persuasive but unsound reasoning, and that coordination mechanisms alone cannot overcome weak reasoning foundations [S09].

S23 reduces explicit debate's token cost but also removes the full visible debate transcript at inference time, so its enterprise auditability implications remain unresolved [S21] [S23].

S23's main debate dataset is limited to arithmetic problems and a fixed three-agent, two-round debate format, so its internalization results should not be treated as a general replacement for explicit debate on long-context or tool-using tasks [S23].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[autogen-multi-agent-conversation-framework|AutoGen Multi-Agent Conversation Framework]]
- [[latent-agents-internalized-debate|Latent Agents and Internalized Multi-Agent Debate]]
- [[contradiction-register|Contradiction Register]]

## Open Questions

- Which debate failures are caused by shared model biases versus poor debate prompts or insufficient agent diversity source-needed?
- When does the extra cost of multiagent debate justify itself compared with self-consistency, retrieval, verification, or tool execution source-needed?
- How far do S09's Knight-Knave-Spy results transfer to S08's factuality, math, chess, and MMLU settings source-needed?
- When does internalized debate preserve enough of explicit debate's correction behavior to justify losing a visible debate transcript [S23]?
