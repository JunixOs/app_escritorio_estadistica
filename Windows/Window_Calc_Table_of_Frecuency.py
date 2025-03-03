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

class Process_Column_Of_Data:
    def __init__(self , Root_Window, Table , Data_To_Analized , T_Quartil , T_Decil , T_Percentil):
        self.Root_Window = Root_Window
        self.Results = {}
        self.Type_Of_Variable = None
        self.Table_Frecuences = Table # de la clase TreeviewFrame
        self.Table_Quartil = T_Quartil
        self.Table_Decil = T_Decil
        self.Table_Percentil = T_Percentil
        self.Labels = []
        self.Data_To_Analized = Data_To_Analized
        self.Precision = 3
        self.Amplitude_N_Decimals = None

    def Calc_Results(self , Precision):
        self.Precision = Precision
        if(isinstance(self.Data_To_Analized , dict)):
            Results = Main_Function(self.Data_To_Analized["S_Column"])
        else:
            Results = Main_Function(self.Data_To_Analized)

        if(Results["Frecuences_Cuant_For_Many_Values"] != None):
            self.Type_Of_Variable = "Cuantitative_Grouped"
            self.Amplitude_N_Decimals = Results["Variables_Cuant_For_Many_Values"]["C_Decimals_Number"]
        elif(Results["Frecuences_Cuant_Normal_Extended"] != None):
            self.Type_Of_Variable = "Cuantitative_Not_Grouped"
        elif(Results["Frecuences_Cuali_Normal_Extended"] != None):
            self.Type_Of_Variable = "Cualitative"
            self.Table_For_Quartiles = None
            self.Table_For_Deciles = None
            self.Table_For_Percentiles = None

        Without_None = {}
        for key,value in Results.items():
            if(value != None):
                Without_None[key] = value

        self.Results = Without_None

    def Table_For_Cuant_Grouped_Data(self):
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
    
    def Put_Data_On_Table_For_Cuant_Grouped_Data(self):
        if(self.Amplitude_N_Decimals == None):
            raise Exception("Hubo un error al calcular la tabla de frecuencias.")

        Variables = self.Results["Variables_Cuant_For_Many_Values"]
        Frecuences = self.Results["Frecuences_Cuant_For_Many_Values"]

        if(not self.Table_Frecuences.Has_Rows()):
            self.Table_Frecuences.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            for a in range(0 , Variables["m"]):
                self.Table_Frecuences.treeview.insert(
                    "", END , values=(
                        a+1, 
                        f"{Frecuences['Intervals'][a][0]:.{self.Amplitude_N_Decimals}f}", 
                        f"{Frecuences['Intervals'][a][1]:.{self.Amplitude_N_Decimals}f}", 
                        f"{Frecuences['Groups'][a]:.{self.Amplitude_N_Decimals}f}", 
                        f"{Frecuences['xi'][a]:.{self.Precision}f}",
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        f"{Frecuences['hi'][a]:.{self.Precision}f}",
                        f"{Frecuences['Hi'][a]:.{self.Precision}f}",
                        f"{Frecuences['hi_percent'][a]:.{self.Precision}f}%",
                        f"{Frecuences['Hi_percent'][a]:.{self.Precision}f}%",)
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

    def Table_For_Cuant_Not_Grouped_Data(self):
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
        
    def Put_Data_On_Table_For_Cuant_Not_Grouped_Data(self):
        Variables = self.Results["Variables_Cuant_Normal_Extended"]
        Frecuences = self.Results["Frecuences_Cuant_Normal_Extended"]
        if(not self.Table_Frecuences.Has_Rows()):
            self.Table_Frecuences.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            for a in range(0 , Variables["Number_Statistic_Variables"]):
                self.Table_Frecuences.treeview.insert(
                    "", END , values=(
                        Frecuences["xi"][a],
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        f"{Frecuences['hi'][a]:.{self.Precision}f}",
                        f"{Frecuences['Hi'][a]:.{self.Precision}f}",
                        f"{Frecuences['hi_percent'][a]:.{self.Precision}f}%",
                        f"{Frecuences['Hi_percent'][a]:.{self.Precision}f}%",) , tags=("font_arial_10",))
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

    def Table_For_Cualitative_Data(self):
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

    def Put_Data_On_Table_For_Cualitative_Data(self):
        Variables = self.Results["Variables_Cuali_Normal_Extended"]
        Frecuences = self.Results["Frecuences_Cuali_Normal_Extended"]
        if(not self.Table_Frecuences.Has_Rows()):
            self.Table_Frecuences.treeview.tag_configure("font_arial_10", font=("Arial", 10))
            for a in range(0 , Variables["N_Character_Modalities"]):
                self.Table_Frecuences.treeview.insert(
                    "", END , values=(
                        Frecuences["ai"][a],
                        Frecuences["fi"][a],
                        Frecuences["Fi"][a],
                        f"{Frecuences['hi'][a]:.{self.Precision}f}",
                        f"{Frecuences['Hi'][a]:.{self.Precision}f}",
                        f"{Frecuences['hi_percent'][a]:.{self.Precision}f}%",
                        f"{Frecuences['Hi_percent'][a]:.{self.Precision}f}%",) , tags=("font_arial_10",))
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

    def Create_Tables_For_Frecuences(self):
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

    def Put_Data_On_Frecuences_Tables(self):
        if(self.Table_Frecuences.Has_Rows()):
            self.Table_Frecuences.clear_table()

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

    def Display_Table_Frecuences(self):
        self.Table_Frecuences.Display()
    def Hidden_Table_Frecuences(self):
        self.Table_Frecuences.Hidden()

    def Destroy_Labels(self):
        if(len(self.Labels) != 0):
            for a in range(0 , len(self.Labels)):
                self.Labels[a].destroy()
            self.Labels = []
    
    def Label_SM_For_Grouped_Data(self , S_Measures):
        self.Destroy_Labels()

        b=0
        for key,value in S_Measures.items():
            if(b < 3):
                lab = Label(self.Root_Window , text=f"{key}\n{value:.{self.Precision}f}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
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
                    lab = Label(self.Root_Window , text=f"{key}\n{String}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)

                else:
                    lab = Label(self.Root_Window , text=f"{key}\nMo: {value[0]:.{self.Precision}f}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)

            elif(b < 6):
                lab = Label(self.Root_Window , text=f"{key}\n{value:.{self.Precision}f}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
            else:
                lab = Label(self.Root_Window , text=f"{key}\n{value:.{self.Precision}f}" , font=("Times New Roman" , 12) , bg="#CBEFE3" , justify=CENTER , width=20)
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
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            for lab in self.Labels:
                lab.place_forget()
            
    def Destroy_Tables_Of_Frecuences(self):
        self.Table_Frecuences.destroy()

    def Table_For_Quartiles(self):
        self.Table_Quartil.treeview.config(columns=("1") , show="headings")
        self.Table_Quartil.treeview.heading("1" , text="Cuartiles (Q_k)")

        self.Table_Quartil.treeview.config(height=6)

        for a in range(1 , 2):
            self.Table_Quartil.treeview.column(f"{a}" , anchor="center" , width=140)

    def Put_Data_On_Table_For_Quartiles(self , Quantiles):
        if(not self.Table_Quartil.Has_Rows()):
            self.Table_Quartil.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            if(not Quantiles["Cuartil"]):
                self.Table_Quartil.treeview.insert(
                    "", END , values=(
                        "Sin resultados",
                    ))
            else:
                for a in range(0 , 3):
                    self.Table_Quartil.treeview.insert(
                        "", END , values=(
                            f"Q_{a+1} = {Quantiles['Cuartil'][a]:.{self.Precision}f}",
                        ))

            for col in self.Table_Quartil.treeview["columns"]:
                self.Table_Quartil.treeview.column(col, anchor="center")

    def Table_For_Deciles(self):
        self.Table_Decil.treeview.config(columns=("1") , show="headings")
        self.Table_Decil.treeview.heading("1" , text="Deciles (D_k)")

        self.Table_Decil.treeview.config(height=6)

        for a in range(1 , 2):
            self.Table_Decil.treeview.column(f"{a}" , anchor="center" , width=140)
    
    def Put_Data_On_Table_For_Deciles(self , Quantiles):
        if(not self.Table_Decil.Has_Rows()):
            self.Table_Decil.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            if(not Quantiles["Decil"]):
                self.Table_Decil.treeview.insert(
                    "", END , values=(
                        "Sin resultados",
                    ))
            else:
                for a in range(0 , 9):
                    self.Table_Decil.treeview.insert(
                        "", END , values=(
                            f"D_{a+1} = {Quantiles['Decil'][a]:.{self.Precision}f}",
                        ))

            for col in self.Table_Decil.treeview["columns"]:
                self.Table_Decil.treeview.column(col, anchor="center")

    def Table_For_Percentiles(self):
        self.Table_Percentil.treeview.config(columns=("1") , show="headings")
        self.Table_Percentil.treeview.heading("1" , text="Percentiles (P_k)")

        self.Table_Percentil.treeview.config(height=6)

        for a in range(1 , 2):
            self.Table_Percentil.treeview.column(f"{a}" , anchor="center" , width=140)

    def Put_Data_On_Table_For_Percentiles(self , Quantiles):
        if(not self.Table_Percentil.Has_Rows()):
            self.Table_Percentil.treeview.tag_configure("font_arial_10", font=("Arial", 10))

            if(not Quantiles["Percentil"]):
                self.Table_Percentil.treeview.insert(
                    "", END , values=(
                        "Sin resultados",
                    ))
            else:
                for a in range(0 , 99):
                    self.Table_Percentil.treeview.insert(
                        "", END , values=(
                            f"P_{a+1} = {Quantiles['Percentil'][a]:.{self.Precision}f}",
                        ))

            for col in self.Table_Percentil.treeview["columns"]:
                self.Table_Percentil.treeview.column(col, anchor="center")

    def Create_Table_For_Quantiles(self):
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            self.Table_For_Quartiles()
            self.Table_For_Deciles()
            self.Table_For_Percentiles()

    def Put_Data_On_Quantiles_Tables(self):
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            if(self.Table_Quartil.Has_Rows() and self.Table_Decil.Has_Rows() and self.Table_Percentil.Has_Rows()):
                self.Table_Quartil.clear_table()
                self.Table_Decil.clear_table()
                self.Table_Percentil.clear_table()
            
            if("Quantiles_For_Grouped_Data" in self.Results):
                Quantiles = self.Results["Quantiles_For_Grouped_Data"]
            elif("Quantiles_For_Not_Grouped_Data" in self.Results):
                Quantiles = self.Results["Quantiles_For_Not_Grouped_Data"]
            self.Put_Data_On_Table_For_Quartiles(Quantiles)
            self.Put_Data_On_Table_For_Deciles(Quantiles)
            self.Put_Data_On_Table_For_Percentiles(Quantiles)

    def Display_Tables_Quartiles(self):
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            self.Table_Quartil.place(x=780 , y=261)
            self.Table_Decil.place(x=980 , y=261)
            self.Table_Percentil.place(x=1180 , y=261)
    def Hidden_Tables_Quartiles(self):
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            self.Table_Quartil.place_forget()
            self.Table_Decil.place_forget()
            self.Table_Percentil.place_forget()

    def Destroy_Tables_Quartiles(self):
        if(self.Type_Of_Variable == "Cuantitative_Grouped" or self.Type_Of_Variable == "Cuantitative_Not_Grouped"):
            self.Table_Quartil.destroy()
            self.Table_Decil.destroy()
            self.Table_Percentil.destroy()

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

    def Display_Results_By_Column_Name(Event):
        Selection = Column_Selection.get()
        for t in Global_Views.values():
            t.Hidden_Labels()
            t.Hidden_Table_Frecuences()
            t.Hidden_Tables_Quartiles()

        Global_Views[f"{Selection}"].Display_Labels()
        Global_Views[f"{Selection}"].Display_Table_Frecuences()
        Global_Views[f"{Selection}"].Display_Tables_Quartiles()
        Precision.set(Global_Views[f"{Selection}"].Precision)

    def Display_Results_For_Single_Column_Data(Precision , Data_From_Widget_Entry , Imported_Data_From_Single_Column):
        global Global_Views
        if(Global_Views == {}):
            Table_For_Data_Column = TreeviewFrame(Window_Frecuences_Table)
            Table_For_Quartile = TreeviewFrame(Window_Frecuences_Table)
            Table_For_Decile = TreeviewFrame(Window_Frecuences_Table)
            Table_For_Percentile = TreeviewFrame(Window_Frecuences_Table)

            if(Imported_Data_From_Single_Column != {}):
                Results_From_Single_Column = {}
                key, value = next(iter(Imported_Data_From_Single_Column.items()))
                Results_Viewer_For_Single_Column_Data = Process_Column_Of_Data(Window_Frecuences_Table , Table_For_Data_Column , value , Table_For_Quartile , Table_For_Decile , Table_For_Percentile) # Para datos importados de Excel
                Results_Viewer_For_Single_Column_Data.Calc_Results(Precision)
                Results_From_Single_Column[f"{key}"] = Results_Viewer_For_Single_Column_Data.Results
            else:
                Results_From_Single_Column = None
                Results_Viewer_For_Single_Column_Data = Process_Column_Of_Data(Window_Frecuences_Table , Table_For_Data_Column , Data_From_Widget_Entry , Table_For_Quartile , Table_For_Decile , Table_For_Percentile) # Para datos ingresados manuamente
                Results_Viewer_For_Single_Column_Data.Calc_Results(Precision)
                Results_From_Single_Column = Results_Viewer_For_Single_Column_Data.Results

            Results_Viewer_For_Single_Column_Data.Create_Tables_For_Frecuences()
            Results_Viewer_For_Single_Column_Data.Create_Table_For_Quantiles()
            Results_Viewer_For_Single_Column_Data.Create_Labels_Summary_Measures()

            Results_Viewer_For_Single_Column_Data.Put_Data_On_Frecuences_Tables()
            Results_Viewer_For_Single_Column_Data.Put_Data_On_Quantiles_Tables()

            Results_Viewer_For_Single_Column_Data.Display_Labels()
            Results_Viewer_For_Single_Column_Data.Display_Table_Frecuences()
            Results_Viewer_For_Single_Column_Data.Display_Tables_Quartiles()

            Global_Views["S_Column"] = Results_Viewer_For_Single_Column_Data
            
            return Results_From_Single_Column , Global_Views["S_Column"].Type_Of_Variable
        else:
            Global_Views["S_Column"].Precision = Precision
            Global_Views["S_Column"].Create_Labels_Summary_Measures()
            Global_Views["S_Column"].Put_Data_On_Frecuences_Tables()
            Global_Views["S_Column"].Put_Data_On_Quantiles_Tables()

            Global_Views["S_Column"].Display_Labels()

    def Display_Results_For_Multiple_Column_Data(Precision , Imported_Data_From_Multiple_Columns):
        global Global_Views
        Results_From_Multiple_Columns = {}
        Type_Of_Variable_For_Multiple_Columns = {}
        if(Global_Views == {}):
            for key,values in Imported_Data_From_Multiple_Columns.items():
                Results_Viewer_For_Multiple_Columns_Data = None
                Table_Frecuences = None
                Table_For_Quartile = None
                Table_For_Decile = None
                Table_For_Percentile = None

                Table_For_Quartile = TreeviewFrame(Window_Frecuences_Table)
                Table_For_Decile = TreeviewFrame(Window_Frecuences_Table)
                Table_For_Percentile = TreeviewFrame(Window_Frecuences_Table)
                
                Table_Frecuences = TreeviewFrame(Window_Frecuences_Table)

                Results_Viewer_For_Multiple_Columns_Data = Process_Column_Of_Data(Window_Frecuences_Table , Table_Frecuences , values , Table_For_Quartile , Table_For_Decile , Table_For_Percentile)
                Results_Viewer_For_Multiple_Columns_Data.Calc_Results(Precision)
                Results_Viewer_For_Multiple_Columns_Data.Create_Tables_For_Frecuences()
                Results_Viewer_For_Multiple_Columns_Data.Create_Table_For_Quantiles()
                Results_Viewer_For_Multiple_Columns_Data.Create_Labels_Summary_Measures()

                Results_Viewer_For_Multiple_Columns_Data.Put_Data_On_Quantiles_Tables()
                Results_Viewer_For_Multiple_Columns_Data.Put_Data_On_Frecuences_Tables()

                Global_Views[f"{key}"] = Results_Viewer_For_Multiple_Columns_Data
                Results_From_Multiple_Columns[f"{key}"] = Results_Viewer_For_Multiple_Columns_Data.Results
                Type_Of_Variable_For_Multiple_Columns[f"{key}"] = Results_Viewer_For_Multiple_Columns_Data.Type_Of_Variable
                Columns_Name.append(f"{key}")

            Text_Column_Selection.place(x=40 , y=170)
            Column_Selection.place(x=300 , y=170)
            Column_Selection.set(Columns_Name[0])
            Column_Selection["values"] = Columns_Name

            Display_Results_By_Column_Name(None)

            return Results_From_Multiple_Columns , Type_Of_Variable_For_Multiple_Columns
        else:
            Selection = Column_Selection.get()
            Global_Views[f"{Selection}"].Precision = Precision
            Global_Views[f"{Selection}"].Create_Labels_Summary_Measures()
            Global_Views[f"{Selection}"].Put_Data_On_Frecuences_Tables()
            Global_Views[f"{Selection}"].Put_Data_On_Quantiles_Tables()

            Global_Views[f"{Selection}"].Display_Labels()

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
            t.Destroy_Labels()
            t.Destroy_Tables_Of_Frecuences()
            t.Destroy_Tables_Quartiles()
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
    Input_Precision_Results = Spinbox(Window_Frecuences_Table , width=2 , textvariable=Precision , from_=3 , to=8 , increment=1 , font=("Courier New" , 13) , bg="#ffffff" , state="readonly" , command= lambda: Interact_Precision())
    Input_Precision_Results.place(x=1050 , y=135)

    Text_Column_Selection = Label(Window_Frecuences_Table , text="Seleccione el nombre de la columna: " , font=("Times New Roman", 13) , bg="#FEE1AB")
    Column_Selection = ttk.Combobox(Window_Frecuences_Table , font=("Courier New" , 13) , values=Columns_Name , state="readonly" , width=40)
    Column_Selection.bind('<<ComboboxSelected>>', Display_Results_By_Column_Name)

    Btn_Generate_Excel = Button(Window_Frecuences_Table , text="Exportar tabla a Excel" , font=("Times New Roman" , 13) , bg="#EBF3F7" , command= lambda: Generate_Window_Export_Excel(Window_Frecuences_Table , Global_Results_From_Single_Column , Global_Results_From_Multiple_Columns , Global_Type_Of_Variable_Single_Column , Global_Type_Of_Variable_Multiple_Column))
    Btn_Generate_Excel.place(x=960 , y=210)
    Btn_Generate_Excel.config(state="disabled")

    Btn_Show_Graph = Button(Window_Frecuences_Table , text="Mostrar grafico" , font=("Times New Roman" , 13) , bg="#EBF3F7" , command= lambda: W_Show_Graph.Create_Windows_Show_Graphs(Window_Frecuences_Table , Global_Results_From_Single_Column , Global_Results_From_Multiple_Columns , Precision.get() , Graphs))
    Btn_Show_Graph.place(x=1211 , y=210)
    Btn_Show_Graph.config(state="disabled")

    Section_Frecuences_Table = Label(Window_Frecuences_Table , height=32 , bg="#CBEFE3" , highlightthickness=2 , highlightbackground="#000000")
    Section_Frecuences_Table.place(x=29 , y=255 , width=1340)

    Btn_Back = Button(Window_Frecuences_Table , text="Volver", font=("Times New Roman" , 12) , command=Back_to_main_window , width=134 , bg="#F4B0C0")
    Btn_Back.place(x=10 , y=760 , width=1380)

    Window_Frecuences_Table.protocol("WM_DELETE_WINDOW" , Back_to_main_window)
    Window_Frecuences_Table.resizable(False,False)
    Window_Frecuences_Table.mainloop()