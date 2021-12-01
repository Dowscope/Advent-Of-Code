#!/usr/bin/python

#----------------- For Part 2 ---------------------

# Function to return an array of summed numbers
def three_meas_window(input):
    three_meas = []
    for i in range(len(input)-2):
        three_meas.append(input[i] + input[i+1] + input[i+2])
    return three_meas

#----------------- For Part 1 ---------------------

# Function to return the number of times the depth
# increases
def depth_increase_count(input):
    count = 0
    previous_number = 0
    for num in input:
        if previous_number == 0:
            previous_number = num
        elif previous_number < num:
            count += 1
            previous_number = num
        elif previous_number >= num:
            previous_number = num
    return count

# Open the input file and read into string array
input_file = open('input.txt')
input_text = input_file.read().split('\n')

# Convert to int array
# Using inline if to handle the blank line.  Future implement should handle blank
# lines before this step.
input_num = [int( n if n != '' else 0) for n in input_text]

# Display on screen
print(depth_increase_count(three_meas_window(input_num)))