import pygame as py
from settings import *

class PLAYER(py.sprite.Sprite): #Child class of pygames sprite class
    def __init__(self, pos, group):
        super().__init__(group)#this gives this class access to the functions inside the group class
        self.image = py.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)#set the pos to be in the center of the rect
