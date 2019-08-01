from tkinter import *
import fileManaging as fm
import subprocess
import os
import StaticParameter as SP


#    funzione che mostra a video un messaggio
#    passatole come primo parametro per un tempo (in secondi) passato come secondo parametrp
def show_dialog_with_time(text, time):
    def close(to_close):
        to_close.quit()
        to_close.destroy()

    dialog = Tk()
    dialog.config(bg=SP.root_background_color)
    dialog.geometry("+210+180")  # distanza da sinistra e dall'alto del popup
    dialog.overrideredirect(1)  # rimuove la barra che permetterebbe di chiudere la finestra appena creata

    label = Label(dialog, text=text,
                  bg=SP.pop_up_colour_background,
                  font=SP.font_piccolo,
                  wraplength=500,
                  bd=4,
                  fg=SP.white,
                  relief=GROOVE
                  )
    label.configure(anchor="center")
    label.pack(expand=True)

    # time*1000 serve a convertire i secondi passati come parametro in millisecondi richiesti dalla funzione after
    dialog.after(time * 1000, close, dialog)
    dialog.mainloop()


#  funzione per avere un pulsante di uscita dalla schermata attuale con testo variabile passato come param
def exit_button_with_text(root, text):

            pulstante_uscita = Button(root,
                                      text=text,
                                      command=lambda: root.destroy(),
                                      bg=SP.button_background_color,
                                      font=SP.font_piccolo,
                                      fg=SP.font_color,
                                      bd=4,
                                      activebackground=SP.active_background_color)
            pulstante_uscita.config(height=3, width=10)
            pulstante_uscita.pack(side=BOTTOM, fill=BOTH)


# questa funzione permette di creare un pulsante
# che quando premuto apre la schermata show_file
# i parametri richiesti per la creazione del bottone sono: -frame su cui il bottone verrà applicato
#                                                          -testo che apparirà sul pulsante
def bottom_with_text(frame, text):
            pulsante = Button(frame,
                              text=text,
                              bg=SP.button_background_color,
                              relief="ridge",
                              font=SP.font_piccolo,
                              fg=SP.font_color,
                              bd=20,
                              command=lambda: show_file(text.replace("Pulsante ", "")),
                              activebackground=SP.active_background_color,
                              activeforeground=SP.black)

            pulsante.config(width=20, height=3)
            return pulsante


# funzione che crea una schermata che chiede all'utente la conferma dello spegnimento del device
def spegni_con_conferma():
    root = Tk()
    root.attributes('-fullscreen', True)
    root.config(bg=SP.root_background_color)
    frame = Frame(root)
    frame.config(bg=SP.root_background_color)
    frame.pack()
    label = Label(frame, text="Vuoi spegnere il dispositivo?",
                  bg=SP.root_background_color,
                  fg=SP.font_color,
                  width=90, height=4,
                  font=SP.font_medio
                  )
    label.pack()

    pulsante_spegni = Button(frame,
                             text="Spegni",
                             bg=SP.button_background_color,
                             command=lambda: subprocess.Popen(['shutdown', '-h', 'now']),
                             font=SP.font_piccolo,
                             fg=SP.font_color,
                             relief="ridge",
                             bd=20,
                             activebackground=SP.active_background_color)
    pulsante_spegni.config(height=5, width=23)
    pulsante_spegni.pack(side=LEFT)

    pulsante_annulla = Button(frame,
                              text="Annulla",
                              bg=SP.button_background_color,
                              fg=SP.font_color,
                              command=lambda: root.destroy(),
                              font=SP.font_piccolo,
                              relief="ridge",
                              bd=20,
                              activebackground=SP.active_background_color)
    pulsante_annulla.config(height=5, width=23)  # altezza 5
    pulsante_annulla.pack(side=RIGHT)
    root.mainloop()


# funzione che richiama una schermata chiedendo all'utente la conferma dell'eliminazione del file selezionato
def elimina_file_con_conferma(path, nome_file):

    def confirmed_deletion(path, nome_file):
        fm.delete_element_from_list(nome_file,fm.name_file)
        os.remove(os.path.join(path, nome_file))
        root.quit()
        root.destroy()

    def abort_deletion():
        root.quit()
        root.destroy()

    root = Tk()
    root.attributes('-fullscreen', True)
    root.config(bg=SP.root_background_color)

    frame = Frame(root)
    frame.config(bg=SP.root_background_color)
    frame.pack()

    label = Label(
        frame, text="Attenzione!\nVuoi eliminare\n" + nome_file + " ?",
        bg=SP.root_background_color,
        width=90, height=3,
        font=SP.font_medio)
    label.pack()

    pulsante_elimina = Button(frame,
                              text="Elimina",
                              bg=SP.button_background_color,
                              command=lambda: confirmed_deletion(path, nome_file),
                              font=SP.font_piccolo,
                              relief="ridge",
                              bd=20,
                              activebackground=SP.active_background_color)
    pulsante_elimina.config(height=5, width=23)
    pulsante_elimina.pack(side=LEFT)

    pulsante_annulla = Button(frame,
                              text="Annulla",
                              bg=SP.button_background_color,
                              command=lambda: abort_deletion(),
                              font=SP.font_piccolo,
                              relief="ridge",
                              bd=20,
                              activebackground=SP.active_background_color)
    pulsante_annulla.config(height=5, width=23)  # altezza 5
    pulsante_annulla.pack(side=RIGHT)
    root.mainloop()


