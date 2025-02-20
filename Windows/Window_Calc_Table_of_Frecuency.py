import sys
import os
import numpy
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Calcs.Calc_Values_Tables import *
from Window_Export_Excel import Generate_Window_Export_Excel
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Windows.Window_Import_Excel as W_Import_Excel
import Window_Show_Graph as W_Show_Graph

# Variables Globales
Labels_Window_Frecuences_Table = []
Global_Calcs_From_Single_Column = {}
Global_Calcs_From_Multiple_Columns = {}
Global_Type_Of_Variable_Single_Column = "" # Obtiene el tipo de variable, solo para analisis que involucren una columna de datos
Global_Type_Of_Variable_Multiple_Column = {} # Obtiene el tipo de variable, solo para analisis que involucren multiples columnas de datos
Global_Tables = {} # Se encarga de almacenar todos los calculos y tablas que resultan de cada columna analizada
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
        self.place(x=40 , y=430)

    def Hidden(self):
        self.place_forget()

class Process_Column_Of_Data:
    def __init__(self , Root_Window, Table , Input):
        self.Root_Window = Root_Window
        self.Results = {}
        self.Type_Of_Variable = None
        self.Table = Table # de la clase TreeviewFrame
        self.Labels = []
        self.Input = Input
        self.Precision = 3

    def Calc_Results(self , Precision):
        self.Precision = Precision
        if(isinstance(self.Input , dict)):
            Results = Main_Function(self.Input["S_Column"])
        else:
            Results = Main_Function(self.Input)

        if(Results["Frecuences_Cuant_For_Many_Values"] != None):
            self.Type_Of_Variable = "Cuantitative_Grouped"
        elif(Results["Frecuences_Cuant_Normal_Extended"] != None):
            self.Type_Of_Variable = "Cuantitative_Not_Grouped"
        elif(Results["Frecuences_Cuali_Normal_Extended"] != None):
            self.Type_Of_Variable = "Cualitative"

        Without_None = {}
        for key,value in Results.items():
            if(value != None):
                Without_None[key] = value

        self.Results = Without_None

    def Table_For_Cuant_Grouped_Data(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold") , background="lightblue")

        self.Table.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10", "11") , show="headings")
        self.Table.treeview.heading("1" , text="m")
        self.Table.treeview.heading("2" , text="Li")
        self.Table.treeview.heading("3" , text="Ls")
        self.Table.treeview.heading("4" , text="Grupos")
        self.Table.treeview.heading("5" , text="xi")
        self.Table.treeview.heading("6" , text="fi")
        self.Table.treeview.heading("7" , text="Fi")
        self.Table.treeview.heading("8" , text="hi")
        self.Table.treeview.heading("9" , text="Hi")
        self.Table.treeview.heading("10" , text="hi%")
        self.Table.treeview.heading("11" , text="HI%")

        self.Table.treeview.config(height=13)

        for a in range(1 , 12):
            self.Table.treeview.column(f"{a}" , anchor="center" , width=104)

    def Put_Data_On_Table_For_Cuant_Grouped_Data(self):
        Variables = self.Results["Variables_Cuant_For_Many_Values"]
        Frecuences = self.Results["Frecuences_Cuant_For_Many_Values"]

        if(not self.Table.Has_Rows()):
            self.Table.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            for a in range(0 , Variables["m"]):
                self.Table.treeview.insert(
                    "", END , values=(
                        a+1, 
                        Frecuences["Intervals"][a][0], 
                        Frecuences["Intervals"][a][1], 
                        Frecuences["Groups"][a], 
                        round(Frecuences["xi"][a] , self.Precision),
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        round(Frecuences["hi"][a] , self.Precision),
                        round(Frecuences["Hi"][a] , self.Precision),
                        f"{round(Frecuences['hi_percent'][a] , self.Precision)}%",
                        f"{round(Frecuences['Hi_percent'][a] , self.Precision)}%",)
                ,tags=("font_arial_10",))

            self.Table.treeview.insert(
                "" , END , values=(
                    "Total",
                    "",
                    "",
                    "",
                    "",
                    numpy.sum(Frecuences["fi"]),
                    "",
                    round(numpy.sum(Frecuences["hi"])),
                    "",
                    f"{round(numpy.sum(Frecuences['hi_percent']))}%",
                    "",
                ),tags=("font_arial_10",))

            # Crear un tag para aplicar la negrita
            self.Table.treeview.tag_configure("last_row", font=("Arial", 10, "bold") , background="lightgreen")

            last_item = self.Table.treeview.get_children()[-1]  # Obtener la última fila
            self.Table.treeview.item(last_item, tags=("last_row",))

            for col in self.Table.treeview["columns"]:
                    self.Table.treeview.column(col, anchor="center")

    def Table_For_Cuant_Not_Grouped_Data(self):
        self.Table.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7") , show="headings")
        self.Table.treeview.heading("1" , text="xi")
        self.Table.treeview.heading("2" , text="fi")
        self.Table.treeview.heading("3" , text="Fi")
        self.Table.treeview.heading("4" , text="hi")
        self.Table.treeview.heading("5" , text="Hi")
        self.Table.treeview.heading("6" , text="hi%")
        self.Table.treeview.heading("7" , text="HI%")

        self.Table.treeview.config(height=13)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        for a in range(1 , 8):
            self.Table.treeview.column(f"{a}" , anchor="center" , width=163)
        
    def Put_Data_On_Table_For_Cuant_Not_Grouped_Data(self):
        Variables = self.Results["Variables_Cuant_Normal_Extended"]
        Frecuences = self.Results["Frecuences_Cuant_Normal_Extended"]
        if(not self.Table.Has_Rows()):
            self.Table.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            for a in range(0 , Variables["Number_Statistic_Variables"]):
                self.Table.treeview.insert(
                    "", END , values=(
                        Frecuences["xi"][a],
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        round(Frecuences["hi"][a] , self.Precision),
                        round(Frecuences["Hi"][a] , self.Precision),
                        f"{round(Frecuences['hi_percent'][a] , self.Precision)}%",
                        f"{round(Frecuences['Hi_percent'][a] , self.Precision)}%",) , tags=("font_arial_10",))
            self.Table.treeview.insert(
                "" , END , values=(
                    "Total",
                    numpy.sum(Frecuences["fi"]),
                    "",
                    round(numpy.sum(Frecuences["hi"])),
                    "",
                    f"{round(numpy.sum(Frecuences['hi_percent']))}%",
                    "",
                )
            )

            self.Table.treeview.tag_configure("last_row", font=("Arial", 10, "bold") , background="lightgreen")

            last_item = self.Table.treeview.get_children()[-1]  # Obtener la última fila
            self.Table.treeview.item(last_item, tags=("last_row",))

            for col in self.Table.treeview["columns"]:
                self.Table.treeview.column(col, anchor="center")

    def Table_For_Cualitative_Data(self):
        self.Table.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7") , show="headings")
        self.Table.treeview.heading("1" , text="ai")
        self.Table.treeview.heading("2" , text="fi")
        self.Table.treeview.heading("3" , text="Fi")
        self.Table.treeview.heading("4" , text="hi")
        self.Table.treeview.heading("5" , text="Hi")
        self.Table.treeview.heading("6" , text="hi%")
        self.Table.treeview.heading("7" , text="HI%")

        self.Table.treeview.config(height=13)

        for a in range(1 , 8):
            self.Table.treeview.column(f"{a}" , anchor="center" , width=163)

    def Put_Data_On_Table_For_Cualitative_Data(self):
        Variables = self.Results["Variables_Cuali_Normal_Extended"]
        Frecuences = self.Results["Frecuences_Cuali_Normal_Extended"]
        if(not self.Table.Has_Rows()):
            self.Table.treeview.tag_configure("font_arial_10", font=("Arial", 10))
            for a in range(0 , Variables["N_Character_Modalities"]):
                self.Table.treeview.insert(
                    "", END , values=(
                        Frecuences["ai"][a],
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        round(Frecuences["hi"][a] , self.Precision),
                        round(Frecuences["Hi"][a] , self.Precision),
                        f"{round(Frecuences['hi_percent'][a] , self.Precision)}%",
                        f"{round(Frecuences['Hi_percent'][a] , self.Precision)}%",) , tags=("font_arial_10",))
            self.Table.treeview.insert(
                "" , END , values=(
                    "Total",
                    numpy.sum(Frecuences["fi"]),
                    "",
                    round(numpy.sum(Frecuences["hi"])),
                    "",
                    f"{round(numpy.sum(Frecuences['hi_percent']))}%",
                    "",
                )
            )

            self.Table.treeview.tag_configure("last_row", font=("Arial", 10, "bold") , background="lightgreen")

            last_item = self.Table.treeview.get_children()[-1]  # Obtener la última fila
            self.Table.treeview.item(last_item, tags=("last_row",))

            for col in self.Table.treeview["columns"]:
                self.Table.treeview.column(col, anchor="center")

    def Create_Tables(self):
        match(self.Type_Of_Variable):
            case "Cuantitative_Grouped":
                self.Table_For_Cuant_Grouped_Data()
            case "Cuantitative_Not_Grouped":
                self.Table_For_Cuant_Not_Grouped_Data()
            case "Cualitative":
                self.Table_For_Cualitative_Data()
            case _:
                raise Exception("No se pudo identificar el tipo de variable.")

        style = ttk.Style()
        style.configure("Treeview.Heading" , font=("Arial" , 10) , padding=(5 , 10))

        style.map("Treeview",
                foreground=[("selected", "black")],
                background=[("selected", "skyblue")])

    def Put_Data_On_Tables(self):
        if(self.Table.Has_Rows()):
            self.Table.clear_table()

        match(self.Type_Of_Variable):
            case "Cuantitative_Grouped":
                self.Put_Data_On_Table_For_Cuant_Grouped_Data()
            case "Cuantitative_Not_Grouped":
                self.Put_Data_On_Table_For_Cuant_Not_Grouped_Data()
            case "Cualitative":
                if(self.Results["Variables_Cuali_Normal_Extended"] != None):
                    self.Put_Data_On_Table_For_Cualitative_Data()
            case _:
                raise Exception("No se pudo identificar el tipo de variable.")

    def Display_Table(self):
        self.Table.Display()
    def Hidden_Table(self):
        self.Table.Hidden()

    def Destroy_Labels(self):
        if(len(self.Labels) != 0):
            for a in range(0 , len(self.Labels)):
                self.Labels[a].destroy()
            self.Labels = []
    
    def Label_SM_For_Grouped_Data(self , S_Measures):
        self.Destroy_Labels()
        if(self.Precision >=3 and self.Precision<5):
            Precision = 2
        elif(self.Precision>=5 and self.Precision<7):
            Precision = 4
        elif(self.Precision>=7 and self.Precision<=8):
            Precision = 6
        b=0
        for key,value in S_Measures.items():
            if(b < 3):
                lab = Label(self.Root_Window , text=f"{key}\n{round(value , Precision)}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
            elif(b == 3):
                if(len(value) > 1):
                    sub=1
                    String = ""
                    for a in range(0 , len(value)):
                        if(a >= 3 or a == len(value) - 1):
                            String += f"Mo_{sub}: {round(value[a] , Precision)}"
                            break
                        else:
                            String += f"Mo_{sub}: {round(value[a] , Precision)}\n"
                        sub += 1
                    lab = Label(self.Root_Window , text=f"{key}\n{String}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)

                else:
                    lab = Label(self.Root_Window , text=f"{key}\nMo: {round(value[0] , Precision)}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)

            elif(b < 6):
                lab = Label(self.Root_Window , text=f"{key}\n{round(value , Precision)}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
            else:
                lab = Label(self.Root_Window , text=f"{key}\n{round(value , Precision)}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
            self.Labels.append(lab)
            b +=1

    def Create_Labels_Summary_Measures(self):
        match(self.Type_Of_Variable):
            case "Cuantitative_Grouped":
                    S_Measures = self.Results["Summary_Measures_For_Grouped_Data"]
                    self.Label_SM_For_Grouped_Data(S_Measures)
            case "Cuantitative_Not_Grouped":
                    S_Measures = self.Results["Summary_Measures_For_Not_Grouped_Data"]
                    self.Label_SM_For_Grouped_Data(S_Measures)
            case "Cualitative":
                pass
            case _:
                raise Exception("No se pudo identificar el tipo de variable.")

    def Display_Labels(self):
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            b = 0
            for lab in self.Labels:
                if(b < 3):
                    x_pos = 31+(280*b)
                    lab.place(x=x_pos , y=260)
                elif(b == 3):
                    x_pos = 40+(280*b) - (280*3)
                    lab.place(x=x_pos , y=320)
                elif(b < 6):
                    x_pos = 40 + (280*b) - (280*3)
                    lab.place(x=x_pos , y=320)
                else:
                    x_pos = 40 + (280*b) - (280*5)
                    lab.place(x=x_pos , y=380)
                b += 1

    def Hidden_Labels(self):
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            for lab in self.Labels:
                lab.place_forget()
            
    def Destroy_Tables(self):
        self.Table.destroy()

def Create_Window_Frecuences_Table(Main_Window):
    Main_Window.state(newstate="withdraw")

    def Back_to_main_window():
        Window_Frecuences_Table.destroy()
        Main_Window.state(newstate="normal")
        Main_Window.geometry("1240x700+135+100")
        Main_Window.title("StatApp beta v1.6")
        Main_Window.lift()

    def Display_Table_For_Column_Name(Event):
        Selection = Column_Selection.get()
        for t in Global_Tables.values():
            t.Hidden_Labels()
            t.Hidden_Table()
        Global_Tables[f"{Selection}"].Display_Labels()
        Global_Tables[f"{Selection}"].Display_Table()
        Precision.set(Global_Tables[f"{Selection}"].Precision)

    def Create_Table_For_Single_Column(Precision , Input , Data_From_Single_Column):
        global Global_Tables
        if(Global_Tables == {}):
            Table_For_Data_Column = TreeviewFrame(Window_Frecuences_Table)
            if(Data_From_Single_Column != {}):
                Table_Single_Column = Process_Column_Of_Data(Window_Frecuences_Table , Table_For_Data_Column , Data_From_Single_Column["S_Column"])
            else:
                Table_Single_Column = Process_Column_Of_Data(Window_Frecuences_Table , Table_For_Data_Column , Input)
            Table_Single_Column.Calc_Results(Precision)
            Table_Single_Column.Create_Tables()
            Table_Single_Column.Create_Labels_Summary_Measures()
            Table_Single_Column.Put_Data_On_Tables()
            Table_Single_Column.Display_Labels()
            Table_Single_Column.Display_Table()

            Global_Tables["S_Column"] = Table_Single_Column

            return Global_Tables["S_Column"].Results , Global_Tables["S_Column"].Type_Of_Variable
        else:
            Global_Tables["S_Column"].Precision = Precision
            Global_Tables["S_Column"].Create_Labels_Summary_Measures()
            Global_Tables["S_Column"].Put_Data_On_Tables()

            Global_Tables["S_Column"].Display_Labels()

    def Create_Table_For_Multiple_Columns(Precision , Data_From_Multiple_Columns):
        global Global_Tables
        Results_For_Multiple_Columns = {}
        Type_Of_Variable_For_Multiple_Columns = {}
        if(Global_Tables == {}):
            for key,values in Data_From_Multiple_Columns.items():
                Table_Multiple_Columns = None
                Table = None
                Table = TreeviewFrame(Window_Frecuences_Table)
                Table_Multiple_Columns = Process_Column_Of_Data(Window_Frecuences_Table , Table , values)
                Table_Multiple_Columns.Calc_Results(Precision)
                Table_Multiple_Columns.Create_Tables()
                Table_Multiple_Columns.Create_Labels_Summary_Measures()
                Table_Multiple_Columns.Put_Data_On_Tables()

                Global_Tables[f"{key}"] = Table_Multiple_Columns
                Results_For_Multiple_Columns[f"{key}"] = Table_Multiple_Columns.Results
                Type_Of_Variable_For_Multiple_Columns[f"{key}"] = Table_Multiple_Columns.Type_Of_Variable
                Columns_Name.append(f"{key}")

            Text_Column_Selection.place(x=40 , y=130)
            Column_Selection.place(x=300 , y=130)
            Column_Selection.set(Columns_Name[0])
            Column_Selection["values"] = Columns_Name

            Display_Table_For_Column_Name(None)

            return Results_For_Multiple_Columns , Type_Of_Variable_For_Multiple_Columns
        else:
            Selection = Column_Selection.get()
            Global_Tables[f"{Selection}"].Precision = Precision
            Global_Tables[f"{Selection}"].Create_Labels_Summary_Measures()
            Global_Tables[f"{Selection}"].Put_Data_On_Tables()

            Global_Tables[f"{Selection}"].Display_Labels()

    def Create_Table(Precision , Input , Data_From_Single_Column , Data_From_Multiple_Columns):
        global Global_Calcs_From_Single_Column , Global_Calcs_From_Multiple_Columns , Global_Type_Of_Variable_Single_Column , Global_Type_Of_Variable_Multiple_Column
        try:
            
            Input = str(Input.get())
            if(Input == ""):
                raise Exception("No se han ingresado datos")
            try:
                Precision = int(Precision.get())
            except Exception:
                raise Exception("Valor de precision invalida, intente nuevamente.")

            if(Data_From_Multiple_Columns == {}):
                if(Global_Calcs_From_Single_Column == {} and Global_Type_Of_Variable_Single_Column == {}):
                    Dictionary_Values , Type_Of_Variable = Create_Table_For_Single_Column(Precision , Input , Data_From_Single_Column)
                    Global_Type_Of_Variable_Single_Column = Type_Of_Variable
                    Global_Calcs_From_Single_Column = Dictionary_Values
                else:
                    Create_Table_For_Single_Column(Precision , Input , Data_From_Single_Column)
            else:
                if(Global_Calcs_From_Multiple_Columns == {} and Global_Type_Of_Variable_Multiple_Column == {}):
                    Dictionary_Values , Type_Of_Variable = Create_Table_For_Multiple_Columns(Precision , Data_From_Multiple_Columns)
                    Global_Type_Of_Variable_Multiple_Column = Type_Of_Variable
                    Global_Calcs_From_Multiple_Columns = Dictionary_Values
                else:
                    Create_Table_For_Multiple_Columns(Precision , Data_From_Multiple_Columns)

        except (IndexError , ValueError , NameError , TypeError , Exception) as e:
            messagebox.showerror("Error" , f"{e}")
        else:
            Btn_Calculate_Again.config(state="normal")
            Input_Data.config(state="disabled")

            Btn_Generate_Table.config(state="disabled")
            Btn_Generate_Excel.config(state="normal")
            Btn_Show_Graph.config(state="normal")
            Btn_Import_Data_From_File.config(state="disabled")

    def Calculate_Again(Columns_Name , Column_Selection , Data_From_Multiple_Columns):
        global Global_Calcs_From_Single_Column , Global_Calcs_From_Multiple_Columns , Global_Type_Of_Variable , Global_Tables
        Btn_Calculate_Again.config(state="disabled")

        Input_Data.config(state="normal")
        Input_Data.delete(0 , END)
        Precision.set(3)
        Btn_Import_Data_From_File.config(state="normal")
        Global_Calcs_From_Single_Column.clear()
        Global_Calcs_From_Multiple_Columns.clear()
        Global_Type_Of_Variable = ""
        Column_Selection.set("")
        Column_Selection['values'] = tuple([])
        Columns_Name.clear() # NOTA: Usa clear() para limpiar correctamente todos los valores dentro de la variable
        Column_Selection.update()
        Text_Column_Selection.place_forget()
        Column_Selection.place_forget()
        Data_From_Multiple_Columns.clear()
        Data_From_Single_Column.clear()
        Graphs.clear()

        for t in Global_Tables.values():
            t.Destroy_Labels()
            t.Destroy_Tables()
            t = None

        Global_Tables.clear()

        Btn_Generate_Table.config(state="normal")
        Btn_Generate_Excel.config(state="disabled")
        Btn_Show_Graph.config(state="disabled")

    def Interact_Precision():
        if(Global_Calcs_From_Single_Column != {} or Global_Calcs_From_Multiple_Columns != {}):
            Create_Table(Precision , Data , Data_From_Multiple_Columns)

    Window_Frecuences_Table = Toplevel(Main_Window)
    Window_Frecuences_Table.geometry("1240x800+135+40") # Hacer mas ancha la ventana
    Window_Frecuences_Table.title("Tabla de frecuencias")
    Window_Frecuences_Table.config(bg="#6C6E72")
    Icon = PhotoImage(file="Images/icon.png")
    Window_Frecuences_Table.iconphoto(False , Icon)

    Data = StringVar(Window_Frecuences_Table) # Estos datos se introducen como texto en el campo de texto de la ventana
    Data.set("")
    Precision = IntVar(Window_Frecuences_Table)
    Columns_Name = []
    Data_From_Multiple_Columns = {}
    Data_From_Single_Column = {}
    Graphs = {}

    Title = Label(Window_Frecuences_Table , text="Calculo de Tablas de Frecuencia" , font=("Times New Roman" , 22), foreground="#ffffff", justify=CENTER , width=76 , bg="#9DAEC6" , highlightthickness=1 ,highlightbackground="#ffffff")
    Title.place(x=9 , y=10)

    Section_Input = Label(Window_Frecuences_Table , width=168 ,height=30, bg="#FEE1AB" , highlightthickness=2 , highlightbackground="#000000")
    Section_Input.place(x=29 , y=65)


    Text_Input_Data = Label(Window_Frecuences_Table , text="Ingrese los valores:", font=("Times New Roman" , 13) , bg="#FEE1AB")
    Text_Input_Data.place(x=40 , y=90)
    Input_Data = Entry(Window_Frecuences_Table , textvariable=Data , border=1 , cursor="xterm" , width=100 , font=("Courier New" , 13) , bg="#ffffff" , relief="sunken")
    Input_Data.place(x=180 , y=90)
    Input_Data.focus()

    Text_Column_Selection = Label(Window_Frecuences_Table , text="Seleccione el nombre de la columna: " , font=("Times New Roman", 13) , bg="#FEE1AB")
    Column_Selection = ttk.Combobox(Window_Frecuences_Table , font=("Courier New" , 13) , values=Columns_Name , state="readonly" , width=40)
    Column_Selection.bind('<<ComboboxSelected>>', Display_Table_For_Column_Name)

    Text_Input_Precision_Results = Label(Window_Frecuences_Table , text="Precision:" , font=("Times New Roman" , 13) , bg="#FEE1AB")
    Text_Input_Precision_Results.place(x=840 , y=130)
    Input_Precision_Results = Spinbox(Window_Frecuences_Table , width=10 , textvariable=Precision , from_=3 , to=8 , increment=1 , font=("Courier New" , 13) , bg="#ffffff" , command= lambda: Interact_Precision())
    Input_Precision_Results.place(x=980 , y=130)

    Section_Frecuences_Table = Label(Window_Frecuences_Table , width=168 , height=32 , bg="#CBEFE3" , highlightthickness=2 , highlightbackground="#000000")
    Section_Frecuences_Table.place(x=29 , y=255)

    Btn_Import_Data_From_File = Button(Window_Frecuences_Table , text="Importar datos de un Excel" , font=("Times New Roman" , 13) , width=24 , bg="#EBF3F7" , command= lambda: W_Import_Excel.Create_Window_Import_Excel(Window_Frecuences_Table , Data , Input_Data , Data_From_Single_Column , Data_From_Multiple_Columns))
    Btn_Import_Data_From_File.place(x=860 , y=170)

    Btn_Calculate_Again = Button(Window_Frecuences_Table , text="Calcular con otros valores" , font=("Times New Roman" , 13) , width=20 , bg="#F4B0C0" , command= lambda: Calculate_Again(Columns_Name , Column_Selection , Data_From_Multiple_Columns))
    Btn_Calculate_Again.place(x=780 , y=210)
    Btn_Calculate_Again.config(state="disabled")

    Btn_Generate_Table = Button(Window_Frecuences_Table , text="Generar Tabla" , font=("Times New Roman" , 13) , width=16 , bg="#F4B0C0" , command= lambda: Create_Table(Precision , Data , Data_From_Single_Column , Data_From_Multiple_Columns)) # Si no colocas lambda: o colocas parentesis a la funcion, esta se ejecuta cuando el boton se crea, y puede generar problemas
    Btn_Generate_Table.place(x=1020 , y=210)

    Btn_Generate_Excel = Button(Window_Frecuences_Table , text="Exportar tabla a Excel" , font=("Times New Roman" , 13) , bg="#EBF3F7" , command= lambda: Generate_Window_Export_Excel(Window_Frecuences_Table , Global_Calcs_From_Single_Column , Global_Calcs_From_Multiple_Columns , Global_Type_Of_Variable_Single_Column , Global_Type_Of_Variable_Multiple_Column))
    Btn_Generate_Excel.place(x=800 , y=275)
    Btn_Generate_Excel.config(state="disabled")

    Btn_Show_Graph = Button(Window_Frecuences_Table , text="Mostrar grafico" , font=("Times New Roman" , 13) , bg="#EBF3F7" , command= lambda: W_Show_Graph.Create_Windows_Show_Graphs(Window_Frecuences_Table , Global_Calcs_From_Single_Column , Global_Calcs_From_Multiple_Columns , Precision.get() , Graphs))
    Btn_Show_Graph.place(x=1051 , y=275)
    Btn_Show_Graph.config(state="disabled")

    Btn_Back = Button(Window_Frecuences_Table , text="Volver", font=("Times New Roman" , 12) , command=Back_to_main_window , width=134 , bg="#F4B0C0")
    Btn_Back.place(x=10 , y=760)

    Window_Frecuences_Table.protocol("WM_DELETE_WINDOW" , Back_to_main_window)
    Window_Frecuences_Table.resizable(False,False)
    Window_Frecuences_Table.mainloop()