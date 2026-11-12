---
source_id: S21
type: project-note
authorship: AI-assisted-draft-requires-student-review
date: 2026-07-06
---

# Project Scope and Research Hypotheses

## Research Object

This project studies **reliable knowledge and tool use for enterprise AI agents**.

Reliability does not mean that a model produces fluent single-turn answers. It means that the system can maintain consistency across traceable knowledge, explicit permissions, correct tool selection, verifiable state changes, and appropriate human oversight. An enterprise agent that can answer questions but cannot cite its basis, can call tools but cannot prove authorization, or can complete tasks but cannot roll back errors is not a lab-grade reliable system.

The project treats MCP, multi-agent systems, RAG, and LLM Wiki as four different layers of an enterprise-agent stack:

- MCP: the boundary for tools and context exchange.
- Multi-agent systems: task decomposition and verification topology.
- RAG: retrieval from raw evidence at query time.
- LLM Wiki: pre-compilation of multi-source knowledge into a maintainable persistent structure.

## Core Concepts

### MCP

Model Context Protocol is treated as the tool and context connection layer. It can help AI applications discover, read, and call external tools, resources, and prompts in a standardized way. Its value is interoperability.

MCP does not automatically solve business correctness. It can tell a system what tools exist and how to call them, but it does not guarantee that the model chooses the right tool, that the user has the correct authorization, that tool output is true, or that a write action should be executed.

### RAG

Retrieval-Augmented Generation is treated as the raw-evidence channel. Its role is to return to original material at query time, retrieve relevant passages, and let the model generate an answer from those passages.

RAG is strong when high-risk facts, current information, or direct citations are needed. Its risks are retrieval misses, fragmented evidence, and repeated synthesis work at every query.

### LLM Wiki

LLM Wiki is treated as the compiled-knowledge channel. Instead of retrieving raw chunks at every query, an ingest process converts sources into persistent, linked Markdown knowledge pages.

Its strength is accumulated synthesis: conflicts, entity relations, research questions, and maintenance history can be preserved. Its risk is that early ingest errors may harden into the wiki, summaries may drift, and readers may over-trust derived pages instead of checking sources.

### Multi-Agent Systems

Multi-agent systems are treated as a task-decomposition and verification topology. Different agents can play roles such as retriever, policy checker, critic, tool executor, and human-escalation coordinator.

They do not automatically increase reliability. If agents share the same model, context, and false assumptions, they can amplify correlated errors. They are useful only when roles, evidence sources, and final arbitration are meaningfully differentiated.

## Research Questions

1. Can an LLM-maintained wiki function as reliable generative research memory rather than only an attractive summarizer?
2. Should RAG and LLM Wiki replace each other, or should they form a dual-channel architecture of raw evidence plus compiled knowledge?
3. What can MCP provide for enterprise agents, and which permission, security, and tool-selection problems does it not solve?
4. When do multi-agent systems improve reliability, and when do they merely add cost, delay, and error-propagation paths?
5. How should a lab-grade second brain record sources, claims, conflicts, time versions, tool calls, state changes, and human review?
6. Which pressure points most reveal hidden failures in an LLM-maintained wiki, such as conflict merging, entity confusion, numerical drift, low-quality source contamination, and over-synthesis?

## Expected Evidence and Workflow

The project's evidence should come from reproducible files, logs, and saved artifacts rather than subjective impressions alone. At minimum it should include:

- `source_manifest.md`: all sources, quality levels, intended use, and shareability.
- `wiki/`: AI-generated or maintained knowledge pages.
- `schema/`: page templates, maintenance rules, and prompts.
- `logs/`: ingest, query, and maintenance records.
- `evidence/`: diffs, screenshots, terminal output, reproduction results, or page excerpts.

This note is AI-assisted and must be reviewed by the student before being treated as a personal project statement.
