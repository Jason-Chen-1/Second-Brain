---
title: ReAct Reasoning and Acting
page_type: concept
status: draft
updated: 2026-07-09
sources: [S02, S03, S04, S05, S06, S07, S11]
confidence: high
---

# ReAct Reasoning and Acting

## Core Definition

ReAct is a prompting paradigm in which a language model generates verbal reasoning traces and task-specific actions in an interleaved trajectory, so thoughts can guide actions and observations from tools or environments can update later reasoning [S02].

In Yao et al.'s ICLR 2023 paper, ReAct augments an agent's action space with free-form language thoughts that do not directly change the external environment but do update the model's context for later reasoning or acting [S02].

## Key Claims

- ReAct is designed to combine two previously separated capabilities: chain-of-thought style reasoning and action generation for interaction with external sources such as Wikipedia APIs, web environments, or text-game environments [S02].
- For HotpotQA and FEVER, S02 uses a simple Wikipedia API with `search[entity]`, `lookup[string]`, and `finish[answer]` actions, and the authors explicitly state that this API is weaker than state-of-the-art lexical or neural retrievers [S02].
- The main prompting experiments use a frozen PaLM-540B model with few-shot in-context examples; the paper reports additional GPT-3 `text-davinci-002` experiments in an appendix [S02].
- For HotpotQA and FEVER prompts, the authors manually compose ReAct-format trajectories from 6 HotpotQA training cases and 3 FEVER training cases, and report that adding more examples did not improve performance [S02].
- On PaLM-540B prompting, ReAct scores 27.4 exact match on HotpotQA and 60.9 accuracy on FEVER, compared with Act-only scores of 25.7 and 58.9 and chain-of-thought scores of 29.4 and 56.3 [S02].
- Combining ReAct with chain-of-thought self-consistency gives the best reported prompting numbers in Table 1: ReAct to CoT-SC reaches 35.1 exact match on HotpotQA, while CoT-SC to ReAct reaches 64.6 accuracy on FEVER [S02].
- In a manual HotpotQA error analysis, S02 reports that successful ReAct trajectories had a 6% false-positive rate versus 14% for chain-of-thought, while failed ReAct trajectories were attributed to 47% reasoning error, 23% search-result error, and 29% label ambiguity [S02].
- In the same analysis, failed chain-of-thought trajectories were attributed to 56% hallucination, 16% reasoning error, and 28% label ambiguity, which the authors use to argue that ReAct is more grounded but less flexible than pure chain-of-thought [S02].
- On ALFWorld, the best ReAct trial reaches a 71% overall success rate, compared with 45% for the best Act-only trial, 37% for BUTLER, and 53% for the best ReAct-IM ablation [S02].
- On WebShop, ReAct reports a score of 66.6 and a 40.0% success rate, compared with Act-only at 62.3 and 30.1%, imitation learning at 59.9 and 29.1%, imitation learning plus reinforcement learning at 62.4 and 28.7%, and expert humans at 82.1 and 59.6% [S02].
- S02 reports that ReAct outperforms imitation or reinforcement learning baselines on ALFWorld and WebShop by absolute success-rate gains of 34% and 10% while using only one or two in-context examples for those decision-making tasks [S02].

## Evidence and Sources

S02 is a high-quality public paper/PDF in the manifest, dated 2022-10-06 there and published as an ICLR 2023 conference paper in the PDF text [S02].

The paper evaluates ReAct on four main benchmarks: HotpotQA for multi-hop question answering, FEVER for fact verification, ALFWorld for text-based household tasks, and WebShop for webpage navigation and shopping tasks [S02].

S02 reports initial fine-tuning experiments on HotpotQA using 3,000 ReAct-generated correct-answer trajectories to fine-tune PaLM-8B and PaLM-62B models, and it states that fine-tuned ReAct becomes the best of Standard, CoT, Act, and ReAct among those four methods [S02].

