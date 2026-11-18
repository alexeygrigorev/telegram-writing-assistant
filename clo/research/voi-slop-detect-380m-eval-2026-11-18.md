# Evaluation: VoightKampffLabs/voi-slop-detect-380M and Lightweight Alternatives

Evaluated on 2026-11-18 against 32 English documents from alexeygrigorev/telegram-writing-assistant across 4 categories:

- human_voice_raw (n=6): unedited English Telegram voice transcripts in inbox/used/ (152 - 395 words)
- edited_published_substack (n=10): human-edited, published Substack articles in reference/substack/ (1,310 - 3,546 words)
- unedited_raw_articles (n=8): unedited bot-generated drafts in articles/raw-articles/ (583 - 2,617 words)
- unedited_claw_drafts (n=8): unedited AI drafts in articles/claw-drafts/ (1,654 - 3,533 words)

Preprocessing: YAML frontmatter stripped; fenced code blocks emptied to bare triple-backtick pairs per the voi-slop-detect-380M model card.

## Summary Comparison

| Detector | Peak RSS | Load Time | Inf Time (32 docs) | AUROC (voice vs claw) | AUROC (substack vs claw) | AUROC (substack vs raw) |
|---|---:|---:|---:|---:|---:|---:|
| voi-slop-detect-380M (ONNX q8, first512) | 805.7 MB | 1.84 s | ~10 s / chunk | 1.000 | 0.988 | 0.600 |
| voi-slop-detect-380M (ONNX q8, chunk_mean) | 805.7 MB | 1.84 s | 1601.19 s (all chunks) | 1.000 | 1.000 | 0.537 |
| voi-slop-detect-380M (PyTorch bf16, first512) | 1106.1 MB | 23.66 s | 1065.86 s (33.3 s/doc) | 1.000 | 0.988 | 0.588 |
| fakespot-ai/roberta-base-ai-text-detection-v1 | 892.1 MB | 32.02 s | 158.16 s (4.9 s/doc) | 0.792 | 0.575 | 0.838 |
| AICodexLab/answerdotai-ModernBERT-base-ai-detector (1024 tok) | 903.9 MB | 33.53 s | 923.78 s (28.9 s/doc) | 0.458 | 0.000 | 0.250 |
| Hello-SimpleAI/chatgpt-detector-roberta | 908.4 MB | 22.76 s | 294.71 s (9.2 s/doc) | 0.062 | 0.050 | 0.287 |
| slop-tells heuristic (regex/lexicon) | 37.9 MB | 0.07 s | 0.05 s | 0.875 | 0.512 | 0.838 |

Note on heavier models not run: desklib/ai-text-detector-v1.01 (1,655 MB safetensors) and SuperAnnotate/ai-detector (1,351 MB safetensors) exceed the 1.5 GB container memory limit in fp32 on CPU.

## Group Scores by Detector (Mean / Median / Min - Max, Flagged Count)

### VoightKampffLabs/voi-slop-detect-380M (ONNX q8)

Shipped thresholds from bands.json: human_max = 0.15, flag_min = 0.4256, generated_min = 0.75.

- human_voice_raw (n=6): first512 mean 0.0154 (0.0064 - 0.0248), 0/6 flagged (>=0.4256)
- edited_published_substack (n=10): first512 mean 0.4519 (0.1170 - 0.7698), 6/10 flagged (>=0.4256); chunk_mean 0.3637 (0.2139 - 0.5293)
- unedited_raw_articles (n=8): first512 mean 0.5074 (0.3310 - 0.7956), 4/8 flagged (>=0.4256); chunk_mean 0.3801 (0.2478 - 0.5293)
- unedited_claw_drafts (n=8): first512 mean 0.9616 (0.7053 - 0.9996), 8/8 flagged (>=0.4256); chunk_mean 0.9038 (0.7094 - 0.9868)

### Alternative Detectors

- fakespot-ai/roberta-base-ai-text-detection-v1: human_voice_raw mean 0.0279 (0/6), edited_published_substack mean 0.0273 (0/10), unedited_raw_articles mean 0.1449 (1/8), unedited_claw_drafts mean 0.0520 (0/8 at >=0.5). Misses modern 2026 LLM drafts.
- AICodexLab/answerdotai-ModernBERT-base-ai-detector: human_voice_raw mean 0.0025 (0/6), edited_published_substack mean 0.2609 (3/10), unedited_raw_articles mean 0.1114 (1/8), unedited_claw_drafts mean 0.0001 (0/8). Inverted on edited Substack vs claw-drafts.
- Hello-SimpleAI/chatgpt-detector-roberta: scored 0.0003 on all 8 unedited_claw_drafts and 0.0005 mean on unedited_raw_articles (0/16 detected). Obsolete for post-2023 models.
- slop-tells heuristic (regex/lexicon): human_voice_raw 0.0000, edited_published_substack 0.0560, unedited_raw_articles 0.1814, unedited_claw_drafts 0.0583. Catches overt formatting/cliche tells in raw-articles (AUROC 0.838 vs substack) at 0 MB model RAM, but misses clean-prose 2026 AI slop.

