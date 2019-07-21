import tkinter.messagebox
from tkinter import *
import fileManaging as fm
import GUIkeyboard as key
import subprocess
import os


'''##############################################################################################################'''
'''###########                                  ATTENZIONE                             ##########################'''
'''###########    cambiare il path per poter utilizzare il programma sul proprio PC    ##########################'''
'''##############################################################################################################'''

path_che_simula_luogo_delle_chiavette = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudiofromChiavetta"
path_che_simula_la_memoria_interna_del_raspberry = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudioRSPmemory"

'''##############################################################################################################'''
'''
######                            ATTENZIONE                                              ###########
######              ABILITARE  PER UTILIZZARE IL SW SUL RASPBERRY            ###########

import GPIOmanaging
import registrazione as Reg
path_che_simula_luogo_delle_chiavette = "/media/pi"
path_che_simula_la_memoria_interna_del_raspberry = "/home/pi/Documents/fileAudio"
os.chdir("/home/pi/Desktop/Main/")
#subprocess.Popen(['unclutter','-idle','0'])   #comando per rimuovere il cursore
##########################################################################################
'''

'''#############                       VARIABILI GLOBALI              ###########################'''
asnwer=False
stopper=None
recording=False

font_size_piccolo = 20
font_size_medio   = 33
font_size_grande  = 80
font_stile = "Helvetica"
font_piccolo = (font_stile, font_size_piccolo)
font_medio = (font_stile, font_size_medio)
font_grande = (font_stile, font_size_grande)

exit_text= "Torna al menu principale"

'''############                 numero di pulsanti collegati                   ######################'''
number_of_phisical_button=6

name_recoded_file= "/reg.wav"

class SchermateGUI:

############ schermata del MENUPRINCIPALE ###################à

    def menu_principale():

        root = Tk()
        root.config(bg="pale green")
        root.attributes('-fullscreen', True)
        frame = Frame(root)

    ##########   caratteristiche dei quattro pulsanti del menu Principale    ###########
        pulsante_registra= Button(frame,
                                  text="Registra",
                                  bg="orange",
                                  command=lambda:SchermateGUI.registra(),
                                  font = font_piccolo,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="orange2")
                                #activeforeground="blue")
        pulsante_registra.grid(row=0, column=0)
        pulsante_registra.config(height=5, width=22)

        pulsante_importa_esporta = Button(frame,
                                          text="Importa/Esporta ",
                                          bg="red",
                                          command=SchermateGUI.esporta_importa,
                                          font = font_piccolo,
                                          relief="ridge",
                                          bd=20,
                                          activebackground="red2")
        pulsante_importa_esporta.grid(row=0, column=1)
        pulsante_importa_esporta.config(height=5, width=22)

        pulsante_associa = Button(frame,
                                  text="Associa",
                                  bg="yellow",
                                  command=lambda:SchermateGUI.schermata_pulsanti(root, number_of_phisical_button),
                                  font = font_piccolo,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="yellow2")
        pulsante_associa.grid(row=1, column=0)
        pulsante_associa.config(height=5, width=22)

        pulsante_associazioni = Button(frame,
                                       text="Lista Associazioni",
                                       bg="red3",
                                       command=SchermateGUI.schermata_associazioni,
                                       font = font_piccolo,
                                       relief="ridge",
                                       bd=20,
                                       activebackground="red4")
        pulsante_associazioni.grid(row=1, column=1)
        pulsante_associazioni.config(height=5, width=22)

        ######################   metodo che importa il menu a cascata in qst menu principale###############
        SchermateGUI.menu_cascata_con_exit(root)

        frame.pack()
        root.mainloop()  # funzione che continua a tenere aperto la finetra principale



    '''################################################################################################################'''
    '''###################                 funzioni che aprono le varie schermate                       ###############'''
    '''################################################################################################################'''


