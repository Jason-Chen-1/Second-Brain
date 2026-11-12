# S07 AutoGen Extraction Notes

- Source metadata checked in `raw/source_manifest.md`: S07 is `AutoGen - Wu et al.`, dated 2023-08-16, public, paper/PDF, medium quality, with intended use for multi-agent orchestration and human/tool participation.
- PDF extraction used bundled Python with `pdfplumber`; the PDF has 43 pages.
- Core definition checked from abstract and Section 2: AutoGen is an open-source framework for LLM applications built from multiple conversable agents and conversation programming.
- Agent abstraction checked from Section 2.1: `ConversableAgent` is the highest-level abstraction; `AssistantAgent` and `UserProxyAgent` are built-in subclasses; agents can use LLM, human, and tool capabilities.
- Conversation programming checked from Section 2.2: agents use `send`, `receive`, and `generate_reply`; auto-reply invokes response generation after message receipt unless termination conditions are met; control can combine natural language and Python.
- Application list checked from Section 3/Figure 3: math problem solving, retrieval-augmented chat, ALFWorld, multi-agent coding, dynamic group chat, and conversational chess.
- MATH results checked from Figure 4 and Appendix D: AutoGen reports 69.48% full MATH test accuracy with GPT-4 versus 55.18% for GPT-4; qualitative tests report AutoGen at 3/3 and 2/3 on two level-5 problems.
- Retrieval-Augmented Chat checked from Section 3 and Appendix D: Natural Questions evaluation uses 5,332 non-redundant context documents and 6,775 queries; about 19.4% of questions trigger `Update Context`.
- ALFWorld results checked from Section 3/Table 3: ReAct average 54, ALFChat two-agent average 54, ALFChat three-agent average 69; best-of-three scores are 66, 63, and 77.
- OptiGuide results checked from Section 3 and Appendix D: workflow code reduced from over 430 lines to 100 lines; coffee user study reports 4 minutes 35 seconds average with ChatGPT plus Code Interpreter versus about 1.5 minutes with AutoGen-based OptiGuide; multi-agent design improves unsafe-code F1 by 8 points with GPT-4 and 35 points with GPT-3.5-turbo.
- Dynamic group chat checked from Appendix D: on 12 tasks, GPT-4 solves 9 with two-agent chat, 11 with group chat, and 8 with group chat using task-based speaker selection.
- MiniWobChat checked from Appendix D: success rate is 52.8% across 49 MiniWoB++ tasks, 3.6 percentage points below RCI.
- Evidentiary boundary: medium-quality preprint/framework report; many results are demonstrations, pilot studies, selected tasks, or appendix evaluations rather than a single standardized benchmark suite.
