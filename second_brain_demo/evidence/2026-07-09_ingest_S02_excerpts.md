# S02 Ingest Evidence Notes

Source: S02, `raw/S02.pdf`, "ReAct: Synergizing Reasoning and Acting in Language Models" by Yao et al., manifest date 2022-10-06.

Verification notes:

- PDF extraction reported 33 pages.
- Manifest labels S02 as a public, high-quality paper/PDF intended for reasoning-action loops and interpretable tool use.
- Method checked: ReAct interleaves verbal thoughts, actions, and observations; thoughts update context but do not directly change the external environment.
- Model/setup checked: main experiments use PaLM-540B prompting; appendix reports GPT-3 `text-davinci-002` ReAct results.
- Tool/action space checked: HotpotQA and FEVER use a simple Wikipedia API with `search[entity]`, `lookup[string]`, and `finish[answer]`.
- HotpotQA/FEVER numbers checked from Table 1: Standard 28.7/57.1, CoT 29.4/56.3, CoT-SC 33.4/60.4, Act 25.7/58.9, ReAct 27.4/60.9, CoT-SC to ReAct 34.2/64.6, ReAct to CoT-SC 35.1/62.0, supervised SOTA 67.5/89.5.
- Failure analysis checked from Table 2: ReAct success false positive 6%, CoT success false positive 14%; ReAct failures 47% reasoning error, 23% search-result error, 29% label ambiguity; CoT failures 56% hallucination, 16% reasoning error, 28% label ambiguity.
- ALFWorld/WebShop numbers checked from Tables 3 and 4: best ReAct ALFWorld overall success 71% versus best Act 45% and BUTLER 37%; WebShop ReAct score 66.6 and success rate 40.0%.
- Limitations checked: ReAct trails CoT/CoT-SC on HotpotQA before combination; repetitive thought/action loops appear as a failure mode; large action spaces can exceed in-context learning limits; main PaLM experiments were not fully reproducible because PaLM was not openly accessible at the time.
- Safety boundary checked from ethics statement: experiments avoid private or dangerous actions by limiting interactions to constrained benchmark environments.

No contradiction with existing S01-derived RAG page was detected; S02 adds a distinct prompting/action-loop concept rather than revising S01's RAG architecture claims.
