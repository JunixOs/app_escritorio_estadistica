import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Exceptions.Exception_Warning import Raise_Warning
from tkinter import *
from tkinter import messagebox
import pandas as pd # type: ignore
import re

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
        
    def Validate_Path(self, File_Path):
        if(not File_Path):
            raise Raise_Warning("No se ha ingresado la ruta del archivo.")
        if (not os.path.exists(File_Path)):
            raise Exception("El archivo Excel no existe en la ruta especificada.")

    def Validate_Sheets(self, Sheet_Number , File_Path):
        if(isinstance(Sheet_Number , float)):
            raise Raise_Warning("Numero de hoja no valido, solo valores enteros.")
        
        Unloaded_Excel = pd.ExcelFile(f"{File_Path}")
        Sheets = Unloaded_Excel.sheet_names
        if(Sheet_Number > len(Sheets)):
            raise Raise_Warning("No existe el numero de hoja especificado.")
        
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

class Import_Preview:
    def __init__(self , Table_Preview_Data , Imported_Data):
        self.Table_Preview_Data = Table_Preview_Data # Treeview
        self.Imported_Data = Imported_Data

    def Insert_Imported_Data_To_Preview(self , Start_Row , End_Row):
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
        if(End_Row - Start_Row + 1 >= 100):
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

        self.Table_Preview_Data.Progress_Bar.Close_Progress_Bar()

        messagebox.showinfo("Success" , "Datos procesados con exito.\nYa puede salir de la ventana de importacion.")


class Load_Data_In_Preview:
    def Module_Table_Of_Frecuency(self , Table_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Imported_Data_From_Excel_For_Calcs , Import_Multiple_Columns , Imported_Data , Imported_Column_Names , Start_Row , End_Row):
        Table_Preview_Data.clear_table()
        Load_Preview = Import_Preview(Table_Preview_Data , Imported_Data)

        if(Data_From_Entry_Widget.get()):
            Data_From_Entry_Widget.set("")
        if(Imported_Data_From_Excel_For_Calcs):
            Imported_Data_From_Excel_For_Calcs.clear()

        match(Import_Multiple_Columns):
            case True:
                text = "columnas importadas: "

                for column in Imported_Column_Names:
                    Imported_Data_From_Excel_For_Calcs[column] = [value for value in Imported_Data[column].dropna()]
                    text = text + column + "  "

                Widget_Input_Data.config(state="disabled")
                Data_From_Entry_Widget.set(text)

                Load_Preview.Insert_Imported_Data_To_Preview(Start_Row , End_Row)

            case False:
                Imported_Data_From_Excel_For_Calcs[f"{Imported_Column_Names}"] = [value[0] for value in Imported_Data.values]

                Widget_Input_Data.config(state="disabled")
                Data_From_Entry_Widget.set(f"Columna Importada: {Imported_Column_Names}")

                Load_Preview.Insert_Imported_Data_To_Preview(Start_Row , End_Row)

    def Module_Venn_Diagram(self , Table_Preview_Data , Data_From_Entry_Widgets , Widgets_Input_Data , Imported_Data_From_Excel_For_Calcs , Imported_Data , Imported_Column_Names , Start_Row , End_Row):
        Table_Preview_Data.clear_table()
        Load_Preview = Import_Preview(Table_Preview_Data , Imported_Data)

        for data_widget in Data_From_Entry_Widgets.values():
            if(data_widget.get()):
                data_widget.set("")

        if(Imported_Data_From_Excel_For_Calcs):
            Imported_Data_From_Excel_For_Calcs.clear()

        for i , (data_widget , widget) in enumerate(zip(Data_From_Entry_Widgets.values() , Widgets_Input_Data.values())):
            if(i < len(Imported_Column_Names)):
                Imported_Data_From_Excel_For_Calcs[Imported_Column_Names[i]] = [value for value in Imported_Data[Imported_Column_Names[i]].dropna()]

                widget.config(state="disabled")
                data_widget.set(f"Columna Importada: {Imported_Column_Names[i]}")
            else:
                widget.config(state="disabled")

        Load_Preview.Insert_Imported_Data_To_Preview(Start_Row , End_Row)


