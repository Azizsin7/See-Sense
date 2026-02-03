# See-Sense: AI-Driven Carbohydrate Estimation for Type 1 Diabetes Management

> * Smart food recognition powered by computer vision to reduce the cognitive
burden of carbohydrate counting for people with Type 1 Diabetes.

---

## 📋 Table of Contents

* [Overview](#overview)
* [Project Goals](#project-goals)
* [Key Features](#key-features)
* [Technical Architecture](#technical-architecture)
* [Installation](#installation)
* [Quick Start](#quick-start)
* [Project Structure](#project-structure)
* [Model Performance](#model-performance)
* [Safety and Clinical Validation](#safety-and-clinical-validation)
* [Usage Examples](#usage-examples)
* [License](#license)
* [Contact and Support](#contact-and-support)

---

## Overview

**See-Sense** is a research-driven AI system that leverages computer vision to
automatically identify food items and estimate their carbohydrate content.
Designed specifically for the Type 1 Diabetes (T1D) community, it aims to
reduce the mental burden of manual carbohydrate counting—a critical component
of insulin dosing.

### Research Question

> * How effectively can computer vision models (EfficientNetB0) identify food
items and provide accurate carbohydrate values for insulin dosing, when audited
against clinical safety buckets?*

---

## Project Goals

1. **Build a Gold Standard Dataset** - Create a high-quality, clinically
validated food dataset free from imposter images and labeling errors
2. **Optimize for Consumer Hardware** - Deploy efficient models on
consumer-grade GPUs (e.g., RTX 3050 series)
3. **Ensure Clinical Safety** - Audit model predictions against established
carbohydrate bucketing logic:
   * **Keto** (0-5g)
   * **Low** (5-20g)
   * **Medium** (20-50g)
   * **High** (>50g)
4. **Improve Model Accuracy** - Achieve high classification precision and
carbohydrate estimation accuracy
5. **Create User-Friendly Applications** - Provide real-time food recognition
via camera interface

---

## Key Features

* **EfficientNetB0-Based Classification** - Lightweight yet powerful deep
learning backbone
* **Real-Time Camera Integration** - Live food recognition with instant
carbohydrate estimates
* **Gold Standard Dataset** - Manually curated and clinically validated food
images
* **Mixed Precision Training** - FP16 optimization for efficient VRAM usage
* **Clinical Safety Auditing** - Carbohydrate bucket validation for insulin
dosing confidence
* **Modular Pipeline** - Organized workflow from data preparation through model
deployment

---

## Technical Architecture

### Tech Stack

| Component | Technology |
| ----------- | ----------- |
| **Deep Learning Framework** | TensorFlow 2.15+ / Keras |
| **Computer Vision** | OpenCV, Pillow |
| **Data Processing** | Pandas, NumPy |
| **Model Optimization** | Mixed Precision (FP16), Memory Limiting |
| **Visualization** | Matplotlib, Seaborn |
| **Interface** | Tkinter (GUI), OpenCV (Real-time video) |
| **Hardware Target** | NVIDIA RTX 3050/3000 series (3.2GB VRAM) |

### Model Architecture

* **Backbone**: EfficientNetB0 pre-trained on ImageNet
* **Training Strategy**: Transfer Learning with fine-tuning
* **Loss Function**: Categorical Cross-Entropy
* **Optimization**: Adam with ReduceLROnPlateau
* **Callbacks**: ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
* **Memory Management**: Mixed precision (FP16) for VRAM efficiency

---

## Installation

### Prerequisites

* Python 3.8+
* NVIDIA GPU with CUDA support (optional but recommended)
* 8GB+ RAM
* 20GB+ disk space for datasets

* **Dataset & Requirements**
The raw image data (2.52GB) is hosted on Kaggle to ensure high-speed delivery
and version control.

1. **Download:** [See-Sense Dataset on Kaggle](https://shorturl.at/vflxE)
2. **Setup:** Unzip the contents into the `1_food_datasets/` folder.
3. **Verify:** Ensure your directory looks like this:

   ```bash

    1_food_datasets/

        ├── IFood2019/
        │   ├── train_set/          # ~100k images
        │   ├── val_set/            # ~12k images
        │   ├── class_list.txt      # ID to Food Name mapping
        │   ├── train_labels.csv    # Image ID -> Class ID
        │   └── val_labels.csv      # Image ID -> Class ID
    ```

### Setup Instructions

  1. **Create a virtual environment**

  Windows:

  ```powershell
  python -m venv T1Dc_win
  .\T1Dc_win\Scripts\activate
  ```

  Linux

  ```bash
  python3 -m venv T1Dc
  source T1Dc/bin/activate
  ```

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Verify TensorFlow GPU support** (optional)

   ```bash
   python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
   ```

---

## Quick Start

### Run the Live Camera Demo

Experience real-time food recognition:

```bash
cd 6_final_presentation
python "Live Camera.py"
```

This launches an interactive camera interface where you can:

* Point your camera at food items
* See real-time predictions with confidence scores
* View estimated carbohydrate values
* Verify safety bucket classifications

---

## Project Structure

```bash
See-Sense/
├── 0_domain_study/           # Research and background literature
├── 1_food_datasets/          # Raw dataset collections (IFood2019)
├── 2_data_preparation/       # Data cleaning, preprocessing, and labeling
│   ├── master_data_cleaning.ipynb
│   └── final_training_data_v3_gold.csv  # Gold standard dataset
├── 3_data_exploration/       # EDA, visualization, and analysis
├── 4_data_analysis/          # Carbohydrate bucketing analysis
├── 5_model_training/         # Model training and evaluation
│   ├── training_model_V3.py
│   ├── real_test.py
│   └── seesense_fresh_v1.keras  # Trained model
├── 6_final_presentation/     # User-facing applications
│   └── Live Camera.py        # Real-time inference interface
├── project_review/           # Project retrospectives, constraints, guides
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── CONTRIBUTING.md           # Contribution guidelines
```

---

## Model Performance

| Metric | Value |
| -------- | ------- |
| **Architecture** | EfficientNetB0 |
| **Training Dataset** | ~5,000+ validated images |
| **Optimization** | Mixed Precision (FP16) |
| **Model Size** | 91.9MB |
| **Inference Speed** | <100ms per image (RTX 3050) |
| **Memory Usage** | 3.2GB VRAM (limited) |

* Performance metrics subject to dataset and training configuration. See
`5_model_training/README.md` for detailed benchmarks.

---

## Safety and Clinical Validation

### Carbohydrate Safety Buckets

Model predictions are validated against clinically-defined carbohydrate ranges:

| Bucket | Carbs (g) | Clinical Use |
| -------- | ----------- | -------------- |
| **Keto** | 0-5 | Low/no carbs |
| **Low** | 5-20 | Minimal insulin |
| **Medium** | 20-50 | Standard coverage |
| **High** | >50 | Higher dosing |

### Safety Auditing Process

1. Model predicts carbohydrate range
2. Prediction is mapped to safety bucket
3. Clinical audit validates bucket accuracy
4. Results logged for model improvement

---

## Usage Examples

### Example 1: Identify Food from Image File

```python
import tensorflow as tf
import cv2

model = tf.keras.models.load_model('5_model_training/seesense_fresh_v1.keras')
image = cv2.imread('food_image.jpg')
# Preprocess and predict
prediction = model.predict(image)
```

### Example 2: Real-Time Camera Feed

Launch the interactive camera demo:

```bash
cd 6_final_presentation
python "Live Camera.py"
```

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE)
file for details.

---

## Contact and Support

### Project Author

#### Aziz Azizi

* GitHub: [@Azizsin7](https://github.com/Azizsin7)
* Email: [Contact via GitHub](https://github.com/Azizsin7)

### Support

* **Issues & Bug Reports**: [GitHub Issues](https://github.com/Azizsin7/See-Sense/issues)
* **Documentation**: See [README](README.md) and module-specific READMEs
* **Questions**: Open a Discussion or Issue on GitHub

---

## Acknowledgments

* **Dataset**: IFood2019 dataset used as foundation
* **Model**: EfficientNetB0 architecture by Google Brain
* **Community**: Type 1 Diabetes research and engineering community

---

## Additional Resources

* [Contributing Guide](CONTRIBUTING.md)
* [Domain Study](0_domain_study/README.md)
* [Data Preparation Guide](2_data_preparation/README.md)
* [Model Training Guide](5_model_training/README.md)
* [Data Exploration Guide](3_data_exploration/README.md)

---

**Last Updated**: January 30, 2026  
**Status**: Active Development
