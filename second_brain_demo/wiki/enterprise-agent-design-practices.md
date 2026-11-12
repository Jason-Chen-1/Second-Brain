---
title: Enterprise Agent Design Practices
page_type: concept
status: draft
updated: 2026-07-09
sources: [S02, S07, S12, S13, S15, S17, S21]
confidence: medium
---

# Enterprise Agent Design Practices

## Core Definition

Enterprise agent design practices are pragmatic engineering decisions about when to use agents, how to expose tools, when to choose single-agent versus multi-agent systems, and how to add safeguards such as human escalation and risk-based controls [S17].

S17 is an official OpenAI practice-guide capture from 2025, but the manifest labels it medium quality and the capture cautions that it should be used as practical design guidance rather than as a formal security or authorization specification [S17].

S21 frames reliable enterprise agents around traceable knowledge, explicit permissions, correct tool selection, verifiable state changes, and appropriate human oversight, which provides the project-level scope for this practice page [S21].

## Key Claims

- S17 is titled "A Practical Guide to Building AI Agents," authored by OpenAI, dated 2025, and listed in the manifest as an official practice guide capture with medium quality [S17].
- S17 says the guide gives pragmatic guidance about when to use agents, how to design tools, when to use single versus multi-agent systems, and how to add safeguards [S17].
- S17 supports the argument that multi-agent systems should not be introduced by default [S17].
- S17 helps define human escalation and risk-based safeguards for reliable enterprise agent design [S17].
- S17 provides engineering framing for reliable enterprise agents but is not a formal security or authorization specification [S17].
- S02 shows that ReAct-style agents can interleave reasoning, actions, and observations, but it also warns that connecting language models to external action spaces can create risks from inappropriate lookup or harmful actions [S02].
- S07 shows that multi-agent frameworks can include LLM-backed, human-backed, and tool-backed agents, but it also warns that agent workflows involving code execution or function calls can be risky and require safeguards [S07].
- S13 provides MCP-specific implementation-risk guidance for security boundaries, including session security, least privilege, sandboxing, and token passthrough [S13].
- S15 provides the broader governance frame for generative AI risk management, including incident monitoring, TEVV record retention, system inventory, third-party impact documentation, provenance measurement, and unmeasured-risk documentation [S15].
- S21 says MCP, multi-agent systems, RAG, and LLM Wiki are different enterprise-agent stack layers rather than interchangeable reliability mechanisms [S21].

## Evidence and Sources

The captured S17 source says it should help teams decide when to use agents and how to design tools, which makes it a practice layer above the narrower ReAct prompting pattern and AutoGen framework layer [S02] [S07] [S17].

Synthesis: a single-agent design should remain the default candidate when the task can be handled by one agent with bounded tools and clear safeguards, while multi-agent designs need an additional justification such as distinct roles, human participation, tool execution boundaries, or orchestration needs [S07] [S17].

Synthesis: tool design for enterprise agents should combine S17's practical tool-risk framing with MCP authorization from S12, MCP security controls from S13, and organization-level governance from S15, because tool exposure creates authorization, implementation-security, and governance obligations [S12] [S13] [S15] [S17].

Synthesis: human escalation belongs in enterprise agent design when risk, ambiguity, or side effects exceed the agent's allowed autonomy; S17 names human escalation and risk-based safeguards, S07 provides a framework example with human-backed agents, and S15 provides governance categories for incident response and oversight [S07] [S15] [S17].

Synthesis: S21 turns the design question from "can the model answer?" into "can the system cite evidence, prove authorization, choose tools correctly, verify state changes, and support oversight?" [S17] [S21].

## Limitations and Counter-Evidence

S17 is a medium-quality official practice guide capture rather than a benchmark, specification, or full source-body extraction, so it should not independently support numerical performance claims, protocol requirements, or security controls [S17].

S17 should not override MCP authorization or security sources, because the capture explicitly says to use it as practical design guidance rather than a formal security or authorization specification [S12] [S13] [S17].

S17's captured source does not provide detailed criteria for choosing single-agent versus multi-agent architectures, so specific thresholds for cost, latency, reliability, or task complexity remain `source-needed` [S17].

S17's captured source does not provide detailed human-escalation procedures, so escalation triggers, approval records, and rollback plans must be sourced from future practice guides or internal policy before being treated as requirements [S17].

S21 is an AI-assisted project note requiring student review, so its project framing should be treated as scope and hypotheses rather than final validated design guidance [S21].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[react-reasoning-and-acting|ReAct Reasoning and Acting]]
- [[autogen-multi-agent-conversation-framework|AutoGen Multi-Agent Conversation Framework]]
- [[model-context-protocol-authorization|Model Context Protocol Authorization]]
- [[model-context-protocol-security-best-practices|Model Context Protocol Security Best Practices]]
- [[generative-ai-risk-governance|Generative AI Risk Governance]]
- [[project-scope-and-research-hypotheses|Project Scope and Research Hypotheses]]

## Open Questions

- What concrete decision rubric should choose single-agent, multi-agent, or ordinary workflow automation for a given enterprise task source-needed?
- Which tool-risk levels require human approval before execution source-needed?
- What audit record is sufficient for human escalation, override, and rollback in a tool-using agent workflow source-needed?
