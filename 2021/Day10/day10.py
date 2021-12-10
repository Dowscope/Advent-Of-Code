#!/usr/bin/python


def check_line(line):
    chunk = []
    for i in range(len(line)):
        if line[i] == ']':
            pre_char = chunk.pop()
            if pre_char != '[':
                return [False, pre_char, line[i]]
        elif line[i] == ')':
            pre_char = chunk.pop()
            if pre_char != '(':
                return [False, pre_char, line[i]]
        elif line[i] == '}':
            pre_char = chunk.pop()
            if pre_char != '{':
                return [False, pre_char, line[i]]
        elif line[i] == '>':
            pre_char = chunk.pop()
            if pre_char != '<':
                return [False, pre_char, line[i]]
        else:
            chunk.append(line[i])
    if len(chunk) > 0:
        return [True, "incomplete", chunk]
    return [True, "", ""]

input_text = open("input.txt").read().split("\n")

results = []
chunks = []
for line in input_text:
    is_valid = check_line(line)
    if not is_valid[0]:
        results.append(is_valid[2])
    if is_valid[0]:
        if is_valid[1] == "incomplete":
            chunks.append(is_valid[2])

points_p2 = []
for c in chunks:
    chunk_points = 0
    while(len(c) > 0):
        last = c.pop()
        if last == '(':
            chunk_points = (chunk_points * 5) + 1
        elif last == '[':
            chunk_points = (chunk_points * 5) + 2
        elif last == '{':
            chunk_points = (chunk_points * 5) + 3
        elif last == '<':
            chunk_points = (chunk_points * 5) + 4
    points_p2.append(chunk_points)


points = 0
for r in results:
    if r == ')':
        points = points + 3
    elif r == ']':
        points = points + 57
    elif r == '}':
        points = points + 1197
    elif r == '>':
        points = points + 25137

points_p2.sort()
middle = int(len(points_p2) / 2)
print(points_p2[middle])