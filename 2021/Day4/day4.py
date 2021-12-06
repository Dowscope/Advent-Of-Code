#!/usr/bin/python3

from colorama import Fore

ball_calls = []
all_boards = []

def gen_boards(input):
    line_count = 0

    boards = []
    board = []

    ball_calls = input[0].split(',')
    input.pop(0)

    for line in input:
        if line == '':
            input.remove(line)

    for i in range(len(input)):
        if line_count < 5:
            board.append(input[i])
            line_count += 1
            continue

        boards.append(board)
        line_count = 1
        board.clear()
        board.append(input[i])
    boards.append(board)
    return boards

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
                continue
            else:
                n = [num, False]
                new_line.append(n)
        new_board.append(new_line)
    return new_board

def calc_win(board, call):
    sum_of_nums = 0
    for line in board:
        for num in line:
            if num[1]:
                continue
            sum_of_nums += int(num[0])
    result = int(call) * sum_of_nums
    print(result)
        
def is_winner(board, call):
    for i in range(len(board)):
        horz_count = 0
        vert_count = 0

        for num in board[i]:
            if num[1]:
                horz_count += 1
                if horz_count == 5:
                    calc_win(board, call)
                    return True

        for j in range(5):
            if board[j][i][1]:
                vert_count += 1
                if vert_count == 5:
                    calc_win(board, call)
                    return True
        

def check_boards(call):
    for b in all_boards:
        for line in b:
            for num in line:
                if num[0] == call:
                    num[1] = True
                    if is_winner(b, call):
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

unclean_boards = gen_boards(input_text)

print(unclean_boards)

# for b in boards:
#     all_boards.append(clean_board(b))

# play_bingo()

# for b in all_boards:
#     print_c_board(b)

