#!/usr/bin/python

# -------------  SETUP ------------------------------
input_data = open("sample.txt").read().split("\n\n")

input_template = input_data[0]
pair_insertions_raw = input_data[1].split("\n")

pair_insertions = []
for pair in pair_insertions_raw:
    p = pair.split(" -> ")
    pair_insertions.append(p)

# ------------- PART 1 -------------------
def get_insertion_index(template):
    for i in range(len(pair_insertions)):
        if pair_insertions[i][0] == template:
            return i
    return -1

next_template = ""
steps = 40
for step in range(steps):
    if not step == 0:
        input_template = next_template
    for i in range(len(input_template)):
        if i < len(input_template) - 1:
            if i == 0:
                next_template = input_template[i]
            template_pair = input_template[i] + input_template[i+1]
            insertion_index = get_insertion_index(template_pair)
            if insertion_index == -1:
                print("No insertion found")
                continue
            element = pair_insertions[insertion_index][1]
            next_template = next_template + element + input_template[i+1]
    # print("Step " + str(step + 1) + ": " + next_template)

elements = {}
for e in next_template:
    if elements.get(e):
        count = elements.get(e)
        elements[e] = count + 1
    else:
        elements.update({e:1})

elements_sorted=dict(sorted(elements.items(),key= lambda x:x[1]))

last = elements_sorted.popitem()
first = list(elements_sorted.values())[0]
print(list(last)[1] - first)