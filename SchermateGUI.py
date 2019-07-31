from tkinter import *
import fileManaging as fm
from ListAssociationView import ListAssociationView as Lav
import GUIkeyboard as key
import os
from RecordView import RecordView as rv
from ImportExportView import ImportExportView as iev
import Reproduction

import UtilityView as uv


'''##############################################################################################################'''
'''###########                                  ATTENZIONE                             ##########################'''
'''###########    cambiare il path per poter utilizzare il programma sul proprio PC    ##########################'''
'''##############################################################################################################'''

path_punto_accesso_chiavette = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudiofromChiavetta"
path_che_simula_la_memoria_interna_del_raspberry = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudioRSPmemory"
path_liste =r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\Liste"

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
pop_up_colour_background="#A5ACAF"
exit_text= "Torna al menu principale"

#  numero di pulsanti collegati
number_of_phisical_button=5

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
                                  command=lambda:rv.registra(path_che_simula_la_memoria_interna_del_raspberry),
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
                                          command=lambda :iev.import_export(path_punto_accesso_chiavette,
                                                                            path_che_simula_la_memoria_interna_del_raspberry),
                                          font=font_piccolo,
                                          fg=font_color,
                                          relief="ridge",
                                          bd=4,
                                          activebackground=active_background_color)
        pulsante_importa_esporta.grid(row=0, column=1)
        pulsante_importa_esporta.config(height=6, width=24)

        # ASSOCIA
        pulsante_associa = Button(frame,
                                  text="Volume",
                                  bg=button_background_color,
                                  command=lambda:SchermateGUI.impostazioni(),
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
                                       command=SchermateGUI.schermata_associazioni,
                                       font=font_piccolo,
                                       fg=font_color,
                                       relief="ridge",
                                       bd=4,
                                       activebackground=active_background_color)
        pulsante_associazioni.grid(row=1, column=1)
        pulsante_associazioni.config(height=6, width=24)

        #  metodo che importa il menu a cascata nel menu principale
        SchermateGUI.menu_cascata_menu_principale(root)

        frame.pack()
        root.mainloop()  # funzione che continua a tenere aperto la finetra principale



    '''################################################################################################################'''
    '''###################                 funzioni che aprono le varie schermate                       ###############'''
    '''################################################################################################################'''

    # schermata che appare dopo aver cliccato sul pulsante REGISTRA nel MENUPRINCIPALE
    def registra():
        '''
        def update_clock(self):
            now = time.strftime("%H:%M:%S", time.gmtime())
            self.clock.configure(text=now)
            # call this function again in one second
            self.after(1000, self.update_clock)
        '''
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg=root_background_color)

        frame = Frame(root)
        frame.config(bg=root_background_color)
        frame.pack()

        label = Label(frame, text="Premi su Start per registrare",
                      bg=root_background_color,
                      width=90, height=3,
                      font=font_medio,
                      fg="white"
                      )
        label.pack()

        #    funzione che fa partire la registrazione
        def start_recoding(name_recoded_file):
            global recording
            global stopper
            global new_name
            recording=True

            label["text"] = "Registrazione in corso.....\nPremi il pulsante rosso per interrompere"

            final_path= path_che_simula_la_memoria_interna_del_raspberry + name_recoded_file
            Reg.start(final_path)

        #  funzione che ferma la registrazione e chiede all'utente il nome del file registrato
        def stop_recording():
            global stopper
            global recording

            if recording:
                
                Reg.stop() 
                label["text"] = "Registrazione effettuata con successo!"

                # funzione che richiama la tastiera e chiede all'utente il nome del file
                new_name=key.keyBoard()

                # path completo del nome del file appena registrato
                initial= path_che_simula_la_memoria_interna_del_raspberry + "/reg.wav"

                # path completo del file registrato rinominato
                final= path_che_simula_la_memoria_interna_del_raspberry + "/" + new_name + ".wav"
                # funzione che rinomina il file audio appena registrayo
                os.rename(initial, final)
                recording = False
                label["text"] = "Premi su Start per registrare"

            else:
                SchermateGUI.show_dialog_with_time("Attenzione\n"
                                                   "La registrazione non è ancora partita\n"
                                                   "Premi sul pulsante verde per avviarla",2)
                #tkinter.messagebox.showinfo("Attenzione","La registrazione non è ancora partita, premi sul pulsante verde",parent=root)

        pulsante_play = Button(frame,
                               text="Inizia a registrare",
                               bg=button_background_color,
                               command=lambda: start_recoding(name_recoded_file),
                               font=font_piccolo,
                               fg=font_color,
                               relief="ridge",
                               bd=20,
                               activebackground=active_background_color)
        pulsante_play.config(height=5, width=23)
        pulsante_play.pack(side=LEFT)

        pulsante_stop = Button(frame,
                               text="Interrompi la registrazione",
                               bg=button_background_color,
                               command=lambda: stop_recording(),
                               font=font_piccolo,
                               fg=font_color,
                               relief="ridge",
                               bd=20,
                               activebackground=active_background_color)
        pulsante_stop.config(height=5, width=23)
        pulsante_stop.pack(side=RIGHT)

        SchermateGUI.exit_button_with_text(root, exit_text)
               
        root.mainloop()

    # schermata che permette di importare ed esportare i file da/su chiavetta
    def esporta_importa():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg=root_background_color)

        frame=Frame(root)
        frame.config(bg=root_background_color)
        frame.pack()

        label = Label(frame, text="Scegli l'azione desiderata",
                      bg=root_background_color,
                      width=90, height=1,
                      font=font_medio,
                      fg="white"
                      )
        label.pack();

        pulsante_importa = Button(frame,
                                  text="Importa",
                                  bg=button_background_color,
                                  command=lambda:scegli_chiavetta_importa(),
                                  font=font_piccolo,
                                  fg=font_color,
                                  relief="ridge",
                                  bd=20,
                                  activebackground=active_background_color)
        pulsante_importa.pack(side=LEFT)
        pulsante_importa.config(height=5, width=22)

        pulsante_esporta = Button(frame,
                                  text="Esporta",
                                  bg=button_background_color,
                                  command=lambda:scegli_chiavetta_esporta(),
                                  font=font_piccolo,
                                  fg=font_color,
                                  relief="ridge",
                                  bd=20,
                                  activebackground=active_background_color)
        pulsante_esporta.pack(side=RIGHT)
        pulsante_esporta.config(height=5, width=22)

        #    funzione che richiama la sottoschermata dopo aver cliccato su "ESPORTA"
        def scegli_chiavetta_esporta():
            root = Tk()
            root.attributes('-fullscreen', True)
            root.config(bg=root_background_color)

            frame = Frame(root, bg=root_background_color)
            frame.pack()

            # passo alla funzione pi\media e quindi verranno visualizzate a schermo le chiavette disponibili
            dirs = os.listdir(path_punto_accesso_chiavette)

            label = Label(frame,
                          text="Selezionare la chiavetta su cui esportare i file audio",
                          bd=20,
                          bg=root_background_color,
                          font=font_piccolo,
                          fg="white")
            label.grid(row=1, column=0)
            label.config(width=50, height=4)

            # index necessario a ??
            index = 2
            # ciclo che stampa tante "chiavette" quante inserite nel device
            for cartella in dirs:
                path_chiavetta = os.path.join(path_punto_accesso_chiavette, cartella)
                pulsante = SchermateGUI.button_USB_key(frame, "esportare", cartella,
                                                       path_che_simula_la_memoria_interna_del_raspberry, path_chiavetta)
                pulsante.grid(row=index, column=0)
                index += 1

            SchermateGUI.exit_button_with_text(root, "Torna indietro")

            root.mainloop()

        #    funzione che richiama la sottoschermata dopo aver cliccato su "IMPORTA"
        def scegli_chiavetta_importa():
            root = Tk()
            root.attributes('-fullscreen', True)
            root.config(bg=root_background_color)

            frame = Frame(root, bg=root_background_color)
            frame.pack()

            # passo alla funzione pi\media e quindi verranno visualizzate a schermo le chiavette disponibili
            dirs = os.listdir(path_punto_accesso_chiavette)

            label = Label(frame, text="Selezionare la chiavetta da dove importare i file audio",
                          bd=20,
                          bg=root_background_color,
                          font=font_piccolo,
                          fg="white")
            label.grid(row=1, column=0)
            label.config(width=50, height=4)

            # index necessario a ??
            index = 2
            # ciclo che stampa tante "chiavette" quante inserite nel device
            for cartella in dirs:
                path_chiavetta = os.path.join(path_punto_accesso_chiavette, cartella)
                pulsante = SchermateGUI.button_USB_key(frame,
                                                       "importare",
                                                       cartella,
                                                       path_chiavetta,
                                                       path_che_simula_la_memoria_interna_del_raspberry)
                pulsante.grid(row=index, column=0)
                index += 1

            SchermateGUI.exit_button_with_text(root, "Torna indietro")
            root.mainloop()
            # END OF scegli_chiavetta_importa ######################

        SchermateGUI.exit_button_with_text(root, exit_text)
        root.mainloop()
        # END OF esporta_importa

    #  schermata che appare dopo aver cliccato il pulsante ASSOCIAZIONI nel MENU PRINCIPALE
    def schermata_associazioni():
        root = Tk()
        root.attributes('-fullscreen', True)

        root.config(bg=root_background_color)
        current_list = fm.name_file
        frame = Frame(root)
        frame.config(bg=root_background_color)


        label_memo =Label(frame, text=current_list,
                          font=font_piccolo,
                          bg=root_background_color,
                          bd=20,
                          width=200,
                          height=2)
        label_memo.pack(side=TOP)
        sorted_list = fm.give_sorted_list()

        my_list= Listbox(root,  #yscrollcommand = scrollbar.set ,
                         font=font_piccolo,
                         fg="white",
                         width=90, height=8,
                         bg=root_background_color,

                         activestyle="none")


        for audio in sorted_list:
            my_list.insert(END,audio)


        frame.pack()
        my_list.pack()
        Lav.menu_cascata_schermata_associazioni(root)
        uv.exit_button_with_text(root, exit_text)
        root.mainloop()

    # Schermata che appare dopo aver cliccato su ASSOCIA nel MENU PRINCIPALE
    def schermata_pulsanti(closingroot, number_of_button):

        def close(root):
            root.destroy()
            SchermateGUI.schermata_associazioni()

        closingroot.destroy()
        root = Tk()
        root.attributes('-fullscreen', True)

        frame = Frame(root)

        text = Text(frame, wrap="none", bg=root_background_color)
        vsb = Scrollbar(frame, orient="vertical", command=text.yview,width=40)
        vsb.config(width=90)
        text.configure(yscrollcommand=vsb.set,width=3,bg=root_background_color)
        vsb.pack(side="left", fill="y")
        text.pack(side ="left",fill="both",expand=True)

        pulstante_uscita = Button(frame,
                                  text="Torna \nindietro",
                                  command=lambda: close(root),
                                  bd=20,
                                  bg=button_background_color,
                                  font=font_piccolo,
                                  fg=font_color,
                                  activebackground=active_background_color)
        pulstante_uscita.config(height=50, width=18)

        #  ciclo che crea "number_of_button" pulsanti
        for i in range(number_of_button):
            pulsante = SchermateGUI.bottom_with_text(frame, "Pulsante " + str(i + 1))
            pulsante.pack(side=TOP, fill=BOTH)
            text.window_create("end", window=pulsante)
            text.insert("end", "\n")

        text.configure(state="disabled")
        frame.pack(fill="both", expand=True)
        pulstante_uscita.pack(side=RIGHT, fill=BOTH)
        root.mainloop()

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





    # ###### funzione che permette di avere un menu a cascata con la funzione di uscire dal main program ##########
    def menu_cascata_menu_principale(master):
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

