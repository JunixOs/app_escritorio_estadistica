import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Tools import Get_Resource_Path , Delete_Actual_Window , Save_New_Configurations_In_JSON_File , Read_Data_From_JSON , Check_Threads_Alive , Center_Window , Insert_Data_In_Log_File , Get_Detailed_Info_About_Error
from Special_Tkinter_Widgets import Spinbox_With_Validation , Table_Widget
from Calcs.Imports.Import_Data_From_Excel import Selecter_Of_Data_For_Single_Range_Of_Cells , Selecter_Of_Data_For_Multiple_Range_Of_Cells , Importer_Of_All_Data_In_Excel_File
from Window_Progress_Bar import W_Progress_Bar
from Exceptions.Exception_Warning import Raise_Warning

from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
import threading

def Select_File_In_User_Device(W_Import_Excel , File_Path_Stringvar_Value , Table_For_Show_Data , Sheet_Number_Intvar_Value):
    Path_File = filedialog.askopenfilename(filetypes=[("Archivos Excel" , "*.xlsx")])
    if(Path_File):
        if(File_Path_Stringvar_Value):
            File_Path_Stringvar_Value.set("")
            File_Path_Stringvar_Value.set(Path_File)
        else:
            File_Path_Stringvar_Value.set(Path_File)

        Sheet_Number_Intvar_Value.set(1)

        if(not Path_File in Table_For_Show_Data.Extra_Data_For_Been_Saved):
            Table_For_Show_Data.Extra_Data_For_Been_Saved.clear()
        
        Import_All_Data_For_Show_In_Table(W_Import_Excel , File_Path_Stringvar_Value , Sheet_Number_Intvar_Value , Table_For_Show_Data)

def Import_All_Data_For_Show_In_Table(W_Import_Excel , File_Path_Stringvar_Value , Sheet_Number_Intvar_Value , Table_For_Show_Data):
    try:
        Class_Progress_Bar = W_Progress_Bar(W_Import_Excel)
        Class_Progress_Bar.Start_Progress_Bar("Cargando excel, esto podria tomar un momento...")

        if (not os.path.exists(File_Path_Stringvar_Value.get())):
            File_Path_Stringvar_Value.set("")
            raise Raise_Warning("El archivo Excel no existe en la ruta especificada.")

        File_Path = File_Path_Stringvar_Value.get()
        
        Class_Import_All_Data = Importer_Of_All_Data_In_Excel_File(W_Import_Excel , File_Path , Sheet_Number_Intvar_Value , Table_For_Show_Data)

        Threads_List = []

        Thread = threading.Thread(target=Class_Import_All_Data.Get_Excel_File)
        Threads_List.append(Thread)
        Thread.start()

        W_Import_Excel.after(
            500 , 
            Check_Threads_Alive , 
            Threads_List , 
            W_Import_Excel , 
            Class_Progress_Bar , 
            Class_Import_All_Data.Load_Excel_In_Table , 
        )

    except Raise_Warning as e:
        Class_Progress_Bar.Close_Progress_Bar()
        Insert_Data_In_Log_File(e , "Advertencia" , "Importacion de datos")
        messagebox.showwarning("Advertencia" , e)
    except Exception:
        Class_Progress_Bar.Close_Progress_Bar()
        Insert_Data_In_Log_File("Ocurrio un error al importar los datos del archivo" , "Error" , "Importacion de datos" , Get_Detailed_Info_About_Error())
        messagebox.showerror("Error" , "Ocurrio un error al importar los datos del archivo")

