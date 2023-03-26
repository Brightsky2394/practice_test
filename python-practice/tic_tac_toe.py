#!/usr/bin/python3
from random import randrange

def display_board(board):
    print("+-------" * 3, "+", sep='')
    for row in range(3):
        print("|       " * 3, "|", sep='')
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end='')
        print("|")
        print("|       " * 3, "|", sep='')
        print("+-------" * 3, "+", sep='')

def make_list_of_free_fields(board):
    free_list = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_list.append((row, col))
    return free_list


def enter_move(board):
    approve = False
    while not approve:
        move = input("Enter the number of move : ")
        approve = len(move) == 1 and '1' <= move <= '9'
        if not approve:
            print("Bad move - repeat input!")
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        approve = sign not in ['X', 'O']
        if not approve:
            print("Field already occupied - repeat input!")
            continue
    board[row][col] = 'O'

def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        num = randrange(cnt)
        row, col = free[num]
        board[row][col] = 'X'

def victory_for(board, sgn):
    if sgn == 'X':
        who = 'me'
    elif sgn == 'O':
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who
    return None

board = [[3 * i + j + 1 for j in range(3)] for i in range(3)]
board[1][1] = 'X'
free_field = make_list_of_free_fields(board)
human_turn = True
while len(free_field):
    display_board(board)
    if human_turn:
        enter_move(board)
        result = victory_for(board, 'O')
    else:
        draw_move(board)
        result = victory_for(board, 'X')
    if result is not None:
        break
    human_turn = not human_turn
    free_field = make_list_of_free_fields(board)

if result == 'me':
    print("I won")
elif result == 'you':
    print("You won")
else:
    print("Tie")



