# S12 MCP Authorization Extraction Notes

- Source metadata checked in `raw/source_manifest.md`: S12 is `MCP Authorization, stable spec 2025-11-25 - Model Context Protocol`, dated 2025-11-25, public, official spec capture, high quality, with intended use for OAuth 2.1, audience binding, PKCE, version supersession, and token handling.
- Raw capture checked in `raw/S12_mcp_authorization.source.md`: source ID S12, type `official-specification`, accessed 2026-07-06, shareability public, quality high.
- Core specification checked: S12 is the stable MCP authorization specification used to discuss OAuth 2.1, PKCE, audience binding, and token handling.
- Project-use claims checked: S12 is the normative source for authorization boundaries and supports claims that MCP connection does not automatically imply safe or authorized tool use.
- Supersession boundary checked: S12 should be used for production authorization claims rather than S14's launch article, while S14 remains historical positioning.
- Security boundary checked: S12 should be paired with current security best practices in S13 for production security guidance.
- Page decision: created `wiki/model-context-protocol-authorization.md` because authorization is a stable concept distinct from the existing MCP architecture page.
