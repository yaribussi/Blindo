import Recorder
import pyaudio
from Recorder import *


#funzioni per la registrazione con parametro il nome del file da registrare
#nel momento in cui inizia la registrazione si richiede all'utente di inserire


def start(name):
    global rec_file
    rec=Recorder()
    rec_file = rec.open(name, 'wb')
    rec_file.start_recording()
   

def stop():
    global rec_file
    rec_file.stop_recording()
    rec_file.close()
 



