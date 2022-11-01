import pygame as py
import sys
from settings import *
from level import Level

#Class-Game----------------------------------------
class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
        self.clock = py.time.Clock()
        self.level = Level()

    def run(self):
        while True: #GAME-LOOP---------------------------------------
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

            dt = self.clock.tick()/1000 #FPS HANDLER
            self.level.run(dt)
            py.display.update()#WORKS LIKE FLIP BUT CAN UPDAT PORTIONS OF THE SCREEN IF WE WANT
        #END-OF-GAME-LOOP--------------------------------------------------------------------------
if __name__ == '__main__':
    game =  Game()
    game.run()#RUNS THE GAME LOOP

