# 5. Model Training: The See-Sense Neural Engine

## Overview

This folder contains the core training logic for the **See-Sense AI**.  
We utilize **Transfer Learning** with the **EfficientNetB0** architecture to
transform visual food data into **clinical carbohydrate estimates**.

The pipeline is engineered to balance **high-performance deep learning** with
the **accessibility of local consumer hardware**.

---

## Training Environment & Compute Power

### WSL2 (Windows Subsystem for Linux)

To achieve professional-grade training on a Windows machine, the model was
trained within a **WSL2 (Ubuntu)** environment. This setup ensures:

- **Native Linux Performance** – High-speed file handling and compatibility with
advanced deep learning libraries  
- **Seamless Integration** – Direct access to Windows-hosted datasets while
utilizing Linux-native GPU drivers  

---

### NVIDIA GPU Acceleration (RTX 3050)

Training for **251 food classes** is computationally expensive. I offload this
complexity to the **NVIDIA GeForce RTX 3050** using:

- **CUDA & cuDNN** – Thousands of CUDA cores accelerate matrix multiplication
via WSL2  
- **Efficiency** – 20×–50× speedup compared to CPU-only training  
- **Tensor Cores** – Leveraged via `mixed_float16` (Mixed Precision) to reduce
training time while maintaining numerical precision required for **T1D safety**

---

## Technical Strategy: *The Script Breakdown*

The training script follows a strict sequence to ensure **hardware stability**
and **clinical accuracy**.

---

### 1. Hardware Protection & Optimization

- **VRAM Protection** – GPU memory is capped at **3.2 GB** to prevent
out-of-memory (OOM) crashes on consumer hardware  
- **Mixed Precision** – Heavy computation uses 16-bit floats, while the final
decision layer remains 32-bit for numerical stability  

This delivers **professional-grade performance** on a laptop-class GPU without
sacrificing accuracy.

---

### 2. The Model: EfficientNetB0

- **Backbone** – EfficientNetB0 pre-trained on ImageNet for optimal
efficiency-to-accuracy ratio  
- **BatchNorm Freeze ("Anti-Cheat Lock")** – All BatchNormalization layers are
frozen to preserve pre-trained statistics and prevent validation collapse  
- **Custom Head**
  - Global Average Pooling  
  - Dropout (`0.4`) for overfitting mitigation  
  - Dense layer (`512` units) mapping visual features to nutritional predictions

---

### 3. Clinical Robustness (Data Pipeline)

- **Data Shuffling** – `df.sample(frac=1)` ensures the validation set is a
balanced cross-section of all food types  
- **Augmentation** – Real-time rotations, zoom, and brightness adjustments
enable robust recognition in:
  - Dim restaurants  
  - Varying camera angles  
  - Real-world lighting conditions  

---

## The Training Pipeline

### Input / Output

| File                     | Role                                              |
|--------------------------|---------------------------------------------------|
| `final_training_data.csv`| Input – Gold-standard prepared dataset            |
| `seesense_fresh_v1.keras`| Output – Trained model weights (“The Brain”)      |
| `class_indices.json`     |Mapping from numerical indices to food classes     |

---

### 📉 Training Callbacks (Automated Quality Control)

- **ModelCheckpoint** – Saves only the model with the highest validation
accuracy  
- **ReduceLROnPlateau** – Lowers learning rate when improvement stalls  
- **EarlyStopping** – Halts training when performance plateaus to prevent
overfitting  

---

- Safety Note

This model is the primary engine for carbohydrate estimation.
The combination of WSL2 stability and EfficientNet accuracy is intentionally
designed to minimize margin-of-error in clinical T1D scenarios.
