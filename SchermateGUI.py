
#from recode_audio import Recoding
import tkinter.messagebox
from tkinter import filedialog
from tkinter import *
import fileManaging as fm      ##################
import os
import GUIkeyboard as key
import time
import registrazione as Reg
import subprocess
import shutil
from time import gmtime,strftime
from threading import Thread,Lock

os.chdir("/home/pi/Desktop/Main/")
#print(os.getcwd())
###########    cambiare il path per poter utilizzare il programma sul proprio PC    ###################
#pathCheSimulaChiavetta = r"C:\Users\Massimiliano\Desktop\Nuova cartella"
#pathCheSimulaLaMemoriaInternaDelRaspberry = r"C:\Users\Massimiliano\Desktop\Blindo"
##########################################################################################
stopper=None
recording=False
#'''
######                            ATTENZIONE                                              ###########
######              ABILITARE QUESTO IMPORT PER UTILIZZARE IL SW SUL RASPBERRY            ###########

import GPIOmanaging
import registrazione as Reg

#######                            ATTENZIONE                                                     ##########
#######       i path sottostanti servono quando si utiliza il Raspberry                           ##########
#######     in questo caso bisogna commentare i path sovrastanti e abilitare quelli sottostanti   ##########
pathCheSimulaChiavetta = "/media/pi"
pathCheSimulaLaMemoriaInternaDelRaspberry = "/home/pi/Documents/fileAudio"
##########################################################################################
#'''
###########                 caratteristiche grafiche di default             #######################
fontSize = 20
fontStile = "Helvetica"
font = (fontStile, fontSize)
scrittaUscita="Torna al menu principale"

############                 numero di pulsanti collegati                   ######################
numberOfButton=6
#################################################################################################
nomeFile="/reg.wav"

########  classe contenente tutte le schermate che verranno riprodotte dal programma ##########

class Lancio(Thread):

    def __init__(self,nome):
        
        Thread.__init__(self)
        self.nome = nome
        
    def run(self):

        shutil.move("/home/pi/Documents/fileAudio/reg.wav",
                    "/home/pi/Documents/nomeCambiato.wav")

class SchermateGUI:


########        variablile globale per sapere il path da dove prelevare i file audio (chiesto all'utente)
    finalPath=""

