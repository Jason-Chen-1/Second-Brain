---
title: Model Context Protocol Authorization
page_type: concept
status: draft
updated: 2026-07-11
sources: [S11, S12, S13, S14]
confidence: high
---

# Model Context Protocol Authorization

## Core Definition

MCP Authorization is the authorization boundary for MCP deployments, with S12 captured as the stable Model Context Protocol authorization specification dated 2025-11-25 [S12].

S12 is the normative source in this knowledge base for MCP authorization boundaries, including OAuth 2.1, PKCE, audience binding, and token handling [S12].

## Key Claims

- S12 is an official MCP specification capture, public, high quality, accessed on 2026-07-06, and dated 2025-11-25 [S12].
- S12 is the stable MCP authorization specification used to discuss OAuth 2.1, PKCE, audience binding, and token handling [S12].
- S12 supports the claim that an MCP connection does not automatically imply safe or authorized tool use [S12].
- S12 should be used for production authorization claims rather than Anthropic's S14 launch article [S12] [S14].
- S12 should be paired with current MCP security best practices in S13 for production security guidance, including session security, least privilege, sandboxing, and token passthrough [S12] [S13].

## Evidence and Sources

The captured S12 source says it is the stable MCP authorization specification and the normative source for authorization boundaries [S12].

The captured S12 source says it is used in update-pair reasoning with S14 and S13 [S12].

Synthesis: S14 provides historical positioning for MCP as an open connection standard, while S12 supersedes S14 for production authorization requirements [S12] [S14].

Synthesis: [[model-context-protocol-architecture|MCP Architecture]] describes the host/client/server and tool/context exchange layer, while MCP Authorization describes whether and how MCP-connected tool use is authorized [S11] [S12].

## Limitations and Counter-Evidence

S12 should not be treated as a complete implementation-security checklist by itself, because the captured source says to pair it with current security best practices in S13 [S12].

S13 supplies current implementation-risk and mitigation coverage for MCP deployments, including session security, least privilege, sandboxing, and token passthrough [S13].

S14 remains useful for MCP history and positioning, but it is superseded by S12 for current production authorization requirements [S12] [S14].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[model-context-protocol-architecture|Model Context Protocol Architecture]]
- [[model-context-protocol-security-best-practices|Model Context Protocol Security Best Practices]]

## Open Questions

- Which OAuth 2.1 requirements from the full S12 specification should be expanded into implementation checklists source-needed?
- How should MCP clients enforce audience binding and token handling across multiple servers source-needed?
- Which S13 security controls should be mandatory before authorizing write-capable MCP tools source-needed?
