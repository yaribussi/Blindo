import pickle as pk
import pygame.mixer as PM
import RPi.GPIO as GPIO
import SchermateGUI
import Pause


#import time
import subprocess
import os
import pyaudio
import wave


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

path= "/home/pi/Documents/fileAudio"
pathfileaudio="/home/pi/Documents/fileAudio"

#name_recoded_file='/home/pi/Desktop/Main/lista'

pulsante_1 = 5            #   giallo
pulsante_2 = 24           #   viola
pulsante_3 = 21           #   blu
pulsante_4 = 26           #   verde

pulsante_5 = 4            #   nero
pulsante_6 = 17           #   grigio
pulsante_pause = 22       #   bianco

GPIO.setup(pulsante_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_pause, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

############    funzione che riproduce un file audio dato uno specifico path        ##########

def play_single_file(path_file_audio):

        PM.init()
        PM.music.load(path_file_audio)
        PM.music.play()

###########  funzione che carica la "lista finale" e cerca al suo interno se esiste
###########   un oggetto fileAudio con lo stesso idButton del pulsante che è stato premuto
def search_and_play_file(id):

    try:

        with open("lista finale1", 'rb') as io:
              my_objects = pk.load(io)


              for audio in my_objects:
                   if int(audio.idButton) == id:
                      SchermateGUI.show_dialog_with_time("In riproduzione il file audio: "
                                            +  audio.name + "associato al pulsante "+audio.idButton,2)
                      play_single_file(path + "/" + audio.name)
                   else:
                       SchermateGUI.show_dialog_with_time("Attenzione, nessun file\nassociato a questo pulsante",2)
                      
    except (FileNotFoundError, IOError) as e:
            print(e)

##########          insieme di funzioni per riprodurre il fileAudio             ############à
#########           DEVONO avere come parametro il pulsante a cui sono associate

PAUSE=Pause.Pause()

def play_and_pause(pulsante):
    global PAUSE
    PAUSE.toggle()
    
    
def my_function1(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        search_and_play_file(1)
    
    
def my_function2(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        search_and_play_file(2)
    
def my_function3(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        search_and_play_file(3)

    
def my_function4(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        search_and_play_file(4)
        
def my_function5(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        search_and_play_file(5)

def my_function6(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        search_and_play_file(6)
##################################################################################################

#######         funzione che aspetta il cambio di evento (from LOW to HIGH)
#######         di tutti i pulsanti collegati alla sccheda
#######         le funzioni richamate da "callback" devono accettare lo stesso parametro del evento che le chiama
#######         infatti tutte le "myFunction"  accettano come parametro il PIN del pulsante
#######         il parametro bounctime fa lo stesso effetto della funzione time.sleep(0.5)
def interupt():

    GPIO.add_event_detect(pulsante_1, GPIO.RISING, callback=my_function1, bouncetime=500)
    GPIO.add_event_detect(pulsante_2, GPIO.RISING, callback=my_function2, bouncetime=500)
    GPIO.add_event_detect(pulsante_3, GPIO.RISING, callback=my_function3, bouncetime=500)
    GPIO.add_event_detect(pulsante_4, GPIO.RISING, callback=my_function4, bouncetime=500)
    GPIO.add_event_detect(pulsante_5, GPIO.RISING, callback=my_function5, bouncetime=500)
    GPIO.add_event_detect(pulsante_6, GPIO.RISING, callback=my_function6, bouncetime=500)
    
    GPIO.add_event_detect(pulsante_pause, GPIO.RISING, callback=play_and_pause, bouncetime=500)
    

interupt()
