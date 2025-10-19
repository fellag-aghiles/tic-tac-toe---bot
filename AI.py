import pygame as pg
import copy as cp
import numpy as np
from Game import Board
from Constant import AI, PLAYER

class Ai:
    def __init__(self, player=AI):
        # Set the marker for the AI (usually a specific number or symbol)
        self.player = AI

    def minimax(self, board: Board, maximazing):
        # First, check if the game has ended
        case = board.final_state()
        if case == AI:
            return 1, None    # AI has won
        if case == PLAYER:
            return -1, None   # Human player has won
        elif board.isfull():
            return 0, None    # The game is a tie

        if maximazing:
            maxeval = -100
            bestmove = None
            # Try every possible move for the AI
            empty_sqrs = board.getEmptySqrs()
            for (row, col) in empty_sqrs:
                temp_board = cp.deepcopy(board)
                temp_board.mark(col, row, AI)
                eval = self.minimax(temp_board, False)[0]
                if eval > maxeval:
                    maxeval = eval
                    bestmove = (row, col)
            return maxeval, bestmove

        else:
            mineval = 100
            bestmove = None
            # Simulate each move the human could make
            empty_sqrs = board.getEmptySqrs()
            for (row, col) in empty_sqrs:
                temp_board = cp.deepcopy(board)
                temp_board.mark(col, row, PLAYER)
                eval = self.minimax(temp_board, True)[0]
                if eval < mineval:
                    mineval = eval
                    bestmove = (row, col)
            return mineval, bestmove

    def eval(self, main_board):
        # Decide on the best move based on the current board
        eval, move = self.minimax(main_board, True)
        print(f'AI has chosen to mark the square in pos {move} with an eval of: {eval}')
        return move