class Import_Excel_Using_Single_Range_Of_Cells(Validator , Load_Data_In_Preview):
    def __init__(self , File_Path , Sheet_Number , Range_Cells):
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
        Load_Data_In_Preview.__init__(self)

        self.File_Path = File_Path
        self.Sheet_Number = Sheet_Number - 1
        self.Str_Range_Of_Cells = Range_Cells
        self.Import_Multiple_Columns = False

    def Process_Input_Data(self):
        """  
            Permite Validar y Procesar los rangos de celdas ingresados, la ruta del archivo excel ingresado y el numero de hoja
            de este.
        """
        Validator.Validate_Path(self , self.File_Path)
        Validator.Validate_Sheets(self, self.Sheet_Number , self.File_Path)

        self.Start_Column , self.Start_Row , self.End_Column , self.End_Row = Validator.Validate_Format_For_Each_Range_Cells(self , self.Str_Range_Of_Cells)

        self.Start_Row , self.End_Row = int(self.Start_Row) , int(self.End_Row)

        self.Start_Row , self.End_Row , self.Start_Column , self.End_Column = Validator.Validate_Order_For_Each_Range_Cells(self, self.Start_Row , self.End_Row , self.Start_Column , self.End_Column)

        if(self.End_Column != self.Start_Column):
            self.Import_Multiple_Columns = True
    
    def Manage_Import_For_Module_Table_Of_Frecuency(self , Table_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Imported_Data_From_Excel_For_Calcs):
        try:
    
            self.Extract_Data_From_Excel_Dataframe(Table_Preview_Data.Excel_Dataframe , Table_Preview_Data.Total_Rows_In_Excel , Table_Preview_Data.Total_Columns_In_Excel)

            Load_Data_In_Preview.Module_Table_Of_Frecuency(
                self , Table_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Imported_Data_From_Excel_For_Calcs , 
                self.Import_Multiple_Columns , self.Imported_Data , self.Imported_Column_Names , self.Start_Row , self.End_Row)
    
        except Raise_Warning as e:
            Table_Preview_Data.Progress_Bar.Close_Progress_Bar()
            messagebox.showwarning("Advertencia" , f"{e}")
        except Exception as e:
            Table_Preview_Data.Progress_Bar.Close_Progress_Bar()
            messagebox.showerror("Error" , f"{e}")

    def Manage_Import_For_Module_Venn_Diagram(self , Table_Preview_Data , Data_From_Entry_Widgets , Widgets_Input_Data , Imported_Data_From_Excel_For_Calcs):
        try:
            self.Extract_Data_From_Excel_Dataframe(Table_Preview_Data.Excel_Dataframe , Table_Preview_Data.Total_Rows_In_Excel , Table_Preview_Data.Total_Columns_In_Excel)

            if(len(self.Imported_Column_Names) < 2):
                raise Raise_Warning("No se puede importar menos de 2 columnas.")
            
            Load_Data_In_Preview.Module_Venn_Diagram(
                self , Table_Preview_Data , Data_From_Entry_Widgets , Widgets_Input_Data , Imported_Data_From_Excel_For_Calcs , self.Imported_Data , self.Imported_Column_Names , self.Start_Row , self.End_Row
            )

        except Raise_Warning as e:
            Table_Preview_Data.Progress_Bar.Close_Progress_Bar()
            messagebox.showwarning("Advertencia" , f"{e}")
        except Exception as e:
            Table_Preview_Data.Progress_Bar.Close_Progress_Bar()
            messagebox.showerror("Error" , f"{e}")

    def Extract_Data_From_Excel_Dataframe(self , Excel_Dataframe , Total_Rows_In_Excel , Total_Columns_In_Excel):

        Validator.Validate_Row_Limit_Excel(self, self.Start_Row , self.End_Row , Total_Rows_In_Excel)
        Validator.Validate_Column_Limit_Excel(self , self.Start_Column , self.End_Column , Total_Columns_In_Excel)

        if(self.Start_Column != self.End_Column):
            Idx_Columns = [idx for idx in range(string_to_index(self.Start_Column) , string_to_index(self.End_Column) + 1)]
            self.Imported_Column_Names = [col_name for i , col_name in enumerate(Excel_Dataframe.columns) if i in Idx_Columns]
            if("" in self.Imported_Column_Names):
                raise Raise_Warning("Se intento importar datos sin un encabezado adecuado. Por favor, coloque un nombre adecuado a los datos y coloquelos en la primera fila.")

        else:
            Idx_Columns = [string_to_index(self.Start_Column)]
            self.Imported_Column_Names = Excel_Dataframe.columns[string_to_index(self.Start_Column)]
            if(self.Imported_Column_Names == ""):
                raise Raise_Warning("Se intento importar datos sin un encabezado adecuado. Por favor, coloque un nombre adecuado a los datos y coloquelos en la primera fila.")

        if(self.Start_Row == 1):
            self.Imported_Data = Excel_Dataframe.iloc[self.Start_Row-1:self.End_Row-1 , Idx_Columns]
        else:
            self.Imported_Data = Excel_Dataframe.iloc[self.Start_Row-2:self.End_Row-1 , Idx_Columns]

        self.Imported_Data = self.Imported_Data.dropna()

        Validator.Validate_Data_Imported_Is_Null(self , self.Imported_Data)



