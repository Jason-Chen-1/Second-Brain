---
title: Generative AI Risk Governance
page_type: concept
status: draft
updated: 2026-07-09
sources: [S04, S05, S06, S13, S15, S21]
confidence: high
---

# Generative AI Risk Governance

## Core Definition

Generative AI risk governance is the organizational practice of using NIST AI 600-1, a July 2024 cross-sectoral profile and companion resource to AI RMF 1.0, to identify and manage risks that are novel to or exacerbated by generative AI systems [S15].

S15 treats the AI RMF profile as an implementation of AI RMF functions, categories, and subcategories for the generative AI technology setting, based on the framework user's requirements, risk tolerance, and resources [S15].

S21 supplies this project's reliability framing, where traceable knowledge, explicit permissions, verifiable state changes, and human oversight are part of the system-level target rather than optional documentation [S21].

## Key Claims

- NIST AI 600-1 is titled "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile," was approved by the NIST Editorial Review Board on 2024-07-25, and is listed in the manifest as a high-quality official report with publication date 2024-07-26 [S15].
- S15 says AI RMF 1.0 was released in January 2023 and is intended for voluntary use to help organizations incorporate trustworthiness considerations into AI design, development, use, and evaluation [S15].
- S15 defines the document as a cross-sectoral AI RMF profile for generative AI, including common activities or business processes such as large language models, cloud-based services, and acquisition [S15].
- S15 states that suggested actions are organized under AI RMF functions tagged as `GV` for Govern, `MP` for Map, `MS` for Measure, and `MG` for Manage [S15].
- S15 lists 12 risk categories for generative AI: CBRN information or capabilities, confabulation, dangerous/violent/hateful content, data privacy, environmental impacts, harmful bias or homogenization, human-AI configuration, information integrity, information security, intellectual property, obscene/degrading/abusive content, and value chain and component integration [S15].
- S15 says the Generative AI Public Working Group focused on four primary considerations: governance, content provenance, pre-deployment testing, and incident disclosure [S15].
- S15 says the suggested actions primarily address those four considerations and that future revisions will include additional AI RMF subcategories, risks, and suggested actions as the space evolves and empirical evidence indicates additional risks [S15].
- S15 says not every AI RMF subcategory is included and not every suggested action applies to every AI actor or AI actor task [S15].

## Evidence and Sources

S15 describes risk in the AI RMF context as a composite of likelihood and consequence, and it notes that some risks are empirically demonstrated in similar contexts while others may be unlikely, speculative, or uncertain in a given context [S15].

S15 says generative AI risks vary by lifecycle stage, scope, source of risk, and time scale, including design, development, deployment, operation, and decommissioning stages; individual-system, application, and ecosystem scopes; model, input, output, and human-behavior sources; and abrupt or extended materialization timelines [S15].

S15 recommends organizational responsibilities for periodic review of content provenance and incident monitoring, after-action reviews for generative AI incident response and disclosure, and document-retention policies for TEVV and digital-content transparency history [S15].

S15 recommends inventorying organizational generative AI systems and considering provenance, known issues, oversight roles, intellectual-property and sensitive-data considerations, foundation models, model versions, and access modes in inventory entries [S15].

S15 recommends documenting downstream impacts such as third-party plugins, establishing incident-reporting criteria, tracing digital-content origin and modification, using metrics for provenance and misinformation patterns, documenting risks that cannot be measured quantitatively, and evaluating model-capability claims with empirically validated methods [S15].

Synthesis: [[model-context-protocol-security-best-practices|MCP Security Best Practices]] addresses protocol-adjacent implementation controls such as session security, least privilege, sandboxing, and token passthrough, while S15 supplies the broader organizational risk-governance frame for generative AI systems that use such tools [S13] [S15].

Synthesis: S21's required evidence folders, including `source_manifest.md`, `wiki/`, `schema/`, `logs/`, and `evidence/`, operationalize part of the governance evidence layer for this project [S15] [S21].

## Limitations and Counter-Evidence

S15 is a governance profile and companion resource, not an agent implementation guide or benchmark, so it should be paired with technical evaluation sources such as API-Bank, tau-bench, and ToolSandbox when making claims about agent task performance [S04] [S05] [S06] [S15].

S15 explicitly says suggested-action implementation varies by risk type, generative AI system characteristics, lifecycle stage, and relevant AI actors, so its actions should not be copied into a deployment as universal requirements without context analysis [S15].

S15 includes future-revision uncertainty because additional AI RMF subcategories, risks, and suggested actions may be added as generative AI evolves and more empirical evidence appears [S15].

The CBRN section reports that recent research found LLM outputs about biological threat creation and attack planning provided minimal assistance beyond traditional search-engine queries at the time of those studies, so CBRN risk claims should distinguish future capability monitoring from demonstrated operational increase [S15].

S21 is a project note rather than a governance standard, so it can define local evidence expectations but should not replace S15 for external generative AI risk governance claims [S15] [S21].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[model-context-protocol-security-best-practices|Model Context Protocol Security Best Practices]]
- [[api-bank-tool-augmented-llm-benchmark|API-Bank Tool-Augmented LLM Benchmark]]
- [[tau-bench-agent-consistency-benchmark|Tau-Bench Agent Consistency Benchmark]]
- [[toolsandbox-stateful-tool-use-benchmark|ToolSandbox Stateful Tool-Use Benchmark]]
- [[project-scope-and-research-hypotheses|Project Scope and Research Hypotheses]]

## Open Questions

- Which S15 suggested actions should become concrete audit events for enterprise agent systems source-needed?
- How should S15's qualitative unmeasured-risk documentation be combined with benchmark metrics such as `pass^k` source-needed?
- Which governance artifacts are required before a tool-connected generative AI agent should be allowed to perform write actions source-needed?
