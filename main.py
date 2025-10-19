import sys
from Game import *
from AI import *
import time


def main():
   
    game = Game()
    ai = Ai()
    gamemode = "ai"

    while(True):
        for event in pg.event.get():

            # quit event
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            pg.display.update()


            # mouse event
            
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = event.pos
                col = pos[0] // SQUARE
                row = pos[1] // SQUARE
                if game.board.isEmptySqr(col,row):
                    game.makeMove(col,row)
                    pg.display.update()
                    if game.board.final_state() ==AI:
                        win(AI,game)
                    elif game.board.final_state() ==PLAYER:
                        win(PLAYER,game)
            if event.type  == pg.KEYDOWN:                
                if event.key == pg.K_r:
                    restart(game)

            if game.player == ai.player and gamemode == "ai":
                
                pg.display.update()
                move = ai.eval(game.board)
                game.makeMove(move[1],move[0])
       

def win(player,game):
    print(f"the player {player} WON!!")
    time.sleep(1)
    restart(game)

def restart(game):
   game.__init__()
    

if __name__ == '__main__':
    main()