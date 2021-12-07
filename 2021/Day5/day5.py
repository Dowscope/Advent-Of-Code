#!/usr/bin/python

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.touch_counts = 0
    def print(self):
        return str(self.touch_counts) if self.touch_counts > 0 else "."
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def add_touch_count(self):
        self.touch_counts = self.touch_counts + 1
    def get_touch_counts(self):
        return self.touch_counts

def print_grid():
    grid = ""
    for y in range(size[1]+1):
        for x in range(size[0]+1):
            for c in cells:
                if c.get_x() == x and c.get_y() == y:
                    grid += c.print()
        grid += '\n'
    print(grid)

def update_grid(x, y):
    for c in cells:
        if c.get_x() == x and c.get_y() == y:
            c.add_touch_count()
            return

def show_result():
    counter = 0
    for c in cells:
        if c.get_touch_counts() > 1:
            counter += 1
    return counter

input_file = open("input.txt")
input_text = input_file.read().split("\n")
coords = []

for coords_raw in input_text:
    coord_raw = coords_raw.split(" -> ")
    coord = []
    for c in coord_raw:
        new_coord = c.split(",")
        coord.append(new_coord)
    coords.append(coord)

size = [0,0]
for c in coords:
    for i in c:
        if int(i[0]) > size[0]:
            size[0] = int(i[0])
        if int(i[1]) > size[1]:
            size[1] = int(i[1])

cells = []
for x in range(size[0]+1):
    for y in range(size[1]+1):
        cells.append(Cell(x, y))

for c in coords:
    start_coord = c[0]
    end_coord = c[1]
    if start_coord[0] == end_coord[0]:
        for i in range(abs(int(start_coord[1]) - int(end_coord[1]))+1):
            if int(start_coord[1]) < int(end_coord[1]):
                update_grid(int(start_coord[0]), int(start_coord[1]) + i)
                continue
            else:
                update_grid(int(start_coord[0]), int(end_coord[1]) + i)
                continue
    if start_coord[1] == end_coord[1]:
        for i in range(abs(int(start_coord[0]) - int(end_coord[0]))+1):
            if int(start_coord[0]) < int(end_coord[0]):
                update_grid(int(start_coord[0]) + i, int(start_coord[1]))
                continue
            else:
                update_grid(int(end_coord[0]) + i, int(start_coord[1]))
                continue

print(len(cells))
print(show_result())