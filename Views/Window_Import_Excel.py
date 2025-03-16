import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Path_Manager import Get_Resource_Path
from Calcs.Imports.Import_Data_From_Excel import Import_Excel_Using_Single_Range_Of_Cells
from Calcs.Imports.Import_Data_From_Excel import Import_Excel_Using_Multiple_Range_Of_Cells
from Window_Progress_Bar import W_Progress_Bar
from Exceptions.Exception_Warning import Raise_Warning

from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd # type: ignore
import threading

def index_to_string(i):
    Letter = ''
    Temp = i
    while Temp >= 0:
        Letter = chr(Temp % 26 + 65) + Letter
        Temp = Temp // 26 - 1
    return Letter

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

    def Load_Excel_File(self , File_Path , Sheet_Number):
        try:
            if(File_Path):
                self.data = pd.ExcelFile(File_Path)
                self.sheets = self.data.sheet_names

                if(Sheet_Number.get() > len(self.sheets)):
                    Sheet_Number.set(Sheet_Number.get() - len(self.sheets))
                    raise Raise_Warning(f"El numero de hoja {Sheet_Number.get() + len(self.sheets)} no existe.")
                
                Sheet_N = Sheet_Number.get() - 1

                self.Load_Sheet_Data(Sheet_N)
        except Raise_Warning as e:
            self.Progress_Bar.Close_Progress_Bar()
            messagebox.showwarning("Advertencia" , f"{e}")
        except Exception as e:
            self.Progress_Bar.Close_Progress_Bar()
            messagebox.showerror("Error" , f"{e}")

    def Load_Sheet_Data(self , Sheet_Number):
        self.treeview.delete(*self.treeview.get_children())

        data = self.data.parse(sheet_name=Sheet_Number)

        data = data.head(50)

        self.treeview["columns"] = []
        self.treeview["columns"] = ["N° fila/columna"] + [f"{i}" for i in range(len(data.columns))]

        self.treeview.heading("N° fila/columna", text="N° fila/columna")
        self.treeview.column("N° fila/columna" , anchor="center" , width=120 , stretch=False)
        for i , col in enumerate(data.columns):
            Col_Letter = index_to_string(i)
            self.treeview.heading(f"{i}" , text=Col_Letter)
            self.treeview.column(f"{i}" , anchor="center" , width=120 , stretch=False)

        # Insertar los datos en el Treeview
        val = tuple([1] + data.columns.tolist())
        self.treeview.insert("" , "end" , values=val)
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
                raise Raise_Warning("El archivo Excel no existe en la ruta especificada.")

            if(isinstance(Sheet_Number.get() , float)):
                Sheet_Number.set(1)
                raise Raise_Warning("Numero de hoja no valido, solo valores enteros")

            threading.Thread(target= lambda: Preview.Load_Excel_File(Path.get() , Sheet_Number)).start()
        except Raise_Warning as e:
            Preview.Progress_Bar.Close_Progress_Bar()
            messagebox.showwarning("Advertencia" , f"{e}")
        except Exception as e:
            Preview.Progress_Bar.Close_Progress_Bar()
            messagebox.showerror("Error" , f"{e}")

