#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2026-01-05

@author: Aziz Azizi
"""

import os
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Setup Paths
SCRIPT_DIR = Path(os.getcwd())
PROJECT_ROOT = SCRIPT_DIR if SCRIPT_DIR.name == "See-Sense" else SCRIPT_DIR.parent

# Data Path
CSV_PATH = PROJECT_ROOT / "2_data_preparation" / "final_training_data_v3_gold.csv"

# Output Path
OUTPUT_DIR = PROJECT_ROOT / "4_data_analysis"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Data
if not CSV_PATH.exists():
    CSV_PATH = PROJECT_ROOT / "2_data_preparation" / "final_training_data.csv"

print(f"Loading data from: {CSV_PATH}")
df = pd.read_csv(CSV_PATH)


# Define Clinical Bucketing Logic
def get_bucket(carbs):
    if carbs <= 5:
        return "1. Keto/Very Low (0-5g)"
    if carbs <= 15:
        return "2. Low Carb (6-15g)"
    if carbs <= 30:
        return "3. Medium Carb (16-30g)"
    return "4. High Carb (31g+)"


df["carb_category"] = df["carbs_per_100g"].apply(get_bucket)

# Visualization
plt.figure(figsize=(10, 6))
category_order = sorted(df["carb_category"].unique())

sns.countplot(data=df, x="carb_category", order=category_order, palette="RdYlGn_r")

plt.title("T1D Safety Audit: Image Distribution by Carb Bucket")
plt.xlabel("Clinical Carbohydrate Category")
plt.ylabel("Total Training Images")
plt.xticks(rotation=15)
plt.tight_layout()

plot_output = OUTPUT_DIR / "carb_bucket_distribution.png"
plt.savefig(plot_output)
print(f"Distribution plot saved to: {plot_output}")

# Summary Statistics
print("\n--- Dataset Balance Summary ---")
summary = df["carb_category"].value_counts().sort_index()
print(summary)

summary.to_csv(OUTPUT_DIR / "bucket_summary_report.csv")
print(f"Report saved to: {OUTPUT_DIR / 'bucket_summary_report.csv'}")
