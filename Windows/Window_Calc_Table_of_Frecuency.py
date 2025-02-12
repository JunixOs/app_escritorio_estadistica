import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Calcs.Calc_Values_Tables import *
from Window_Export_Excel import Generate_Window_Export_Excel
from Windows_Errors import Frecuences_Error
from tkinter import *
from tkinter import ttk
import Window_Select_File as W_Select_File
import Window_Show_Graph as W_Show_Graph

# Variables Globales
Labels_Window_Frecuences_Table = []
Global_Calcs = {}
Global_Type_Of_Variable = ""
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

    def Display(self):
        self.place(x=40 , y=330)

    def Hidden(self):
        self.place_forget()
def Display_Or_Hidden_Tables(Tables , Table_Name , Display):
    if(Display):
        for key,value in Tables.items():
            if(key == Table_Name):
                value.Display()
            else:
                value.Hidden()
    else:
        for key,value in Tables.items():
            if(key == Table_Name):
                value.Hidden()

def Put_Data_On_Table_Cuant_For_Many_Values(Table_For_Many_Values , Variables , Frecuences):
    if(not Table_For_Many_Values.Has_Rows()):
        for a in range(0 , Variables["m"]):
            Table_For_Many_Values.treeview.insert(
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
                    f"{Frecuences['hi_percent'][a]}%",
                    f"{Frecuences['Hi_percent'][a]}%",)
            )
        for col in Table_For_Many_Values.treeview["columns"]:
            Table_For_Many_Values.treeview.column(col, anchor="center")
def Put_Data_On_Table_Cuant_Normal(Table_Normal , Variables , Frecuences):
    if(not Table_Normal.Has_Rows()):
        for a in range(0 , Variables["Number_Statistic_Variables"]):
            Table_Normal.treeview.insert(
                "", END , values=(
                    Frecuences["xi"][a],
                    Frecuences["fi"][a],
                    Frecuences["hi"][a],
                    f"{Frecuences['hi_percent'][a]}%",)
            )
        for col in Table_Normal.treeview["columns"]:
            Table_Normal.treeview.column(col , anchor="center")
def Put_Data_On_Table_Cuant_Extended(Table_Extended , Variables, Frecuences):
    if(not Table_Extended.Has_Rows()):
        for a in range(0 , Variables["Number_Statistic_Variables"]):
            Table_Extended.treeview.insert(
                "", END , values=(
                    Frecuences["xi"][a],
                    Frecuences["fi"][a],
                    Frecuences["Fi"][a],
                    Frecuences["hi"][a],
                    Frecuences["Hi"][a],
                    f"{Frecuences['hi_percent'][a]}%",
                    f"{Frecuences['Hi_percent'][a]}%",)
            )
        for col in Table_Extended.treeview["columns"]:
            Table_Extended.treeview.column(col, anchor="center")
def Put_Data_On_Table_Cuali_Normal(Table_Normal , Variables , Frecuences):
    if(not Table_Normal.Has_Rows()):
        for a in range(0 , Variables["N_Character_Modalities"]):
            Table_Normal.treeview.insert(
                "", END , values=(
                    Frecuences["ai"][a],
                    Frecuences["fi"][a],
                    Frecuences["hi"][a],
                    f"{Frecuences['hi_percent'][a]}%",)
            )
        for col in Table_Normal.treeview["columns"]:
            Table_Normal.treeview.column(col, anchor="center")
def Put_Data_On_Table_Cuali_Extended(Table_Extended , Variables , Frecuences):
    if(not Table_Extended.Has_Rows()):
        for a in range(0 , Variables["N_Character_Modalities"]):
            Table_Extended.treeview.insert(
                "", END , values=(
                    Frecuences["ai"][a],
                    Frecuences["fi"][a],
                    Frecuences["Fi"][a],
                    Frecuences["hi"][a],
                    Frecuences["Hi"][a],
                    f"{Frecuences['hi_percent'][a]}%",
                    f"{Frecuences['Hi_percent'][a]}%",)
            )
        for col in Table_Extended.treeview["columns"]:
            Table_Extended.treeview.column(col, anchor="center")

