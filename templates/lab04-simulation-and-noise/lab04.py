"""Lab 4 · Simulation and Noise

Implement every function marked TODO. Keep the names and signatures unchanged:
the autograder imports them. See README.md for details.
"""

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import hellinger_fidelity
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, ReadoutError, depolarizing_error

BASIS = ["rz", "sx", "x", "cx"]


def run_counts(qc: QuantumCircuit, shots: int = 1024, seed: int | None = None) -> dict[str, int]:
    """Ideal AerSimulator counts for a measured circuit."""
    # TODO
    raise NotImplementedError


def to_basis(qc: QuantumCircuit, optimization_level: int = 1) -> QuantumCircuit:
    """`qc` transpiled to BASIS gates (seed_transpiler=7)."""
    # TODO
    raise NotImplementedError


def depolarizing_noise(p1: float, p2: float) -> NoiseModel:
    """Depolarizing error p1 on rz/sx/x and p2 on cx, for all qubits."""
    # TODO
    raise NotImplementedError


def add_readout_error(noise_model: NoiseModel, p: float) -> NoiseModel:
    """Add a symmetric readout error p to every qubit; return the model."""
    # TODO
    raise NotImplementedError


def noisy_counts(qc: QuantumCircuit, noise_model: NoiseModel, shots: int = 1024, seed: int | None = None) -> dict[str, int]:
    """AerSimulator counts with `noise_model` applied."""
    # TODO
    raise NotImplementedError


def fidelity(ideal: dict[str, int], noisy: dict[str, int]) -> float:
    """Hellinger fidelity between two counts dictionaries."""
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


def ghz(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(n - 1):
        qc.cx(i, i + 1)
    qc.measure_all()
    return qc


if __name__ == "__main__":
    qc = ghz(3)
    _try("1. run_counts", lambda: print(run_counts(qc, seed=1)))

    def part2():
        t = to_basis(qc)
        print("before:", dict(qc.count_ops()))
        print("after: ", dict(t.count_ops()))
        print(t.draw())

    _try("2. to_basis", part2)

    def parts3to6():
        model = add_readout_error(depolarizing_noise(0.005, 0.03), 0.02)
        print(model)
        ideal = run_counts(qc, seed=1)
        noisy = noisy_counts(qc, model, seed=1)
        print("noisy:", noisy)
        print(f"Hellinger fidelity: {fidelity(ideal, noisy):.3f}")
        plot_histogram([ideal, noisy], legend=["ideal", "noisy"], title="GHZ(3)")
        plt.show()

    _try("3-6. noise", parts3to6)
