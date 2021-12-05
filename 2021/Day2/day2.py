<<<<<<< HEAD
#!/usr/bin/python3
=======
#!/usr/bin/python
>>>>>>> 125b17aef4cb412396482b24c7b187af6123916d

# Open the input file and read into string array
input_file = open('input.txt')
input_text = input_file.read().split('\n')
<<<<<<< HEAD
 
=======

>>>>>>> 125b17aef4cb412396482b24c7b187af6123916d
# Variables to identify the position of the sub
horizontal_position = 0
vertical_position = 0

<<<<<<< HEAD
# Part 2 variables
aim_position = 0

# Loop through the input list.
=======
# Part 2 Variables
aim_position = 0

>>>>>>> 125b17aef4cb412396482b24c7b187af6123916d
for move in input_text:
    waypoint = move.split(' ')
    if waypoint[0] == "forward":
        horizontal_position += int(waypoint[1])
<<<<<<< HEAD
        vertical_position += aim_position * int(waypoint[1])
=======
        vertical_position += aim_position * int(waypoint[0])
>>>>>>> 125b17aef4cb412396482b24c7b187af6123916d
    elif waypoint[0] == "up":
        aim_position -= int(waypoint[1])
    elif waypoint[0] == "down":
        aim_position += int(waypoint[1])

<<<<<<< HEAD
# Print the result  
print(horizontal_position * vertical_position)
=======
# Display the result
print(horizontal_position * vertical_position)
>>>>>>> 125b17aef4cb412396482b24c7b187af6123916d
