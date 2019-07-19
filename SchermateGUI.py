
'''###########    cambiare il path per poter utilizzare il programma sul proprio PC    ###################'''
'''##############################################################################################################'''

pathCheSimulaChiavetta = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudiofromChiavetta"
pathCheSimulaLaMemoriaInternaDelRaspberry = r"C:\Users\yari7\Downloads\UNIBS\IEEE\Projects\Blindo\fileAudioRSPmemory"

'''##############################################################################################################'''



'''
######                            ATTENZIONE                                              ###########
######              ABILITARE QUESTO IMPORT PER UTILIZZARE IL SW SUL RASPBERRY            ###########

import GPIOmanaging
import registrazione as Reg
from recode_audio import Recoding

#######                            ATTENZIONE                                                     ##########
#######       i path sottostanti servono quando si utiliza il Raspberry                           ##########
#######     in questo caso bisogna commentare i path sovrastanti e abilitare quelli sottostanti   ##########
pathCheSimulaChiavetta = "/media/pi"
pathCheSimulaLaMemoriaInternaDelRaspberry = "/home/pi/Documents/fileAudio"
##########################################################################################
'''
###########                 caratteristiche grafiche di default             #######################



import tkinter.messagebox
from tkinter import *
import fileManaging as fm      ##################
import os
import GUIkeyboard as key
import subprocess


stopper=None
recording=False
fontSize = 20
fontStile = "Helvetica"
font = (fontStile, fontSize)
exit_text= "Torna al menu principale"

############                 numero di pulsanti collegati                   ######################
number_of_phisical_button=6
#################################################################################################

name_recoded_file= "/reg.wav"

class SchermateGUI:

############ schermata del MENUPRINCIPALE ###################à
    def menu_principale():
        
        root = Tk()
        root.config(bg="pale green")
        #root.geometry("800x480")
        root.attributes('-fullscreen', True)

        frame = Frame(root)

    ##########   caratteristiche dei quattro pulsanti del menu Principale    ###########
        pulsante_registra= Button(frame,
                                text="Registra",
                                bg="orange" ,
                                command=SchermateGUI.registra,
                                font = font,
                                relief="ridge",
                                bd=20,
                                activebackground="orange")
                                #activeforeground="blue")
        pulsante_registra.grid(row=0, column=0)
        pulsante_registra.config(height=5, width=22)


        pulsante_importa_esporta = Button(frame,
                                 text="Importa/Esporta ",
                                 bg="red",
                                 command=SchermateGUI.esporta_importa,
                                 font = font,
                                 relief="ridge",
                                 bd=20,
                                 activebackground="red")
        pulsante_importa_esporta.grid(row=0, column=1)
        pulsante_importa_esporta.config(height=5, width=22)

        pulsante_associa = Button(frame,
                                  text="Associa",
                                  bg="yellow",
                                  command=lambda:SchermateGUI.schermata_pulsanti(root, number_of_phisical_button),
                                  font = font,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="yellow")
        pulsante_associa.grid(row=1, column=0)
        pulsante_associa.config(height=5, width=22)

        pulsante_associazioni = Button(frame,
                                 text="Lista Associazioni",
                                 bg="red3",
                                 command=SchermateGUI.schermata_associazioni,
                                 font = font,
                                 relief="ridge",
                                 bd=20,
                                 activebackground="red3")
        pulsante_associazioni.grid(row=1, column=1)
        pulsante_associazioni.config(height=5, width=22)

      #SchermateGUI.exit_button_with_text(root,"Chiudi il programma")

        ######################   metodo che importa il menu a cascata in qst menu principale###############
        SchermateGUI.menu_cascata_con_exit(root)

        frame.pack()
        root.mainloop()  # funzione che continua a tenere aperto la finetra principale


    """
################################################################################################################
###################                 funzioni che aprono le varie schermate                       ###############
################################################################################################################
    """

