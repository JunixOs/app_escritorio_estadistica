from tkinter import *
from tkinter import ttk
def index_to_string(i):
    Letter = ''
    Temp = i
    while Temp >= 0:
        Letter = chr(Temp % 26 + 65) + Letter
        Temp = Temp // 26 - 1
    return Letter

def Create_Window_Create_Venn_Diagram(Main_Window = None):
    def Back():
        for widget in W_Create_Venn_Diagram.winfo_children():
            widget.destroy()
        W_Create_Venn_Diagram.grab_release()
        W_Create_Venn_Diagram.quit()
        W_Create_Venn_Diagram.destroy()

        Main_Window.state(newstate="normal")
        Main_Window.lift()

    if(__name__ == "__main__"):
        W_Create_Venn_Diagram = Tk()
    else:
        Main_Window.state(newstate="withdraw")
        W_Create_Venn_Diagram = Toplevel(Main_Window)

    W_Create_Venn_Diagram.geometry("1300x800+110+48")
    Icon = PhotoImage(file="Images/icon.png")
    W_Create_Venn_Diagram.iconphoto(False , Icon)
    W_Create_Venn_Diagram.title("Crear Diagramas de Venn")
    W_Create_Venn_Diagram.grab_set()
    W_Create_Venn_Diagram.lift()
    W_Create_Venn_Diagram.config(bg="#9EABC5")
    W_Create_Venn_Diagram.protocol("WM_DELETE_WINDOW" , Back)

    Main_Title = Label(W_Create_Venn_Diagram , text="Crear Diagramas de Venn" , bg="#A7D0D9" , font=("Times New Roman" , 22) , justify=CENTER , foreground="#000000" , highlightthickness=1 , highlightbackground="#000000" , relief="raised")
    Main_Title.place(x=10 , y=10 , width=1280 , height=50)

    Section_Input = Label(W_Create_Venn_Diagram , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)
    Section_Input.place(x=30 , y=80 , width=1240 , height=240)

    Main_Frame_Input = Frame(W_Create_Venn_Diagram, bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)
    Main_Frame_Input.place(x=30, y=80, width=1240, height=180)

    # Crear canvas
    canvas = Canvas(Main_Frame_Input, width=1220, height=180)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Crear scrollbar
    scrollbar = ttk.Scrollbar(Main_Frame_Input, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # canvas para usar el scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # frame dentro del canvas que contenga el contenido desplazable
    content_frame = Frame(canvas, width=1240 , bg="#CDC4FF")

    # Crear una ventana interna dentro del canvas que se desplazará
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # widgets dinámicos (Labels y Entries) al content_frame
    for i in range(7):
        Text_Input_Data = Label(content_frame, text=f"Conjunto {index_to_string(i)}:", font=("Times New Roman", 13), bg="#CDC4FF", justify=LEFT)
        Text_Input_Data.grid(row=i*2, column=0, padx=10, pady=10, sticky="w")

        Input_Data = Entry(content_frame, font=("Courier New", 13), relief="sunken", border=1 , width=109)
        Input_Data.grid(row=i*2, column=1, padx=10, pady=10, sticky="w")

    # Actualiza la región de desplazamiento
    content_frame.update_idletasks()  # Asegura que los widgets estén completamente renderizados
    canvas.config(scrollregion=canvas.bbox("all"))  # Actualiza la región desplazable

    Btn_Import_Data = Button(W_Create_Venn_Diagram , text="Importar datos" , font=("Times New Roman" , 13) , bg="#F9FFD1" , command=lambda : Main_Frame_Input.place(x=30, y=80, width=1240, height=180))
    Btn_Import_Data.place(x=80 , y=270)

    Btn_Generate_Venn_Diagram = Button(W_Create_Venn_Diagram , text="Generar Diagrama" , font=("Times New Roman" , 13) , bg="#FFD9FA" , command=Main_Frame_Input.place_forget)
    Btn_Generate_Venn_Diagram.place(x=1080 , y=270)

    Section_Diagram = Label(W_Create_Venn_Diagram , bg="#CBEFE3" , highlightbackground="#000000" , highlightthickness=1)
    Section_Diagram.place(x=30 , y=340 , width=1240 , height=420)

    Btn_Volver = Button(W_Create_Venn_Diagram , text="Volver" , font=("Times New Roman" , 13) , bg="#F9FFD1" , command=Back)
    Btn_Volver.pack(side=BOTTOM , fill=BOTH)

    W_Create_Venn_Diagram.resizable(False , False)
    W_Create_Venn_Diagram.mainloop()

if(__name__ == "__main__"):
    Create_Window_Create_Venn_Diagram()