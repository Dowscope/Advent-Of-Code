with open('data.txt', 'r') as file:
    lines = file.readlines()

def isSymbol(character, use=0):
    if use == 1:
        return not character.isalpha() and not character.isdigit() and character != '.'
    return not character.isalpha() and not character.isdigit()

part_numbers = []
gears = []

for line_index,line in enumerate(lines):
    print(line_index, line)
    line = line.replace('\n', '')
    num = {
        'n': '',
        'startingValue': -1
    }

    for char_index, character in enumerate(line):
        # print(char_index, character)
               
        if character.isdigit():
            # print('Digit')
            if num['startingValue'] == -1:
                num['n'] = character
                num['startingValue'] = char_index
            else:
                num['n'] += character       
        elif isSymbol(character):
            if num['startingValue'] != -1:
                print(f"End of Num: {num['n']}")
                starting_y = line_index - 1 if line_index - 1 >= 0 else line_index
                ending_y = line_index + 1 if line_index + 1 < len(lines) else line_index

                starting_x = num['startingValue'] - 1 if num['startingValue'] - 1 >= 0 else num['startingValue']
                ending_x = num['startingValue'] + len(num['n']) if num['startingValue'] + len(num['n']) < len(line) else num['startingValue'] + len(num['n']) - 1
                
                print(f"SX: {starting_x} | SY: {starting_y} |EX: {ending_x} | EY: {ending_y} | Line: {line_index} | Num: {num['n']}")

                found = False;
                for y in range(starting_y, ending_y + 1):
                    for x in range(starting_x, ending_x + 1):
                        print(f"X: {x} | Y: {y} | SYM: {lines[y][x]}")
                        if isSymbol(lines[y][x], 1):
                            print(f"{lines[y][x]} found inside {x},{y}")
                            if lines[y][x] == '*':
                                gear_found = False
                                if gears:
                                    for gear in gears:
                                        if gear['x'] == x and gear['y'] == y:
                                            gear['gears'].append(num['n'])
                                            gear_found = True
                                    if not gear_found:
                                        gears.append({
                                            'x': x,
                                            'y': y,
                                            'gears': [num['n']]
                                        })
                                else:
                                    gears.append({
                                        'x': x,
                                        'y': y,
                                        'gears': [num['n']]
                                    })
                            found = True
                if found:
                    print("found")
                    part_numbers.append(num['n'])
                        
                num['n'] = ''
                num['startingValue'] = -1

        if char_index == len(line)-1:
            if num['startingValue'] != -1:
                print(f"End of Num: {num['n']}")
                starting_y = line_index - 1 if line_index - 1 >= 0 else line_index
                ending_y = line_index + 1 if line_index + 1 < len(lines) else line_index

                starting_x = num['startingValue'] - 1 if num['startingValue'] - 1 >= 0 else num['startingValue']
                ending_x = num['startingValue'] + len(num['n']) if num['startingValue'] + len(num['n']) < len(line) else num['startingValue'] + len(num['n']) - 1
                
                print(f"SX: {starting_x} | SY: {starting_y} |EX: {ending_x} | EY: {ending_y} | Line: {line_index} | Num: {num['n']}")

                found = False;
                for y in range(starting_y, ending_y + 1):
                    for x in range(starting_x, ending_x + 1):
                        print(f"X: {x} | Y: {y} | SYM: {lines[y][x]}")
                        if isSymbol(lines[y][x], 1):
                            print(f"{lines[y][x]} found inside {x},{y}")
                            if lines[y][x] == '*':
                                gear_found = False
                                if gears:
                                    for gear in gears:
                                        if gear['x'] == x and gear['y'] == y:
                                            gear['gears'].append(num['n'])
                                            gear_found = True
                                    if not gear_found:
                                        gears.append({
                                            'x': x,
                                            'y': y,
                                            'gears': [num['n']]
                                        })
                                else:
                                    gears.append({
                                        'x': x,
                                        'y': y,
                                        'gears': [num['n']]
                                    })
                            found = True
                if found:
                    part_numbers.append(num['n'])
                        
                num['n'] = ''
                num['startingValue'] = -1

result_pn = 0
for num in part_numbers:
    result_pn += int(num)

result_gr = 0
for gear in gears:
    if len(gear['gears']) == 2:
        ratio = 1
        for g in gear['gears']:
            ratio *= int(g)
        result_gr += ratio

# print(part_numbers.keys())
# print(gears)
print(result_gr)