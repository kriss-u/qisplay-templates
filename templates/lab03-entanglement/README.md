# Lab 3 · Entanglement

Multi-qubit states can be entangled: you can't describe them qubit by qubit.
You build the standard entangled states here and write a test that tells
entangled states from product states.

## Learning goals

- Prepare all four Bell states
- Generalize to the n-qubit GHZ state
- Read Qiskit's qubit ordering: in `"q1q0"`, qubit 0 is the **rightmost** bit
- Detect entanglement through the purity of a reduced density matrix

## Tasks

Implement the `TODO` functions in `lab03.py`.

1. **`bell_state(name)`**: a 2-qubit circuit preparing one of
   - `"phi+"`: (|00⟩ + |11⟩)/√2
   - `"phi-"`: (|00⟩ − |11⟩)/√2
   - `"psi+"`: (|01⟩ + |10⟩)/√2
   - `"psi-"`: (|01⟩ − |10⟩)/√2

   Raise `ValueError` for anything else.
2. **`ghz_state(n)`**: an n-qubit circuit preparing (|0…0⟩ + |1…1⟩)/√2.
3. **`is_entangled(state)`**: for a 2-qubit `Statevector`, return `True` if it is
   entangled. Trace out one qubit and check whether what's left is pure
   (purity 1) or mixed (purity < 1). Allow for floating-point error.
4. **Challenge: `w_state()`**: a 3-qubit circuit preparing
   (|001⟩ + |010⟩ + |100⟩)/√3.

## Hints

- `partial_trace(state, [0])` from `qiskit.quantum_info` traces out qubit 0.
- A `DensityMatrix` has `.purity()`, which can return a complex number with a zero
  imaginary part.
- For the W state, start with `ry` on one qubit so that it is |1⟩ with probability
  1/3, then split the remaining amplitude with controlled gates.

## Submitting

Use **Project menu → Download as .zip** and upload the zip to Gradescope.
Keep the file name `lab03.py` and the function names and signatures unchanged.
