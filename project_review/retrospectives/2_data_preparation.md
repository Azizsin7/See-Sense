# Retrospective – Milestone 2: Data Preparation (See‑Sense)

## Summary

In this milestone, I transformed raw iFood‑2019 images and labels into a
clinical-grade training dataset. I built a master cleaning notebook that
maps 251 food classes to carbohydrate values, assigns clinical release-rate
categories, and generates a validated "gold standard" training file with full
audit traceability.

## ✅ What Went Well

- **Modular pipeline:** I structured the master notebook into clear, auditable
steps (initial cleaning → nutritional mapping → merge → validation), making it
easy to trace any issue back to its source.
- **Clinical mapping:** I created `carb_data.csv` linking all 251 classes to
per-100g carb values and "Fast Release" vs "Slow Release" categories, grounding
the dataset in T1D clinical context.
- **Gold standard generation:** I merged image paths, fine-grained labels, and
carb data into `final_training_data_v3_gold.csv`, ensuring every row links an
image to both a food class and a carb count.
- **Audit trail:** I ran consistency checks in `real_audit_results.csv` to catch
missing values, mismatches, and data integrity errors before training.
- **Version control:** I preserved earlier versions (`final_training_data.csv`)
to maintain a full history and enable reproducibility.

## ⚠️ What Could Be Improved

- **Carb value sourcing:** I used reference values from NHS/USDA guidelines,
but some foods (especially regional dishes) lacked precise carb data; manual
clinical review or empirical testing would have been ideal.
- **Portion standardization:** Images in iFood‑2019 vary in portion size;
I didn't implement portion-detection logic, so all carb estimates assume a
fixed reference serving.
- **Error handling:** The master notebook lacked graceful fallbacks for missing
class mappings or label mismatches; adding explicit error logs would help
diagnose failures faster.
- **Performance profiling:** I didn't measure processing time or memory usage;
for much larger datasets, this could become a bottleneck.

## 🚀 Action Items (next steps)

- Add explicit error logs and warnings to the master notebook (e.g.,
"Missing class mapping for class_id 42") to speed up debugging.
- Implement a portion-detection step or add a "portion_multiplier" column for
images with non-standard serving sizes.
- Run the full pipeline once more end-to-end to confirm reproducibility for a
fresh user.

## What I Learned

- Data cleaning and mapping are 80% of the work; the raw dataset had far more
inconsistencies than I expected.
- Clinical datasets require stricter validation than general ML projects; every
carb value and class label carries medical weight.
- Keeping an audit trail (intermediate files, validation results) is invaluable
for debugging and trust-building later.
