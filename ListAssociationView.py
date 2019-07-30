from tkinter import *
import fileManaging as fm
import UtilityView as uv

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

exit_text = "Torna al menu principale"


class ListAssociationView:

    #  schermata che appare dopo aver cliccato il pulsante ASSOCIAZIONI nel MENU PRINCIPALE
    def schermata_associazioni():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg=root_background_color)

        frame = Frame(root)
        frame.config(bg=root_background_color)

        label_memo = Label(frame, text="Questi sono le associazioni\nScorri per vederle tutte",
                           font=font_medio,
                           fg="white",
                           bg=root_background_color,
                           bd=20,
                           width=200,
                           height=2)
        label_memo.pack(side=TOP)
        sorted_list = fm.give_sorted_list()

        my_list = Listbox(root,  # yscrollcommand = scrollbar.set ,
                          font=font_piccolo,
                          fg="white",
                          width=90, height=8,
                          bg=root_background_color,

                          activestyle="none")

        for audio in sorted_list:
            my_list.insert(END, audio)

        frame.pack()
        my_list.pack()

        uv.exit_button_with_text(root, exit_text)
        root.mainloop()
