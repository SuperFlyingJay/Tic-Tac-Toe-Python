# Tic Tac Toe - Console-Based
#
# This program will allow the user to play Tic Tac Toe against the computer. 
#The board will be drawn in text-characters on the screen.
#
# Author: I aint givin you my name
# Date Created: August 12, 2024
# Last Modified: August 26         , 2024

EMPTY = "empty"
COMPUTER = "X"
PLAYER = "O"

WHO_SHOULD_GO_FIRST_PROMPT = "Who should go first? "

board = [
         EMPTY, EMPTY, EMPTY,
         EMPTY, EMPTY, EMPTY,
         EMPTY, EMPTY, EMPTY
        ]

def get_symbol(the_board, square_number):
         symbol = the_board[square_number - 1]
         if symbol == EMPTY:
                  return square_number
                  
         return symbol
                  
def draw_board(the_board):
         for row in range(3):
                  print("   |   |   ")
                  print(" {} | {} | {} ".format(get_symbol(the_board, row * 3 + 1), get_symbol(the_board, row * 3 + 2), get_symbol(the_board, row *3 + 3)))
                  print("   |   |   ")
                  if row < 2:
                           print("---+---+---")

print("Hello, lets play Tic Tac Toe!")
print("I'll be {} and you can be {}.".format(COMPUTER, PLAYER))

whose_turn = input(WHO_SHOULD_GO_FIRST_PROMPT).upper()
while whose_turn != COMPUTER and whose_turn != PLAYER:
         print("ERROR: Please enter {} or {}".format(COMPUTER, PLAYER))
         whose_turn = input(WHO_SHOULD_GO_FIRST_PROMPT).upper()
draw_board(board)
