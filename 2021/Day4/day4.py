#!/usr/bin/python3

from colorama import Fore


class Bingo_card:
    def __init__(self, board_text):
        self.numbers = board_text
        self.last_call_number= 0
        self.won = False
        self.result = 0
    def print(self):
        for line in self.numbers:
            printable_line = ''
            for num in line:
                if num[1]:
                    printable_line += Fore.YELLOW
                printable_line += num[0] + " "
                if num[1]:
                    printable_line += Fore.RESET
            print(printable_line)
        print('')
    def print_result(self):
        print(self.result)
    def print_last_call(self):
        print(self.last_call_number)
    def is_won(self):
        return self.won
    def is_winner(self):
        for i in range(len(self.numbers)):
            horz_count = 0
            vert_count = 0

            for num in self.numbers[i]:
                if num[1]:
                    horz_count += 1
                    if horz_count == 5:
                        self.calc_win()
                        self.won = True
                        return True

            for j in range(5):
                if self.numbers[j][i][1]:
                    vert_count += 1
                    if vert_count == 5:
                        self.calc_win()
                        self.won = True
                        return True
    def calc_win(self):
        sum_of_nums = 0
        for line in self.numbers:
            for num in line:
                if num[1]:
                    continue
                sum_of_nums += int(num[0])
        self.result = self.last_call_number * sum_of_nums
    def update(self, call):
        self.last_call_number = int(call)
        for line in self.numbers:
            for num in line:
                if num[0] == call:
                    num[1] = True
                    if self.is_winner():
                        return True
        return False

def gen_boards(input):
    line_count = 0

    board = []

    global ball_calls
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
        game_boards.append(Bingo_card(clean_board(board)))
        line_count = 1
        board.clear()
        board.append(input[i])
    game_boards.append(Bingo_card(clean_board(board)))

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
    for b in game_boards:
        if b.is_won():
            continue
        elif b.update(call):
            global wins
            wins = wins + 1
            if wins == len(game_boards):
                return [True, b]
    return [False,'']

def play_bingo():
    for call in ball_calls:
        success = check_boards(call)
        if success[0]:
            print("BINGO")
            success[1].print_result()
            success[1].print()
            break

ball_calls = []
game_boards = []
wins = 0

input_file = open("input.txt")
input_text = input_file.read().split("\n")

gen_boards(input_text)

play_bingo()

# for b in game_boards:
#     b.print()

