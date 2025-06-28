import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Tools import Check_Threads_Alive
from Exceptions.Exception_Warning import Raise_Warning
from Views.Window_Progress_Bar import W_Progress_Bar

from tkinter import *
from tkinter import messagebox
import pandas as pd # type: ignore
import re
import threading

import time

def index_to_string(i):
    Letter = ''
    Temp = i
    while Temp >= 0:
        Letter = chr(Temp % 26 + 65) + Letter
        Temp = Temp // 26 - 1
    return Letter

def string_to_index(s):
    result = 0
    for char in s:
        result = result * 26 + (ord(char.upper()) - 65 + 1)
    return result - 1

def Display_Messagebox_For_Error_In_Thread(Info_About_Error):
    match(Info_About_Error[0]):
        case "RuntimeError":
            messagebox.showerror("Error" , Info_About_Error[1])
        case "Raise_Warning":
            messagebox.showwarning("Advertencia" , Info_About_Error[1])
        case "Exception":
            messagebox.showerror("Error" , Info_About_Error[1])

class Validator:
    def Validate_Format_For_Each_Range_Cells(self , One_Range_Cells):
        One_Range_Cells = One_Range_Cells.upper()
        One_Range_Cells = re.match(r"([A-Z]{1,3})(\d+):([A-Z]{1,3})(\d+)" , One_Range_Cells.strip())
        if(not One_Range_Cells):
            raise Raise_Warning("El rango de celdas ingresado es incorrecto.")
        return One_Range_Cells.groups()

    def Validate_Order_For_Each_Range_Cells(self , Start_Row , End_Row , Start_Column , End_Column):
        if(Start_Column == End_Column and Start_Row == End_Row):
            raise Raise_Warning("No se puede seleccionar una sola celda.")
        elif(Start_Row > End_Row):
            Start_Row , End_Row = End_Row , Start_Row
        elif(Start_Column > End_Column):
            Start_Column , End_Column = End_Column , Start_Column
        return Start_Row , End_Row , Start_Column , End_Column
    
    def Validate_Order_For_All_Range_Cells(self , Ranges_Of_Cells):
        Dict_Range_Cells = {}
        Order_For_Range_Cells = []
        for range_cells in Ranges_Of_Cells:
            if(range_cells[0].isdigit()):
                raise Raise_Warning("El rango de celdas ingresado es incorrecto.")
            
            Dict_Range_Cells[f"{string_to_index(range_cells[0])}"] = range_cells
            Order_For_Range_Cells.append(string_to_index(range_cells[0]))
        
        Order_For_Range_Cells.sort()
        return [Dict_Range_Cells[f"{idx}"] for idx in Order_For_Range_Cells]

    def Validate_For_Avoid_Repeated_Range_Cells(self , Ranges_Of_Cells):
        for range_cell in Ranges_Of_Cells:
            if(Ranges_Of_Cells.count(range_cell) > 1):
                raise Raise_Warning("No se puede importar el mismo rango de celdas dos veces.")

    def Validate_Row_Limit_Excel(self , Input_Start_Row , Input_End_Row , Limit_Excel_End_Rows):
        if(Input_Start_Row > Limit_Excel_End_Rows or Input_End_Row > Limit_Excel_End_Rows):
            raise Raise_Warning("Se intento acceder a una fila no valida, fuera de alcance o sin nungun dato. Intente nuevamente.")
        
    def Validate_Column_Limit_Excel(self , Input_Start_Column , Input_End_Column , Limit_Excel_End_Columns):
        Input_Start_Column = string_to_index(Input_Start_Column)
        Input_End_Column = string_to_index(Input_End_Column)
        
        if(Input_Start_Column > Limit_Excel_End_Columns or Input_End_Column > Limit_Excel_End_Columns):
            raise Raise_Warning("Se intento acceder a una columna no valida, fuera de alcance o sin nungun dato. Intente nuevamente.")
        
    def Validate_Data_Imported_Is_Null(self , Imported_Data , Validate_All_Imported_Data = True):
        if(Validate_All_Imported_Data):
            if(Imported_Data.isnull().all().all()):
                raise Raise_Warning("Los datos seleccionados están vacíos o contienen solo valores nulos.")
            if(Imported_Data.isnull().any().any()):
                raise Raise_Warning("Los datos seleccionados contienen algun valor nulo. Por favor, revise si los datos tienen un formato adecuado.")
        else:
            if(Imported_Data.isnull().all()):
                raise Raise_Warning("Los datos seleccionados están vacíos o contienen solo valores nulos.")
            if(Imported_Data.isnull().any()):
                raise Raise_Warning("Los datos seleccionados contienen algun valor nulo. Por favor, revise si los datos tienen un formato adecuado.")


