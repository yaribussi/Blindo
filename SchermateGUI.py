from tkinter import *
from RecordView import RecordView as rv
from AssociateView import AssociateView as av
from ImportExportView import ImportExportView as iev
from ListAssociationView import ListAssociationView as lav
import UtilityView as uv
import Reproduction


'''##############################################################################################################'''
'''###########                                  ATTENZIONE                             ##########################'''
'''###########    cambiare il path per poter utilizzare il programma sul proprio PC    ##########################'''
'''##############################################################################################################'''

path_punto_accesso_chiavette = r"C:\Users\Diego Berardi\Desktop\file audio blindo\punto di accesso chiavette"
path_che_simula_la_memoria_interna_del_raspberry = r"C:\Users\Diego Berardi\Desktop\file audio blindo\simula memoria interna"


'''##############################################################################################################'''
'''
######                            ATTENZIONE                                              ###########
######              ABILITARE  PER UTILIZZARE IL SW SUL RASPBERRY            ###########

import GPIOmanaging
import registrazione as Reg
path_punto_accesso_chiavette = "/media/pi"
path_che_simula_la_memoria_interna_del_raspberry = "/home/pi/Documents/fileAudio"
os.chdir("/home/pi/Desktop/Main/")
#subprocess.Popen(['unclutter','-idle','0'])   #comando per rimuovere il cursore
##########################################################################################
'''

'''#############                       VARIABILI GLOBALI              ###########################'''
asnwer=False

recording=False

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
#active_background_color = "#B4D4E4"
active_background_color="#C8D7DC"
root_background_color = "#708090"
font_color = "#E0E0E0"

exit_text= "Torna al menu principale"

#  numero di pulsanti collegati
number_of_phisical_button=6

# nome di default del file registrato
name_recoded_file= "/reg.wav"


