'''
Disabilitare l'import sottostante per la versione PC
Abilitare l'import sottostante per la versione RASPBERRY
'''
#import registrazione as reg

from tkinter import *
import KeyboardView as key
import UtilityView as uv
import StaticParameter as SP
import os

recording = False


class RecordView:

    def registra(path_che_simula_la_memoria_interna_del_raspberry):
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg=SP.root_background_color)

        frame = Frame(root)
        frame.config(bg=SP.root_background_color)
        frame.pack()

        label = Label(frame, text="Premi su Start per registrare",
                      bg=SP.root_background_color,
                      width=90,
                      height=3,
                      font=SP.font_medio,
                      fg=SP.root_font_color
                      )
        label.pack()

        #    funzione che fa partire la registrazione
        def start_recoding(name_recoded_file):
            global recording
            global new_name
            # nascono il pulsante PLAY REGISTRAIONE
            pulsante_play.pack_forget()

            # visualuzzo il pulsante STOP REGISTRAZIONE
            pulsante_stop.pack()

            recording = True

            #cambio il contenuto del label informativo
            label["text"] = "Registrazione in corso.....\nPremi il pulsante per interrompere"

            final_path = path_che_simula_la_memoria_interna_del_raspberry + name_recoded_file

            reg.start(final_path)

        #  funzione che ferma la registrazione e chiede all'utente il nome del file registrato
        def stop_recording():
            global recording
            # nascono il pulsante stop recording con il metodo pack_forget
            pulsante_stop.pack_forget()
            # abilito il pulsante play
            pulsante_play.pack()

            if recording:
                reg.stop()

                # funzione che richiama la tastiera e chiede all'utente il nome del file
                new_name = key.keyboard()

                # path completo del nome del file appena registrato
                initial = os.path.join(path_che_simula_la_memoria_interna_del_raspberry, "reg.wav")

                # path completo del file registrato rinominato
                final = os.path.join(path_che_simula_la_memoria_interna_del_raspberry, new_name + ".wav")

                # funzione che rinomina il file audio appena registrato
                os.rename(initial, final)

                recording = False

                label["text"] = "Premi il pulsante per registrare"

        # caratteristiche pulsante INIZIA REGISTRAZIONE
        pulsante_play = Button(frame,
                               text="Inizia a registrare",
                               bg=SP.button_background_color,
                               command=lambda: start_recoding(SP.name_recoded_file),
                               font=SP.font_piccolo,
                               fg=SP.button_font_color,
                               relief=SP.bord_style,
                               bd=SP.bord_size,
                               activebackground=SP.active_background_color)
        pulsante_play.config(height=5, width=23)
        pulsante_play.pack()

        # caratteristiche pulsante  STOP REGISTRAZIONE
        pulsante_stop = Button(frame,
                               text="Interrompi la registrazione",
                               bg=SP.button_background_color,
                               command=lambda: stop_recording(),
                               font=SP.font_piccolo,
                               fg=SP.button_font_color,
                               relief=SP.bord_style,
                               bd=SP.bord_size,
                               activebackground=SP.active_background_color)
        pulsante_stop.config(height=5, width=23)

        uv.exit_button_with_text(root, SP.exit_text)

        root.mainloop()