class Loader_Of_Data:
    def __init__(self):
        self.Table_Preview_Data = None

        self.Entry_Widget_For_W_Table_Frecuency = None
        self.Value_For_Entry_Widget_W_Table_Frecuency = None

        self.Entry_Widgets_For_Venn_Diagram = None
        self.Values_For_Entry_Widgets_Venn_Diagram = None

        self.Imported_Data_From_Excel_For_Calcs = {}
        self.Import_Multiple_Columns = False
        self.Imported_Data = None
        self.Imported_Column_Names = None
        self.Start_Row = None
        self.End_Row = None

    def Insert_Imported_Data_To_Preview(self):
        self.Table_Preview_Data.treeview.delete(*self.Table_Preview_Data.treeview.get_children())

        self.Imported_Data = self.Imported_Data.dropna(axis=1, how='all')
        self.Table_Preview_Data.treeview["columns"] = []
        self.Table_Preview_Data.treeview["columns"] = ["fila"] + self.Imported_Data.columns.tolist()

        self.Table_Preview_Data.treeview.heading("fila" , text="N° fila")
        self.Table_Preview_Data.treeview.column("fila" , anchor="center" , width=120 , stretch=False)
        for col in self.Imported_Data.columns:
            self.Table_Preview_Data.treeview.heading(col , text=col)
            self.Table_Preview_Data.treeview.column(col , anchor="center" , width=120 , stretch=False)

        Dot_Text = tuple(["......."] for _ in range(0 , len(self.Table_Preview_Data.treeview["columns"])))
        N_Imported_Columns = self.Imported_Data.count().tolist()
        Total_Row_Text = tuple(["Datos Importados:"] + N_Imported_Columns)

        # Insertar los datos fila por fila
        if(self.End_Row - self.Start_Row + 1 >= 100):
            for (index, row) in (self.Imported_Data.head(20).iterrows()):
                    values = tuple([index + 2] + row.tolist())
                    self.Table_Preview_Data.treeview.insert("" , "end" , values=values)
            for i in range(0 , 3):
                self.Table_Preview_Data.treeview.insert("" , "end" , values=Dot_Text)
            for (index, row) in (self.Imported_Data.tail(10).iterrows()):
                    values = tuple([index + 2] + row.tolist())
                    self.Table_Preview_Data.treeview.insert("" , "end" , values=values)
            self.Table_Preview_Data.treeview.insert("" , "end" , values=Total_Row_Text)
        else:
            for (index, row) in (self.Imported_Data.iterrows()):
                    values = tuple([index + 1] + row.tolist())
                    self.Table_Preview_Data.treeview.insert("" , "end" , values=values)
            self.Table_Preview_Data.treeview.insert("" , "end" , values=Total_Row_Text)

        messagebox.showinfo("Success" , "Datos procesados con exito.\nYa puede salir de la ventana de importacion.")

    def Load_For_Module_Table_Of_Frecuency(self):
        self.Table_Preview_Data.clear_table()

        if(self.Value_For_Entry_Widget_W_Table_Frecuency.get()):
            self.Value_For_Entry_Widget_W_Table_Frecuency.set("")
        if(self.Imported_Data_From_Excel_For_Calcs):
            self.Imported_Data_From_Excel_For_Calcs.clear()

        match(self.Import_Multiple_Columns):
            case True:
                text = "columnas importadas: "

                for column in self.Imported_Column_Names:
                    self.Imported_Data_From_Excel_For_Calcs[column] = [value for value in self.Imported_Data[column].dropna()]
                    text = text + column + "  "

                self.Entry_Widget_For_W_Table_Frecuency.config(state="disabled")
                self.Value_For_Entry_Widget_W_Table_Frecuency.set(text)

                self.Insert_Imported_Data_To_Preview()

            case False:
                self.Imported_Data_From_Excel_For_Calcs[f"{self.Imported_Column_Names}"] = [value[0] for value in self.Imported_Data.values]

                self.Entry_Widget_For_W_Table_Frecuency.config(state="disabled")
                self.Value_For_Entry_Widget_W_Table_Frecuency.set(f"Columna Importada: {self.Imported_Column_Names}")

                self.Insert_Imported_Data_To_Preview()

    def Load_For_Module_Venn_Diagram(self):
        self.Table_Preview_Data.clear_table()

        for data_widget in self.Entry_Widgets_For_Venn_Diagram.values():
            if(data_widget.get()):
                data_widget.set("")

        if(self.Imported_Data_From_Excel_For_Calcs):
            self.Imported_Data_From_Excel_For_Calcs.clear()

        for i , (data_widget , widget) in enumerate(zip(self.Values_For_Entry_Widgets_Venn_Diagram.values() , self.Entry_Widgets_For_Venn_Diagram.values())):
            if(i < len(self.Imported_Column_Names)):
                self.Imported_Data_From_Excel_For_Calcs[self.Imported_Column_Names[i]] = [value for value in self.Imported_Data[self.Imported_Column_Names[i]].dropna()]

                widget.config(state="disabled")
                data_widget.set(f"Columna Importada: {self.Imported_Column_Names[i]}")
            else:
                widget.config(state="disabled")

        self.Insert_Imported_Data_To_Preview(self.Start_Row , self.End_Row)


