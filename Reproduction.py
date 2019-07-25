import pickle as pk
import pygame.mixer as PM
import RPi.GPIO as GPIO
import SchermateGUI
import Pause
import fileManaging as fm
from math import log10, floor


path= "/home/pi/Documents/fileAudio"

class Reproduction:

    def reproduce_file_audio(self, id, list):
        find = False
        messaggio =""
        for audio in list:
            if int(audio.idButton) == id:
                PM.init()
                PM.music.load(path + "/" + audio.name)
                PM.music.play()
                messaggio ="In riproduzione il file audio: \n" + audio.name + " \nassociato al pulsante " + audio.idButton
                #SchermateGUI.SchermateGUI.show_dialog_with_time("In riproduzione il file audio: \n" + audio.name + " \nassociato al pulsante " + audio.idButton, 2)
                find = True
        if find == False:
            messaggio = "Attenzione: \nnessun file\nassociato a questo pulsante"
            #SchermateGUI.SchermateGUI.show_dialog_with_time("Attenzione: \nnessun file\nassociato a questo pulsante", 2)
        return messaggio

    # a seguire 2 funzioni per aumentare e diminuire il volume
    # ogni volta che vengono richiamate cambiano il valore del volume del 10 per cento
    def increse_vol():

        PM.init()
        current_volume = PM.music.get_volume()
        PM.music.set_volume(current_volume + 0.1)

    def decrese_vol():

        PM.init()
        current_volume = PM.music.get_volume()
        PM.music.set_volume(current_volume - 0.1)

    # funzione che restituisce il valore del volume in un range da 10 a 100
    def give_volume():

        PM.init()
        volume = PM.music.get_volume()
        volume = round(volume, -int(floor(log10(abs(volume)))))

        volume = volume * 100

        if volume < 20:
            volume = 10.0
        elif volume < 10:
            volume = 0
        return str(volume)[:3].replace('.',
                                       '')  # rimuove il punto decimale del volume convertito nell' intervallo 10-100

