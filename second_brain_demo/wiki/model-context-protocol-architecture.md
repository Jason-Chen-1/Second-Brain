---
title: Model Context Protocol Architecture
page_type: concept
status: draft
updated: 2026-07-11
sources: [S02, S11, S12, S13, S14, S19, S22]
confidence: mixed
---

# Model Context Protocol Architecture

## Core Definition

The Model Context Protocol architecture overview is official technical documentation that defines MCP's basic architecture for host, client, server, tools, resources, prompts, and capability negotiation [S11].

S11 is used in this project as the baseline for what MCP provides at the tool/context exchange layer [S11].

Anthropic's 2024-11-25 launch article positions MCP historically as an open standard for connecting AI assistants to tools, content repositories, and development environments [S14].

S19 is a medium-quality repository capture useful for comparing MCP-style connection patterns in an LLM Wiki implementation, but it is not an MCP architecture specification [S11] [S19].

S22 uses MCP to mean maximum clique problem rather than Model Context Protocol, so this page treats S22 only as acronym disambiguation and not as architecture evidence [S11] [S22].

## Key Claims

- S11 defines the MCP architecture roles of host, client, and server [S11].
- S11 defines MCP primitives for tools, resources, and prompts [S11].
- S11 includes capability negotiation as part of the MCP architecture overview [S11].
- S11 supports distinguishing the MCP architecture layer from production authorization and security details covered by later sources S12 and S13 [S11].
- S11 is an official technical documentation capture, public, high quality, accessed on 2026-07-06, and listed in the manifest as continuously updated [S11].
- S14 is a public, medium-quality official release webpage by Anthropic, dated 2024-11-25, and is used for MCP's original positioning as a connection standard rather than for current production authorization requirements [S14].
- S14 frames MCP as background for why an open connection standard exists for AI assistants and external systems [S14].
- S12 is the stable MCP authorization specification dated 2025-11-25, and it supersedes S14 for production authorization claims while preserving S14 as historical positioning [S12] [S14].
- S13 is the current MCP security best-practices capture used for implementation risks and mitigations, including session security, least privilege, sandboxing, and token passthrough [S13].
- S19 is a public repository capture for `llmwiki`, active in 2026, and is useful for comparing MCP-style connection patterns in document-ingestion and generated-Markdown workflows [S19].
- S22 is a 2015-05-26 medium-quality academic PDF about the maximum clique problem, and it shows that the abbreviation MCP can refer to graph optimization rather than the Model Context Protocol [S22].

## Evidence and Sources

The captured S11 source says the official MCP architecture overview defines the basic architecture used throughout the project, including host, client, server, tools, resources, prompts, and capability negotiation [S11].

The captured S11 source says its project use is defining what MCP provides at the tool/context exchange layer and distinguishing architecture from authorization and security details [S11].

The captured S14 source says it provides historical positioning for MCP as an open standard for connecting AI assistants to tools, content repositories, and development environments [S14].

Synthesis: MCP architecture is a protocol and integration boundary for exposing context and capabilities, while [[react-reasoning-and-acting|ReAct]] is a prompting pattern for how a model chooses and reasons through actions in an environment [S02] [S11].

Synthesis: S14 explains MCP's initial product and ecosystem motivation, while S11 supplies the later architecture vocabulary used by this knowledge base; neither S14 nor S11 should be treated as the current production authorization or security source by itself [S11] [S14].

Synthesis: [[model-context-protocol-authorization|MCP Authorization]] covers OAuth 2.1, PKCE, audience binding, and token handling, while this page covers the host/client/server and capability architecture layer [S11] [S12].

Synthesis: [[model-context-protocol-security-best-practices|MCP Security Best Practices]] complements MCP architecture and authorization by covering implementation risks and mitigations for MCP deployments [S11] [S12] [S13].

Synthesis: [[second-brain-implementation-patterns|Second-Brain Implementation Patterns]] can use S19 to compare how public LLM Wiki repositories operationalize MCP-style connection patterns, while this page should continue to source protocol architecture claims to S11 rather than repository examples [S11] [S19].

Synthesis: [[mcp-acronym-disambiguation|MCP Acronym Disambiguation]] should be used when deciding whether a source is about Model Context Protocol or the maximum clique problem, because S11/S14 and S22 use the same abbreviation for different domains [S11] [S14] [S22].

## Limitations and Counter-Evidence

S11 should not be used alone for production authorization or security claims, because its capture explicitly says to pair the architecture overview with S12 and S13 for those topics [S11].

S11 is continuously updated official documentation, so concrete architecture claims should be tied to the captured access date of 2026-07-06 unless later ingests update the page [S11].

S11 is an overview source rather than a full security or authorization specification, so normative deployment claims should wait for the dedicated authorization and security sources [S11].

S14 is a launch article and should be used for history and positioning, not for current production authorization requirements [S14].

S14 is the earlier item in an update pair with later authorization and security sources; S12 supersedes S14 for production authorization requirements, and S13 supplies current security best-practice guidance [S12] [S13] [S14].

S19 should not be used as evidence for normative MCP architecture requirements because it is a repository capture and the source itself is included only as an implementation comparison for LLM Wiki workflows [S11] [S19].

S22 should not be used as evidence for Model Context Protocol requirements because its MCP means maximum clique problem and its evidence concerns graph-optimization formulations and clique-finding algorithms [S22].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[react-reasoning-and-acting|ReAct Reasoning and Acting]]
- [[model-context-protocol-authorization|Model Context Protocol Authorization]]
- [[model-context-protocol-security-best-practices|Model Context Protocol Security Best Practices]]
- [[second-brain-implementation-patterns|Second-Brain Implementation Patterns]]
- [[mcp-acronym-disambiguation|MCP Acronym Disambiguation]]

## Open Questions

- Which MCP capability-negotiation details belong on this architecture page versus a later protocol-version page source-needed?
- How should MCP hosts expose tool, resource, and prompt capabilities to agents while preserving least privilege source-needed?
- What audit events should be recorded at host, client, and server boundaries when MCP tools are invoked source-needed?
