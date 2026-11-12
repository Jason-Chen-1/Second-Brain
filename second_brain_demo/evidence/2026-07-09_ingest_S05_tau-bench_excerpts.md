# S05 Tau-Bench Extraction Notes

- Source metadata checked in `raw/source_manifest.md`: S05 is `tau-bench - Yao et al.`, dated 2024-06-17, public, paper/PDF, high quality, with intended use for enterprise-agent consistency and `pass^k` metrics.
- PDF extraction used bundled Python with `pdfplumber`; the PDF has 50 pages.
- Core definition checked from abstract/introduction: tau-bench evaluates dynamic conversations between an LM-simulated user and a language agent with domain-specific API tools and policy guidelines.
- Metric checked from Section 3: `pass^k` measures the chance that all `k` independent trials succeed, averaged across tasks; default `pass^1` equals average reward and `pass@1`.
- Domain statistics checked from Table 1: retail has 500 users, 50 products, 1,000 orders, 7 write APIs, 8 non-write APIs, and 115 tasks; airline has 500 users, 300 flights, 2,000 reservations, 6 write APIs, 7 non-write APIs, and 50 tasks.
- Experiment settings checked from Section 5: main results use at least 3 trials per task, agent temperature 0.0, user temperature 1.0, and a 30-agent-action limit.
- Main results checked from Table 2: `gpt-4o` FC scores 61.2 retail, 35.2 airline, 48.2 average; `gpt-4-turbo` FC scores 57.7, 32.4, 45.1; `claude-3-opus` FC scores 44.2, 34.7, 39.5; `meta-llama-3-70B` uses text ReAct and scores 14.8, 14.4, 14.6.
- Consistency result checked from Section 5.1/Figure 4 prose: `gpt-4o` FC retail `pass^8` drops below 25% despite more than 60% average `pass^1`.
- Failure analysis checked from Section 5.2: among 115 sampled `gpt-4o` FC retail trajectories, 40 initially failed, 4 were fixed as user-instruction typo/ambiguity, and 36 remaining failures were agent issues.
- Policy ablation checked from Table 3/prose: removing domain policy changes `gpt-4o` scores from 61.2 to 56.8 in retail and 33.2 to 10.8 in airline; `gpt-3.5` changes from 20.0 to 14.5 in retail and 10.8 to 9.6 in airline.
- Evidentiary boundary: high-quality public paper, but the benchmark uses synthetic customer-service data and LM-simulated users, and S05 explicitly notes simulation, annotation, and domain-scope limitations.
