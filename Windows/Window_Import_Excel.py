from Window_Progress_Bar import W_Progress_Bar

from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd # type: ignore
import openpyxl
from openpyxl.utils import column_index_from_string
import threading
import string

class TreeviewFrame(ttk.Frame):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hscrollbar = ttk.Scrollbar(self, orient=HORIZONTAL)
        self.vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        self.treeview = ttk.Treeview(
            self,
            xscrollcommand=self.hscrollbar.set,
            yscrollcommand=self.vscrollbar.set
        )
        self.hscrollbar.config(command=self.treeview.xview)
        self.hscrollbar.pack(side=BOTTOM, fill=X)
        self.vscrollbar.config(command=self.treeview.yview)
        self.vscrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.pack(fill="both" , expand=True)

        self.Progress_Bar = None
        self.Root_Window = None

    def Has_Rows(self):
        return len(self.treeview.get_children()) > 0
    
    def clear_table(self):
        if(self.Has_Rows()):
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            self.treeview["columns"] = []

    def Display(self):
        self.place(x=40 , y=430)

    def Hidden(self):
        self.place_forget()

    def Insert_Imported_Data_To_Preview(self, data , start_row , end_row):
        # encabezados
        self.treeview.delete(*self.treeview.get_children())

        data = data.dropna(axis=1, how='all')
        self.treeview["columns"] = []
        self.treeview["columns"] = ["fila"] + data.columns.tolist()

        self.treeview.heading("fila" , text="N° fila")
        self.treeview.column("fila" , anchor="center" , width=120 , stretch=False)
        for col in data.columns:
            self.treeview.heading(col , text=col)
            self.treeview.column(col , anchor="center" , width=120 , stretch=False)

        Dot_Text = tuple(["......."] for _ in range(0 , len(self.treeview["columns"])))

        # Insertar los datos fila por fila
        if(end_row - start_row + 1 >= 100):
            for (index, row) in (data.head().iterrows()):
                    values = tuple([index + 2] + row.tolist())
                    self.treeview.insert("" , "end" , values=values)
            for i in range(0 , 3):
                self.treeview.insert("" , "end" , values=Dot_Text)
            for (index, row) in (data.tail().iterrows()):
                    values = tuple([index + 2] + row.tolist())
                    self.treeview.insert("" , "end" , values=values)
        else:
            for (index, row) in (data.iterrows()):
                    values = tuple([index + 1] + row.tolist())
                    self.treeview.insert("" , "end" , values=values)

        self.Progress_Bar.Close_Progress_Bar()

        messagebox.showinfo("Success" , "Datos procesados con exito.\nYa puede salir de la ventana de importacion.")

    def Load_Excel_File(self , File_Path , Sheet_Number):
        try:
            if(File_Path):
                self.data = pd.ExcelFile(File_Path)
                self.sheets = self.data.sheet_names

                if(Sheet_Number.get() > len(self.sheets)):
                    Sheet_Number.set(Sheet_Number.get() - len(self.sheets))
                    raise Exception(f"El numero de hoja {Sheet_Number.get() + len(self.sheets)} no existe.")
                
                Sheet_N = Sheet_Number.get() - 1

                self.Load_Sheet_Data(Sheet_N)
        except Exception as e:
            self.Progress_Bar.Close_Progress_Bar()
            messagebox.showerror("Error" , f"{e}")

    def Load_Sheet_Data(self , Sheet_Number):
        self.treeview.delete(*self.treeview.get_children())

        data = self.data.parse(sheet_name=Sheet_Number)

        data = data.head(50)

        self.treeview["columns"] = []
        self.treeview["columns"] = ["N° fila/columna"] + [string.ascii_uppercase[i] for i in range(len(data.columns))]

        self.treeview.heading("N° fila/columna", text="N° fila/columna")
        self.treeview.column("N° fila/columna" , anchor="center" , width=120 , stretch=False)
        for i , col in enumerate(data.columns):
            Col_Letter = string.ascii_uppercase[i]
            self.treeview.heading(Col_Letter , text=Col_Letter)
            self.treeview.column(Col_Letter , anchor="center" , width=120 , stretch=False)

        # Insertar los datos en el Treeview
        for (index, row) in data.iterrows():
            values = tuple([index + 2] + row.tolist())
            self.treeview.insert("", "end", values=values)

        self.Progress_Bar.Close_Progress_Bar()
    
