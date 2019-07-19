"""
Simple on-screen keyboard using tkinter
Author : Ajinkya Padwad
Version 1.0
"""

from tkinter import *
import tkinter



buttons = [
'1','2','3','4','5','6','7','8','9','0','?',')','-','INVIO',
'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','!','$','£','BACK',
'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','[',']','_','+','!'
,
'z', 'x', 'c', 'v', 'b', 'n', 'm', '_', '.','#','-','-','+',
'SPACE'
]
result=""
def select(value):

	if value == "BACK":
		# allText = entry.get()[:-1]
		# entry.delete(0, tkinter,END)
		# entry.insert(0,allText)

		entry.delete(len(entry.get())-1,tkinter.END)

	elif value == "SPACE":
		entry.insert(tkinter.END, ' ')
	elif value == " Tab ":
		entry.insert(tkinter.END, '    ')
	#elif value == "INVIO":
	else :
		entry.insert(tkinter.END,value)
def close(root):
        
        global result
        result = entry.get()
        root.quit()
        root.destroy()

def HosoPop(kb):

	varRow = 2
	varColumn = 0

	for button in buttons:

		command = lambda x=button: select(x)

		if button == "INVIO":
			tkinter.Button(kb, text=button, width=15,heigh=6, bg="#3c4987", fg="#ffffff",
					   activebackground="#ffffff", activeforeground="#3c4987", relief='raised',
                                               font=("Helvetica",13), padx=1,
					   pady=1, bd=5, command=lambda:close(kb)).grid(row=6,column=0 ,columnspan=3)

		elif button == "SPACE" :
			tkinter.Button(kb, text=button, width=30,heigh=6, bg="#3c4987",
                                       font=("Helvetica",13), fg="#ffffff",
						   activebackground="#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
						   pady=1, bd=5, command=command).grid(row=6,column=1 ,columnspan=9)
		elif button == "BACK" :
			tkinter.Button(kb, text=button, width=15,heigh=6, bg="#3c4987",
                                       font=("Helvetica",13), fg="#ffffff",
						   activebackground="#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
						   pady=1, bd=5, command=command).grid(row=6, column=8,columnspan=3)
		else:
			tkinter.Button(kb,text= button,width=5,heigh=2,
                                       font=("Helvetica",15),bg="#3c4987", fg="#ffffff",
				activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
				pady=1, bd=6,command=command).grid(row=varRow,column=varColumn)


		varColumn +=1

		if varColumn > 13 and varRow == 2:
			varColumn = 0
			varRow+=1
		if varColumn > 13 and varRow == 3:
			varColumn = 0
			varRow+=1
		if varColumn > 13 and varRow == 4:
			varColumn = 0
			varRow+=1



def keyBoard():
	kb = tkinter.Tk()

	kb.attributes('-fullscreen', True)


	label1 = Label(kb,text="Sciegli con che nome vuoi salvare il file",font=("Helvetica",20)).grid(row=0,columnspan=11)

	global entry
	entry = Entry(kb,width=30)
	entry.config(font=("Helvetica",30))
	entry.grid(row=1,columnspan=11)

	HosoPop(kb)


	kb.mainloop()

	return result


