from tkinter import *
from tkinter import messagebox
import os
import sys

def Create_Window_Multiple_Graphs(Father_Window):
    try:
        raise Exception("La caracteristica aun esta en desarrollo y no esta disponible por el momento.")
    except Exception as e:
        messagebox.showwarning("Advertencia" , f"{e}")
        return 0

    if(__name__ != "__main__"):
        W_Multiple_Grahps = Toplevel(Father_Window)
    else:
        W_Multiple_Grahps = Tk()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    W_Multiple_Grahps.geometry("700x500+250+150")
    W_Multiple_Grahps.title("Crear Multiples Graficos")
    Icon = PhotoImage(master=W_Multiple_Grahps , file="Images/icon.png")
    W_Multiple_Grahps.iconphoto(False , Icon)
    W_Multiple_Grahps.grab_set()

    

    W_Multiple_Grahps.resizable(False , False)
    W_Multiple_Grahps.mainloop()