#########    schermata che appare dopo aver cliccato sul pulsante REGISTRA nel MENUPRINCIPALE           ##########
#########    momentaneamente non svolge alcuna funzione oltre a quella di permettere di tornare nel MENUPRINCIPALE
    def registra():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="orange")    

        frame = Frame(root)
        frame.config(bg="orange")
        frame.pack()

        label = Label(frame, text="Premi su Start per registrare",
                      bg="orange",
                      width=90, height=3,
                      font=font_medio
                      )
        label.pack()

        ##########              funzione che fa partire la registrazione
        def start_recoding(name_recoded_file):
            global recording
            global stopper
            global new_name

            recording=True

            label["text"] = "Registrazione in corso.....\nPremi il pulsante rosso per interrompere"

            final_path= path_che_simula_la_memoria_interna_del_raspberry + name_recoded_file
            stopper = Reg.start(final_path)

        #########   funzione che ferma la registrazione
        def stop_recording():
            global stopper
            global recording

            if recording:
                
                Reg.stop(stopper) 
                label["text"] = "Registrazione effettuata con successo!"
                
                new_name=key.keyBoard()

                initial= path_che_simula_la_memoria_interna_del_raspberry + "/reg.wav"
                final= path_che_simula_la_memoria_interna_del_raspberry + "/" + new_name + ".wav"
                
                os.rename(initial,final)
                recording=False
                label["text"] ="Premi su Start per registrare"

            else:
                tkinter.messagebox.showinfo("Attenzione","La registrazione non è ancora partita, premi sul pulsante verde",parent=root)

        pulsante_play = Button(frame,
                               text="Inizia a registrare",
                               bg="green",
                               command=lambda: start_recoding(name_recoded_file),
                               font=font_piccolo,
                               relief="ridge",
                               bd=20,
                               activebackground="green")
        pulsante_play.config(height=5, width=23)
        pulsante_play.pack(side=LEFT)

        pulsante_stop = Button(frame,
                               text="Interrompi la registrazione",
                               bg="firebrick3",
                               command=lambda: stop_recording(),
                               font=font_piccolo,
                               relief="ridge",
                               bd=20,
                               activebackground="red")
        pulsante_stop.config(height=5, width=23) #altezza 5
        pulsante_stop.pack(side=RIGHT)

        SchermateGUI.exit_button_with_text(root, exit_text)
               
        root.mainloop()

    #schermata che permette di importare ed esportare i file da/su chiavetta
    def esporta_importa():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="orange")

        frame=Frame(root)
        frame.config(bg='orange')
        frame.pack()

        label = Label(frame, text="Scegli l'azione desiderata",
                      bg="orange",
                      width=90, height=1,
                      font=font_medio
                      )
        label.pack();

        pulsante_importa = Button(frame,
                                  text="Importa",
                                  bg="goldenrod1",
                                  command=lambda:scegli_chiavetta_importa(),
                                  font=font_piccolo,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="Dark orange")
        pulsante_importa.pack(side=LEFT)
        pulsante_importa.config(height=5, width=22)

        pulsante_esporta = Button(frame,
                                  text="Esporta",
                                  bg="tomato",
                                  command=lambda:scegli_chiavetta_esporta(),
                                  font=font_piccolo,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="tomato3")
        pulsante_esporta.pack(side=RIGHT)
        pulsante_esporta.config(height=5, width=22)

        #############       funzione che richiama la sottoschermata dopo aver cliccato su "ESPORTA"
        def scegli_chiavetta_esporta():
            root = Tk()
            root.attributes('-fullscreen', True)
            root.config(bg="DarkOrange1")

            frame = Frame(root, bg="DarkOrange1")
            frame.pack()

            # passo alla funzione pi\media e quindi verranno visualizzate a schermo le chiavette disponibili
            dirs = os.listdir(path_che_simula_luogo_delle_chiavette)

            label = Label(frame, text="Selezionare la chiavetta su cui esportare i file audio",
                          bd=20,
                          bg="DarkOrange1",
                          font=font_piccolo)
            label.grid(row=1, column=0)
            label.config(width=50, height=4)

            index = 2

            for cartella in dirs:
                path_chiavetta = os.path.join(path_che_simula_luogo_delle_chiavette, cartella)
                pulsante = SchermateGUI.button_USB_key(frame, "esporare", cartella,
                                                       path_che_simula_la_memoria_interna_del_raspberry, path_chiavetta)
                pulsante.grid(row=index, column=0)
                index += 1

            SchermateGUI.exit_button_with_text(root, exit_text)

            root.mainloop()

        ############       funzione che richiama la sottoschermata dopo aver cliccato su "IMPORTA"
        def scegli_chiavetta_importa():
            root = Tk()
            root.attributes('-fullscreen', True)
            root.config(bg="DarkOrange1")

            frame = Frame(root, bg="DarkOrange1")
            frame.pack()

            # passo alla funzione pi\media e quindi verranno visualizzate a schermo le chiavette disponibili
            dirs = os.listdir(path_che_simula_luogo_delle_chiavette)

            label = Label(frame, text="Selezionare la chiavetta da dove importare i file audio",
                          bd=20,
                          bg="DarkOrange1",
                          font=font_piccolo)
            label.grid(row=1, column=0)
            label.config(width=50, height=4)

            index = 2
            for cartella in dirs:
                path_chiavetta = os.path.join(path_che_simula_luogo_delle_chiavette, cartella)
                pulsante = SchermateGUI.button_USB_key(frame, "importare", cartella, path_chiavetta,
                                                       path_che_simula_la_memoria_interna_del_raspberry)
                pulsante.grid(row=index, column=0)
                index += 1

            SchermateGUI.exit_button_with_text(root, exit_text)
            root.mainloop()
            ############ end of scegli_chiavetta_importa ######################

        SchermateGUI.exit_button_with_text(root, exit_text)
        root.mainloop()


    ############  schermata che appare dopo aver cliccato il pulsante ASSOCIAZIONI nel MENU PRINCIPALE
    def schermata_associazioni():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="DarkOrange1")

        frame = Frame(root)
        frame.config(bg="DarkOrange1")

        label_memo =Label(frame, text="Questi sono le associazioni che hai precedentemente fatto\nScorri per vederle tutte",
                          font=font_piccolo,
                          bg="DarkOrange1",
                          bd=20,
                          width=200,
                          height=2)
        label_memo.pack(side=TOP)
        sorted_list = fm.give_sorted_list()

        my_list= Listbox(root,  #yscrollcommand = scrollbar.set ,
                         font=font_piccolo,
                         width=90, height=8,
                         bg="DarkOrange1",

                         activestyle="none")


        for audio in sorted_list:
            my_list.insert(END,audio)


        frame.pack()
        my_list.pack()

        SchermateGUI.exit_button_with_text(root, exit_text)
        root.mainloop()

