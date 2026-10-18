# Lab 8 · QFT and Phase Estimation

The quantum Fourier transform (QFT) is the core of phase estimation, which in
turn drives Shor's algorithm and many quantum simulation methods. You build both
from basic gates.

## Learning goals

- Build the QFT from Hadamards and controlled-phase rotations
- Check a circuit against a library implementation with `Operator.equiv`
- Implement quantum phase estimation (QPE) for U = P(2πφ)
- Understand how the number of counting qubits sets the precision

## Tasks

Implement the `TODO` functions in `lab08.py`.

1. **`qft(n)`**: the n-qubit QFT, including the final swaps, built from `h`,
   `cp` and `swap`. It must match `QFTGate(n)` as an operator.
2. **`inverse_qft(n)`**: the inverse of (1).
3. **`qpe_circuit(phase, n_count)`**: `n_count` counting qubits (0 … n_count-1),
   one target qubit (index `n_count`) prepared in |1⟩, and `n_count` classical
   bits. U = P(2π·`phase`) has |1⟩ as an eigenvector with eigenvalue
   e^{2πi·phase}. Apply H to the counting qubits, then controlled-U^(2^j) from
   counting qubit j, then the inverse QFT on the counting qubits, and measure
   counting qubit *i* into classical bit *i*.
4. **`estimate_phase(phase, n_count, shots, seed)`**: run (3), take the most
   frequent outcome k, and return k / 2^n_count.

## Hints

- QFT: for each qubit from the highest index down, apply H to it, then
  `cp(π / 2**(j - k), k, j)` from each lower qubit k. Finish with swaps that
  reverse the qubit order.
- Controlled-U^(2^j) for U = P(θ) is just `cp(θ * 2**j, j, target)`.
- If φ = k / 2ⁿ exactly, QPE gives k every time. Otherwise it gives the nearest
  value with high probability.

## Submitting

Use **Project menu → Download as .zip** and upload the zip to Gradescope.
Keep the file name `lab08.py` and the function names and signatures unchanged.
