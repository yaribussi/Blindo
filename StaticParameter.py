'''
ATTENZIONE ABILITARE LE LINEE  [5 6 7] PER UTILIZZO SU PC
'''

#path_punto_accesso_chiavette = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudiofromChiavetta"
#path_che_simula_la_memoria_interna_del_raspberry = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudioRSPmemory"
#path_liste =r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\Liste"

'''
ATTENZIONE ABILITARE LE LINEE  [14 15 16 17 18] PER UTILIZZO SU RASPBERRY

ABILITARE NEL FILE "RECORD_VIEW" L'IMPORT ALLA RIGA 5 
'''
import GPIOmanaging
path_punto_accesso_chiavette = "/media/pi"
path_che_simula_la_memoria_interna_del_raspberry = "/home/pi/Documents/fileAudio"
path_liste ="/home/pi/Documents/Lists"
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
button_font_color = "black"
pop_up_colour_background="#505050"
root_font_color= "white"
black="black"

recode_view_button_color= "#C0392B"
import_export_button_color="#5499C7"
list_association_button_color="#27AE60"
setting_button_color="#554F9D"
utility_button_color="#DFB606"
archive_manager_button_color="#F7DC6F"

recode_view_root_color= "#D98880"
import_export_root_color="#85C1E9"
list_association_root_color="#58D68D"
setting_root_color="#775DC0"
utility_root_color="#E3CB63"
archive_manager_root_color="#F0B27A"

key_keyboard_color = "#5499C7"
root_keyboard_color = "#B989C4"

cascade_main_menu= "#554F9D"
cascade_list_association_menu="#554F9F"

import_button_color=import_export_button_color
export_button_color= import_export_button_color

import_root_color=import_export_root_color
export_root_color= import_export_root_color


green="#69F505"
red="#D55858"

exit_button_color="#BDC3C7"





currentTheme = 1  #0 for default theme - 1 for coloured theme
theme={

        "confirm_button_background":    [button_background_color, green],
        "delete_button_background":     [button_background_color, red],

        "exit_button_with_text":        [button_background_color, exit_button_color],
        "import_button_background":        [button_background_color, import_button_color],
        "export_button_background":        [button_background_color, export_button_color],

        "import_root_background": [root_background_color, import_root_color],
        "export_root_background": [root_background_color, export_root_color],

        "key_button_background":        [button_background_color, key_keyboard_color],
        "root_keyboard":                [root_background_color, root_keyboard_color],

        "usb_key_button":[button_background_color, key_keyboard_color],

        "setting_main_menu": [root_background_color, cascade_main_menu],

        "root_setting_view": [root_background_color, setting_root_color],
        "frame_setting_view": [root_background_color, setting_root_color],
        "label_setting_view": [root_background_color, setting_root_color],
        "button_setting_view": [button_background_color, setting_button_color],

        "root_list_association_view": [root_background_color, list_association_root_color],
        "frame_list_association_view":[root_background_color, list_association_root_color],
        "label_list_association_view":[root_background_color, list_association_root_color],
        "button_list_association_view": [button_background_color, list_association_button_color],
        "listbox_list_association_view":[root_background_color, list_association_root_color],
        "menu_list_association_view":[root_background_color, list_association_button_color],

        "root_utility_view": [root_background_color, utility_root_color],
        "frame_utility_view":[root_background_color, utility_root_color],
        "label_utility_view":[root_background_color, utility_root_color],
        "button_utility_view": [button_background_color, utility_button_color],
        "listbox_utility_view": [root_background_color, utility_root_color],

        "root_import_export_view": [root_background_color, import_export_root_color],
        "frame_import_export_view": [root_background_color, import_export_root_color],
        "label_import_export_view": [root_background_color, import_export_root_color],
        "button_import_export_view": [button_background_color, import_export_button_color],

        "root_record_view": [root_background_color, recode_view_root_color],
        "frame_record_view": [root_background_color, recode_view_root_color],
        "label_record_view": [root_background_color, recode_view_root_color],
        "button_record_view": [button_background_color, recode_view_button_color],

        "root_archive_manager_view":[root_background_color, archive_manager_root_color],
        "frame_archive_manager_view": [root_background_color, archive_manager_root_color],
        "label_archive_manager_view": [root_background_color, archive_manager_root_color],
        "button_archive_manager_view": [button_background_color, archive_manager_button_color]
}
def standard_color_setting(guiObjectName):
    return theme[guiObjectName].__getitem__(currentTheme)

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
name_recoded_file= "reg.wav"

# abilita fullscreen con True, disabilita con False
full_screen_option=True

# messaggi interazione utente
message_label_quit_device="Vuoi spegnere il dispositivo?"
message_text_button_confirm="Conferma"
message_text_button_abort="Annulla"

# questo è il nome della cartella contenente le sottocartelle delle singole liste esportate
expor_folder_name="Liste"


# funzione che modifica la grandezza del bordi dei pulsanti
def set_bord_size(new_size):
    global bord_size
    bord_size = new_size


# funzione che modifica lo stile dei bordi dei pulsanti
def set_bord_style(choosed_style): # 0-5
    bord_styles_set = ["flat", "groove", "raised", "ridge", "solid", "sunken"]
    global bord_style
    bord_style = bord_styles_set[choosed_style]

