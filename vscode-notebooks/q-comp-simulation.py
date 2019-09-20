# %%
import numpy as np
import time

# Import Qiskit
import qiskit
from qiskit import IBMQ, QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute
from qiskit.compiler import transpile
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from qiskit.providers.aer import noise

from qiskit.quantum_info import state_fidelity, process_fidelity
from qiskit.tools.qi.qi import outer

# Tomography functions
from qiskit.ignis.verification.tomography import state_tomography_circuits, StateTomographyFitter, process_tomography_circuits, ProcessTomographyFitter
import qiskit.ignis.mitigation.measurement as mc

# custom extensions
import sys
sys.path.append("..")
import myextensions

# %%[markdown]
# # Try Header
#
# does it work??

# %%


# %%
