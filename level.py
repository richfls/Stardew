import pygame as py
from settings import *

class Level:
    def __init__(self):
        #gets a reference (address) to the currently set display surface
        self.display_surface = py.display.get_surface()
        #class "group" is part of pygame's sprites support. it is a class that manages a *list* of sprites.
        self.all_sprites = py.sprite.Group()

        self.setup()#call the setup function

    def setup(self):
        self.player = Player((640))


    def run(self, dt):
        print("run game")
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)#draw fuction from group class
        self.all_sprites.update()#another fuction from group class
