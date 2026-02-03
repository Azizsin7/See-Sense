# Retrospective – Milestone 0: Domain Study (See‑Sense)

## Context

This milestone scoped the See‑Sense project: researching automated food
recognition to estimate carbohydrate content for nutritional health and diabetes
self‑management. Work included a literature survey, dataset scouting
(e.g., iFood‑2019), clinical framing, and identifying computer‑vision
and ethical challenges.

## ✅ What Went Well

- Focused literature review: identified clinical requirements (carb counting
precision, absorption rates) and key datasets (iFood‑2019) relevant to
carbohydrate estimation.
- Clear technical direction: selected modern CV approaches (e.g., EfficientNet
family) and confirmed feasibility of fine‑grained food classification to
distinguish high vs low carb items.
- Early safety framing: drafted initial ethics considerations (hidden sugars,
PII, sensitive health implications) and stakeholder mapping.
- Central resources: collected datasets, clinical notes, and tool references
under `0_domain_study/literature`.

## ⚠️ What Could Be Better

- Depth vs time: deeper critical appraisal of clinical studies and dataset
biases was limited by schedule.
- Documentation hygiene: notes and ad‑hoc findings were scattered across
personal files and notebooks.
- Scope clarity: initial ideation drifted between broad nutritional uses and
strict diabetes dosing — we need a firm decision on the primary product scope.

## 🚀 Action Items (next steps)

- Centralize literature summaries with short takeaways and citations in one
canonical file `0_domain_study/README.md`.
- Define dataset inclusion/exclusion criteria (label quality, licensing,
carb ground truth).
- Create an ethics & safety checklist for data handling, model outputs, and
user guidance.
- Prototype a minimal classification benchmark using EfficientNetB0 on a
small labeled subset to validate feasibility and estimate error margins.
- Decide product scope (informational guidance)
and record the decision with rationale and risk mitigations.

## Key Learnings

- Clinical precision matters: visual misclassification (e.g., cauliflower vs
potato mash) can meaningfully change carb estimates and downstream insulin decisions.
- Dataset quality > quantity for clinical use: reliable ground‑truth
carbohydrate labels and consistent portioning are essential.
- Ethics must be baked in: early hazard identification (hidden sugars,
vulnerable users) changes both data choices and product scope.

---

## Problem Identification (See‑Sense)

### Summary

Milestone 0 focused on selecting and scoping the core See‑Sense problem:
using computer vision to identify food items and estimate carbohydrate
content to help people manage glycemic control. I converged on a
clinically relevant, technically feasible direction but surfaced important
ata, evaluation, and ethics questions.

#### What Went Well

- Clear problem criteria: I prioritized clinical impact (carb estimation
accuracy) and user safety over broad novelty.
- Strong domain research input: findings from `0_domain_study` (carb release
rates, hidden sugars, dataset constraints) informed realistic success criteria.
- Feasible technical baseline: test modern CV architectures
(EfficientNet family) and to evaluate on labeled subsets
(iFood‑2019 and local data).

#### What Could Be Improved

- Ground‑truth availability: I underestimated the difficulty of obtaining
reliable carbohydrate labels and portion‑standardized images.
- Evaluation metrics: need clearer, clinically meaningful metrics (e.g., carb
error in grams, vs. top‑1 classification accuracy).
- Stakeholder validation: I should have engaged a clinician to
validate chosen targets and safety thresholds.
- Data provenance: licensing and PII concerns for candidate datasets need
formal policy and tracking.

#### Action Items (next steps)

- Define evaluation metrics tied to clinical effect (e.g., mean absolute carb
error per meal; critical error rate thresholds).
- Build a small labeled benchmark (50–200 images across common classes) with
reliable carb labels to estimate baseline error.

#### Lessons Learned

- Problem framing must start from the user outcome (carb grams → insulin
decisions), not only technical accuracy.
- Small, high‑quality labeled sets are more valuable than large noisy
collections for clinical tasks.
- Early, simple governance (dataset policy + ethics checklist) prevents
rework later.
