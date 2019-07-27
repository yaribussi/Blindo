import pickle as pk
import pygame.mixer as PM
import RPi.GPIO as GPIO
from ButtonController import Button_controller as bc
import ButtonController
import SchermateGUI
import Pause
import subprocess


import os
import pyaudio
import wave

os.chdir("/home/pi/Desktop/Main/")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

path= "/home/pi/Documents/fileAudio"
pathfileaudio="/home/pi/Documents/fileAudio"


'''
pulsante_1 = 5            #   giallo
pulsante_2 = 24           #   viola
pulsante_3 = 21           #   blu
pulsante_4 = 26           #   verde

pulsante_5 = 4            #   nero
pulsante_6 = 17           #   grigio
'''

pulsanti = [5, 24, 21, 26, 4, 17]
pulsante_pause = 22       #   bianco
quit_device_button = 3


def my_function_who_calls_controller(idButton):
    global bc
    #GPIO.remove_event_detect(pulsanti[idButton])
    bc_object.manage_pulsante_riproduzione(idButton)
    

def my_play_and_pause(pulsante):
    global bc
    bc_object.manage_pulsante_play_pause()


def turn_off_device(pulsante):
    SchermateGUI.SchermateGUI.spegni_con_conferma()


def interrupt():
    for i in range(6):
        GPIO.add_event_detect(pulsanti[i], GPIO.RISING, callback=lambda x,  button=i+1: my_function_who_calls_controller(button), bouncetime=500)

    GPIO.add_event_detect(pulsante_pause, GPIO.RISING, callback=my_play_and_pause, bouncetime=500)

    GPIO.add_event_detect(quit_device_button, GPIO.FALLING, callback=turn_off_device, bouncetime=500)


for i in range (6):
    GPIO.setup(pulsanti[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(pulsante_pause, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(quit_device_button, GPIO.IN)

bc_object = bc(Pause.Pause())
interrupt()