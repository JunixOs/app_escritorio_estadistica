import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Calcs.Venn.Calc_Venn_Diagram import Venn_Diagram
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

    def Process_Data(Widget_Venn_Graph):
        try:
            Graph = Venn_Diagram(Collection_On_Inputs , Data_From_External_File)

            Veen_Graph = Graph.Generate_Diagrams()

            if(Widget_Venn_Graph):
                Widget_Venn_Graph.destroy()
            
            Widget_Venn_Graph = FigureCanvasTkAgg(Veen_Graph , master=W_Create_Venn_Diagram)
            Widget_Venn_Graph.place(x=30 , y=250 , width=1240 , height=510)

        except Exception as e:
            messagebox.showerror("Error" , f"{e}")

    Main_Window.state(newstate="withdraw")
    W_Create_Venn_Diagram = Toplevel(Main_Window)

    W_Create_Venn_Diagram.geometry("1300x800+110+48")
    Icon = PhotoImage(file="Images/icon.png")
    W_Create_Venn_Diagram.iconphoto(False , Icon)
    W_Create_Venn_Diagram.title("Crear Diagramas de Venn")
    W_Create_Venn_Diagram.lift()
    W_Create_Venn_Diagram.config(bg="#9EABC5")

    Collection_On_Inputs = {}
    Data_From_External_File = set()
    Widget_Venn_Graph = None

    Main_Title = Label(W_Create_Venn_Diagram , text="Crear Diagramas de Venn" , bg="#A7D0D9" , font=("Times New Roman" , 22) , justify=CENTER , foreground="#000000" , highlightthickness=1 , highlightbackground="#000000" , relief="raised")
    Main_Title.place(x=10 , y=10 , width=1280 , height=50)

    Section_Input = Label(W_Create_Venn_Diagram , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)
    Section_Input.place(x=30 , y=80 , width=1240 , height=160)

    Frame_Sets = Frame(W_Create_Venn_Diagram, bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)
    Frame_Sets.place(x=30, y=80, width=1240 , height=100)

    Canvas_Set = Canvas(Frame_Sets, width=1220, height=100)
    Canvas_Set.grid(row=0, column=0, sticky="nsew")

    ScrollBar_Frame = ttk.Scrollbar(Frame_Sets, orient="vertical", command=Canvas_Set.yview)
    ScrollBar_Frame.grid(row=0, column=1, sticky="ns")

    Canvas_Set.configure(yscrollcommand=ScrollBar_Frame.set)

    Content_Frame_Sets = Frame(Canvas_Set, width=1240 , bg="#CDC4FF")

    Canvas_Set.create_window((0, 0), window=Content_Frame_Sets, anchor="nw")

    for i in range(3):
        Input_Data_Set = StringVar(W_Create_Venn_Diagram)
        Input_Data_Set.set("")
        Set_Name = index_to_string(i)

        Text_Widget_Input_Data_Set = Label(Content_Frame_Sets, text=f"Conjunto {Set_Name}:", font=("Times New Roman", 13), bg="#CDC4FF", justify=LEFT)
        Text_Widget_Input_Data_Set.grid(row=i*2, column=0, padx=10, pady=10, sticky="w")

        Widget_Input_Data_Set = Entry(Content_Frame_Sets, font=("Courier New", 13), relief="sunken", border=1 , width=109 , textvariable=Input_Data_Set)
        Widget_Input_Data_Set.grid(row=i*2, column=1, padx=10, pady=10, sticky="w")

        Collection_On_Inputs[f"{Set_Name}"] = ["" , Widget_Input_Data_Set , Input_Data_Set]


    Content_Frame_Sets.update_idletasks()  # Asegura que los widgets estén completamente renderizados
    Canvas_Set.config(scrollregion=Canvas_Set.bbox("all"))  # Actualiza la región desplazable

    Btn_Import_Data = Button(W_Create_Venn_Diagram , text="Importar datos" , font=("Times New Roman" , 13) , bg="#F9FFD1" , command=lambda : Frame_Sets.place(x=30, y=80, width=1240, height=180))
    Btn_Import_Data.place(x=80 , y=190)

    Btn_Generate_Venn_Diagram = Button(W_Create_Venn_Diagram , text="Generar Diagrama" , font=("Times New Roman" , 13) , bg="#FFD9FA" , command= lambda: Process_Data(Widget_Venn_Graph))
    Btn_Generate_Venn_Diagram.place(x=1080 , y=190)

    Section_Diagram = Label(W_Create_Venn_Diagram , bg="#CBEFE3" , highlightbackground="#000000" , highlightthickness=1)
    Section_Diagram.place(x=30 , y=250 , width=1240 , height=510)

    Section_Graph_Venn = Label(W_Create_Venn_Diagram , text="Tu grafico se mostrara aqui" , font=("Times New Roman" , 13)  , anchor="center" , bg="#ffffff" , highlightbackground="#000000" , highlightthickness=1)
    Section_Graph_Venn.place(x=30 , y=250 , width=900 , height=510)

    Btn_Export_Graph = Button(W_Create_Venn_Diagram , text="Exportar Grafico" , font=("Times New Roman" , 13) , bg="#FFD9FA")
    Btn_Export_Graph.place(x=990 , y=490 , width=210)

    Btn_Volver = Button(W_Create_Venn_Diagram , text="Volver" , font=("Times New Roman" , 13) , bg="#F9FFD1" , command=Back)
    Btn_Volver.pack(side=BOTTOM , fill=BOTH)

    W_Create_Venn_Diagram.protocol("WM_DELETE_WINDOW" , Back)
    W_Create_Venn_Diagram.resizable(False , False)
    W_Create_Venn_Diagram.mainloop()

if(__name__ == "__main__"):
    Create_Window_Create_Venn_Diagram()