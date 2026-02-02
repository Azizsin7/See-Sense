# Food Datasets: The Foundation of See-Sense

## Overview

This folder contains the raw and processed data used to train and validate the
See-Sense food recognition model. In accordance with our core research
principles, raw data is kept in its original state to ensure full
reproducibility for future clinical audits or medical research.

Dataset & Requirements
The raw image data (2.52GB) is hosted on Kaggle to ensure high-speed delivery
and version control.

1. **Download:** [See-Sense Dataset on Kaggle](https://shorturl.at/vflxE)
2. **Setup:** Unzip the contents into the `1_food_datasets/` folder.
3. **Verify:** Ensure your directory looks like this:

   ```text

    1_food_datasets/
        ├── IFood2019/
        │   ├── train_set/          # ~100k images
        │   ├── val_set/            # ~12k images
        │   ├── class_list.txt      # ID to Food Name mapping
        │   ├── train_labels.csv    # Image ID -> Class ID
        │   └── val_labels.csv      # Image ID -> Class ID
    ```

## Dataset: iFood-2019 (FGVC6)

The primary dataset utilized is the iFood-2019, curated for the Fine-Grained
Visual Categorization (FGVC) challenge. This dataset was selected because it
provides the granular detail necessary for medical-grade carbohydrate
estimation rather than broad, non-specific food categories.
[iFood-2019](https://www.kaggle.com/c/ifood-2019-fgvc6/overview)

## Data Classification

### 📂 train_set

    - Type: Unstructured (Images)

    - Contents: Thousands of images across 251 fine-grained food classes.

    - T1D Relevance: Provides the visual diversity (lighting, angles, plating)
    necessary for the model to recognize foods in real-world dining scenarios,
    reducing the risk of misidentification which could lead to incorrect
    insulin dosing.

### 📂 val_set

    - Type: Unstructured (Images)

    - Contents: A separate set of images used to test the model’s accuracy on
    unseen data.

    - T1D Relevance: Critical for ensuring the model does not "memorize" specific
    images but actually learns to identify the glucose-influencing agents
    correctly across new and varied meal presentations.

### 📄 class_list.txt

    - Type: Metadata / Structured

    - Description: A mapping file linking numerical Class IDs to human-readable
    food names.

    - Note: This file serves as the "Source of Truth" for the 251 categories
    supported by the model.

### 📄 train_labels.csv & val_labels.csv

    - Type: Structured (Tabular)

    - Format: .csv

    - Columns: image_name, label

    - T1D Relevance: These labels act as the "Gold Standard." In T1D management,
    mislabeling a high-carb item as a low-carb item is a significant medical
    risk; therefore, these labels are treated as high-veracity clinical targets.