#########    schermata che appare dopo aver cliccato sul pulsante REGISTRA nel MENUPRINCIPALE##########
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
                      width=90, height=4,
                      font=font
                      )
        label.pack()

            
        ##########              funzione che fa partire la registrazione
        def start_recoding(name_recoded_file):
            
            global recording
            global stopper
            global new_name

            recording=True

            label["text"] = "Registrazione in corso.....\nPremi il pulsante rosso per interrompere"

            final_path= pathCheSimulaLaMemoriaInternaDelRaspberry + name_recoded_file
            stopper = Reg.start(final_path)

        #########   funzione che ferma la registrazione
        def stop_recording():
            global stopper
            global recording

            if recording:
                
                Reg.stop(stopper) 
                label["text"] = "Registrazione effettuata con successo!"
                
                new_name=key.keyBoard()

                initial=pathCheSimulaLaMemoriaInternaDelRaspberry+"/reg.wav"
                final=pathCheSimulaLaMemoriaInternaDelRaspberry +"/" +new_name+".wav"
                
                os.rename(initial,final)
                recording=False
                label["text"] ="Premi su Start per registrare"

            else:
                tkinter.messagebox.showinfo("Attenzione","La registrazione non è ancora partita, premi sul pulsante verde",parent=root)

        pulsante_play = Button(frame,
                               text="Inizia a registrare",
                               bg="green",
                               command=lambda: start_recoding(name_recoded_file),
                               font=font,
                               relief="ridge",
                               bd=20,
                               activebackground="green")
        pulsante_play.config(height=5, width=23)
        pulsante_play.pack(side=LEFT)

        pulsante_stop = Button(frame,
                               text="Interrompi la registrazione",
                               bg="firebrick3",
                               command=lambda: stop_recording(),
                               font=font,
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
                      width=90, height=4,
                      font=font
                      )
        label.pack();

        pulsante_importa = Button(frame,
                                  text="Importa",
                                  bg="Dark orange2",
                                  command=lambda:scegli_chiavetta_importa(),
                                  font=font,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="Dark orange2")
        pulsante_importa.pack(side=LEFT)
        pulsante_importa.config(height=5, width=22)

        pulsante_esporta = Button(frame,
                                  text="Esporta",
                                  bg="yellow",
                                  command=lambda:scegli_chiavetta_esporta(),
                                  font=font,
                                  relief="ridge",
                                  bd=20,
                                  activebackground="yellow")
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
            dirs = os.listdir(pathCheSimulaChiavetta)

            label = Label(frame, text="Selezionare la chiavetta su cui esportare i file audio",
                          bd=20,
                          bg="DarkOrange1",
                          font=font)
            label.grid(row=1, column=0)
            label.config(width=50, height=3)

            index = 2

            for cartella in dirs:
                path_chiavetta = os.path.join(pathCheSimulaChiavetta, cartella)
                pulsante = SchermateGUI.bottom_USB_key(frame, "esporare", cartella,
                                                       pathCheSimulaLaMemoriaInternaDelRaspberry, path_chiavetta)
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
            dirs = os.listdir(pathCheSimulaChiavetta)

            label = Label(frame, text="Selezionare la chiavetta da dove importare i file audio",
                          bd=20,
                          bg="DarkOrange1",
                          font=font)
            label.grid(row=1, column=0)
            label.config(width=50, height=3)

            index = 2
            for cartella in dirs:
                path_chiavetta = os.path.join(pathCheSimulaChiavetta, cartella)
                pulsante = SchermateGUI.bottom_USB_key(frame, "importare", cartella, path_chiavetta,
                                                       pathCheSimulaLaMemoriaInternaDelRaspberry)
                pulsante.grid(row=index, column=0)
                index += 1

            SchermateGUI.exit_button_with_text(root, exit_text)

            root.mainloop()
            ############ end of scegli_chiavetta_importa

        SchermateGUI.exit_button_with_text(root, exit_text)
        root.mainloop()


    ############  schermata che appare dopo aver cliccato il pulsante ASSOCIAZIONI nel MENU PRINCIPALE
    def schermata_associazioni():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="DarkOrange1")

        frame = Frame(root)
        frame.config(bg="DarkOrange1")

        label_memo =Label(frame,text="Questi sono le associazioni che hai precedentemente fatto\nScorri per vederle tutte",
                            font=font,
                            bg="DarkOrange1",
                            bd=20,
                            width=200,
                            height=2)
        label_memo.pack(side=TOP)
        sorted_list = fm.giveSortedList()

        my_list= Listbox(root, #yscrollcommand = scrollbar.set ,
                              font=font,
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
                                  font = font,
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


    ######         schermata che appare dopo aver cliccato sul pulsante IMPOSTAZIONI nel MENUPRINCIPALE##########
    def impostazioni():
        current_volume = fm.giveVolume()
            ##### funzioni di servizio che cambiano il volume e aggiornano il suo valore che è stampato all'utente
        def changeVolumeOnDisplay():
            label.configure(text=fm.giveVolume())

        def IncreseAndChange():
            fm.increseVol()
            changeVolumeOnDisplay()


        def DecreseAndChange():
            fm.decreseVol()
            changeVolumeOnDisplay()

        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="Dark orange2")
        frame = Frame(root)
        frame.config(bg="Dark orange2")
        frame.pack()
        buttonColor="orange"

    ######## stampa del valore del volume in un intervallo 10-100
        label = Label(frame,
                      text=current_volume,
                      font=font
                      ,bg=buttonColor,
                      activebackground=buttonColor,
                      relief="ridge",
                        bd=20)
        label.grid(row=2, column=0,columnspan=3)
        label.config(width=40,heigh=2)

        pulsante_vol = Button(frame,      #pulsante per diminuire il volume
                              text="-",
                              font = font,
                              command=DecreseAndChange,
                              bg=buttonColor,
                                relief="ridge",
                                bd=20,
                      activebackground=buttonColor)
        pulsante_vol.grid(row=0)
        pulsante_vol.config(height=3, width=5)

        pulsante_vol = Button(frame,      #pulsante per aumentare il volume
                              text="+",
                              font = font,
                              command=IncreseAndChange,
                              bg=buttonColor,
                      activebackground=buttonColor,
                                relief="ridge",
                                bd=20)
        pulsante_vol.grid(row=0, column=2)
        pulsante_vol.config(height=3, width=5)

        scritta_vol = Label(frame, text="volume",
                            height=3, width=20,
                            font = font,
                            bg=buttonColor,
                      activebackground=buttonColor,
                                relief="ridge",
                                bd=20)
        scritta_vol.grid(row=0, column=1)
        SchermateGUI.exit_button_with_text(root, exit_text)
        root.mainloop()


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
        dialog.geometry("+700+400")
        dialog.overrideredirect(1)

        label = Label(dialog, text=text,
                          bg="orange",
                          font=font,
                          wraplength=200,
                          bd=20
                      )
        label.configure(anchor="center")
        label.pack(expand=True)

        dialog.after(time*1000, close, dialog)
        dialog.mainloop()

