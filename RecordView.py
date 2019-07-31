from tkinter import *
#da commentare per la versione PC
#import registrazione as reg
import GUIkeyboard as key
import UtilityView as uv
import os

recording = False

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

# nome di default del file registrato
name_recoded_file= "/reg.wav"


class RecordView:

    def registra(path_che_simula_la_memoria_interna_del_raspberry):
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
            global new_name

            recording = True

            label["text"] = "Registrazione in corso.....\nPremi il pulsante rosso per interrompere"

            final_path = path_che_simula_la_memoria_interna_del_raspberry + name_recoded_file

            reg.start(final_path)

        #  funzione che ferma la registrazione e chiede all'utente il nome del file registrato
        def stop_recording():
            global recording

            if recording:

                reg.stop()
                label["text"] = "Registrazione effettuata con successo!"

                # funzione che richiama la tastiera e chiede all'utente il nome del file
                new_name = key.keyBoard()

                # path completo del nome del file appena registrato
                initial = path_che_simula_la_memoria_interna_del_raspberry + "/reg.wav"

                # path completo del file registrato rinominato
                final = path_che_simula_la_memoria_interna_del_raspberry + "/" + new_name + ".wav"
                # funzione che rinomina il file audio appena registrayo
                os.rename(initial, final)
                recording = False
                label["text"] = "Premi su Start per registrare"

            else:
                uv.show_dialog_with_time("Attenzione\n"
                                                   "La registrazione non è ancora partita\n"
                                                   "Premi sul pulsante verde per avviarla", 2)
                # tkinter.messagebox.showinfo("Attenzione","La registrazione non è ancora partita, premi sul pulsante verde",parent=root)

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

        uv.exit_button_with_text(root, exit_text)

        root.mainloop()