The reproducibility statement says the main experiments use PaLM, which was not openly accessible at the time of the paper, and points readers to included prompts, additional GPT-3 experiments, and associated GPT-3 ReAct prompting code [S02].

## Limitations and Counter-Evidence

ReAct prompting is not uniformly better than chain-of-thought: on PaLM-540B HotpotQA, ReAct at 27.4 exact match trails chain-of-thought at 29.4 and CoT-SC at 33.4 before combination with CoT-SC [S02].

The paper reports that ReAct's interleaved thought-action-observation structure can reduce reasoning flexibility, with one common failure mode in which the model repeats previous thoughts and actions instead of recovering [S02].

For ReAct on knowledge-intensive tasks, informative search is critical; S02 attributes 23% of sampled ReAct HotpotQA failures to search results that are empty or do not contain useful information [S02].

The paper states that complex tasks with large action spaces may require more demonstrations than fit comfortably in in-context learning input limits, motivating fine-tuning and higher-quality human annotations as future work [S02].

The ethics statement warns that connecting language models to external action spaces can create risks such as looking up inappropriate or private information or taking harmful actions, and the paper reduces that risk by limiting experiments to constrained Wikipedia, WebShop, and benchmark environments without dangerous actions [S02].

Synthesis: ReAct and Toolformer both address tool use by language models, but ReAct uses prompted interleaving of thoughts, actions, and observations in an environment, while Toolformer fine-tunes a model on self-supervised API-call annotations so it can decide when and how to call tools during generation [S02] [S03].

Synthesis: API-Bank evaluates related tool-use skills at benchmark level by separating API Call, Retrieve+Call, and Plan+Retrieve+Call abilities, whereas ReAct is a prompting paradigm for generating thought-action-observation trajectories [S02] [S04].

Synthesis: Tau-bench evaluates ReAct-style text agents as one method variant in longer tool-agent-user customer-service interactions, and S05 reports that natively supported function calling consistently outperforms text-formatted ReAct and Act-only baselines for the tested state-of-the-art models [S02] [S05].

Synthesis: ToolSandbox's appendix reports that adding ReAct prompting to its default interactive tool-use setup gives small or minimal score changes for four tested models, which S06 attributes to the baseline setup already providing reasoning signals through user and execution-environment interaction [S02] [S06].

Synthesis: AutoGen can embed ReAct-style prompting inside a multi-agent workflow; in S07's ALFWorld application, a two-agent AutoGen system integrates ReAct prompting and matches ReAct at 54% average success, while adding a grounding agent raises average success to 69% [S02] [S07].

Synthesis: ReAct describes a model behavior pattern for interleaving thoughts, actions, and observations, while [[model-context-protocol-architecture|MCP Architecture]] defines an application protocol layer for exchanging tool and context capabilities among hosts, clients, and servers [S02] [S11].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[toolformer-self-supervised-tool-use|Toolformer Self-Supervised Tool Use]]
- [[api-bank-tool-augmented-llm-benchmark|API-Bank Tool-Augmented LLM Benchmark]]
- [[tau-bench-agent-consistency-benchmark|Tau-Bench Agent Consistency Benchmark]]
- [[toolsandbox-stateful-tool-use-benchmark|ToolSandbox Stateful Tool-Use Benchmark]]
- [[autogen-multi-agent-conversation-framework|AutoGen Multi-Agent Conversation Framework]]
- [[model-context-protocol-architecture|Model Context Protocol Architecture]]

## Open Questions

- How should production agents decide when to expose ReAct-style reasoning traces to users, logs, or auditors without leaking sensitive intermediate content source-needed?
- What tool permissioning and sandboxing controls are required before ReAct-style action loops interact with real enterprise systems rather than constrained benchmarks source-needed?
- How well do S02's few-shot ReAct results transfer to smaller, newer, or instruction-tuned models outside PaLM-540B and GPT-3 `text-davinci-002` [S02]?
