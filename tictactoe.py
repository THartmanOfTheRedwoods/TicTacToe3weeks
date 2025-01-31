#!/usr/bin/env python

x_or_o = 1 # Indicates turn
# Each variable below represents a spot on the tictactoe board.
a1 = 256  # 100000000
a2 = 128  # 010000000
a3 =  64  # 001000000
b1 =  32  # 000100000
b2 =  16  # 000010000
b3 =   8  # 000001000
c1 =   4  # 000000100
c2 =   2  # 000000010
c3 =   1  # 000000001
# Winning moves
w1 = 448  # 111000000
w2 =  56  # 000111000
w3 =   7  # 000000111
w4 = 292  # 100100100
w5 = 146  # 010010010
w6 =  73  # 001001001
w7 = 273  # 100010001
w8 =  84  # 001010100

# Moves made by X
x_board = 0
# Moves made by O
o_board = 0
# Variables to track winner
winner_x = False
winner_o = False

def has_winner():
    global w1, w2, w3, w4, w5, w6, w7, w8, winner_x, winner_o
    winner_x = ((x_board & w1 == w1) or
                (x_board & w2 == w2) or
                (x_board & w3 == w3) or
                (x_board & w4 == w4) or
                (x_board & w5 == w5) or
                (x_board & w6 == w6) or
                (x_board & w7 == w7) or
                (x_board & w8 == w8)) # Check if X is a winner
    winner_o = ((o_board & w1 == w1) or
                (o_board & w2 == w2) or
                (o_board & w3 == w3) or
                (o_board & w4 == w4) or
                (o_board & w5 == w5) or
                (o_board & w6 == w6) or
                (o_board & w7 == w7) or
                (o_board & w8 == w8))    # Check if O is a winner
    return winner_x or winner_o


def game_over():
    global x_board, o_board
    return ((x_board | o_board) >= 511) or has_winner()


def get_x_or_o(p):
    """
    Determines if a spot is filled by x, o, or is empty.
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
    n = m+1
    print("  a", "b", "c", sep=" " * m)
    print(" " * n, " " * m, " " * m, sep='|')
    print(f"1 {get_x_or_o(a1)} ", f" {get_x_or_o(b1)} ", f" {get_x_or_o(c1)} ", sep='|')
    print(" "+"_" * m, "_" * m, "_" * m, sep='|')
    print(" " * n, " " * m, " " * m, sep='|')
    print(f"2 {get_x_or_o(a2)} ", f" {get_x_or_o(b2)} ", f" {get_x_or_o(c2)} ", sep='|')
    print(" "+"_" * m, "_" * m, "_" * m, sep='|')
    print(" " * n, " " * m, " " * m, sep='|')
    print(f"3 {get_x_or_o(a3)} ", f" {get_x_or_o(b3)} ", f" {get_x_or_o(c3)} ", sep='|')
    print(" " * n, " " * m, " " * m, sep='|')

def add_marker(sq):
    global x_board, o_board
    board = x_board | o_board
    if board & sq == sq:
        print( "This space is occupied" )
        return False
    if x_or_o == 1:
        x_board = x_board | sq
    else:
        o_board = o_board | sq
    return True


def get_move():
    """
    Requests a players intended move, verifies it is an open spot, and updates the x or o board if it's available.
    :return:
    """
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, x_or_o, x_board, o_board
    move = input("Make your choice: ")
    if move.lower() == "q":
        return False

    if move == "a1":
        if not add_marker(a1): return True
    if move == "a2":
        if not add_marker(a2): return True
    if move == "a3":
        if not add_marker(a3): return True
    if move == "b1":
        if not add_marker(b1): return True
    if move == "b2":
        if not add_marker(b2): return True
    if move == "b3":
        if not add_marker(b3): return True
    if move == "c1":
        if not add_marker(c1): return True
    if move == "c2":
        if not add_marker(c2): return True
    if move == "c3":
        if not add_marker(c3): return True

    x_or_o = (x_or_o + 1) % 2  # Rotate marker.
    return True

tic_tac_toe_board()
while get_move() and not game_over():
    tic_tac_toe_board()

tic_tac_toe_board()
if winner_x:
    print("X Wins!!!")
elif winner_o:
    print("O Wins!!!")
else:
    print("It's a draw.")