def Execute_Classes_For_Import_Data(W_Import_Excel , Cell_Range , Table_Preview_Data , Source_Module_Name , Entry_Widget_For_W_Table_Frecuency , Value_For_Entry_Widget_W_Table_Frecuency , Imported_Data_From_Excel , Sheet_Number):
    try:
        """ 
            FALTA MODIFICAR ESTO PARA EVITAR RUNTIME ERROR CON THREADS
        """
        Class_Progress_Bar = W_Progress_Bar(W_Import_Excel)
        Class_Progress_Bar.Start_Progress_Bar()

        Threads_List = []

        if(not Cell_Range.get()):
            raise Raise_Warning("No se ha ingresado un rango de celdas.")
        
        if(";" in Cell_Range.get()):
            Class_For_Import_Excel = Selecter_Of_Data_For_Multiple_Range_Of_Cells(W_Import_Excel , Table_Preview_Data , Cell_Range.get() , Source_Module_Name , Entry_Widget_For_W_Table_Frecuency , Value_For_Entry_Widget_W_Table_Frecuency , Imported_Data_From_Excel)

            Class_For_Import_Excel.Process_Input_Data()
            Thread = threading.Thread(target= lambda: Class_For_Import_Excel.Select_Data_From_Excel_Dataframe(Table_Preview_Data.Extra_Data_For_Been_Saved[Sheet_Number - 1]["All_Excel_Sheet_Data"] , Table_Preview_Data.Extra_Data_For_Been_Saved[Sheet_Number - 1]["Total_Rows_In_Excel_Sheet"] , Table_Preview_Data.Extra_Data_For_Been_Saved[Sheet_Number - 1]["Total_Columns_In_Excel_Sheet"]))
            Threads_List.append(Thread)
            Thread.start()

            W_Import_Excel.after(
                550 , 
                Check_Threads_Alive , 
                Threads_List ,
                W_Import_Excel , 
                Class_Progress_Bar , 
                Class_For_Import_Excel.Load_Excel_Data_In_Table
            )
        elif(":" in Cell_Range.get()):
            Class_For_Import_Excel = Selecter_Of_Data_For_Single_Range_Of_Cells(W_Import_Excel , Table_Preview_Data , Cell_Range.get() , Source_Module_Name , Entry_Widget_For_W_Table_Frecuency , Value_For_Entry_Widget_W_Table_Frecuency , Imported_Data_From_Excel)

            Class_For_Import_Excel.Process_Input_Data()
            Thread = threading.Thread(target= lambda: Class_For_Import_Excel.Select_Data_From_Excel_Dataframe(Table_Preview_Data.Extra_Data_For_Been_Saved[Sheet_Number - 1]["All_Excel_Sheet_Data"] , Table_Preview_Data.Extra_Data_For_Been_Saved[Sheet_Number - 1]["Total_Rows_In_Excel_Sheet"] , Table_Preview_Data.Extra_Data_For_Been_Saved[Sheet_Number - 1]["Total_Columns_In_Excel_Sheet"]))
            Threads_List.append(Thread)
            Thread.start()

            W_Import_Excel.after(
                550 , 
                Check_Threads_Alive , 
                Threads_List ,
                W_Import_Excel , 
                Class_Progress_Bar , 
                Class_For_Import_Excel.Load_Excel_Data_In_Table
            )
        else:
            raise Raise_Warning("El rango de celdas ingresado es invalido.")

    except (FileNotFoundError , Raise_Warning) as e:
        messagebox.showwarning("Advertencia" , f"{e}")
        Insert_Data_In_Log_File(e , "Advertencia" , "Importacion de datos")
    except Exception as e:
        messagebox.showerror("Error" , "Ocurrio un error al importar los datos del archivo")
        Insert_Data_In_Log_File("Ocurrio un error al importar los datos del archivo" , "Error" , "Importacion de datos" , Get_Detailed_Info_About_Error())

