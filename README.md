# QuantumHalfAdder
Half adder circuit done with qubits and CNOT and Toffoli quantum logic gates. 
Necessary to pip install qiskit and qiskit_aer. Recommend using a virtual environment

## General Half Adder

A regular half adder takes two inputs, A and B, which can each be 0 or 1 (binary values). It's called a *half* adder because it only accounts for a carry-out. There's no carry-in like you'd have in a full adder.

The **sum bit** (bit 0) is calculated using A XOR B.

The **carry bit** (bit 1) is calculated using A AND B — this captures the situation where 1 + 1 = 2, which is binary **10**: the 1 is the carry, and the 0 is the sum.

More details can be found here

https://www.geeksforgeeks.org/half-adder-in-digital-logic/

## Quantum Half Adder
Instead of using a general half adder, this program uses a quantum half adder, with python's **qiskit** library. First, instead of representing the inputs as binary numbers, it represents them as **qubits**, |0> and |1>, respectively. On a conceptual level, it is necessary to understand that these are represented by vectors 1 0 and 0 1 respectively. First, a circuit must be created with the following line

`circuit = QuantumCircuit(3, 2)`

This creates a circuit with 3 qubits and 2 classic bits. Qubits 0 and 1 are the inputs, while 2 holds the carry bit. 2 will be used to hold the sum bit, as this will make the processing into regular bits/results much easier. The two qubit inputs can be customized however you would like, by changing the two lines shown below in the code.

`circuit.h(0)`

`circuit.x(1)`

The above input puts qubit 0 into a hadamard(superposition) state. Due to the nature of the hadamard matrix, as shown below, the 1 0 vector becomes a sqrt(2)/2 sqrt(2)/2 vector, or half 1, half 0, in probability. By default, the qubits are initialized as |0> in qiskit. X is the **quantum NOT gate**, which flips |0> to 1, vice versa. If you wanted qubit 0 to be the **superposition of |1>**, you must first circuit.x(0), then circuit.h(0).

The half adder then uses a **toffoli** gate to compute the carry and place it into qubit 2, and then a CX/CNOT/quantum XOR into qubit 1, as the sum. To explain it simply, both of these gates require taking tensor products of the qubits, Qubits 0 and 1 for the CNOT, Qubits 0, 1, and 2 for toffoli/CCNOT. The toffoli is an 8 x 8 matrix, while the CNOT is a 4 x 4. The rest of the program is predicated on running a simulator rather than simply accepting the mathematical probabilities, comparing these, and creating a visual display for the circuit. The code for the in-text visual display was created with the help of GPT 4o
