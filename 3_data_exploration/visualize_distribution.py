#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2026-01-04

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
OUTPUT_DIR = PROJECT_ROOT / "3_data_exploration"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Data
if not CSV_PATH.exists():
    print(f"Error: Could not find CSV at {CSV_PATH}")
    CSV_PATH = Path("2_data_preparation/final_training_data_v3_gold.csv")

df = pd.read_csv(CSV_PATH)

# Distribution of Carbohydrates
plt.figure(figsize=(10, 6))
sns.histplot(df["carbs_per_100g"], bins=20, kde=True, color="skyblue")
plt.title("Distribution of Carbohydrate Values")
plt.xlabel("Carbs per 100g")
plt.ylabel("Number of Images")
plt.savefig(OUTPUT_DIR / "carb_histogram.png")
print(f"Saved: {OUTPUT_DIR / 'carb_histogram.png'}")

# Top 20 Most Frequent Categories
plt.figure(figsize=(12, 8))
top_20 = df["food_name"].value_counts().head(20)
sns.barplot(
    x=top_20.values, y=top_20.index, hue=top_20.index, palette="viridis", legend=False
)
plt.title("Top 20 Food Categories by Image Count")
plt.xlabel("Number of Images")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "class_counts.png")
print(f"Saved: {OUTPUT_DIR / 'class_counts.png'}")

# Highest Carb Foods
plt.figure(figsize=(12, 8))
high_carb = (
    df[["food_name", "carbs_per_100g"]]
    .drop_duplicates()
    .sort_values("carbs_per_100g", ascending=False)
    .head(20)
)
sns.barplot(
    x="carbs_per_100g",
    y="food_name",
    data=high_carb,
    hue="food_name",
    palette="Reds_r",
    legend=False,
)
plt.title("Top 20 Highest Carbohydrate Foods (g/100g)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "high_carb_foods.png")
print(f"Saved: {OUTPUT_DIR / 'high_carb_foods.png'}")

print("\nAnalysis Complete")
print(f"Total Unique Classes: {df['food_name'].nunique()}")
print(f"Average Carb Value: {df['carbs_per_100g'].mean():.2f}g")
