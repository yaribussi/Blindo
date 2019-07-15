#Ciao ragazzi, sono Samu

import pickle as pk
import pygame.mixer as PM
import RPi.GPIO as GPIO
#import time
import subprocess
import Pause
import os

import pyaudio
import wave


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

path= "/home/pi/Documents/fileAudio"
pathfileaudio="/home/pi/Documents/fileAudio"

#nomeFile='/home/pi/Desktop/Main/lista'

pulsante_1 = 5     #giallo
pulsante_2 = 24    #viola
pulsante_3 = 21    # blu
pulsante_4 = 26     #verde 

pulsante_5 = 4    #nero
pulsante_6 = 17   #grigio
pulsante_pause = 22 #bianco    

GPIO.setup(pulsante_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_pause, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

############    funzione che riproduce un file audio dato uno specifico path        ##########

def playSingleFile(pathfileaudio):
        
        #PM.pre_init(44100,-16,1,2024)
        PM.init()
        PM.music.load(pathfileaudio)
        PM.music.play()






###########  funzione che carica la "lista finale" e cerca al suo interno se esiste
###########   un oggetto fileAudio con lo stesso idButton del pulsante che è stato premuto
def searchAndPlayFile(id):
    #print(os.getcwd())
    try:
        #with open("lista finale1", 'rb') as io:
        with open("lista finale1", 'rb') as io:
              my_objects = pk.load(io)
    #          print(os.getcwd())

              for audio in my_objects:
                  #print(audio.name + " " + str(audio.idButton)+ "/n")
                  if int(audio.idButton) == id:
                      playSingleFile(path + "/" + audio.name)
                      
    except (FileNotFoundError, IOError) as e:
            print(e)

##########          insieme di funzioni per riprodurre il fileAudio             ############à
#########           DEVONO avere come parametro il pulsante a cui sono associate

PAUSE=Pause.Pause()

def playNpause(pulsante):
    global PAUSE
    PAUSE.toggle()
    
    
def myFunction1(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        searchAndPlayFile(1)
    
    
def myFunction2(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        searchAndPlayFile(2)
    
def myFunction3(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        searchAndPlayFile(3)

    
def myFunction4(pulsante):
        global PAUSE
        PAUSE = Pause.Pause()
        searchAndPlayFile(4)
        
def myFunction5(pulsante):
        #'''
        global PAUSE
        PAUSE = Pause.Pause()
        searchAndPlayFile(5)
        #'''
        #subprocess.Popen(['tvservice', '--off'])
    
def myFunction6(pulsante):
        #subprocess.Popen([['tvservice', '--preferred']])
        #'''
        global PAUSE
        PAUSE = Pause.Pause()
        searchAndPlayFile(6)
        #'''
##################################################################################################

#######         funzione che aspetta il cambio di evento (from LOW to HIGH)
#######         di tutti i pulsanti collegati alla sccheda
#######         le funzioni richamate da "callback" devono accettare lo stesso parametro del evento che le chiama
#######         infatti tutte le "myFunction"  accettano come parametro il PIN del pulsante
#######         il parametro bounctime fa lo stesso effetto della funzione time.sleep(0.5)
def interupt():
    #PM.init()
    GPIO.add_event_detect(pulsante_1, GPIO.RISING,callback=myFunction1,bouncetime=500)
    GPIO.add_event_detect(pulsante_2, GPIO.RISING,callback=myFunction2,bouncetime=500)
    GPIO.add_event_detect(pulsante_3, GPIO.RISING,callback=myFunction3,bouncetime=500)
    GPIO.add_event_detect(pulsante_4, GPIO.RISING,callback=myFunction4,bouncetime=500)
    GPIO.add_event_detect(pulsante_5, GPIO.RISING,callback=myFunction5,bouncetime=500)
    GPIO.add_event_detect(pulsante_6, GPIO.RISING,callback=myFunction6,bouncetime=500)
    
    GPIO.add_event_detect(pulsante_pause, GPIO.RISING,callback=playNpause,bouncetime=500)
    

interupt()
