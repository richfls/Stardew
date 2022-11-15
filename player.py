import pygame as py
from settings import *
from support import *
from timer import *

class Player(py.sprite.Sprite): #Child class of pygames sprite class
    def __init__(self, pos, group):
        super().__init__(group)#this gives this class access to the functions inside the group class
        
        self.import_assets()

        self.image = py.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)#set the pos to be in the center of the rect

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0
        #general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        #movement
        self.direction = py.math.Vector2()
        self.pos = py.math.Vector2(self.rect.center)
        self.speed = 200
        self.timers = {
            'tool use': Timer(350, self.use_tool)
            }

        #tools
        self.selected_tool = "axe"

    def use_tool(self):
        print(self.selected_tool)

    def import_assets(self):
        self.animations = {'up':[],'down':[],'left':[],'right':[],
                           'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
                           'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
                           'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
                           'right_water':[],'left_water':[],'up_water':[],'down_water':[]}

        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation]=import_folder(full_path)
        print(self.animations)

    def animate(self,dt):#animation method
        self.frame_index += 4 * dt#increase frame number
        if self.frame_index >= len(self.animations[self.status]):#check if we've reached the end of the frame list
            self.frame_index = 0#reset the frame index if we've reached the end
        self.image = self.animations[self.status][int(self.frame_index)]#sets image to correct frame

    def input(self):
        keys = py.key.get_pressed()
        if not self.timers['tool use'].active:
            if keys[py.K_UP]:
                self.direction.y = -1
                self.status = "up"
            elif keys[py.K_DOWN]:
                self.direction.y = 1
                self.status = "down"
            elif keys[py.K_RIGHT]:
                self.direction.x = 1
                self.status = "right"
            elif keys[py.K_LEFT]:
                self.direction.x = -1
                self.status = "left"
            else:
                self.direction.y = 0
                self.direction.x = 0

        if keys[py.K_SPACE]:
            self.timers['tool use'].activate()
            self.direction = py.math.Vector2()
            self.frame_index = 0
        
        #print(self.direction)

    def get_status(self):
        #check if the player is not moving
        if self.direction.magnitude() == 0:
            #add _idle to the status
            self.status = self.status.split("_")[0] + "_idle"
            #tool use
            if self.timers['tool use'].active:
                print("tool is being used")
                self.status = self.status.split("_")[0] + "_" + self.selected_tool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
        
        
    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #print(self.direction)
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y 

    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)
