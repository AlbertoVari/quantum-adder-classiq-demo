from classiq import QBit, qfunc, Output, allocate, Model, synthesize, show

@qfunc
def quantum_adder(a: Output[QBit], b: Output[QBit], result: Output[QBit]):
    # Allocate bits
    allocate(1, a)
    allocate(1, b)
    allocate(1, result)

    # Apply XOR logic for demonstration
    result |= a ^ b

# Create the model
adder_model = Model(qfunc=quantum_adder)

# Synthesize the circuit
synthesized_model = synthesize(adder_model)

# Visualize circuit
show(synthesized_model)