##########à Schermata che appare dopo aver cliccato su ASSOCIA nel MENU PRINCIPALE
    def schermata_pulsanti(closingroot, number_of_button):
        closingroot.quit()
        root = Tk()
        root.attributes('-fullscreen', True)

        frame = Frame(root)

        text = Text(frame, wrap="none", bg="yellow")
        vsb = Scrollbar(frame, orient="vertical", command=text.yview,width=40)
        vsb.config(width=90)################------------>
        text.configure(yscrollcommand=vsb.set,width=3,bg="yellow")
        vsb.pack(side="left", fill="y")
        text.pack(side ="left",fill="both",expand=True)

        pulstante_uscita = Button(frame
                                  ,
                                  text="Torna al\nmenu principale",
                                  command=lambda: root.destroy(),
                                  bd = 20,
                                  bg="yellow",
                                  font = font_piccolo,
                                  activebackground="yellow")
        pulstante_uscita.config(height=50, width=18)

        ##########  ciclo che crea i bottoni necessari  ###########
        for i in range(number_of_button):
            pulsante = SchermateGUI.bottom_with_text(frame, "Pulsante " + str(i + 1))
            pulsante.pack(side=TOP, fill=BOTH)
            text.window_create("end", window=pulsante)
            text.insert("end", "\n")

        text.configure(state="disabled")
        frame.pack(fill="both", expand=True)
       
        pulstante_uscita.pack(side=RIGHT,fill=BOTH)
       
        root.mainloop()

    def impostazioni():
        current_volume = fm.give_volume()
            ##### funzioni di servizio che cambiano il volume e aggiornano il suo valore che è stampato all'utente
        def changeVolumeOnDisplay():
            label.configure(text=fm.give_volume())

        def IncreseAndChange():
            fm.increse_vol()
            changeVolumeOnDisplay()


        def DecreseAndChange():
            fm.decrese_vol()
            changeVolumeOnDisplay()

        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="Dark orange")
        frame = Frame(root)
        frame.config(bg="Dark orange")
        frame.pack()
        buttonColor="orange"

    ######## stampa del valore del volume in un intervallo 10-100
        label = Label(frame,
                      text=current_volume,
                      font=font_grande,width=4
                      ,bg="Dark orange"
                      )
        label.grid(row=1, column=1)
        

        pulsante_vol = Button(frame,      #pulsante per diminuire il volume
                              text="-",
                              font = font_grande,
                              command=DecreseAndChange,
                              bg=buttonColor,
                                relief="ridge",
                                bd=10,
                      activebackground=buttonColor)
        pulsante_vol.grid(row=1)
        pulsante_vol.config(height=1, width=2)

        pulsante_vol = Button(frame,      #pulsante per aumentare il volume
                              text="+",
                              font = font_grande,
                              command=IncreseAndChange,
                              bg=buttonColor,
                              activebackground=buttonColor,
                                relief="ridge",
                                bd=10)
        pulsante_vol.grid(row=1, column=2)
        pulsante_vol.config(height=1, width=2)

        scritta_vol = Label(frame, text="Volume",heigh =2,
                            font = font_medio,
                            bg="Dark orange")

        scritta_vol.grid(row=0, column=1)
        SchermateGUI.exit_button_with_text(root, exit_text)
        root.mainloop()




    ######         schermata che appare dopo aver cliccato sul pulsante IMPOSTAZIONI nel MENUPRINCIPALE##########


    '''
###################################################################################################
#############                   FUNZIONI DI SERVIZIO A SEGUIRE                     ################
###################################################################################################
    '''
