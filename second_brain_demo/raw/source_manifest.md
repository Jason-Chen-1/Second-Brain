# Source Manifest

Initial source access date: **2026-07-06** unless a later ingest log states otherwise. Quality labels: `high` for peer-reviewed work or official specifications/reports; `medium` for preprints, official practice guides, active repositories, or project-created notes; `low` for weakly verified secondary commentary; `synthetic` for created test or project materials.

| ID | Title / Author | Date | URL / File | Type | Shareability | Quality | Intended Use |
|---|---|---:|---|---|---|---|---|
| S01 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks - Lewis et al. | 2020-05-22 | `S01.pdf`; https://arxiv.org/abs/2005.11401 | paper/PDF | public | high | RAG baseline, source traceability, knowledge updating |
| S02 | ReAct: Synergizing Reasoning and Acting in Language Models - Yao et al. | 2022-10-06 | `S02.pdf`; https://arxiv.org/abs/2210.03629 | paper/PDF | public | high | reasoning-action loops and interpretable tool use |
| S03 | Toolformer - Schick et al. | 2023-02-09 | `S03.pdf`; https://arxiv.org/abs/2302.04761 | paper/PDF | public | high | when and how models choose tools |
| S04 | API-Bank - Li et al. | 2023-12 | `S04.pdf`; https://aclanthology.org/2023.emnlp-main.187/ | paper/PDF | public | high | numerical precision and API-planning evaluation |
| S05 | tau-bench - Yao et al. | 2024-06-17 | `S05.pdf`; https://arxiv.org/abs/2406.12045 | paper/PDF | public | high | enterprise-agent consistency and `pass^k` metrics |
| S06 | ToolSandbox - Lu et al. | 2024-08-08 | `S06.pdf`; https://arxiv.org/abs/2408.04682 | paper/PDF | public | high | stateful, multi-turn, insufficient-information tool evaluation |
| S07 | AutoGen - Wu et al. | 2023-08-16 | `S07.pdf`; https://arxiv.org/abs/2308.08155 | paper/PDF | public | medium | multi-agent orchestration and human/tool participation |
| S08 | Improving Factuality and Reasoning through Multiagent Debate - Du et al. | 2023-05-23 | `S08.pdf`; https://arxiv.org/abs/2305.14325 | paper/PDF | public | medium | positive claim that debate improves factuality |
| S09 | Can LLM Agents Really Debate? - Wu, Li & Li | 2025-11-11 | `S09.pdf`; https://arxiv.org/abs/2511.07784 | paper/PDF | public | medium | counterpoint to S08; debate limits and majority pressure |
| S10 | LLM Wiki - Andrej Karpathy | 2026-04-04 | `S10_llm_wiki.source.md`; https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f | source capture | public | medium | LLM Wiki pattern and medium-scale knowledge compilation |
| S11 | MCP Architecture Overview - Model Context Protocol | continuously updated | `S11_mcp_architecture.source.md`; https://modelcontextprotocol.io/docs/learn/architecture | official docs capture | public | high | host/client/server architecture and protocol boundaries |
| S12 | MCP Authorization, stable spec 2025-11-25 - Model Context Protocol | 2025-11-25 | `S12_mcp_authorization.source.md`; https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization | official spec capture | public | high | OAuth 2.1, audience binding, PKCE, version supersession |
| S13 | MCP Security Best Practices - Model Context Protocol | continuously updated | `S13_mcp_security_best_practices.source.md`; https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices | official security docs capture | public | high | session hijacking, least privilege, sandboxing, token passthrough |
| S14 | Introducing the Model Context Protocol - Anthropic | 2024-11-25 | `S14_introducing_mcp.source.md`; https://www.anthropic.com/news/model-context-protocol | announcement capture | public | medium | original MCP positioning as a connection standard |
| S15 | NIST AI 600-1: Generative AI Profile - Autio et al. | 2024-07-26 | `S15.pdf`; `S15_nist_ai_600_1.source.md`; https://doi.org/10.6028/NIST.AI.600-1 | official report/PDF + capture | public | high | enterprise risk governance and measurement |
| S16 | MCP Security Cheat Sheet - OWASP | continuously updated | `S16_owasp_mcp_security.source.md`; https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html | security webpage capture | public | high | excessive permissions, key exposure, tool poisoning |
| S17 | A Practical Guide to Building AI Agents - OpenAI | 2025 | `S17_openai_agents_guide.source.md`; https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/ | official practice guide capture | public | medium | single-vs-multi-agent tradeoffs, tool risk, human escalation |
| S18 | obsidian-second-brain - Eugeniu Ghelbur | active in 2026 | `S18_obsidian_second_brain.source.md`; https://github.com/eugeniughelbur/obsidian-second-brain | repository capture | public | medium | implementation reference for commands, search, and maintenance |
| S19 | llmwiki - Lucas Astorian | active in 2026 | `S19_llmwiki_repo.source.md`; https://github.com/lucasastorian/llmwiki | repository capture | public | medium | implementation reference for MCP-connected document ingestion |
| S20 | Karpathy's LLM Wiki, and whether it's worth wiring up - Artificial Ideas | 2026 | `S20_artificial_ideas_llm_wiki.source.md`; https://artificial-ideas.com/learn/karpathy-llm-wiki/ | critique/opinion capture | public | low | low-quality source handling; LLM Wiki as RAG complement |
| S21 | Project Scope and Research Hypotheses | 2026-07-06 | `S21_project_scope_note.md` | project note | shareable | medium | project boundaries and non-obvious synthesis |
| S22 | Solving the Maximum Clique Problem with Symmetric Rank-One Nonnegative Matrix Approximation - Belachew & Gillis | 2015-05-26 | `S22.pdf`; https://arxiv.org/abs/1505.07077 | paper/PDF | public | medium | MCP acronym disambiguation: Maximum Clique Problem vs Model Context Protocol |
| S23 | Latent Agents - Yi, Mueller & Lee | 2026-04-27 | `S23.pdf`; https://arxiv.org/abs/2604.24881 | paper/PDF | public | medium | internalized multi-agent debate, token cost, and agent-specific subspaces |
| S24 | Project folder structure screenshot | 2026-07-08 | `S24.png` | screenshot | project screenshot/shareable | synthetic | screenshot ingestion and visible-vs-inferred information |

## Coverage Notes

- The raw folder currently contains 24 numbered sources, S01-S24.
- Source types include papers/PDFs, official documentation, official reports, repository captures, opinion captures, a project note, and a screenshot.
- S20 is the designated low-quality source and must not independently support a key conclusion.
- S24 is a screenshot source; its visible information must be separated from interpretation.
