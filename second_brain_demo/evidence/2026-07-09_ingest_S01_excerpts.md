# S01 Ingest Evidence Notes

Source: S01, `raw/S01.pdf`, "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" by Lewis et al., manifest date 2020-05-22.

Verification notes:

- PDF extraction reported 19 pages.
- Manifest labels S01 as a public, high-quality paper/PDF intended for RAG baseline, source traceability, and knowledge updating.
- Architecture checked: RAG combines a BART-large generator with a DPR-initialized retriever over a Wikipedia dense-vector index; documents are latent variables marginalized by RAG-Sequence or RAG-Token.
- Corpus/index checked: experiments use the December 2018 Wikipedia dump, 100-word disjoint chunks, about 21 million documents, FAISS MIPS retrieval.
- Open-domain QA numbers checked from Table 1: RAG-Sequence reports NQ 44.5, TQA 56.8/68.0, WQ 45.2, CT 52.2 exact match.
- Generation/classification numbers checked from Table 2 and adjacent results text: RAG-Token Jeopardy Q-BLEU-1 22.2 vs BART 19.7; RAG FEVER 3-way 72.5 and 2-way 89.5 label accuracy.
- Human evaluation checked from Section 4.3/Table 4: RAG better factuality 42.7%; BART better factuality 7.1%.
- Knowledge update result checked from Section 4.5: matched 2016/2018 indices score 70%/68%; mismatched index/year settings score 12%/4%.
- Limitations checked: DPR retrieval supervision on NQ/TQA, no improvement from null-document mechanisms, preliminary retrieval collapse on story generation, and no direct FEVER sentence-evidence task because of Wikipedia dump mismatch.

No existing wiki topic pages were available beyond the malformed index, so no source conflict was detected during this ingest.
