from tkinter import *
import Reproduction
import StaticParameter as SP
import UtilityView as uv



class SettingsView:
    def set_aspect():
        root = Tk()
        root.attributes('-fullscreen', SP.full_screen_option)
        root.config(bg=SP.root_background_color)
        frame = Frame(root)
        frame.config(bg=SP.root_background_color)
        frame.pack()
        label = Label(root, text="Scegli il tuo bordo preferito",
                      bg=SP.root_background_color,
                      fg=SP.root_font_color,
                      width=0, height=1,
                      font=SP.font_medio
                      )
        label.pack(side=TOP)

        for i in range(6):
            relif_button = Button(
                                frame,
                                text=SP.bord_styles_set[i],
                                font=SP.font_piccolo,
                                fg=SP.button_font_color,
                                command=lambda: SP.set_bord_style(i),
                                bg=SP.button_background_color,
                                relief=SP.bord_styles_set[i],
                                bd=20,
                                activebackground=SP.active_background_color,
                                activeforeground=SP.button_font_color)
            relif_button.config(height=4, width=10)
            relif_button.grid(row=3,column=i)

    def choose_button_aspect():
        root = Tk()
        root.attributes('-fullscreen', SP.full_screen_option)
        root.config(bg=SP.root_background_color)
        frame = Frame(root)
        frame.config(bg=SP.root_background_color)
        frame.pack()
        label = Label(frame, text="Cosa vuoi?",
                      bg=SP.root_background_color,
                      fg=SP.root_font_color,
                      width=90, height=4,
                      font=SP.font_medio
                      )
        label.pack()

        change_size_button = Button(frame,
                                    text="set size",
                                    bg=SP.button_background_color,
                                    command=lambda: SP.set_bord_size(),
                                    font=SP.font_piccolo,
                                    fg=SP.button_font_color,
                                    relief=SP.bord_style,
                                    bd=SP.bord_size,
                                    activebackground=SP.active_background_color)
        change_size_button.config(height=5, width=23)
        change_size_button.pack(side=LEFT)

        change_style_button = Button(frame,
                                     text="set style",
                                     bg=SP.button_background_color,
                                     fg=SP.button_font_color,
                                     command=lambda: SettingsView.set_aspect(),
                                     font=SP.font_piccolo,
                                     relief=SP.bord_style,
                                     bd=SP.bord_size,
                                     activebackground=SP.active_background_color)
        change_style_button.config(height=5, width=23)  # altezza 5
        change_style_button.pack(side=RIGHT)
        uv.exit_button_with_text(root, SP.exit_text)
        root.mainloop()

    def setting_view():
        root = Tk()
        root.attributes('-fullscreen', SP.full_screen_option)
        root.config(bg=SP.root_background_color)
        frame = Frame(root)
        frame.config(bg=SP.root_background_color)
        frame.pack()
        label = Label(frame, text="Impostazioni varie",
                      bg=SP.root_background_color,
                      fg=SP.root_font_color,
                      width=90, height=4,
                      font=SP.font_medio
                      )
        label.pack()

        change_size_button = Button(frame,
                                    text="caratteristiche pulsanti",
                                    bg=SP.button_background_color,
                                    command=lambda: SettingsView.choose_button_aspect(),
                                    font=SP.font_piccolo,
                                    fg=SP.button_font_color,
                                    relief=SP.bord_style,
                                    bd=SP.bord_size,
                                    activebackground=SP.active_background_color)
        change_size_button.config(height=5, width=23)
        change_size_button.pack(side=LEFT)

        change_style_button = Button(frame,
                                     text="volume",
                                     bg=SP.button_background_color,
                                     fg=SP.button_font_color,
                                     command=lambda: SettingsView.volume_view(),
                                     font=SP.font_piccolo,
                                     relief=SP.bord_style,
                                     bd=SP.bord_size,
                                     activebackground=SP.active_background_color)
        change_style_button.config(height=5, width=23)  # altezza 5
        change_style_button.pack(side=RIGHT)
        uv.exit_button_with_text(root, SP.exit_text)
        root.mainloop()

    def volume_view():
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
            root.attributes('-fullscreen', SP.full_screen_option)
            root.config(bg=SP.root_background_color)
            frame = Frame(root)
            frame.config(bg=SP.root_background_color)
            frame.pack()


            # visualizza del valore del volume in un intervallo 10-100
            current_vol_label = Label(
                                    frame,
                                    text=current_volume,
                                    font=SP.font_grande,
                                    width=4,
                                    bg=SP.root_background_color,
                                    fg=SP.root_font_color
                                    )
            current_vol_label.grid(row=1, column=1)

            # pulsante per diminuire il volume
            decrese_vol_button = Button(
                                  frame,
                                  text="-",
                                  font=SP.font_grande,
                                  fg=SP.button_font_color,
                                  command=decrese_and_change,
                                  bg=SP.button_background_color,
                                  relief=SP.bord_style,
                                  bd=SP.bord_size,
                                  activebackground=SP.active_background_color,
                                  activeforeground=SP.button_font_color)
            decrese_vol_button.grid(row=1)
            decrese_vol_button.config(height=1, width=2)

            # pulsante per aumentare il volume
            increse_vol_button = Button(
                                  frame,
                                  text="+",
                                  font=SP.font_grande,
                                  fg=SP.button_font_color,
                                  command=increse_and_change,
                                  bg=SP.button_background_color,
                                  activebackground=SP.active_background_color,
                                  activeforeground=SP.button_font_color,
                                  relief=SP.bord_style,
                                  bd=SP.bord_size)
            increse_vol_button.grid(row=1, column=2)
            increse_vol_button.config(height=1, width=2)

            scritta_vol = Label(frame,
                                text="Volume",
                                heigh=2,
                                font=SP.font_medio,
                                fg=SP.root_font_color,
                                bg=SP.root_background_color)

            scritta_vol.grid(row=0, column=1)
            uv.exit_button_with_text(root, SP.exit_text)
            root.mainloop()
