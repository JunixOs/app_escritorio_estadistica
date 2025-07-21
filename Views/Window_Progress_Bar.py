import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Tools import Get_Resource_Path , Delete_Actual_Window
from tkinter import ttk
from tkinter import *
import time
import threading

class W_Progress_Bar:
    def __init__(self , Root_Window):
        self.Root_Window = Root_Window
        self.Progress_Window = None
        self.Progress_Window = None

    def Back(self):
        pass
    def Start_Progress_Bar(self , Text_Progress_Bar = "Procesando, esto podria tomar un tiempo."):
        self.Progress_Window = Toplevel(self.Root_Window)
        self.Progress_Window.title("Cargando")
        self.Progress_Window.geometry("500x100+500+400")
        self.Progress_Window.protocol("WM_DELETE_WINDOW" , self.Back)
        Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
        self.Progress_Window.iconphoto(False , Icon)
        self.Progress_Window.grab_set()
        self.Progress_Window.lift()

        self.Label = Label(self.Progress_Window , text=Text_Progress_Bar , font=("Times New Roman" , 13))
        self.Label.pack(pady=10)

        self.Progress_Bar = ttk.Progressbar(self.Progress_Window , orient="horizontal" , length=200 , mode="indeterminate")
        self.Progress_Bar.pack(pady=10)
        self.Progress_Bar.start()

    def Close_Progress_Bar(self):
        if(self.Progress_Window and self.Progress_Bar):
            Delete_Actual_Window(self.Root_Window , self.Progress_Window)

def tarea_larga(Progress , root):
    # Simula una tarea larga
    time.sleep(5)  # Aquí va la operación que tarde mucho
    print("Tarea finalizada!")

    root.after(0 , Progress.Close_Progress_Bar)

def iniciar_tarea():
    try:
        Progress = W_Progress_Bar(root)
        Progress.Start_Progress_Bar()

        # Iniciar la tarea en un hilo separado
        threading.Thread(target=tarea_larga , args=(Progress , root)).start()
    except Exception as e:
        root.after(0, Progress.Close_Progress_Bar)
        print(f"{e}")

if __name__ == "__main__":
    root = Tk()
    root.title("Ventana con Barra de Progreso")
    root.geometry("400x200")

    # Botón que inicia la operación
    start_button = Button(root, text="Iniciar operación", command=iniciar_tarea)
    start_button.pack(pady=20)
    root.mainloop()