def elimina_file_con_conferma_multipla(selected_file):

    def confirmed_deletion():
        for list in os.listdir(SP.path_liste):
            for file in selected_file:
                fm.delete_element_from_list(file, list)

        for el in selected_file:
            os.remove(os.path.join(SP.path_che_simula_la_memoria_interna_del_raspberry, el))
        root.quit()
        root.destroy()

    def abort_deletion():
        root.quit()
        root.destroy()

    root = Tk()
    root.attributes('-fullscreen', True)
    root.config(bg=SP.root_background_color)

    frame = Frame(root)
    frame.config(bg=SP.root_background_color)
    frame.pack()

    label = Label(
        frame, text="Attenzione!\nVuoi eleiminare " +str(len(selected_file))+"?",
        bg=SP.root_background_color,
        width=90, height=3,
        font=SP.font_medio)
    label.pack()

    pulsante_elimina = Button(frame,
                              text="Elimina",
                              bg=SP.button_background_color,
                              command=lambda: confirmed_deletion(),
                              font=SP.font_piccolo,
                              relief="ridge",
                              bd=20,
                              activebackground=SP.active_background_color)
    pulsante_elimina.config(height=5, width=23)
    pulsante_elimina.pack(side=LEFT)

    pulsante_annulla = Button(frame,
                              text="Annulla",
                              bg=SP.button_background_color,
                              command=lambda: abort_deletion(),
                              font=SP.font_piccolo,
                              relief="ridge",
                              bd=20,
                              activebackground=SP.active_background_color)
    pulsante_annulla.config(height=5, width=23)  # altezza 5
    pulsante_annulla.pack(side=RIGHT)
    root.mainloop()



# schermata che appare DOPO aver cliccato uno dei pulsatni della lista
# che vengono mostrati DOPO aver cliccato il pulsante ASSOCIA nel MENUPRINCIPALE
# richiede come parametro l'ID del pulsante che ha richiamato questa funzione
# parametro necessario per un trackback
def show_file(idButton):
    #  permette di fare l'associazione di un fileAudio dato un ID di un pulsante passato come parametro
    def bind_button(id, root):
        song_name = mylist.get('active')
        fm.bind(song_name, id)
        root.destroy()

    #   funzione che elimina l'elemento selezionato dopo aver chiesto all'utente      #########
    def delete_item(root):

        song_name = mylist.get('active')
        elimina_file_con_conferma(SP.path_che_simula_la_memoria_interna_del_raspberry,song_name)
        root.destroy()
            # #############   END OF delete_item ####################

    #   START OF show_file
    root = Tk()
    root.attributes('-fullscreen', True)

    scrollbar = Scrollbar(root)
    scrollbar.config(width=70)
    scrollbar.pack(side=LEFT, fill=Y)
    formats = SP.formats_audio
    mydict = {}
    mylist = Listbox(root,
                     yscrollcommand=scrollbar.set,
                     font=SP.font_piccolo,
                     fg="white",
                     bg=SP.root_background_color)
    # questo ciclo controlla tutte le sottocartelle del path passato in os.walk
    # e inserisce in mylist tutti i file con un'estensione contenuta in "formats"
    for radice, cartelle, files in os.walk(SP.path_che_simula_la_memoria_interna_del_raspberry, topdown=False):
        for name in files:
            for tipo in formats:
                if tipo in name:
                    temp_str = os.path.join(radice, name)
                    mydict[name] = temp_str
                    mylist.insert(END, name)
    mylist.pack(side=LEFT, fill=BOTH, expand=True)

    mylist.pack(side=LEFT, fill=BOTH, expand=1, )
    scrollbar.config(command=mylist.yview)

    #  pulsante che si trova alla destra della lista di file audio NELLA schermata  ASSOCIA
    pulstante_associa_fileAudio = Button(root,
                                         text="Scegli il file \n"
                                              "che vuoi associare\n "
                                              "al Pulsante" + idButton + "\n"
                                                                         "e poi clicca qui \n",
                                         command=lambda: bind_button(int(idButton), root),
                                         bg=SP.button_background_color,
                                         font=SP.font_piccolo,
                                         fg=SP.font_color,
                                         bd=20,
                                         activebackground=SP.active_background_color)
    pulstante_associa_fileAudio.config(height=5, width=25)
    pulstante_associa_fileAudio.pack(side=TOP, fill=BOTH)

    #  pulsante per eliminare i file audio selezionati     ###############
    pulstante_elimina_fileAudio = Button(root,
                                         text="Scegli il file \n"
                                              "che vuoi eliminare\n"
                                              "e clicca qui",
                                         command=lambda: delete_item(root),
                                         bg=SP.button_background_color,
                                         bd=20,
                                         activebackground=SP.active_background_color,
                                         font=SP.font_piccolo,
                                         fg=SP.font_color)
    pulstante_elimina_fileAudio.config(height=4, width=25)
    pulstante_elimina_fileAudio.pack(fill=BOTH)

    exit_button_with_text(root, "Torna alla lista pulsanti")

    # questa funzione permette di creare un pulsante
    # che quando premuto apre la schermata show_file
    # i parametri richiesti per la creazione del bottone sono: -frame su cui il bottone verrà applicato
    #                                                          -testo che apparirà sul pulsante


