from Reproduction import Reproduction as repr
import fileManaging as fm
from Pause import Pause
class Button_controller:

    def __init__(self, pause):
        self.__pause=Pause()
    '''
    def set_pause(self, pause):
        self.__pause=pause

    def get_pause(self):
        return self.pause
    '''
    def manage_pulsante_riproduzione(self, idPulsante):
        list = fm.give_sorted_list()
        repr.reproduce_file_audio(idPulsante, list)

    def manage_pulsante_play_pause(self):
        self.__pause.toggle()


