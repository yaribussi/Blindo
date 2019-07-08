import Recorder
import pyaudio
from Recorder import *
import time

#istanzio l'oggetto registratore
rec = Recorder()

#funzioni per la registrazione con parametro il nome del file da registrare
#nel momento in cui inizia la registrazione si richiede all'utente di inserire


def start(name):
    rec=Recorder()
    recFile = rec.open(name, 'wb')
    recFile.start_recording()
    return recFile
    

def stop(recFile):
    recFile.stop_recording()
    recFile.close()
 

#name = 'AudiodiProva'
#stopObj = start(name, rec)
#time.sleep(10.0)
#stop(stopObj)

