"""Lab 8 · QFT and Phase Estimation

Implement every function marked TODO. Keep the names and signatures unchanged:
the autograder imports them. See README.md for details.
"""

import math

from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFTGate
from qiskit.quantum_info import Operator
from qiskit_aer import AerSimulator


def qft(n: int) -> QuantumCircuit:
    """The n-qubit QFT (with swaps) from h, cp and swap gates."""
    # TODO
    raise NotImplementedError


def inverse_qft(n: int) -> QuantumCircuit:
    """The inverse of qft(n)."""
    # TODO
    raise NotImplementedError


def qpe_circuit(phase: float, n_count: int) -> QuantumCircuit:
    """Phase estimation of U = P(2*pi*phase) on |1>, with n_count counting qubits."""
    # TODO
    raise NotImplementedError


def estimate_phase(phase: float, n_count: int, shots: int = 1024, seed: int | None = None) -> float:
    """Most likely QPE outcome k, returned as k / 2**n_count."""
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


if __name__ == "__main__":
    def part1():
        print(qft(3).draw())
        print("matches QFTGate(4):", Operator(qft(4)).equiv(Operator(QFTGate(4))))

    _try("1. qft", part1)
    _try("2. inverse_qft", lambda: print(Operator(qft(3).compose(inverse_qft(3))).equiv(Operator(QuantumCircuit(3)))))
    _try("3. qpe_circuit", lambda: print(qpe_circuit(0.375, 3).draw()))

    def part4():
        print("phase 0.375, 3 bits ->", estimate_phase(0.375, 3, seed=1))
        for bits in [2, 4, 6, 8]:
            est = estimate_phase(1 / 3, bits, seed=1)
            print(f"phase 1/3, {bits} bits -> {est:.5f} (error {abs(est - 1 / 3):.5f})")

    _try("4. estimate_phase", part4)
