"""Lab 1 · Qiskit Basics

Implement every function marked TODO. Keep the names and signatures unchanged:
the autograder imports them. See README.md for details.
"""

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter


def single_qubit_circuit() -> QuantumCircuit:
    """A 1-qubit circuit that applies X, then H."""
    # TODO
    raise NotImplementedError


def ghz_with_measurement() -> QuantumCircuit:
    """3 qubits, 3 classical bits: H(0), CX(0,1), CX(1,2), barrier, measure i -> i."""
    # TODO
    raise NotImplementedError


def circuit_stats(qc: QuantumCircuit) -> dict:
    """{"num_qubits", "num_clbits", "depth", "size", "ops"} for the circuit."""
    # TODO
    raise NotImplementedError


def append_circuits(first: QuantumCircuit, second: QuantumCircuit) -> QuantumCircuit:
    """A new circuit: `first` followed by `second`. Leave both inputs unchanged."""
    # TODO
    raise NotImplementedError


def undo(qc: QuantumCircuit) -> QuantumCircuit:
    """`qc` followed by its inverse."""
    # TODO
    raise NotImplementedError


def parameterized_rotation() -> tuple[QuantumCircuit, Parameter]:
    """(qc, theta): a 1-qubit circuit applying ry(theta), with theta = Parameter("theta")."""
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
    _try("1. single_qubit_circuit", lambda: print(single_qubit_circuit().draw()))
    _try("2. ghz_with_measurement", lambda: print(ghz_with_measurement().draw()))
    _try("3. circuit_stats", lambda: print(circuit_stats(ghz_with_measurement())))

    def part4():
        a = QuantumCircuit(2)
        a.h(0)
        b = QuantumCircuit(2)
        b.cx(0, 1)
        print(append_circuits(a, b).draw())

    _try("4. append_circuits", part4)
    _try("5. undo", lambda: print(undo(single_qubit_circuit()).draw()))

    def part6():
        qc, theta = parameterized_rotation()
        print(qc.draw())
        print("bound to pi/2:")
        print(qc.assign_parameters({theta: 3.14159 / 2}).draw())

    _try("6. parameterized_rotation", part6)
