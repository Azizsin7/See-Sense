# Notes

## Challenges

This folder documents the technical journey of the **See-Sense** project,
tracking the evolution of the dataset and the training iterations.

---

## Data Acquisition & Cleaning Issues

### **Data Integrity (The "Gold" Dataset)**

* The Issue: Training failed repeatedly with UnimplementedError or
InvalidArgumentError mid-epoch.

* The Discovery: We found Corrupted/Imposter Images. These were files that:

  * Had a .jpg extension but were actually empty or contained HTML error text.

  * Were truncated (half-downloaded), causing the PIL (Pillow) loader to crash.

  * Used color spaces (like CMYK) that TensorFlow's decode_jpeg couldn't
  handle, leading to "ghost" errors that only appeared after 2–3 hours of training.

* The Solution: I built a rigorous cleaning pipeline to generate
final_training_data_v3_gold.csv. This involved:

  * The "Imposter" Filter: A script that physically opened every image file
  using PIL.Image.open() and image.verify() to ensure the data was a valid,
  readable image before adding it to the CSV.

  * Path Standardization: Converted all Windows backslashes (\) to universal
  forward slashes (/) so the model could train on Linux, Windows, or Cloud
  environments without modification.

  * Label Verification: Cross-referencing image IDs with the master
  nutrition list to ensure "Apple" images weren't being fed into the
  model with "Pizza" carb values.

* Impact: Before this cleaning, the model had 0% progress because it crashed
every single time it hit a bad file. After the "Gold" dataset was finalized,
the model successfully completed its first full 25-epoch run.

---

## Training & Hardware Optimization

### **1. VRAM Management (RTX 3050)**

* **Issue:** The model would crash with "Out of Memory" (OOM) errors.
* **Solution:** * Limited GPU growth to **3.2GB**.
  * Implemented **Mixed Precision (FP16)** via `mixed_float16` to speed up
  training and reduce memory footprint.

### **2. The "Anti-Cheat" Safety Lock**

* **Issue:** Validation accuracy often plummeted when fine-tuning EfficientNet.
* **Solution:** Manually froze all `BatchNormalization` layers to preserve
pre-trained ImageNet statistics during the first phase of training.

---

## Model Training History

We iterated through multiple training sessions to find the best balance between
accuracy and clinical safety.

| Model Version | Architecture | Optimization | Accuracy | Status |
| :--- | :--- | :--- | :--- | :--- |
| v1 (Baseline) | EfficientNetB0 | Default | ~50% | High Overfit |
| v3 (Mixed) | EfficientNetB0 | Mixed Precision | ~70% | Faster Training |
| v2 (Balanced) | EfficientNetB0 | Dropout 0.4 + BN Freeze | ~73% | Current |

> **Note:** Final metrics are saved in `5_model_training/` alongside the
`.keras` model files.

---

## Key Learnings

* **Data Quality > Model Complexity:** Spending time on the `v3_gold` CSV was
more impactful than tweaking hyperparameters.
* **Hardware Constraints:** Learning to work within a 4GB VRAM limit forced
better efficiency in batch sizing and image preprocessing.
