#!/usr/bin/python

input_data = open("input.txt").read().split("\n\n")
dots_raw = input_data[0].split("\n")
folds_raw = input_data[1].split("\n")

dots = []
folds = []
width = 0
height = 0
board = [[]]

for d in dots_raw:
    dot_coord = d.split(",")
    dots.append(dot_coord)

for f in folds_raw:
    a = f.split(" ")
    fold_coord = a[2].split("=")
    folds.append(fold_coord)

for dot in dots:
    if int(dot[0]) > width:
        width = int(dot[0])
    if int(dot[1]) > height:
        height = int(dot[1])

for y in range(height):
    row = []
    for x in range(width):
        row.append(".")
    board.append(row)

print(board[0])