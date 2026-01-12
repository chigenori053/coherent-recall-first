from enum import Enum, auto

class DecisionState(Enum):
    """
    Trinary Logic States for Recall-First Architecture.
    
    The system does not force a Binary Truth (True/False).
    It allows for an explicit 'Unknown' state to prevent hallucination.
    """
    
    # 1. High Resonance / Familiarity
    # The pattern matches internal memory. Safe to proceed.
    ACCEPT = auto()
    
    # 2. Conflict / Contradiction
    # The pattern actively contradicts known memory (Destructive Interference).
    REJECT = auto()
    
    # 3. Low Resonance / Novelty
    # The pattern is neither known nor contradictory. It is new.
    # Triggers Abductive Reasoning or Learning.
    REVIEW = auto()
