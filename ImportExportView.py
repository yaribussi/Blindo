from tkinter import *
import UtilityView as uv
import os

path_punto_accesso_chiavette = r"C:\Users\Diego Berardi\Desktop\file audio blindo\punto di accesso chiavette"
path_che_simula_la_memoria_interna_del_raspberry = r"C:\Users\Diego Berardi\Desktop\file audio blindo\simula memoria interna"


'''##############################################################################################################'''
'''
######                            ATTENZIONE                                              ###########
######              ABILITARE  PER UTILIZZARE IL SW SUL RASPBERRY            ###########
path_punto_accesso_chiavette = "/media/pi"
path_che_simula_la_memoria_interna_del_raspberry = "/home/pi/Documents/fileAudio"

#############                       VARIABILI GLOBALI              ###########################
'''

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

exit_text= "Torna al menu principale"


class ImportExportView:

    # schermata che permette di importare ed esportare i file da/su chiavetta
    def import_export(path_punto_accesso_chiavette, path_che_simula_la_memoria_interna_del_raspberry):
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg=root_background_color)

        frame = Frame(root)
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
                                  command=lambda: scegli_chiavetta_importa(),
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
                                  command=lambda: scegli_chiavetta_esporta(),
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
                pulsante = uv.button_USB_key(frame, "esportare", cartella,
                                             path_che_simula_la_memoria_interna_del_raspberry, path_chiavetta)
                pulsante.grid(row=index, column=0)
                index += 1

            uv.exit_button_with_text(root, exit_text)

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
                pulsante = uv.button_USB_key(frame,
                                             "importare",
                                             cartella,
                                             path_chiavetta,
                                             path_che_simula_la_memoria_interna_del_raspberry)
                pulsante.grid(row=index, column=0)
                index += 1

            uv.exit_button_with_text(root, exit_text)
            root.mainloop()

        uv.exit_button_with_text(root, exit_text)
        root.mainloop()