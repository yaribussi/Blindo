import pickle as pk
import os
from fileAudio import FileAudio
import pygame.mixer as PM
from math import log10, floor
import shutil
import re


################          nome del file sul quale verranno salvati
################          (e dal quale verranno caricati) i fileAudio e i loro parametri#
nameFile = 'lista finale'


######## funzione che ritorna la lista dei fileAudio presenti in "lista finale" riordinata in base al numero del pulsante
def give_sorted_list():

    list=[]

    if os.path.isfile("./" + nameFile):
        try:
            with open(nameFile, 'rb') as io:
                my_objects = pk.load(io)
                my_objects.sort(key=lambda x: int(str(x.idButton)))


                for audio in my_objects:
                    if str(audio.name) != "DEFAULT":
                        formattedNumber = '{:5s}'.format(audio.idButton)
                        list.append("Pulsante "+formattedNumber+" ------->  " +str(audio.name)+ "\n")

                

        except (FileNotFoundError, IOError) as e:
            print(e)
    return list

############  funzione che elimina da lista finale i fileAudio che vengono eliminati tramite la GUI
def delete_element_from_list(nomeFileDaRimuovere):

     if os.path.isfile("./" + nameFile):
        try:
            with open(nameFile, 'rb') as io:
                my_objects = pk.load(io)

                for audio in my_objects:
                    if audio.name == nomeFileDaRimuovere:
                        my_objects.remove(audio)

            save_file_audio(my_objects)

        except (FileNotFoundError, IOError) as e:
            print(e)



######    funzione che carica il file conenente la lista di oggetti,
######    inserisce un nuovo elemento alla lista di oggetti file audio, i cui attributi sono:
######    "nome file audio, id bottone",
######     e la salva in un file che sovrascrive il precedente
def bind(audio_name, id):
    #devo farlo perchè se non ci sono almeno due elementi nella lista di oggetti, questa non è iterabile, quindi non posso effettuare il for audio in my_objects
    default = FileAudio('DEFAULT', 0)
    file_audio = FileAudio(audio_name, id)

    my_objects = [default]
    if os.path.isfile("./" + nameFile):
        try:
            with open(nameFile, 'rb') as io:
                my_objects = pk.load(io)

                for audio in my_objects:
                    if audio.name == audio_name or audio.idButton == id:
                        my_objects.remove(audio)
                my_objects.append(file_audio)


                save_file_audio(my_objects)

        except (FileNotFoundError, IOError) as e:
            print(e)
    else:
        my_objects.append(file_audio)
        save_file_audio(my_objects)


#### funzione per salvare la lista di fileAudio come un unico oggetto con nome "lista finale" #####
def save_file_audio(my_objects):
    with open(nameFile, 'wb') as output:
        pk.dump(my_objects, output, -1)


##### funzione che utilizza la funzione di sitema "shutil.copy" per copiare i file da un path ad un altro
def copy_file_from_path_to_another(initialPath, endingPath):
    shutil.copy(initialPath, endingPath)

##### funzione che serve a togliere tutti gli zero non significativi e arrotonda il numero trovato########
def round_to_1(x):
    return round(x, -int(floor(log10(abs(x)))))

######   a seguire 2 funzioni per aumentare e diminuire il volume
######  ogni volta che vengono richiamate cambiano il valore del volume del 10 per cento
def increse_vol():

    PM.init()
    current_volume=PM.music.get_volume()
    PM.music.set_volume(current_volume+0.1)

def decrese_vol():

    PM.init()
    current_volume = PM.music.get_volume()
    PM.music.set_volume(current_volume-0.1)

#fumzione che restituisce il valore del volume in un range da 10 a 100
def give_volume():

    PM.init()
    volume=PM.music.get_volume()
    volume=round_to_1(volume)

    volume = volume * 100

    if volume < 20:
        volume = 10.0
    elif volume<10 :
        volume=0
    return str(volume)[:3]


