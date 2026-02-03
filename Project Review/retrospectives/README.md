# Retrospectives

Reflections and learnings from each milestone of the
See‑Sense project.

## Purpose

Retrospectives capture what went well, what could
be improved, and what I learned at each phase of
the project. They serve as:

- **Accountability records:** Clear documentation
  of decisions, wins, and challenges at each
  stage.
- **Learning artifacts:** Insights about data
  pipelines, model training, clinical design, and
  project management that inform future work.
- **Audit trails:** For a clinical project like
  See‑Sense, retrospectives document the
  reasoning behind technical choices and safety
  considerations.
- **Reproducibility guides:** Action items and
  lessons learned help others (or future versions
  of the project) avoid pitfalls.

## Retrospective Structure

Each milestone retrospective follows this format:

- **Summary:** One-sentence description of the
  milestone's goal and outcome.
- **✅ What Went Well:** Wins, effective
  approaches, and strengths.
- **⚠️ What Could Be Improved:** Gaps, challenges,
  and lessons learned.
- **🚀 Action Items (next steps):** Concrete,
  forward-looking tasks for the next milestone or
  iteration.
- **What I Learned:** Key insights and takeaways.

## Project Milestones

### **Milestone 0: Domain Study and Problem Identification**

([0_domain_study.md](0_domain_study.md))

Research phase: How effectively can computer vision models (EfficientNetB0)
identify food items and provide accurate carbohydrate values for insulin
dosing, when audited against clinical safety buckets?

- Problem Identification

Scoping: defining the core problem (automated food
recognition for carb estimation), selecting
success criteria, and identifying ethical/safety
considerations.

### **Milestone 1: Food Datasets**

([1_food_datasets.md](1_food_datasets.md))

Dataset sourcing: evaluating iFood‑2019 as the
primary dataset, setting up reproducible
downloads, documenting raw data structure, and
planning carb enrichment.

### **Milestone 2: Data Preparation**

([2_data_preparation.md](2_data_preparation.md))

Data pipeline: transforming raw iFood images and
labels into a "gold standard" dataset by mapping
251 food classes to carbohydrate values,
validating consistency, and preserving audit
trails.

### **Milestone 3: Data Exploration**

([3_data_exploration.md](3_data_exploration.md))

Statistical audit: generating carbohydrate
distribution histograms, class-balance
visualizations, and high-risk food charts to
identify dataset biases before model training.

### **Milestone 4: Data Analysis**

([4_data_analysis.md](4_data_analysis.md))

Clinical bucketing: categorizing foods into four
insulin-impact tiers (Keto/Very Low, Low, Medium,
High Carb) and auditing dataset coverage to
prevent clinical blind spots.

### **Milestone 5: Model Training**

([5_model_training.md](5_model_training.md))

Deep learning: training EfficientNetB0 on WSL2
with mixed-precision optimization, implementing
safety callbacks, and producing
`seesense_fresh_v1.keras` for 251-class food
recognition.

### **Milestone 6: Final Presentation**

([6_final_presentation.md](6_final_presentation.md))

Synthesis: creating end-to-end presentation deck
and live demo script to communicate the system's
capabilities, validate proof-of-concept, and
outline future validation steps.

## Key Themes Across Retrospectives

### Clinical Safety First

Every decision—dataset selection, model
architecture, validation metrics—prioritizes T1D
safety over generic ML accuracy. I ask: "What
could go wrong clinically?" before choosing
technical approaches.

### Data Quality as Foundation

Investing heavily in data preparation (cleaning,
mapping, auditing) prevents expensive rework
later. Garbage in = garbage out, especially for
medical applications.

### Reproducibility & Transparency

All code, data, and processes are documented to
enable others to replicate, audit, and extend the
work. This is non-negotiable for clinical
research.

### Incremental Validation

Rather than waiting until the end, I validated at
each stage (audit dataset distribution,
per-bucket model metrics, live demo). Early
feedback catches problems before they compound.

## How to Use This Folder

### For Learning & Reflection

Read retrospectives in sequence to understand the
project arc, decisions, and lessons learned. Use
action items as guides for similar projects.

### For Project Continuity

If revisiting this project, read the "Action
Items" sections first to understand what was
planned next. Use "What Could Be Improved" as a
prioritized to-do list.

### For Extending the Project

The final presentation retrospective outlines
future work (user testing, mobile deployment,
regulatory validation). Use those action items as
starting points for the next phase.

## Template

See `_template.md` for a blank retrospective
template ready to adapt for new milestones.

---

**Project Status**: All core milestones complete.
Prototype ready for user testing and clinical
validation.
