#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2026-01-26

@author: Aziz Azizi
"""

import os
import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image

# Dynamic Path
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR.parent
MODEL_PATH = SCRIPT_DIR / "seesense_fresh_v1.keras"
GOLD_CSV = BASE_PATH / "2_data_preparation" / "final_training_data_v3_gold.csv"
TEST_FOLDER = SCRIPT_DIR / "real_test"
SAVE_PATH = SCRIPT_DIR / "test_results_graph.png"

# Load model & data
print("Loading model and class data...")
model = tf.keras.models.load_model(str(MODEL_PATH))
df_gold = pd.read_csv(GOLD_CSV)
class_names = sorted(df_gold["food_name"].unique())

# Select 5 random images
image_files = [
    f for f in os.listdir(TEST_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

if len(image_files) < 5:
    print(f"Only found {len(image_files)} images. Testing all available.")
    sample_files = image_files
else:
    sample_files = random.sample(image_files, 5)

# Visualization
plt.figure(figsize=(20, 10))
plt.suptitle(
    "See-Sense Neural Engine: Random Sample Test", fontsize=20, fontweight="bold"
)

for i, img_name in enumerate(sample_files):
    img_path = TEST_FOLDER / img_name

    # Process image
    img_orig = Image.open(img_path).convert("RGB")
    img_resized = img_orig.resize((224, 224))
    img_array = np.array(img_resized).astype("float32")
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    preds = model.predict(img_array, verbose=0)[0]
    class_idx = np.argmax(preds)
    label = class_names[class_idx]
    confidence = preds[class_idx] * 100

    # Subplot image
    plt.subplot(2, 5, i + 1)
    plt.imshow(img_orig)
    plt.title(f"Pred: {label.upper()}", fontsize=10, color="blue")
    plt.axis("off")

    # Subplot confidence bar
    plt.subplot(2, 5, i + 6)
    color = "green" if confidence > 70 else "orange" if confidence > 40 else "red"
    plt.bar(["Confidence"], [confidence], color=color)
    plt.ylim(0, 100)
    plt.ylabel("%")
    plt.text(0, confidence + 2, f"{confidence:.1f}%", ha="center", fontweight="bold")

# Save
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig(SAVE_PATH)
print(f"Success! Graph saved as: {SAVE_PATH}")
plt.show()
