# Data Preparation

## Overview

This folder contains the logic used to transform raw datasets into
clinical-grade training data. We have consolidated our scripts into a Master
Notebook to provide a transparent, step-by-step audit trail of how food images
are mapped to carbohydrate values for Type 1 Diabetes (T1D) management.

## The Master Workflow

### master_data_cleaning.ipynb

This notebook serves as the primary orchestrator for the data preparation phase.
It executes the following modular steps to ensure data integrity:

### iFood-2019 Initial Cleaning

    - Input: 1_food_datasets/train_labels.csv

    - Output: IFood2019_processed.csv

    - Description: Cleans headers and standardizes image path references.

### Nutritional Mapping & Release Rates

    - Input: 1_food_datasets/class_list.txt

    - Output: carb_data.csv

    - Description: Maps the 251 food classes to specific carbohydrate counts
    (per 100g) and assigns clinical categories: "Fast Release" (added sugars)
    or "Slow Release" (starchy/complex).

### Gold Standard Dataset Generation

    - Input: IFood2019_processed.csv and carb_data.csv

    - Output: final_training_data_v3_gold.csv

    - Description: Merges image paths, fine-grained labels, and clinical carb
    data into a single, high-veracity training file.

    - Note: Previous iterations (final_training_data.csv) are preserved to
    maintain a complete version history.

### Safety & Audit Validation

    - Input: final_training_data_v3_gold.csv

    - Output: real_audit_results.csv

    - Description: Evaluates the mathematical consistency of the prepared data
    to ensure no errors were introduced during the merge.