########## funzione per avere un pulsante di uscita con testo variabile ##############
    def exit_button_with_text(root, text):

        pulstante_uscita = Button(root,
                                  text=text,
                                  command=lambda: root.destroy(),
                                  bg="yellow3",
                                  font=font,
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
                                  font=font,
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
                          font=font,
                          bd=20,
                          command=lambda: SchermateGUI.show_file(text.replace("Pulsante ", " ")),
                          activebackground="green",
                          activeforeground="black")

        pulsante.config(width=20, height=3)
        return pulsante

    def bottom_USB_key(frame, mod, nome_chiavetta, path_origine, path_destinzaione):

        pulsante = Button(frame, text=nome_chiavetta,
                          bg="yellow",
                          font=font,
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

        ###############  piccola funzione di servizio interna#####
        ###############   permette di fare l'associazione di un fileAudio dato un ID di un pulsante
        def bind_button(id,root):
            song_name = mylist.get('active')
            fm.bind(song_name, id)
            root.destroy()

        #############    elimina l'elemento selezionato dopo aver chiesto all'utente      #########
        def delete_item(root):
            song_name = mylist.get('active')
            asnwer = tkinter.messagebox.askquestion('Attenzione', 'Vuoi eliminare il file:   '+song_name+'  ?',
                                                    parent=root)
            if asnwer == 'yes':
                
                os.remove(pathCheSimulaLaMemoriaInternaDelRaspberry+"/"+song_name)
                fm.deleteElementFromList(song_name)

            SchermateGUI.show_file(idButton)
            root.destroy()
##############   END OF delete_item ####################
            
        root = Tk()
        root.attributes('-fullscreen', True)

        dirs = os.listdir(pathCheSimulaLaMemoriaInternaDelRaspberry)
        dirs.sort()
        scrollbar = Scrollbar(root)
        scrollbar.config(width = 70)
        scrollbar.pack(side=LEFT, fill=Y)

        mylist = Listbox(root, yscrollcommand=scrollbar.set, font=font,bg="pale green")  # , selectmode=EXTENDED)

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
                                   font=font,
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
                                   font=font)
        pulstante_elimina_fileAudio.config(height=4, width=25)
        pulstante_elimina_fileAudio.pack( fill=BOTH)

        SchermateGUI.exit_button_with_text(root, "Torna alla lista pulsanti")

