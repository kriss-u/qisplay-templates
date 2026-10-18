"""Lab 6 · Deutsch-Jozsa and Bernstein-Vazirani

Implement every function marked TODO. Keep the names and signatures unchanged:
the autograder imports them. See README.md for details.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def constant_oracle(n: int, output: int) -> QuantumCircuit:
    """(n + 1)-qubit oracle for f(x) = output."""
    # TODO
    raise NotImplementedError


def balanced_oracle(n: int, mask: str) -> QuantumCircuit:
    """(n + 1)-qubit oracle for f(x) = parity(x AND mask); mask is non-zero."""
    # TODO
    raise NotImplementedError


def deutsch_jozsa_circuit(oracle: QuantumCircuit, n: int) -> QuantumCircuit:
    """n + 1 qubits, n clbits: the Deutsch-Jozsa circuit around `oracle`."""
    # TODO
    raise NotImplementedError


def is_constant(oracle: QuantumCircuit, n: int) -> bool:
    """True if `oracle` is constant, using a single shot."""
    # TODO
    raise NotImplementedError


def bernstein_vazirani(secret: str) -> str:
    """Recover `secret` with one oracle query; return the measured bitstring."""
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
    n = 3
    _try("1-2. oracles", lambda: print(balanced_oracle(n, "101").draw()))
    _try("3. deutsch_jozsa_circuit", lambda: print(deutsch_jozsa_circuit(balanced_oracle(n, "101"), n).draw()))

    def part4():
        print("constant 0:", is_constant(constant_oracle(n, 0), n))
        print("constant 1:", is_constant(constant_oracle(n, 1), n))
        print("balanced:  ", is_constant(balanced_oracle(n, "110"), n))

    _try("4. is_constant", part4)

    def part5():
        for secret in ["1011", "0001", "0000"]:
            print(f"secret {secret} -> found {bernstein_vazirani(secret)}")

    _try("5. bernstein_vazirani", part5)
