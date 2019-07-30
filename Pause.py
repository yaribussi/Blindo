import pygame.mixer as PM

class Pause:

    def __init__(self):
        self.unpaused = True

    def toggle(self):
        if self.unpaused:
            PM.music.pause()
            # print("in pause")
            self.unpaused=not self.unpaused
            
        else:
            PM.music.unpause()
            # print("in play")
            self.unpaused=not self.unpaused

    # this method will reset the paused value to the default one, False
    def reset(self):
        self.unpaused = True
