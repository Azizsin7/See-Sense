# Retrospective – Milestone 5: Model Training (See‑Sense)

## Summary

In this milestone, I built and trained the core See‑Sense neural engine using
Transfer Learning (EfficientNetB0) on an NVIDIA RTX 3050 GPU within a WSL2
environment. The trained model maps visual food data to 251 fine-grained
classes with clinical-grade robustness, producing `seesense_fresh_v1.keras`
and a class-index mapping for downstream carbohydrate estimation.

## ✅ What Went Well

- **Hardware-aware engineering:** I implemented mixed-precision training
(16-bit floats for computation, 32-bit for the final layer) to achieve 20–50×
speedup on consumer hardware without sacrificing T1D safety-critical numerical
precision.
- **VRAM protection:** I capped GPU memory at 3.2GB to prevent out-of-memory
crashes on the RTX 3050, enabling stable training on a laptop-class GPU.
- **Transfer learning foundation:** Pre-trained EfficientNetB0 (ImageNet)
provided excellent initial features; I froze BatchNormalization layers to
preserve pre-trained statistics and prevent validation collapse.
- **Clinical data pipeline:** Real-time augmentation (rotations, zoom,
brightness) ensures the model generalizes to real-world conditions (dim
restaurants, varying camera angles, phone photos).
- **Automated quality control:** I implemented `ModelCheckpoint`,
`ReduceLROnPlateau`, and `EarlyStopping` callbacks to avoid overfitting and
capture the best validation checkpoint.
- **Reproducible outputs:** Saved `seesense_fresh_v1.keras`,
`class_indices.json`, and training logs for audit trails and replication.

## ⚠️ What Could Be Improved

- **Class weighting not implemented:** I didn't apply the class weights from
the earlier bucketing analysis to the loss function, which means rare High
Carb classes may still be underweighted during optimization.
- **Per-bucket validation metrics:** I relied on overall validation accuracy
but didn't track precision/recall separately by carb bucket, so I missed early
warning signs of High Carb blind spots.
- **Hyperparameter tuning limited:** Learning rate, batch size, and dropout were
mostly defaults; a proper grid search or Bayesian optimization could improve
convergence.
- **No ablation studies:** I didn't systematically test the impact of
augmentation types, dropout rates, or frozen vs. unfrozen BatchNorm on
final accuracy.
- **Missing deployment readiness:** The model wasn't quantized or converted to
a mobile format (e.g., TFLite), so real-world phone deployment wasn't tested.

## 🚀 Action Items (next steps)

- **Implement per-bucket validation report:** During retraining, log precision,
recall, and F1 per carb bucket; identify any buckets below clinical acceptance
thresholds (target: >90% F1 for High Carb).
- **Apply class weighting:** Integrate the class imbalance weights from
`4_data_analysis` into the loss function (e.g., `class_weight=class_weights`
in Keras) and retrain.
- **Conduct inference benchmarking:** Test inference time on target hardware
(phones, tablets) to ensure real-time performance for clinical deployment.
- **Quantization & mobile export:** Convert `seesense_fresh_v1.keras` to TFLite
format and test on-device accuracy to ensure numerical precision is maintained
for carb estimation.
- **Create a model evaluation dashboard:** Generate a comprehensive report
showing overall accuracy, per-class confusion matrix, per-bucket metrics,
and false-positive/negative rates for high-risk scenarios.
- **Document training reproducibility:** Record exact hyperparameters,
augmentation config, hardware specs, and random seeds to enable retraining
if the model drifts over time.

## What I Learned

- Transfer learning is powerful but not a silver bullet: careful data pipeline
design (augmentation, shuffling, stratification) matters as much as the architecture.
- Consumer hardware is viable for deep learning if you respect memory
constraints and use mixed precision wisely.
- Clinical ML requires different metrics than general computer vision: per-class
accuracy and per-bucket robustness trump overall accuracy when lives depend on
the model.
- Early stopping and callbacks save days of debugging; they're not optional for
clinical-grade training.
