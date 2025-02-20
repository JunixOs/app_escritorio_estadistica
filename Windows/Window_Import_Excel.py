from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd # type: ignore
import openpyxl

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
            for i in range(2 , 6):
                self.treeview.heading(f"{i}", text="")

    def Display(self):
        self.place(x=40 , y=430)

    def Hidden(self):
        self.place_forget()
    def insert_data(self, columns, data , start_row , end_row):
        # encabezados
        
        for i , col in enumerate(columns, start=2):
            self.treeview.heading(f"{i}", text=col)  # Asigna el texto del encabezado para cada columna
            i += 1
        
        # Insertar los datos fila por fila
        for i, (index, row) in enumerate(data.iterrows(), start=start_row):
            if(end_row - start_row + 1 > 150):
                if(i >10+start_row-1 and i<=13+start_row-1):
                    self.treeview.insert("" , "end" , values=("......." , "......."))
                    continue
                elif(i>13+start_row-1 and i<=end_row - start_row + 1 - 10):
                    continue
                values = tuple([i] + row.tolist())
                self.treeview.insert("" , "end" , values=values)
            else:
                values = tuple([i] + row.tolist())
                self.treeview.insert("" , "end" , values=values)
            i += 1

def Import_Data_From_Single_Column(File_Path , Sheet_Number , column , start_row , end_row , Preview , Data , Data_From_Single_Column):
    Load_Excel = openpyxl.load_workbook(File_Path.get() , read_only=True)

    if(start_row > 2000):
        Excel = pd.read_excel(File_Path.get() , sheet_name=Sheet_Number , engine="openpyxl" , usecols=f"{column}:{column}" , skiprows=start_row - 1 , nrows=end_row-start_row+1)
        header_row = Excel.iloc[0]
        if header_row.isnull().any() or any(header_row == '') or not any(isinstance(header_row , str)):
            Excel.columns = [f"Columna {i+1}" for i in range(Excel.shape[1])]
        
        data = Excel.copy()
        data.dropna()

        columns = data.columns

        Preview.clear_table()
        Preview.insert_data(columns , data , start_row , end_row)
    else:
        Excel = pd.read_excel(File_Path.get() , sheet_name=Sheet_Number , engine="openpyxl" , usecols=f"{column}:{column}" , nrows=end_row + 10)
        if(start_row == 1):
            data = Excel.iloc[start_row-1:end_row-1]
            data.dropna()

            columns = data.columns

            Preview.clear_table()
            Preview.insert_data(columns , data , 2 , end_row)
        else:
            data = Excel.iloc[start_row-2:end_row-1]
            data.dropna()
            columns = data.columns

            Preview.clear_table()
            Preview.insert_data(columns , data , start_row , end_row)

    if isinstance(Excel.columns , str):
        Excel.columns = ["Datos Importados"] * Excel.shape[1]

    if data.isnull().all().all():
        raise Exception("Los datos seleccionados están vacíos o contienen solo valores nulos.")
    Data_From_Single_Column["S_Column"] = [value[0] for value in data.values]

    if(Data):
        Data.set("")
    if __name__ != "__main__":
        """ data = ' '.join(map(str , data.squeeze()))
        Data.set(data) """
        Data.set(f"Columna Importada: {Excel.columns[0]}")
    
    Load_Excel.close()

def Import_Data_From_Multiple_Columns(File_Path , Sheet_Number , start_column , end_column , start_row , end_row , Preview , Data , Data_From_Multiple_Columns):
    start_col_index = ord(start_column.upper()) - ord('A')
    end_col_index = ord(end_column.upper()) - ord('A')
    if(end_col_index - start_col_index + 1 > 5):
        raise Exception("Solo puede importar 5 columnas como maximo.")
    
    Load_Excel = openpyxl.load_workbook(File_Path.get() , read_only=True)

    if(start_row > 2000):
        Excel = pd.read_excel(File_Path.get() , sheet_name=Sheet_Number , engine="openpyxl" , usecols=f"{start_column}:{end_column}" , skiprows=start_row - 1 , nrows=end_row-start_row+1 , header=None)
        header_row = Excel.iloc[0]
        if header_row.isnull().any() or any(header_row == '') or not any(isinstance(header_row , str)):
            Excel.columns = [f"Columna {i+1}" for i in range(Excel.shape[1])]
        
        data = Excel.copy()
        columns = data.columns

        Preview.clear_table()
        Preview.insert_data(columns , data , start_row , end_row)
    else:
        Excel = pd.read_excel(File_Path.get() , sheet_name=Sheet_Number , engine="openpyxl" , usecols=f"{start_column}:{end_column}" , nrows=end_row + 10)
        if(start_row == 1):
            data = Excel.iloc[start_row-1:end_row-1]
            columns = data.columns

            Preview.clear_table()
            Preview.insert_data(columns , data , 2 , end_row)
        else:
            data = Excel.iloc[start_row-2:end_row-1]
            columns = data.columns

            Preview.clear_table()
            Preview.insert_data(columns , data , start_row , end_row)

    if data.isnull().all().all():
        raise Exception("Los datos seleccionados están vacíos o contienen solo valores nulos.")

    if(Data):
        Data.set("")
    text = "columnas importadas: "
    for Column in Excel.columns:
        Data_From_Multiple_Columns[Column] = [value for value in data[Column].dropna()]
        text = text + Column + "  "

    Load_Excel.close()

    Data.set(text)

