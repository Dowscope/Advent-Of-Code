#!/usr/bin/python

# Open the input file and read into string array
input_file = open('input.txt')
input_text = input_file.read().split('\n')

# Variables to identify the position of the sub
horizontal_position = 0
vertical_position = 0

# Part 2 Variables
aim_position = 0

for move in input_text:
    waypoint = move.split(' ')
    if waypoint[0] == "forward":
        horizontal_position += int(waypoint[1])
        vertical_position += aim_position * int(waypoint[0])
    elif waypoint[0] == "up":
        aim_position -= int(waypoint[1])
    elif waypoint[0] == "down":
        aim_position += int(waypoint[1])

# Display the result
print(horizontal_position * vertical_position)
