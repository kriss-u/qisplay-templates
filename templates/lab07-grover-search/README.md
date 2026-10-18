# Lab 7 · Grover's Search

Grover's algorithm finds one of M marked items among N = 2ⁿ in about
(π/4)·√(N/M) oracle calls, where a classical search needs about N/M.

## Learning goals

- Build a phase oracle that flips the sign of marked bitstrings
- Build the diffuser (inversion about the mean)
- Pick the number of iterations, and see what happens when you overshoot
- Run the full search and read the result

## Tasks

Implement the `TODO` functions in `lab07.py`. Bitstrings use Qiskit's ordering
(the rightmost character is qubit 0).

1. **`phase_oracle(n, marked)`**: an n-qubit circuit that multiplies |x⟩ by −1
   for every bitstring x in `marked` and leaves all other states unchanged.
2. **`diffuser(n)`**: the n-qubit operator 2|s⟩⟨s| − I (up to a global phase),
   where |s⟩ is the uniform superposition.
3. **`optimal_iterations(n, m)`**: ⌊(π/4)·√(2ⁿ/m)⌋.
4. **`grover_circuit(n, marked)`**: uniform superposition, then
   `optimal_iterations` rounds of oracle and diffuser, then `measure_all()`.
5. **`search(n, marked, shots, seed)`**: run (4) on `AerSimulator` and return the
   `len(marked)` most frequent bitstrings, most frequent first.

When you run the file it also plots the success probability against the number
of iterations, so you can see it peak and fall.

## Hints

- A multi-controlled Z on all n qubits flips only |1…1⟩. Surround it with X gates
  on the qubits that should be 0 to flip any other bitstring.
- `ZGate().control(n - 1)` from `qiskit.circuit.library` is an n-qubit gate.
  Add it with `qc.append(gate, range(n))`.
- Diffuser: H on all qubits, flip the phase of |0…0⟩, then H on all qubits again.

## Submitting

Use **Project menu → Download as .zip** and upload the zip to Gradescope.
Keep the file name `lab07.py` and the function names and signatures unchanged.
