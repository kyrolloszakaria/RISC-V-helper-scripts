def hex_to_binary(hex_string):
    binary_string = bin(int(hex_string, 16))[2:].zfill(len(hex_string)*4)
    return binary_string

def binary_to_decimal(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number

def decimal_to_binary(decimal_number):
    binary_string = bin(decimal_number)[2:]
    return binary_string

def binary_to_hex(binary_string):
    hex_string = hex(int(binary_string, 2))[2:]
    return hex_string

def hex_to_decimal(hex_string):
    decimal_number = int(hex_string, 16)
    return decimal_number

def decimal_to_hex(decimal_number):
    hex_string = hex(decimal_number)[2:]
    return hex_string

# Example usage
choice = input("Enter the input format (h, b, decimal): ")

if choice == "h":
    hex_value = input("Enter a hexadecimal value: ")
    binary_value = hex_to_binary(hex_value)
elif choice == "b":
    binary_value = input("Enter a binary value: ")
else:  
    decimal_value = int(input("Enter a decimal value: "))
    binary_value = decimal_to_binary(decimal_value)

print(binary_value)
print(len(binary_value))
tag_bits = 4
index_bits = 12
print('tag bits in hex: ')
print(binary_to_hex(binary_value[0:(tag_bits)]))
print('cache line in hex: ')
print(binary_to_hex(binary_value[tag_bits:(tag_bits+index_bits)]))
print('offset bits in hex')
print(binary_to_hex(binary_value[(tag_bits+index_bits):]))

print('tag bits in binary: ')
print(binary_value[0:(tag_bits)])
print('cache line in binary: ')
print(binary_value[tag_bits:(tag_bits+index_bits)])
print('offset bits in binary')
print(binary_value[(tag_bits+index_bits):])

print('tag bits in decimal: ')
print(binary_to_decimal( binary_value[0:(tag_bits)]))
print('cache line in decimal: ')
print(binary_to_decimal( binary_value[tag_bits:(tag_bits+index_bits)]))
print('offset bits in decimal')
print(binary_to_decimal( binary_value[(tag_bits+index_bits):]))

