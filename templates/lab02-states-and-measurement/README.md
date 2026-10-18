# Lab 2 · States and Measurement

Here you prepare single-qubit states and compare two views of them: the exact
statevector, and the counts you get by measuring many times.

## Learning goals

- Prepare the six cardinal states |0⟩, |1⟩, |+⟩, |−⟩, |+i⟩, |−i⟩
- Compute a circuit's `Statevector` and its outcome probabilities
- Choose a rotation angle that gives a target probability
- Sample measurements with `AerSimulator` and compare them to the probabilities

## Tasks

Implement the `TODO` functions in `lab02.py`.

1. **`prepare_state(label)`**: return a 1-qubit circuit that turns |0⟩ into the
   state named by `label`, one of `"0"`, `"1"`, `"+"`, `"-"`, `"+i"`, `"-i"`. Raise
   `ValueError` for anything else.
2. **`statevector_of(qc)`**: the circuit's final `Statevector`.
3. **`probabilities(qc)`**: a dictionary of bitstring to probability, such as
   `{"0": 0.5, "1": 0.5}`.
4. **`ry_angle_for(p_one)`**: the angle θ such that `ry(θ)` applied to |0⟩ gives
   P(1) = `p_one`.
5. **`measure_counts(qc, shots, seed)`**: measure every qubit and run the circuit on
   `AerSimulator`. Pass `seed` as `seed_simulator` so results are repeatable, and
   return the counts. Don't modify `qc`.

## Hints

- |+i⟩ = S·H|0⟩ and |−i⟩ = S†·H|0⟩.
- `ry(θ)|0⟩ = cos(θ/2)|0⟩ + sin(θ/2)|1⟩`.
- `qc.measure_all(inplace=False)` returns a measured copy of the circuit.
- `plot_bloch_multivector(state)` from `qiskit.visualization` draws a Bloch sphere.

## Submitting

Use **Project menu → Download as .zip** and upload the zip to Gradescope.
Keep the file name `lab02.py` and the function names and signatures unchanged.
