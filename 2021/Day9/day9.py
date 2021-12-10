#!/usr/bin/python

input_file = open("input.txt").read().split("\n")
input_text = []

for line in input_file:
    l = list(line)
    input_text.append(l)

lowest_point = []

for y in range(len(input_text)):
    for x in range(len(input_text[y])):
        neighbours = []
        if y > 0:
            neighbours.append(input_text[y-1][x])
        if y < len(input_text)-1:
            neighbours.append(input_text[y+1][x])
        if x > 0:
            neighbours.append(input_text[y][x-1])
        if x < len(input_text[y])-1:
            neighbours.append(input_text[y][x+1])
        lower_num = input_text[y][x]
        for num in neighbours:
            if num == lower_num:
                continue
            elif num < lower_num:
                lower_num = num
        if lower_num == input_text[y][x]:
            lowest_point.append(input_text[y][x])

sum = 0
for n in lowest_point:
    sum = sum + 1 + int(n)

print(lowest_point)