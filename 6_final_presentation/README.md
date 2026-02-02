# Final Presentation & Project Results

This folder contains the final output of the **See-Sense** project, designed
to showcase the system's ability to classify food and audit carbohydrate
content for Type 1 Diabetes safety.

---

## Presentation Assets

### 1. Main Presentation

* **File:** `see-sense.pptx`
* **Content:** Detailed slides covering the project lifecycle:

### 2. Live Demo

* **File:** `live_demo.py`
* **Purpose:** A real-time inference script to demonstrate the model's
performance.
* **Usage:**

```powershell
    python 6_final_presentation/live_demo.py
```

* **Features:** * Real-time image loading and preprocessing.
  * Top-K class predictions.
  * Display of associated carbohydrate values per 100g based on the
  `final_training_data`.

---

## Prerequisites for Demo

Ensure the following are available before starting the live demo:

* **Model File:** `5_model_training/seesense_fresh_v1.keras`
* **Label Map:** `5_model_training/class_indices.json`
* **Environment:** Activated `T1Dc_win` or `seesense_env`.
