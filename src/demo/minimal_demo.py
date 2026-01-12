
import sys
import os

# Add src to path so we can import core modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from core.recall_engine import RecallEngine
from core.decision_state import DecisionState

def main():
    print("=== COHERENT: Recall-First Minimal Demo ===")
    
    engine = RecallEngine()
    
    # Scene 1: Novelty Detection
    print("\n--- Scene 1: Observation (Novelty) ---")
    observation = "Apple is Red"
    decision = engine.observe(observation)
    print(f"[Decision] STATE: {decision.name} (Novelty Detected)")
    
    if decision == DecisionState.REVIEW:
        print(">> System does not know this. Triggering Learning...")
        engine.learn(observation)

    # Scene 2: Recall (Confirmation)
    print("\n--- Scene 2: Recall (Confirmation) ---")
    # Same observation
    decision_2 = engine.observe(observation)
    print(f"[Decision] STATE: {decision_2.name} (Matches Memory)")
    
    if decision_2 == DecisionState.ACCEPT:
        print(">> Recall Successful. System validates this truth.")

    # Scene 3: Ambiguity/Conflict
    print("\n--- Scene 3: Conflict Check ---")
    # New observation distinct from the first
    observation_3 = "Apple is Blue"
    decision_3 = engine.observe(observation_3)
    # In this minimal demo, simple resonance check might return REVIEW (Low resonance)
    # A full system would check for specific "Apple" binding conflict.
    print(f"[Decision] STATE: {decision_3.name} (Weak Resonance)")

if __name__ == "__main__":
    main()