class Import_Excel_Using_Multiple_Range_Of_Cells(Validator , Load_Data_In_Preview):
    def __init__(self , File_Path , Sheet_Number , Range_Cells):
        Validator.__init__(self)
        Load_Data_In_Preview.__init__(self)

        self.File_Path = File_Path
        self.Sheet_Number = Sheet_Number - 1
        self.Str_Range_Of_Cells = Range_Cells

        self.Collection_Of_Cells = {
            "Columns" : [],
            "Rows" : [],
        }
        self.Imported_Data = None
        self.Import_Mutiple_Columns = True

    def Process_Input_Data(self):
        Fixed_Ranges_Of_Cells = []

        Validator.Validate_Path(self , self.File_Path)
        Validator.Validate_Sheets(self, self.Sheet_Number , self.File_Path)

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
        
    def Manage_Import_For_Module_Table_Of_Frecuency(self , Table_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Imported_Data_From_Excel_For_Calcs):
        try:
            self.Extract_Data_From_Excel_Dataframe(Table_Preview_Data.Excel_Dataframe , Table_Preview_Data.Total_Rows_In_Excel , Table_Preview_Data.Total_Columns_In_Excel)

            Load_Data_In_Preview.Module_Table_Of_Frecuency(
                self , Table_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Imported_Data_From_Excel_For_Calcs , self.Import_Mutiple_Columns ,
                self.Imported_Data , self.Imported_Column_Names , self.Start_Row , self.End_Row
            )

        except Raise_Warning as e:
            Table_Preview_Data.Progress_Bar.Close_Progress_Bar()
            messagebox.showwarning("Advertencia" , f"{e}")
        except Exception as e:
            Table_Preview_Data.Progress_Bar.Close_Progress_Bar()
            messagebox.showerror("Error" , f"{e}")

    def Manage_Import_For_Module_Venn_Diagram(self , Table_Preview_Data , Data_From_Entry_Widgets , Widgets_Input_Data , Imported_Data_From_Excel_For_Calcs):
        try:
            self.Extract_Data_From_Excel_Dataframe(Table_Preview_Data.Excel_Dataframe , Table_Preview_Data.Total_Rows_In_Excel , Table_Preview_Data.Total_Columns_In_Excel)

            if(len(self.Imported_Column_Names) < 2):
                raise Raise_Warning("No se puede importar menos de 2 columnas.")
            elif(len(self.Imported_Column_Names) > 6):
                raise Raise_Warning("No se puede importar mas de 6 columnas.")
            
            Load_Data_In_Preview.Module_Venn_Diagram(
                self , Table_Preview_Data , Data_From_Entry_Widgets , Widgets_Input_Data , Imported_Data_From_Excel_For_Calcs , self.Imported_Data , self.Imported_Column_Names , self.Start_Row , self.End_Row
            )

        except Raise_Warning as e:
            Table_Preview_Data.Progress_Bar.Close_Progress_Bar()
            messagebox.showwarning("Advertencia" , f"{e}")
        except Exception as e:
            Table_Preview_Data.Progress_Bar.Close_Progress_Bar()
            messagebox.showerror("Error" , f"{e}")

    def Extract_Data_From_Excel_Dataframe(self , Excel_Dataframe , Total_Rows_In_Excel , Total_Columns_In_Excel):
        start_time = time.time()

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
        print(self.Imported_Column_Names)
        if("" in self.Imported_Column_Names):
            raise Raise_Warning("Se intento importar datos sin un encabezado adecuado. Por favor, coloque un nombre adecuado a los datos y coloquelos en la primera fila.")

        Concat_Columns = []
        try:
            n = 0
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

        end_time = time.time()
        print(f"Tiempo de carga del excel final: {end_time - start_time:.9f}")
        start_time = end_time
