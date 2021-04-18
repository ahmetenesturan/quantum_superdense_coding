from qiskit import *
circ = QuantumCircuit(2,2)
circ.h(0)
circ.cnot(0,1)
inp = input("Enter a 2 digit binary number: ")
if inp[0] == '1':
    circ.x(0)

if inp[1] == '1':
    circ.z(0)

circ.cnot(0,1)
circ.h(0)

circ.measure(0,0)
circ.measure(1,1)

sim = Aer.get_backend("qasm_simulator")
result = execute(circ, backend=sim, shots=1024).result()

count = result.get_counts()
print(count)