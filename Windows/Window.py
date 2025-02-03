import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Calcs.Frecuences_Calc import *
from tkinter import *
from tkinter import ttk

# Variables Globales
Labels_Window_Frecuences_Table = []
#
class TreeviewFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        self.treeview = ttk.Treeview(
            self,
            yscrollcommand=self.vscrollbar.set
        )
        self.vscrollbar.config(command=self.treeview.yview)
        self.vscrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.pack(fill="both" , expand=True)

    def has_rows(self):
        return len(self.treeview.get_children()) > 0
    
    def clear_table(self):
        if(self.has_rows()):
            for item in self.treeview.get_children():
                self.treeview.delete(item)

def Create_Window_Frecuences_Table():
    Main_Window.state(newstate="withdraw")

    def Back_to_main_window():
        Main_Window.state(newstate="normal")
        Main_Window.geometry("1240x700+135+100")
        Main_Window.title("Seleccion")
        Window_Frecuences_Table.destroy()
    def Delete_Labels(Labels):
        if(len(Labels) != 0):
            for a in range(0 , len(Labels)):
                Labels[a].destroy()
        Labels_Window_Frecuences_Table = []

    def Create_Table(Precision , Input , Table_Frecuences):
        try:
            Table_Frecuences.clear_table()
            
            Delete_Labels(Labels_Window_Frecuences_Table)

            Input = str(Input.get())
            Precision = int(Precision.get())
            Variables , Frecuences = Main_Function(Precision, Input)
        
            for a in range(0 , Variables["m"]):
                Table_Frecuences.treeview.insert(
                    "", END , values=(
                        a+1, 
                        Frecuences["Intervals"][a][0], 
                        Frecuences["Intervals"][a][1], 
                        Frecuences["Groups"][a], 
                        Frecuences["xi"][a],
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        Frecuences["hi"][a],
                        Frecuences["Hi"][a],
                        f"{Frecuences["hi_percent"][a]}%",
                        f"{Frecuences["Hi_percent"][a]}%",)
                )
            for col in Table_Frecuences.treeview["columns"]:
                Table_Frecuences.treeview.column(col, anchor="center")

            b=0
            for key,value in Variables.items():
                x_pos = 40+(215*b)
                lab = Label(Window_Frecuences_Table , text=f"{key} = {value}" , font=("Times New Roman" , 12) , bg="#FEE1AB")
                lab.place(x=x_pos , y=240)
                Labels_Window_Frecuences_Table.append(lab)
                b +=1
        except (IndexError , ValueError, TypeError):
            Error_Icon = PhotoImage(file="Images/error_icon.png")
            Win_Err = Toplevel(Window_Frecuences_Table)
            Win_Err.geometry("700x100+400+400")
            Win_Err.title("Error")
            Win_Err.iconphoto(False,Error_Icon)

            Text = Label(Win_Err , text="Hubo un error al procesar los datos" , font=("Times New Roman" , 13) , justify=CENTER)
            Text.place(x=240 , y=20)

            Btn_Close = Button(Win_Err , text="Cerrar" , font=("Times New Roman" , 13) , command= Win_Err.destroy)
            Btn_Close.place(x=330 , y=60)

            Win_Err.protocol("WM_DELETE_WINDOW" , Win_Err.destroy)
            Win_Err.grab_set()
            Win_Err.resizable(False,False)
            Win_Err.mainloop()

    Window_Frecuences_Table = Toplevel(Main_Window)
    Window_Frecuences_Table.geometry("1240x700+135+100")
    Window_Frecuences_Table.title("Tabla de frecuencias")
    Window_Frecuences_Table.config(bg="#6C6E72")
    Window_Frecuences_Table.iconphoto(False , Icon)

    # Grid = 16 rows , 16 columns
    Data = StringVar(Window_Frecuences_Table)
    Precision = IntVar(Window_Frecuences_Table)
    
    Title = Label(Window_Frecuences_Table , text="Calculo de Tablas de Frecuencia" , font=("Times New Roman" , 22), foreground="#ffffff", justify=CENTER , width=76 , bg="#9DAEC6" , highlightthickness=1 ,highlightbackground="#ffffff")
    Title.place(x=9 , y=10)

    Section_Input = Label(Window_Frecuences_Table , width=168 ,height=10, bg="#FEE1AB" , highlightthickness=2 , highlightbackground="#000000")
    Section_Input.place(x=29 , y=65)

    Text_Input_Data = Label(Window_Frecuences_Table , text="Ingrese los valores:", font=("Times New Roman" , 13) , bg="#FEE1AB")
    Text_Input_Data.place(x=40 , y=90)
    Input_Data = Entry(Window_Frecuences_Table , textvariable=Data , border=1 , cursor="xterm" , width=100 , font=("Courier New" , 13) , bg="#ffffff")
    Input_Data.place(x=180 , y=90)
    Input_Data.focus()

    Text_Input_Precision_Results = Label(Window_Frecuences_Table , text="Precision:" , font=("Times New Roman" , 13) , bg="#FEE1AB")
    Text_Input_Precision_Results.place(x=40 , y=130)
    Input_Precision_Results = Spinbox(Window_Frecuences_Table , width=10 , textvariable=Precision , from_=0 , to=6 , increment=1 , font=("Courier New" , 13) , bg="#ffffff")
    Input_Precision_Results.place(x=180 , y=130)

    Btn_Calc_Table = Button(Window_Frecuences_Table , text="Generar Tabla" , font=("Times New Roman" , 15) , width=30 , bg="#F4B0C0" , command= lambda: Create_Table(Precision , Data , Table)) # Si no colocas lambda: o colocas parentesis a la funcion, esta se ejecuta cuando el boton se crea, y puede generar problemas
    Btn_Calc_Table.place(x=600 , y=130)

    Section_Frecuences_Table = Label(Window_Frecuences_Table , width=168 , height=30 , bg="#FEE1AB" , highlightthickness=2 , highlightbackground="#000000")
    Section_Frecuences_Table.place(x=29 , y=180)

    
    Table = TreeviewFrame(Window_Frecuences_Table)
    Table.config(width=10, height=0)
    Table.place(x=40 , y=355)

    Table.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10", "11") , show="headings")
    Table.treeview.heading("1" , text="m")
    Table.treeview.heading("2" , text="Li")
    Table.treeview.heading("3" , text="Ls")
    Table.treeview.heading("4" , text="Grupos")
    Table.treeview.heading("5" , text="xi")
    Table.treeview.heading("6" , text="fi")
    Table.treeview.heading("7" , text="Fi")
    Table.treeview.heading("8" , text="hi")
    Table.treeview.heading("9" , text="Hi")
    Table.treeview.heading("10" , text="hi%")
    Table.treeview.heading("11" , text="HI%")

    for a in range(1 , 12):
        Table.treeview.column(f"{a}" , anchor="center" , width=104)

    style = ttk.Style()
    style.configure("Treeview.Heading" , font=("Arial" , 10))

    style.map("Treeview",
            foreground=[("selected", "black")],
            background=[("selected", "skyblue")])

    Btn_Back = Button(Window_Frecuences_Table , text="Volver", font=("Times New Roman" , 12) , command=Back_to_main_window , width=134 , bg="#F4B0C0")
    Btn_Back.place(x=10 , y=660)

    Window_Frecuences_Table.protocol("WM_DELETE_WINDOW" , Back_to_main_window)
    Window_Frecuences_Table.resizable(False,False)
    Window_Frecuences_Table.mainloop()

def Create_Window_Samplings():
    pass

Main_Window = Tk()

Image_Right_Section = PhotoImage(file="Images/normal_distribution.png")
Image_Right_Section.subsample(10)
Icon = PhotoImage(file="Images/icon.png")

Main_Window.geometry("1240x700+135+100")
Main_Window.title("Seleccion")
Main_Window.config(bg="#9DAEC6")
Main_Window.iconphoto(False,Icon)

Right_Section = Label(Main_Window , width=531 , height=691 , bg="#F7EDCB" , image=Image_Right_Section , highlightthickness=2 , highlightbackground="#000000")
Right_Section.place(x=700 , y=0)

BtnFrecuencyTable = Button(Main_Window,text="Crear tabla de frecuencias", font=("Times New Roman", 14) , command=Create_Window_Frecuences_Table , width=30)
BtnFrecuencyTable.place(x=190,y=300)

Main_Window.resizable(False,False)
Main_Window.mainloop()