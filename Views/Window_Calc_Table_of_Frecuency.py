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
import Views.Window_Import_Excel as W_Import_Excel
import Window_Show_Graph as W_Show_Graph

# Variables Globales
Labels_Window_Frecuences_Table = []
Global_Results_From_Single_Column = {}
Global_Results_From_Multiple_Columns = {}
Global_Type_Of_Variable_Single_Column = "" # Obtiene el tipo de variable, solo para analisis que involucren una columna de datos
Global_Type_Of_Variable_Multiple_Column = {} # Obtiene el tipo de variable, solo para analisis que involucren multiples columnas de datos
Global_Views = {} # Se encarga de almacenar todos los calculos y tablas que resultan de cada columna analizada
#
class TreeviewFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        self.treeview = ttk.Treeview(
            self,
            yscrollcommand=self.vscrollbar.set,
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


class Table_Of_Frecuences:
    def __init__(self , W_Calc_Table_Frec):
        self.W_Calc_Table_Frec = W_Calc_Table_Frec

    def Create_Table_For_Cuantitative_Grouped_Data(self):
        self.Table_Frecuences = TreeviewFrame(self.W_Calc_Table_Frec)

        self.Table_Frecuences.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10", "11") , show="headings")
        self.Table_Frecuences.treeview.heading("1" , text="m")
        self.Table_Frecuences.treeview.heading("2" , text="Li")
        self.Table_Frecuences.treeview.heading("3" , text="Ls")
        self.Table_Frecuences.treeview.heading("4" , text="Grupos")
        self.Table_Frecuences.treeview.heading("5" , text="xi")
        self.Table_Frecuences.treeview.heading("6" , text="fi")
        self.Table_Frecuences.treeview.heading("7" , text="Fi")
        self.Table_Frecuences.treeview.heading("8" , text="hi")
        self.Table_Frecuences.treeview.heading("9" , text="Hi")
        self.Table_Frecuences.treeview.heading("10" , text="hi%")
        self.Table_Frecuences.treeview.heading("11" , text="HI%")

        self.Table_Frecuences.treeview.config(height=13)

        for a in range(1 , 12):
            if(a == 1):
                self.Table_Frecuences.treeview.column(f"{a}" , anchor="center" , width=60 , stretch=False)
            elif(a > 1 and a < 5):
                self.Table_Frecuences.treeview.column(f"{a}" , anchor="center" , width=145 , stretch=False)
            elif(a == 6):
                self.Table_Frecuences.treeview.column(f"{a}" , anchor="center" , width=90 , stretch=False)
            elif(a >= 10 and a <= 11):
                self.Table_Frecuences.treeview.column(f"{a}" , anchor="center" , width=118 , stretch=False)
            else:
                self.Table_Frecuences.treeview.column(f"{a}" , anchor="center" , width=118 , stretch=False)

        style = ttk.Style()
        style.configure("Treeview.Heading" , font=("Arial" , 10) , padding=(5 , 10))

        style.map("Treeview",
                foreground=[("selected", "black")],
                background=[("selected", "skyblue")])

    def Create_Table_For_Cuantitative_Not_Grouped_Data(self):
        self.Table_Frecuences = TreeviewFrame(self.W_Calc_Table_Frec)

        self.Table_Frecuences.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7") , show="headings")
        self.Table_Frecuences.treeview.heading("1" , text="xi")
        self.Table_Frecuences.treeview.heading("2" , text="fi")
        self.Table_Frecuences.treeview.heading("3" , text="Fi")
        self.Table_Frecuences.treeview.heading("4" , text="hi")
        self.Table_Frecuences.treeview.heading("5" , text="Hi")
        self.Table_Frecuences.treeview.heading("6" , text="hi%")
        self.Table_Frecuences.treeview.heading("7" , text="HI%")

        self.Table_Frecuences.treeview.config(height=13)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        for a in range(1 , 8):
            self.Table_Frecuences.treeview.column(f"{a}" , anchor="center" , width=185)

        style = ttk.Style()
        style.configure("Treeview.Heading" , font=("Arial" , 10) , padding=(5 , 10))

        style.map("Treeview",
                foreground=[("selected", "black")],
                background=[("selected", "skyblue")])

    def Create_Table_For_Cualitative_Data(self):
        self.Table_Frecuences = TreeviewFrame(self.W_Calc_Table_Frec)

        self.Table_Frecuences.treeview.config(columns=("1", "2" ,"3", "4", "5", "6", "7") , show="headings")
        self.Table_Frecuences.treeview.heading("1" , text="ai")
        self.Table_Frecuences.treeview.heading("2" , text="fi")
        self.Table_Frecuences.treeview.heading("3" , text="Fi")
        self.Table_Frecuences.treeview.heading("4" , text="hi")
        self.Table_Frecuences.treeview.heading("5" , text="Hi")
        self.Table_Frecuences.treeview.heading("6" , text="hi%")
        self.Table_Frecuences.treeview.heading("7" , text="HI%")

        self.Table_Frecuences.treeview.config(height=13)

        for a in range(1 , 8):
            self.Table_Frecuences.treeview.column(f"{a}" , anchor="center" , width=185)

        style = ttk.Style()
        style.configure("Treeview.Heading" , font=("Arial" , 10) , padding=(5 , 10))

        style.map("Treeview",
                foreground=[("selected", "black")],
                background=[("selected", "skyblue")])

    def Put_Data_On_Table_For_Cuantitative_Grouped_Data(self , Results , Precision , Amplitude_N_Decimals):
        if(Amplitude_N_Decimals == None):
            raise Exception("Hubo un error al calcular la tabla de frecuencias.")
    
        self.Table_Frecuences.clear_table()

        Variables = Results["Variables_Cuant_For_Many_Values"]
        Frecuences = Results["Frecuences_Cuant_For_Many_Values"]

        if(not self.Table_Frecuences.Has_Rows()):
            self.Table_Frecuences.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            for a in range(0 , Variables["m"]):
                self.Table_Frecuences.treeview.insert(
                    "", END , values=(
                        a+1, 
                        f"{Frecuences['Intervals'][a][0]:.{Amplitude_N_Decimals}f}", 
                        f"{Frecuences['Intervals'][a][1]:.{Amplitude_N_Decimals}f}", 
                        f"{Frecuences['Groups'][a]:.{Amplitude_N_Decimals}f}", 
                        f"{Frecuences['xi'][a]:.{Precision}f}",
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        f"{Frecuences['hi'][a]:.{Precision}f}",
                        f"{Frecuences['Hi'][a]:.{Precision}f}",
                        f"{Frecuences['hi_percent'][a]:.{Precision}f}%",
                        f"{Frecuences['Hi_percent'][a]:.{Precision}f}%",)
                ,tags=("font_arial_10",))

            self.Table_Frecuences.treeview.insert(
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
            self.Table_Frecuences.treeview.tag_configure("last_row", font=("Arial", 10, "bold") , background="lightgreen")

            last_item = self.Table_Frecuences.treeview.get_children()[-1]  # Obtener la última fila
            self.Table_Frecuences.treeview.item(last_item, tags=("last_row",))

            for col in self.Table_Frecuences.treeview["columns"]:
                    self.Table_Frecuences.treeview.column(col, anchor="center" , stretch=False)

    def Put_Data_On_Table_For_Cuantitative_Not_Grouped_Data(self , Results , Precision):
        self.Table_Frecuences.clear_table()
        
        Variables = Results["Variables_Cuant_Normal_Extended"]
        Frecuences = Results["Frecuences_Cuant_Normal_Extended"]
        
        if(not self.Table_Frecuences.Has_Rows()):
            self.Table_Frecuences.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            for a in range(0 , Variables["Number_Statistic_Variables"]):
                self.Table_Frecuences.treeview.insert(
                    "", END , values=(
                        Frecuences["xi"][a],
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        f"{Frecuences['hi'][a]:.{Precision}f}",
                        f"{Frecuences['Hi'][a]:.{Precision}f}",
                        f"{Frecuences['hi_percent'][a]:.{Precision}f}%",
                        f"{Frecuences['Hi_percent'][a]:.{Precision}f}%",) , tags=("font_arial_10",))
            self.Table_Frecuences.treeview.insert(
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

            self.Table_Frecuences.treeview.tag_configure("last_row", font=("Arial", 10, "bold") , background="lightgreen")

            last_item = self.Table_Frecuences.treeview.get_children()[-1]  # Obtener la última fila
            self.Table_Frecuences.treeview.item(last_item, tags=("last_row",))

            for col in self.Table_Frecuences.treeview["columns"]:
                self.Table_Frecuences.treeview.column(col, anchor="center")

    def Put_Data_On_Table_For_Cualitative_Data(self , Results , Precision):
        self.Table_Frecuences.clear_table()
        
        Variables = Results["Variables_Cuali_Normal_Extended"]
        Frecuences = Results["Frecuences_Cuali_Normal_Extended"]
        if(not self.Table_Frecuences.Has_Rows()):
            self.Table_Frecuences.treeview.tag_configure("font_arial_10", font=("Arial", 10))
            for a in range(0 , Variables["N_Character_Modalities"]):
                self.Table_Frecuences.treeview.insert(
                    "", END , values=(
                        Frecuences["ai"][a],
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        f"{Frecuences['hi'][a]:.{Precision}f}",
                        f"{Frecuences['Hi'][a]:.{Precision}f}",
                        f"{Frecuences['hi_percent'][a]:.{Precision}f}%",
                        f"{Frecuences['Hi_percent'][a]:.{Precision}f}%",) , tags=("font_arial_10",))
            self.Table_Frecuences.treeview.insert(
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

            self.Table_Frecuences.treeview.tag_configure("last_row", font=("Arial", 10, "bold") , background="lightgreen")

            last_item = self.Table_Frecuences.treeview.get_children()[-1]  # Obtener la última fila
            self.Table_Frecuences.treeview.item(last_item, tags=("last_row",))

            for col in self.Table_Frecuences.treeview["columns"]:
                self.Table_Frecuences.treeview.column(col, anchor="center")

    def Display_Table(self):
        self.Table_Frecuences.Display()

    def Hidden_Table(self):
        self.Table_Frecuences.Hidden()

    def Destroy_Table(self):
        self.Table_Frecuences.destroy()


class Checkbox_Is_Continue:
    def __init__(self , W_Calc_Table_Frec):
        self.W_Calc_Table_Frec = W_Calc_Table_Frec
        self.Checkbox_Is_Continue = None
        self.Checked_Is_Continue = BooleanVar(self.W_Calc_Table_Frec)
        self.Checked_Is_Continue.set(False)
    
    def Create_Checkbox(self):
        self.Checkbox_Is_Continue = Checkbutton(self.W_Calc_Table_Frec , text="Variable Cuantitativa Continua" , variable=self.Checked_Is_Continue , font=("Times New Roman" , 13) , bg="#FEE1AB")

    def Display_Checkbox(self):
        if(self.Checkbox_Is_Continue):
            self.Checkbox_Is_Continue.place(x=40 , y=210)
    
    def Hidden_Checkbox(self):
        if(self.Checkbox_Is_Continue):
            self.Checkbox_Is_Continue.place_forget()

    def Destroy_Checkbox(self):
        if(self.Checkbox_Is_Continue):
            self.Checkbox_Is_Continue.destroy()


class Quantiles_Table:
    def __init__(self , W_Calc_Table_Frec):
        self.W_Calc_Table_Frec = W_Calc_Table_Frec
        self.Quartiles_Table = TreeviewFrame(self.W_Calc_Table_Frec)
        self.Deciles_Table = TreeviewFrame(self.W_Calc_Table_Frec)
        self.Percentiles_Table = TreeviewFrame(self.W_Calc_Table_Frec)

        self.Quantiles_Table_Collection = {
            "Q" : ["Cuartiles" , self.Quartiles_Table] ,
            "D" : ["Deciles" , self.Deciles_Table] , 
            "P" : ["Percentiles" , self.Percentiles_Table] ,
        }

    def Build_Table(self , Quantile_Name , Quantile_Initial , Quantile_Table):
        Quantile_Table.treeview.config(columns=("1") , show="headings")
        Quantile_Table.treeview.heading("1" , text=f"{Quantile_Name} ({Quantile_Initial}_k)")

        Quantile_Table.treeview.config(height=6)

        for a in range(1 , 2):
            Quantile_Table.treeview.column(f"{a}" , anchor="center" , width=140)

    def Put_Data_On_Table(self , Quantile_Data , Quantile_Table , Quantile_Initial , Precision):
        Quantile_Table.clear_table()
        if(not Quantile_Table.Has_Rows()):
            Quantile_Table.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            if(not Quantile_Data):
                Quantile_Table.treeview.insert(
                    "", END , values=(
                        "Sin resultados",
                    ))
            else:
                for a in range(0 , len(Quantile_Data)):
                    Quantile_Table.treeview.insert(
                        "", END , values=(
                            f"{Quantile_Initial}_{a+1} = {Quantile_Data[a]:.{Precision}f}",
                        ))

            for col in Quantile_Table.treeview["columns"]:
                Quantile_Table.treeview.column(col, anchor="center")

    def Create_Tables(self):
        if(self.Quantiles_Table_Collection):
            for key , info_table in self.Quantiles_Table_Collection.items():
                self.Build_Table(info_table[0] , key , info_table[1])

    def Put_Data_On_Tables(self , Quantile_Data , Precision):
        if(self.Quantiles_Table_Collection):
            Quantile_Data_Keys = [k for k in Quantile_Data.keys()]
            for i , (key , info_table) in enumerate(self.Quantiles_Table_Collection.items()):
                info_table[1].clear_table()
                self.Put_Data_On_Table(Quantile_Data[f"{Quantile_Data_Keys[i]}"] , info_table[1] , key , Precision)

    def Display_Tables(self):
        if(self.Quantiles_Table_Collection):
            x_pos = 780
            for table in self.Quantiles_Table_Collection.values():
                table[1].place(x=x_pos , y=261)
                x_pos += 200

    def Hidden_Tables(self):
        if(self.Quantiles_Table_Collection):
            for table in self.Quantiles_Table_Collection.values():
                table[1].place_forget()

    def Destroy_Tables(self):
        if(self.Quantiles_Table_Collection):
            for table in self.Quantiles_Table_Collection.values():
                table[1].destroy()


class Labels_Summary_Measures:
    def __init__(self , W_Calc_Table_Frec):
        self.W_Calc_Table_Frec = W_Calc_Table_Frec
        self.Labels_Collection = []

    def Create_Labels(self, S_Measures):
        self.Destroy_Labels()

        b=0
        for key,value in S_Measures.items():
            if(b < 3):
                if(value == "Indeterminado"):
                    lab = Label(self.W_Calc_Table_Frec , text=f"{key}\n{value}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
                else:
                    lab = Label(self.W_Calc_Table_Frec , text=f"{key}\n{value:.{self.Precision}f}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
            elif(b == 3):
                if(len(value) > 1):
                    sub=1
                    String = ""
                    for a in range(0 , len(value)):
                        if(a >= 3 or a == len(value) - 1):
                            String += f"Mo_{sub}: {value[a]:.{self.Precision}f}"
                            break
                        else:
                            String += f"Mo_{sub}: {value[a]:.{self.Precision}f}\n"
                        sub += 1
                    lab = Label(self.W_Calc_Table_Frec , text=f"{key}\n{String}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)

                else:
                    lab = Label(self.W_Calc_Table_Frec , text=f"{key}\nMo: {value[0]:.{self.Precision}f}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)

            elif(b < 6):
                lab = Label(self.W_Calc_Table_Frec , text=f"{key}\n{value:.{self.Precision}f}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
            else:
                lab = Label(self.W_Calc_Table_Frec , text=f"{key}\n{value:.{self.Precision}f}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
            self.Labels_Collection.append(lab)
            b +=1
        
    def Display_Labels(self):
        if(self.Labels_Collection):
            b = 0
            for lab in self.Labels_Collection:
                if(b < 3):
                    x_pos = 40 + (255*b)
                    lab.place(x=x_pos , y=260)
                elif(b == 3):
                    x_pos = 40 + (255*b) - (255*3)
                    lab.place(x=x_pos , y=320)
                elif(b < 6):
                    x_pos = 40 + (255*b) - (255*3)
                    lab.place(x=x_pos , y=320)
                else:
                    x_pos = 40 + (255*b) - (255*5)
                    lab.place(x=x_pos , y=380)
                b += 1

    def Hidden_Labels(self):
        if(self.Labels_Collection):
            for lab in self.Labels_Collection:
                lab.place_forget()

    def Destroy_Labels(self):
        if(self.Labels_Collection):
            for lab in self.Labels_Collection:
                lab.destroy()
            self.Labels_Collection = []


class Process_Column_Of_Data(Table_Of_Frecuences , Labels_Summary_Measures , Quantiles_Table , Checkbox_Is_Continue):
    def __init__(self , W_Calc_Table_Frec , Data_To_Analized , Precision , Variable_Name , Multiple_Columns = False):
        self.W_Calc_Table_Frec = W_Calc_Table_Frec

        self.Data_To_Analized = Data_To_Analized
        self.Precision = Precision
        self.Results = {}
        self.Type_Of_Variable = None
        self.Amplitude_N_Decimals = None
        self.Variable_Name = Variable_Name
        self.Multiple_Columns = Multiple_Columns

        Table_Of_Frecuences.__init__(self, W_Calc_Table_Frec)

        Labels_Summary_Measures.__init__(self, W_Calc_Table_Frec)

        Quantiles_Table.__init__(self , W_Calc_Table_Frec)

        Checkbox_Is_Continue.__init__(self, W_Calc_Table_Frec)
        Checkbox_Is_Continue.Create_Checkbox(self)

    def Calc_Results(self , Repeated_Calc):
        Results = Main_Function(self.Data_To_Analized , [self.Checked_Is_Continue , self.Checkbox_Is_Continue] , Repeated_Calc)

        if(Results["Frecuences_Cuant_For_Many_Values"] != None):
            self.Type_Of_Variable = "Cuantitative_Grouped"
            self.Amplitude_N_Decimals = Results["Variables_Cuant_For_Many_Values"]["C_Decimals_Number"]
        elif(Results["Frecuences_Cuant_Normal_Extended"] != None):
            self.Type_Of_Variable = "Cuantitative_Not_Grouped"
        elif(Results["Frecuences_Cuali_Normal_Extended"] != None):
            self.Type_Of_Variable = "Cualitative"
            self.Checkbox_Is_Continue = None
        
        Without_None = {}
        for key,value in Results.items():
            if(value != None):
                Without_None[key] = value

        self.Results = Without_None

        if(Repeated_Calc):
            Table_Of_Frecuences.Destroy_Table(self)
            Labels_Summary_Measures.Destroy_Labels(self)
            self.Create_Widgets_For_Results(Repeated_Calc)
            self.Put_Data_On_Widgets_For_Results()
            self.Display_Widgets_For_Results()
            self.Update_Global_Results_And_Type_Of_Variable()

    def Update_Global_Results_And_Type_Of_Variable(self):
        global Global_Results_From_Multiple_Columns , Global_Results_From_Single_Column , Global_Type_Of_Variable_Multiple_Column , Global_Type_Of_Variable_Single_Column
        if(self.Variable_Name and self.Multiple_Columns):
            Global_Results_From_Multiple_Columns[f"{self.Variable_Name}"].clear()
            Global_Type_Of_Variable_Multiple_Column[f"{self.Variable_Name}"] = ""

            Global_Results_From_Multiple_Columns[f"{self.Variable_Name}"] = self.Results
            Global_Type_Of_Variable_Multiple_Column[f"{self.Variable_Name}"] = self.Type_Of_Variable
        elif(self.Variable_Name):
            Global_Results_From_Single_Column[f"{self.Variable_Name}"] = self.Results
            Global_Type_Of_Variable_Single_Column = self.Type_Of_Variable
        else:
            Global_Results_From_Single_Column = self.Results
            Global_Type_Of_Variable_Single_Column = self.Type_Of_Variable

    def Activate_Checkbox_Funcionality(self):
        if(self.Checkbox_Is_Continue):
            self.Checkbox_Is_Continue.config(command= lambda: self.Calc_Results(True))

    def Create_Widgets_For_Results(self , Repeated_Calc = False):
        match(self.Type_Of_Variable):
            case "Cuantitative_Grouped":
                Table_Of_Frecuences.Create_Table_For_Cuantitative_Grouped_Data(self)
                if(not Repeated_Calc):
                    Quantiles_Table.Create_Tables(self)
            case "Cuantitative_Not_Grouped":
                Table_Of_Frecuences.Create_Table_For_Cuantitative_Not_Grouped_Data(self)
                if(not Repeated_Calc):
                    Quantiles_Table.Create_Tables(self)
            case "Cualitative":
                Table_Of_Frecuences.Create_Table_For_Cualitative_Data(self)
            case _:
                raise Exception("No se pudo identificar el tipo de variable.")

    def Put_Data_On_Widgets_For_Results(self):
        if(self.Table_Frecuences.Has_Rows()):
            self.Table_Frecuences.clear_table()

        match(self.Type_Of_Variable):
            case "Cuantitative_Grouped":
                S_Measures = self.Results["Summary_Measures_For_Grouped_Data"]
                Quantile_Data = self.Results["Quantiles_For_Grouped_Data"]

                Table_Of_Frecuences.Put_Data_On_Table_For_Cuantitative_Grouped_Data(self , self.Results , self.Precision , self.Amplitude_N_Decimals)
                Labels_Summary_Measures.Create_Labels(self , S_Measures)
                Quantiles_Table.Put_Data_On_Tables(self , Quantile_Data , self.Precision)
            case "Cuantitative_Not_Grouped":
                S_Measures = self.Results["Summary_Measures_For_Not_Grouped_Data"]
                Quantile_Data = self.Results["Quantiles_For_Not_Grouped_Data"]
        
                Table_Of_Frecuences.Put_Data_On_Table_For_Cuantitative_Not_Grouped_Data(self , self.Results , self.Precision)
                Labels_Summary_Measures.Create_Labels(self , S_Measures)
                Quantiles_Table.Put_Data_On_Tables(self , Quantile_Data , self.Precision)
            case "Cualitative":
                Table_Of_Frecuences.Put_Data_On_Table_For_Cualitative_Data(self , self.Results , self.Precision)
            case _:
                raise Exception("No se pudo identificar el tipo de variable.")

    def Display_Widgets_For_Results(self):
        Table_Of_Frecuences.Display_Table(self)
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            Labels_Summary_Measures.Display_Labels(self)
            Quantiles_Table.Display_Tables(self)
            if(self.Checkbox_Is_Continue):
                Checkbox_Is_Continue.Display_Checkbox(self)

    def Hidden_Widgets_For_Results(self):
        Table_Of_Frecuences.Hidden_Table(self)
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            Labels_Summary_Measures.Hidden_Labels(self)
            Quantiles_Table.Hidden_Tables(self)
            if(self.Checkbox_Is_Continue):
                Checkbox_Is_Continue.Hidden_Checkbox(self)

    def Destroy_Widgets_For_Results(self):
        Table_Of_Frecuences.Destroy_Table(self)
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            Labels_Summary_Measures.Destroy_Labels(self)
            Quantiles_Table.Destroy_Tables(self)
            if(self.Checkbox_Is_Continue):
                Checkbox_Is_Continue.Destroy_Checkbox(self)

def Create_Window_Frecuences_Table(Main_Window):
    Main_Window.state(newstate="withdraw")

    def Back_to_main_window():
        Calculate_Again(Columns_Name , Column_Selection , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns)
        for widget in Window_Frecuences_Table.winfo_children():
            widget.destroy()

        Window_Frecuences_Table.grab_release()
        Window_Frecuences_Table.quit()
        Window_Frecuences_Table.destroy()
        Main_Window.state(newstate="normal")
        Main_Window.geometry("1240x700+135+100")
        Main_Window.title("StatPhi beta v1.8")
        Main_Window.lift()

    def Display_Results_By_Column_Name(Event = None):
        Selection = Column_Selection.get()
        for t in Global_Views.values():
            t.Hidden_Widgets_For_Results()

        Global_Views[f"{Selection}"].Display_Widgets_For_Results()
        Precision.set(Global_Views[f"{Selection}"].Precision)

    def Display_Results_For_Single_Column_Data(Precision , Data_From_Widget_Entry , Imported_Data_From_Single_Column):
        global Global_Views
        if(Global_Views == {}):
            if(Imported_Data_From_Single_Column != {}):
                Results_From_Single_Column = {}
                key, value = next(iter(Imported_Data_From_Single_Column.items()))
                Results_On_Window_For_Single_Variable = Process_Column_Of_Data(Window_Frecuences_Table , value , Precision , key) # Para datos importados de Excel
                Results_On_Window_For_Single_Variable.Calc_Results(False)
                Results_From_Single_Column[f"{key}"] = Results_On_Window_For_Single_Variable.Results
            else:
                Results_From_Single_Column = None
                Results_On_Window_For_Single_Variable = Process_Column_Of_Data(Window_Frecuences_Table , Data_From_Widget_Entry , Precision , None) # Para datos ingresados manuamente
                Results_On_Window_For_Single_Variable.Calc_Results(False)
                Results_From_Single_Column = Results_On_Window_For_Single_Variable.Results

            Results_On_Window_For_Single_Variable.Create_Widgets_For_Results()
            Results_On_Window_For_Single_Variable.Put_Data_On_Widgets_For_Results()
            Results_On_Window_For_Single_Variable.Activate_Checkbox_Funcionality()
            Results_On_Window_For_Single_Variable.Display_Widgets_For_Results()

            Global_Views["S_Column"] = Results_On_Window_For_Single_Variable
            
            return Results_From_Single_Column , Global_Views["S_Column"].Type_Of_Variable
        else:
            Global_Views["S_Column"].Precision = Precision
            Global_Views["S_Column"].Put_Data_On_Widgets_For_Results()

            Global_Views["S_Column"].Display_Widgets_For_Results()

    def Display_Results_For_Multiple_Column_Data(Precision , Imported_Data_From_Multiple_Columns):
        global Global_Views
        Results_From_Multiple_Columns = {}
        Type_Of_Variable_For_Multiple_Columns = {}
        if(Global_Views == {}):
            for key , values in Imported_Data_From_Multiple_Columns.items():
                Results_On_Window_For_Multiple_Variables = None

                Results_On_Window_For_Multiple_Variables = Process_Column_Of_Data(Window_Frecuences_Table , values , Precision , key , True)
                Results_On_Window_For_Multiple_Variables.Calc_Results(False)

                Results_On_Window_For_Multiple_Variables.Create_Widgets_For_Results()
                Results_On_Window_For_Multiple_Variables.Put_Data_On_Widgets_For_Results()
                Results_On_Window_For_Multiple_Variables.Activate_Checkbox_Funcionality()

                Global_Views[f"{key}"] = Results_On_Window_For_Multiple_Variables
                Results_From_Multiple_Columns[f"{key}"] = Results_On_Window_For_Multiple_Variables.Results
                Type_Of_Variable_For_Multiple_Columns[f"{key}"] = Results_On_Window_For_Multiple_Variables.Type_Of_Variable
                Columns_Name.append(f"{key}")

            Text_Column_Selection.place(x=40 , y=170)
            Column_Selection.place(x=300 , y=170)
            Column_Selection.set(Columns_Name[0])
            Column_Selection["values"] = Columns_Name

            Display_Results_By_Column_Name()

            return Results_From_Multiple_Columns , Type_Of_Variable_For_Multiple_Columns
        else:
            Selection = Column_Selection.get()
            Global_Views[f"{Selection}"].Precision = Precision
            Global_Views[f"{Selection}"].Put_Data_On_Widgets_For_Results()

            Global_Views[f"{Selection}"].Display_Widgets_For_Results()

    def Display_Results(Precision , Data_From_Widget_Entry , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns):
        global Global_Results_From_Single_Column , Global_Results_From_Multiple_Columns , Global_Type_Of_Variable_Single_Column , Global_Type_Of_Variable_Multiple_Column
        try:
            Data_From_Widget_Entry = str(Data_From_Widget_Entry.get())
            if(Data_From_Widget_Entry == ""):
                raise Exception("No se han ingresado datos")
            try:
                Precision = int(Precision.get())
            except Exception:
                raise Exception("Valor de precision invalida, intente nuevamente.")

            if(not Imported_Data_From_Multiple_Columns):
                if(not Global_Results_From_Single_Column and Global_Type_Of_Variable_Single_Column == ""):
                    Dictionary_Values , Type_Of_Variable = Display_Results_For_Single_Column_Data(Precision , Data_From_Widget_Entry , Imported_Data_From_Single_Column)
                    Global_Type_Of_Variable_Single_Column = Type_Of_Variable
                    Global_Results_From_Single_Column = Dictionary_Values
                else:
                    Display_Results_For_Single_Column_Data(Precision , Data_From_Widget_Entry , Imported_Data_From_Single_Column)

            elif(not Imported_Data_From_Single_Column):
                if(not Global_Results_From_Multiple_Columns and not Global_Type_Of_Variable_Multiple_Column):
                    Dictionary_Values , Type_Of_Variable = Display_Results_For_Multiple_Column_Data(Precision , Imported_Data_From_Multiple_Columns)
                    Global_Type_Of_Variable_Multiple_Column = Type_Of_Variable
                    Global_Results_From_Multiple_Columns = Dictionary_Values
                else:
                    Display_Results_For_Multiple_Column_Data(Precision , Imported_Data_From_Multiple_Columns)
            else:
                raise Exception("No se han ingresado datos.")

        except (IndexError , ValueError , NameError , TypeError , Exception) as e:
            messagebox.showerror("Error" , f"{e}")
            Calculate_Again(Columns_Name , Column_Selection , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns)
        else:
            Input_Data.config(state="disabled")

            Btn_Generate_Table.config(text="Calcular con otros valores")
            Btn_Generate_Excel.config(state="normal")
            Btn_Show_Graph.config(state="normal")
            Btn_Import_Data_From_File.config(state="disabled")

    def Calculate_Again(Columns_Name , Column_Selection , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns):
        global Global_Results_From_Single_Column , Global_Results_From_Multiple_Columns , Global_Type_Of_Variable_Single_Column , Global_Type_Of_Variable_Multiple_Column , Global_Views

        Input_Data.config(state="normal")
        Input_Data.delete(0 , END)
        Precision.set(3)
        Btn_Import_Data_From_File.config(state="normal")

        Imported_Data_From_Multiple_Columns.clear()
        Imported_Data_From_Single_Column.clear()
        Global_Results_From_Single_Column.clear()
        Global_Results_From_Multiple_Columns.clear()
        Global_Type_Of_Variable_Single_Column = ""
        Global_Type_Of_Variable_Multiple_Column.clear()

        Column_Selection.set("")
        Column_Selection['values'] = tuple([])
        Columns_Name.clear() # NOTA: Usa clear() para limpiar correctamente todos los valores dentro de la variable
        Column_Selection.update()

        Text_Column_Selection.place_forget()
        Column_Selection.place_forget()
        Graphs.clear()

        for t in Global_Views.values():
            t.Destroy_Widgets_For_Results()
            t = None

        Global_Views.clear()

        Btn_Generate_Table.config(state="normal")
        Btn_Generate_Excel.config(state="disabled")
        Btn_Show_Graph.config(state="disabled")

    def Interact_Precision():
        global Global_Results_From_Multiple_Columns , Global_Results_From_Single_Column
        if(Global_Results_From_Single_Column or Global_Results_From_Multiple_Columns):
            Display_Results(Precision , Data_From_Widget_Entry , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns)

    def Interact_Btn_Generate_Table(Precision , Data_From_Widget_Entry , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns , Columns_Name , Column_Selection):
        global Global_Results_From_Single_Column , Global_Results_From_Multiple_Columns
        if(Global_Results_From_Multiple_Columns or Global_Results_From_Single_Column):
            Calculate_Again(Columns_Name , Column_Selection , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns)
            Btn_Generate_Table.config(text="Calcular Tabla")
        else:
            Display_Results(Precision , Data_From_Widget_Entry , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns)

    Window_Frecuences_Table = Toplevel(Main_Window)
    Window_Frecuences_Table.geometry("1400x800+60+55") # 1240
    Window_Frecuences_Table.title("Tabla de frecuencias")
    Window_Frecuences_Table.config(bg="#6C6E72")
    Icon = PhotoImage(file="Images/icon.png")
    Window_Frecuences_Table.iconphoto(False , Icon)

    Data_From_Widget_Entry = StringVar(Window_Frecuences_Table) # Estos datos se introducen como texto en el campo de texto de la ventana
    Data_From_Widget_Entry.set("")
    Precision = IntVar(Window_Frecuences_Table)
    Columns_Name = []
    Imported_Data_From_Multiple_Columns = {}
    Imported_Data_From_Single_Column = {}
    Graphs = {}

    Title = Label(Window_Frecuences_Table , text="Calculo de Tablas de Frecuencia" , font=("Times New Roman" , 22), foreground="#ffffff", justify=CENTER , bg="#9DAEC6" , highlightthickness=1 ,highlightbackground="#ffffff")
    Title.place(x=9 , y=10 , width=1380)

    Section_Input = Label(Window_Frecuences_Table ,height=30, bg="#FEE1AB" , highlightthickness=2 , highlightbackground="#000000")
    Section_Input.place(x=29 , y=65 , width=1340)


    Text_Input_Data = Label(Window_Frecuences_Table , text="Ingrese los valores:", font=("Times New Roman" , 13) , bg="#FEE1AB")
    Text_Input_Data.place(x=40 , y=90)
    Input_Data = Entry(Window_Frecuences_Table , textvariable=Data_From_Widget_Entry , border=1 , cursor="xterm" , width=125 , font=("Courier New" , 13) , bg="#ffffff" , relief="sunken")
    Input_Data.place(x=180 , y=90 , width=1179)
    Input_Data.focus()

    Btn_Import_Data_From_File = Button(Window_Frecuences_Table , text="Importar Datos" , font=("Times New Roman" , 13) , width=16 , bg="#EBF3F7" , command= lambda: W_Import_Excel.Create_Window_Import_Excel(Window_Frecuences_Table , Data_From_Widget_Entry , Input_Data , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns))
    Btn_Import_Data_From_File.place(x=70 , y=130)

    Btn_Generate_Table = Button(Window_Frecuences_Table , text="Calcular Tabla" , font=("Times New Roman" , 13) , width=22 , bg="#F4B0C0" , command= lambda: Interact_Btn_Generate_Table(Precision , Data_From_Widget_Entry , Imported_Data_From_Single_Column , Imported_Data_From_Multiple_Columns , Columns_Name , Column_Selection)) # Si no colocas lambda: o colocas parentesis a la funcion, esta se ejecuta cuando el boton se crea, y puede generar problemas
    Btn_Generate_Table.place(x=1120 , y=130)

    Text_Input_Precision_Results = Label(Window_Frecuences_Table , text="Precision:" , font=("Times New Roman" , 13) , bg="#FEE1AB")
    Text_Input_Precision_Results.place(x=960 , y=135)
    Input_Precision_Results = Spinbox(Window_Frecuences_Table , width=3 , textvariable=Precision , from_=3 , to=10 , increment=1 , font=("Courier New" , 13) , bg="#ffffff" , state="readonly" , command= lambda: Interact_Precision())
    Input_Precision_Results.place(x=1050 , y=135)

    Text_Column_Selection = Label(Window_Frecuences_Table , text="Seleccione el nombre de la columna: " , font=("Times New Roman", 13) , bg="#FEE1AB")
    Column_Selection = ttk.Combobox(Window_Frecuences_Table , font=("Courier New" , 13) , values=Columns_Name , state="readonly" , width=40)
    Column_Selection.bind('<<ComboboxSelected>>', Display_Results_By_Column_Name)

    Btn_Generate_Excel = Button(Window_Frecuences_Table , text="Exportar tabla a Excel" , font=("Times New Roman" , 13) , bg="#EBF3F7" , command= lambda: Generate_Window_Export_Excel(Window_Frecuences_Table , Global_Results_From_Single_Column , Global_Results_From_Multiple_Columns , Global_Type_Of_Variable_Single_Column , Global_Type_Of_Variable_Multiple_Column))
    Btn_Generate_Excel.place(x=960 , y=210)
    Btn_Generate_Excel.config(state="disabled")

    Btn_Show_Graph = Button(Window_Frecuences_Table , text="Mostrar grafico" , font=("Times New Roman" , 13) , bg="#EBF3F7" , command= lambda: W_Show_Graph.Create_Window_Show_Graph(Window_Frecuences_Table , Global_Results_From_Single_Column , Global_Results_From_Multiple_Columns , Precision.get() , Graphs))
    Btn_Show_Graph.place(x=1211 , y=210)
    Btn_Show_Graph.config(state="disabled")

    Section_Frecuences_Table = Label(Window_Frecuences_Table , height=32 , bg="#CBEFE3" , highlightthickness=2 , highlightbackground="#000000")
    Section_Frecuences_Table.place(x=29 , y=255 , width=1340)

    Btn_Back = Button(Window_Frecuences_Table , text="Volver", font=("Times New Roman" , 12) , command=Back_to_main_window , width=134 , bg="#F4B0C0")
    Btn_Back.place(x=10 , y=760 , width=1380)

    Window_Frecuences_Table.protocol("WM_DELETE_WINDOW" , Back_to_main_window)
    Window_Frecuences_Table.resizable(False,False)
    Window_Frecuences_Table.mainloop()