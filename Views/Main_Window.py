import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Tools import Get_Resource_Path , Get_Version , Verify_Configurations_Folder , Verify_Logs_Folder , Delete_Log_Files_After_Certain_Time , Insert_Data_In_Log_File , Load_Global_Styles , Get_RAM_Memory_In_Device , Get_Number_Of_Util_Threads_In_Device , Center_Window , Get_Detailed_Info_About_Error
from Exceptions.Exception_Warning import Raise_Warning
from Views.Window_View_Logs import Create_Window_View_Logs
import Views.Table_of_Frecuency.Window_Calc_Table_of_Frecuency as W_Calc_Table
import Views.Venn_Diagram.Window_Create_Venn_Diagram as W_Venn_Diagram
import Views.MAS.Window_MAS as W_MAS
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def On_Closing():
    for widget in Main_Window.winfo_children():
        widget.destroy()
    Main_Window.quit()
    Main_Window.destroy()

RAM_Memory = Get_RAM_Memory_In_Device()
Util_Threads = Get_Number_Of_Util_Threads_In_Device()
try:
    if(RAM_Memory["Available"] < 1):
        raise Exception("El programa no puede iniciarse.\nSe ha detectado menos de 1GB de memoria RAM disponible.")
    
    if(Util_Threads < 2):
        raise Exception("El programa no puede iniciarse.\nSe han detectado menos de nucleos en su sistema.")

    try:
        Verify_Configurations_Folder()

        Verify_Logs_Folder()
        Delete_Log_Files_After_Certain_Time()
    except Exception:
        raise Exception("Hubo un error al verificar los archivos de configuracion.")

except Raise_Warning as e:
    messagebox.showwarning("Advertencia" , e)
    Insert_Data_In_Log_File(e , "Advertencia" , "Inicio del programa")
except Exception as e:
    messagebox.showerror("Error" , e)
    Insert_Data_In_Log_File(e , "Error" , "Inicio del programa" , Get_Detailed_Info_About_Error())
else:
    try:
        if(Util_Threads == 2):
            raise Raise_Warning("Se han detectado dos nucleos en su sistema.\nPodra seguir usando el programa,\npero los calculos seran mas lentos de lo normal.")
    except Raise_Warning as e:
        messagebox.showwarning("Advertencia" , e)
        Insert_Data_In_Log_File(e , "Advertencia" , "Inicio del programa")

    Main_Window = Tk()

    Image_Right_Section = PhotoImage(file=Get_Resource_Path("Images/normal_distribution.png"))
    Image_Right_Section.subsample(10)
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))

    Global_ttk_Style = ttk.Style()
    Global_ttk_Style.theme_use("clam")

    Load_Global_Styles(Global_ttk_Style)

    Center_Window(Main_Window , 1240 , 700)

    Main_Window.title(f"StatPhi {Get_Version()}")
    Main_Window.config(bg="#9DAEC6")
    Main_Window.iconphoto(False , Icon)

    Right_Section = Label(Main_Window , width=531 , height=691 , bg="#F7EDCB" , image=Image_Right_Section , highlightthickness=2 , highlightbackground="#000000")
    Right_Section.place(x=700 , y=0)

    BtnFrecuencyTable = Button(Main_Window , text="Crear tabla de frecuencias" , font=("Times New Roman", 14) , command= lambda: W_Calc_Table.Create_Window_Frecuences_Table(Main_Window) , width=30 , bg="#FBCFC6")
    BtnFrecuencyTable.place(x=190 , y=220)

    BtnVennDiagram = Button(Main_Window , text="Crear Diagramas de Venn" , font=("Times New Roman", 14) , command= lambda: W_Venn_Diagram.Create_Window_Create_Venn_Diagram(Main_Window) , width=30 , bg="#FBCFC6")
    BtnVennDiagram.place(x=190 , y=300)

    BtnMAS = Button(Main_Window , text="Calcular tamaño de muestra" , font=("Times New Roman", 14) , command= lambda: W_MAS.Create_Window_MAS(Main_Window) , width=30 , bg="#FBCFC6")
    BtnMAS.place(x=190 , y=380)

    Main_Window.protocol("WM_DELETE_WINDOW", On_Closing)
    Main_Window.resizable(False,False)
    
    Insert_Data_In_Log_File("Programa iniciado con exito" , "Operacion exitosa" , "Seccion principal")

    Btn_Logs = Button(Main_Window , text="\U0001F4DC" , font=("Segoe UI Emoji", 12) , bg="#F7EDCB" , command= lambda: Create_Window_View_Logs(Main_Window))
    Btn_Logs.place(x=5 , y=5)

    Main_Window.mainloop()

    Insert_Data_In_Log_File("Programa cerrado" , "Operacion de cierre" , "Cierre de programa")