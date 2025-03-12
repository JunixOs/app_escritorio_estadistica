import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Exceptions.Exception_Warning import Raise_Warning
from tkinter import *
from tkinter import messagebox
import pandas as pd # type: ignore
import openpyxl
from openpyxl.utils import column_index_from_string
import re

class Validator:
    def Validate_For_Each_Range_Cells(self , One_Range_Cells):
        One_Range_Cells = One_Range_Cells.upper()
        One_Range_Cells = re.match(r"([A-Z]{1,3})(\d+):([A-Z]{1,3})(\d+)" , One_Range_Cells.strip())
        if(not One_Range_Cells):
            raise Raise_Warning("El rango de celdas ingresado es incorrecto.")
        return One_Range_Cells.groups()

    def Validate_Order_Range_Cells(self , Start_Row , End_Row , Start_Column , End_Column):
        if(Start_Column == End_Column and Start_Row == End_Row):
            raise Raise_Warning("No se puede seleccionar una sola celda.")
        elif(Start_Row > End_Row):
            Start_Row , End_Row = End_Row , Start_Row
        elif(Start_Column > End_Column):
            Start_Column , End_Column = End_Column , Start_Column
        return Start_Row , End_Row , Start_Column , End_Column
    
    def Validate_Row_Limit_Excel(self , Input_Start_Row , Input_End_Row , Limit_Excel_End_Rows):
        if(Input_Start_Row > Limit_Excel_End_Rows or Input_End_Row > Limit_Excel_End_Rows):
            raise Raise_Warning("Se intento acceder a una fila no valida, fuera de alcance o sin nungun dato. Intente nuevamente.")
        
    def Validate_Column_Limit_Excel(self , Input_Start_Column , Input_End_Column , Limit_Excel_End_Columns):
        Input_Start_Column = column_index_from_string(Input_Start_Column)
        Input_End_Column = column_index_from_string(Input_End_Column)

        if(Input_Start_Column > Limit_Excel_End_Columns or Input_End_Column > Limit_Excel_End_Columns):
            raise Raise_Warning("Se intento acceder a una fila no valida, fuera de alcance o sin nungun dato. Intente nuevamente.")
        
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
        
    def Validate_Data_Imported_Is_Null(self , Imported_Data):
        if(Imported_Data.isnull().all().all()):
            raise Raise_Warning("Los datos seleccionados están vacíos o contienen solo valores nulos.")
        if(Imported_Data.isnull().any().any()):
            raise Raise_Warning("Los datos seleccionados contienen algun valor nulo. Por favor, revise si los datos tienen un formato adecuado.")


class Import_Preview:
    def __init__(self , W_Preview_Data , Imported_Data):
        self.W_Preview_Data = W_Preview_Data # Treeview
        self.Imported_Data = Imported_Data

    def Insert_Imported_Data_To_Preview(self , Start_Row , End_Row):
        self.W_Preview_Data.treeview.delete(*self.W_Preview_Data.treeview.get_children())

        self.Imported_Data = self.Imported_Data.dropna(axis=1, how='all')
        self.W_Preview_Data.treeview["columns"] = []
        self.W_Preview_Data.treeview["columns"] = ["fila"] + self.Imported_Data.columns.tolist()

        self.W_Preview_Data.treeview.heading("fila" , text="N° fila")
        self.W_Preview_Data.treeview.column("fila" , anchor="center" , width=120 , stretch=False)
        for col in self.Imported_Data.columns:
            self.W_Preview_Data.treeview.heading(col , text=col)
            self.W_Preview_Data.treeview.column(col , anchor="center" , width=120 , stretch=False)

        Dot_Text = tuple(["......."] for _ in range(0 , len(self.W_Preview_Data.treeview["columns"])))

        # Insertar los datos fila por fila
        if(End_Row - Start_Row + 1 >= 100):
            for (index, row) in (self.Imported_Data.head().iterrows()):
                    values = tuple([index + 2] + row.tolist())
                    self.W_Preview_Data.treeview.insert("" , "end" , values=values)
            for i in range(0 , 3):
                self.W_Preview_Data.treeview.insert("" , "end" , values=Dot_Text)
            for (index, row) in (self.Imported_Data.tail().iterrows()):
                    values = tuple([index + 2] + row.tolist())
                    self.W_Preview_Data.treeview.insert("" , "end" , values=values)
        else:
            for (index, row) in (self.Imported_Data.iterrows()):
                    values = tuple([index + 1] + row.tolist())
                    self.W_Preview_Data.treeview.insert("" , "end" , values=values)

        self.W_Preview_Data.Progress_Bar.Close_Progress_Bar()

        messagebox.showinfo("Success" , "Datos procesados con exito.\nYa puede salir de la ventana de importacion.")

