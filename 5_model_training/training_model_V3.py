#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2026-01-18

@author: Aziz Azizi
"""

import os
import json
import pandas as pd
import tensorflow as tf
from pathlib import Path
from tensorflow.keras import layers, models, mixed_precision
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# VRAM PROTECTION
gpus = tf.config.list_physical_devices("GPU")
if gpus:
    try:
        tf.config.set_logical_device_configuration(
            gpus[0], [tf.config.LogicalDeviceConfiguration(memory_limit=3200)]
        )
        print("GPU Memory Limit set to 3.2GB")
    except RuntimeError as e:
        print(e)

# MIXED PRECISION
policy = mixed_precision.Policy("mixed_float16")
mixed_precision.set_global_policy(policy)
print("Mixed precision activated")

# Paths
SCRIPT_DIR = Path(os.getcwd())
base_path = SCRIPT_DIR if SCRIPT_DIR.name == "See-Sense" else SCRIPT_DIR.parent
csv_path = base_path / "2_data_preparation" / "final_training_data.csv"
model_dir = base_path / "5_model_training"
os.makedirs(model_dir, exist_ok=True)

# Data Load and Shuffle
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Cannot find CSV at {csv_path}")

df = pd.read_csv(csv_path)
df["filepath"] = df["filepath"].str.replace("\\", "/", regex=False)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.15,
    horizontal_flip=True,
    rotation_range=20,
    zoom_range=0.2,
    brightness_range=[0.8, 1.2],
)

train_gen = datagen.flow_from_dataframe(
    df,
    directory=str(base_path),
    x_col="filepath",
    y_col="food_name",
    target_size=(224, 224),
    batch_size=16,
    class_mode="categorical",
    subset="training",
)

val_gen = datagen.flow_from_dataframe(
    df,
    directory=str(base_path),
    x_col="filepath",
    y_col="food_name",
    target_size=(224, 224),
    batch_size=16,
    class_mode="categorical",
    subset="validation",
)

# Save Class Indices
class_indices = {v: k for k, v in train_gen.class_indices.items()}
with open(os.path.join(model_dir, "class_indices.json"), "w") as f:
    json.dump(class_indices, f)
print(f"Saved labels to {os.path.join(model_dir, 'class_indices.json')}")

# Model Building
base_model = EfficientNetB0(
    weights="imagenet", include_top=False, input_shape=(224, 224, 3)
)

for layer in base_model.layers:
    if isinstance(layer, layers.BatchNormalization):
        layer.trainable = False

model = models.Sequential(
    [
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.BatchNormalization(),
        layers.Dropout(0.4),
        layers.Dense(512, activation="relu"),
        layers.Dense(
            len(train_gen.class_indices), activation="softmax", dtype="float32"
        ),
    ]
)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

# Callbacks
checkpoint = ModelCheckpoint(
    os.path.join(model_dir, "seesense_fresh_v1.keras"),
    monitor="val_accuracy",
    save_best_only=True,
    mode="max",
)
lr_reducer = ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=2, verbose=1)
early_stop = EarlyStopping(
    monitor="val_accuracy", patience=6, restore_best_weights=True
)

# Start Training
print("Starting training...")
model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=25,
    callbacks=[checkpoint, lr_reducer, early_stop],
)