## Exact Scores on Sample Files (voi-slop-detect-380M ONNX q8)

| Group | File | Words | first512 | chunk_mean | chunk_max |
|---|---|---:|---:|---:|---:|
| human_voice_raw | inbox/used/20260226_112618_AlexeyDTC_msg2504_transcript.txt | 183 | 0.0205 | 0.0205 | 0.0205 |
| human_voice_raw | inbox/used/20260831_185020_AlexeyDTC_msg4898_transcript.txt | 152 | 0.0064 | 0.0064 | 0.0064 |
| edited_published_substack | reference/substack/2026-08-14-how-to-do-evals-in-2026.md | 2647 | 0.1170 | 0.2139 | 0.3506 |
| edited_published_substack | reference/substack/2026-10-20-trends-in-agentic-engineering.md | 1907 | 0.3148 | 0.3380 | 0.4670 |
| edited_published_substack | reference/substack/2026-01-30-telegram-assistant.md | 1809 | 0.4458 | 0.3971 | 0.6264 |
| edited_published_substack | reference/substack/2026-05-29-minsearch-the-small-search-library.md | 2292 | 0.7698 | 0.5293 | 0.8028 |
| unedited_raw_articles | articles/raw-articles/benchmarking-sqlitesearch.md | 973 | 0.3310 | 0.2947 | 0.4731 |
| unedited_raw_articles | articles/raw-articles/testing-agents-with-judge-pattern.md | 603 | 0.7956 | 0.4691 | 0.7358 |
| unedited_claw_drafts | articles/claw-drafts/making-a-better-git.md | 3533 | 0.7053 | 0.7094 | 0.9410 |
| unedited_claw_drafts | articles/claw-drafts/context-engineering.md | 1879 | 0.9989 | 0.9132 | 0.9988 |
| unedited_claw_drafts | articles/claw-drafts/ai-skeptic-scorecard.md | 1928 | 0.9996 | 0.8487 | 0.9996 |

Full 32-file scores and metrics are saved in clo/research/voi-slop-detect-380m-eval-2026-11-18.json.

## Comparison with Pangram Baseline and Key Findings

1. Pangram alignment and false-positive rate: At voi-slop-detect-380M's shipped flag_min (0.4256), 6/10 (60%) of Alexey's published Substack articles are flagged. This aligns closely with Alexey's Pangram baseline (~60% AI). On pure human voice transcripts, the false-positive rate is 0/6 (0%).
2. Pure AI slop vs human/edited writing: voi-slop-detect-380M is the only tested lightweight open-source model that reliably detects 2026 LLM drafts (0.9616 mean on claw-drafts vs 0.0154 on human voice, AUROC 1.000). Using chunk_mean across all 512-token chunks achieves AUROC 1.000 between edited_published_substack (max 0.5293) and unedited_claw_drafts (min 0.7094).
3. Raw-articles vs edited Substack: voi-slop-detect-380M only weakly separates articles/raw-articles (mean 0.5074, chunk_mean 0.3801) from reference/substack (mean 0.4519, chunk_mean 0.3637), because both are built from Alexey's brain dumps plus LLM synthesis/editing and sit in the "AI-edited" middle band (0.3 - 0.5).
4. ONNX q8 vs PyTorch bf16: ONNX quantized (428 MB on disk) has only 0.0059 mean absolute score drift (0.0227 max) compared to PyTorch bf16, while using 300 MB less Peak RSS (805.7 MB vs 1106.1 MB) and running ~3x faster per 512-token pass on CPU.

## Integration Feasibility and Recommendation

- Feasibility: Suitable for CPU-only deployment in a 1.5 GB RAM container using onnx/model_quantized.onnx (805.7 MB Peak RSS, 1.84 s cold load, ~3 - 10 s per 512-token chunk). Avoid PyTorch bf16 on CPU (33.3 s/doc, 1106 MB RSS).
- Deployment gotchas: (a) Copy onnx/model_quantized.onnx and onnx/model_quantized.onnx_data into a real directory without huggingface_hub symlinks so onnxruntime external data validation succeeds. (b) In transformers 5.x PyTorch loading, omit trust_remote_code=True (the repo has auto_map in config.json without configuration_ultrabert.py).
- Recommended setup for telegram-writing-assistant: Run voi-slop-detect-380M (ONNX q8) as an async post-/process draft check (not on every incoming message), using a domain-calibrated threshold (chunk_mean >= 0.60 instead of the shipped 0.4256) to keep false positives on Alexey's edited Substack voice at 0% while catching 100% of unedited LLM slop. Pair with the zero-RAM slop-tells regex linter for instant structural/vocabulary checks.
