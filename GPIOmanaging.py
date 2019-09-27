import RPi.GPIO as GPIO
from ButtonController import Button_controller as bc
import UtilityView as uv
import Pause
import fileManaging as fm
import registrazione
import os
import subprocess
from time import sleep
#os.chdir("/home/pi/Desktop/Main/")
import StaticParameter as SP
from ListAssociationView import ListAssociationView as lav
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

from pyudev import Context, Monitor
from pyudev.monitor import MonitorObserver
context = Context()
monitor = Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')



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


pulsante_levetta_registrazione = 17           #   grigio

# setup pin button
for i in range (5):
    GPIO.setup(pulsanti[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(pulsante_pause, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pulsante_levetta_registrazione, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(quit_device_button, GPIO.IN)

green_led=20
red_led=16

# setup led 
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)
# accendo il led verde all'avvio
GPIO.output(green_led, GPIO.HIGH)
GPIO.output(red_led, GPIO.LOW)


levetta_registrazione_attivata=False


frequency = 20 #[Hz]
green_led_PWM = GPIO.PWM(green_led, frequency)
red_led_PWM = GPIO.PWM(red_led, frequency)


number_of_called = 0


def auto_import(device):

    # number of called rimuove il problema della doppia chiamata
    global number_of_called
    number_of_called += 1

    if device.action == "add" and number_of_called == 1:
        lav.auto_import_list()

        # accensione contemporanea del led rosso e verde
        # start(duty_cycle) accetta come paramentro un valore da 0 a 100
        # che rappresenta il valore del DC
        # con questo for vorrei avere una trnsizione dal rosso al verde ù
        # (passando per i colori intermediari) della durata totale di 1 secondo (100*0.1[s])

        for duty_cicle_value in range(0, 100):
            green_led_PWM.start(duty_cicle_value)
            red_led_PWM.start(100-duty_cicle_value)
            sleep(0.01)

        green_led_PWM.stop()
        red_led_PWM.stop()
    else:
        number_of_called = 0


observer = MonitorObserver(monitor, callback=auto_import, name='monitor-observer')
observer.start()


def falling(channel, id_button):

    registrazione.stop()
    
    recoded_name_file = "audio_pulsante_"+str(id_button)+".wav"
    fm.bind(recoded_name_file, id_button)
    
    GPIO.remove_event_detect(channel)
    GPIO.add_event_detect(channel, GPIO.RISING, callback=lambda x: rising(channel, id_button), bouncetime=50)


def rising(channel, id_button):
    global bc
    if levetta_registrazione_attivata:
        GPIO.remove_event_detect(channel)
        GPIO.add_event_detect(channel, GPIO.FALLING,
                              callback=lambda x: falling(channel, id_button),
                              bouncetime=50)

        recoded_name_file="audio_pulsante_"+str(id_button)+".wav"
        registrazione.start(os.path.join(pathfileaudio, recoded_name_file))

    else:
        bc_object.manage_pulsante_riproduzione(id_button)


def levetta_registrazione(channel):

    global levetta_registrazione_attivata
    levetta_registrazione_attivata = not levetta_registrazione_attivata

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
    choice = uv.multi_choice_view(SP.message_label_quit_device,
                                SP.message_text_button_confirm,
                                SP.message_text_button_abort)
    if choice:
        subprocess.Popen(['shutdown', '-h', 'now'])
    else:
        return


def interrupt():
    for i in range(5):
        GPIO.add_event_detect(pulsanti[i], GPIO.RISING,
                              callback=lambda x,  button=i+1, channel=pulsanti[i]: rising(channel, button),
                              bouncetime=50)

    GPIO.add_event_detect(pulsante_levetta_registrazione, GPIO.RISING,
                          callback=levetta_registrazione,
                          bouncetime=300)

    GPIO.add_event_detect(pulsante_pause, GPIO.RISING,
                          callback=my_play_and_pause,
                          bouncetime=300)

    GPIO.add_event_detect(quit_device_button, GPIO.FALLING,
                          callback=turn_off_device,
                          bouncetime=3000)


bc_object = bc(Pause.Pause())
interrupt()
