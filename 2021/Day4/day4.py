#!/usr/bin/python3

from colorama import Fore

def print_c_board(board):
    for line in board:
        printable_line = ''
        for num in line:
            if num[1]:
                printable_line += Fore.YELLOW
            printable_line += num[0] + " "
            if num[1]:
                printable_line += Fore.RESET
        print(printable_line)
    print('')

def clean_board(board):
    new_board = []
    for line in board:
        nums = line.split(' ')
        new_line = []
        for num in nums:
            if num == "":
                pass
            else:
                n = [num, False]
                new_line.append(n)
        new_board.append(new_line)
    return new_board
        
def is_winner(board):
    for line in board:
        horz_count = 0
        for num in line:
            if num[1]:
                horz_count += 1
                if horz_count == 5:
                    return True

def check_boards(call):
    for b in all_boards:
        for line in b:
            for num in line:
                if num[0] == call:
                    num[1] = True
                    if is_winner(b):
                        return [True,b]
    return [False,'']

def play_bingo():
    for call in ball_calls:
        success = check_boards(call)
        if success[0]:
            print("BINGO")
            print_c_board(success[1])
            break

input_file = open("sample.txt")
input_text = input_file.read().split("\n")

ball_calls = []
line_count = 0

all_boards = []
boards = []
board = []

ball_calls = input_text[0].split(',')
input_text.pop(0)

for line in input_text:
    if line == '':
        input_text.remove(line)

for i in range(len(input_text)):
    if line_count < 5:
        board.append(input_text[i])
        line_count += 1
        continue

    boards.append(board)
    line_count = 1
    board.clear()
    board.append(input_text[i])
boards.append(board)


for b in boards:
    all_boards.append(clean_board(b))

play_bingo()



