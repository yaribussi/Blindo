import pickle as pk
import os
from fileAudio import FileAudio
import pygame.mixer as PM
from math import log10, floor
import shutil
import re


################          nome del file sul quale verranno salvati
################          (e dal quale verranno caricati) i fileAudio e i loro parametri#
nameFile = 'lista finale1'
#nameFile='/home/pi/Desktop/Main/lista'
#nameFile ="/home/pi/lista finale"

######## funzione che ritorna la lista dei fileAudio presenti in "lista finale" riordinata in base al numero del pulsante
def giveSortedList():

    list=[]
    #if os.path.isfile(nameFile):
    #os.chdir("/home/pi/Desktop/Main/")
    #print(os.getcwd())
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
def deleteElementFromList(nomeFileDaRimuovere):

    #os.chdir("/home/pi/Desktop/Main/")
    if os.path.isfile("./" + nameFile):
        try:
            with open(nameFile, 'rb') as io:
                my_objects = pk.load(io)

                for audio in my_objects:
                    if audio.name == nomeFileDaRimuovere:
                        my_objects.remove(audio)

            saveFileAudio(my_objects)

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

    #os.chdir("/home/pi/Desktop/Main/")

    my_objects = [default]
    if os.path.isfile("./" + nameFile):
        try:
            with open(nameFile, 'rb') as io:
                my_objects = pk.load(io)

                for audio in my_objects:
                    if audio.name == audio_name or audio.idButton == id:
                        my_objects.remove(audio)
                my_objects.append(file_audio)


                saveFileAudio(my_objects)

        except (FileNotFoundError, IOError) as e:
            print(e)
    else:
        my_objects.append(file_audio)
        saveFileAudio(my_objects)


#### funzione per salvare la lista di fileAudio come un unico oggetto con nome "lista finale" #####
def saveFileAudio(my_objects):
    #os.chdir("/home/pi/Desktop/Main/")
    with open(nameFile, 'wb') as output:
        pk.dump(my_objects, output, -1)


##### funzione che utilizza la funzione di sitema "shutil.copy" per copiare i file da un path ad un altro
def copyFileFromPathToAnother(initialPath,endingPath):
    shutil.copy(initialPath, endingPath)

##### funzione che serve a togliere tutti gli zero non significativi e arrotonda il numero trovato########
def round_to_1(x):
    return round(x, -int(floor(log10(abs(x)))))

######   a seguire 2 funzioni per aumentare e diminuire il volume
######  ogni volta che vengono richiamate cambiano il valore del volume del 10 per cento
def increseVol():

    PM.init()
    currentVolume=PM.music.get_volume()
    PM.music.set_volume(currentVolume+0.1)

def decreseVol():

    PM.init()
    currentVolume = PM.music.get_volume()
    PM.music.set_volume(currentVolume-0.1)

#fumzione che restituisce il valore del volume in un range da 10 a 100
def giveVolume():

    PM.init()
    volume=PM.music.get_volume()
    volume=round_to_1(volume)

    volume = volume * 100

    if volume < 20:
        volume = 10.0
    elif volume<10 :
        volume=0
    return str(volume)[:3]


#funzione di prova che riempie una lista di oggetti e la salva in un file
'''
def fillList():
     try:
         with open(nameFile, 'wb') as io:
             my_objects = []
             for i in range(0, 5):
                 nome = input("inserire il nome del file")
                 id = input("inserire l'id del bottone")
                 file_audio = FileAudio(nome, id)
                 my_objects.append(file_audio)
             pk.dump(my_objects, io, -1)
     except (FileNotFoundError, IOError) as e:
         print(e)
'''
