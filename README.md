# FOWT Dynamic Power Cable — AI Surrogate Model Portfolio

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-2.x-green)

## 概要（日本語）

浮体式洋上風力発電機（FOWT）動力電源ケーブルの疲労・動力応答を予測する機械学習代理モデルの実装ポートフォリオです。

OrcaFlex 時域シミュレーションデータを用いて CNN-GRU サロゲートモデルを構築し、リアルタイム疲労状態推定を実現します（Marine Structures 2024, R²=0.9864 の手法を PyTorch で実装）。

**キーワード**：Lazy-Wave Cable, Fatigue Surrogate Model, CNN-GRU, XGBoost, Lumada APM

## Overview (English)

Machine learning surrogate model portfolio for predicting fatigue damage and dynamic response of FOWT dynamic power cables. Implements CNN-GRU architecture from Marine Structures 2024 using PyTorch, with XGBoost baseline and Streamlit monitoring dashboard.

## Code

| # | Script | Description | Status |
|---|--------|-------------|--------|
| 01 | `code/01_wind_data_eda.py` | Wind SCADA EDA (Kaggle T1.csv) | ✅ |
| 02 | `code/02_fatigue_surrogate_XGBoost.ipynb` | XGBoost fatigue surrogate (→ B-14) | 🔲 |
| 03 | `code/03_seabed_ML_prediction.ipynb` | Seabed parameter ML (→ B-20) | 🔲 |
| 04 | `code/04_lstm_cable_tension.ipynb` | LSTM cable tension time-series | 🔲 |
| 05 | `code/05_CNN_GRU_cable_surrogate.ipynb` | **CNN-GRU core model (→ B-13)** | 🔲 |
| 06 | `code/06_cable_health_monitor_demo/` | Streamlit Dashboard + LLM Report | 🔲 |

## Tech Stack

- **Simulation**: OrcaFlex (Python API)
- **ML**: XGBoost, PyTorch (CNN-GRU, LSTM, Autoencoder)
- **Explainability**: SHAP
- **Fatigue**: fatpack (Rainflow counting)
- **Dashboard**: Streamlit
- **LLM Report**: Claude API (Anthropic)

## Repository Layout

```
.
├── code/             # All Python scripts and notebooks
├── notes/
│   ├── papers/       # Paper reading notes (one .md per paper)
│   └── learning/     # Self-study notes: concepts, cheatsheets, walkthroughs
├── figures/          # Visual outputs from analyses
├── seminars/         # Time-stamped group-meeting deliverables
│                     #   <YYYY-MM-DD>_<topic>/  ← dates only in folder name
├── _local/           # Gitignored container — never pushed
│   ├── data/         #   raw datasets (CSV, OrcaFlex .sim)
│   └── pdfs/         #   literature PDFs
└── LOG.md            # Session-by-session progress log
```

Why not date-named folders? **Git already tracks time.** Folders carry
**content**. Only `seminars/` and `LOG.md` are date-aware because they
archive time-stamped events.

Why `_local/`? Everything that must stay on disk but never leave the
machine (raw CSVs, PDFs, private OrcaFlex outputs) lives under a single
underscore-prefixed folder. One look at the repo root tells you what is
pushed (no leading underscore) versus what is local (`_local/`).

## Progress

See [`LOG.md`](./LOG.md) — newest entry on top.

---

*Research direction: FOWT dynamic cable lazy-wave configuration × ML surrogate model (M1, Yokohama National University)*
