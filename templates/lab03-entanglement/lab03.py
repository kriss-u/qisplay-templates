"""Lab 3 · Entanglement

Implement every function marked TODO. Keep the names and signatures unchanged:
the autograder imports them. See README.md for details.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace


def bell_state(name: str) -> QuantumCircuit:
    """A 2-qubit circuit preparing "phi+", "phi-", "psi+" or "psi-"."""
    # TODO
    raise NotImplementedError


def ghz_state(n: int) -> QuantumCircuit:
    """An n-qubit circuit preparing (|0...0> + |1...1>)/sqrt(2)."""
    # TODO
    raise NotImplementedError


def is_entangled(state: Statevector) -> bool:
    """True if the 2-qubit pure `state` is entangled."""
    # TODO
    raise NotImplementedError


def w_state() -> QuantumCircuit:
    """Challenge: a 3-qubit circuit preparing (|001> + |010> + |100>)/sqrt(3)."""
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Try your code: press Run. Unfinished parts are skipped.
# ---------------------------------------------------------------------------

def _try(label, fn):
    print(f"\n== {label} ==")
    try:
        fn()
    except NotImplementedError:
        print("not implemented yet")


def _probs(qc: QuantumCircuit) -> dict[str, float]:
    return {str(k): round(float(v), 4) for k, v in Statevector.from_instruction(qc).probabilities_dict().items()}


if __name__ == "__main__":
    def part1():
        for name in ["phi+", "phi-", "psi+", "psi-"]:
            print(name.ljust(5), np.round(Statevector.from_instruction(bell_state(name)).data, 3))

    _try("1. bell_state", part1)
    _try("2. ghz_state(4)", lambda: print(_probs(ghz_state(4))))

    def part3():
        bell = Statevector.from_instruction(bell_state("phi+"))
        product = Statevector.from_label("+0")
        print("Bell state entangled?   ", is_entangled(bell))
        print("|+>|0> entangled?       ", is_entangled(product))

    _try("3. is_entangled", part3)
    _try("4. w_state", lambda: print(_probs(w_state())))
