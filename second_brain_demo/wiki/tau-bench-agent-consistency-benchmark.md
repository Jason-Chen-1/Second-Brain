---
title: Tau-Bench Agent Consistency Benchmark
page_type: concept
status: draft
updated: 2026-07-11
sources: [S02, S04, S05, S06]
confidence: mixed
---

# Tau-Bench Agent Consistency Benchmark

## Core Definition

Tau-bench is a benchmark for Tool-Agent-User interaction that evaluates whether language agents can converse with simulated users, use domain API tools, follow domain-specific policy documents, and reach the correct final database state in realistic customer-service tasks [S05].

The benchmark introduces `pass^k` as a reliability metric: unlike `pass@k`, which credits at least one success among `k` independent trials, `pass^k` measures the chance that all `k` independent trials of the same task succeed, averaged across tasks [S05].

## Key Claims

- Tau-bench argues that many prior language-agent benchmarks provide all information upfront and do not test sustained human interaction or domain-policy adherence, both of which are important for real deployments [S05].
- A tau-bench task is formulated as interaction with two external state sources: databases through API tools and a simulated user through natural language dialogue [S05].
- The benchmark uses domain-specific policy documents as part of the agent context, and some policy restrictions are not enforced by the API, so the agent must reason over the policy before acting [S05].
- The simulated user is implemented with `gpt-4-0613`; the user can see the user-agent conversation history but not the agent-tool interaction history [S05].
- A task instance contains a hidden user instruction plus a ground-truth annotation of expected database write actions and, when relevant, required output substrings for user-facing answers [S05].
- Episode reward is binary and equals `r_action * r_output`, where `r_action` checks whether the final database matches the unique ground-truth database outcome and `r_output` checks whether necessary information was provided to the user [S05].
- Tau-bench's first release focuses on two customer-service domains, `tau-retail` and `tau-airline`, chosen because they support synthetic but realistic products, prices, flights, policies, and diverse user tasks [S05].
- `tau-retail` contains 500 users, 50 products, 1,000 orders, 7 write APIs, 8 non-write APIs, and 115 tasks [S05].
- `tau-airline` contains 500 users, 300 flights, 2,000 reservations, 6 write APIs, 7 non-write APIs, and 50 tasks [S05].
- The paper reports main results over at least 3 trials per task, with agent language-model temperature set to `0.0`, simulated-user temperature set to `1.0`, and each task limited to at most 30 agent actions [S05].
- In Table 2, function-calling `gpt-4o` scores 61.2 `pass^1` on retail, 35.2 on airline, and 48.2 average; `gpt-4-turbo` scores 57.7, 32.4, and 45.1; `claude-3-opus` scores 44.2, 34.7, and 39.5; and `meta-llama-3-70B` scores 14.8, 14.4, and 14.6 using text ReAct rather than function calling [S05].
- The paper highlights consistency failure: even the best reported `gpt-4o` function-calling agent has more than 60% average retail task success at `pass^1`, but its retail `pass^8` drops below 25% [S05].
- In tau-retail failure analysis for 115 one-trial `gpt-4o` function-calling trajectories, 40 tasks initially failed, 4 failures were attributed to user-instruction typo or ambiguity and fixed, and the remaining 36 agent issues were broken down into wrong argument or information, wrong decision-making, and partial resolution of compound requests [S05].
- Removing the domain policy from the function-calling system prompt degrades `gpt-4o` `pass^1` from 61.2 to 56.8 on retail and from 33.2 to 10.8 on airline, which the authors interpret as showing that airline's more ad-hoc rules require policy use more strongly [S05].

## Evidence and Sources

S05 is a high-quality public paper/PDF in the manifest, dated 2024-06-17, with intended use for enterprise-agent consistency and `pass^k` metrics [S05].

The paper describes a three-stage construction process: manual database-schema, API, and policy design; LM-assisted data generation using GPT-4-generated and human-polished code; and manual task annotation plus validation through agent runs to reduce ambiguity in user instructions [S05].

The domain APIs include both read and write tools; the appendix lists retail read APIs such as `find_user_id_by_email`, `get_order_details`, and `get_user_details`, plus retail write APIs such as `cancel_pending_order`, `modify_pending_order_items`, and `return_delivered_order_items` [S05].

The paper reports that a `gpt-4o` function-calling agent paired with GPT-4 user simulation on `tau-retail` costs about `$0.38` per task for the agent and `$0.23` per task for the user simulation, and says one trial per task costs around `$200` [S05].

Synthesis: Tau-bench extends the benchmark picture beyond API-call correctness by evaluating longer user-agent-tool trajectories, final database state, policy following, and repeated-trial reliability, while [[api-bank-tool-augmented-llm-benchmark|API-Bank]] evaluates API calling, retrieval, and planning over tool-use dialogues and executable APIs [S04] [S05].

Synthesis: Tau-bench can evaluate [[react-reasoning-and-acting|ReAct]]-style text agents as a method variant, but S05 reports that natively supported function calling consistently outperforms text-formatted ReAct and Act-only baselines for the tested state-of-the-art models [S02] [S05].

Synthesis: [[toolsandbox-stateful-tool-use-benchmark|ToolSandbox]] and tau-bench both evaluate conversational tool-use agents, but S06 emphasizes state dependencies, minefields, and milestone scoring over arbitrary trajectories, while S05 emphasizes domain policies, final database-state comparison, and repeated-trial `pass^k` reliability [S05] [S06].

## Limitations and Counter-Evidence

The benchmark uses synthetic customer-service data and LM-simulated users; S05 states that user instructions can contain typos or ambiguity, user simulations may lack all domain knowledge, and the user-simulation LM can have reasoning, calculation, long-context, or instruction-following limits [S05].

Tau-bench's first demonstration covers only retail and airline domains; the authors identify more complex domains such as medical, tax, or legal as future directions for more capable agents [S05].

The authors note that the manual annotation process is difficult, requires deep understanding of both the domain and agent capabilities, and may include implicit bias because `gpt-4-turbo` function-calling runs were used to tune user prompts during curation [S05].

The reward is fast and objective but imperfect: the paper notes that a correct final database state can be necessary but not sufficient for success if, for example, an agent performs a return without explicit user confirmation, violating the domain policy [S05].

Contradiction: S05 describes tau-bench as comparing final database state with an expected state while allowing stochastic conversational variation, but S06 characterizes tau-bench as requiring action matching to a single predetermined sequence; this is preserved in [[contradiction-register|Contradiction Register]] [S05] [S06].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[react-reasoning-and-acting|ReAct Reasoning and Acting]]
- [[api-bank-tool-augmented-llm-benchmark|API-Bank Tool-Augmented LLM Benchmark]]
- [[toolsandbox-stateful-tool-use-benchmark|ToolSandbox Stateful Tool-Use Benchmark]]
- [[contradiction-register|Contradiction Register]]

## Open Questions

- How should `pass^k` be interpreted for production agent launch criteria when the acceptable failure rate differs by domain, customer impact, and reversibility of database writes source-needed?
- Can tau-bench-style final-state evaluation be extended to real enterprise tools where executing failed write actions may be unsafe or irreversible source-needed?
- How much do S05's function-calling versus ReAct conclusions change for later models, stricter tool schemas, or agent scaffolds that were not tested in the 2024 paper [S05]?