############ schermata del MENUPRINCIPALE ###################à
    def MenuPrincipale():
        
        root = Tk()
        root.config(bg="pale green")
        

        #root.geometry("800x480")
        root.attributes('-fullscreen', True)


        frame = Frame(root)

    ##########   caratteristiche dei quattro pulsanti del menu Principale    ###########
        pulsanteRegistra= Button(frame,
                                text="Registra",
                                bg="orange" ,
                                command=SchermateGUI.registra,
                                font = font,
                                relief="ridge",
                                bd=20,
                                activebackground="orange")
                                #activeforeground="blue")
        pulsanteRegistra.grid(row=0, column=0)
        pulsanteRegistra.config(height=5, width=22)


        pulsanteImporta = Button(frame,
                                 text="Importa File ",
                                 bg="red",
                                 command=SchermateGUI.scegliChiavetta,
                                 font = font,
                                 relief="ridge",
                                 bd=20,
                                 activebackground="red")
        pulsanteImporta.grid(row=0, column=1)
        pulsanteImporta.config(height=5, width=22)

        pulsanteAssocia = Button(frame,
                                 text="Associa",
                                bg="yellow" ,
                                 command=lambda:SchermateGUI.schermataPulsanti(root,numberOfButton),
                                 font = font,
                                 relief="ridge",
                                 bd=20,
                                 activebackground="yellow")
        pulsanteAssocia.grid(row=1, column=0)
        pulsanteAssocia.config(height=5, width=22)

        pulsanteAssociazioni = Button(frame,
                                 text="Lista Associazioni",
                                 bg="red3",
                                 command=SchermateGUI.schermataAssociazioni,
                                 font = font,
                                 relief="ridge",
                                 bd=20,
                                 activebackground="red3")
        pulsanteAssociazioni.grid(row=1, column=1)
        pulsanteAssociazioni.config(height=5, width=22)
      #
      #SchermateGUI.pulsanteUscitaConTesto(root,"Chiudi il programma")

        ######################   metodo che importa il menu a cascata in qst menu principale###############
        SchermateGUI.menuCascataConExit(root)

        frame.pack()
        #os.rename("lista finale","cambiato!")
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
        
        
        def giveTime():
            datetime.datetime.now()
        def chooseName():
            global newName
            newName=key.keyBoard()
        
            
        ##########              funzione che fa partire la registrazione
        def startRecoding(nameRecodedFile):
            
            global recording
            global stopper
            global newName
            recording=True
            label["text"] = "Registrazione in corso.....\nPremi il pulsante rosso per interrompere"

            #date= strftime("%m-%d %H:%M:%S")
            finalPath=pathCheSimulaLaMemoriaInternaDelRaspberry+ nomeFile
            #finalPath=pathCheSimulaLaMemoriaInternaDelRaspberry + "/" + nameRecodedFile+date+".wav"

            stopper = Reg.start(finalPath)  

        #########               funzione che ferma la registrazione
        def stopRecording():
            global stopper
            global recording

            if recording:
                
                Reg.stop(stopper) 
                label["text"] = "Registrazione effettuata con successo!"
                
                newName=key.keyBoard()
                initial=pathCheSimulaLaMemoriaInternaDelRaspberry+"/reg.wav"
                final=pathCheSimulaLaMemoriaInternaDelRaspberry +"/" +newName+".wav"
                
                os.rename(initial,final)
                recording=False
                label["text"] ="Premi su Start per registrare"
                
            
            else:
                tkinter.messagebox.showinfo("Attenzione","La registrazione non è ancora partita, premi sul pulsante verde",parent=root)
            
         

        pulsante_play = Button(frame,
                               text="Inizia a registrare",
                               bg="green",
                               command=lambda: startRecoding(nomeFile),
                               font=font,
                               relief="ridge",
                               bd=20,
                               activebackground="green")

        pulsante_play.config(height=5, width=23)
        pulsante_play.pack(side=LEFT)
        

        pulsante_stop = Button(frame,
                               text="Interrompi la registrazione",
                               bg="firebrick3",
                               command=lambda: stopRecording(),
                               font=font,
                               relief="ridge",
                               bd=20,
                               activebackground="red")
        pulsante_stop.config(height=5, width=23) #altezza 5
        pulsante_stop.pack(side=RIGHT)

       
        SchermateGUI.pulsanteUscitaConTesto(root, scrittaUscita)
        
               
        root.mainloop()
        

##########         schermata che appare dopo aver cliccato sul pulsante IMPORTA nel MENUPRINCIPALE##########
    def scegliChiavetta():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="DarkOrange1")
        frame=Frame(root,bg="DarkOrange1")
        frame.pack()
        dirs = os.listdir(pathCheSimulaChiavetta)  # passo alla funzione pi\media e quindi verranno visualizzate a schermo le chiavette disponibili

        label = Label(frame, text="Selezionare la chiavetta da dove importare i file audio",
                      bd=20,
                      bg="DarkOrange1",
                      font=font)
        label.grid(row=1, column=0)
        label.config(width=50, height=3)

        index = 2
        for cartella in dirs:
            pulsante = SchermateGUI.pulsanteChiavetta(frame, cartella)
            pulsante.grid(row=index, column=0)
            index += 1

        SchermateGUI.pulsanteUscitaConTesto(root,scrittaUscita)

        root.mainloop()

    ############  schermata che appare dopo aver cliccato il pulsante ASSOCIAZIONI nel MENU PRINCIPALE
    def schermataAssociazioni():
        root = Tk()
        root.attributes('-fullscreen', True)
        root.config(bg="DarkOrange1")
        frame = Frame(root)
        frame.config(bg="DarkOrange1")

        labelMemo =Label(frame,text="Questi sono le associazioni che hai precedentemente fatto\nScorri per vederle tutte",
                            font=font,
                            bg="DarkOrange1",
                            bd=20,
                            width=200,
                            height=2

                            )
        labelMemo.pack(side=TOP)
        sortedList = fm.giveSortedList()

        #scrollbar = Scrollbar(root,width=35)
        #scrollbar.pack(side=LEFT, fill=Y)

        myList= Listbox(root, #yscrollcommand = scrollbar.set ,
                              font=font,
                              width=90, height=8,
                              bg="DarkOrange1",
                              
                              activestyle="none")


        for audio in sortedList:
            myList.insert(END,audio)


        frame.pack()
        myList.pack()
        #scrollbar.config(command=myList.yview)

        SchermateGUI.pulsanteUscitaConTesto(root,scrittaUscita)
        root.mainloop()

