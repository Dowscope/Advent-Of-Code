#!/usr/bin/python3

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.rangex = abs(self.x2 - self.x1)
        self.rangey = abs(self.y2 - self.y1)
    def print(self):
        print(str(self.x1) + "," + str(self.y1) + " -> " + str(self.x2) + "," + str(self.y2))
    def check_for_touch(self, line):
        touches = 0
        for y in range(self.rangey):
            for x in range(self.rangex):
                print(x,y)
        # for y in rangeY:
        #     print(y)
        #     for x in rangeX:
        #         print("this: " + x,y)
        #         if line.is_on(x, y):
        #             touches += 1

        return touches
    def is_on(self, ax, ay):
        for y in range(abs(self.y2 - self.y1)):
            for x in range(abs(self.x2 - self.x1)):
                startx = self.x1
                starty = self.y1
                print("is_on")
                if self.y1 > self.y2:
                    starty = self.y2
                if self.x1 > self.x2:
                    startx = self.x2
                if startx + x == ax and starty + y == ay:
                    return True
        return False

def show_result():
    counter = 0
    while(len(lines) > 1):
        line = lines[0]
        lines.pop(0);
        for l in lines:
            counter = counter + line.check_for_touch(l)
    return counter

input_file = open("sample.txt")
input_text = input_file.read().split("\n")
coords = []

for coords_raw in input_text:
    coord_raw = coords_raw.split(" -> ")
    coord = []
    for c in coord_raw:
        new_coord = c.split(",")
        coord.append(new_coord)
    coords.append(coord)

lines = []
for c in coords:
    start_coord = c[0]
    end_coord = c[1]
    if start_coord[0] == end_coord[0] or start_coord[1] == end_coord[1]:
        lines.append(Line(start_coord[0], start_coord[1], end_coord[0], end_coord[1]))

# print(len(lines))
print(show_result())

# for l in lines:
#     print(l.print())