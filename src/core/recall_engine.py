from .holographic_memory import HolographicMemory
from .decision_state import DecisionState

class RecallEngine:
    """
    The Reasoning Loop: Observe -> Resonate -> Decide.
    """
    
    def __init__(self):
        self.memory = HolographicMemory(dimension=2048)
        self.threshold_accept = 0.8
        self.threshold_reject = 0.5
        
    def observe(self, concept: str) -> DecisionState:
        """
        The Core Loop.
        1. Encode Input
        2. Check Resonance
        3. Make Decision
        4. Learn (if Review -> Accept path taken in full system, specialized here for demo)
        """
        # 1. Encode
        vector = self.memory.encode(concept)
        
        # 2. Resonate
        resonance = self.memory.resonate(vector)
        print(f"[Engine] Input: '{concept}' | Resonance: {resonance:.4f}")
        
        # 3. Decide (Trinary Logic)
        if resonance > self.threshold_accept:
            return DecisionState.ACCEPT
        elif resonance < self.threshold_accept:
            # For this simple demo, we treat low resonance as Novelty (REVIEW)
            # In a full system, REJECT requires specific negative interference check.
            return DecisionState.REVIEW
            
        return DecisionState.REVIEW

    def learn(self, concept: str):
        """
        Explicit learning step.
        """
        print(f"[Engine] Learning: '{concept}'")
        vector = self.memory.encode(concept)
        self.memory.add(vector)
