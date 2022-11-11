import pygame as py

class Time:
    def __init__(self,duration, func = None):
        self.duration = duration
        self.func = func #code that happens once the timer is done
        self.start_time = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = py.time.get_ticks()

    def deactivate(self):
        self.activate = False
        self.start_time = 0

    def update(self):
        current_time = py.time.get_ticks()

        if current_time - self.start_time >= self.duration:
            self.deactivate()
            if self.func:#if there's something to run afterwards
                self.func()#run it