def Select_File(Path , Preview , Sheet_Number):
    Path_File = filedialog.askopenfilename(filetypes=[("Archivos Excel" , "*.xlsx")])
    if Path_File:
        if Path:
            Path.set("")
            Path.set(Path_File)
        else:
            Path.set(Path_File)

        Load_Excel_To_Preview(Path , Sheet_Number , Preview)

def Load_Excel_To_Preview(Path, Sheet_Number , Preview):
    if(Path):
        try:
            Preview.Progress_Bar.Start_Progress_Bar("Cargando excel, esto podria tomar un momento...")

            if (not os.path.exists(Path.get())):
                Path.set("")
                raise Exception("El archivo Excel no existe en la ruta especificada.")
            """ elif(not Path.get().lower().endwith(".xlsx")):
                Path.set("")
                raise Exception("El archivo seleccionado no es un archivo Excel.") """

            if(isinstance(Sheet_Number.get() , float)):
                Sheet_Number.set(1)
                raise Exception("Numero de hoja no valido, solo valores enteros")

            threading.Thread(target= lambda: Preview.Load_Excel_File(Path.get() , Sheet_Number)).start()
        except Exception as e:
            Preview.Progress_Bar.Close_Progress_Bar()
            messagebox.showerror("Error" , f"{e}")

def Import_Data_From_Single_Column(File_Path , Widget_Sheet_Number , column , start_row , end_row , Preview , Data_From_Widget_Entry , Data_From_Single_Column , Input_Data):
    try:
        if(Data_From_Widget_Entry):
            Data_From_Widget_Entry.set("")
        if(Data_From_Single_Column):
            Data_From_Single_Column.clear()

        Load_Excel = openpyxl.load_workbook(File_Path.get() , read_only=True)
        Sheet_Number = Widget_Sheet_Number.get()
        Sheet_Number -= 1

        Sheet_Name = Load_Excel.sheetnames[Sheet_Number]
        Sheet = Load_Excel[Sheet_Name]

        total_rows = Sheet.max_row
        total_columns = Sheet.max_column
        column_index = column_index_from_string(column)

        if(end_row > total_rows):
            raise Exception("Se intento acceder a una fila no valida, intente nuevamente.")
        elif(column_index > total_columns):
            raise Exception("Se intento acceder a una columna no valida, intente nuevamente.")

        if(start_row > 2000):
            Excel = pd.read_excel(File_Path.get() , sheet_name=Sheet_Number , engine="openpyxl" , usecols=f"{column}:{column}" , skiprows=start_row - 1 , nrows=end_row-start_row+10)
            header_row = Excel.iloc[0]
            if header_row.isnull().any() or any(header_row == '') or not any(isinstance(header_row , str)):
                Excel.columns = [f"Columna {i+1}" for i in range(Excel.shape[1])]
            
            data = Excel.copy()
        else:
            Excel = pd.read_excel(File_Path.get() , sheet_name=Sheet_Number , engine="openpyxl" , usecols=f"{column}:{column}" , nrows=end_row + 10)
            if(start_row == 1):
                data = Excel.iloc[start_row-1:end_row-1]
            else:
                data = Excel.iloc[start_row-2:end_row-1]

        data.dropna()
        if isinstance(Excel.columns , str):
            Excel.columns = ["Datos Importados"] * Excel.shape[1]

        if data.isnull().all().all():
            raise Exception("Los datos seleccionados están vacíos o contienen solo valores nulos. Por favor, intente con otra columna")
        
        if data.isnull().any().any():
            raise Exception("Los datos seleccionados contienen algun valor nulo. Por favor, revise si los datos tienen un formato adecuado o si el rango de celdas que ingreso cubre solamente los datos a importar y ninguna celda mas.")
        
        Preview.clear_table()
        Preview.Insert_Imported_Data_To_Preview(data , start_row , end_row)

        Data_From_Single_Column[f"{Excel.columns[0]}"] = [value[0] for value in data.values]
        
        Load_Excel.close()

        Data_From_Widget_Entry.set(f"Columna Importada: {Excel.columns[0]}")

    except (FileNotFoundError , Exception) as e:
        Preview.Progress_Bar.Close_Progress_Bar()
        messagebox.showerror("Error" , f"{e}")
    else:
        Input_Data.config(state="disabled")

