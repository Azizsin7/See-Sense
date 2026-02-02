#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2026-01-27

@author: Aziz Azizi
"""

import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import cv2
import numpy as np
import pandas as pd
import tensorflow as tf

# path finder
current_dir = os.path.dirname(os.path.abspath(__file__))

# relative-path
MODEL_PATH = os.path.join(
    current_dir, "..", "5_model_training", "seesense_fresh_v1.keras"
)

GOLD_CSV = os.path.join(
    current_dir, "..", "2_data_preparation", "final_training_data_v3_gold.csv"
)


# Load Model
print("Loading See-Sense AI Engine...")
if not os.path.exists(MODEL_PATH):
    print(f"ERROR: Model file not found at: {MODEL_PATH}")
    exit()

model = tf.keras.models.load_model(MODEL_PATH)

df_gold = pd.read_csv(GOLD_CSV)
class_names = sorted(df_gold["food_name"].unique())

carb_lookup = (
    df_gold.drop_duplicates("food_name")
    .set_index("food_name")["carbs_per_100g"]
    .to_dict()
)


# Helper: Analyze Image
def analyze_image(img_bgr):
    """Processes the image and returns AI predictions"""
    h, w, _ = img_bgr.shape

    # Center square crop for the model
    min_dim = min(h, w)
    y1 = (h - min_dim) // 2
    x1 = (w - min_dim) // 2
    crop = img_bgr[y1 : y1 + min_dim, x1 : x1 + min_dim]

    # Preprocess for Keras (224x224)
    rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(rgb, (224, 224))
    img_array = np.expand_dims(resized.astype("float32"), axis=0)

    # Predict
    preds = model.predict(img_array, verbose=0)[0]
    idx = np.argmax(preds)

    label = class_names[idx].upper()
    conf = preds[idx] * 100
    carbs = carb_lookup.get(class_names[idx], "??")

    return label, conf, carbs, img_bgr


# Camera
cap = cv2.VideoCapture(0)

# Main Scanner UI Setup
cv2.namedWindow("See-Sense Scanner", cv2.WINDOW_NORMAL)
cv2.resizeWindow("See-Sense Scanner", 1000, 800)

print("\n SCANNER ACTIVE")
print("Aim the brackets at the food.")
print("SPACE = Camera Scan | U = Upload Image | Q = Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot access camera.")
        break

    h, w, _ = frame.shape
    center_x, center_y = w // 2, h // 2

    # Target box settings
    box_size = 300
    x1, y1 = center_x - box_size // 2, center_y - box_size // 2
    x2, y2 = center_x + box_size // 2, center_y + box_size // 2

    # Draw Corner Brackets
    length = 40
    thickness = 3
    color = (0, 255, 0)  # Green

    # Top Left
    cv2.line(frame, (x1, y1), (x1 + length, y1), color, thickness)
    cv2.line(frame, (x1, y1), (x1, y1 + length), color, thickness)
    # Top Right
    cv2.line(frame, (x2, y1), (x2 - length, y1), color, thickness)
    cv2.line(frame, (x2, y1), (x2, y1 + length), color, thickness)
    # Bottom Left
    cv2.line(frame, (x1, y2), (x1 + length, y2), color, thickness)
    cv2.line(frame, (x1, y2), (x1, y2 - length), color, thickness)
    # Bottom Right
    cv2.line(frame, (x2, y2), (x2 - length, y2), color, thickness)
    cv2.line(frame, (x2, y2), (x2, y2 - length), color, thickness)

    cv2.putText(
        frame,
        "PLACE FOOD INSIDE BRACKETS",
        (center_x - 140, y2 + 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2,
    )

    cv2.imshow("See-Sense Scanner", frame)

    key = cv2.waitKey(1) & 0xFF

    # Logic Triggers
    if key == ord(" "):
        print("\n Analyzing camera frame...")
        roi = frame[max(0, y1) : min(h, y2), max(0, x1) : min(w, x2)]
        label, conf, carbs, display_img = analyze_image(roi)

    elif key == ord("u"):
        print("\n Opening file browser...")
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        file_path = askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        root.destroy()

        if not file_path:
            continue

        img = cv2.imread(file_path)
        if img is None:
            print("Failed to load image.")
            continue
        label, conf, carbs, display_img = analyze_image(img)

    elif key == ord("q"):
        break
    else:
        continue

    # Result
    # Resize FIRST so text doesn't overflow
    canvas_w, canvas_h = 1100, 850
    final_display = cv2.resize(display_img, (canvas_w, canvas_h))

    # Top Overlay Bar
    overlay = final_display.copy()
    cv2.rectangle(overlay, (0, 0), (canvas_w, 185), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.7, final_display, 0.3, 0, final_display)

    # UI Text
    cv2.putText(
        final_display,
        f"ITEM: {label}",
        (40, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.7,
        (0, 255, 0),
        3,
    )
    cv2.putText(
        final_display,
        f"CARBS: {carbs}g (per 100g)",
        (40, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.3,
        (0, 255, 255),
        2,
    )
    cv2.putText(
        final_display,
        f"CONFIDENCE: {conf:.1f}%",
        (40, 165),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (200, 200, 200),
        1,
    )

    win_result = "See-Sense Result"
    cv2.namedWindow(win_result, cv2.WINDOW_NORMAL)
    cv2.imshow(win_result, final_display)

    print(f"Prediction Complete: {label}. Press any key to return to scan.")
    cv2.waitKey(0)

    # Crash-proof window destruction
    try:
        if cv2.getWindowProperty(win_result, cv2.WND_PROP_VISIBLE) >= 1:
            cv2.destroyWindow(win_result)
    except:
        pass

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("System Shutdown Successfully.")