def Create_Window_Configuration_Import_Excel(W_Import_Excel=None):
    def Close_Settings_Window():
        try:
            Save_New_Configurations_In_JSON_File("import_excel_settings" , void_tolerance=Void_Tolerance_Number.get() , maximun_rows_to_display_in_preview=Number_Rows_To_Display.get() , import_matrix_data=Import_Data_Matrix.get())
        except Exception:
            messagebox.showerror("Error" , "Algo salio mal al guardar la configuracion.\nAsegurese que todos los datos esten bien escritos.")
            Insert_Data_In_Log_File("Algo salio mal al guardar la configuracion. Asegurese que todos los datos esten bien escritos." , "Error" , "Importacion de datos de un excel" , Get_Detailed_Info_About_Error())
        else:
            Insert_Data_In_Log_File("Datos guardados correctamente en el archivo de configuracion de importacion de datos de un excel" , "Operacion exitosa" , "Importacion de datos de un excel")
    
    JSON_Settings_Data = Read_Data_From_JSON("import_excel_settings")
    
    W_Configuration_Import_Excel = Toplevel(W_Import_Excel)

    W_Configuration_Import_Excel.grab_set()
    # W_Configuration_Import_Excel.geometry("500x200+500+350")
    Center_Window(W_Configuration_Import_Excel , 500 , 200)
    W_Configuration_Import_Excel.title("Configurar Importacion")
    W_Configuration_Import_Excel.config(bg="#d1e7d2")
    Icon = PhotoImage(master=W_Configuration_Import_Excel , file=Get_Resource_Path("Images/icon.png"))
    W_Configuration_Import_Excel.iconphoto(False , Icon)
    W_Configuration_Import_Excel.protocol("WM_DELETE_WINDOW" , lambda: Delete_Actual_Window(W_Import_Excel , W_Configuration_Import_Excel , False , Close_Settings_Window))
    W_Configuration_Import_Excel.lift()

    Void_Tolerance_Number = IntVar(W_Configuration_Import_Excel)
    Number_Rows_To_Display = IntVar(W_Configuration_Import_Excel)
    Import_Data_Matrix = BooleanVar(W_Configuration_Import_Excel)

    Label_Input_Void_Tolerance = Label(W_Configuration_Import_Excel , text="Tolerancia de celdas vacias (0 - 25):" , font=("Times New Roman" , 12) , bg="#d1e7d2")
    Label_Input_Void_Tolerance.place(x=20 , y=20)
    Input_Void_Tolerance = Spinbox_With_Validation(W_Configuration_Import_Excel , 25 , 0 , 1 , Void_Tolerance_Number , "place" , 3 , x=400 , y=20)
    Void_Tolerance_Number.set(JSON_Settings_Data["void_tolerance"])

    Label_Input_Number_Rows_To_Display = Label(W_Configuration_Import_Excel , text="Filas en la previsualizacion (0 - 2000)" , font=("Times New Roman" , 13) , bg="#d1e7d2")
    Label_Input_Number_Rows_To_Display.place(x=20 , y=60)
    Input_Number_Rows_To_Display = Spinbox_With_Validation(W_Configuration_Import_Excel , 1000 , 10 , 10 , Number_Rows_To_Display , "place" , 5 , x=400 , y=60)
    Number_Rows_To_Display.set(JSON_Settings_Data["maximun_rows_to_display_in_preview"])

    #Checkbox_Import_Data_Matrix = Checkbutton(W_Configuration_Import_Excel , text="Importar matriz de datos" , font=("Times New Roman" , 13) , bg="#d1e7d2" , variable=Import_Data_Matrix)
    #Checkbox_Import_Data_Matrix.place(x=20 , y=100)
    #Import_Data_Matrix.set(JSON_Settings_Data["import_matrix_data"])

    W_Configuration_Import_Excel.resizable(False , False)
    W_Import_Excel.wait_window(W_Configuration_Import_Excel)

    W_Configuration_Import_Excel.mainloop()

