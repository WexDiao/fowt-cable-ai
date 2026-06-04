# Progress Log

Running log of meaningful sessions. Newest entry on top. One bullet per
thing that actually got *done* (commits, deliverables, decisions) — not
intentions.

For the why behind a session, look at the linked PR / commit / file.

---

## 2026-06-05 · Seminar delivered + repo reorganised

- 🎤 Delivered group-meeting talk (9-slide English deck, ~5 min)
  → `seminars/2026-06-05_cable_review_and_eda/`
- 🛠 First AI mini-project complete: end-to-end EDA on Kaggle SCADA T1.csv
  → `notebooks/01_wind_data_eda.py` (8 PNGs in `figures/eda_wind_scada/`)
- 📓 Code walkthrough doc written: `notes/concepts/eda_code_walkthrough.md`
- 📓 Concept notes added:
  `notes/concepts/python_data_stack_cheatsheet.md`,
  `notes/concepts/dynamic_cable_basics.md`,
  `notes/concepts/kaggle_scada_setup.md`
- 🗂 Added top-level `seminars/` folder for time-stamped talks
  (dates live in folder name, not in repo structure)
- 📌 Decided research direction = **OrcaFlex global simulation + AI**
  (Beier 2023 simplified stress factor → bending-Kc correction via NN +
  full surrogate model as 12-week target)

---

## How to use this file

- Add a new section at the top whenever you finish a meaningful chunk
- Date as H2 (`## YYYY-MM-DD · short title`)
- Bullets describe *what was completed*, link to file or commit
- Use emojis sparingly as visual anchors: 🎤 talks · 🛠 code · 📓 notes ·
  📌 decisions · 🐛 bugs fixed · 🔬 experiments
- Keep entries terse — the diffs are in git, this file is the index
