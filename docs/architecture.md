# Architecture: Recall-First Engine

## 1. The Inference Flow
The COHERENT architecture inverts the traditional RAG (Retrieval-Augmented Generation) flow. instead of "Retrieve then Generate", we perform **"Recall then Decide"**.

```mermaid
graph TD
    Input[Input Stimulus] --> Encoding[Holographic Encoding]
    Encoding --> Resonance[Resonance Check (Memory)]
    Resonance --> Logic{Trinary Logic}
    
    Logic -- High Resonance --> Accept[ACCEPT: Retrieve & Act]
    Logic -- Low Resonance --> Review[REVIEW: Abductive Loop]
    Logic -- Conflict --> Reject[REJECT: Error Handling]
    
    Review --> Hypothesis[Generate Hypothesis]
    Hypothesis --> Encoding
```

## 2. Key Components

### Holographic Memory (DHM)
The system does not use a database or a key-value store. It uses a **Distributed Representation**.
*   **Storage**: All knowledge is superimposed into a single (or layered) high-dimensional tensor.
*   **Retrieval**: Querying the memory with a vector returns a "cleaned" version of that vector if it exists in memory (Auto-associative).

### Resonance-Based Decision
The core metric is **Resonance** (Cosine Similarity or Dot Product magnitude in Complex space).
*   **High Resonance**: The system "knows" this pattern. It is trusted.
*   **Low Resonance**: The system is "unfamiliar". This triggers the **Review** state, preventing hallucination.

## 3. Difference from LLMs
| Feature | LLM (Transformer) | COHERENT (Holographic) |
| :--- | :--- | :--- |
| **Basic Unit** | Token Probability | Memory Vector |
| **Knowledge Storage** | Model Weights (Implicit) | Superposed Tensor (Explicit) |
| **Inference** | Next-Token Prediction | Resonance-Based Recall |
| **Unknowns** | Hallucination risk | Explicit "REVIEW" state |
