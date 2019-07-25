import pickle as pk
import pygame.mixer as PM
import RPi.GPIO as GPIO
from ButtonController import Button_controller as bc
import SchermateGUI
import Pause
import fileManaging as fm

path= "/home/pi/Documents/fileAudio"

class Reproduction:


    def reproduce_file_audio(self, id, list):
        find = False
        for audio in list:
            if int(audio.idButton) == id:
                PM.init()
                PM.music.load(path + "/" + audio.name)
                PM.music.play()

                SchermateGUI.SchermateGUI.show_dialog_with_time("In riproduzione il file audio: \n"
                                                                + audio.name + " \nassociato al pulsante " + audio.idButton,
                                                                2)
                find = True
        if find == False:
            SchermateGUI.SchermateGUI.show_dialog_with_time(
                "Attenzione: \nnessun file\nassociato a questo pulsante", 2)