def Import_Data_From_Multiple_Columns(File_Path , Widget_Sheet_Number , start_column , end_column , start_row , end_row , Preview , Data_From_Widget_Entry , Data_From_Multiple_Columns , Input_Data):
    try:
        if(Data_From_Widget_Entry):
            Data_From_Widget_Entry.set("")

        if(Data_From_Multiple_Columns):
            Data_From_Multiple_Columns.clear()

        Load_Excel = openpyxl.load_workbook(File_Path.get() , read_only=True)
        Sheet_Number = Widget_Sheet_Number.get()
        Sheet_Number -= 1

        Sheet_Name = Load_Excel.sheetnames[Sheet_Number]
        Sheet = Load_Excel[Sheet_Name]

        total_rows = Sheet.max_row
        total_columns = Sheet.max_column
        start_column_index = column_index_from_string(start_column)
        end_column_index = column_index_from_string(end_column)

        if(end_row > total_rows):
            raise Exception("Se intento acceder a una fila no valida, intente nuevamente.")
        elif(start_column_index > total_columns or end_column_index > total_columns):
            raise Exception("Se intento acceder a una columna no valida, intente nuevamente.")

        if(start_row > 2000):
            Excel = pd.read_excel(File_Path.get() , sheet_name=Sheet_Number , engine="openpyxl" , usecols=f"{start_column}:{end_column}" , skiprows=start_row - 1 , nrows=end_row-start_row+1 , header=None)
            header_row = Excel.iloc[0]
            if header_row.isnull().any() or any(header_row == '') or not any(isinstance(header_row , str)):
                Excel.columns = [f"Columna {i+1}" for i in range(Excel.shape[1])]
            
            data = Excel.copy()
        else:
            Excel = pd.read_excel(File_Path.get() , sheet_name=Sheet_Number , engine="openpyxl" , usecols=f"{start_column}:{end_column}" , nrows=end_row + 10)
            if(start_row == 1):
                data = Excel.iloc[start_row-1:end_row-1]
            else:
                data = Excel.iloc[start_row-2:end_row-1]

        if data.isnull().all().all():
            raise Exception("Los datos seleccionados están vacíos o contienen solo valores nulos.")
        
        if data.isnull().any().any():
            raise Exception("Los datos seleccionados contienen algun valor nulo. Por favor, revise si los datos tienen un formato adecuado.")
        
        Preview.clear_table()
        Preview.Insert_Imported_Data_To_Preview(data , start_row , end_row)

        text = "columnas importadas: "
        for Column in Excel.columns:
            Data_From_Multiple_Columns[Column] = [value for value in data[Column].dropna()]
            text = text + Column + "  "

        Load_Excel.close()

        Data_From_Widget_Entry.set(text)

    except (FileNotFoundError , Exception) as e:
        Preview.Progress_Bar.Close_Progress_Bar()
        messagebox.showerror("Error" , f"{e}")
    else:
        Input_Data.config(state="disabled")

