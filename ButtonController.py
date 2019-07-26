from Reproduction import Reproduction as repr
import fileManaging as fm
import SchermateGUI
from Pause import Pause

class Button_controller:

    def __init__(self, pause):
        self.__pause=pause
    '''
    def set_pause(self, pause):
        self.__pause=pause

    def get_pause(self):
        return self.pause
    '''
    def manage_pulsante_riproduzione(self, idPulsante):
        list = fm.load_list()
        self.__pause.reset()
        messaggio = repr.reproduce_file_audio(self, idPulsante, list)
       # SchermateGUI.SchermateGUI.show_dialog_with_time(messaggio, 2)

    def manage_pulsante_play_pause(self):
        self.__pause.toggle()


