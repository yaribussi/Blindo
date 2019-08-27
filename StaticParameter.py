'''
ATTENZIONE ABILITARE LE LINEE  [5 6 7] PER UTILIZZO SU PC
'''

path_punto_accesso_chiavette = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudiofromChiavetta"
path_che_simula_la_memoria_interna_del_raspberry = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudioRSPmemory"
path_liste =r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\Liste"

'''
ATTENZIONE ABILITARE LE LINEE  [14 15 16 17 18] PER UTILIZZO SU RASPBERRY

ABILITARE NEL FILE "RECORD_VIEW" L'IMPORT ALLA RIGA 5 
'''
#import GPIOmanaging
#path_punto_accesso_chiavette = "/media/pi"
#path_che_simula_la_memoria_interna_del_raspberry = "/home/pi/Documents/fileAudio"
#path_liste ="/home/pi/Documents/Lists"
#os.chdir("/home/pi/Desktop/Main/")
#subprocess.Popen(['unclutter','-idle','0'])   #comando per rimuovere il cursore


import os
# VARIABILI GLOBALI


# formati audio disponibili
formats_audio= [".mp3", ".wav", ".wma", ".ogg", ".flac"]

# caratteristiche font
font_keyboard_key = 13
font_size_piccolo = 20
font_size_medio   = 33
font_size_grande  = 80
font_stile = "Helvetica"
keyboard_key_font= (font_stile, font_keyboard_key)
font_piccolo = (font_stile, font_size_piccolo)
font_medio = (font_stile, font_size_medio)
font_grande = (font_stile, font_size_grande)

# colori GUI
button_background_color = "#404040"
active_background_color="#C8D7DC"
root_background_color = "#708090"
button_font_color = "#E0E0E0"
pop_up_colour_background="#505050"
root_font_color= "white"
black="black"

# testo visualizzato nel pulsante che torna al menu principale
exit_text= "Torna al menu principale"

# stile bordi pulsanti
bord_styles_set = ["flat", "groove", "raised", "ridge", "solid", "sunken"]

# grandezza bordi pulsanti
bord_size = 4

# scelta del bordo "RAISED"
bord_style = bord_styles_set[2]

#  numero di pulsanti collegati
number_of_phisical_button=5

# nome di default del file registrato
name_recoded_file= "/reg.wav"


# funzione che modifica la grandezza del bordi dei pulsanti
def set_bord_size(new_size):
    global bord_size
    bord_size = new_size


# funzione che modifica lo stile dei bordi dei pulsanti
def set_bord_style(choosed_style): # 0-5
    bord_styles_set = ["flat", "groove", "raised", "ridge", "solid", "sunken"]
    global bord_style
    bord_style = bord_styles_set[choosed_style]

