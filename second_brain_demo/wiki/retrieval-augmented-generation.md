---
title: Retrieval-Augmented Generation
page_type: concept
status: draft
updated: 2026-07-09
sources: [S01, S02, S07, S10, S20]
confidence: mixed
---

# Retrieval-Augmented Generation

## Core Definition

Retrieval-augmented generation (RAG) is a sequence-to-sequence modeling approach that combines parametric memory in a pre-trained generator with non-parametric memory in a retrievable document index, so generation can condition on external passages as well as model parameters [S01].

In Lewis et al.'s 2020 formulation, the generator is BART-large and the retriever is initialized from Dense Passage Retrieval (DPR), with Wikipedia passages retrieved by maximum inner product search (MIPS) and treated as latent variables during generation [S01].

## Key Claims

- RAG was proposed to address limitations of parametric-only language models: difficulty revising memory, limited prediction provenance, and hallucination risk on knowledge-intensive tasks [S01].
- The paper defines two variants: RAG-Sequence uses the same retrieved document for the whole generated sequence, while RAG-Token can condition each generated token on a different retrieved document [S01].
- The experiments use a December 2018 Wikipedia dump split into 100-word disjoint chunks, producing about 21 million documents in a FAISS MIPS index [S01].
- The retriever and generator are jointly fine-tuned without direct supervision for which document should be retrieved; the document encoder and document index are kept fixed because updating them would require periodic index refreshes [S01].
- On open-domain QA test results, RAG-Sequence reports 44.5 exact match on Natural Questions, 56.8 on the standard TriviaQA split, 68.0 on TriviaQA-Wiki, 45.2 on WebQuestions, and 52.2 on CuratedTrec [S01].
- RAG can generate correct Natural Questions answers even when the answer is absent from all retrieved documents, with the paper reporting 11.8% accuracy in that subset where an extractive model would score 0% [S01].
- On Open MS-MARCO NLG, RAG-Sequence outperforms the BART baseline by 2.6 BLEU-1 points and 2.6 ROUGE-L points, while the authors caution that some MS-MARCO questions require gold passages or information outside Wikipedia [S01].
- In Jeopardy question generation, RAG-Token scores 22.2 Q-BLEU-1 versus BART's 19.7, and human evaluators rated RAG-Token more factual than BART in 42.7% of pairwise cases versus 7.1% for BART [S01].
- On FEVER, RAG scores 72.5 label accuracy for 3-way classification and 89.5 for 2-way classification, within 4.3% and 2.7% of cited state-of-the-art systems that use stronger evidence access or supervision [S01].
- Replacing the non-parametric memory can update model behavior: with 2016 and 2018 Wikipedia indices, the paper reports 70% accuracy for 2016 world leaders with the 2016 index and 68% for 2018 world leaders with the 2018 index, while mismatched index/year combinations fall to 12% and 4% [S01].

## Evidence and Sources

S01 is a high-quality public paper by Lewis et al. dated 2020-05-22 in the manifest, and it is the primary source for this page's architecture, evaluation, and limitation claims [S01].

The paper reports that the RAG models contain 626 million trainable parameters, combining 110 million parameters for the DPR query encoder, an untrained/fixed 110 million parameter DPR document encoder, and 406 million trainable parameters from BART-large [S01].

The non-parametric memory is not counted as trainable parameters, but the paper describes it as 21 million 728-dimensional vectors, about 15.3 billion values, with index compression reducing a reported CPU memory requirement from about 100 GB to 36 GB in the Hugging Face implementation [S01].

## Limitations and Counter-Evidence

The paper's RAG results are tied to a specific experimental setup: a December 2018 Wikipedia index, DPR initialization, BART-large generation, and task-specific fine-tuning, so the reported benchmark numbers should not be generalized to arbitrary RAG systems without re-evaluation [S01].

The paper notes that RAG's retriever is initialized from DPR trained with retrieval supervision on Natural Questions and TriviaQA, which limits claims that all improvements come from unsupervised retrieval learning [S01].

The authors tried adding a null-document mechanism to model cases where no useful document was retrieved, but they report that learned null document embeddings, a static learned bias, and a neural-network logit did not improve performance [S01].

Preliminary experiments found retrieval collapse on tasks such as story generation, where the retriever learned to return the same documents regardless of input and the generator learned to ignore them, making RAG perform equivalently to BART [S01].

For FEVER evidence extraction, the paper does not directly tackle sentence-level evidence retrieval because FEVER uses a different Wikipedia dump than the RAG index; this leaves a gap between label classification and full evidence provenance [S01].

Synthesis: RAG and ReAct both use external knowledge, but S01's RAG is a fine-tuned seq2seq architecture that marginalizes retrieved Wikipedia passages, while S02's ReAct is a prompting paradigm that interleaves language thoughts, tool actions, and observations through an external API or environment [S01] [S02].

Synthesis: AutoGen's Retrieval-Augmented Chat uses a retrieval-augmented user proxy and retrieval-augmented assistant around a vector database, and its interactive `Update Context` loop is an application orchestration pattern rather than the same model-level RAG architecture defined in S01 [S01] [S07].

Synthesis: [[llm-wiki|LLM Wiki]] and RAG both externalize knowledge beyond model parameters, but S10 describes a persistent Markdown knowledge-base maintenance pattern around raw sources, derived wiki pages, schema files, ingest/query/lint workflows, and an index-like wiki structure rather than the trainable retriever-generator architecture evaluated in S01 [S01] [S10].

Synthesis: S20 is a low-quality critique/opinion source that frames LLM Wiki as a RAG complement rather than a RAG replacement, so it is useful for recording the design tension but not for overriding S01's primary RAG claims or S10's LLM Wiki concept claims [S01] [S10] [S20].

## Links to Other Pages

- [[index|Knowledge Base Index]]
- [[react-reasoning-and-acting|ReAct Reasoning and Acting]]
- [[autogen-multi-agent-conversation-framework|AutoGen Multi-Agent Conversation Framework]]
- [[llm-wiki|LLM Wiki]]
- [[contradiction-register|Contradiction Register]]

## Open Questions

- How much of RAG's open-domain QA gain depends on DPR pretraining and retrieval supervision rather than the RAG marginalization objective itself [S01]?
- What validation is needed before using index replacement as an enterprise knowledge-update mechanism, given that the paper demonstrates world-leader update behavior but also reports mismatched-index failures [S01]?
- When should a production system prefer RAG-Sequence, RAG-Token, or a more recent retrieval architecture for auditability, latency, and answer faithfulness source-needed?
