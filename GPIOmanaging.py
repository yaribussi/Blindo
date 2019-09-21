import RPi.GPIO as GPIO
from ButtonController import Button_controller as bc
import UtilityView as uv
import Pause
import fileManaging as fm
import registrazione
import os
import subprocess
#os.chdir("/home/pi/Desktop/Main/")
import StaticParameter as SP
from ListAssociationView import ListAssociationView as lav
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

from pyudev import Contex, Monitor
from pyudev.monitor import MonitorObserver
context=Context()
monitor=Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

def auto_import(device):
    if (device.action==add):
        lav.auto_import_list()

observer=MonitorObserver(monitor,callback=auto_import,name='monitor-observer')


path = "/home/pi/Documents/fileAudio"
pathfileaudio = "/home/pi/Documents/fileAudio"


'''
pulsante_1 = 5            #   giallo
pulsante_2 = 24           #   viola
pulsante_3 = 21           #   blu
pulsante_4 = 26           #   verde

pulsante_5 = 4            #   nero
pulsante_6 = 17           #   grigio
pulsante_pause = 22       #   bianco
'''

pulsanti = [5, 24, 21, 26, 4]#, 17]
pulsante_pause = 22       
quit_device_button = 3

green_led=20
red_led=16

pulsante_levetta_registrazione = 17           #   grigio

# setup pin button
for i in range (5):
    GPIO.setup(pulsanti[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(pulsante_pause, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_levetta_registrazione, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(quit_device_button, GPIO.IN)

# setup led 
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)


levetta_registrazione_attivata=False

# accendo il led verde all'avvio
GPIO.output(green_led, GPIO.HIGH)
GPIO.output(red_led, GPIO.LOW)


def falling(channel, id_button):

    registrazione.stop()
    
    recoded_name_file = "audio_pulsante_"+str(id_button)+".wav"
    fm.bind(recoded_name_file, id_button)
    
    GPIO.remove_event_detect(channel)
    GPIO.add_event_detect(channel, GPIO.RISING, callback=lambda x: rising(channel, id_button), bouncetime=100)


def rising(channel, id_button):
    global bc
    if levetta_registrazione_attivata:
        GPIO.remove_event_detect(channel)
        GPIO.add_event_detect(channel, GPIO.FALLING, callback=lambda x: falling(channel, id_button), bouncetime=100)

        recoded_name_file="audio_pulsante_"+str(id_button)+".wav"
        registrazione.start(os.path.join(pathfileaudio, recoded_name_file))

    else:
        bc_object.manage_pulsante_riproduzione(id_button)


def levetta_registrazione(channel):

    global levetta_registrazione_attivata
    levetta_registrazione_attivata = not levetta_registrazione_attivata
    print(levetta_registrazione_attivata)
    
    if levetta_registrazione_attivata:
        GPIO.output(red_led, GPIO.HIGH)
        GPIO.output(green_led, GPIO.LOW)

    else:
        GPIO.output(green_led, GPIO.HIGH)
        GPIO.output(red_led, GPIO.LOW)
    

def my_play_and_pause(pulsante):
    global bc
    bc_object.manage_pulsante_play_pause()


def turn_off_device(pulsante):
    choice=uv.multi_choice_view(SP.message_label_quit_device,
                                SP.message_text_button_confirm,
                                SP.message_text_button_abort)
    if choice:
        subprocess.Popen(['shutdown', '-h', 'now'])
    else:
        return



def interrupt():
    for i in range(5):
        GPIO.add_event_detect(pulsanti[i], GPIO.RISING, callback=lambda x,  button=i+1, channel=pulsanti[i]: rising(channel, button), bouncetime=300)

    GPIO.add_event_detect(pulsante_levetta_registrazione, GPIO.RISING, callback=levetta_registrazione, bouncetime=300)

    GPIO.add_event_detect(pulsante_pause, GPIO.RISING, callback=my_play_and_pause, bouncetime=300)

    GPIO.add_event_detect(quit_device_button, GPIO.FALLING, callback=turn_off_device, bouncetime=3000)


bc_object = bc(Pause.Pause())
interrupt()