class Import_Excel_Using_Single_Range_Of_Cells(Validator):
    def __init__(self , File_Path , Sheet_Number , Range_Cells):
        Validator.__init__(self)

        self.File_Path = File_Path
        self.Sheet_Number = Sheet_Number - 1
        self.Range_Cells = Range_Cells
        self.Import_Multiple_Columns = False

    def Process_Input_Data(self):
        Validator.Validate_Path(self , self.File_Path)
        Validator.Validate_Sheets(self, self.Sheet_Number , self.File_Path)

        self.Start_Column , self.Start_Row , self.End_Column , self.End_Row = Validator.Validate_For_Each_Range_Cells(self , self.Range_Cells)

        self.Start_Row , self.End_Row = int(self.Start_Row) , int(self.End_Row)

        self.Start_Row , self.End_Row , self.Start_Column , self.End_Column = Validator.Validate_Order_Range_Cells(self, self.Start_Row , self.End_Row , self.Start_Column , self.End_Column)

        if(self.End_Column != self.Start_Column):
            self.Import_Multiple_Columns = True
    
    def Import_Data(self , W_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Data_From_Single_Column , Data_From_Multiple_Columns):
        Previous_Loaded_Excel = openpyxl.load_workbook(self.File_Path , read_only=True)

        Sheet_Name = Previous_Loaded_Excel.sheetnames[self.Sheet_Number]
        Sheet = Previous_Loaded_Excel[Sheet_Name]

        Total_Rows_In_Excel = Sheet.max_row
        Total_Columns_In_Excel = Sheet.max_column

        Validator.Validate_Row_Limit_Excel(self, self.Start_Row , self.End_Row , Total_Rows_In_Excel)
        Validator.Validate_Column_Limit_Excel(self , self.Start_Column , self.End_Column , Total_Columns_In_Excel)

        Load_Excel = pd.read_excel(self.File_Path , sheet_name=self.Sheet_Number , engine="openpyxl" , usecols=f"{self.Start_Column}:{self.End_Column}" , nrows=self.End_Row + 10)
        if("Unnamed" in Load_Excel.columns):
            raise Raise_Warning("Se intento importar datos sin un encabezado adecuado. Por favor, coloque un nombre adecuado a los datos y coloquelos en la primera fila.")

        self.Imported_Column_Names = Load_Excel.columns        
        if(self.Start_Row == 1):
            self.Imported_Data = Load_Excel.iloc[self.Start_Row-1:self.End_Row-1]
        else:
            self.Imported_Data = Load_Excel.iloc[self.Start_Row-2:self.End_Row-1]

        Validator.Validate_Data_Imported_Is_Null(self , self.Imported_Data)

        self.Load_Imports_In_Preview(W_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Data_From_Single_Column , Data_From_Multiple_Columns)
    
    def Load_Imports_In_Preview(self, W_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Data_From_Single_Column , Data_From_Multiple_Columns):
        W_Preview_Data.clear_table()
        Load_Preview = Import_Preview(W_Preview_Data , self.Imported_Data)

        if(Data_From_Entry_Widget.get()):
            Data_From_Entry_Widget.set("")
        if(Data_From_Single_Column):
            Data_From_Single_Column.clear()
        if(Data_From_Multiple_Columns):
            Data_From_Multiple_Columns.clear()

        match(self.Import_Multiple_Columns):
            case True:
                text = "columnas importadas: "

                for column in self.Imported_Column_Names:
                    Data_From_Multiple_Columns[column] = [value for value in self.Imported_Data[column].dropna()]
                    text = text + column + "  "

                Widget_Input_Data.config(state="disabled")
                Data_From_Entry_Widget.set(text)

                Load_Preview.Insert_Imported_Data_To_Preview(self.Start_Row , self.End_Row)

            case False:
                Data_From_Single_Column[f"{self.Imported_Column_Names[0]}"] = [value[0] for value in self.Imported_Data.values]

                Widget_Input_Data.config(state="disabled")
                Data_From_Entry_Widget.set(f"Columna Importada: {self.Imported_Column_Names[0]}")

                Load_Preview.Insert_Imported_Data_To_Preview(self.Start_Row , self.End_Row)

