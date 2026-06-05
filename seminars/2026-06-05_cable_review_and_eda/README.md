# Seminar · 2026-06-05 · Cable Review & EDA

Group meeting talk. ~5 minutes. Two-track narrative:

1. **Ocean engineering** (6 slides) — funnel down from a literature review to
   an actionable research direction.
2. **AI** (3 slides) — the first concrete mini-project: an EDA pipeline on
   public wind SCADA data, as Step 0 of the cable-surrogate roadmap.

## Files

| File | Purpose |
|------|---------|
| `slides_en.pptx` | Final deck delivered at the meeting |
| `speech_notes.md` | Per-slide talking points + term explanations (Chinese) |
| `generate_slides.py` | Reproducible rebuilds — all paths relative to repo root |

## Rebuild the deck

```bash
python seminars/2026-06-05_cable_review_and_eda/generate_slides.py
```

Reads PNGs from `figures/eda_wind_scada/`, writes `slides_en.pptx` next to
the script. Re-run the EDA notebook first if you want fresh figures:

```bash
python code/01_wind_data_eda.py
```

## Slide map

| # | Title | Key idea |
|---|-------|----------|
| 1 | Cover | Diao Jingyu, Seminar 20260605 |
| 2 | Field overview | 6 research areas in Cerik & Huang 2024 → filter to 2 accessible (global / fatigue-global half) |
| 3 | Zoom-in | The 2 accessible areas split into 4 active sub-directions; 3 research gaps as the "question bank" |
| 4 | Our feasible path | Tool-gate funnel → **OrcaFlex global simulation + AI** is the only viable route; 4 AI candidates |
| 5 | Beier 2023 | Inter-array cable fatigue with a simplified stress-factor method — proves OrcaFlex-only fatigue is possible (no UFLEX needed at preliminary stage) |
| 6 | Beyond Beier | 6 extension directions; most promising = bending-Kc correction + NN surrogate |
| 7 | AI mini-project: purpose · data · flowchart | Why this project · what data we use · how the code flows (standard ISO flowchart) |
| 8 | EDA findings (1/2) | Plot 1 daily wind + Plot 2 24-h rolling |
| 9 | EDA findings (2/2) | Plot 3 correlation + Plot 4 power curve |

## Source literature

- Cerik B. C. & Huang L., *Recent advances in mechanical analysis and design
  of dynamic power cables for floating offshore wind turbines*, Ocean
  Engineering 311 (2024).
  → `notes/papers/Recent advances...动力电缆综述.md`
- Beier J. et al., *Fatigue Analysis of Inter-Array Power Cables between Two
  Floating Offshore Wind Turbines Including a Simplified Method to Estimate
  Stress Factors*, JMSE 11(7), 1254 (2023).
  → `notes/papers/Fatigue Analysis of Inter-Array...精读.md`