############                      funzione che mostra a video un messaggio
############    passatole come parametro per un tempo (in secondi) passato come secondo parametrp
    def show_dialog_with_time(text, time):

        def close(to_close):
            to_close.quit()
            to_close.destroy()

        dialog = Tk()
        dialog.config(bg="orange")
        dialog.geometry("+210+180") # distanza da sinistra e dall'alto del popup
        dialog.overrideredirect(1)   # rimuove la barra che permetterebbe di chiudere la finestra appena creata

        label = Label(dialog, text=text,
                      bg="blue",
                      font=font_piccolo,
                      wraplength=500,
                      bd=10,
                      fg="white",
                      relief=GROOVE
                      )
        label.configure(anchor="center")
        label.pack(expand=True)

        dialog.after(time*1000, close, dialog)
        dialog.mainloop()

    def spegni_con_conferma():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="orange")
        frame = Frame(root)
        frame.config(bg="orange")
        frame.pack()
        label = Label(frame, text="Vuoi spegnere il dispositivo?",
                          bg="orange",
                          width=90, height=4,
                          font=font_piccolo
                          )
        label.pack()


        pulsante_spegni = Button(frame,
                                 text="Spegni",
                                 bg="green",
                                 command=lambda: subprocess.Popen(['shutdown','-h','now']),
                                 font=font_piccolo,
                                 relief="ridge",
                                 bd=20,
                                 activebackground="green")
        pulsante_spegni.config(height=5, width=23)
        pulsante_spegni.pack(side=LEFT)

        pulsante_annulla = Button(frame,
                                  text="Annulla",
                                  bg="firebrick3",
                                  command=lambda: root.destroy(),
                                  font=font_piccolo,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="red")
        pulsante_annulla.config(height=5, width=23)  # altezza 5
        pulsante_annulla.pack(side=RIGHT)


        root.mainloop()
    def elimina_file_con_conferma(nome_file):

        def conferma_eliminazione():
            global asnwer
            asnwer=True
            root.quit()
            root.destroy()

        def annulla_eliminiazione():
            global asnwer
            asnwer=False
            root.quit()
            root.destroy()


        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="orange")

        frame = Frame(root)
        frame.config(bg="orange")
        frame.pack()

        label = Label(frame, text="Vuoi eliminare il file\n"+nome_file+"  ?",
                          bg="orange",
                          width=90, height=1,
                          font=font_medio
                          )
        label.pack()

        pulsante_elimina = Button(frame,
                                  text="Elimina",
                                  bg="green",
                                  command=lambda:conferma_eliminazione(),
                                  font=font_piccolo,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="green")
        pulsante_elimina.config(height=5, width=23)
        pulsante_elimina.pack(side=LEFT)

        pulsante_annulla = Button(frame,
                                  text="Annulla",
                                  bg="firebrick3",
                                  command=lambda:annulla_eliminiazione(),
                                  font=font_piccolo,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="red")
        pulsante_annulla.config(height=5, width=23)  # altezza 5
        pulsante_annulla.pack(side=RIGHT)

        root.mainloop()
