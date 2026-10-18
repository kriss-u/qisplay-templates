# Lab 4 · Simulation and Noise

Real quantum computers only run a few native gates, and every operation is a
little noisy. In this lab you transpile circuits to a hardware-style basis and
simulate them with noise models in Qiskit Aer.

## Learning goals

- Run circuits on `AerSimulator` with repeatable seeds
- Transpile to a basis gate set and see how the circuit changes
- Build a `NoiseModel` with depolarizing gate errors and readout errors
- Compare ideal and noisy results with the Hellinger fidelity

## Tasks

Implement the `TODO` functions in `lab04.py`. `BASIS` is the gate set used
throughout: `["rz", "sx", "x", "cx"]`.

1. **`run_counts(qc, shots, seed)`**: ideal simulation, returning the counts.
2. **`to_basis(qc, optimization_level)`**: transpile `qc` so that it only uses
   gates from `BASIS`, plus `measure` and `barrier`. Pass `seed_transpiler=7`.
3. **`depolarizing_noise(p1, p2)`**: a `NoiseModel` with a depolarizing error of
   probability `p1` on every 1-qubit basis gate (`rz`, `sx`, `x`) and `p2` on `cx`.
4. **`add_readout_error(noise_model, p)`**: add a symmetric readout error to every
   qubit (a 0 is read as 1 with probability `p`, and a 1 as 0 with probability
   `p`), then return the model.
5. **`noisy_counts(qc, noise_model, shots, seed)`**: simulate with the noise model.
6. **`fidelity(ideal, noisy)`**: the Hellinger fidelity between two counts
   dictionaries.

When you run the file it plots ideal and noisy counts for a GHZ circuit side by
side. Try larger noise or more qubits and see how the fidelity drops.

## Hints

- `from qiskit_aer.noise import NoiseModel, depolarizing_error, ReadoutError`
- `noise_model.add_all_qubit_quantum_error(error, ["rz", "sx", "x"])`
- `ReadoutError([[1 - p, p], [p, 1 - p]])`
- `qiskit.quantum_info.hellinger_fidelity`

## Submitting

Use **Project menu → Download as .zip** and upload the zip to Gradescope.
Keep the file name `lab04.py` and the function names and signatures unchanged.
