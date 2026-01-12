# Demo Walkthrough

The `minimal_demo.py` script demonstrates the lifecycle of a single concept being learned and recalled.

## 1. Scenario
We simulate a simplified agent that learns associations between "Keys" and "Values".
*   **Context**: The agent starts with an empty memory (Tabula Rasa).
*   **Input**: `("Apple", "Red")`

## 2. Execution Flow

### Step 1: Observation (Review)
The agent sees `("Apple", "Red")`.
*   It queries its memory.
*   **Resonance**: ~0.0 (Novelty).
*   **Decision**: `REVIEW` (I don't know this).
*   **Action**: Encode and Store (Learn).

### Step 2: Confirmation
The agent sees `("Apple", "Red")` again.
*   It queries its memory.
*   **Resonance**: > 0.9 (High familiarity).
*   **Decision**: `ACCEPT` (I know this).

### Step 3: Conflict (Reject)
The agent sees `("Apple", "Blue")`.
*   It binds "Apple" and queries.
*   Memory recalls "Red".
*   Input says "Blue".
*   **Distance**: High.
*   **Decision**: `REJECT` (Conflict detected).

## 3. What to watch in logs
Look for the `[Decision]` tag in the output.
*   `[Decision] STATE: REVIEW (Novle)`: Indicates safe handling of unknowns.
*   `[Decision] STATE: ACCEPT (Known)`: Indicates successful recall.
