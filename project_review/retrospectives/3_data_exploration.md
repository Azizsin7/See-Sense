# Retrospective – Milestone 3: Data Exploration (See‑Sense)

## Summary

In this milestone, I explored the "Gold Standard" dataset to audit its
statistical distribution before model training. I created three key
visualizations (carbohydrate distribution, class balance, high-carb foods)
to identify dataset biases and ensure the model won't develop blind spots
that could lead to clinical dosing errors.

## ✅ What Went Well

- **Clinical-first exploration:** I framed every visualization around T1D
risk—not just accuracy metrics. Each chart answered: "Will the model recognize
high-risk foods?" and "Is my dataset skewed?"
- **Three focused visualizations:** I created:
  - **Carb histogram:** Shows the frequency distribution of carbohydrate
  densities, revealing if the dataset covers the full glycemic spectrum.
  - **Class balance chart:** Top-20 food classes by image count, flagging
  severe class imbalance (e.g., 1,000 pizza images vs. 10 lentil images).
  - **High-carb foods chart:** Ranks foods by carb density per 100g,
  highlighting the "non-negotiable" high-risk items requiring perfect accuracy.
- **Reusable script:** `visualize_distribution.py` is modular and can be re-run
on updated datasets without modification.
- **No data mutation:** I kept the gold-standard dataset pristine throughout
exploration.

## ⚠️ What Could Be Improved

- **Statistical rigor:** I relied mainly on counts and histograms; I skipped
deeper distributions (quantiles, skewness tests, outlier analysis) that might
have surfaced hidden patterns.
- **Class imbalance quantification:** I didn't compute a formal imbalance metric
(e.g., Gini coefficient, max/min class ratio) to make imbalance severity
concrete.
- **Correlation analysis:** I didn't explore whether high-carb foods cluster
together visually (e.g., similar colors, textures) or if they're visually
diverse—this would affect model generalization.
- **Missing data audit:** I didn't explicitly check for missing carb values or
mislabeled entries that might bias exploration.

## 🚀 Action Items (next steps)

- Add a "class imbalance report" to quantify the severity (e.g., "Class
imbalance ratio: 100:1").
- Implement stratified sampling or class weighting recommendations based on
observed imbalance.
- Add a "missing/suspicious data" check to flag any null or inconsistent
values early.
- Document any dataset limitations discovered (e.g., "Pizza dominates; rare
foods underrepresented").

## What I Learned

- Exploratory analysis is not just descriptive—it's a risk audit. Every
visualization must ask: "What could go wrong clinically?"
- Class imbalance can be hidden in raw counts; I need better metrics to make
it actionable.
- Visualization clarity matters: simple, labeled charts are better than dense
dashboards for communicating findings to clinicians.
