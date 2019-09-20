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
            (Cu3Gate(np.pi / 2, np.pi / 2, -np.pi / 2), [q[0], q[1]], [])
        ]
        for inst in rule:
            definition.append(inst)
        self.definition = definition

    def inverse(self):
        """Invert this gate."""
        return CvdgGate()

    def to_matrix(self):
        return 1 / 2 * np.array([[1 + 1j, 1 - 1j],
                                 [1 - 1j, 1 + 1j]], dtype=complex)


class CvdgGate(Gate):
    """controlled-v dagger gate."""

    def __init__(self):
        """Create new cv gate"""
        super().__init__("cvdg", 2, [])

    def _define(self):
        """
        gate cvdg c, t
        { cu3(-pi/2, -pi/2, pi/2) c,t; }
        """
        definition = []
        q = QuantumRegister(2, "q")
        rule = [
            (Cu3Gate(-np.pi / 2, -np.pi / 2, np.pi / 2), [q[0], q[1]], [])
        ]
        for inst in rule:
            definition.append(inst)
        self.definition = definition

    def inverse(self):
        """Invert this gate."""
        return CvGate()

    def to_matrix(self):
        return 1 / 2 * np.array([[1 - 1j, 1 + 1j],
                                 [1 + 1j, 1 - 1j]], dtype=complex)


def cv(self, ctl, tgt):
    """Apply CV to circuit."""
    return self.append(CvGate(), [ctl, tgt], [])


def cvdg(self, ctl, tgt):
    """Apply CVDg to circuit."""
    return self.append(CvdgGate(), [ctl, tgt], [])


QuantumCircuit.cv = cv
QuantumCircuit.cvdg = cvdg
