# Tic Tac Toe - Console-Based
#
# This program will allow the user to play Tic Tac Toe against the computer. 
#The board will be drawn in text-characters on the screen.
#
# Author: I aint givin you my name
# Date Created: August 12, 2024
# Last Modified: August 22, 2024

EMPTY = "empty"
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
  
draw_board(board         )