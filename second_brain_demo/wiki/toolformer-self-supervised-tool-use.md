---
title: Toolformer Self-Supervised Tool Use
page_type: concept
status: draft
updated: 2026-07-11
sources: [S02, S03, S04]
confidence: high
---

# Toolformer Self-Supervised Tool Use

## Core Definition

Toolformer is a language-model training approach that teaches a model to decide which external APIs to call, when to call them, what arguments to pass, and how to incorporate returned results into later token prediction [S03].

Schick et al.'s Toolformer method samples candidate API calls into ordinary text, executes those calls, keeps calls only when the API result reduces the model's future-token loss by at least a filtering threshold, and fine-tunes the model on the surviving API-augmented text [S03].

## Key Claims

- Toolformer is designed to address language-model weaknesses in factual lookup, arithmetic, low-resource-language understanding, and temporal awareness by giving the model access to tools such as search engines, calculators, translation systems, calendars, and question-answering systems [S03].
- The paper uses five tools: a question-answering system based on Atlas, a BM25 Wikipedia search engine over the KILT Wikipedia dump, a calculator supporting the four basic arithmetic operations with outputs rounded to two decimal places, a 600M-parameter NLLB machine-translation system for translation into English, and a calendar API that returns the current date [S03].
- Toolformer represents API calls as text sequences with special delimiters and, in practice, uses existing token sequences such as `[` and `]` rather than modifying the underlying language model vocabulary [S03].
- The training setup uses GPT-J with 6.7B parameters as the base language model and a subset of CCNet as the language-modeling dataset [S03].
- For API-call filtering, the method compares loss with the call and result against the minimum of no call and call-without-result, retaining calls only when the loss reduction is at least the tool's filtering threshold [S03].
- With filtering threshold `tau_f = 1.0`, the augmented dataset contains 18,526 question-answering examples, 60,974 Wikipedia-search examples, 994 calculator examples, 20,587 calendar examples, and 1,034 machine-translation examples [S03].
- Toolformer fine-tuning uses batch size 128, learning rate `1e-5`, linear warmup for the first 10% of training, up to 25,000 examples per API, maximum sequence length 1,024, and DeepSpeed ZeRO-3 on 8 NVIDIA A100 40GB GPUs with BF16 [S03].
- In zero-shot LAMA subsets, Toolformer reports 33.8 on SQuAD, 11.5 on Google-RE, and 53.5 on T-REx, outperforming GPT-J, GPT-J fine-tuned on CCNet, Toolformer with API calls disabled, OPT 66B, and GPT-3 175B on those reported rows [S03].
- On math benchmarks, Toolformer reports 40.4 on ASDiv, 29.4 on SVAMP, and 44.0 on MAWPS, while GPT-3 175B reports 14.0, 10.0, and 19.8 respectively [S03].
- On question answering, Toolformer reports 26.3 on WebQuestions, 17.7 on Natural Questions, and 48.8 on TriviaQA, outperforming same-size GPT-J baselines but falling short of GPT-3 175B at 29.0, 22.6, and 65.9 [S03].
- On temporal tasks, Toolformer reports 16.3 on TEMPLAMA and 27.3 on DATESET, but the paper notes that TEMPLAMA improvement does not come from the calendar tool because the calendar API is used for only 0.2% of TEMPLAMA examples [S03].
- Toolformer does not degrade ordinary language-modeling perplexity when API calls are disabled: the paper reports Toolformer-disabled perplexity of 10.3 on WikiText and 10.5 on CCNet, matching GPT-J+CC on both datasets [S03].
- The paper's scaling analysis finds that useful tool leverage emerges around 775M parameters for the tested GPT-2/GPT-J family, while smaller models perform similarly with and without tools [S03].

## Evidence and Sources

S03 is a high-quality public paper/PDF in the manifest, dated 2023-02-09, and is the primary source for this page's method, tool inventory, benchmark, and limitation claims [S03].

The downstream experiments use prompted zero-shot evaluation, meaning models are instructed in natural language but are not given task-specific in-context examples of how to use tools for the benchmark being solved [S03].

Toolformer is evaluated against GPT-J, GPT-J+CC, Toolformer with API calls disabled, OPT 66B, and GPT-3 175B across reported benchmark tables [S03].

## Limitations and Counter-Evidence

Toolformer cannot use tools in a chain in the reported setup, because API calls for each tool are generated independently and the fine-tuning data contains no examples of using one tool's output as another tool's input [S03].

The reported approach does not allow interactive tool use, so a model cannot browse multiple search results or refine a query when a search engine returns poor results [S03].

The paper reports sensitivity to exact input wording when deciding whether to call an API, consistent with known prompt sensitivity in zero-shot and few-shot language-model settings [S03].

Toolformer can be sample-inefficient for some tools; the authors note that processing more than a million documents yields only a few thousand useful calculator-call examples [S03].

The reported method does not account for tool-dependent computational cost when deciding whether to make an API call [S03].

Toolformer trails GPT-3 175B on the reported WebQuestions, Natural Questions, and TriviaQA rows, which the authors attribute partly to the simplicity of the search engine and lack of interactive query refinement [S03].

Synthesis: Toolformer trains a model to decide when to insert API calls, while API-Bank evaluates whether models can call known APIs, retrieve unknown APIs, and plan multiple API calls inside an executable benchmark system [S03] [S04].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[react-reasoning-and-acting|ReAct Reasoning and Acting]]
- [[retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[api-bank-tool-augmented-llm-benchmark|API-Bank Tool-Augmented LLM Benchmark]]

## Open Questions

- How should enterprise agents price tool calls when the Toolformer objective does not include tool-specific latency, money, or risk costs [S03]?
- Can self-supervised API-call filtering be combined with ReAct-style interactive planning so a model can both learn tool affordances and refine failed tool calls over multiple steps [S02] [S03]?
- What safeguards are needed before a self-supervised tool-use model can learn from logs that include sensitive or permissioned enterprise tool outputs source-needed?
