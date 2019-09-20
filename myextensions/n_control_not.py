from qiskit.circuit import QuantumCircuit

def _n_cnot_inner(qc, ctrls, target, working_bits):
    n = len(ctrls)
    if len(working_bits) < n - 2:
        raise ValueError('working qubit is not enough, given {} bit need at least {} bit'.format(
            len(working_bits), n - 2))
    qs = [ctrls[i] for i in range(n)]
    qs = qs + [working_bits[i] for i in range(n - 2)]
    qs = qs + [target]
    for i in range(n - 2):
        qc.ccx(qs[n - 1 - i], qs[-2 - i], qs[-1 - i])
    qc.ccx(qs[0], qs[1], qs[n])
    for i in reversed(range(n - 2)):
        qc.ccx(qs[n - 1 - i], qs[-2 - i], qs[-1 - i])
    for i in range(1, n - 2):
        qc.ccx(qs[n - 1 - i], qs[-2 - i], qs[-1 - i])
    qc.ccx(qs[0], qs[1], qs[n])
    for i in reversed(range(1, n - 2)):
        qc.ccx(qs[n - 1 - i], qs[-2 - i], qs[-1 - i])


def n_control_not_linear(self, ctrls, target, anc):
    if len(ctrls) == 1:
        self.cx(ctrls[0], target)
    if len(ctrls) == 2:
        self.ccx(ctrls[0], ctrls[1], target)
    else:
        if len(anc) < 1:
            raise ValueError(
                'ancillary qubit needs to be at least 1 bit, given {} bit'.format(len(anc)))

        n = len(ctrls) + 2
        m = int((n + 1) // 2)
        _anc = anc[0]
        _n_cnot_inner(self, ctrls[:m], _anc, ctrls[m:] + [target])
        _n_cnot_inner(self, ctrls[m:] + [_anc], target, ctrls[:m])
        _n_cnot_inner(self, ctrls[:m], _anc, ctrls[m:] + [target])
        _n_cnot_inner(self, ctrls[m:] + [_anc], target, ctrls[:m])


QuantumCircuit.n_control_not_linear = n_control_not_linear
