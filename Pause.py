import pygame.mixer as PM

class Pause():

    def __init__(self):
        self.paused = True

    def toggle(self):
        if self.paused:
            PM.music.pause()
            self.paused=not self.paused
            
        else:
            PM.music.unpause()
            self.paused=not self.paused
