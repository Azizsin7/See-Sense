# Retrospective – Milestone 4: Data Analysis (See‑Sense)

## Summary

In this milestone, I audited the dataset for clinical safety using
carbohydrate-based bucketing. I created the `carb_bucket.py` script to
categorize the 251 food classes into four clinical tiers (Keto/Very Low, Low,
Medium, High Carb) and generated a distribution audit to identify any "clinical
blind spots" where the model might under-estimate carb value.

## ✅ What Went Well

- **Clinical categorization logic:** I defined four carb-impact buckets—not
arbitrary; each tier reflects real T1D dosing scenarios (0–5g minimal,
31g+ high-risk).
- **Automated auditing:** `carb_bucket.py` classifies all 251 classes and
generates `carb_bucket_distribution.png`, making it easy to spot imbalances
at a glance.
- **Safety framing:** Every analysis asked: "Will the model recognize
high-risk foods?" rather than generic accuracy metrics.
- **Reproducibility:** The script reads from the gold-standard dataset and
produces consistent, auditable outputs.
- **Identified skew:** The audit revealed which carb buckets are
underrepresented—actionable insight for the next stage.

## ⚠️ What Could Be Improved

- **Class balancing not addressed:** I identified the imbalance but didn't
propose fixes (e.g., synthetic data augmentation, class weighting) at this
stage.
- **Missing per-bucket accuracy targets:** I didn't define clinical minimum
accuracy requirements per bucket (e.g., "High Carb bucket must achieve >95% F1").
- **No stratification by food type:** High-carb items include sweets, grains,
and starches—visually diverse. I didn't analyze if the imbalance clusters by
subtype.
- **Limited sensitivity analysis:** I didn't test how robust the bucketing is
to measurement error (e.g., ±2g carb variance).

## 🚀 Action Items (next steps)

- **Implement class weighting:** Use `carb_bucket.py` output to calculate
class weights in the training loss function (higher weight for underrepresented
High Carb classes).
- **Define per-bucket validation metrics:** Create a validation report tracking
accuracy, precision, and recall per bucket during training to catch clinical
blind spots early.
- **Stratified train/val split:** Ensure training and validation sets mirror
the bucket distribution to prevent validation collapse on rare classes.
- **Augmentation strategy for imbalanced buckets:** Plan additional data
augmentation (rotations, brightness, zoom) for underrepresented High Carb
food images to boost effective training samples.
- **Threshold tuning:** After training, apply bucket-specific confidence
thresholds (e.g., require higher confidence for rare High Carb predictions
to minimize false positives).

## What I Learned

- Clinical auditing is not just about numbers—it's about identifying where
the model will fail in the real world.
- Imbalanced data in medical ML is dangerous: the model will optimize for the
common case (low-carb foods) at the expense of rare but critical cases
(high-carb/high-risk meals).
- Bucketing simplifies communication: clinicians can understand "High Carb
bucket" better than abstract class indices.
