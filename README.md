# COHERENT: Recall-First Holographic Reasoning Foundation

> **Holographic Inference beyond the Generative AI paradigm.**
> *A minimal research prototype demonstrating the feasibility of Recall-First Cognitive Architecture.*

---

## ⚠️ Disclaimer
**This repository is a minimal research prototype prepared for proposal evaluation.**
It does not represent the full system described in the project proposal. It is intended solely to demonstrate the core algorithmic principles of the "Recall-First" architecture.

---

## 1. Project Abstract
**Recent AI models generate "plausible" answers, but lack "certainty".**
The COHERENT project proposes a paradigm shift from **"Generation-First"** to **"Recall-First"**. By utilizing high-dimensional Holographic Memory (Hyperdimensional Computing) as the substrate for reasoning, we establish a system that "recalls" the correct path before "generating" an answer.

This repository provides a proof-of-concept implementation of the core engine: **Holographic Recall Loop** and **Trinary Decision Logic**.

## 2. Core Philosophy

### 2.1 Generating is NOT Understanding
Current LLMs predict the next token based on probability. They do not distinctively separate "what they know" from "what they hallucinate".
**Recall-First** architecture ensures that decision-making is grounded in retrieved, high-resonance memory states.

### 2.2 Holographic Memory as the Substrate
We use **Holographic Reduced Representations (HRR)** with complex-valued vectors.
*   **Superposition**: Storing multiple concepts without growing memory size.
*   **Interference**: Constructive interference implies "familiarity"; destructive interference implies "novelty".
*   **Resonance**: The intensity of the memory response guides the reasoning process.

### 2.3 Trinary Decision Logic (The "Halt" Problem)
Unlike binary logic (True/False), our system employs Trinary Logic to handle ambiguity:
1.  **ACCEPT (Recall)**: Strong resonance found. Confidence is high.
2.  **REJECT (Error)**: Contradiction detected.
3.  **REVIEW (Uncertain)**: Weak resonance. Requires further observation or hypothesis generation (Abductive Reasoning).

## 3. Repository Structure
This repository contains a minimal, dependency-light implementation of the core algorithms.

*   `src/core/`: The heart of the system.
    *   `holographic_memory.py`: Complex-vector memory operations (HRR).
    *   `recall_engine.py`: The iterative recall loop.
    *   `decision_state.py`: Definition of Trinary Logic states.
*   `src/demo/`: Executable demonstrations.
    *   `minimal_demo.py`: A self-contained script showing the "Recall -> Decision" flow.
*   `docs/`: Detailed architectural explanations.

## 4. Quick Start

### Prerequisites
*   Python 3.10+
*   `numpy` (For vector operations)

### Installation
```bash
git clone https://github.com/your-org/coherent-recall-first.git
cd coherent-recall-first
pip install numpy
```

### Running the Demo
Execute the minimal demo to see the Recall-First engine in action:

```bash
python src/demo/minimal_demo.py
```

You will observe the system:
1.  **Observing** an input pattern.
2.  **Resonating** against its Holographic Memory.
3.  **Deciding** (ACCEPT/REVIEW) based on resonance thresholds.
4.  **Learning** (Constructive Interference) if validated.

## 5. Contact & License
This research is part of a proposal for the Mitoh Advanced Program.
Licensed under the **Apache License 2.0**.
