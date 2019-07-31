from tkinter import *
import fileManaging as fm
import UtilityView as uv
import GUIkeyboard as key
import os

answer= False

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

path_liste =r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\Liste"


class ListAssociationView:

    #  schermata che appare dopo aver cliccato il pulsante ASSOCIAZIONI nel MENU PRINCIPALE
    def schermata_associazioni():
        root = Tk()
        root.attributes('-fullscreen', True)

        root.config(bg=root_background_color)
        current_list = fm.name_file
        frame = Frame(root)
        frame.config(bg=root_background_color)

        label_memo = Label(frame, text=current_list,
                           font=font_piccolo,
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
        ListAssociationView.menu_cascata_schermata_associazioni(root)
        uv.exit_button_with_text(root, exit_text)
        root.mainloop()
    def schermata_pulsanti(closingroot, number_of_button):

        def close(root):
            root.destroy()
            ListAssociationView.schermata_associazioni()

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
        menu = Menu(master, font=font_medio, bg=root_background_color)
        master.config(menu=menu)
        # crea il menu a cascata
        subMenu = Menu(menu, font=font_medio, bg=root_background_color)
        menu.add_cascade(label="Opzioni", font=font_medio, menu=subMenu, )  # menu a cascata
        # riga di separazione
        subMenu.add_separator()
        subMenu.add_command(label="Nuova Lista     ", font=font_medio, command=lambda:ListAssociationView.new_list_view(master))
        subMenu.add_separator()
        subMenu.add_command(label="Mostra Liste    ", font=font_medio, command=lambda: ListAssociationView.show_list(master))
        subMenu.add_separator()
        subMenu.add_command(label="Modifica Lista", font=font_medio, command=lambda:ListAssociationView.schermata_pulsanti(master,5))
        subMenu.add_separator()


    def new_list_view(root):
        root.destroy()
        new_list_name=key.keyBoard()
        fm.create_list(new_list_name)
        ListAssociationView.schermata_associazioni()

    def show_list(closing_root):
        closing_root.destroy()
        def delete_item(root):
            global answer
            list_name = mylist.get('active')
            uv.elimina_file_con_conferma(path_liste,list_name)

            if list_name == fm.name_file:
                fm.change_list('Lista di default')

            # senza questo destroy l'eliminazione non avviene finchè il programma non viene chiuso
            # questa tecnica è usata anche nella funzione select_items_and_copy
            root.destroy()
            ListAssociationView.schermata_associazioni()
            # #############   END OF delete_item ####################

        def upload_list(root):
            list_name = mylist.get('active')
            fm.change_list(list_name)
            root.destroy()
            ListAssociationView.schermata_associazioni()

        #   START OF show_list
        root = Tk()
        root.attributes('-fullscreen', True)

        scrollbar = Scrollbar(root)
        scrollbar.config(width = 70)
        scrollbar.pack(side=LEFT, fill=Y)

        mylist = Listbox(root, yscrollcommand=scrollbar.set, font=font_piccolo, bg=root_background_color)

        # questo ciclo controlla tutte le sottocartelle del path passato in os.walk
        # e inserisce in mylist tutti i file con un'estensione contenuta in "formats"
        for lista in os.listdir(path_liste):
            mylist.insert(END, lista)
        mylist.pack(side=LEFT, fill=BOTH, expand=True)

        mylist.pack(side=LEFT, fill=BOTH, expand=1, )
        scrollbar.config(command=mylist.yview)

        #  pulsante che si trova alla destra della lista di file audio NELLA schermata  ASSOCIA
        pulstante_associa_fileAudio = Button(root,
                                             text="CARICA LISTA",
                                             command=lambda: upload_list(root) ,
                                             bg=root_background_color,
                                             font=font_piccolo,
                                             bd=20,
                                             activebackground=root_background_color)
        pulstante_associa_fileAudio.config(height=5, width=25)
        pulstante_associa_fileAudio.pack(side=TOP, fill=BOTH)

        #  pulsante per eliminare i file audio selezionati     ###############
        pulstante_elimina_fileAudio = Button(root,
                                             text="ELIMINA LISTA",
                                             command=lambda: delete_item(root),
                                             bg=root_background_color,
                                             bd=20,
                                             activebackground=root_background_color,
                                             font=font_piccolo)
        pulstante_elimina_fileAudio.config(height=4, width=25)
        pulstante_elimina_fileAudio.pack( fill=BOTH)

        uv.exit_button_with_text(root, "Torna al menu principale ")
