# Project Constraints

## Technical & Hardware Constraints

1. **The NVIDIA/CUDA Requirement**
   Unlike a basic Python script, my project is bound by Compute Architecture.

    - The Constraint: To achieve usable training speeds for 251 food classes,
    the model requires an NVIDIA GPU with specific CUDA and cuDNN versions.

    - The Result: This creates a hardware "gatekeeper"—the code is highly
    performant but lacks portability on machines without dedicated NVIDIA
    hardware.
2. **Latency vs. Model Depth**
   Since the end goal is a Live Camera application for real-time T1D support,
   I cannot use the most "massive" neural networks.

    - The Constraint: I had to choose a model (EfficientNet) that is
    small enough to run inference in milliseconds but deep enough to recognize
    complex food shapes.

    - The Trade-off: Increasing accuracy often increases lag; you had to find
    the "sweet spot" where the camera doesn't freeze.

### Data & Logical Constraints

1. **Inter-Class Similarity**
    Recognizing 251 classes is a massive logical hurdle compared to the standard
    "Dog vs. Cat" AI projects.

    - The Constraint: Many food items look nearly identical (e.g., White Rice
    vs. Basmati Rice).

    - The Impact: This limited the model's "Confidence Score." I learned
    that the AI is only as good as the visual distinctness of the dataset.

2. **Categorical Complexity for T1D**
    In a medical context (Type 1 Diabetes), the cost of a "wrong" prediction is
    higher than in a general app.

    - The Constraint: The model must not only identify the food but eventually
    associate it with a Carbohydrate value.

    - The Hurdle: Mapping 251 visual classes to a nutritional database requires
    a perfect 1-to-1 match, leaving no room for "vague" labels.

### Development & Workflow Constraints

- Environment Isolation
     Windows-based development for AI has its own set of "path" and "permission"
     constraints.

I had to work strictly within the T1Dc(wsl2 for model training) virtual
environment to prevent dependency conflicts with other Python projects.

### External Constraints

1. The "Nutritional Database" Gap
The AI can see the food, but the carb data comes from external sources like
the USDA or nutrition APIs.

    - The Constraint: There is no universal, perfect "Visual-to-Carb" map.

    - The Challenge: Different countries and brands have different carb counts
    for the exact same-looking apple or slice of bread. My model is
    constrained by the geographic accuracy of the external nutrition data it
    links to.

2. Environmental Variability (Lighting & Setting)
The model is trained on clean datasets, but the "real world" is messy.

    - The Constraint: I cannot control the user's kitchen lighting,
    the camera quality or the plate color.

    - The Impact: Shadow, glare, and "background noise" (like a messy table)
    act as external stressors that can degrade model performance regardless of
    how well I wrote the code.

3. Regulatory & Safety Sensitivity (The "Medical" Bar)
Because this project is for T1D management, it falls into a high-stakes category.

    - The Constraint: I cannot give "Medical Advice."

    - The Legal Hurdle: Even if the model is 99% accurate, an external
    constraint is the safety disclaimer. I have to design the UI to
    ensure the user knows to "verify before dosing," because a 10g carb
    error can lead to hypoglycemia.

4. Dependency Ecosystem (The "Version Trap")
I am at the mercy of the developers of TensorFlow, NVIDIA, and Python.

    - The Constraint: When TensorFlow updates, or NVIDIA releases a new driver,
    it can "break" my local environment.

    - The Result: I spent significant time managing these external library
    versions (like the scikit-learn vs sklearn issue) rather than building new
    features.
