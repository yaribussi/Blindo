import Recorder
from Recorder import *


# istanzio l'oggetto registratore
rec = Recorder()

# funzioni per la registrazione con parametro il nome del file da registrare
# nel momento in cui inizia la registrazione si richiede all'utente di inserire

def start(name):
    rec = Recorder()
    rec_file = rec.open(name, 'wb')
    rec_file.start_recording()
    return rec_file
    

def stop(rec_file):
    rec_file.stop_recording()
    rec_file.close()
 