def bottom_with_text(frame, text):
    pulsante = Button(frame,
                      text=text,
                      bg=SP.button_background_color,
                      relief="ridge",
                      font=SP.font_piccolo,
                      fg=SP.font_color,
                      bd=20,
                      command=lambda: show_file(text.replace("Pulsante", "")),
                      activebackground=SP.active_background_color,
                      activeforeground="black")

    pulsante.config(width=20, height=3)
    return pulsante


# funzione che crea un pulsante che visualizza i file da un path di origine
# e li copia in un path destinzaione
# mod: può essere "ESPORTA" o "IMPORTA" serve a rendere questa funzione più generale
def button_USB_key(frame, mod, nome_chiavetta, path_origine, path_destinzaione):
    pulsante = Button(frame, text=nome_chiavetta,
                      bg=SP.button_background_color,
                      font=SP.font_piccolo,
                      fg=SP.font_color,
                      bd=20,
                      activebackground=SP.active_background_color,
                      command=lambda: show_and_select_item_from_path(mod, path_origine, path_destinzaione)
                      )
    pulsante.config(width=40, height=3)
    return pulsante


# schermata che stampa a video i file contenuti in un determinato path
def show_and_select_item_from_path(mod, path_origine, path_destinzaione):
    #     funzione che copia la lista dei file selizionati in un'altra directory
    #     dall'utente nella schermata IMPORTA, dopo aver cliccato sul pulsante
    #     avnte la scritta, appunto IMPORTA
    def select_items_and_copy(root):

        selected = [mylist.get(idx) for idx in mylist.curselection()]
        # pop up con durata 2 secondi che informa di attendere
        show_dialog_with_time("L'operazione potrebbe richedere alcuni istanti...", 2)
        # ciclo che copia tutti i file selezionati dall'utente
        for file in selected:
            fm.copy_file_from_path_to_another(mydict[file], path_destinzaione)

        show_dialog_with_time("Operazione conclusa con successo", 2)
        root.destroy()
        # ######                 END OF select_items_and_copy    ###################

    def delete_selected_elements(root):
        selected = [mylist.get(idx) for idx in mylist.curselection()]
        # elimina_file_con_conferma(path_origine, str(number_of_deleted_file) + " file audio")

        elimina_file_con_conferma_multipla(selected)

        root.destroy()

    root = Tk()
    root.attributes('-fullscreen', True)
    formats = [".mp3", ".wav", ".wma", ".ogg", ".flac"]

    label_info = Label(root, text=path_origine,
                       bg=SP.root_background_color,
                       width=90, height=3,
                       font=SP.font_piccolo
                       )
    label_info.pack()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=LEFT, fill=Y)
    mylist = Listbox(root,
                     yscrollcommand=scrollbar.set,
                     selectmode=MULTIPLE,
                     font=SP.font_piccolo,
                     fg="white",
                     bg=SP.root_background_color)
    mydict = {}

    for radice, cartelle, files in os.walk(path_origine, topdown=False):
        for name in files:
            for tipo in formats:
                if tipo in name:
                    temp_str = os.path.join(radice, name)
                    mydict[name] = temp_str
                    mylist.insert(END, name)
    mylist.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(width=70, command=mylist.yview)
    exit_button_with_text(root, "Torna indietro")

    # ############        caratteristiche pulsante IMPORTA/ESPORTA        ######################
    testo_pulsante = "Seleziona i file \nche desideri " + mod + "\ne poi clicca qui"
    pulstante_importa = Button(root,
                               text=testo_pulsante,
                               bg=SP.button_background_color,
                               command=lambda: select_items_and_copy(root),
                               font=SP.font_piccolo,
                               fg=SP.font_color,
                               bd=40,
                               activebackground=SP.active_background_color)
    pulstante_importa.config(height=4, width=20)

    pulstante_importa.pack(side=TOP, fill=BOTH)

    # visualizza il pulsante solo in modalità esporta
    if mod =="esportare...":
        pulstante_elimina = Button(root,
                                   text="Scegli il file \nche vuoi eliminare",
                                   bg=SP.button_background_color,
                                   command=lambda: delete_selected_elements(root),
                                   font=SP.font_piccolo,
                                   bd=40,
                                   activebackground=SP.active_background_color)
        pulstante_elimina.config(height=9, width=20)
        pulstante_elimina.pack(side=TOP, fill=BOTH)

    root.mainloop()
