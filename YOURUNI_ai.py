
#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author: YOUR NAME AND UNI 
"""

import random
import sys
import time
import math

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    if color == 2:
        co = 1
    elif color == 1:
        co = 2
    diff = get_score(board)[color-1] - get_score(board)[co-1]
    return diff

"""
def compute_utility(board, color):
  
  WEIGHTS = [4, -3, 2, 2, 2, 2, -3, 4,
               -3, -4, -1, -1, -1, -1, -4, -3,
               2, -1, 1, 0, 0, 1, -1, 2,
               2, -1, 0, 1, 1, 0, -1, 2,
               2, -1, 0, 1, 1, 0, -1, 2,
               2, -1, 1, 0, 0, 1, -1, 2,
               -3, -4, -1, -1, -1, -1, -4, -3,
               4, -3, 2, 2, 2, 2, -3, 4]
   utility = 0
   weights = [[1000, -500, 300, 300, 300, 300, -500, 1000,]
              [-500, -600, -300, -300, -300, -300, -600, -500,
              [300, -100, 100, 0, 0, 100, -100, 300],
              [300, -100, 0, 100, 100, 0, -100, 300],
              [300, -100, 0, 100, 100, 0, -100, 300],
              [300, -100, 100, 0, 0, 100, -100, 300],
              [-500, -600, -100, -100, -100, -100, -600, -500],
              [1000, -500, 300, 300, 300, 300, -500, 1000]]
   for i in range(len(board)):
     for j in range(len(board)[i]):
       if board[i][j] = (color - 1):
          utility
"""


############ MINIMAX ###############################

def minimax_min_node(board, color):

    if color == 2:
      opp_color = 1
    elif color == 1:
      opp_color = 2

    if not get_possible_moves(board, opp_color):      
        return compute_utility(board, color)     

    beta = math.inf
    for i, j in get_possible_moves(board, opp_color):
        new_board = play_move(board, opp_color, i, j)
        utility = minimax_max_node(new_board, color)
        if utility < beta:
            beta = utility
    return beta


def minimax_max_node(board, color):
    """
    Return the minimum score the MAX player can achieve 
    with any move starting at board. 
    """
    if not get_possible_moves(board, color):
        return compute_utility(board, color)

    alpha = -math.inf
    for i, j in get_possible_moves(board, color):
        new_board = play_move(board, color, i, j)
        utility = minimax_min_node(new_board, color)
        if utility > alpha:
            alpha = utility
    return alpha

def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move.
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.
    """

    moves = get_possible_moves(board, color)

    best_move = None
    alpha = -math.inf
    for move in moves: 
      i,j = move 
      new_board = play_move(board, color, i, j)
      score = minimax_min_node(new_board, color)
      if score > alpha: 
        best_move = move
        alpha = score 

    return best_move 



    """best_action = None
    best_utility = -math.inf
    for i, j in get_possible_moves(board, color):
        board = play_move(board, color, i, j)
        utility = minimax_min_node(board, color)
        if utility > best_utility:
            best_utility = utility
            best_action = i, j
    return best_action
    """
    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, level, limit): 
    if color == 2:
      opp_color = 1
    elif color == 1:
      opp_color = 2

    if not get_possible_moves(board, opp_color):      
        return compute_utility(board, color)     

    beta = math.inf
    for i, j in get_possible_moves(board, opp_color):
        new_board = play_move(board, opp_color, i, j)
        if level+1 > limit:
            continue
        utility = alphabeta_max_node(new_board, color, beta, level+1, limit)
        if utility < beta:
            beta = utility
        if beta < alpha: 
          return beta 
    return beta



#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, beta, level, limit):
    if not get_possible_moves(board, color):
        return compute_utility(board, color)

    alpha = -math.inf
    for i, j in get_possible_moves(board, color):
        new_board = play_move(board, color, i, j)
        if level+1 > limit:
            continue
        utility = alphabeta_min_node(new_board, color, alpha, level+1, limit)
        if utility > alpha:
            alpha = utility
        if alpha > beta:
            return alpha
    return alpha

def select_move_alphabeta(board, color): 
    moves = get_possible_moves(board, color)

    best_move = None
    alpha = -math.inf
    for move in moves: 
        if move==(0,0) or move==(0,7) or move==(7,0) or move==(7,7):
            return move
        i,j = move 
        new_board = play_move(board, color, i, j)
        score = alphabeta_min_node(new_board, color, alpha, 0, 4)
        if score > alpha: 
            best_move = move
            alpha = score 
        return best_move 

####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Your Mom") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            #movei, movej = select_move_minimax(board, color)
            movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
