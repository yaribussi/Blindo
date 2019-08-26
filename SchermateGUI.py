from tkinter import *
from RecordView import RecordView as rv
from ImportExportView import ImportExportView as iev
import Reproduction
import StaticParameter as SP
import UtilityView as uv
from ListAssociationView import ListAssociationView as lav
from SettingsView import SettingsView as sv

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
                                  fg=SP.button_font_color,
                                  relief=SP.bord_style,
                                  bd=SP.bord_size,
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
                                          fg=SP.button_font_color,
                                          relief=SP.bord_style,
                                          bd=SP.bord_size,
                                          activebackground=SP.active_background_color)
        pulsante_importa_esporta.grid(row=0, column=1)
        pulsante_importa_esporta.config(height=6, width=24)

        # PULSANTE IMPOSTAZIONI
        pulsante_impostazioni = Button(frame,
                                       text="Volume",
                                       bg=SP.button_background_color,
                                       command=lambda:sv.volume_view(),
                                       font=SP.font_piccolo,
                                       fg=SP.button_font_color,
                                       relief=SP.bord_style,
                                       bd=SP.bord_size,
                                       activebackground=SP.active_background_color)
        pulsante_impostazioni.grid(row=1, column=0)
        pulsante_impostazioni.config(height=6, width=24)

        # PULSANTE LISTA ASSOCIAZIONI
        pulsante_associazioni = Button(frame,
                                       text="Lista Associazioni",
                                       bg=SP.button_background_color,
                                       command=lav.schermata_associazioni,
                                       font=SP.font_piccolo,
                                       fg=SP.button_font_color,
                                       relief=SP.bord_style,
                                       bd=SP.bord_size,
                                       activebackground=SP.active_background_color)
        pulsante_associazioni.grid(row=1, column=1)
        pulsante_associazioni.config(height=6, width=24)

        #  metodo che importa il menu a cascata nel menu principale
        SchermateGUI.menu_cascata_menu_principale(root)

        frame.pack()
        root.mainloop()  # funzione che continua a tenere aperto la finetra principale



    # schermata di volume_view accessibile dal menu cascata


    # funzione che permette di avere un menu a cascata con la funzione di uscire dal main program
    def menu_cascata_menu_principale(master):
        # serve a rimuovere la riga tratteggiata che permette di spostare le ozioni col mouse
        master.option_add('*tearOff', FALSE)
        menu = Menu(master,
                    font=SP.font_medio,
                    fg=SP.root_font_color,
                    bg=SP.root_background_color, )
        master.config(menu=menu)
        # crea il menu a cascata
        subMenu = Menu(menu,
                       font=SP.font_medio,
                       fg=SP.root_font_color,
                       bg=SP.root_background_color, )
        menu.add_cascade(label="Impostazioni", font=SP.font_medio, menu=subMenu, )  # menu a cascata
        # riga di separazione
        subMenu.add_separator()
        subMenu.add_command(label="Impostazioni     ", font=SP.font_medio)#, command=lambda:sv.setting_view())
        subMenu.add_separator()
        subMenu.add_command(label="Spegni    ", font=SP.font_medio, command=lambda: uv.spegni_con_conferma())

        subMenu.add_separator()
        subMenu.add_command(label="Chiudi programma", font=SP.font_medio, command=master.destroy)
        subMenu.add_separator()