def Process_File_Data(File_Path , Widget_Sheet_Number , Cell_Range , Preview , Data_From_Widget_Entry , Input_Data , Checked_Import_Multiple_Columns , Data_From_Single_Column , Data_From_Multiple_Columns):
    """ Separar en diferentes ventanas, uno para importar de un .xlsx y otro para importar de un .txt """
    try:
        Preview.Progress_Bar.Start_Progress_Bar()

        Sheet_Number = Widget_Sheet_Number.get()
        if(not File_Path.get()):
            raise Exception("No se ha ingresado la ruta del archivo.")
        
        if (not os.path.exists(File_Path.get())):
            raise Exception("El archivo Excel no existe en la ruta especificada.")

        if(isinstance(Sheet_Number , float)):
            raise Exception("Numero de hoja no valido, solo valores enteros")
        
        Unload_Excel = pd.ExcelFile(f"{File_Path.get()}")
        Sheets = Unload_Excel.sheet_names
        if(Sheet_Number > len(Sheets)):
            raise Exception("No existe el numero de hoja especificado")
        if(not Cell_Range.get()):
            raise Exception("No se ha ingresado un rango de celdas.")
        elif(Cell_Range.get().count(":") > 1):
            raise Exception("El rango de celdas ingresado es invalido.")
        
        First_Pair, Last_Pair = Cell_Range.get().split(':') # Si ingreso C10:D100 lo separa a "C10" y "D100"
        column_start = First_Pair[0].upper() # Agarro C
        column_end = Last_Pair[0].upper() # Agarro D


        start_row = int(First_Pair[1:])  # El inicio de la fila (por ejemplo, '10')
        end_row = int(Last_Pair[1:])  # El fin de la fila (por ejemplo, '100')
        match(Checked_Import_Multiple_Columns):
            case True:
                if column_start == column_end:  # Verificar si la selección es una sola columna
                    if start_row == end_row:  # Verificar si la selección es una sola fila
                        raise Exception("Seleccionaste una celda individual, no es un rango válido.")
                    raise Exception("No se permite seleccionar datos de una sola columna.")
                
                threading.Thread(target= lambda: Import_Data_From_Multiple_Columns(File_Path , Widget_Sheet_Number , column_start , column_end , start_row , end_row , Preview , Data_From_Widget_Entry , Data_From_Multiple_Columns , Input_Data)).start()
            case False:
                if column_start == column_end:
                    if start_row == end_row:
                        raise Exception("Seleccionaste una celda individual, no es un rango válido.")
                else:
                    raise Exception("Solo se permite seleccionar datos de una sola columna.")
                threading.Thread(target= lambda: Import_Data_From_Single_Column(File_Path , Widget_Sheet_Number , column_start , start_row , end_row , Preview , Data_From_Widget_Entry , Data_From_Single_Column , Input_Data)).start()
            case _:
                raise Exception("Hubo un error al realizar la importacion.")

    except (FileNotFoundError , Exception) as e:
        Preview.Progress_Bar.Close_Progress_Bar()
        messagebox.showerror("Error" , f"{e}")

