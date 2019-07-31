import pickle as pk
import os
from fileAudio import FileAudio
import shutil


# nome del file sul quale verranno salvati
# (e dal quale verranno caricati) i fileAudio e i loro parametri#
name_file = 'Lista di default '
path_liste =r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\Liste"


def change_list(list_name):
    global name_file
    name_file = list_name

# funzione che ritorna la lista delle stringhe dei fileAudio presenti in "lista finale" riordinata in base al numero del pulsante
def give_sorted_list():
    final_path = os.path.join(path_liste, name_file)
    list=[]

    if os.path.isfile(final_path):
        try:
           with open(final_path, 'rb') as io:
                my_objects = pk.load(io)
                my_objects.sort(key=lambda x: int(str(x.idButton)))

                for audio in my_objects:
                    if str(audio.name) != "DEFAULT":
                        formattedNumber = '{:5s}'.format(str(audio.idButton))
                        list.append("Pulsante "+formattedNumber+" ------->  " +str(audio.name)+ "\n")

                

        except (FileNotFoundError, IOError) as e:
            print(e)
    return list


# funzione che elimina da lista finale i fileAudio che vengono eliminati tramite la GUI
def delete_element_from_list(nomeFileDaRimuovere):
    final_path = os.path.join(path_liste, name_file)

    if os.path.isfile(final_path):
        try:
            with open(final_path, 'rb') as io:
                my_objects = pk.load(io)

                for audio in my_objects:
                    if audio.name == nomeFileDaRimuovere:
                        my_objects.remove(audio)

            save_file_audio(my_objects)

        except (FileNotFoundError, IOError) as e:
            print(e)


# binding between the button and the name of the file audio
def bind(audio_name, id):
    # default element needed to pass through the list of file audio if it has only one element
    default = FileAudio('DEFAULT', 0)
    file_audio = FileAudio(audio_name,id)

    final_path = os.path.join(path_liste, name_file)

    my_objects = [default]
    if os.path.isfile(final_path):
        try:
            final_path = os.path.join(path_liste, name_file)
            with open(final_path, 'rb') as io:
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


def load_list():
    try:
        final_path = os.path.join(path_liste, name_file)
        with open(final_path, 'rb') as io:
            my_objects = pk.load(io)
    except (FileNotFoundError, IOError) as e:
        print(e)
    return my_objects


# funzione per salvare la lista di fileAudio come un unico oggetto con nome "lista finale" #####
def save_file_audio(my_objects):
    final_path=os.path.join(path_liste, name_file)
    with open(final_path, 'wb') as output:
        pk.dump(my_objects, output, -1)


# funzione che utilizza la funzione di sitema "shutil.copy" per copiare i file da un path ad un altro
def copy_file_from_path_to_another(initialPath, endingPath):
    shutil.copy(initialPath, endingPath)


# funzione che serve a togliere tutti gli zero non significativi e arrotonda il numero trovato########
def round_to_1(x):
    return




