# Retrospective – Milestone 6: Final Presentation (See‑Sense)

## Summary

In this final milestone, I synthesized the entire See‑Sense project into a
comprehensive presentation and live demo. I created `see-sense.pptx` to
communicate the problem, methodology, and results to clinical and technical
audiences, and built `live_demo.py` to showcase real-time inference on food
images with carbohydrate predictions.

## ✅ What Went Well

- **End-to-end storytelling:** I crafted a narrative arc from problem
(T1D carb-counting burden) → solution (computer vision + clinical bucketing)
→ validation (model performance on high-risk foods).
- **Live demo infrastructure:** `live_demo.py` seamlessly loads the trained
model (`seesense_fresh_v1.keras`), applies preprocessing, and displays top-K
predictions with associated carb values—bridging model outputs to clinical
context.
- **Cross-audience communication:** The presentation balances technical depth
(architecture, training details) with clinical relevance (bucket accuracy,
real-world use cases) for both engineers and clinicians.
- **Reproducible demo:** Clear documentation of prerequisites (model file, class
indices, environment setup) ensures anyone can run the live demo without
friction.
- **Proof of concept:** The demo validates end-to-end flow: image → model
inference → carbohydrate estimate, demonstrating clinical viability.

## ⚠️ What Could Be Improved

- **User testing absent:** I didn't test the live demo on diverse food images
or in real-world lighting conditions to validate robustness claims.
- **Presentation depth:** High-level slides may not address deep clinical
questions (e.g., "What's the carb estimation error margin?" or "How does
this compare to manual counting?").
- **Deployment readiness:** The demo runs on desktop; I didn't address mobile
deployment or offline mode, which are critical for clinical adoption.
- **Error handling in demo:** `live_demo.py` lacks graceful fallbacks for
low-confidence predictions or unrecognized foods—essential for clinical
safety.
- **Missing regulatory context:** No mention of FDA/regulatory pathways,
clinical validation plans, or liability disclaimers that would be necessary
for real deployment.

## 🚀 Action Items (Future Iterations)

- **Expand user testing:** Test the live demo with 50–100 diverse food images
(different cuisines, lighting, portion sizes, camera angles) and document
failure modes.
- **Implement confidence thresholding:** Modify `live_demo.py` to flag
low-confidence predictions and suggest manual verification for high-risk foods.
- **Add error margins to predictions:** Display not just "carbs: 25g" but
"carbs: 25g ± 3g (95% CI)" based on per-class validation metrics.
- **Build mobile prototype:** Port the model to TFLite and test on Android/iOS
to validate on-device performance and latency.
- **Draft clinical validation plan:** Outline a prospective study protocol
comparing See‑Sense carb estimates to reference lab values (USDA) and clinician
manual counts.
- **Add regulatory roadmap:** Document FDA 510(k) vs. 513(g) classification
options and establish a compliance checklist.
- **Create training materials:** Build clinician guides and patient instructions
for safe use of the demo (e.g., "When to trust the model, when to ask a
dietitian").

## Key Learnings (Project Reflections)

- **From idea to demo in one project cycle:** Scoping was critical—focusing on
251 food classes with clinical bucketing made the problem tractable.
- **Clinical grade ≠ production ready:** A working demo proves concept but falls
far short of real-world deployment; user testing, error handling, and regulatory
validation are separate major efforts.
- **Presentation is the bridge:** Without clear storytelling, even strong
technical work goes unappreciated. The live demo makes the model tangible.
- **Data quality compounds:** Every earlier mistake (dataset imbalance, missing
carb labels, poor augmentation) surfaces in the final model. Investing in data
hygiene saves rework later.
