#!/usr/bin/python

byte_length = 12

# ---- Redesigned for part 2

def common_bit_rec(input, switch, index):
    if len(input) == 1:
        return input[0]
    zero_input = []
    one_input = []
    for num in input:
        if num[index] == '1':
            one_input.append(num)
        else:
            zero_input.append(num)   
    print(len(one_input), len(zero_input))
    if switch:
        if len(one_input) == len(zero_input):
            return common_bit_rec(one_input, switch, index+1)
        elif len(one_input) > len(zero_input):
            return common_bit_rec(one_input, switch, index+1)
        else:
            return common_bit_rec(zero_input, switch, index+1)
    else:
        if len(one_input) == len(zero_input):
            return common_bit_rec(zero_input, switch, index+1)
        elif len(one_input) > len(zero_input):
            return common_bit_rec(zero_input, switch, index+1)
        else:
            return common_bit_rec(one_input, switch, index+1)      

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

# Get results for Gamma Rate (Switch is True) and Epsilon Rate (Switch is False)
# gamma_rate = int(common_bits(input_text, True, 0), 2)
# epsilon_rate = int(common_bits(input_text, False, 0), 2)

# Part 2 - Get results
o2_generator = int(common_bit_rec(input_text, True, 0), 2)
co2_scrubber_rating = int(common_bit_rec(input_text, False, 0), 2)

# Calculate the power consumption
# power_consumption = gamma_rate * epsilon_rate

# Calculate the Life Support rating
life_support_rating = o2_generator * co2_scrubber_rating
print(life_support_rating)

