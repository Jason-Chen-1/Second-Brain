---
title: ToolSandbox Stateful Tool-Use Benchmark
page_type: concept
status: draft
updated: 2026-07-11
sources: [S04, S05, S06, S07]
confidence: high
---

# ToolSandbox Stateful Tool-Use Benchmark

## Core Definition

ToolSandbox is a Python-native benchmark for evaluating LLM tool-use agents in stateful, conversational, and interactive settings with mutable world state, a simulated user, and tool execution through an execution environment [S06].

The benchmark evaluates trajectories with human-authored Milestones and Minefields: Milestones define key events that must occur in a trajectory, while Minefields define events that must not occur, such as hallucinated tool calls in insufficient-information scenarios [S06].

## Key Claims

- S06 argues that prior tool-use benchmarks often evaluate stateless web services from a single-turn prompt or evaluate predefined off-policy dialogue trajectories, while real task-oriented tool use is stateful, conversational, and interactive [S06].
- ToolSandbox represents mutable state with an `ExecutionContext`, tools as Python functions, and role communication among User, Agent, and Execution Environment through a `MessageBus` [S06].
- Stateful tools in ToolSandbox inspect, depend on, or manipulate world states such as cellular service, Wi-Fi, location service, and low-battery mode [S06].
- Stateful tools make up 44% of the ToolSandbox toolbox, and their implicit dependencies test whether an agent can track world state and tool-call stack effects [S06].
- ToolSandbox uses a GPT-4o-powered user simulator for on-policy conversational rollouts, and the simulator can terminate with an `end_conversation` tool when it judges the task complete or impossible [S06].
- The paper reports that adding Knowledge Boundary and Demonstration prompt components to the user simulator reduced hallucination from 12.4% to 6.97% and instruction-following error from 6.20% to 0.77% in a GPT-4o simulator/GPT-4o agent setup over 1,032 manually annotated trajectories [S06].
- ToolSandbox contains 1,032 test scenarios, 34 tools, an average of 13.9 turns, and an average of 3.80 tool calls, compared in Table 4 with API-Bank at 261 test cases, 73 tools, 3.88 average turns, and 2.04 average tool calls [S06].
- The 34 tools cover 11 domains: Contact, Messaging, Reminder, System settings, Time utilities, Math utilities, Map, Weather, Stock, Conversion, and Holiday [S06].
- ToolSandbox scenario counts include 152 Single Tool Call, 656 Multiple Tool Call, 584 Single User Turn, 224 Multiple User Turn, 192 State Dependency, 472 Canonicalization, and 224 Insufficient Information scenarios; a scenario can belong to multiple categories [S06].
- S06 states that 85% of ToolSandbox scenarios are associated with at least one difficult category among Multiple Tool Call, Multiple User Turn, State Dependency, and Insufficient Information [S06].
- In Table 5, `GPT-4o-2024-05-13` has the highest average similarity score at 73.0, followed by `Claude-3-Opus-20240229` at 69.2, `GPT-3.5-Turbo-0125` at 65.6, `GPT-4-0125-Preview` at 64.3, and `Claude-3-Sonnet-20240229` at 63.8 [S06].
- In Table 5, the best open-source model listed by the authors, `Hermes-2-Pro-Mistral-7B`, scores 31.4 average similarity, more than 20 points below `Claude-3-Haiku-20240307` at 54.9 [S06].
- The Insufficient Information category has an inverse pattern in Table 5: `Mistral-7B-Instruct-v0.3` scores 76.8 and `Gemini-1.5-Pro-001` scores 76.2, while `GPT-4o-2024-05-13` scores 42.0 and `GPT-3.5-Turbo-0125` scores 22.3; S06 interprets some high scores from weaker models as a side effect of not issuing tool calls rather than a generally positive outcome [S06].
- The State Dependency category shows an unusual pattern where larger models such as GPT-4 and Claude-3-Opus can perform worse than smaller models because they may issue erroneous parallel tool calls when tools are dependent [S06].
- A ReAct prompting appendix reports small or minimal gains over the default ToolSandbox prompt: GPT-4o rises from 73.0 to 73.6, Claude-3-Opus from 69.2 to 69.3, GPT-4-0125-Preview from 64.3 to 65.2, and Claude-3-Sonnet from 63.8 to 63.7 [S06].

## Evidence and Sources

S06 is a high-quality public paper/PDF in the manifest, dated 2024-08-08, with intended use for stateful, multi-turn, insufficient-information tool evaluation [S06].

The ToolSandbox evaluation strategy maps Milestones to trajectory snapshots while preserving a topological ordering over milestone dependencies, allowing multiple valid trajectories to satisfy the same task [S06].

ToolSandbox uses Minefields to penalize trajectories that take forbidden actions; the paper gives an insufficient-information example where a task lacks the current timestamp and the model should not call `timestamp_diff` with a hallucinated argument [S06].

Synthesis: ToolSandbox complements [[api-bank-tool-augmented-llm-benchmark|API-Bank]] by moving from executable API-call evaluation toward mutable world-state evaluation with dynamic trajectories, simulated users, and intermediate milestone checks [S04] [S06].

Synthesis: ToolSandbox and [[tau-bench-agent-consistency-benchmark|Tau-Bench]] both evaluate conversational tool-use agents, but ToolSandbox emphasizes state dependencies, minefields for impossible tasks, and milestone scoring over arbitrary trajectories, while tau-bench emphasizes domain-policy following and repeated-trial `pass^k` reliability [S05] [S06].

Synthesis: ToolSandbox is an evaluation benchmark for stateful conversational tool use, while [[autogen-multi-agent-conversation-framework|AutoGen]] is a framework for constructing multi-agent conversations with LLM, human, and tool-backed agents [S06] [S07].

## Limitations and Counter-Evidence

S06 states that authoring Milestones and Minefields requires deep knowledge of tool capacities and many iterations, which hinders scalability [S06].

S06 reports that its user simulator still has non-negligible hallucination and instruction-following errors despite prompt controls [S06].

Mandatory confirmation and authentication are not addressed in ToolSandbox, even though the paper identifies them as important for tool-use LLM designs and transactional services [S06].

ToolSandbox does not currently address daemon-style tools such as timers, where a tool returns after spawning a background process that later interrupts the main process [S06].

Some ToolSandbox tools depend on external web services, such as weather search, and S06 says this can affect reproducibility [S06].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[api-bank-tool-augmented-llm-benchmark|API-Bank Tool-Augmented LLM Benchmark]]
- [[tau-bench-agent-consistency-benchmark|Tau-Bench Agent Consistency Benchmark]]
- [[react-reasoning-and-acting|ReAct Reasoning and Acting]]
- [[autogen-multi-agent-conversation-framework|AutoGen Multi-Agent Conversation Framework]]
- [[contradiction-register|Contradiction Register]]

## Open Questions

- How should ToolSandbox-style milestone and minefield authoring be scaled without losing the interpretability of human-authored intermediate checks source-needed?
- How should stateful tool benchmarks model confirmation, authentication, and permission boundaries before write actions in enterprise systems source-needed?
- How stable are ToolSandbox scores when external-service-backed tools are cached or replaced by deterministic local fixtures [S06]?
