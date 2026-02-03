# Individual Key Learnings

1. Hardware is the Heartbeat
   I learned that high-level AI isn't just about Python; it’s about the hardware
   beneath it. Configuring NVIDIA CUDA and cuDNN taught me how to bridge the gap
   between software and GPU architecture. Moving from CPU training to GPU
   acceleration was a turning point that allowed the model to process 251
   classes in a fraction of the time.

2. Data is Messy, Management is Key
    Managing a dataset with 250+ categories taught me about Inter-class
    Similarity. Distinguishing between "White Bread" and "Whole Wheat Bread"
    isn't just a coding challenge; it’s a data engineering challenge. I
    learned to use Confusion Matrices to visualize exactly where the model
    struggles and why.

3. The "Clean Code" Discipline
    One of my biggest takeaways was the importance of Linting (Ruff) and GitHub
    Actions. Initially, fixing "unused imports" (like the ghost shutil error!)
    or formatting issues felt like an extra step. However, I now realize this
    discipline ensures the project is professional, scalable, and readable for
    other developers.

- **Success metrics**:
      - Achieving >80% accuracy on the top-tier food categories.