def Process_File_Data(Window_Root , File_Path , Sheet_Number , Cell_Range , Preview , Data , Input_Data , Checked_Import_Multiple_Columns , Data_From_Single_Column , Data_From_Multiple_Columns):
    """ Implementar una previsualizacion de archivos .xlsx """
    """ Separar en diferentes ventanas, uno para importar de un .xlsx y otro para importar de un .txt """
    try:
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
        
        Sheet_Number -= 1
        
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
                    raise Exception("Seleccionaste solo una columna individual.")
                
                Import_Data_From_Multiple_Columns(File_Path , Sheet_Number , column_start , column_end , start_row , end_row , Preview , Data , Data_From_Multiple_Columns)
            case False:
                if column_start == column_end:
                    if start_row == end_row:
                        raise Exception("Seleccionaste una celda individual, no es un rango válido.")
                else:
                    raise Exception("Solo se permite seleccionar datos de una sola fila.")
                Import_Data_From_Single_Column(File_Path , Sheet_Number , column_start , start_row , end_row , Preview , Data , Data_From_Single_Column)
            case _:
                raise Exception("Hubo un error al realizar la importacion")

    except (FileNotFoundError , Exception) as e:
        messagebox.showerror("Error" , f"{e}")
    else:
        Input_Data.config(state="disabled")
        Reply = messagebox.askquestion("Success" , "Datos procesados con exito.\n¿Deseea salir de la ventana de importacion? ")
        if(Reply == "yes"):
            Window_Root.destroy()

def Select_File(Path):
    Path_File = filedialog.askopenfilename(filetypes=[("Archivos Excel" , "*.xlsx")])
    if Path_File:
        if Path:
            Path.set("")
            Path.set(Path_File)
        else:
            Path.set(Path_File)

def Create_Window_Import_Excel(Father_Window , Data , Input_Data , Data_From_Single_Column , Data_From_Multiple_Columns):
    if __name__ == "__main__":
        Window_Root = Tk()
    else:
        Window_Root = Toplevel(Father_Window)

    Icon = PhotoImage(file="Images/icon.png")

    Window_Root.grab_set()
    Window_Root.geometry("700x550+400+220")
    Window_Root.title("Seleccionar Archivo")
    Window_Root.config(bg="#d1e7d2")
    Window_Root.iconphoto(False , Icon)
    
    Path = StringVar(Window_Root)
    Cell_Range = StringVar(Window_Root)
    Sheet_Number = IntVar(Window_Root)
    Import_Multiple_Colums = BooleanVar(Window_Root)

    Text_Input_Path_File = Label(Window_Root , text="Ingrese la ruta del archivo: " , bg="#d1e7d2" , font=("Times New Roman" , 12))
    Text_Input_Path_File.place(x=20 , y=20)
    Path_File = Entry(Window_Root , font=("Courier New" , 11) , textvariable=Path , width=52)
    Path_File.place(x=210 , y=22)
    Btn_Select_File = Button(Window_Root , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_File(Path) , width=10 , bg="#ffe3d4")
    Btn_Select_File.place(x=50 , y=50)

    Text_Input_Sheet_Number = Label(Window_Root , text="Numero de Hoja: " , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Sheet_Number.place(x=20 , y=100)
    Input_Sheet_Number = Spinbox(Window_Root , font=("Courier New" , 13) , textvariable=Sheet_Number , from_=1 , to=100 , width=4)
    Input_Sheet_Number.place(x=210 , y=100)

    style = ttk.Style()
    style.configure("Custom.TCheckbutton", font=("Times New Roman", 13) , background="#d1e7d2")
    Input_Multiple_Columns = ttk.Checkbutton(Window_Root , text="Importar datos de multiples columnas" , variable=Import_Multiple_Colums , style="Custom.TCheckbutton")
    Input_Multiple_Columns.place(x=380 , y=100)

    Text_Input_Cells_Range = Label(Window_Root , text="Ingrese el rango de celdas:\nSolo los datos" , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Cells_Range.place(x=20 , y=140)
    Cells_Range = Entry(Window_Root , font=("Courier New" , 13) , textvariable=Cell_Range , width=47)
    Cells_Range.place(x=210 , y=140)

    Preview_Data = Frame(Window_Root)
    Preview_Data.place(x=20 , y=190)

    Text_Preview_Data = TreeviewFrame(Preview_Data) # Aqui no puedo usar StingVar(), solo usar los metodos get() y set()
    Text_Preview_Data.treeview.config(height=14)
    Text_Preview_Data.pack(side=TOP, fill=BOTH, expand=True)
    Text_Preview_Data.treeview.config(columns=("1", "2" ,"3", "4", "5" , "6") , show="headings")
    Text_Preview_Data.treeview.heading("1" , text="indice")
    for a in range(1 , 7):
        Text_Preview_Data.treeview.column(f"{a}" , anchor="center" , width=106)

    """ Scroll = Scrollbar(Preview_Data , command=Text_Preview_Data.yview)
    Scroll.pack(side=RIGHT , fill=Y)

    Text_Preview_Data.config(yscrollcommand=Scroll.set)
    Text_Preview_Data.insert(END , "Una vez procesado tu archivo, tus datos se mostraran aqui...")
    Text_Preview_Data.config(font=("Times New Roman" , 13)) """

    Btn_Process_Data = Button(Window_Root , text="Procesar Archivo" , font=("Times New Roman" , 13) , width=25 , bg="#ffe3d4" , command=lambda: Process_File_Data(Window_Root , Path , Sheet_Number.get() , Cell_Range , Text_Preview_Data , Data , Input_Data , Import_Multiple_Colums.get() , Data_From_Single_Column , Data_From_Multiple_Columns))
    Btn_Process_Data.pack(side=BOTTOM)

    Window_Root.resizable(False,False)
    Window_Root.mainloop()

if __name__ == "__main__":
    Create_Window_Import_Excel(None , "" , "" , "" , {})