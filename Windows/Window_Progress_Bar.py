from tkinter import ttk
from tkinter import *
import time

class Create_Window_Progress_Bar:
    def __init__(self , Root_Window):
        self.Progress_Window = Toplevel(Root_Window)
        self.Progress_Window.title("Cargando")
        self.Progress_Window.geometry("300x100+450+250")
        self.Progress_Window.grab_set()
        self.Progress_Window.lift()

        self.Label = Label(self.Progress_Window , text="Procesando, por favor espere" , font=("Times New Roman" , 13))
        self.Label.pack(pady=10)

        self.Progress_Bar = ttk.Progressbar(self.Progress_Window , orient="horizontal" , length=200 , mode="indeterminate")
        self.Progress_Bar.pack(pady=10)
        self.Progress_Bar.start()


def long_operation():
    Progress = Create_Window_Progress_Bar(root)  # Muestra la ventana de progreso y la barra

    
    def update_progress(step):
        if step < 5:  # 5 pasos de proceso
            print(f"Operación {step+1} en curso...")
            root.after(1000, update_progress, step + 1)  # Llama nuevamente después de 1 segundo
        else:
            # Detener la barra de progreso
            Progress.Progress_Bar.stop()
            Progress.Progress_Window.destroy()  # Cierra la ventana de progreso
    update_progress(0)
root = Tk()
root.title("Ventana con Barra de Progreso")
root.geometry("400x200")

# Botón que inicia la operación
start_button = Button(root, text="Iniciar operación", command=long_operation)
start_button.pack(pady=20)
root.mainloop()