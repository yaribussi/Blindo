import os

#path_punto_accesso_chiavette = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudiofromChiavetta"
#path_che_simula_la_memoria_interna_del_raspberry = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudioRSPmemory"
#path_liste =r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\Liste"

import GPIOmanaging
path_punto_accesso_chiavette = "/media/pi"
path_che_simula_la_memoria_interna_del_raspberry = "/home/pi/Documents/fileAudio"
path_liste ="/home/pi/Documents/Lists"
os.chdir("/home/pi/Desktop/Main/")

#subprocess.Popen(['unclutter','-idle','0'])   #comando per rimuovere il cursore



# VARIABILI GLOBALI

name_file = 'Lista di default'

# formati audio disponibili
formats_audio= [".mp3", ".wav", ".wma", ".ogg", ".flac"]

# caratteristiche font
font_size_piccolo = 20
font_size_medio   = 33
font_size_grande  = 80
font_stile = "Helvetica"
font_piccolo = (font_stile, font_size_piccolo)
font_medio = (font_stile, font_size_medio)
font_grande = (font_stile, font_size_grande)

button_background_color = "#404040"
active_background_color="#C8D7DC"
root_background_color = "#708090"
font_color = "#E0E0E0"
pop_up_colour_background="#505050" #"#A5ACAF"
white="white"
black="black"
exit_text= "Torna al menu principale"

#  numero di pulsanti collegati
number_of_phisical_button=5

# nome di default del file registrato
name_recoded_file= "/reg.wav"