def Delete_Labels(Labels):
    """ Terminar, mostrar valores como Media, promedio , etc """
    if(len(Labels) != 0):
        for a in range(0 , len(Labels)):
            Labels[a].destroy()
    Labels_Window_Frecuences_Table = []

def Create_Window_Frecuences_Table(Main_Window):
    Main_Window.state(newstate="withdraw")

    def Back_to_main_window():
        Main_Window.state(newstate="normal")
        Main_Window.geometry("1240x700+135+100")
        Main_Window.title("StatApp beta v1.5")
        Window_Frecuences_Table.destroy()

    def Create_Table(Precision , Input , Tables):
        global Global_Calcs , Global_Type_Of_Variable
        try:
            for a in Tables.values():
                a.clear_table()

            Input = str(Input.get())
            Precision = int(Precision.get())
            Is_Discrete = None
            """ Delete_Labels(Labels_Window_Frecuences_Table) """

            if(Checked_Cuantitative_Variable.get()):
                Type_Of_Variable = "Cuantitative"
                if(Checked_Cuantitative_Continuous.get()):
                    Is_Discrete = False
                elif(Checked_Cuantitative_Discret.get()):
                    Is_Discrete = True
                else:
                    raise Frecuences_Error("NO TYPE DEFINED" , "No se pudo detectar si la variable Cuantitativa \n es Discreta o Continua.")
            elif(Checked_Cualitative_Variable.get()):
                Type_Of_Variable = "Cualitative"
            else:
                raise Frecuences_Error("NO TYPE DEFINED" , "No se pudo detectar el tipo de variable")

            Dictionary_Values = Main_Function(Precision, Input , Type_Of_Variable , Is_Discrete)

            match(Type_Of_Variable):
                case "Cuantitative":
                    V_Cuantitative = Dictionary_Values["Variables_Cuant_Normal_Extended"]
                    F_Cuantitative = Dictionary_Values["Frecuences_Cuant_Normal_Extended"]
                    if(V_Cuantitative != None and F_Cuantitative != None):
                        Put_Data_On_Table_Cuant_Normal(Tables["Cuantitative_Normal"] , V_Cuantitative , F_Cuantitative)

                        Put_Data_On_Table_Cuant_Extended(Tables["Cuantitative_Extended"] , V_Cuantitative , F_Cuantitative)
                    else:
                        Tables["Cuantitative_Normal"].treeview.insert("" , END , values=(
                            "None",
                            "Demasiados Datos",
                            "Calculo Omitido",
                            "None",
                        ))
                        Tables["Cuantitative_Extended"].treeview.insert("", END , values=(
                        "None",
                        "None",
                        "None",
                        "Demasiados Datos Calculo Omitido",
                        "None",
                        "None",
                        "None",))
                    
                    V_Cuantitative_For_Many_Values = Dictionary_Values["Variables_Cuant_For_Many_Values"]
                    F_Cuantitative_For_Many_Values = Dictionary_Values["Frecuences_Cuant_For_Many_Values"]

                    if(V_Cuantitative_For_Many_Values != None and F_Cuantitative_For_Many_Values != None):
                        Put_Data_On_Table_Cuant_For_Many_Values(Tables["Cuantitative_For_Many_Values"] , V_Cuantitative_For_Many_Values , F_Cuantitative_For_Many_Values)
                    else:
                        Tables["Cuantitative_For_Many_Values"].treeview.insert("", END , values=(
                        "None",
                        "None",
                        "None",
                        "None",
                        "Pocos",
                        "Datos",
                        "Calculo Omitido",
                        "None",
                        "None",
                        "None",
                        "None",))
                case "Cualitative":
                    V_Cualitative = Dictionary_Values["Variables_Cuali_Normal_Extended"]
                    F_Cualitative = Dictionary_Values["Frecuences_Cuali_Normal_Extended"]

                    Put_Data_On_Table_Cuali_Normal(Tables["Cualitative_Normal"] , V_Cualitative , F_Cualitative)

                    Put_Data_On_Table_Cuali_Extended(Tables["Cualitative_Extended"] , V_Cualitative , F_Cualitative)

                case _:
                    raise Frecuences_Error("NO TYPE DEFINED" , "No se pudo detectar el tipo de variable")

            """ b=0
            for key,value in Variables.items():
                x_pos = 40+(215*b)
                lab = Label(Window_Frecuences_Table , text=f"{key} = {value}" , font=("Times New Roman" , 12) , bg="#FEE1AB")
                lab.place(x=x_pos , y=260)
                Labels_Window_Frecuences_Table.append(lab)
                b +=1 """
            Global_Calcs = Dictionary_Values
            Global_Type_Of_Variable = Type_Of_Variable
        except (IndexError , ValueError , NameError , TypeError) as e:
            Win_err = Frecuences_Error("ERROR" , e)
            Win_err.Create_Window(Window_Frecuences_Table)
        except Frecuences_Error as e:
            e.Create_Window(Window_Frecuences_Table)
        else:
            Btn_Calculate_Again.config(state="normal")
            Checkbox_Cualitative_Variable.config(state="disabled")
            Checkbox_Cuantitative_Variable.config(state="disabled")
            Input_Data.config(state="disabled")
            
            Btn_Generate_Excel.config(state="normal")
            Btn_Show_Graph.config(state="normal")
            Btn_Select_File.config(state="disabled")

            Checkbox_Cuantitative_Discret.config(state="disabled")
            Checkbox_Cuantitative_Continuous.config(state="disabled")

    def Switch_on_Tables():
        if(Checked_Cualitative_Variable.get()):
            if(Checked_Normal_Table.get()):
                Display_Or_Hidden_Tables(Dictionary_Tables , "Cualitative_Normal" ,True)
            elif(Checked_Extended_Table.get()):
                Display_Or_Hidden_Tables(Dictionary_Tables , "Cualitative_Extended" , True)
            else:
                Display_Or_Hidden_Tables(Dictionary_Tables , "Cualitative_Normal" , False)
                Display_Or_Hidden_Tables(Dictionary_Tables , "Cualitative_Extended" , False)
        elif(Checked_Cuantitative_Variable.get()):
            if(Checked_Normal_Table.get()):
                Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_Normal" , True)
            elif(Checked_Extended_Table.get()):
                Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_Extended" , True)
            elif(Checked_Cuant_For_Many_Values.get()):
                Display_Or_Hidden_Tables(Dictionary_Tables, "Cuantitative_For_Many_Values" , True)
            else:
                Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_Normal" , False)
                Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_Extended" , False)
                Display_Or_Hidden_Tables(Dictionary_Tables, "Cuantitative_For_Many_Values" , False)
        else:
            Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_Normal" , False)
            Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_Extended" , False)
            Display_Or_Hidden_Tables(Dictionary_Tables, "Cuantitative_For_Many_Values" , False)

            Display_Or_Hidden_Tables(Dictionary_Tables , "Cualitative_Normal" , False)
            Display_Or_Hidden_Tables(Dictionary_Tables , "Cualitative_Extended" , False)

    def Checked_Cuantitative():
        if(Checked_Cuantitative_Variable.get()):

            Checkbox_Normal_Table.config(state="normal")
            Checkbox_Extended_Table.config(state="normal")

            Checkbox_For_Many_Values.config(state="normal")
            Checkbox_For_Many_Values.place(x=240 , y=210)

            Checkbox_Cuantitative_Discret.config(state="normal")
            Checkbox_Cuantitative_Discret.place(x=440 , y=130)

            Checkbox_Cuantitative_Continuous.config(state="normal")
            Checkbox_Cuantitative_Continuous.place(x=440 , y=170)

            Switch_on_Tables()
        else:
            Table_Cuantitative_For_Many_Values.place_forget()

            Checkbox_Normal_Table.config(state="disabled")
            Checkbox_Extended_Table.config(state="disabled")

            Checkbox_For_Many_Values.config(state="disabled")
            Checkbox_For_Many_Values.place_forget()

            Checkbox_Cuantitative_Discret.config(state="disabled")
            Checkbox_Cuantitative_Discret.place_forget()
            Checked_Cuantitative_Discret.set(False)

            Checkbox_Cuantitative_Continuous.config(state="disabled")
            Checkbox_Cuantitative_Continuous.place_forget()
            Checked_Cuantitative_Continuous.set(False)

            Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_Normal" , False)
            Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_Extended" , False)
            Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_For_Many_Values" , False)

    def Checked_Cualitative():
        if(Checked_Cualitative_Variable.get()):

            Checkbox_Normal_Table.config(state="normal")
            Checkbox_Extended_Table.config(state="normal")

            Checkbox_For_Many_Values.config(state="disabled")
            Checkbox_For_Many_Values.place_forget()

            Checkbox_Cuantitative_Discret.config(state="disabled")
            Checkbox_Cuantitative_Discret.place_forget()
            Checked_Cuantitative_Discret.set(False)

            Checkbox_Cuantitative_Continuous.config(state="disabled")
            Checkbox_Cuantitative_Continuous.place_forget()
            Checked_Cuantitative_Continuous.set(False)

            if(Checked_Cuant_For_Many_Values.get()):
                Checked_Cuant_For_Many_Values.set(False)
                Display_Or_Hidden_Tables(Dictionary_Tables , "Cuantitative_For_Many_Values" , False)
            Checkbox_For_Many_Values.place_forget()
            Switch_on_Tables()
        else:
            Table_Cualitative_Extended.Hidden()

            Checkbox_Normal_Table.config(state="disabled")
            Checkbox_Extended_Table.config(state="disabled")

            Display_Or_Hidden_Tables(Dictionary_Tables , "Cualitative_Normal" , False)
            Display_Or_Hidden_Tables(Dictionary_Tables , "Cualitative_Extended" , False)

    def Only_Check_Cualitative():
        if(Checked_Cualitative_Variable.get() and Checked_Cuantitative_Variable.get()):
            Checked_Cuantitative_Variable.set(False)

        if(not Checked_Cualitative_Variable.get() and not Checked_Cuantitative_Variable.get()):
            Checked_Normal_Table.set(False)
            Checked_Extended_Table.set(False)
            Checked_Cuant_For_Many_Values.set(False)
        Checked_Cualitative()

    def Only_Check_Cuantitative():
        if(Checked_Cuantitative_Variable.get() and Checked_Cualitative_Variable.get()):
            Checked_Cualitative_Variable.set(False)

        if(not Checked_Cualitative_Variable.get() and not Checked_Cuantitative_Variable.get()):
            Checked_Normal_Table.set(False)
            Checked_Extended_Table.set(False)
            Checked_Cuant_For_Many_Values.set(False)
        Checked_Cuantitative()

    def Only_Check_Normal():
        if((Checked_Normal_Table.get() and Checked_Extended_Table.get()) or (Checked_Normal_Table.get() and Checked_Cuant_For_Many_Values.get())):
            Checked_Extended_Table.set(False)  # Desmarcar el checkbox extendido
            Checked_Cuant_For_Many_Values.set(False)
        Switch_on_Tables()

    def Only_Check_Extended():
        if((Checked_Extended_Table.get() and Checked_Normal_Table.get()) or (Checked_Extended_Table.get() and Checked_Cuant_For_Many_Values.get())):
            Checked_Normal_Table.set(False)
            Checked_Cuant_For_Many_Values.set(False)
        Switch_on_Tables()

    def Only_Check_Many_Values():
        if((Checked_Cuant_For_Many_Values.get() and Checked_Normal_Table.get()) or (Checked_Cuant_For_Many_Values.get() and Checked_Extended_Table.get())):
            Checked_Normal_Table.set(False)  # Desmarcar el checkbox normal
            Checked_Extended_Table.set(False)
        Switch_on_Tables()

    def Only_Check_Cuant_Discret():
        if(Checked_Cuantitative_Discret.get() and Checked_Cuantitative_Continuous.get()):
            Checked_Cuantitative_Continuous.set(False)
    def Only_Check_Cuant_Continuous():
        if(Checked_Cuantitative_Continuous.get() and Checked_Cuantitative_Discret.get()):
            Checked_Cuantitative_Discret.set(False)
    def Calculate_Again(Tables):
        global Global_Calcs , Global_Type_Of_Variable
        for value in Tables.values():
            value.clear_table()
        Btn_Calculate_Again.config(state="disabled")
        Checkbox_Cualitative_Variable.config(state="normal")
        Checkbox_Cuantitative_Variable.config(state="normal")
        Checked_Cuantitative_Variable.set(False)
        Checked_Cualitative_Variable.set(False)

        Switch_on_Tables()

        Checked_Extended_Table.set(False)
        Checked_Normal_Table.set(False)
        Checked_Cuant_For_Many_Values.set(False)
        Checkbox_Normal_Table.config(state="disabled")
        Checkbox_Extended_Table.config(state="disabled")
        Checkbox_For_Many_Values.config(state="disabled")
        Checkbox_For_Many_Values.place_forget()

        Input_Data.config(state="normal")
        Input_Data.delete(0 , END)
        Precision.set(0)
        Btn_Select_File.config(state="normal")
        Global_Calcs = {}
        Global_Type_Of_Variable = ""

        Checkbox_Cuantitative_Continuous.config(state="normal")
        Checkbox_Cuantitative_Continuous.place_forget()
        Checked_Cuantitative_Continuous.set(False)

        Checkbox_Cuantitative_Discret.config(state="normal")
        Checkbox_Cuantitative_Discret.place_forget()
        Checked_Cuantitative_Discret.set(False)

    Window_Frecuences_Table = Toplevel(Main_Window)
    Window_Frecuences_Table.geometry("1240x700+135+100")
    Window_Frecuences_Table.title("Tabla de frecuencias")
    Window_Frecuences_Table.config(bg="#6C6E72")
    Icon = PhotoImage(file="Images/icon.png")
    Window_Frecuences_Table.iconphoto(False , Icon)

    Data = StringVar(Window_Frecuences_Table)
    Precision = IntVar(Window_Frecuences_Table)
    Checked_Cualitative_Variable = BooleanVar(Window_Frecuences_Table)
    Checked_Cuantitative_Variable = BooleanVar(Window_Frecuences_Table)

    Checked_Cuantitative_Discret = BooleanVar(Window_Frecuences_Table)
    Checked_Cuantitative_Continuous = BooleanVar(Window_Frecuences_Table)

    Checked_Normal_Table = BooleanVar(Window_Frecuences_Table)
    Checked_Extended_Table = BooleanVar(Window_Frecuences_Table)
    Checked_Cuant_For_Many_Values = BooleanVar(Window_Frecuences_Table)
    
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
    Input_Precision_Results = Spinbox(Window_Frecuences_Table , width=10 , textvariable=Precision , from_=1 , to=8 , increment=1 , font=("Courier New" , 13) , bg="#ffffff")
    Input_Precision_Results.place(x=980 , y=130)


    Checkbox_Cuantitative_Variable = Checkbutton(Window_Frecuences_Table , text="Variable Cuantitativa" , font=("Times New Roman" , 13) , bg="#FEE1AB" , variable=Checked_Cuantitative_Variable , command=Only_Check_Cuantitative)
    Checkbox_Cuantitative_Variable.place(x=40 , y=130)

    Checkbox_Cualitative_Variable = Checkbutton(Window_Frecuences_Table , text="Variable Cualitativa" , font=("Times New Roman" , 13) , bg="#FEE1AB", variable=Checked_Cualitative_Variable , command=Only_Check_Cualitative)
    Checkbox_Cualitative_Variable.place(x=40 , y=170)

    Checkbox_Normal_Table = Checkbutton(Window_Frecuences_Table , text="Tabla Normal" , font=("Times New Roman" , 13) , bg="#FEE1AB" , variable=Checked_Normal_Table , command=Only_Check_Normal)
    Checkbox_Normal_Table.place(x=240 , y=130)
    Checkbox_Normal_Table.config(state="disabled")

    Checkbox_Extended_Table = Checkbutton(Window_Frecuences_Table , text="Tabla Extendida", font=("Times New Roman" , 13) , bg="#FEE1AB" , variable=Checked_Extended_Table , command=Only_Check_Extended)
    Checkbox_Extended_Table.place(x=240 , y=170)
    Checkbox_Extended_Table.config(state="disabled")

    Checkbox_For_Many_Values = Checkbutton(Window_Frecuences_Table , text="Para muchas variables" , font=("Times New Roman" , 13) , bg="#FEE1AB" , variable=Checked_Cuant_For_Many_Values , command=Only_Check_Many_Values)
    Checkbox_For_Many_Values.config(state="disabled")

    Checkbox_Cuantitative_Discret = Checkbutton(Window_Frecuences_Table , text="Discreta" , font=("Times New Roman" , 13) , bg="#FEE1AB" , variable=Checked_Cuantitative_Discret , command=Only_Check_Cuant_Discret)
    Checkbox_Cuantitative_Discret.config(state="disabled")
    Checkbox_Cuantitative_Continuous = Checkbutton(Window_Frecuences_Table , text="Continua" , font=("Times New Roman" , 13) , bg="#FEE1AB" , variable=Checked_Cuantitative_Continuous , command=Only_Check_Cuant_Continuous)
    Checkbox_Cuantitative_Continuous.config(state="disabled")

    Btn_Select_File = Button(Window_Frecuences_Table , text="Seleccionar datos de un Excel" , font=("Times New Roman" , 13) , width=24 , bg="#EBF3F7" , command= lambda: W_Select_File.Create_Window_Select_File(Window_Frecuences_Table , Data , Input_Data , Btn_Select_File))
    Btn_Select_File.place(x=860 , y=170)

    Btn_Calculate_Again = Button(Window_Frecuences_Table , text="Calcular con otros valores" , font=("Times New Roman" , 13) , width=20 , bg="#F4B0C0" , command= lambda: Calculate_Again(Dictionary_Tables))
    Btn_Calculate_Again.place(x=780 , y=210)
    Btn_Calculate_Again.config(state="disabled")

    Btn_Generate_Table = Button(Window_Frecuences_Table , text="Generar Tabla" , font=("Times New Roman" , 13) , width=16 , bg="#F4B0C0" , command= lambda: Create_Table(Precision , Data , Dictionary_Tables)) # Si no colocas lambda: o colocas parentesis a la funcion, esta se ejecuta cuando el boton se crea, y puede generar problemas
    Btn_Generate_Table.place(x=1020 , y=210)

    Section_Frecuences_Table = Label(Window_Frecuences_Table , width=168 , height=25 , bg="#FEE1AB" , highlightthickness=2 , highlightbackground="#000000")
    Section_Frecuences_Table.place(x=29 , y=255)

    Btn_Generate_Excel = Button(Window_Frecuences_Table , text="Exportar tabla en Excel" , font=("Times New Roman" , 13) , bg="#EBF3F7" , command= lambda: Generate_Window_Export_Excel(Window_Frecuences_Table , Global_Calcs , Global_Type_Of_Variable))
    Btn_Generate_Excel.place(x=800 , y=275)
    Btn_Generate_Excel.config(state="disabled")

    Btn_Show_Graph = Button(Window_Frecuences_Table , text="Mostrar grafico" , font=("Times New Roman" , 13) , bg="#EBF3F7" , command= lambda: W_Show_Graph.Create_Window_Show_Graph(Window_Frecuences_Table , Global_Calcs , Precision.get()))
    Btn_Show_Graph.place(x=1051 , y=275)
    Btn_Show_Graph.config(state="disabled")

    """ Tabla para Variables Cuantitativas Continuas o Discretas con muchos datos """
    Table_Cuantitative_For_Many_Values = TreeviewFrame(Window_Frecuences_Table)

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

    Table_Cuantitative_For_Many_Values.treeview.config(height=13)

    for a in range(1 , 12):
        Table_Cuantitative_For_Many_Values.treeview.column(f"{a}" , anchor="center" , width=104)

    """ Tabla para Variables Cuantitativas Discretas con pocos datos de frecuencia """
    Table_Cuantitative_Normal = TreeviewFrame(Window_Frecuences_Table)

    Table_Cuantitative_Normal.treeview.config(columns=("1", "2" ,"3", "4") , show="headings")
    Table_Cuantitative_Normal.treeview.heading("1" , text="xi")
    Table_Cuantitative_Normal.treeview.heading("2" , text="fi")
    Table_Cuantitative_Normal.treeview.heading("3" , text="hi")
    Table_Cuantitative_Normal.treeview.heading("4" , text="hi%")

    Table_Cuantitative_Normal.treeview.config(height=13)

    for a in range(1 ,5):
        Table_Cuantitative_Normal.treeview.column(f"{a}" , anchor="center" , width=285)

    """ Tabla para Variables Cuantitativas Discretas con muchos datos de frecuencia """
    Table_Cuantitative_Extended = TreeviewFrame(Window_Frecuences_Table)

    Table_Cuantitative_Extended.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7") , show="headings")
    Table_Cuantitative_Extended.treeview.heading("1" , text="xi")
    Table_Cuantitative_Extended.treeview.heading("2" , text="fi")
    Table_Cuantitative_Extended.treeview.heading("3" , text="Fi")
    Table_Cuantitative_Extended.treeview.heading("4" , text="hi")
    Table_Cuantitative_Extended.treeview.heading("5" , text="Hi")
    Table_Cuantitative_Extended.treeview.heading("6" , text="hi%")
    Table_Cuantitative_Extended.treeview.heading("7" , text="HI%")

    Table_Cuantitative_Extended.treeview.config(height=13)

    for a in range(1 , 8):
        Table_Cuantitative_Extended.treeview.column(f"{a}" , anchor="center" , width=163)
    
    """ Tabla Cualitativa con pocos datos de frecuencia"""
    Table_Cualitative_Normal = TreeviewFrame(Window_Frecuences_Table)

    Table_Cualitative_Normal.treeview.config(columns=("1", "2" ,"3", "4") , show="headings")
    Table_Cualitative_Normal.treeview.heading("1" , text="ai")
    Table_Cualitative_Normal.treeview.heading("2" , text="fi")
    Table_Cualitative_Normal.treeview.heading("3" , text="hi")
    Table_Cualitative_Normal.treeview.heading("4" , text="hi%")

    Table_Cualitative_Normal.treeview.config(height=13)

    for a in range(1 , 5):
        Table_Cualitative_Normal.treeview.column(f"{a}" , anchor="center" , width=285)
    """ Tabla Cualitativa con mas datos de frecuencia """
    Table_Cualitative_Extended = TreeviewFrame(Window_Frecuences_Table)

    Table_Cualitative_Extended.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7") , show="headings")
    Table_Cualitative_Extended.treeview.heading("1" , text="ai")
    Table_Cualitative_Extended.treeview.heading("2" , text="fi")
    Table_Cualitative_Extended.treeview.heading("3" , text="Fi")
    Table_Cualitative_Extended.treeview.heading("4" , text="hi")
    Table_Cualitative_Extended.treeview.heading("5" , text="Hi")
    Table_Cualitative_Extended.treeview.heading("6" , text="hi%")
    Table_Cualitative_Extended.treeview.heading("7" , text="HI%")

    Table_Cualitative_Extended.treeview.config(height=13)

    for a in range(1 , 8):
        Table_Cualitative_Extended.treeview.column(f"{a}" , anchor="center" , width=163)

    style = ttk.Style()
    style.configure("Treeview.Heading" , font=("Arial" , 10) , padding=(5 , 10))

    style.map("Treeview",
            foreground=[("selected", "black")],
            background=[("selected", "skyblue")])

    Dictionary_Tables = dict(
        Cuantitative_For_Many_Values = Table_Cuantitative_For_Many_Values,
        Cuantitative_Normal = Table_Cuantitative_Normal,
        Cuantitative_Extended = Table_Cuantitative_Extended,
        Cualitative_Normal = Table_Cualitative_Normal,
        Cualitative_Extended = Table_Cualitative_Extended,
    )

    Btn_Back = Button(Window_Frecuences_Table , text="Volver", font=("Times New Roman" , 12) , command=Back_to_main_window , width=134 , bg="#F4B0C0")
    Btn_Back.place(x=10 , y=660)

    Window_Frecuences_Table.protocol("WM_DELETE_WINDOW" , Back_to_main_window)
    Window_Frecuences_Table.resizable(False,False)
    Window_Frecuences_Table.mainloop()