####### funzione che permette di avere un menu a cascata con la funzione di uscire dal main program ##########
    def menu_cascata_con_exit(master):
        def spegni():
            asnwer = tkinter.messagebox.askquestion('Attenzione', 'Vuoi spegnere il dispositivo?',
                                                    parent=master)
            if asnwer == 'yes':

                messagebox.showwarning("Attenzione","Ricordati di spegnere l'interruttore appena lo schermo diventa nero")
                subprocess.Popen(['shutdown','-h','now'])
                


        menu=Menu(master,font=font,bg="pale green")
        master.config(menu=menu)

        subMenu = Menu(menu,font=font,bg="pale green")
        menu.add_cascade(label="Impostazioni" ,font=font,menu=subMenu,)  # menu a cascata
        #subMenu.add_command(label="Nuovo utente",font=font, command=lambda :Signup())
        #subMenu.add_command(label="Accedi",font=font, command=lambda :Login())
        subMenu.add_separator()                                 #riga di separazione
        subMenu.add_command(label="     Volume     ",font=font, command=SchermateGUI.impostazioni)
        subMenu.add_separator()
        subMenu.add_command(label="     Spegni    ",font=font, command=lambda: spegni())

        subMenu.add_separator()
        subMenu.add_command(label="Chiudi programma",font=font, command=master.destroy)

############   schermata che stampa a video i file contenuti in un determinato path     ###############à
    def show_and_select_item_from_path(mod, path_origine, path_destinzaione):

            ######    funzione che copia la lista dei file selizionati in un'altra direcctory
            ######    dall'utente nella schermata IMPORTA, dopo aver cliccato sul pulsante
            ######    avnte la scritta, appunto IMPORTA
        def select_items_and_copy(root):

            selected = [mylist.get(idx) for idx in mylist.curselection()]

            #### ciclo che copia tutti i file selezionati dall'utente

            for file in selected:
                
                fm.copyFileFromPathToAnother(mydict[file],path_destinzaione)

            SchermateGUI.show_dialog_with_time("Operazione conclusa con successo",2)

            root.destroy()
        ###########                 END OF select_items_and_copy

        root = Tk()
        root.attributes('-fullscreen', True)
        formats = [".mp3", ".wav", ".wma", ".ogg", ".flac"]
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=LEFT, fill=Y)
        mylist = Listbox(root, yscrollcommand=scrollbar.set, selectmode=MULTIPLE, font=font,bg="pale green")
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

##########        caratteristiche pulsante IMPORTA        ######################
        testo_pulsante="Seleziona i file \nche desideri "+mod+"\ne poi clicca qui"
        pulstante_importa = Button(root,
                                   text=testo_pulsante,
                                   bg="spring green",
                                   command=lambda: select_items_and_copy(root),
                                   font=font,
                                   bd=40,
                                   activebackground="green3")
        pulstante_importa.config(height=10, width=20)
        pulstante_importa.pack(side=TOP, fill=BOTH)

        root.mainloop()

SchermateGUI.menu_principale()
