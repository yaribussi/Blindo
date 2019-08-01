"""
Simple on-screen keyboard using tkinter
Author : Ajinkya Padwad
Version 1.0
"""

from tkinter import *
import tkinter
import StaticParameter as SP


buttons = [
'1','2','3','4','5','6','7','8','9','0','(',')','$','CANCELLA',

'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','[',']','€','SALVA',

'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','/','!','?','"',''
,
'z', 'x', 'c', 'v', 'b', 'n', 'm', '_', '-','#','*','+','.',
'SPAZIO'
]
result=""
def select(value):

	if value == "CANCELLA":
		# allText = entry.get()[:-1]
		# entry.delete(0, tkinter,END)
		# entry.insert(0,allText)

		entry.delete(len(entry.get())-1,tkinter.END)

	elif value == "SPAZIO":
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
	key_background = SP.button_background_color
	key_foreground = SP.black
	key_active_background = SP.active_background_color
	key_active_foreground = SP.white
	key_relief = 'raised'
	key_font = SP.font_piccolo

	varRow = 2
	varColumn = 0

	for button in buttons:

		command = lambda x=button: select(x)

		if button == "CANCELLA":
			tkinter.Button(
						kb, text=button, width=15, heigh=6,
						bg=key_background,
						fg=key_foreground,
						activebackground=key_active_background,
						activeforeground=key_active_foreground,
						relief=key_relief,
						font=key_font,
						padx=1, pady=1,
						bd=5,
						command=command).grid(row=6, column=0, columnspan=3)

		elif button == "SPAZIO":
			tkinter.Button(
						kb, text=button, width=30, heigh=6,
						bg=key_background,
						font=key_font, fg=key_foreground,
						activebackground=key_active_background,
						activeforeground=key_active_foreground,
						relief=key_relief,
						padx=1, pady=1,
						bd=5,
						command=command).grid(row=6, column=1, columnspan=9)
		elif button == "SALVA" :
			tkinter.Button(
						kb, text=button, width=15, heigh=6,
						bg=key_background,
						font=key_font,
						fg=key_foreground,
						activebackground=key_active_background,
						activeforeground=key_active_background,
						relief=key_relief,
						padx=1, pady=1,
						bd=5,
						command=lambda: close(kb)).grid(row=6, column=8, columnspan=3)
		else:
			tkinter.Button(
						kb, text=button, width=5, heigh=2,
						font=key_font,
						bg=key_background,
						fg=key_foreground,
						activebackground = key_active_background,
						activeforeground=key_active_foreground,
						relief=key_relief,
						padx=1, pady=1,
						bd=6,
						command=command).grid(row=varRow, column=varColumn)


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
	label_font = ("Helvetica",20)
	label_bg_color = SP.root_background_color
	label_text = "Scegli con che nome vuoi salvare il file"

	entry_font = ("Helvetica",30)
	entry_background = SP.white
	entry_foreground = SP.black
	kb = tkinter.Tk()

	kb.attributes('-fullscreen', True)
	kb.config(bg=SP.root_background_color)
	label_scritta=Label(
						kb,
						text=label_text,
						font=label_font,
						bg=label_bg_color)
	label_scritta.grid(row=0, columnspan=11)

	global entry
	entry = Entry(kb, width=37)
	entry.config(
				font=entry_font,
				bg=entry_background,
				fg=entry_foreground)
	entry.grid(row=1, column=0, columnspan=13)

	HosoPop(kb)


	kb.mainloop()

	return result



#print(keyBoard())