########## funzione per avere un pulsante di uscita con testo variabile ##############
    def exit_button_with_text(root, text):

        pulstante_uscita = Button(root,
                                  text=text,
                                  command=lambda: root.destroy(),
                                  bg="yellow3",
                                  font=font_piccolo,
                                  bd=20,
                                  activebackground="yellow3")
        pulstante_uscita.config(height=3, width=10)
        pulstante_uscita.pack(side=BOTTOM, fill=BOTH)

########## funzione per avere un pulsante di ritorno al menu ptincipale ##############
    def pulsante_torna_menu_principale(root):

        pulstante_uscita = Button(root,
                                  text="Torna al menu principale",
                                  command=lambda: SchermateGUI.menu_principale(),
                                  bg="green",
                                  font=font_piccolo,
                                  bd=20,
                                  activebackground="green")
        pulstante_uscita.config(height=2, width=25)
        pulstante_uscita.pack(side=BOTTOM, fill=BOTH)

        root.destroy()

########## questa funzione permette di creare un bottone#########à
########## i parametri richiesti per la creazione del bottone sono: -frame su cui il bottone verrà applicato
##########                                                          -testo che apparirà sul bottone
    def bottom_with_text(frame, text):
        pulsante = Button(frame,
                          text=text,
                          bg="green",
                          relief="ridge",
                          font=font_piccolo,
                          bd=20,
                          command=lambda: SchermateGUI.show_file(text.replace("Pulsante ", " ")),
                          activebackground="green",
                          activeforeground="black")

        pulsante.config(width=20, height=3)
        return pulsante

    def button_USB_key(frame, mod, nome_chiavetta, path_origine, path_destinzaione):

        pulsante = Button(frame, text=nome_chiavetta,
                          bg="yellow",
                          font=font_piccolo,
                          bd=20,
                          activebackground="DarkOrange1",
                          command=lambda: SchermateGUI.show_and_select_item_from_path(mod, path_origine, path_destinzaione)
                          )
        pulsante.config(width=40, height=3)
        return pulsante

#####        schermata che appare DOPO aver cliccato uno dei pulsatni della lista
#####        che vengono mostrati DOPO aver cliccato il pulsante ASSOCIA nel MENUPRINCIPALE
#####        richiede come parametro l'ID del pulsante che ha richiamato questa funzione
#####        parametro necessario per un trackback
    def show_file(idButton):

        ###############  funzione di servizio interna#####
        ###############   permette di fare l'associazione di un fileAudio dato un ID di un pulsante
        def bind_button(id,root):
            song_name = mylist.get('active')
            fm.bind(song_name, id)
            root.destroy()

        #############    elimina l'elemento selezionato dopo aver chiesto all'utente      #########
        def delete_item(root):
            global asnwer
            song_name = mylist.get('active')
            SchermateGUI.elimina_file_con_conferma(song_name)
            #asnwer = tkinter.messagebox.askquestion('Attenzione', 'Vuoi eliminare il file:   '+song_name+'  ?',
             #                                       parent=root)
            if asnwer == True:
                
                os.remove(os.path.join(path_che_simula_la_memoria_interna_del_raspberry, song_name))
                fm.delete_element_from_list(song_name)



            #SchermateGUI.show_file(idButton)
            #root.destroy()
##############   END OF delete_item ####################
            
        root = Tk()
        root.attributes('-fullscreen', True)

        dirs = os.listdir(path_che_simula_la_memoria_interna_del_raspberry)
        dirs.sort()
        scrollbar = Scrollbar(root)
        scrollbar.config(width = 70)
        scrollbar.pack(side=LEFT, fill=Y)

        mylist = Listbox(root, yscrollcommand=scrollbar.set, font=font_piccolo, bg="pale green")  # , selectmode=EXTENDED)

        # ciclo for che aggiunge alla linkBox tutti i file con una determinata estenzione
        for file in dirs:
            #if file.endswith(): #------>>  all'interno degli apici inserire l'estenzione voluta ex: .wav
                mylist.insert(END, file)

        mylist.pack(side=LEFT, fill=BOTH, expand=1, )
        scrollbar.config(command=mylist.yview)

        ##### pulsante che si trova alla destra della lista di file audio NELLA schermata  ASSOCIA
        pulstante_associa_fileAudio = Button(root,
                                             text="Scegli il file \n"
                                        "che vuoi associare\n "
                                        "al Pulsante"+idButton+"\n"
                                        "e poi clicca qui \n"
                                             ,
                                             command=lambda: bind_button(idButton, root),
                                             bg="green",
                                             font=font_piccolo,
                                             bd=20,
                                             activebackground="green")
        pulstante_associa_fileAudio.config(height=5, width=25)
        pulstante_associa_fileAudio.pack(side=TOP, fill=BOTH)

        ##### pulsante per eliminare i file audio selezionati     ###############
        pulstante_elimina_fileAudio = Button(root,
                                             text="Scegli il file \n"
                                        "che vuoi eliminare\n"
                                        "e clicca qui",
                                             command=lambda :delete_item(root),
                                             bg="red",
                                             bd=20,
                                             activebackground="red",
                                             font=font_piccolo)
        pulstante_elimina_fileAudio.config(height=4, width=25)
        pulstante_elimina_fileAudio.pack( fill=BOTH)

        SchermateGUI.exit_button_with_text(root, "Torna alla lista pulsanti")

