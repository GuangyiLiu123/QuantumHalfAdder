# Quantum Half Adder - Guangyi Liu

from qiskit import QuantumCircuit
simulator = None
# The Actual Quantum Simulator, being from qiskit_aer

import qiskit_aer
simulator = qiskit_aer.AerSimulator()
print("Using qiskit_aer.AerSimulator")
    
# Import visualization if available

from qiskit.visualization import circuit_drawer
VISUALIZATION_AVAILABLE = True



def simulate_circuit(circuit):
    """Simulate the quantum circuit and return results"""
    if simulator is None:
        print("No simulator available. Using expected results.")
        return {"01": 10240}  # Expected result after SWAP, updated to 10240 shots

    sim_to_use = simulator

    job = sim_to_use.run(circuit, shots=10240)  # Increased from 1024 to 10240
    result = job.result()
        
    # Get the counts (measurement results)
    counts = result.get_counts(circuit)
    return counts

def create_half_adder_circuit():
    # Create a circuit with 3 qubits and 2 classical bits
    # qubits 0 and 1 are inputs, qubit 2 will hold the carry bit
    # qubit 1 will be reused to store the sum bit (XOR result) instead of qubit 0
    circuit = QuantumCircuit(3, 2)
    
    # Initialize input qubits
    # Put q_0 in a superposition state using a Hadamard gate
    circuit.h(0)  # Apply Hadamard to first qubit to create superposition |0⟩+|1⟩(Scaled, obviously)
    circuit.x(1)  # Set second input to 1
    
    # Add a barrier for clarity
    circuit.barrier()
    
    # AND
    # The Toffoli/CCX gate acts as an AND operation when the target bit is |0⟩
    circuit.ccx(0, 1, 2)  # Carry bit will be in qubit 2
    
    # XOR
    # CNOT gate acts as XOR between control and target when the target is |0⟩
    # In this case, storing the result in qubit 1
    circuit.cx(0, 1)  # XOR stored in qubit 1
    
    # More clarity to make it not jarring
    circuit.barrier()
    
    # Measure qubits
    # qubit 1 now contains the sum bit, or the XOR/CNOT
    # qubit 2 contains the carry bit, or the AND/Toffoli
    circuit.measure(1, 0)  # Sum bit to classical bit 0
    circuit.measure(2, 1)  # Carry bit to classical bit 1
    
    return circuit

def explain_half_adder_results(results):
    print("\nHalf Adder Explanation:")
    print("The half adder circuit adds two single bits and produces:")
    print(" - A sum bit (the result of XOR operation)")
    print(" - A carry bit (the result of AND operation)")
    print("\nIn our circuit:")
    print(" - Qubit 0 was put in superposition state (|0>+|1>)/√2 using a Hadamard gate")
    print(" - Qubit 1 was initially 1")
    print(" - After the operations, qubit 1 holds the sum and qubit 2 holds the carry")
    print("\nExpected classical outputs with equal probability:")
    print(" - For input 0+1=01: Sum=1, Carry=0")
    print(" - For input 1+1=10: Sum=0, Carry=1")
    
    # Analyze and explain the simulation results
    print("\nActual simulation results:")
    for outcome, count in results.items():
        percentage = (count / sum(results.values())) * 100
        # The bit string is in reverse order (classical bit 0 is on the right)
        bits = outcome[::-1]  # Reverse the string
        
        if len(bits) >= 2:
            sum_bit = bits[0] # order is now "proper"
            carry_bit = bits[1]
            print(f" |{outcome}>: {count} shots ({percentage:.2f}%)")
            print(f" Sum bit: {sum_bit}, Carry bit: {carry_bit}")
            
            if sum_bit == '1' and carry_bit == '0':
                print(" Corresponds to input 0+1=01 (sum=1, carry=0)")
            elif sum_bit == '0' and carry_bit == '1':
                print(" Corresponds to input 1+1=10 (sum=0, carry=1)")
            else:
                print(" Unexpected result")
        else:
            print(f" |{outcome}>: {count} shots ({percentage:.2f}%) - Incomplete measurement")
            
    print("\nSince we put qubit 0 in a superposition of |0> and |1>, we expect to see")
    print("both possible outcomes with roughly equal probability (~50% each).")

# Demonstrate the Half Adder
if __name__ == "__main__":
    print("\n" + "="*80)
    print("HALF ADDER QUANTUM CIRCUIT DEMONSTRATION")
    print("="*80 + "\n")
    
    # Create the half adder circuit
    half_adder_circuit = create_half_adder_circuit()
    
    # Print the circuit
    print("Quantum Circuit for Half Adder:")
    print(half_adder_circuit)
    
    # Draw the circuit in text
    if VISUALIZATION_AVAILABLE:
        # Show text representation
        text_circuit = circuit_drawer(half_adder_circuit, output='text')
        print("\nHalf Adder Circuit Diagram (Text Representation):")
        print(text_circuit)
    
    # Simulate the circuit
    results = simulate_circuit(half_adder_circuit)
    
    # Print the results
    print("\nHalf Adder Simulation Results:")
    for outcome, count in results.items():
        print(f" |{outcome}>: {count} shots ({count/10240:.2%})")  # Updated divisor to 10240
    
    # Explain the results
    explain_half_adder_results(results)