class Import_Excel_Using_Multiple_Range_Of_Cells(Validator):
    def __init__(self , File_Path , Sheet_Number , Range_Cells):
        Validator.__init__(self)

        self.File_Path = File_Path
        self.Sheet_Number = Sheet_Number - 1
        self.Range_Cells = Range_Cells
        self.Collection_Of_Cells = {
            "Columns" : [],
            "Rows" : [],
        }
        self.Imported_Data = None

    def Process_Input_Data(self):
        Validator.Validate_Path(self , self.File_Path)
        Validator.Validate_Sheets(self, self.Sheet_Number , self.File_Path)

        Ranges = self.Range_Cells.split(";")
        for ran in Ranges:
            self.Start_Column , self.Start_Row , self.End_Column , self.End_Row = Validator.Validate_For_Each_Range_Cells(self , ran)
            self.Start_Row , self.End_Row = int(self.Start_Row) , int(self.End_Row)

            self.Start_Row , self.End_Row , self.Start_Column , self.End_Column = Validator.Validate_Order_Range_Cells(self , self.Start_Row , self.End_Row , self.Start_Column , self.End_Column)

            self.Collection_Of_Cells["Columns"].append([self.Start_Column , self.End_Column])
            self.Collection_Of_Cells["Rows"].append([self.Start_Row , self.End_Row])
        
    def Import_Data(self , W_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Data_From_Multiple_Columns):
        Previous_Loaded_Excel = openpyxl.load_workbook(self.File_Path , read_only=True)
        
        Sheet_Name = Previous_Loaded_Excel.sheetnames[self.Sheet_Number]
        Sheet = Previous_Loaded_Excel[Sheet_Name]

        Total_Rows_In_Excel = Sheet.max_row
        Total_Columns_In_Excel = Sheet.max_column

        Arr_Columns = []
        Arr_Rows = []
        for row in self.Collection_Of_Cells["Rows"]:
            Validator.Validate_Row_Limit_Excel(self , row[0] , row[1] , Total_Rows_In_Excel)
            Arr_Rows.append(row[0])
            Arr_Rows.append(row[1])
        
        for col in self.Collection_Of_Cells["Columns"]:
            Validator.Validate_Column_Limit_Excel(self , col[0] , col[1] , Total_Columns_In_Excel)
            Arr_Columns.append(col[0])
            Arr_Columns.append(col[1])

        Only_Unique_Columns = list(set(Arr_Columns))
        Columns_List_To_String = ",".join(Only_Unique_Columns)

        Load_Excel = pd.read_excel(self.File_Path , sheet_name=self.Sheet_Number , engine="openpyxl" , usecols=Columns_List_To_String , nrows=max(Arr_Rows) + 10)
        if("unnamed" in Load_Excel.columns):
            raise Raise_Warning("Se intento importar datos sin un encabezado adecuado. Por favor, coloque un nombre adecuado a los datos y coloquelos en la primera fila.")
        
        self.Imported_Columns_Name = Load_Excel.columns
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
                prev_n = n
                if(column_index_from_string(self.Collection_Of_Cells["Columns"][i][1]) - column_index_from_string(self.Collection_Of_Cells["Columns"][i][1]) >= 1):
                    n += column_index_from_string(self.Collection_Of_Cells["Columns"][i][1]) - column_index_from_string(self.Collection_Of_Cells["Columns"][i][1]) >= 1
                    col = [n_col for n_col in range(prev_n , n + 1)]
                    n += 1
                else:
                    col = n
                    n += 1
                if(self.Collection_Of_Cells["Rows"][i][0] == 1):
                    column_i = Load_Excel.iloc[self.Collection_Of_Cells["Rows"][i][0]-1:self.Collection_Of_Cells["Rows"][i][1]-1 , col]
                else:
                    column_i = Load_Excel.iloc[self.Collection_Of_Cells["Rows"][i][0]-2:self.Collection_Of_Cells["Rows"][i][1]-1 , col]
                column_i.dropna()
                Concat_Columns.append(column_i)

            Previous_Loaded_Excel.close()

            self.Start_Row = min(Arr_Rows)
            self.End_Row = max(Arr_Rows)

            self.Imported_Data = pd.concat(Concat_Columns , axis=1 , ignore_index=True)
            self.Imported_Data.columns = self.Imported_Columns_Name

            Validator.Validate_Data_Imported_Is_Null(self , self.Imported_Data)

            self.Load_Imports_In_Preview(W_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Data_From_Multiple_Columns)
        except Exception as e:
            raise Raise_Warning("Algo salio mal, asegurese de que el rango de celdas ingresado no tenga intersecciones.\nCorrecto: A1:D1001;F1:H1001 \nIncorrecto: A1:D1001;C1:E1001")
        
    def Load_Imports_In_Preview(self, W_Preview_Data , Data_From_Entry_Widget , Widget_Input_Data , Data_From_Multiple_Columns):
        W_Preview_Data.clear_table()
        Load_Preview = Import_Preview(W_Preview_Data , self.Imported_Data)

        if(Data_From_Entry_Widget.get()):
            Data_From_Entry_Widget.set("")
        if(Data_From_Multiple_Columns):
            Data_From_Multiple_Columns.clear()

        text = "columnas importadas: "

        for column in self.Imported_Columns_Name:
            Data_From_Multiple_Columns[column] = [value for value in self.Imported_Data[column].dropna()]
            text = text + column + "  "

        Widget_Input_Data.config(state="disabled")
        Data_From_Entry_Widget.set(text)

        Load_Preview.Insert_Imported_Data_To_Preview(self.Start_Row , self.End_Row)