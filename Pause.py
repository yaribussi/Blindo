import pygame.mixer as PM

class Pause():

    def __init__(self):
        self.paused = True

    def toggle(self):
        if self.paused:
            PM.music.pause()
           # print("in pause")
            self.paused=not self.paused
            
        else:
            PM.music.unpause()
            #print("in play")
            self.paused=not self.paused
            
