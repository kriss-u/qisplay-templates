"""Lab 7 · Grover's Search

Implement every function marked TODO. Keep the names and signatures unchanged:
the autograder imports them. See README.md for details.
"""

import math

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import ZGate
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator


def phase_oracle(n: int, marked: list[str]) -> QuantumCircuit:
    """n qubits: |x> -> -|x> for x in `marked`, identity otherwise."""
    # TODO
    raise NotImplementedError


def diffuser(n: int) -> QuantumCircuit:
    """n qubits: inversion about the uniform superposition."""
    # TODO
    raise NotImplementedError


def optimal_iterations(n: int, m: int) -> int:
    """floor(pi/4 * sqrt(2**n / m))."""
    # TODO
    raise NotImplementedError


def grover_circuit(n: int, marked: list[str]) -> QuantumCircuit:
    """Full Grover circuit with the optimal number of iterations, measured."""
    # TODO
    raise NotImplementedError


def search(n: int, marked: list[str], shots: int = 1024, seed: int | None = None) -> list[str]:
    """The len(marked) most frequent outcomes of grover_circuit, most frequent first."""
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
    n, marked = 4, ["1010"]
    _try("1. phase_oracle", lambda: print(phase_oracle(n, marked).draw()))
    _try("2. diffuser", lambda: print(diffuser(n).draw()))
    _try("3. optimal_iterations", lambda: print(optimal_iterations(n, len(marked))))

    def part4():
        qc = grover_circuit(n, marked)
        sim = AerSimulator()
        counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()
        print(sorted(counts.items(), key=lambda kv: -kv[1])[:4])

    _try("4. grover_circuit", part4)
    _try("5. search", lambda: print(search(5, ["00111", "11000"], seed=1)))

    def sweep():
        oracle, diff = phase_oracle(n, marked), diffuser(n)
        qc = QuantumCircuit(n)
        qc.h(range(n))
        probs = []
        for _ in range(13):
            probs.append(Statevector.from_instruction(qc).probabilities_dict().get(marked[0], 0))
            qc.compose(oracle, inplace=True)
            qc.compose(diff, inplace=True)
        plt.plot(range(len(probs)), probs, "o-")
        plt.xlabel("Grover iterations")
        plt.ylabel(f"P({marked[0]})")
        plt.title("Success probability rises, then falls")
        plt.show()

    _try("sweep", sweep)
