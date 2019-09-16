from tkinter import *
import UtilityView as uv
import os
import StaticParameter as SP


class ImportExportView:

    # schermata che permette di importare ed esportare i file da/su chiavetta
    def import_export(path_punto_accesso_chiavette, path_che_simula_la_memoria_interna_del_raspberry):
        root = Tk()
        root.attributes('-fullscreen', SP.full_screen_option)
        root.config(bg=SP.root_background_color)

        frame = Frame(root)
        frame.config(bg=SP.root_background_color)
        frame.pack()

        label = Label(frame, text="Scegli l'azione desiderata",
                      bg=SP.root_background_color,
                      width=90, height=3,
                      font=SP.font_medio,
                      fg=SP.root_font_color
                      )
        label.pack();

        # numbers_of_key is the number of conneccted key
        numbers_of_key = len(os.listdir(path_punto_accesso_chiavette))

        # le funzioni IMPORTA/ESPORTA vengono visualizzate
        # solamente se è collegata almeno una chiavetta
        if numbers_of_key > 0:
            pulsante_importa = Button(frame,
                                      text="Importa",
                                      bg=SP.button_background_color,
                                      command=lambda: scegli_chiavetta_importa(),
                                      font=SP.font_piccolo,
                                      fg=SP.button_font_color,
                                      bd=SP.bord_size,
                                      relief=SP.bord_style,
                                      activebackground=SP.active_background_color)
            pulsante_importa.pack(side=LEFT)
            pulsante_importa.config(height=5, width=22)

            pulsante_esporta = Button(frame,
                                      text="Esporta",
                                      bg=SP.button_background_color,
                                      command=lambda: scegli_chiavetta_esporta(),
                                      font=SP.font_piccolo,
                                      fg=SP.button_font_color,
                                      bd=SP.bord_size,
                                      relief=SP.bord_style,
                                      activebackground=SP.active_background_color)
            pulsante_esporta.pack(side=RIGHT)
            pulsante_esporta.config(height=5, width=22)
        else:
            # cambio il contenuto e la grandezza del label
            label["text"] = "Inserisci una chiavetta \nper accedere alle altre funzionalità"
            label["height"] = 3

            # pulsante mostrato solo se NON è inserita nessuna chiavetta
            pulsante_memoria_interna = Button(frame,
                                      text="Accedi alla memoria interna",
                                      bg=SP.button_background_color,
                                      command=lambda: uv.show_and_select_item_from_path(
                                                "Memoria interna",path_che_simula_la_memoria_interna_del_raspberry,
                                                path_che_simula_la_memoria_interna_del_raspberry,
                                                "Memoria interna"),
                                      font=SP.font_piccolo,
                                      fg=SP.button_font_color,
                                      bd=SP.bord_size,
                                      relief=SP.bord_style,
                                      activebackground=SP.active_background_color)
            pulsante_memoria_interna.pack()
            pulsante_memoria_interna.config(height=5, width=25)

        #    funzione che richiama la sottoschermata dopo aver cliccato su "ESPORTA"
        def scegli_chiavetta_esporta():
            root = Tk()
            root.attributes('-fullscreen', SP.full_screen_option)
            root.config(bg=SP.root_background_color)

            frame = Frame(root, bg=SP.root_background_color)
            frame.pack()

            # passo alla funzione pi\media e quindi verranno visualizzate a schermo le chiavette disponibili
            dirs = os.listdir(path_punto_accesso_chiavette)

            label = Label(frame,
                          text="Selezionare la chiavetta su cui esportare i file audio",
                          bd=20,
                          bg=SP.root_background_color,
                          font=SP.font_piccolo,
                          fg=SP.root_font_color)
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

            uv.exit_button_with_text(root, SP.exit_text)

            root.mainloop()

        #    funzione che richiama la sottoschermata dopo aver cliccato su "IMPORTA"
        def scegli_chiavetta_importa():
            root = Tk()
            root.attributes('-fullscreen', SP.full_screen_option)
            root.config(bg=SP.root_background_color)

            frame = Frame(root, bg=SP.root_background_color)
            frame.pack()

            # passo alla funzione pi\media e quindi verranno visualizzate a schermo le chiavette disponibili
            dirs = os.listdir(path_punto_accesso_chiavette)

            label = Label(frame, text="Selezionare la chiavetta da dove importare i file audio",
                          bd=20,
                          bg=SP.root_background_color,
                          font=SP.font_piccolo,
                          fg=SP.root_font_color)
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

            uv.exit_button_with_text(root, SP.exit_text)
            root.mainloop()

        uv.exit_button_with_text(root, SP.exit_text)
        root.mainloop()