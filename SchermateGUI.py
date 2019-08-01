from tkinter import *
from RecordView import RecordView as rv
from ImportExportView import ImportExportView as iev
import Reproduction
import StaticParameter as SP
import UtilityView as uv
from ListAssociationView import ListAssociationView as lav


class SchermateGUI:

    # schermata del MENUPRINCIPALE
    def menu_principale():

        root = Tk()
        root.config(bg=SP.root_background_color)
        root.attributes('-fullscreen', True)
        frame = Frame(root)

        # PULSANTE REGISTRA
        pulsante_registra= Button(frame,
                                  text="Registra",
                                  bg=SP.button_background_color,
                                  command=lambda:rv.registra(SP.path_che_simula_la_memoria_interna_del_raspberry),
                                  font=SP.font_piccolo,
                                  fg=SP.font_color,
                                  relief="ridge",
                                  bd=4,
                                  activebackground=SP.active_background_color)
        pulsante_registra.grid(row=0, column=0)
        pulsante_registra.config(height=6, width=24)

        # PULSANTE IMPORTA/ESPORTA
        pulsante_importa_esporta = Button(frame,
                                          text="Importa/Esporta ",
                                          bg=SP.button_background_color,
                                          command=lambda:iev.import_export(SP.path_punto_accesso_chiavette,
                                                                            SP.path_che_simula_la_memoria_interna_del_raspberry),
                                          font=SP.font_piccolo,
                                          fg=SP.font_color,
                                          relief="ridge",
                                          bd=4,
                                          activebackground=SP.active_background_color)
        pulsante_importa_esporta.grid(row=0, column=1)
        pulsante_importa_esporta.config(height=6, width=24)

        # PULSANTE ASSOCIA
        pulsante_associa = Button(frame,
                                  text="Volume",
                                  bg=SP.button_background_color,
                                  command=lambda:SchermateGUI.impostazioni(),
                                  font=SP.font_piccolo,
                                  fg=SP.font_color,
                                  relief="ridge",
                                  bd=4,
                                  activebackground=SP.active_background_color)
        pulsante_associa.grid(row=1, column=0)
        pulsante_associa.config(height=6, width=24)

        # PULSANTE LISTA ASSOCIAZIONI
        pulsante_associazioni = Button(frame,
                                       text="Lista Associazioni",
                                       bg=SP.button_background_color,
                                       command=lav.schermata_associazioni,
                                       font=SP.font_piccolo,
                                       fg=SP.font_color,
                                       relief="ridge",
                                       bd=4,
                                       activebackground=SP.active_background_color)
        pulsante_associazioni.grid(row=1, column=1)
        pulsante_associazioni.config(height=6, width=24)

        #  metodo che importa il menu a cascata nel menu principale
        SchermateGUI.menu_cascata_menu_principale(root)

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
        root.config(bg=SP.root_background_color)
        frame = Frame(root)
        frame.config(bg=SP.root_background_color)
        frame.pack()
        button_color= "orange"

        # visualizza del valore del volume in un intervallo 10-100
        current_vol_label = Label(
                                frame,
                                text=current_volume,
                                font=SP.font_grande,
                                width=4,
                                bg=SP.root_background_color,
                                fg="white"
                                )
        current_vol_label.grid(row=1, column=1)

        # pulsante per diminuire il volume
        decrese_vol_button = Button(
                              frame,
                              text="-",
                              font=SP.font_grande,
                              fg=SP.font_color,
                              command=decrese_and_change,
                              bg=SP.button_background_color,
                              relief="ridge",
                              bd=10,
                              activebackground=SP.active_background_color,
                              activeforeground=SP.font_color)
        decrese_vol_button.grid(row=1)
        decrese_vol_button.config(height=1, width=2)

        # pulsante per aumentare il volume
        increse_vol_button = Button(
                              frame,
                              text="+",
                              font=SP.font_grande,
                              fg=SP.font_color,
                              command=increse_and_change,
                              bg=SP.button_background_color,
                              activebackground=SP.active_background_color,
                              activeforeground=SP.font_color,
                              relief="ridge",
                              bd=10)
        increse_vol_button.grid(row=1, column=2)
        increse_vol_button.config(height=1, width=2)

        scritta_vol = Label(frame,
                            text="Volume",
                            heigh=2,
                            font=SP.font_medio,
                            fg="white",
                            bg=SP.root_background_color)

        scritta_vol.grid(row=0, column=1)
        uv.exit_button_with_text(root, SP.exit_text)
        root.mainloop()


    # funzione che permette di avere un menu a cascata con la funzione di uscire dal main program
    def menu_cascata_menu_principale(master):
        # serve a rimuovere la riga tratteggiata che permette di spostare le ozioni col mouse
        master.option_add('*tearOff', FALSE)
        menu = Menu(master,
                  font=SP.font_medio,
                  fg=SP.font_color,
                  bg=SP.root_background_color,)
        master.config(menu=menu)
        # crea il menu a cascata
        subMenu = Menu(menu,
                       font=SP.font_medio,
                       fg=SP.white,
                       bg=SP.root_background_color,)
        menu.add_cascade(label="Impostazioni", font=SP.font_medio, menu=subMenu, )  # menu a cascata
        # riga di separazione
        subMenu.add_separator()
        subMenu.add_command(label="Volume     ", font=SP.font_medio, command=SchermateGUI.impostazioni)
        subMenu.add_separator()
        subMenu.add_command(label="Spegni    ", font=SP.font_medio, command=lambda: uv.spegni_con_conferma())

        subMenu.add_separator()
        subMenu.add_command(label="Chiudi programma", font=SP.font_medio, command=master.destroy)
        subMenu.add_separator()

