"""Lab 5 · Teleportation and Superdense Coding

Implement every function marked TODO. Keep the names and signatures unchanged:
the autograder imports them. See README.md for details.
"""

from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister, transpile
from qiskit.quantum_info import Statevector, partial_trace, state_fidelity
from qiskit_aer import AerSimulator


def prepare(theta: float, phi: float) -> QuantumCircuit:
    """Provided: the 1-qubit message state ry(theta) then rz(phi) applied to |0>."""
    qc = QuantumCircuit(1)
    qc.ry(theta, 0)
    qc.rz(phi, 0)
    return qc


def superdense_circuit(bits: str) -> QuantumCircuit:
    """2 qubits, 2 clbits: share a Bell pair, encode `bits` on qubit 0, decode, measure."""
    # TODO
    raise NotImplementedError


def teleportation_circuit(theta: float, phi: float) -> QuantumCircuit:
    """3 qubits, no measurement: teleport prepare(theta, phi) from qubit 0 to qubit 2."""
    # TODO
    raise NotImplementedError


def teleported_fidelity(theta: float, phi: float) -> float:
    """Fidelity of qubit 2 after teleportation_circuit with the original message."""
    # TODO
    raise NotImplementedError


def dynamic_teleportation(theta: float, phi: float) -> QuantumCircuit:
    """Challenge: teleport with mid-circuit measurement and if_test corrections."""
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


def _counts(qc: QuantumCircuit, shots: int = 512) -> dict[str, int]:
    sim = AerSimulator()
    return sim.run(transpile(qc, sim), shots=shots).result().get_counts()


if __name__ == "__main__":
    def part1():
        print(superdense_circuit("10").draw())
        for bits in ["00", "01", "10", "11"]:
            print(f"sent {bits} -> received {_counts(superdense_circuit(bits))}")

    _try("1. superdense_circuit", part1)
    _try("2. teleportation_circuit", lambda: print(teleportation_circuit(1.1, 0.4).draw()))
    _try("3. teleported_fidelity", lambda: print(f"{teleported_fidelity(1.1, 0.4):.6f}"))

    def part4():
        qc = dynamic_teleportation(1.1, 0.4)
        print(qc.draw())
        print(_counts(qc))

    _try("4. dynamic_teleportation", part4)
