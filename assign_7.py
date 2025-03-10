# Convert to binary , octal , hexadecimal and then original 

def convert_number(num):
    # Convert to binary, octal, and hexadecimal
    binary = bin(num)[2:]  # [2:] to remove the '0b' prefix
    octal = oct(num)[2:]    # [2:] to remove the '0o' prefix
    hexadecimal = hex(num)[2:]  # [2:] to remove the '0x' prefix

    return binary, octal, hexadecimal

def reconvert_number(binary, octal, hexadecimal):
    # Reconvert binary, octal, and hexadecimal back to the original number
    original_from_binary = int(binary, 2)
    original_from_octal = int(octal, 8)
    original_from_hexadecimal = int(hexadecimal, 16)

    return original_from_binary, original_from_octal, original_from_hexadecimal

# Example usage
number = 12  # You can replace this with any integer
binary, octal, hexadecimal = convert_number(number)

print(f"Original number: {number}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")

original_from_binary, original_from_octal, original_from_hexadecimal = reconvert_number(binary, octal, hexadecimal)

print(f"Reconverted from Binary: {original_from_binary}")
print(f"Reconverted from Octal: {original_from_octal}")
print(f"Reconverted from Hexadecimal: {original_from_hexadecimal}")