def Create_Window_Import_Excel(Father_Window , Value_For_Entry_Widget_W_Table_Frecuency , Entry_Widget_For_W_Table_Frecuency , Imported_Data_From_Excel , Source_Module_Name):
    W_Import_Excel = Toplevel(Father_Window)

    Icon = PhotoImage(master=W_Import_Excel , file=Get_Resource_Path("Images/icon.png"))

    W_Import_Excel.grab_set()
    Center_Window(W_Import_Excel , 800 , 550)

    W_Import_Excel.title("Seleccionar Archivo")
    W_Import_Excel.config(bg="#d1e7d2")
    W_Import_Excel.iconphoto(False , Icon)
    W_Import_Excel.protocol("WM_DELETE_WINDOW" , lambda: Delete_Actual_Window(Father_Window , W_Import_Excel))
    
    # 13 filas y 6 columnas
    for row_idx in range(13):
        W_Import_Excel.rowconfigure(row_idx , weight=1)
    for col_idx in range(6):
        W_Import_Excel.columnconfigure(col_idx , weight=1)

    Path = StringVar(W_Import_Excel)
    Cell_Range = StringVar(W_Import_Excel)
    Sheet_Number = IntVar(W_Import_Excel)

    Table_For_Show_Data = Table_Widget(
        W_Import_Excel , 
        6 , 
        ["fila/columna" , "A" , "B" , "C" , "D" , "E"]
    )
    Table_For_Show_Data.Display_Table(
        "grid" , 
        row=0 , column=0 , columnspan=6 , rowspan=7 , pady=(0 , 1) , sticky="nsew"
    )

    Btn_Configuracion = Button(W_Import_Excel , text="\u2699" , font=("Segoe UI Emoji", 9) , bg="#d1e7d2" , command= lambda: Create_Window_Configuration_Import_Excel(W_Import_Excel))
    Btn_Configuracion.grid(row=8 , column=0 , padx=(8 , 0) , sticky="w")

    Text_Input_Path_File = Label(W_Import_Excel , text="Ingrese la ruta del archivo: " , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Path_File.grid(row=9 , column=0 , padx=(1 , 0))
    Path_File = Entry(W_Import_Excel , font=("Courier New" , 13) , textvariable=Path , state="readonly")
    Path_File.grid(row=9 , column=1 , columnspan=5 , padx=(0 , 5) , sticky="ew")
    Btn_Select_File = Button(W_Import_Excel , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_File_In_User_Device(W_Import_Excel , Path , Table_For_Show_Data , Sheet_Number) , width=10 , bg="#ffe3d4")
    Btn_Select_File.grid(row=10 , column=0 , padx=(2 , 0))

    Text_Input_Sheet_Number = Label(W_Import_Excel , text="Numero de Hoja: " , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Sheet_Number.grid(row=11 , column=0 , padx=(1 , 0))
    Input_Sheet_Number = Spinbox(W_Import_Excel , font=("Courier New" , 13) , textvariable=Sheet_Number , from_=1 , to=100 , width=4 , state="readonly" , command= lambda: Import_All_Data_For_Show_In_Table(W_Import_Excel , Path , Sheet_Number , Table_For_Show_Data))
    Input_Sheet_Number.grid(row=11 , column=1 , sticky="w")

    Text_Input_Cells_Range = Label(W_Import_Excel , text="Ingrese el rango de celdas:" , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Cells_Range.grid(row=12 , column=0 , padx=(1 , 0))
    Cells_Range = Entry(W_Import_Excel , font=("Courier New" , 13) , textvariable=Cell_Range)
    Cells_Range.grid(row=12 , column=1 , columnspan=5 , padx=(0 , 5) , sticky="ew")
    Cells_Range.focus()

    Btn_Process_Data = Button(W_Import_Excel , text="Importar Datos" , font=("Times New Roman" , 13) , width=25 , bg="#ffe3d4" , command=lambda: Execute_Classes_For_Import_Data(W_Import_Excel , Cell_Range , Table_For_Show_Data , Source_Module_Name , Entry_Widget_For_W_Table_Frecuency , Value_For_Entry_Widget_W_Table_Frecuency , Imported_Data_From_Excel , Sheet_Number.get()))
    Btn_Process_Data.grid(row=13 , column=0 , columnspan=6 , sticky="n")

    W_Import_Excel.resizable(False,False)
    Father_Window.wait_window(W_Import_Excel)

    W_Import_Excel.mainloop()