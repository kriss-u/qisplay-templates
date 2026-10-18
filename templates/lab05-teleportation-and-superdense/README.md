# Lab 5 · Teleportation and Superdense Coding

Superdense coding and teleportation are two protocols built on a shared Bell pair,
and each mirrors the other:

| Protocol          | Sends            | Costs              |
| ----------------- | ---------------- | ------------------ |
| Superdense coding | 2 classical bits | 1 qubit + 1 ebit   |
| Teleportation     | 1 qubit          | 2 classical bits + 1 ebit |

## Learning goals

- Encode classical bits with Pauli gates on half of a Bell pair
- Teleport an arbitrary state, then check it with fidelity
- Replace measurements with controlled gates (the deferred measurement principle)
- Write a dynamic circuit with mid-circuit measurement and `if_test`

## Tasks

Implement the `TODO` functions in `lab05.py`.

1. **`superdense_circuit(bits)`**: `bits` is a 2-character string such as `"10"`.
   Alice and Bob share a Bell pair on qubits 0 and 1. Alice encodes `bits` on
   qubit 0, then Bob decodes and measures qubit *i* into classical bit *i*.
   Measuring must give exactly `bits`, in Qiskit's ordering (left character =
   classical bit 1).
2. **`teleportation_circuit(theta, phi)`**: 3 qubits, no measurements. Prepare the
   message on qubit 0 with `prepare(theta, phi)` (provided), create a Bell pair on
   qubits 1 and 2, apply Alice's operations, then apply Bob's corrections as
   **controlled gates** (qubit 1 controls an X on qubit 2, qubit 0 controls a Z on
   qubit 2). Qubit 2 must end up in the message state.
3. **`teleported_fidelity(theta, phi)`**: simulate (2) with `Statevector`, trace
   out qubits 0 and 1, and return the fidelity of qubit 2 with the original
   message. It should be 1.0.
4. **Challenge: `dynamic_teleportation(theta, phi)`**: the real protocol, with
   registers `q` (3 qubits), `m` (2 bits) and `out` (1 bit). Measure qubits 0 and
   1 into `m[0]` and `m[1]`, and apply the corrections with
   `with qc.if_test((m[1], 1)):` and `with qc.if_test((m[0], 1)):`. Then
   apply `prepare(theta, phi).inverse()` to qubit 2 and measure it into `out`. If
   teleportation worked, `out` is always 0.

## Hints

- Bell pair: `h(1)` then `cx(1, 2)`. Alice's step: `cx(0, 1)` then `h(0)`.
- `partial_trace(state, [0, 1])` keeps qubit 2, and `state_fidelity(a, b)`
  compares two states.
- Counts from (4) look like `"0 01"`. The registers are separated by spaces and
  the last one added comes first.

## Submitting

Use **Project menu → Download as .zip** and upload the zip to Gradescope.
Keep the file name `lab05.py` and the function names and signatures unchanged.
