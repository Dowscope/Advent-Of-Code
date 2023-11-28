#!/usr/bin/python

input_data = open("sample.txt").read().split("\n")

map = []
for line in input_data:
    l = list(line)
    map.append(l)

height = len(map)
width = len(map[0])

print(width, height)