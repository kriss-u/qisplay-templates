# Lab 6 · Deutsch–Jozsa and Bernstein–Vazirani

These are the first algorithms where a quantum computer provably needs fewer
oracle queries than a classical one. Both use the same circuit and differ only
in the oracle.

## Learning goals

- Implement oracles U_f|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩ as circuits
- Use phase kickback with an ancilla in |−⟩
- Tell constant from balanced functions with one query (Deutsch–Jozsa)
- Recover a hidden bitstring with one query (Bernstein–Vazirani)

## Conventions

- Oracles act on `n + 1` qubits: inputs are qubits `0 … n-1` and the output
  (ancilla) is qubit `n`.
- Bitstrings use Qiskit's ordering: the **rightmost** character is qubit 0, so
  `"1011"` means qubit 0 = 1, qubit 1 = 1, qubit 2 = 0, qubit 3 = 1.

## Tasks

Implement the `TODO` functions in `lab06.py`.

1. **`constant_oracle(n, output)`**: f(x) = `output` (0 or 1) for every x.
2. **`balanced_oracle(n, mask)`**: f(x) = parity of (x AND mask), where `mask`
   is a non-zero n-character bitstring. This is balanced for any non-zero mask.
3. **`deutsch_jozsa_circuit(oracle, n)`**: n + 1 qubits and n classical bits. Put
   the ancilla in |−⟩ and the inputs in |+⟩, apply the oracle, apply H to the
   inputs, and measure input *i* into classical bit *i*.
4. **`is_constant(oracle, n)`**: run (3) with **one shot** and decide.
5. **`bernstein_vazirani(secret)`**: f(x) = secret · x (mod 2). For a non-zero
   secret that's `balanced_oracle(n, secret)`, and for `"000…0"` it's
   `constant_oracle(n, 0)`. Run the circuit once and return the measured string,
   which should equal `secret`.

## Hints

- f(x) = parity(x AND mask) is a CNOT from each input qubit where the mask has a
  1 to the ancilla. Remember the ordering when you match mask characters to qubits.
- One shot is enough because the outcome is deterministic.

## Submitting

Use **Project menu → Download as .zip** and upload the zip to Gradescope.
Keep the file name `lab06.py` and the function names and signatures unchanged.