def Create_Window_Import_Excel(Father_Window , Data_From_Widget_Entry , Input_Data , Data_From_Single_Column , Data_From_Multiple_Columns):
    def Back():
        for widget in W_Import_Excel.winfo_children():
            widget.destroy()
        W_Import_Excel.grab_release()
        W_Import_Excel.quit()
        W_Import_Excel.destroy()

        Father_Window.lift()
    if __name__ == "__main__":
        W_Import_Excel = Tk()
    else:
        W_Import_Excel = Toplevel(Father_Window)

    Icon = PhotoImage(file="Images/icon.png")

    W_Import_Excel.grab_set()
    W_Import_Excel.geometry("800x550+350+170")
    W_Import_Excel.title("Seleccionar Archivo")
    W_Import_Excel.config(bg="#d1e7d2")
    W_Import_Excel.iconphoto(False , Icon)
    W_Import_Excel.protocol("WM_DELETE_WINDOW" , Back)
    
    Path = StringVar(W_Import_Excel)
    Cell_Range = StringVar(W_Import_Excel)
    Sheet_Number = IntVar(W_Import_Excel)
    Import_Multiple_Colums = BooleanVar(W_Import_Excel)
    Progress_Bar = W_Progress_Bar(W_Import_Excel)

    Text_Input_Path_File = Label(W_Import_Excel , text="Ingrese la ruta del archivo: " , bg="#d1e7d2" , font=("Times New Roman" , 12))
    Text_Input_Path_File.place(x=20 , y=340)
    Path_File = Entry(W_Import_Excel , font=("Courier New" , 11) , textvariable=Path , width=45 , state="readonly")
    Path_File.place(x=210 , y=340)
    Btn_Select_File = Button(W_Import_Excel , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_File(Path , Table_Preview_Data , Sheet_Number) , width=10 , bg="#ffe3d4")
    Btn_Select_File.place(x=50 , y=370)

    Text_Input_Sheet_Number = Label(W_Import_Excel , text="Numero de Hoja: " , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Sheet_Number.place(x=20 , y=410)
    Input_Sheet_Number = Spinbox(W_Import_Excel , font=("Courier New" , 13) , textvariable=Sheet_Number , from_=1 , to=100 , width=4 , state="readonly" , command= lambda: Load_Excel_To_Preview(Path , Sheet_Number , Table_Preview_Data))
    Input_Sheet_Number.place(x=210 , y=410)

    style = ttk.Style()
    style.configure("Custom.TCheckbutton", font=("Times New Roman", 13) , background="#d1e7d2")
    Input_Multiple_Columns = ttk.Checkbutton(W_Import_Excel , text="Importar datos de multiples columnas" , variable=Import_Multiple_Colums , style="Custom.TCheckbutton")
    Input_Multiple_Columns.place(x=380 , y=410)

    Text_Input_Cells_Range = Label(W_Import_Excel , text="Ingrese el rango de celdas:\nSolo los datos" , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Cells_Range.place(x=20 , y=440)
    Cells_Range = Entry(W_Import_Excel , font=("Courier New" , 13) , textvariable=Cell_Range , width=15)
    Cells_Range.place(x=210 , y=440)
    Cells_Range.focus()

    Table_Preview_Data = TreeviewFrame(W_Import_Excel)
    Table_Preview_Data.Progress_Bar = Progress_Bar
    Table_Preview_Data.Root_Window = W_Import_Excel
    Table_Preview_Data.pack(fill=BOTH)
    Table_Preview_Data.treeview.config(height=13)
    Table_Preview_Data.treeview.config(columns=("1", "2" ,"3", "4", "5" , "6") , show="headings")
    Table_Preview_Data.treeview.heading("1" , text="fila/columna")
    Table_Preview_Data.treeview.heading("2" , text="A")
    Table_Preview_Data.treeview.heading("3" , text="B")
    Table_Preview_Data.treeview.heading("4" , text="C")
    Table_Preview_Data.treeview.heading("5" , text="D")
    Table_Preview_Data.treeview.heading("6" , text="E")
    for a in range(1 , 7):
        Table_Preview_Data.treeview.column(f"{a}" , anchor="center" , width=106 , stretch=True)

    Btn_Process_Data = Button(W_Import_Excel , text="Procesar Archivo" , font=("Times New Roman" , 13) , width=25 , bg="#ffe3d4" , command=lambda: Process_File_Data(Path , Sheet_Number , Cell_Range , Table_Preview_Data , Data_From_Widget_Entry , Input_Data , Import_Multiple_Colums.get() , Data_From_Single_Column , Data_From_Multiple_Columns))
    Btn_Process_Data.pack(side=BOTTOM)

    W_Import_Excel.resizable(False,False)
    W_Import_Excel.mainloop()

if __name__ == "__main__":
    Create_Window_Import_Excel(None , "" , "" , "" , {})