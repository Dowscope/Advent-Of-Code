#!/usr/bin/python3

input_text = open("sample.txt").read().split("\n")

data = []

for line in input_text:
    l = line.split()
    data.append(l)

def print_cavern(cavern):
    for line in cavern:
        print(line)

def run_step():
    global input_text
    for y in range(len(input_text)):
        for x in range(len(input_text[y])):
            new_num = int(input_text[y][x]) + 1
            input_text[y].insert(x, new_num)


# for y in range(len(input_text)):
#     for x in range(len(input_text[y])):
#         print(input_text[y][x])

print_cavern(data)
# run_step()
# print_cavern(data)