import numpy as np
from typing import Optional

class HolographicMemory:
    """
    Minimal implementation of Holographic Reduced Representations (HRR)
    using Complex-Valued Vectors.
    """
    
    def __init__(self, dimension: int = 1024):
        self.dimension = dimension
        # The single tensor representing all knowledge
        self.memory_trace = np.zeros(dimension, dtype=np.complex128)
        
    def encode(self, string_input: str) -> np.ndarray:
        """
        Encodes a string into a Holographic Vector.
        Uses a fixed random seed based on the string hash to ensure determinism.
        """
        # Deterministic seeding for demo purposes
        seed = int(hash(string_input) % (2**32))
        rng = np.random.RandomState(seed)
        
        # Phase encoding: Magnitude 1, Random Phase
        phases = rng.uniform(0, 2 * np.pi, self.dimension)
        return np.exp(1j * phases)
        
    def add(self, vector: np.ndarray):
        """
        Bundle (Superposition): M_new = M_old + V
        Learns the new pattern.
        """
        self.memory_trace += vector
        
    def resonate(self, vector: np.ndarray) -> float:
        """
        Calculates Resonance (Energy of correlation).
        
        Resonance = | M . V* | / |M|
        (Normalized projection of Memory onto the Query Vector)
        """
        if np.allclose(self.memory_trace, 0):
            return 0.0
            
        # Dot product with conjugate (Correlation)
        dot_product = np.vdot(self.memory_trace, vector)
        
        # Magnitude
        trace_mag = np.linalg.norm(self.memory_trace)
        vec_mag = np.linalg.norm(vector)
        
        # Resonance is the cosine similarity in complex space
        return np.abs(dot_product) / (trace_mag * vec_mag)
