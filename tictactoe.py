#!/usr/bin/env python

x_or_o = 1 # Indicates turn
# Each variable below represents a spot on the tictactoe board.
a1 = 256 # 100000000
a2 = 128 # 010000000
a3 =  64 # 001000000
b1 =  32 # 000100000
b2 =  16 # 000010000
b3 =   8 # 000001000
c1 =   4 # 000000100
c2 =   2 # 000000010
c3 =   1 # 000000001
# Winning moves
w1 = 448
w2 = 56
w3 = 7
w4 = 292
w5 = 146
w6 = 73
w7 = 273
w8 = 85

# Moves made by X
x_board = 0
# Moves made by O
o_board = 0

def has_winner():
    global w1, w2, w3, w4, w5, w6, w7, w8
    return ((x_board & w1 == w1) or
            (x_board & w2 == w2) or
            (x_board & w3 == w3) or
            (x_board & w4 == w4) or
            (x_board & w5 == w5) or
            (x_board & w6 == w6) or
            (x_board & w7 == w7) or
            (x_board & w8 == w8) or  # Check if X is a winner
            (o_board & w1 == w1) or
            (o_board & w2 == w2) or
            (o_board & w3 == w3) or
            (o_board & w4 == w4) or
            (o_board & w5 == w5) or
            (o_board & w6 == w6) or
            (o_board & w7 == w7) or
            (o_board & w8 == w8))    # Check if O is a winner


def game_over():
    global x_board, o_board
    return ((x_board | o_board) >= 511) or has_winner()


def get_x_or_o(p):
    """
    Determins if a spot is filled by x, o, or is empty.
    :param p: The integer spot on the board.
    :return: str
    """
    global x_board, o_board
    if x_board & p == p:
        return "x"
    if o_board & p == p:
        return "o"
    return "-"

def tic_tac_toe_board():
    """
    Prints our tictactoe board using get_x_or_y to decide which fills a spot.
    :return:
    """
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    m = 3
    print(" a", "b", "c", sep=" " * m)
    print(" " * m, " " * m, " " * m, sep='|')
    print(f"1{get_x_or_o(a1)} ", f" {get_x_or_o(b1)} ", f" {get_x_or_o(c1)} ", sep='|')
    print("_" * m, "_" * m, "_" * m, sep='|')
    print(" " * m, " " * m, " " * m, sep='|')
    print(f"2{get_x_or_o(a2)} ", f" {get_x_or_o(b2)} ", f" {get_x_or_o(c2)} ", sep='|')
    print("_" * m, "_" * m, "_" * m, sep='|')
    print(" " * m, " " * m, " " * m, sep='|')
    print(f"3{get_x_or_o(a3)} ", f" {get_x_or_o(b3)} ", f" {get_x_or_o(c3)} ", sep='|')
    print(" " * m, " " * m, " " * m, sep='|')

def get_move():
    """
    Requests a players intended move, verifies it is an open spot, and updates the x or o board if it's available.
    :return:
    """
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, x_or_o, x_board, o_board
    move = input("Make your choice: ")
    if move.lower() == "q":
        return False

    board = x_board | o_board
    if move == "a1":
        if board & a1 == a1:
            print("This space is occupied")
            return
        if x_or_o == 1:
            x_board = x_board | a1
        else:
            o_board = o_board | a1
    if move == "a2":
        if board & a2 == a2:
            print("This space is occupied")
            return
        if x_or_o == 1:
            x_board = x_board | a2
        else:
            o_board = o_board | a2
    if move == "a3":
        if board & a3 == a3:
            print("This space is occupied")
            return
        if x_or_o == 1:
            x_board = x_board | a3
        else:
            o_board = o_board | a3
    if move == "b1":
        if board & b1 == b1:
            print("This space is occupied")
            return
        if x_or_o == 1:
            x_board = x_board | b1
        else:
            o_board = o_board | b1
    if move == "b2":
        if board & b2 == b2:
            print("This space is occupied")
            return
        if x_or_o == 1:
            x_board = x_board | b2
        else:
            o_board = o_board | b2
    if move == "b3":
        if board & b3 == b3:
            print("This space is occupied")
            return
        if x_or_o == 1:
            x_board = x_board | b3
        else:
            o_board = o_board | b3
    if move == "c1":
        if board & c1 == c1:
            print("This space is occupied")
            return
        if x_or_o == 1:
            x_board = x_board | c1
        else:
            o_board = o_board | c1
    if move == "c2":
        if board & c2 == c2:
            print("This space is occupied")
            return
        if x_or_o == 1:
            x_board = x_board | c2
        else:
            o_board = o_board | c2
    if move == "c3":
        if board & c3 == c3:
            print("This space is occupied")
            return
        if x_or_o == 1:
            x_board = x_board | c3
        else:
            o_board = o_board | c3
    x_or_o = (x_or_o + 1) % 2
    return True

tic_tac_toe_board()
while get_move() and not game_over():
    tic_tac_toe_board()
