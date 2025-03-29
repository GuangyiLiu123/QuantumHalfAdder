# QuantumHalfAdder
Half adder circuit done with qubits and CNOT and Toffoli quantum logic gates. 
Necessary to pip install qiskit and qiskit_aer. Recommend using a virtual environment

## General Half Adder
![image](https://github.com/user-attachments/assets/f7ffc3e1-42bf-4158-a56d-f8bb7024f159)
A regular half adder consists of an input A and an input B. These can either be 0 or 1, representing the respective values of 0 and 1 in binary. The reason it is called a "half-adder" is because it only accounts for the carry out, there is no consideration for any "carry-in". The sum bit(bit 0), is computed with A XOR B. The carry bit(bit 1), the greater bit, is computed with A AND B, so that 1+1 = 2, or 1 0, with the 1 being the carry, and 0 being the sum.

## Quantum Half Adder
Instead of using a general half adder, this program uses a quantum half adder, with python's qiskit library. First, instead of representing the inputs as binary numbers, it represents them as qubits, |0> and |1>, respectively. On a conceptual level, it is necessary to understand that these are represented by vectors 1 0 and 0 1 respectively. First, a circuit must be created with the following line
circuit = QuantumCircuit(3, 2)
This creates a circuit with 3 qubits and 2 classic bits. Qubits 0 and 1 are the inputs, while 2 holds the carry bit. 2 will be used to hold the sum bit, as this will make the processing into regular bits/results much easier. The two qubit inputs can be customized however you would like, by changing the two lines shown below in the code.
circuit.h(0)
circuit.x(1)
The above input is a hadamard 0. This places the 0 in superposition. Due to the nature of the hadamard matrix, as shown below, the 1 0 vector becomes a sqrt(2)/2 sqrt(2)/2 vector, or half 1, half 0, in probability. This is simply for demonstration purposes, and can be customized to have two hadamard inputs of opposing types h(0) and h(1), or regular qubits x(0) and x(1).
![image](https://github.com/user-attachments/assets/d59bb9bd-8719-48ba-ad95-45b5591a2219)
The half adder then uses a toffoli gate to compute the carry and place it into qubit 2, and then a CX/CNOT/quantum XOR into qubit 1, as the sum. To explain it simply, both of these gates require taking tensor products of the qubits, Qubits 0 and 1 for the CNOT, Qubits 0, 1, and 2 for toffoli/CCNOT. The toffoli is an 8*8 matrix, while the CNOT is a 4*4. The rest of the program is predicated on running a simulator rather than simply accepting the mathematical probabilities, comparing these, and creating a visual display for the circuit. The code for the in text visual display was created with the help of GPT 4o
