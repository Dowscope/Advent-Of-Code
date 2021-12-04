#!/usr/bin/python

# function will return most or least common bits 
def common_bits(input, switch, num_of_bits):
    resulting_byte = ""
    for i in range(num_of_bits):
        common_bit = 0
        for num in input_text:
            if num[i] == '1':
                common_bit += 1
            else:
                common_bit -= 1
        if switch:
            resulting_byte += ('1' if common_bit > 1 else '0')
        else:
            resulting_byte += ('0' if common_bit > 1 else '1')
    
    return resulting_byte
# Open the input file and read into string array
input_file = open('input.txt')
input_text = input_file.read().split('\n')

# Number of bits in the file
num_of_bits = 12

# Get results for Gamma Rate (Switch is True) and Epsilon Rate (Switch is False)
gamma_rate = int(common_bits(input_text, True, num_of_bits), 2)
epsilon_rate = int(common_bits(input_text, False, num_of_bits), 2)

# Calculate the power consumption
power_consumption = gamma_rate * epsilon_rate
print(power_consumption)