class Import_Excel_Using_Single_Range_Of_Cells(Validator , Loader_Of_Data):
    def __init__(self , W_Import_Excel , Table_Preview_Data , Range_Cells , Source_Module_Name , Entry_Widget , Value_For_Entry_Widget , Imported_Data_From_Excel):
        """ 
            Esta clase permite importar datos de un Excel externo, siempre y cuando
            el rango de celdas a importar sea de 1.
            Por ejemplo, los siguientes rangos de celdas son validos:
            A1:A1001
            D1:E10000
            Pero estos rangoes serian invalidos:
            A1:A1001;C1:C1001
        """
        Validator.__init__(self)
        Loader_Of_Data.__init__(self)

        self.Str_Range_Of_Cells = Range_Cells
        self.Import_Multiple_Columns = False

        self.Table_Preview_Data = Table_Preview_Data
        self.W_Import_Excel = W_Import_Excel

        self.Source_Module_Name = Source_Module_Name

        if(Source_Module_Name == "Table_Of_Frecuency"):
            self.Entry_Widget_For_W_Table_Frecuency = Entry_Widget
            self.Value_For_Entry_Widget_W_Table_Frecuency = Value_For_Entry_Widget
        elif(Source_Module_Name == "Venn_Diagram"):
            self.Entry_Widgets_For_Venn_Diagram = Entry_Widget
            self.Values_For_Entry_Widgets_Venn_Diagram = Value_For_Entry_Widget

        self.Imported_Data_From_Excel_For_Calcs = Imported_Data_From_Excel

        self.Error_In_Thread = False
        self.Info_About_Error = []

    def Process_Input_Data(self):
        """  
            Permite Validar y Procesar los rangos de celdas ingresados.
        """

        self.Start_Column , self.Start_Row , self.End_Column , self.End_Row = Validator.Validate_Format_For_Each_Range_Cells(self , self.Str_Range_Of_Cells)

        self.Start_Row , self.End_Row = int(self.Start_Row) , int(self.End_Row)

        self.Start_Row , self.End_Row , self.Start_Column , self.End_Column = Validator.Validate_Order_For_Each_Range_Cells(self, self.Start_Row , self.End_Row , self.Start_Column , self.End_Column)

        if(self.End_Column != self.Start_Column):
            self.Import_Multiple_Columns = True

    def Start_Thread_For_Import_Of_Data(self , Function_Close_Thread = None):
        try:
            Class_Progress_Bar = W_Progress_Bar(self.W_Import_Excel)
            Class_Progress_Bar.Start_Progress_Bar()

            Thread_List = []

            Thread = threading.Thread(target= lambda: self.Extract_Data_From_Excel_Dataframe(self.Table_Preview_Data.Excel_Dataframe , self.Table_Preview_Data.Total_Rows_In_Excel , self.Table_Preview_Data.Total_Columns_In_Excel))
            Thread_List.append(Thread)
            Thread.start()

            self.W_Import_Excel.after(500 , Check_Threads_Alive , Thread_List , self.W_Import_Excel , Class_Progress_Bar , Function_Close_Thread)

        except Raise_Warning as e:
            self.W_Import_Excel.after(0 , messagebox.showwarning("Advertencia" , f"{e}"))
            self.Error_In_Thread = True
            return
        except Exception as e:
            self.W_Import_Excel.after(0 , messagebox.showerror("Error" , f"{e}"))
            self.Error_In_Thread = True
            return

    def Function_Close_Thread(self):
        if(self.Error_In_Thread):
            self.Error_In_Thread = False
            Display_Messagebox_For_Error_In_Thread(self.Info_About_Error)
            return
        
        match(self.Source_Module_Name):
            case "Table_Of_Frecuency":
                self.Load_For_Module_Table_Of_Frecuency()
            case "Venn_Diagram":
                if(len(self.Imported_Column_Names) < 2):
                    raise Raise_Warning("No se puede importar menos de 2 columnas.")
                
                self.Load_For_Module_Venn_Diagram()

    def Extract_Data_From_Excel_Dataframe(self , Loaded_Excel_Dataframe , Total_Rows_In_Excel , Total_Columns_In_Excel):
        try:
            Validator.Validate_Row_Limit_Excel(self, self.Start_Row , self.End_Row , Total_Rows_In_Excel)
            Validator.Validate_Column_Limit_Excel(self , self.Start_Column , self.End_Column , Total_Columns_In_Excel)

            if(self.Start_Column != self.End_Column):
                Idx_Columns = [idx for idx in range(string_to_index(self.Start_Column) , string_to_index(self.End_Column) + 1)]
                self.Imported_Column_Names = [col_name for i , col_name in enumerate(Loaded_Excel_Dataframe.columns) if i in Idx_Columns]
                if("" in self.Imported_Column_Names):
                    raise Raise_Warning("Se intento importar datos sin un encabezado adecuado. Por favor, coloque un nombre adecuado a los datos y coloquelos en la primera fila.")

            else:
                Idx_Columns = [string_to_index(self.Start_Column)]
                self.Imported_Column_Names = Loaded_Excel_Dataframe.columns[string_to_index(self.Start_Column)]
                if(self.Imported_Column_Names == ""):
                    raise Raise_Warning("Se intento importar datos sin un encabezado adecuado. Por favor, coloque un nombre adecuado a los datos y coloquelos en la primera fila.")

            if(self.Start_Row == 1):
                self.Imported_Data = Loaded_Excel_Dataframe.iloc[self.Start_Row-1:self.End_Row-1 , Idx_Columns]
            else:
                self.Imported_Data = Loaded_Excel_Dataframe.iloc[self.Start_Row-2:self.End_Row-1 , Idx_Columns]

            self.Imported_Data = self.Imported_Data.dropna()

            Validator.Validate_Data_Imported_Is_Null(self , self.Imported_Data)
        except RuntimeError:
            self.Error_In_Thread = True
            self.Info_About_Error = ["RuntimeError" , "Error al procesar en hilos\nError en tiempo de ejecucion.\nSi ocurre demasiadas veces reportelo."]
            return
        except Raise_Warning as e:
            self.Error_In_Thread = True
            self.Info_About_Error = ["Raise_Warning" , e]
            return
        except Exception as e:
            self.Error_In_Thread = True
            self.Info_About_Error = ["Exception" , e]
            return

