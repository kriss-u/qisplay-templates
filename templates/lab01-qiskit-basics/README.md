# Lab 1 · Qiskit Basics

In this lab you build quantum circuits with Qiskit's `QuantumCircuit` and look at
their structure. Nothing is simulated yet; that comes in Lab 2.

## Learning goals

- Create circuits with quantum and classical bits
- Apply single-qubit gates (`x`, `h`) and two-qubit gates (`cx`)
- Measure qubits into classical bits
- Read a circuit's depth, size, and gate counts
- Combine circuits with `compose`, and undo them with `inverse`
- Use a `Parameter` for a gate angle

## Tasks

Open `lab01.py` and implement each function marked `TODO`. Press **Run** at any
time: parts you haven't finished yet are reported as "not implemented".

1. **`single_qubit_circuit()`**: one qubit, apply X then H.
2. **`ghz_with_measurement()`**: 3 qubits and 3 classical bits. Apply H on qubit 0,
   CX from 0 to 1, CX from 1 to 2, a barrier, then measure qubit *i* into classical
   bit *i*.
3. **`circuit_stats(qc)`**: return a dictionary with the keys `num_qubits`,
   `num_clbits`, `depth`, `size`, and `ops` (a plain `dict` of gate name to count).
4. **`append_circuits(first, second)`**: return a new circuit that runs `first`,
   then `second`. Don't modify the inputs.
5. **`undo(qc)`**: return `qc` followed by its inverse. The result acts as the
   identity.
6. **`parameterized_rotation()`**: return `(qc, theta)`, where `theta` is a
   `Parameter` named `"theta"` and `qc` is a 1-qubit circuit with `ry(theta)`.

## Hints

- `qc.draw()` prints a circuit as text and `qc.draw("mpl")` draws it in the Figures tab.
- `qc.count_ops()` returns an `OrderedDict`. Wrap it in `dict(...)`.
- `compose` returns a new circuit unless you pass `inplace=True`.

## Submitting

Use **Project menu → Download as .zip** and upload the zip to Gradescope.
Keep the file name `lab01.py` and the function names and signatures unchanged,
because the autograder imports them.