####### funzione che permette di avere un menu a cascata con la funzione di uscire dal main program ##########
    def menu_cascata_con_exit(master):
        master.option_add('*tearOff', FALSE)
        menu=Menu(master, font=font_medio, bg="pale green",)
        master.config(menu=menu)

        subMenu = Menu(menu, font=font_medio, bg="pale green",)
        menu.add_cascade(label="Impostazioni", font=font_medio, menu=subMenu, )  # menu a cascata
        #subMenu.add_command(label="Nuovo utente",font_piccolo=font_piccolo, command=lambda :Signup())
        #subMenu.add_command(label="Accedi",font_piccolo=font_piccolo, command=lambda :Login())
        subMenu.add_separator()                                 #riga di separazione
        subMenu.add_command(label="Volume     ", font=font_medio, command=SchermateGUI.impostazioni)
        subMenu.add_separator()
        subMenu.add_command(label="Spegni    ", font=font_medio, command=lambda: SchermateGUI.spegni_con_conferma())

        subMenu.add_separator()
        subMenu.add_command(label="Chiudi programma", font=font_medio, command=master.destroy)
        subMenu.add_separator()
############   schermata che stampa a video i file contenuti in un determinato path     ###############à
    def show_and_select_item_from_path(mod, path_origine, path_destinzaione):

            ######    funzione che copia la lista dei file selizionati in un'altra directory
            ######    dall'utente nella schermata IMPORTA, dopo aver cliccato sul pulsante
            ######    avnte la scritta, appunto IMPORTA
        def select_items_and_copy(root):

            selected = [mylist.get(idx) for idx in mylist.curselection()]


            SchermateGUI.show_dialog_with_time("L'operazione potrebbe richedere alcuni istanti...",2)
            #### ciclo che copia tutti i file selezionati dall'utente
            for file in selected:

                fm.copy_file_from_path_to_another(mydict[file], path_destinzaione)

            SchermateGUI.show_dialog_with_time("Operazione conclusa con successo",2)
            root.destroy()
            #######                 END OF select_items_and_copy    ###################

        root = Tk()
        root.attributes('-fullscreen', True)
        formats = [".mp3", ".wav", ".wma", ".ogg", ".flac"]
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=LEFT, fill=Y)
        mylist = Listbox(root, yscrollcommand=scrollbar.set, selectmode=MULTIPLE, font=font_piccolo, bg="pale green")
        mydict = {}

        for radice, cartelle, files in os.walk(path_origine, topdown=False):
            for name in files:
                for tipo in formats:
                    if tipo in name:
                        temp_str = os.path.join(radice, name)
                        mydict[name] = temp_str
                        mylist.insert(END, name)
        mylist.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.config(width = 70, command=mylist.yview)
        SchermateGUI.exit_button_with_text(root, "Indietro")

##########        caratteristiche pulsante IMPORTA/ESPORTA        ######################
        testo_pulsante="Seleziona i file \nche desideri "+mod+"\ne poi clicca qui"
        pulstante_importa = Button(root,
                                   text=testo_pulsante,
                                   bg="spring green",
                                   command=lambda: select_items_and_copy(root),
                                   font=font_piccolo,
                                   bd=40,
                                   activebackground="green3")
        pulstante_importa.config(height=10, width=20)
        pulstante_importa.pack(side=TOP, fill=BOTH)

        root.mainloop()

#SchermateGUI.menu_principale()