class Import_Excel_Using_Multiple_Range_Of_Cells(Validator , Loader_Of_Data):
    def __init__(self , W_Import_Excel , Table_Preview_Data , Range_Cells , Source_Module_Name , Entry_Widget , Value_For_Entry_Widget , Imported_Data_From_Excel):
        Validator.__init__(self)
        Loader_Of_Data.__init__(self)

        self.Str_Range_Of_Cells = Range_Cells

        self.Error_In_Thread = False
        self.Info_About_Error = []

        self.Collection_Of_Cells = {
            "Columns" : [],
            "Rows" : [],
        }

        self.Import_Multiple_Columns = True

        self.W_Import_Excel = W_Import_Excel
        self.Table_Preview_Data = Table_Preview_Data
        
        self.Source_Module_Name = Source_Module_Name

        if(Source_Module_Name == "Table_Of_Frecuency"):
            self.Entry_Widget_For_W_Table_Frecuency = Entry_Widget
            self.Value_For_Entry_Widget_W_Table_Frecuency = Value_For_Entry_Widget
        elif(Source_Module_Name == "Venn_Diagram"):
            self.Entry_Widgets_For_Venn_Diagram = Entry_Widget
            self.Values_For_Entry_Widgets_Venn_Diagram = Value_For_Entry_Widget

        self.Imported_Data_From_Excel_For_Calcs = Imported_Data_From_Excel

    def Process_Input_Data(self):
        Fixed_Ranges_Of_Cells = []

        Ranges_Of_Cells = self.Str_Range_Of_Cells.split(";")
        Ranges_Of_Cells = Validator.Validate_Order_For_All_Range_Cells(self, Ranges_Of_Cells)
        for ran in Ranges_Of_Cells:
            self.Start_Column , self.Start_Row , self.End_Column , self.End_Row = Validator.Validate_Format_For_Each_Range_Cells(self , ran)
            self.Start_Row , self.End_Row = int(self.Start_Row) , int(self.End_Row)

            self.Start_Row , self.End_Row , self.Start_Column , self.End_Column = Validator.Validate_Order_For_Each_Range_Cells(self , self.Start_Row , self.End_Row , self.Start_Column , self.End_Column)

            Fixed_Ranges_Of_Cells.append(f"{self.Start_Column}{self.Start_Row}:{self.End_Column}{self.End_Row}")
            self.Collection_Of_Cells["Columns"].append([self.Start_Column , self.End_Column])
            self.Collection_Of_Cells["Rows"].append([self.Start_Row , self.End_Row])
        Validator.Validate_For_Avoid_Repeated_Range_Cells(self , Fixed_Ranges_Of_Cells)
        
    def Start_Thread_For_Import_Of_Data(self , Function_Close_Thread = None):
        try:
            Class_Progress_Bar = W_Progress_Bar(self.W_Import_Excel)
            Class_Progress_Bar.Start_Progress_Bar()
            
            Thread_List = []

            Thread = threading.Thread(target= lambda: self.Extract_Data_From_Excel_Dataframe(self.Table_Preview_Data.Excel_Dataframe , self.Table_Preview_Data.Total_Rows_In_Excel , self.Table_Preview_Data.Total_Columns_In_Excel))
            Thread_List.append(Thread)
            Thread.start()

            self.W_Import_Excel.after(500 , Check_Threads_Alive , Thread_List , self.W_Import_Excel , Class_Progress_Bar , Function_Close_Thread)

        except Raise_Warning as e:
            self.W_Import_Excel.after(0 , messagebox.showwarning("Advertencia" , f"{e}"))
            self.Error_In_Thread = True
            return
        except Exception as e:
            self.W_Import_Excel.after(0 , messagebox.showerror("Error" , f"{e}"))
            self.Error_In_Thread = True
            return

    def Function_Close_Thread(self):
        if(self.Error_In_Thread):
            self.Error_In_Thread = False
            Display_Messagebox_For_Error_In_Thread(self.Info_About_Error)
            return
        
        match(self.Source_Module_Name):
            case "Table_Of_Frecuency":
                self.Load_For_Module_Table_Of_Frecuency()
            case "Venn_Diagram":
                if(len(self.Imported_Column_Names) < 2):
                    raise Raise_Warning("No se puede importar menos de 2 columnas.")
                elif(len(self.Imported_Column_Names) > 6):
                    raise Raise_Warning("No se puede importar mas de 6 columnas.")
                
                self.Load_For_Module_Venn_Diagram()

    def Extract_Data_From_Excel_Dataframe(self , Excel_Dataframe , Total_Rows_In_Excel , Total_Columns_In_Excel):
        try:
            Arr_Columns = []
            Arr_Rows = []
            for row in self.Collection_Of_Cells["Rows"]:
                Validator.Validate_Row_Limit_Excel(self , row[0] , row[1] , Total_Rows_In_Excel)
                Arr_Rows.append(row[0])
                Arr_Rows.append(row[1])
            
            for col in self.Collection_Of_Cells["Columns"]:
                Validator.Validate_Column_Limit_Excel(self , col[0] , col[1] , Total_Columns_In_Excel)
                Arr_Columns.append(col[0])
                if(string_to_index(col[1]) - string_to_index(col[0]) > 1):
                    for c in range(string_to_index(col[0]) + 1 , string_to_index(col[1])):
                        Arr_Columns.append(index_to_string(c))
                Arr_Columns.append(col[1])

            Arr_Idx_Columns = [string_to_index(idx) for idx in Arr_Columns]
            Only_Unique_Idx_Columns = list(set(Arr_Idx_Columns))
            Only_Unique_Idx_Columns.sort()

            if(Only_Unique_Idx_Columns == 1):
                raise Raise_Warning("El rango de celdas importado es incorrecto")

            self.Imported_Column_Names = [col for i , col in enumerate(Excel_Dataframe.columns) if i in Only_Unique_Idx_Columns]
            if("" in self.Imported_Column_Names):
                raise Raise_Warning("Se intento importar datos sin un encabezado adecuado. Por favor, coloque un nombre adecuado a los datos y coloquelos en la primera fila.")

            Concat_Columns = []
            try:
                for i in range(0 , len(self.Collection_Of_Cells["Rows"])):
                    """ 
                        ********************************************************************
                        Las condicionales de aqui son importantes para evitar que se
                        importen columnas diferentes a las especificadas, ya que aqui no
                        dependo del valor de indice de de letra de cada columna, debido a
                        que cuando cargo el excel limito solamente a las columnas que me
                        interesa importar y esto genera que cada columna se deba de acceder
                        de manera secuencial
                        Por ejemplo: si ingreso A1:B1001;D1:D1001
                        Solo cargo las columnas A , B y C. 
                        Y para extraer los datos de cada columna debo dirigirme a ellos como
                        0 , 1 y 2 respectivamente.
                        ********************************************************************
                    """
                    if(string_to_index(self.Collection_Of_Cells["Columns"][i][1]) - string_to_index(self.Collection_Of_Cells["Columns"][i][0]) >= 1):
                        col = [n_col for n_col in range(string_to_index(self.Collection_Of_Cells["Columns"][i][0]) , string_to_index(self.Collection_Of_Cells["Columns"][i][1]) + 1)]
                    else:
                        col = string_to_index(self.Collection_Of_Cells["Columns"][i][0])
                    
                    if(self.Collection_Of_Cells["Rows"][i][0] == 1):
                        Adjustment_Value = 1
                    else:
                        Adjustment_Value = 2
                    
                    if(isinstance(col , list)):
                        for c in col:
                            column_i = Excel_Dataframe.iloc[self.Collection_Of_Cells["Rows"][i][0]-Adjustment_Value:self.Collection_Of_Cells["Rows"][i][1]-1 , c]
                            column_i.dropna()
                            Validator.Validate_Data_Imported_Is_Null(self , column_i , False)
                            Concat_Columns.append(column_i)
                    else:
                        column_i = Excel_Dataframe.iloc[self.Collection_Of_Cells["Rows"][i][0]-Adjustment_Value:self.Collection_Of_Cells["Rows"][i][1]-1 , col]
                        column_i.dropna()
                        Validator.Validate_Data_Imported_Is_Null(self , column_i , False)
                        Concat_Columns.append(column_i)
                self.Imported_Data = pd.concat(Concat_Columns , axis=1 , ignore_index=True , join="outer")
                self.Imported_Data.columns = self.Imported_Column_Names
            except Exception as e:
                raise Raise_Warning("Algo salio mal, asegurese de que el rango de celdas ingresado no tenga intersecciones.\nCorrecto: A1:D1001;F1:H1001 \nIncorrecto: A1:D1001;C1:E1001")
            self.Imported_Data.dropna()

            self.Start_Row = min(Arr_Rows)
            self.End_Row = max(Arr_Rows)
        except RuntimeError:
            self.Error_In_Thread = True
            self.Info_About_Error = ["RuntimeError" , "Error al procesar en hilos\nError en tiempo de ejecucion.\nSi ocurre demasiadas veces reportelo."]
            return
        except Raise_Warning as e:
            self.Error_In_Thread = True
            self.Info_About_Error = ["Raise_Warning" , e]
            return
        except Exception as e:
            self.Error_In_Thread = True
            self.Info_About_Error = ["Exception" , e]
            return