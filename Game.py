import pygame as pg
import numpy as np
from Constant import *



class Board:
    def __init__ (self,screen):
        self.squares = np.zeros((3,3))
        self.empty_squares =  self.squares
        self.marked_squares = 0


    def final_state(self, show=False)->int:
        '''
            @return 0 if there is no win yet
            @return 1 if player 1 wins
            @return 2 if player 2 wins
        '''
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]
            
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
             
                return self.squares[row][0]
        
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] !=0:
      
            return self.squares[0][0]
        
        if self.squares[0][2] == self.squares[1][1] ==self.squares[2][0] !=0:
        
            return self.squares[1][1]

        return 0
    
    def mark(self,col,row,player):
        self.squares[row][col] = player
        self.marked_squares += 1




    def isEmptySqr(self,col,row)->bool:
        return self.squares[row][col] ==0

    def getEmptySqrs(self):
        emptySqr = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.squares[row][col] ==0:
                    emptySqr.append((row,col))
        return emptySqr
    
    def isfull(self):
        if self.marked_squares == 9:
            return True
        return False
    
    def isempty(self):
        return self.marked_squares ==0


class Game:
    

    def __init__ (self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.screen.fill(BG_COLOR)
        pg.display.flip()
        self.player = PLAYER
        self.board = Board(self.screen)
        self.drawLine()
    
    
    def drawLine(self):
        # -- colones --
        pg.draw.line(self.screen,LINE_COLOR,(SQUARE,0),(SQUARE,HEIGHT),LINE_SIZE)
        pg.draw.line(self.screen,LINE_COLOR,(WIDTH-SQUARE,0),(WIDTH-SQUARE,HEIGHT),LINE_SIZE)

        # -- rows --
        pg.draw.line(self.screen,LINE_COLOR,(0,SQUARE),(WIDTH,SQUARE),LINE_SIZE)
        pg.draw.line(self.screen,LINE_COLOR,(0,HEIGHT-SQUARE),(WIDTH,HEIGHT-SQUARE),LINE_SIZE)
    
    def drawFig(self,col,row):

        if self.player ==2:
            pg.draw.circle(self.screen,CIRCLE_COLOR,(col*SQUARE+SQUARE //2,row*SQUARE+SQUARE//2),80,CIRCLE_SIZE)

        elif self.player ==1:
            # -- decdendent
            
            start_dec = (col*SQUARE + OFFSET_SHAPE ,row*SQUARE+OFFSET_SHAPE)
            end_dec = (col*SQUARE+SQUARE-OFFSET_SHAPE,row*SQUARE+SQUARE-OFFSET_SHAPE)
            pg.draw.line(self.screen,X_COLOR,start_dec,end_dec,X_SIZE) 

            # --acendent
            start_ace = (col*SQUARE+SQUARE-OFFSET_SHAPE,row*SQUARE+OFFSET_SHAPE)
            end_ace = (col*SQUARE + OFFSET_SHAPE,row*SQUARE+SQUARE-OFFSET_SHAPE)
            pg.draw.line(self.screen,X_COLOR,start_ace,end_ace,X_SIZE) 
            



    def makeMove(self,col,row):
        self.board.mark(col,row,self.player)
        self.drawFig(col,row)
        self.nextPlayer()


    def nextPlayer(self):
        self.player = self.player % 2 +1
