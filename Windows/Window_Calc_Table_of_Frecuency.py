import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Calcs.Calc_Values_Tables import *
from Main_Window import Main_Window , Icon
from Windows_Errors import Frecuences_Error
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

    def Has_Rows(self):
        return len(self.treeview.get_children()) > 0
    
    def clear_table(self):
        if(self.Has_Rows()):
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

    def Create_Table(Precision , Input , Tables):
        try:
            Delete_Labels(Labels_Window_Frecuences_Table)

            if(Checked_Cuantitative_Variable.get()):
                Type_Of_Variable = "Cuantitative"
            elif(Checked_Cuantitative_Variable.get()):
                Type_Of_Variable = "Cualitative"
            else:
                raise Frecuences_Error("NO TYPE DEFINED" , "No se detecto el tipo de variable")
            
            Input = str(Input.get())
            Precision = int(Precision.get())
            Variables , Frecuences = Main_Function(Precision, Input , Type_Of_Variable)

            if(Type_Of_Variable == "Cuantitative"):
                """ Primero se calcula y se genera la tabla extendida para varios valores """


                for a in range(0 , Variables["m"]):
                    Tables["Cuantitative_For_Many_Values"].treeview.insert(
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
                for col in Tables["Cuantitative_For_Many_Values"].treeview["columns"]:
                    Tables["Cuantitative_For_Many_Values"].treeview.column(col, anchor="center")

                for b in range(0 , Variables["m"]):
                    Tables["Cuantitative_For_Many_Values"].treeview.insert(
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
                for col in Tables["Cuantitative_For_Many_Values"].treeview["columns"]:
                    Tables["Cuantitative_For_Many_Values"].treeview.column(col, anchor="center")
            """ b=0
            for key,value in Variables.items():
                x_pos = 40+(215*b)
                lab = Label(Window_Frecuences_Table , text=f"{key} = {value}" , font=("Times New Roman" , 12) , bg="#FEE1AB")
                lab.place(x=x_pos , y=260)
                Labels_Window_Frecuences_Table.append(lab)
                b +=1 """
            
            Btn_Calculate_Again.config(state="normal")
            Checkbox_Cualitative_Variable.config(state="disabled")
            Checkbox_Cuantitative_Variable.config(state="disabled")
        except (IndexError , ValueError, TypeError) as e:
            Error_Icon = PhotoImage(file="Images/error_icon.png")
            Win_Err = Toplevel(Window_Frecuences_Table)
            Win_Err.geometry("700x100+400+400")
            Win_Err.title("Error")
            Win_Err.iconphoto(False,Error_Icon)

            Text = Label(Win_Err , text=f"{e}" , font=("Times New Roman" , 13) , justify=CENTER)
            Text.place(x=240 , y=20)

            Btn_Close = Button(Win_Err , text="Cerrar" , font=("Times New Roman" , 13) , command= Win_Err.destroy)
            Btn_Close.place(x=330 , y=60)

            Win_Err.protocol("WM_DELETE_WINDOW" , Win_Err.destroy)
            Win_Err.grab_set()
            Win_Err.resizable(False,False)
            Win_Err.mainloop()
        except Frecuences_Error as e:
            e.Create_Window(Window_Frecuences_Table)

    def Checked_Cuantitative():
        if(Checked_Cuantitative_Variable.get()):
            Table_Cuantitative_For_Many_Values.place(x=40 , y=395)
            Table_Cualitative_Extended.place_forget()
            Checkbox_Normal_Table.config(state="normal")
            Checkbox_Extended_Table.config(state="normal")
        else:
            Table_Cuantitative_For_Many_Values.place_forget()
            Checkbox_Normal_Table.config(state="disabled")
            Checkbox_Extended_Table.config(state="disabled")
    def Checked_Cualitative():
        if(Checked_Cualitative_Variable.get()):
            Table_Cualitative_Extended.place(x=40 , y=395)
            Table_Cuantitative_For_Many_Values.place_forget()
            Checkbox_Normal_Table.config(state="normal")
            Checkbox_Extended_Table.config(state="normal")
        else:
            Table_Cualitative_Extended.place_forget()
            Checkbox_Normal_Table.config(state="disabled")
            Checkbox_Extended_Table.config(state="disabled")

    def Only_Check_Cualitative():
        if(Checked_Cualitative_Variable.get() and Checked_Cuantitative_Variable.get()):
            Checkbox_Cuantitative_Variable.invoke()
        Checked_Cualitative()
    def Only_Check_Cuantitative():
        if(Checked_Cuantitative_Variable.get() and Checked_Cualitative_Variable.get()):
            Checkbox_Cualitative_Variable.invoke()
        Checked_Cuantitative()

    def Calculate_Again(Tables):
        for value in Tables.value():
            value.clear_table()
        Btn_Calculate_Again.config(state="disabled")
        Checkbox_Cualitative_Variable.config(state="normal")
        Checkbox_Cuantitative_Variable.config(state="normal")

    Window_Frecuences_Table = Toplevel(Main_Window)
    Window_Frecuences_Table.geometry("1240x700+135+100")
    Window_Frecuences_Table.title("Tabla de frecuencias")
    Window_Frecuences_Table.config(bg="#6C6E72")
    Window_Frecuences_Table.iconphoto(False , Icon)

    # Grid = 16 rows , 16 columns
    Data = StringVar(Window_Frecuences_Table)
    Precision = IntVar(Window_Frecuences_Table)
    Checked_Cualitative_Variable = BooleanVar(Window_Frecuences_Table)
    Checked_Cuantitative_Variable = BooleanVar(Window_Frecuences_Table)
    Checked_Normal_Table = BooleanVar(Window_Frecuences_Table)
    Checked_Extended_Table = BooleanVar(Window_Frecuences_Table)
    
    Title = Label(Window_Frecuences_Table , text="Calculo de Tablas de Frecuencia" , font=("Times New Roman" , 22), foreground="#ffffff", justify=CENTER , width=76 , bg="#9DAEC6" , highlightthickness=1 ,highlightbackground="#ffffff")
    Title.place(x=9 , y=10)

    Section_Input = Label(Window_Frecuences_Table , width=168 ,height=30, bg="#FEE1AB" , highlightthickness=2 , highlightbackground="#000000")
    Section_Input.place(x=29 , y=65)


    Text_Input_Data = Label(Window_Frecuences_Table , text="Ingrese los valores:", font=("Times New Roman" , 13) , bg="#FEE1AB")
    Text_Input_Data.place(x=40 , y=90)
    Input_Data = Entry(Window_Frecuences_Table , textvariable=Data , border=1 , cursor="xterm" , width=100 , font=("Courier New" , 13) , bg="#ffffff")
    Input_Data.place(x=180 , y=90)
    Input_Data.focus()


    Text_Input_Precision_Results = Label(Window_Frecuences_Table , text="Precision:" , font=("Times New Roman" , 13) , bg="#FEE1AB")
    Text_Input_Precision_Results.place(x=840 , y=130)
    Input_Precision_Results = Spinbox(Window_Frecuences_Table , width=10 , textvariable=Precision , from_=0 , to=8 , increment=1 , font=("Courier New" , 13) , bg="#ffffff")
    Input_Precision_Results.place(x=980 , y=130)


    Checkbox_Cuantitative_Variable = Checkbutton(Window_Frecuences_Table , text="Variable Cuantitativa" , font=("Times New Roman" , 13) , bg="#FEE1AB" , variable=Checked_Cuantitative_Variable , command=Only_Check_Cuantitative)
    Checkbox_Cuantitative_Variable.place(x=40 , y=130)

    Checkbox_Cualitative_Variable = Checkbutton(Window_Frecuences_Table , text="Variable Cualitativa" , font=("Times New Roman" , 13) , bg="#FEE1AB", variable=Checked_Cualitative_Variable , command=Only_Check_Cualitative)
    Checkbox_Cualitative_Variable.place(x=40 , y=170)

    Checkbox_Normal_Table = Checkbutton(Window_Frecuences_Table , text="Tabla Normal" , font=("Times New Roman" , 13) , bg="#FEE1AB" , variable=Checked_Normal_Table)
    Checkbox_Normal_Table.place(x=240 , y=130)
    Checkbox_Normal_Table.config(state="disabled")

    Checkbox_Extended_Table = Checkbutton(Window_Frecuences_Table , text="Tabla Extendida", font=("Times New Roman" , 13) , bg="#FEE1AB" , variable=Checked_Extended_Table)
    Checkbox_Extended_Table.place(x=240 , y=170)
    Checkbox_Extended_Table.config(state="disabled")

    Btn_Calculate_Again = Button(Window_Frecuences_Table , text="Intentar de nuevo" , font=("Times New Roman" , 14) , width=20 , bg="#F4B0C0" , command= lambda: Calculate_Again(Dictionary_Tables))
    Btn_Calculate_Again.place(x=670 , y=200)
    Btn_Calculate_Again.config(state="disabled")

    Btn_Generate_Table = Button(Window_Frecuences_Table , text="Generar Tabla" , font=("Times New Roman" , 14) , width=20 , bg="#F4B0C0" , command= lambda: Create_Table(Precision , Data , Dictionary_Tables)) # Si no colocas lambda: o colocas parentesis a la funcion, esta se ejecuta cuando el boton se crea, y puede generar problemas
    Btn_Generate_Table.place(x=970 , y=200)

    Section_Frecuences_Table = Label(Window_Frecuences_Table , width=168 , height=25 , bg="#FEE1AB" , highlightthickness=2 , highlightbackground="#000000")
    Section_Frecuences_Table.place(x=29 , y=255)

    """ Tabla para Variables Cuantitativas Continuas o Discretas con muchos datos """
    Table_Cuantitative_For_Many_Values = TreeviewFrame(Window_Frecuences_Table)
    Table_Cuantitative_For_Many_Values.config(width=10, height=0)

    Table_Cuantitative_For_Many_Values.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10", "11") , show="headings")
    Table_Cuantitative_For_Many_Values.treeview.heading("1" , text="m")
    Table_Cuantitative_For_Many_Values.treeview.heading("2" , text="Li")
    Table_Cuantitative_For_Many_Values.treeview.heading("3" , text="Ls")
    Table_Cuantitative_For_Many_Values.treeview.heading("4" , text="Grupos")
    Table_Cuantitative_For_Many_Values.treeview.heading("5" , text="xi")
    Table_Cuantitative_For_Many_Values.treeview.heading("6" , text="fi")
    Table_Cuantitative_For_Many_Values.treeview.heading("7" , text="Fi")
    Table_Cuantitative_For_Many_Values.treeview.heading("8" , text="hi")
    Table_Cuantitative_For_Many_Values.treeview.heading("9" , text="Hi")
    Table_Cuantitative_For_Many_Values.treeview.heading("10" , text="hi%")
    Table_Cuantitative_For_Many_Values.treeview.heading("11" , text="HI%")

    for a in range(1 , 12):
        Table_Cuantitative_For_Many_Values.treeview.column(f"{a}" , anchor="center" , width=104)
    """ Tabla Cualitativa con pocos datos """

    """ Tabla Cualitativa con mas informacion """
    Table_Cualitative_Extended = TreeviewFrame(Window_Frecuences_Table)
    Table_Cualitative_Extended.config(width=10, height=0)

    Table_Cualitative_Extended.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7") , show="headings")
    Table_Cualitative_Extended.treeview.heading("1" , text="a")
    Table_Cualitative_Extended.treeview.heading("2" , text="fi")
    Table_Cualitative_Extended.treeview.heading("3" , text="Fi")
    Table_Cualitative_Extended.treeview.heading("4" , text="hi")
    Table_Cualitative_Extended.treeview.heading("5" , text="Hi")
    Table_Cualitative_Extended.treeview.heading("6" , text="hi%")
    Table_Cualitative_Extended.treeview.heading("7" , text="HI%")

    for a in range(1 , 8):
        Table_Cualitative_Extended.treeview.column(f"{a}" , anchor="center" , width=162)

    style = ttk.Style()
    style.configure("Treeview.Heading" , font=("Arial" , 10))

    style.map("Treeview",
            foreground=[("selected", "black")],
            background=[("selected", "skyblue")])

    Dictionary_Tables = dict(
        Cuantitative_For_Many_Values = Table_Cuantitative_For_Many_Values,
        Cualitative_Extended = Table_Cualitative_Extended,
    )

    Btn_Back = Button(Window_Frecuences_Table , text="Volver", font=("Times New Roman" , 12) , command=Back_to_main_window , width=134 , bg="#F4B0C0")
    Btn_Back.place(x=10 , y=660)

    Window_Frecuences_Table.protocol("WM_DELETE_WINDOW" , Back_to_main_window)
    Window_Frecuences_Table.resizable(False,False)
    Window_Frecuences_Table.mainloop()