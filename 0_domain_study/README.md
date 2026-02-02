# Domain Research: Food Recognition for Nutritional Health

## Overview

This folder contains research regarding the automated recognition of food items
and the estimation of carbohydrate content. Our goal is to bridge the gap
between image data and actionable nutritional information to improve glycemic
control and patient self-management.

## Key Research Areas

### 1. Clinical Impact & Diabetes Management

* **The Carb-Counting Necessity:** Carbohydrate counting is a flexible
meal-planning tool used to understand how food choices affect blood glucose
levels. Precision is vital because any carbohydrate food (milk, fruit, bread,
pasta) is digested into glucose, directly causing blood glucose to increase.
* **The Estimation Gap:** Managing diabetes requires a precise balance between
carbohydrate intake and insulin. Traditional manual logging is prone to human
error (20-30%), which can lead to dangerous fluctuations in blood sugar.
* **Absorption Complexity:** Research identifies different "release rates" for
carbohydrates. Starchy carbs (bread, potatoes) are typically slow or medium
release, while added sugars (glucose, sucrose) are fast-release. See-Sense
aims to help users navigate these complexities instantly.

### 2. Barriers to Accurate Manual Counting

* **IHidden Carbs:** Many users fail to count "natural sugars" like Lactose in
dairy or Fructose in fruit. Conversely, high-fibre foods like sweetcorn or nuts
may not require rapid-acting insulin in normal portions, adding a layer of
calculation difficulty for the patient.
* **Portion Math:** Standard labels provide data per 100g, forcing users to
perform manual mathematics for every meal component to determine their
specific intake.

### 3. Computer Vision Challenges in Food

* **Intra-class Variation:** A "Samosa" can vary significantly in appearance
(triangular vs. round, fried vs. baked) depending on regional preparation.
* **Inter-class Similarity:** Differentiating between similar-looking items
(e.g., Sushi vs. Sashimi) is critical, as the presence of rice radically
changes the carbohydrate density and required insulin dose.

## Key Resources & Links

* **Dataset Selection: iFood-2019 (FGVC6)** My primary source for "Gold Standard"
carbohydrate values.
[iFood-2019](https://www.kaggle.com/c/ifood-2019-fgvc6/overview)

* **EfficientNetB0:** EfficientNet is a more modern architecture that uses
"Compound Scaling" to achieve much higher accuracy while still being very fast.

* **Clinical Workbooks:** Research based on NHS East Lancashire and Diabetes
Care and Education guidelines.
[literature](./literature/)

## Summaries of Findings

* **Finding A:** In T1D management, "close enough" is not enough. Visual
misinterpretation—such as confusing a low-carb cauliflower mash with high-carb
mashed potatoes—can lead to a dangerously inaccurate insulin dose. Maintaining
high-fidelity visual detail ensures the detection of subtle cues (like the grain
of a specific bread or the coating on a protein) that are critical for
differentiating carb counts and preventing glycemic errors.
* **Finding B:** Must count carbs for every meal, 365 days a year. Clinical
research shows that patients often struggle with "hidden sugars" and the mental
fatigue of converting "per 100g" labels into actual plate portions.
* **Finding B:** As noted in NHS clinical workbooks, different foods create
vastly different blood glucose curves. A "Samosa" is a complex mixture of slow
and medium-release carbs, while a "Fizzy Drink" is purely fast-release. See-Sense
utilizes a fine-grained classification approach specifically to distinguish
between these sub-types, allowing for a precise understanding of how a
specific meal will impact a patient's unique blood glucose trajectory.
