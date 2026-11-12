# S04 Ingest Evidence Notes

Source: S04, `raw/S04.pdf`, "API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs" by Li et al., manifest date 2023-12.

Verification notes:

- PDF extraction reported 15 pages.
- Manifest labels S04 as a public, high-quality paper/PDF intended for numerical precision and API-planning evaluation.
- Ability grading checked: Call, Retrieval+Call, and Plan+Retrieval+Call.
- Evaluation system checked: 73 implemented APIs, 314 retained manually annotated dialogues, 753 API calls, 21.5% discarded from 400 annotated dialogues, $8 average annotation cost per dialogue, and 98 person-days to implement APIs.
- Training set checked from Table 2: 1,000 domains, 2,138 APIs, 1,888 dialogues, 5,221 turns, 3,147 single-call and 493 multiple-call instances.
- Evaluation set checked from Table 2: 8 domains, 73 APIs, 314 dialogues, 914 turns, 363 single-call and 122 multiple-call instances.
- Main results checked from Table 3: Alpaca-7B total correctness 15.19%, ChatGLM-6B 16.42%, GPT-3 Davinci 0.57%, GPT-3.5-turbo 47.16%, GPT-4 60.24%, Lynx-7B 39.58%.
- Error distributions checked from Tables 4-6: Alpaca `No API Call` 36.77%; Lynx `API Hallucination` 61.38%; GPT-4 `Failed API Retrieval` 67.86%.
- Limitations checked: English-only benchmark, only Lynx-7B fine-tuned in reported experiments, larger internal commercial model not reported for anonymity reasons.
- Relationship checked against existing S02 and S03 pages: API-Bank evaluates tool-use abilities, while ReAct is a prompting method and Toolformer is a self-supervised API-call training method.

No contradiction with existing S01-S03 pages was detected; S04 adds a benchmark and evaluation framework for tool-augmented LLMs.
