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
		entry.delete(len(entry.get())-1,tkinter.END)

	elif value == "SPAZIO":
		entry.insert(tkinter.END, ' ')
	elif value == " Tab ":
		entry.insert(tkinter.END, '    ')
	else:
		entry.insert(tkinter.END,value)


def close(root):
        global result
        result = entry.get()
        root.quit()
        root.destroy()


def hoso_pop(kb):
	key_background = SP.standard_color_setting("key_button_background")
	key_foreground = SP.button_font_color
	key_active_background = key_background
	key_active_foreground = SP.root_font_color
	key_font = SP.keyboard_key_font

	var_row = 2
	var_column = 0

	for button in buttons:
		command = lambda x=button: select(x)

		if button == "CANCELLA":
			tkinter.Button(
						kb, text=button, width=15, heigh=6,
						bg=SP.standard_color_setting("delete_button_background"),
						fg=key_foreground,
						#activebackground=SP.delete_button_active_background,
						font=key_font,
						padx=1, pady=1,
						bd=5,
						relief=SP.bord_style,
						command=command).grid(row=6, column=0, columnspan=5)

		elif button == "SPAZIO":
			tkinter.Button(
						kb, text=button, width=30, heigh=6,
						bg=key_background,
						font=key_font, fg=key_foreground,
						activebackground=key_active_background,
						activeforeground=key_active_foreground,
						padx=1, pady=1,
						bd=5,
						relief=SP.bord_style,
						command=command).grid(row=6, column=2, columnspan=8)
		elif button == "SALVA":
			tkinter.Button(
						kb, text=button, width=15, heigh=6,
						bg=SP.standard_color_setting("confirm_button_background"),
						font=key_font,
						fg=key_foreground,
						activebackground=SP.standard_color_setting("confirm_button_background"),
						activeforeground=key_active_background,
						padx=1, pady=1,
						bd=5,
						relief=SP.bord_style,
						command=lambda: close(kb)).grid(row=6, column=7, columnspan=5)
		else:
			tkinter.Button(
						kb, text=button, width=5, heigh=2,
						font=key_font,
						bg=key_background,
						fg=key_foreground,
						activebackground = key_active_background,
						activeforeground=key_active_foreground,
						padx=1, pady=1,
						bd=6,
						relief=SP.bord_style,
						command=command).grid(row=var_row, column=var_column)

		var_column += 1
		if var_column > 13 and var_row == 2:
			var_column = 0
			var_row += 1
		if var_column > 13 and var_row == 3:
			var_column = 0
			var_row += 1
		if var_column > 13 and var_row == 4:
			var_column = 0
			var_row += 1


def keyboard(label_keyboard):
	label_font = ("Helvetica",30)
	label_text = label_keyboard

	entry_font = ("Helvetica",30)
	entry_background = SP.root_font_color
	entry_foreground = "black"
	kb = tkinter.Tk()

	kb.attributes('-fullscreen', SP.full_screen_option)
	kb.config(bg=SP.standard_color_setting("root_keyboard"))
	label_scritta=Label(
						kb,
						text=label_text,
						font=label_font,
						bg=SP.standard_color_setting("root_keyboard"),
						fg=SP.root_font_color)

	label_scritta.grid(row=0,column=1, columnspan=11)

	global entry
	entry = Entry(kb, width=37)
	entry.config(
				font=entry_font,
				bg=entry_background,
				fg=entry_foreground)
	entry.grid(row=1, column=0, columnspan=13)

	hoso_pop(kb)

	kb.mainloop()

	return result



#print(keyboard())
