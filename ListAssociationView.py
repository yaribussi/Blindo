from tkinter import *
import pickle as pk
import fileManaging as fm
import UtilityView as uv
import KeyboardView as kv
import StaticParameter as SP
import os
import shutil


class ListAssociationView:

    #  schermata che appare dopo aver cliccato il pulsante ASSOCIAZIONI nel MENU PRINCIPALE
    def schermata_associazioni():
        root = Tk()
        root.attributes('-fullscreen', SP.full_screen_option)

        root.config(bg=SP.root_background_color)
        current_list = fm.name_file
        frame = Frame(root)
        frame.config(bg=SP.root_background_color)

        label_memo = Label(frame, text=current_list,
                           font=SP.font_piccolo,
                           bg=SP.root_background_color,
                           fg=SP.root_font_color,
                           bd=20,
                           width=200,
                           height=2)
        label_memo.pack(side=TOP)
        sorted_list = fm.give_sorted_list()

        my_list = Listbox(root,  # yscrollcommand = scrollbar.set ,
                          font=SP.font_piccolo,
                          fg=SP.root_font_color,
                          width=90, height=8,
                          bg=SP.root_background_color,
                          activestyle="none")

        for audio in sorted_list:
            my_list.insert(END, audio)

        frame.pack()
        my_list.pack()
        ListAssociationView.menu_cascata_schermata_associazioni(root)
        uv.exit_button_with_text(root, SP.exit_text)
        root.mainloop()
    def schermata_pulsanti(closingroot, number_of_button):

        def close(root):
            root.destroy()
            ListAssociationView.schermata_associazioni()

        closingroot.destroy()
        root = Tk()
        root.attributes('-fullscreen', SP.full_screen_option)

        frame = Frame(root)

        text = Text(frame, wrap="none", bg=SP.root_background_color)
        vsb = Scrollbar(frame, orient="vertical", command=text.yview,width=40)
        vsb.config(width=90)
        text.configure(yscrollcommand=vsb.set,width=3,bg=SP.root_background_color)
        vsb.pack(side="left", fill="y")
        text.pack(side ="left",fill="both",expand=True)

        pulstante_uscita = Button(frame,
                                  text="Torna \nindietro",
                                  command=lambda: close(root),
                                  bd=SP.bord_size,
                                  relief=SP.bord_style,
                                  bg=SP.button_background_color,
                                  font=SP.font_piccolo,
                                  fg=SP.button_font_color,
                                  activebackground=SP.active_background_color)
        pulstante_uscita.config(height=50, width=18)

        #  ciclo che crea "number_of_button" pulsanti
        for i in range(number_of_button):
            pulsante = uv.bottom_with_text(frame, "Pulsante " + str(i + 1))
            pulsante.pack(side=TOP, fill=BOTH)
            text.window_create("end", window=pulsante)
            text.insert("end", "\n")

        text.configure(state="disabled")
        frame.pack(fill="both", expand=True)
        pulstante_uscita.pack(side=RIGHT, fill=BOTH)
        root.mainloop()

    def menu_cascata_schermata_associazioni(master):
        # serve a rimuovere la riga tratteggiata che permette di spostare le ozioni col mouse
        master.option_add('*tearOff', FALSE)
        menu = Menu(master,
                    font=SP.font_medio,
                    bg=SP.root_background_color,
                    fg=SP.root_font_color, )
        master.config(menu=menu)
        # crea il menu a cascata
        subMenu = Menu(menu,
                       font=SP.font_medio,
                       bg=SP.root_background_color,
                       fg=SP.root_font_color, )
        menu.add_cascade(label="Opzioni",
                         font=SP.font_medio,
                         menu=subMenu, )  # menu a cascata
        # riga di separazione
        subMenu.add_separator()
        subMenu.add_command(label="Nuova Lista     ", font=SP.font_medio, command=lambda:ListAssociationView.new_list_view(master))
        subMenu.add_separator()
        subMenu.add_command(label="Mostra Liste    ", font=SP.font_medio, command=lambda: ListAssociationView.show_list(master))
        subMenu.add_separator()
        subMenu.add_command(label="Modifica Lista",   font=SP.font_medio, command=lambda:ListAssociationView.schermata_pulsanti(master,5))
        subMenu.add_separator()

    def new_list_view(root):
        root.destroy()
        find_list_existing_name = False
        existing_list=os.listdir(SP.path_liste)

        new_list_name = kv.keyboard()

        for list in existing_list:
            if list == new_list_name:
                find_list_existing_name=True

        if find_list_existing_name:
            choice = uv.multi_choice_view("Esiste già una lista\ncon questo nome\nVuoi sostituirla o preferisci\nassegnare un altro nome?"
                                 ,"Sostituisci",
                                 "Annulla")

            if choice:
                fm.create_list(new_list_name)
            else:
                return

        else:
            fm.create_list(new_list_name)


        ListAssociationView.schermata_associazioni()

    def show_list(closing_root):
        closing_root.destroy()

        def delete_item(root):
            list_name = mylist.get('active')
            uv.elimina_file_con_conferma(SP.path_liste, list_name)

            if list_name == fm.name_file:
                fm.change_list('Lista di default')

            # senza questo destroy() l'eliminazione della lista non avviene finchè il programma non viene chiuso
            # questa tecnica è usata anche nella funzione select_items_and_copy
            root.destroy()
            ListAssociationView.schermata_associazioni()
            # #############   END OF delete_item ####################

        def upload_list(root):
            list_name = mylist.get('active')
            fm.change_list(list_name)
            root.destroy()
            ListAssociationView.schermata_associazioni()

        def show_chiavette():
            root = Tk()
            root.attributes('-fullscreen', SP.full_screen_option)
            root.config(bg=SP.root_background_color)

            frame = Frame(root, bg=SP.root_background_color)
            frame.pack()

            # passo alla funzione pi\media e quindi verranno visualizzate a schermo le chiavette disponibili
            dirs = os.listdir(SP.path_punto_accesso_chiavette)

            label = Label(frame,
                          text="Selezionare la chiavetta su cui esportare la lista",
                          bd=20,
                          bg=SP.root_background_color,
                          font=SP.font_piccolo,
                          fg=SP.root_font_color)
            label.grid(row=1, column=0)
            label.config(width=50, height=4)

            # index necessario a ??
            index = 2


            # ciclo che stampa tante "chiavette" quante inserite nel device
            for USB_key in dirs:

                path_chiavetta = os.path.join(SP.path_punto_accesso_chiavette, USB_key)
                pulsante = Button(frame, text=USB_key,
                                  bg=SP.button_background_color,
                                  font=SP.font_piccolo,
                                  fg=SP.button_font_color,
                                  bd=SP.bord_size,
                                  relief=SP.bord_style,
                                  activebackground=SP.active_background_color,
                                  # Using the "path_chiavetta=path_chiavetta" trick
                                  # causes your function to store the current value
                                  # of "path_chiavetta" at the time your lambda is defined,
                                  # instead of waiting to look up the value of "path_chiavetta" later.
                                  command=lambda path_chiavetta=path_chiavetta: esporta_lista(root, path_chiavetta)
                                  )
                pulsante.config(width=40, height=3)
                pulsante.grid()
                index += 1

            uv.exit_button_with_text(root, SP.exit_text)

            root.mainloop()

        def esporta_lista(root,path_chiavetta_destinazione):
            root.destroy()
            list_name = mylist.get('active')
            final_path_list = os.path.join(SP.path_liste, list_name)
            final_path_chiavetta = os.path.join(path_chiavetta_destinazione, list_name)
            rewite = True

            if os.path.exists(final_path_chiavetta):

                # variabile booleana assegnata dalla risposta dell' utente
                user_choice = uv.multi_choice_view("Attenzione!\nEsiste già una versione di "+list_name+
                                                   "\nScegli l'azione desiderata",

                                                   "Sovrascrivi",
                                                   "Annulla")

                if user_choice:
                    shutil.rmtree(final_path_chiavetta)
                    rewite = True
                    # umask serve a farantire tutti i diritti di scrittura/lettura
                    # alla cartella creata con makedirs
                    oldmask = os.umask(0o77)#0o22
                    os.makedirs(final_path_chiavetta, 0o777)
                    os.umask(oldmask)
                else:
                    rewite=False
                    print(user_choice)
            else:
                os.makedirs(final_path_chiavetta)


            # carico la lista selezionata dall'utente e la metto nell'oggetto "list_obj"
            if rewite:

                try:
                    with open(final_path_list, 'rb') as io:
                        list_objects = pk.load(io)
                        fm.copy_file_from_path_to_another(final_path_list, final_path_chiavetta)

                        for audio in list_objects:
                            if audio.name != "DEFAULT":
                                name_file = str(audio.name)
                                path_scr = os.path.join(SP.path_che_simula_la_memoria_interna_del_raspberry,name_file)

                                fm.copy_file_from_path_to_another(path_scr,
                                                                  final_path_chiavetta)


                except (FileNotFoundError, IOError) as e:
                    print(e)

        #   START OF show_list
        root = Tk()
        root.attributes('-fullscreen', SP.full_screen_option)

        scrollbar = Scrollbar(root)
        scrollbar.config(width = 70)
        scrollbar.pack(side=LEFT, fill=Y)

        mylist = Listbox(root,
                         yscrollcommand=scrollbar.set,
                         font=SP.font_piccolo,
                         bg=SP.root_background_color,
                         fg=SP.root_font_color, )

        # questo ciclo controlla tutte le sottocartelle del path passato in os.walk
        # e inserisce in mylist tutti i file con un'estensione contenuta in "formats"
        for lista in os.listdir(SP.path_liste):
            mylist.insert(END, lista)
        mylist.pack(side=LEFT, fill=BOTH, expand=True)

        mylist.pack(side=LEFT, fill=BOTH, expand=1, )
        scrollbar.config(command=mylist.yview)


        pulstante_esporta_lista = Button(root,
                                         text="Carica lista",
                                         command=lambda: upload_list(root),
                                         bg=SP.button_background_color,
                                         font=SP.font_piccolo,
                                         fg=SP.button_font_color,
                                         bd=SP.bord_size,
                                         relief=SP.bord_style,
                                         activebackground=SP.root_background_color)
        pulstante_esporta_lista.config(height=5, width=25)
        pulstante_esporta_lista.pack(side=TOP, fill=BOTH)

        pulstante_esporta_lista = Button(root,
                                         text="Esporta lista",
                                         command=lambda:show_chiavette(),
                                         bg=SP.button_background_color,
                                         font=SP.font_piccolo,
                                         fg=SP.button_font_color,
                                         bd=SP.bord_size,
                                         relief=SP.bord_style,
                                         activebackground=SP.root_background_color)
        pulstante_esporta_lista.config(height=5, width=25)
        pulstante_esporta_lista.pack(side=TOP, fill=BOTH)

        #  pulsante per eliminare le liste selezionate     ###############
        pulstante_elimina_lista = Button(root,
                                         text="Elimina lista",
                                         command=lambda: delete_item(root),
                                         bg=SP.button_background_color,
                                         bd=SP.bord_size,
                                         relief=SP.bord_style,
                                         activebackground=SP.root_background_color,
                                         font=SP.font_piccolo,
                                         fg=SP.button_font_color)
        pulstante_elimina_lista.config(height=4, width=25)
        pulstante_elimina_lista.pack(fill=BOTH)

        uv.exit_button_with_text(root, "Torna al menu principale ")

