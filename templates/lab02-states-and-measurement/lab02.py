"""Lab 2 · States and Measurement

Implement every function marked TODO. Keep the names and signatures unchanged:
the autograder imports them. See README.md for details.
"""

import math

import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import AerSimulator


def prepare_state(label: str) -> QuantumCircuit:
    """A 1-qubit circuit preparing "0", "1", "+", "-", "+i" or "-i" from |0>."""
    # TODO
    raise NotImplementedError


def statevector_of(qc: QuantumCircuit) -> Statevector:
    """The final statevector of `qc` (no measurements in it)."""
    # TODO
    raise NotImplementedError


def probabilities(qc: QuantumCircuit) -> dict[str, float]:
    """Outcome probabilities, e.g. {"0": 0.5, "1": 0.5}."""
    # TODO
    raise NotImplementedError


def ry_angle_for(p_one: float) -> float:
    """The angle theta such that ry(theta)|0> has P(1) = p_one."""
    # TODO
    raise NotImplementedError


def measure_counts(qc: QuantumCircuit, shots: int = 1024, seed: int | None = None) -> dict[str, int]:
    """Measure all qubits of a copy of `qc`, run it on AerSimulator, return the counts."""
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


def _rounded(probs: dict) -> dict[str, float]:
    return {str(k): round(float(v), 4) for k, v in probs.items()}


if __name__ == "__main__":
    labels = ["0", "1", "+", "-", "+i", "-i"]

    def parts1to3():
        for label in labels:
            sv = statevector_of(prepare_state(label))
            print(f"|{label}>".ljust(5), np.round(sv.data, 3), " P =", _rounded(probabilities(prepare_state(label))))
        plot_bloch_multivector(statevector_of(prepare_state("+i")), title="|+i>")
        plt.show()

    _try("1-3. states and probabilities", parts1to3)

    def part4():
        theta = ry_angle_for(0.25)
        qc = QuantumCircuit(1)
        qc.ry(theta, 0)
        print(f"theta = {theta:.4f}  ->  P = {_rounded(probabilities(qc))}")

    _try("4. ry_angle_for(0.25)", part4)
    _try("5. measure_counts(|+>)", lambda: print(measure_counts(prepare_state("+"), shots=1000, seed=42)))
