# Data Exploration: Visualizing the Glycemic Landscape

## Overview

This folder contains the analytical scripts and visualizations used to audit the
"Gold Standard" dataset. Before training the model, I must understand the
statistical distribution of my data to ensure the AI doesn't develop biases
that could lead to clinical dosing errors in Type 1 Diabetes (T1D) management.

## Exploratory Analysis Script

### [visualize_distribution](visualize_distribution.py)

This script performs a deep dive into the final_training_data_v3_gold.csv to
extract clinical insights. It generates three key visualizations that define
our training health:

#### 1. Carbohydrate Distribution (Histogram)

Filename: [carb_histogram](carb_histogram.png)

Analysis: Visualizes the frequency of different carbohydrate densities across
the entire dataset.

Description: Helps identify if our dataset is skewed toward "hidden carbs"
or low-carb options, ensuring the model is well-exposed to the full spectrum of
glycemic impacts.

#### 2. Class Balance (Top 20 Categories)

Filename: [class_counts](class_counts.png)

Analysis: Ranks the top 20 food items by the number of images available.

Description: Detects "imbalanced classes." If the model sees 1,000 images of
pizza but only 10 images of lentils, it may struggle to recognize the
slower-release carbs that are vital for stable glucose management.

#### 3. High-Impact Agents (Top 20 Highest Carbs)

Filename: [high_carb_foods](high_carb_foods.png)

Analysis: Identifies the foods with the highest carbohydrate density per 100g.

Description: These are the "High-Risk" foods for a T1D patient. Accuracy in
identifying these specific items is non-negotiable, as even a small portion-size
error here can result in significant hyperglycemia.
