import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Calcs.Exports.Export_Excel import Export_Table_In_Excel
from tkinter import *
from tkinter import filedialog

def Select_File(Path):
    Path_File = filedialog.askdirectory(title="Seleccione una carpeta")
    if Path_File:
        if(Path):
            Path.set("")
            Path.set(Path_File)
        else:
            Path.set(Path_File)

def Generate_Window_Export_Excel(Father_Window , Data_From_Single_Column , Data_From_Multiple_Column , Type_Of_Variable_For_Single_Column , Type_Of_Variable_For_Multiple_Column):
    if __name__== "__main__":
        W_Export_Excel = Tk()
    else:
        W_Export_Excel = Toplevel(Father_Window)
        W_Export_Excel.grab_set()

    W_Export_Excel.geometry("700x180+450+350")
    Icon = PhotoImage(file="Images/icon.png")
    W_Export_Excel.iconphoto(False , Icon)
    W_Export_Excel.title("Exportar Excel")

    File_Name = StringVar(W_Export_Excel)
    Path = StringVar(W_Export_Excel)

    Text_Input_File_Name = Label(W_Export_Excel , text="Ingrese el nombre del archivo (opcional):" , font=("Times New Roman" , 13))
    Text_Input_File_Name.place(x=20 , y=20)
    Input_File_Name = Entry(W_Export_Excel , font=("Courier New" , 13) , textvariable=File_Name , width=35)
    Input_File_Name.place(x=315 , y=20)
    Input_File_Name.focus()

    Text_Input_Route = Label(W_Export_Excel , text="Ingrese la ruta de exportacion:" , font=("Times New Roman" , 13))
    Text_Input_Route.place(x=20 , y=60)
    Input_Route = Entry(W_Export_Excel , font=("Courier New" , 13) , textvariable=Path , width=35)
    Input_Route.place(x=315 , y=60)

    Btn_Search_Route = Button(W_Export_Excel , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_File(Path))
    Btn_Search_Route.place(x=100 , y=90)

    Btn_Generate = Button(W_Export_Excel , text="Generar" , font=("Times New Roman" , 13) , width=20 , command=lambda: Export_Table_In_Excel(W_Export_Excel , Data , Type_Of_Variable , Path.get() , File_Name.get()))
    Btn_Generate.pack(side=BOTTOM)

    W_Export_Excel.resizable(False , False)
    W_Export_Excel.mainloop()

if __name__ == "__main__":
    Generate_Window_Export_Excel(None , None , None)