##########à Schermata che appare dopo aver cliccato su ASSOCIA nel MENU PRINCIPALE
    def schermataPulsanti(closingroot, numberOfButton):
        
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
        for i in range(numberOfButton):
            pulsante = SchermateGUI.pulsanteTesto(frame, "Pulsante "+ str(i+1))
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
        root.config(bg="pale green")
        frame = Frame(root)
        frame.config(bg="pale green")
        frame.pack()
        buttonColor="pale green"

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


        '''
        pulsante_lum = Button(frame, text="-",
                              font = font,
                              bg=buttonColor,
                      activebackground=buttonColor,
                                relief="ridge",
                                bd=20)
        pulsante_lum.grid(row=1, column=0)
        pulsante_lum.config(height=3, width=5)

        pulsante_lum = Button(frame,
                              text="+",
                              font = font,
                              bg=buttonColor,
                      activebackground=buttonColor,
                                relief="ridge",
                                bd=20)
        pulsante_lum.grid(row=1, column=2)
        pulsante_lum.config(height=3, width=5)

        scritta_lum = Label(frame,
                            text="luminosità",
                            height=3, width=20,
                            font = font,
                            bg=buttonColor,
                      activebackground=buttonColor,
                                relief="ridge",
                                bd=20)
        scritta_lum.grid(row=1, column=1)
        '''
        SchermateGUI.pulsanteUscitaConTesto(root,scrittaUscita)

        root.mainloop()
    '''
###################################################################################################
#############                   FUNZIONI DI SERVIZIO A SEGUIRE                     ################
###################################################################################################
    '''
########## funzione per avere un pulsante di uscita con testo variabile ##############
    def pulsanteUscitaConTesto(root,text):

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
    def pulsanteTornaMenuPrincipale(root):

        pulstante_uscita = Button(root,
                                  text="Torna al menu principale",
                                  command=lambda: SchermateGUI.MenuPrincipale(),
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
    def pulsanteTesto(frame, text):#, row, column):
        pulsante = Button(frame,
                          text=text,
                          bg="green",
                          relief="ridge",
                          font=font,
                          bd=20,
                          command=lambda: SchermateGUI.showFile(text.replace("Pulsante ", " ")),
                          activebackground="green",
                          activeforeground="black")

        pulsante.config(width=20, height=3)
        return pulsante

    def pulsanteChiavetta(frame, text):
        temp_text = os.path.join(pathCheSimulaChiavetta, text)
        pulsante = Button(frame, text=text,
                          bg="yellow",
                          font=font,
                          bd=20,
                          activebackground="DarkOrange1",
                          command=lambda: SchermateGUI.showAndSelectItemfromPath(temp_text)
                          )
        pulsante.config(width=40, height=3)
        return pulsante

#####        schermata che appare DOPO aver cliccato uno dei pulsatni della lista
#####        che vengono mostrati DOPO aver cliccato il pulsante ASSOCIA nel MENUPRINCIPALE
#####        richiede come parametro l'ID del pulsante che ha richiamato questa funzione
#####        parametro necessario per un trackback
    def showFile(idButton):

        ###############  piccola funzione di servizio interna#####
        ###############   permette di fare l'associazione di un fileAudio dato un ID di un pulsante
        def bindButton(id,root):
            songName = mylist.get('active')
            fm.bind(songName, id)
            root.destroy()

        #############    elimina l'elemento selezionato dopo aver chiesto all'utente      #########
        def deleteItem(root):
            songName = mylist.get('active')
            asnwer = tkinter.messagebox.askquestion('Attenzione', 'Vuoi eliminare il file:   '+songName+'  ?',
                                                    parent=root)
            if asnwer == 'yes':
                
                os.remove(pathCheSimulaLaMemoriaInternaDelRaspberry+"/"+songName)
                fm.deleteElementFromList(songName)

           
            #mylist.update()
            SchermateGUI.showFile(idButton)
            root.destroy()

        
            

            
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
                                   command=lambda: bindButton(idButton, root),
                                   bg="green",
                                   font=font,
                                   bd=20,
                                   activebackground="green"
                                             )

        pulstante_associa_fileAudio.config(height=5, width=25)
        pulstante_associa_fileAudio.pack(side=TOP, fill=BOTH)

        ##### pulsante per eliminare i file audio selezionati     ###############
        pulstante_elimina_fileAudio = Button(root,
                                   text="Scegli il file \n"
                                        "che vuoi eliminare\n"
                                        "e clicca qui",
                                   command=lambda :deleteItem(root),
                                   bg="red",
                                   bd=20,
                                   activebackground="red",
                                   font=font)

        pulstante_elimina_fileAudio.config(height=4, width=25)
        pulstante_elimina_fileAudio.pack( fill=BOTH)

        SchermateGUI.pulsanteUscitaConTesto(root,"Torna alla lista pulsanti")