def Process_File_Data(File_Path , Widget_Sheet_Number , Cell_Range , Preview , Data_From_Widget_Entry , Widget_Input_Data , Imported_Data_From_Excel , Source_Module_Name):
    """ Separar en diferentes ventanas, uno para importar de un .xlsx y otro para importar de un .txt """
    try:
        Preview.Progress_Bar.Start_Progress_Bar()

        if(not Cell_Range.get()):
            raise Raise_Warning("No se ha ingresado un rango de celdas.")
        
        if(";" in Cell_Range.get()):
            Import_Excel = Import_Excel_Using_Multiple_Range_Of_Cells(File_Path.get() , Widget_Sheet_Number.get() , Cell_Range.get())

            Import_Excel.Process_Input_Data()

            match(Source_Module_Name):
                case "Table_Of_Frecuency":
                    threading.Thread(target= lambda: Import_Excel.Manage_Import_For_Module_Table_Of_Frecuency(Preview , Data_From_Widget_Entry , Widget_Input_Data , Imported_Data_From_Excel)).start()
                case "Venn_Diagram":
                    threading.Thread(target= lambda: Import_Excel.Manage_Import_For_Module_Venn_Diagram(Preview , Data_From_Widget_Entry , Widget_Input_Data , Imported_Data_From_Excel)).start()
                case _:
                    raise Exception("Error al resolver el modulo de origen.")
        elif(":" in Cell_Range.get()):
            Import_Excel = Import_Excel_Using_Single_Range_Of_Cells(File_Path.get() , Widget_Sheet_Number.get() , Cell_Range.get())

            Import_Excel.Process_Input_Data()

            match(Source_Module_Name):
                case "Table_Of_Frecuency":
                    threading.Thread(target= lambda: Import_Excel.Manage_Import_For_Module_Table_Of_Frecuency(Preview , Data_From_Widget_Entry , Widget_Input_Data , Imported_Data_From_Excel)).start()
                case "Venn_Diagram":
                    threading.Thread(target= lambda: Import_Excel.Manage_Import_For_Module_Venn_Diagram(Preview , Data_From_Widget_Entry , Widget_Input_Data , Imported_Data_From_Excel)).start()
                case _:
                    raise Exception("Error al resolver el modulo de origen.")
        else:
            raise Raise_Warning("El rango de celdas ingresado es invalido.")

    except (FileNotFoundError , Raise_Warning) as e:
        Preview.Progress_Bar.Close_Progress_Bar()
        messagebox.showwarning("Advertencia" , f"{e}")
    except Exception as e:
        Preview.Progress_Bar.Close_Progress_Bar()
        messagebox.showerror("Error" , f"{e}")

def Create_Window_Import_Excel(Father_Window , Data_From_Widget_Entry , Widget_Input_Data , Imported_Data_From_Excel , Source_Module_Name):
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

    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))

    W_Import_Excel.grab_set()
    W_Import_Excel.geometry("800x550+350+170")
    W_Import_Excel.title("Seleccionar Archivo")
    W_Import_Excel.config(bg="#d1e7d2")
    W_Import_Excel.iconphoto(False , Icon)
    W_Import_Excel.protocol("WM_DELETE_WINDOW" , Back)
    
    Path = StringVar(W_Import_Excel)
    Cell_Range = StringVar(W_Import_Excel)
    Sheet_Number = IntVar(W_Import_Excel)

    Progress_Bar = W_Progress_Bar(W_Import_Excel)

    Text_Input_Path_File = Label(W_Import_Excel , text="Ingrese la ruta del archivo: " , bg="#d1e7d2" , font=("Times New Roman" , 12))
    Text_Input_Path_File.place(x=20 , y=340)
    Path_File = Entry(W_Import_Excel , font=("Courier New" , 11) , textvariable=Path , width=55 , state="readonly")
    Path_File.place(x=210 , y=340)
    Btn_Select_File = Button(W_Import_Excel , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_File(Path , Table_Preview_Data , Sheet_Number) , width=10 , bg="#ffe3d4")
    Btn_Select_File.place(x=50 , y=370)

    Text_Input_Sheet_Number = Label(W_Import_Excel , text="Numero de Hoja: " , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Sheet_Number.place(x=20 , y=410)
    Input_Sheet_Number = Spinbox(W_Import_Excel , font=("Courier New" , 13) , textvariable=Sheet_Number , from_=1 , to=100 , width=4 , state="readonly" , command= lambda: Load_Excel_To_Preview(Path , Sheet_Number , Table_Preview_Data))
    Input_Sheet_Number.place(x=210 , y=410)

    Text_Input_Cells_Range = Label(W_Import_Excel , text="Ingrese el rango de celdas:" , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Cells_Range.place(x=20 , y=440)
    Cells_Range = Entry(W_Import_Excel , font=("Courier New" , 13) , textvariable=Cell_Range , width=55)
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

    Btn_Process_Data = Button(W_Import_Excel , text="Importar Datos" , font=("Times New Roman" , 13) , width=25 , bg="#ffe3d4" , command=lambda: Process_File_Data(Path , Sheet_Number , Cell_Range , Table_Preview_Data , Data_From_Widget_Entry , Widget_Input_Data , Imported_Data_From_Excel , Source_Module_Name))
    Btn_Process_Data.pack(side=BOTTOM)

    W_Import_Excel.resizable(False,False)
    W_Import_Excel.mainloop()

if __name__ == "__main__":
    Create_Window_Import_Excel(None , "" , "" , "" , {})