#!/usr/bin/python

import numpy as np

input_data = open("input.txt").read().split("\n\n")
dots_raw = input_data[0].split("\n")
folds_raw = input_data[1].split("\n")

dots = []
folds = []
width = -1
height = -1
board = []

def print_board(b):
    for y in b:
        l = ""
        for x in y:
            l = l + x
        print(l)

# ----------- Setup ------------

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
width = width + 1
height = height + 1

for y in range(height):
    row = []
    for x in range(width):
        row.append(".")
    board.append(row)

for d in dots:
    board[int(d[1])][int(d[0])] = "#"

# ---------- Folding ----------

new_board = board.copy()
fold_count = 0
for f in folds:
    fold_count = fold_count + 1
    if f[0] == 'y':
        nb = new_board[:int(f[1])]
        merge_board = new_board[int(f[1])+1:]
        merge_board.reverse()
        for y in range(len(nb)-1, -1, -1):
            if len(merge_board) == 0:
                break
            merge_line = merge_board.pop()
            for i in range(len(merge_line)):
                if merge_line[i] == "#":
                    nb[y][i] = "#"
        new_board = nb.copy()
    else:
        nb = []
        merge_board = []
        for y in new_board:
            nb.append(y[:int(f[1])])
            merge_board.append(y[int(f[1])+1:])
        merge_board.reverse()
        for y in nb:
            if len(merge_board) == 0:
                break
            merge_line = merge_board.pop()
            merge_line.reverse()
            for x in range(len(y)-1, -1, -1):
                if len(merge_line) > 0:
                    merge_item = merge_line.pop()
                    if merge_item == "#":
                        y[x] = "#"
        new_board = nb.copy()

    dot_count = 0
    for y in new_board:
        for x in y:
            if x == "#":
                dot_count = dot_count + 1
    print(fold_count, dot_count)

print_board(new_board)