####### funzione che permette di avere un menu a cascata con la funzione di uscire dal main program ##########
    def menuCascataConExit(master):
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
        #subMenu.add_command(label="Chiudi programma",font=font, command=master.destroy)

############   schermata che stampa a video i file contenuti in un determinato path     ###############à
    def showAndSelectItemfromPath(path):

            ######    funzione che copia la lista dei file selizionati in un'altra direcctory
            ######    dall'utente nella schermata IMPORTA, dopo aver cliccato sul pulsante
            ######    avnte la scritta, appunto IMPORTA
        def selectItemsAndCopy(root):
            #pulstante_importa["text"] = "Attendere\nCopia in corso"
            selected = [mylist.get(idx) for idx in mylist.curselection()]

            #### ciclo che copia tutti i file selezionati dall'utente
            #pulstante_importa["text"] = "Attendere\nCopia in corso"

            for file in selected:
                
                fm.copyFileFromPathToAnother(mydict[file], pathCheSimulaLaMemoriaInternaDelRaspberry)
               # mylist.itemconfig(index, {'bg': 'green'})

            tkinter.messagebox.showinfo('Operazione conclusa con successo',
                                        'Gli elementi selezionati sono stati correttamente '
                                        'importati nella memoria interna di Blindo',parent=root)
            root.destroy()

            ##### funzione che colora di (rosso) tutti i file mostrati, ora non utilizzata

        root = Tk()
        root.attributes('-fullscreen', True)
        formats = [".mp3", ".wav", ".wma", ".ogg", ".flac"]
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=LEFT, fill=Y)
        mylist = Listbox(root, yscrollcommand=scrollbar.set, selectmode=MULTIPLE, font=font,bg="pale green")
        mydict = {}

        for radice, cartelle, files in os.walk(path, topdown=False):
            for name in files:
                for tipo in formats:
                    if tipo in name:
                        temp_str = os.path.join(radice, name)
                        mydict[name] = temp_str
                        mylist.insert(END, name)
        mylist.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.config(width = 70, command=mylist.yview)
        SchermateGUI.pulsanteUscitaConTesto(root,"Indietro")

##########        caratteristiche pulsante IMPORTA        ######################à
        pulstante_importa = Button(root,
                                   text="Tocca i file che vuoi\n "
                                        "importare nella memoria\n "
                                        "interna di Blindo\n"
                                        "e poi clicca qui ",
                                   bg="spring green",
                                   command=lambda: selectItemsAndCopy(root),
                                   font=font,
                                   bd=40,
                                   activebackground="green3")
        pulstante_importa.config(height=10, width=20)
        pulstante_importa.pack(side=TOP, fill=BOTH)

        root.mainloop()

SchermateGUI.MenuPrincipale()