class SchermateGUI:

    # schermata del MENUPRINCIPALE
    def menu_principale():

        root = Tk()
        root.config(bg=root_background_color)
        root.attributes('-fullscreen', True)
        frame = Frame(root)

        # REGISTRA
        pulsante_registra= Button(frame,
                                  text="Registra",
                                  bg=button_background_color,
                                  command=lambda: rv.registra(path_che_simula_la_memoria_interna_del_raspberry),
                                  font=font_piccolo,
                                  fg=font_color,
                                  relief="ridge",
                                  bd=4,
                                  activebackground=active_background_color)
        pulsante_registra.grid(row=0, column=0)
        pulsante_registra.config(height=6, width=24)

        # IMPORTA/ESPORTA
        pulsante_importa_esporta = Button(frame,
                                          text="Importa/Esporta ",
                                          bg=button_background_color,
                                          command=lambda: iev.import_export(path_punto_accesso_chiavette, path_che_simula_la_memoria_interna_del_raspberry),
                                          font=font_piccolo,
                                          fg=font_color,
                                          relief="ridge",
                                          bd=4,
                                          activebackground=active_background_color)
        pulsante_importa_esporta.grid(row=0, column=1)
        pulsante_importa_esporta.config(height=6, width=24)

        # ASSOCIA
        pulsante_associa = Button(frame,
                                  text="Associa",
                                  bg=button_background_color,
                                  command=lambda: av.schermata_pulsanti(root, number_of_phisical_button),
                                  font=font_piccolo,
                                  fg=font_color,
                                  relief="ridge",
                                  bd=4,
                                  activebackground=active_background_color)
        pulsante_associa.grid(row=1, column=0)
        pulsante_associa.config(height=6, width=24)

        # LISTA ASSOCIAZIONI
        pulsante_associazioni = Button(frame,
                                       text="Lista Associazioni",
                                       bg=button_background_color,
                                       command=lav.schermata_associazioni,
                                       font=font_piccolo,
                                       fg=font_color,
                                       relief="ridge",
                                       bd=4,
                                       activebackground=active_background_color)
        pulsante_associazioni.grid(row=1, column=1)
        pulsante_associazioni.config(height=6, width=24)

        #  metodo che importa il menu a cascata nel menu principale
        SchermateGUI.menu_cascata_con_exit(root)

        frame.pack()
        root.mainloop()  # funzione che continua a tenere aperto la finetra principale

    # schermata di impostazioni accessibile dal menu cascata
    def impostazioni():
        current_volume = Reproduction.Reproduction.give_volume()

        # funzione che aggiorna il valore del volume cmostrato all'utente
        def change_volume_on_display():
            current_vol_label.configure(text=Reproduction.Reproduction.give_volume())

        # funzione che aumenta il volume e aggiorna il valore nel label
        def increse_and_change():
            Reproduction.Reproduction.increse_vol()
            change_volume_on_display()

        # funzione che abbassa il volume e aggiorna il valore nel label
        def decrese_and_change():
            Reproduction.Reproduction.decrese_vol()
            change_volume_on_display()

        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg=root_background_color)
        frame = Frame(root)
        frame.config(bg=root_background_color)
        frame.pack()
        button_color= "orange"

        # visualizza del valore del volume in un intervallo 10-100
        current_vol_label = Label(
                                frame,
                                text=current_volume,
                                font=font_grande,
                                width=4,
                                bg=root_background_color,
                                fg="white"
                                )
        current_vol_label.grid(row=1, column=1)

        # pulsante per diminuire il volume
        decrese_vol_button = Button(
                              frame,
                              text="-",
                              font=font_grande,
                              fg=font_color,
                              command=decrese_and_change,
                              bg=button_background_color,
                              relief="ridge",
                              bd=10,
                              activebackground=active_background_color)
        decrese_vol_button.grid(row=1)
        decrese_vol_button.config(height=1, width=2)

        # pulsante per aumentare il volume
        increse_vol_button = Button(
                              frame,
                              text="+",
                              font=font_grande,
                              fg=font_color,
                              command=increse_and_change,
                              bg=button_background_color,
                              activebackground=active_background_color,
                              relief="ridge",
                              bd=10)
        increse_vol_button.grid(row=1, column=2)
        increse_vol_button.config(height=1, width=2)

        scritta_vol = Label(frame,
                            text="Volume",
                            heigh=2,
                            font=font_medio,
                            fg="white",
                            bg=root_background_color)

        scritta_vol.grid(row=0, column=1)
        uv.exit_button_with_text(root, exit_text)
        root.mainloop()

    # funzione che permette di avere un menu a cascata con la funzione di uscire dal main program ##########
    def menu_cascata_con_exit(master):
        # serve a rimuovere la riga tratteggiata che permette di spostare le ozioni col mouse
        master.option_add('*tearOff', FALSE)
        menu=Menu(master,
                  font=font_medio,
                  fg="white",
                  bg=root_background_color,)
        master.config(menu=menu)
        # crea il menu a cascata
        subMenu = Menu(menu,
                       font=font_medio,
                       fg="white",
                       bg=root_background_color,)
        menu.add_cascade(label="Impostazioni", font=font_medio, menu=subMenu, )  # menu a cascata
        # riga di separazione
        subMenu.add_separator()
        subMenu.add_command(label="Volume     ", font=font_medio, command=SchermateGUI.impostazioni)
        subMenu.add_separator()
        subMenu.add_command(label="Spegni    ", font=font_medio, command=lambda: uv.spegni_con_conferma())

        subMenu.add_separator()
        subMenu.add_command(label="Chiudi programma", font=font_medio, command=master.destroy)
        subMenu.add_separator()

    #  funzione per avere un pulsante di ritorno al menu ptincipale
    def pulsante_torna_menu_principale(root):

        pulstante_uscita = Button(root,
                                  text="Torna al menu principale",
                                  command=lambda: SchermateGUI.menu_principale(),
                                  bg=button_background_color,
                                  font=font_piccolo,
                                  bd=20,
                                  activebackground=active_background_color)
        pulstante_uscita.config(height=2, width=25)
        pulstante_uscita.pack(side=BOTTOM, fill=BOTH)

        root.destroy()



#SchermateGUI.menu_principale()
