import tkinter 
from tkinter import ttk

def btnClose_click():
    frmMain.destroy()

# generate a window

frmMain = tkinter.Tk()
frmMain.title("Erste Anwendung")
frmMain.wm_geometry('800x600')

# "Close" button generating

btnClose = ttk.Button(frmMain, text = "Beenden", command = btnClose_click)
btnClose.place(x=160,y=80)

# infinity loop
frmMain.mainloop()