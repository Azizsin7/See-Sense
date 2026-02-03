# Retrospective – Milestone 1: Food Datasets

## Summary

In this milestone, I sourced and structured the foundational datasets for
See‑Sense. I selected iFood‑2019 from Kaggle as the primary dataset and set
up a reproducible data pipeline, ensuring raw data integrity and proper
documentation for future clinical audits and research replication.

## ✅ What Went Well

- **Dataset selection:** I identified iFood‑2019 (FGVC6) as the right choice—251
fine‑grained food classes with sufficient visual diversity across lighting,
angles, and plating to capture real‑world dining scenarios.
- **Reproducibility first:** I kept raw datasets unmodified and hosted them on
Kaggle, ensuring anyone can replicate the work without data loss or version
conflicts.
- **Clear metadata:** I created a well‑documented folder structure with
`class_list.txt`, `train_labels.csv`, and `val_labels.csv` to establish a
reliable "source of truth" for food categories and labels.
- **T1D framing:** Throughout the process, I tied every dataset decision back
to clinical relevance—reminding myself that mislabeling high‑carb as low‑carb
carries real medical risk.

## ⚠️ What Could Be Improved

- **Carb enrichment:** iFood‑2019 provides food class labels, but I lacked
automated mapping to reliable carbohydrate values; manual carb annotation
for each class would have been ideal but was time‑constrained.
- **Portion standardization:** The dataset images vary in portion size and
plating style, making it harder to estimate actual carb intake without
additional portion‑detection work.
- **Data augmentation documentation:** I didn't fully plan ahead for how to
augment the training data (rotations, crops, lighting shifts) to improve model
robustness to real‑world photos.
- **Local audit samples:** I didn't set aside a small, clinically audited subset
(20–50 images) with verified carb labels for later safety validation.

## 🚀 Action Items (next steps)

- Create a `carb_data.csv` for each of the 251 classes, linking food names
to reference carb values (from USDA or NHS guidelines).
- Build a small audit set (50 images, 5–10 popular classes) with human‑verified
carb labels to test model predictions against ground truth later.
- Test download and setup from Kaggle to confirm the full pipeline works for a
new user.

## What I Learned

- Fine‑grained classification (251 classes) is much harder than broad categories
but essential for clinical carb accuracy.
- Keeping raw data pristine and hosting it separately (Kaggle) is worth the
extra step—it's non‑negotiable for medical research.
- Metadata (labels, class definitions) is as important as the images themselves;
investing early in clear, consistent labeling saves rework later.
