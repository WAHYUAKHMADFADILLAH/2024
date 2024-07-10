import random as r
def generate_nim():
    # Generate 8-digit NIM
    nim = ''.join(str(r.randint(0, 9)) for _ in range(8))
    return nim

# Generate 5 unique NIMs
nims = set()
while len(nims) < 5:
    nims.add(generate_nim())

    # Replace the last three digits with random numbers
    nims = {nim[:-3] + str(r.randint(0, 999)) for nim in nims}

    # Convert the NIMs to binary, hexadecimal, and octal
for nim in nims:
    print(f'NIM: {nim}')
    print(f'Binary: {int(nim, 10):08b}')
    print(f'Hexadecimal: {int(nim, 10):08x}')
    print(f'Octal: {int(nim, 10):08o}')
    print()

# Calculate the average length of the NIMs
nim_lengths = [len(nim) for nim in nims]
average_length = sum(nim_lengths) / len(nim_lengths)
print(f'Average length of NIMs: {average_length:.2f} digits')

# Find the NIM with the maximum length
max_length_nim = max(nim_lengths, key=lambda x: x)
print(f'NIM with the maximum length: {max_length_nim} digits')
