---
title: Contradiction Register
page_type: register
status: draft
updated: 2026-07-09
sources: [S01, S05, S06, S08, S09, S10, S20]
confidence: mixed
---

# Contradiction Register

## Tau-Bench Evaluation Flexibility

Claim A: The tau-bench paper says its evaluation compares the database state at the end of each episode with the ground-truth expected state, which allows stochastic conversational variation so long as different conversations reach the same end database state [S05].

Claim B: The ToolSandbox paper says tau-bench requires agent action to match a single predetermined sequence, leaving no room for error correction or multiple possible answer sequences [S06].

Applicability: Claim A is from the primary tau-bench source, while Claim B is from a later benchmark-comparison passage in ToolSandbox rather than tau-bench itself [S05] [S06].

Status: Open, leaning toward S05 for tau-bench's own evaluation design because S05 is the primary source and describes final-state database comparison, but S06's critique should be preserved as an external benchmark-comparison claim until a direct reconciliation is available [S05] [S06].

Related pages: [[tau-bench-agent-consistency-benchmark|Tau-Bench Agent Consistency Benchmark]], [[toolsandbox-stateful-tool-use-benchmark|ToolSandbox Stateful Tool-Use Benchmark]].

## Multiagent Debate Benefit Versus Majority Pressure

Claim A: The S08 multiagent debate paper reports that debate improves over single-agent, reflection, and majority-voting baselines on arithmetic, GSM8K, chess move prediction, biographies, MMLU, and chess move validity, and frames debate as a black-box way for language-model agents to critique and refine one another's answers [S08].

Claim B: The S09 controlled study reports that multi-agent debate can improve Knight-Knave-Spy logic-puzzle accuracy, but argues that debate success is primarily driven by intrinsic reasoning strength and diversity, while structural parameters such as debate depth, order, and confidence visibility offer limited gains and majority pressure can suppress independent correction [S09].

Applicability: Claim A covers broad positive empirical results across S08's benchmark families, while Claim B comes from a later controlled logic-puzzle setting designed to distinguish outcome gains from debate-process quality [S08] [S09].

Status: Open; S09 qualifies but does not fully supersede S08 because the tasks, models, dates, and evaluation designs differ, and S09 still reports accuracy gains while narrowing the interpretation of what those gains mean [S08] [S09].

Related pages: [[multiagent-debate-for-factuality-and-reasoning|Multiagent Debate for Factuality and Reasoning]].

## LLM Wiki Replacement Versus RAG Complement

Claim A: S10 defines LLM Wiki as a persistent Markdown knowledge-base pattern with raw sources, generated wiki pages, schema files, and ingest/query/lint workflows, which positions it as a knowledge-base maintenance workflow rather than the same model architecture as RAG [S10].

Claim B: S20 is a low-quality critique/opinion capture that is included for a skeptical view of LLM Wiki and especially for the claim that LLM Wiki should complement rather than replace RAG [S20].

Applicability: Claim A is the medium-quality original concept source for this project's LLM Wiki vocabulary, while Claim B is a low-quality opinion source useful for stress-testing replacement claims but not for independently settling whether LLM Wiki or RAG is preferable [S10] [S20].

Status: Open as a design tension rather than a resolved contradiction; current synthesis keeps RAG and LLM Wiki at different layers because S01 defines RAG as a retriever-generator model architecture and S10 defines LLM Wiki as a persistent Markdown maintenance workflow, while S20 warns against overconfident replacement claims [S01] [S10] [S20].

Related pages: [[llm-wiki|LLM Wiki]], [[retrieval-augmented-generation|Retrieval-Augmented Generation]].
