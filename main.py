# Tic Tac Toe - Console-Based
#
# This program will allow the user to play Tic Tac Toe against the computer. 
#The board will be drawn in text-characters on the screen.
#
# Author: I aint givin you my name
# Date Created: August 12, 2024
# Last Modified: August 21, 2024

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
  print("   |   |   ")
  print(" {} | {} | {} ".format(get_symbol(the_board, 1), get_symbol(the_board, 2), get_symbol(the_board, 3)))
  print("   |   |   ")
  print("---+---+---")
  print("   |   |   ")
  print(" {} | {} | {} ".format(get_symbol(the_board, 4), get_symbol(the_board, 5), get_symbol(the_board, 6)))
  print("   |   |   ")
  print("---+---+---")
  print("   |   |   ")
  print(" {} | {} | {} ".format(get_symbol(the_board, 7), get_symbol(the_board, 8), get_symbol(the_board, 9)))
  print("   |   |   ")

draw_board(board         )