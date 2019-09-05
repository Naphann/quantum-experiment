import warnings
import numpy as np

from qiskit.circuit import Gate
from qiskit.circuit import QuantumCircuit
from qiskit.circuit import QuantumRegister
from qiskit.extensions.standard.cu3 import Cu3Gate 

class CvGate(Gate):
    """controlled-v gate."""


    def __init__(self):
        """Create new cv gate"""
        super().__init__("cv", 2, [])

    def _define(self):
        """
        gate cv c, t
        { u1(0) c; u1(-pi/2) t; cx c,t;
          u3(-pi/4,0,0) t; cx c,t;
          u3(pi/4,pi/2,0) t;
        }
        """
        definition = []
        q = QuantumRegister(2, "q")
        rule = [
            (Cu3Gate(np.pi/2, np.pi/2, -np.pi/2), [q[0], q[1]], []) 
        ]
        for inst in rule:
            definition.append(inst)
        self.definition = definition

    def inverse(self):
        """Invert this gate."""
        return Cu3Gate(-np.pi/2, -np.pi/2, np.pi/2)

    def to_matrix(self):
        return 1/2 * np.array([[1 + 1j, 1 - 1j], 
                               [1 - 1j, 1 + 1j]], dtype=complex)

    def say(self):
        return "hello world"
        

def cv(self, ctl, tgt):
    """Apply CV to circuit."""
    return self.append(CvGate(), [ctl, tgt], [])


QuantumCircuit.cv = cv