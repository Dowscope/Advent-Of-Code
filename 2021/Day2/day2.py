#!/usr/bin/python3

# Open the input file and read into string array
input_file = open('input.txt')
input_text = input_file.read().split('\n')
 
# Variables to identify the position of the sub
horizontal_position = 0
vertical_position = 0

# Loop through the input list.
for move in input_text:
    waypoint = move.split(' ')
    if waypoint[0] == "forward":
        horizontal_position += int(waypoint[1])
    elif waypoint[0] == "up":
        vertical_position -= int(waypoint[1])
    elif waypoint[0] == "down":
        vertical_position += int(waypoint[1])

# Print the result  
print(horizontal_position * vertical_position)