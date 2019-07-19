from tkinter import *

def showDialog(text):
    def close(toClose):
        toClose.quit()
        toClose.destroy()

    dialog = Tk()
    dialog.config(bg="orange")
    dialog.geometry("+700+400")
    dialog.overrideredirect(1)
    label = Label(dialog, text=text,
                      bg="orange",
                      font=("Helvetica",25),
                  wraplength=200,
                  )
    label.configure(anchor="center")
    label.pack(expand=True)
    dialog.after(3000, close, dialog)
    dialog.mainloop()
