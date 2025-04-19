import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..')))

from Path_Manager import Get_Resource_Path
from Calcs.Table_of_Frecuency.Exports.Export_PDF import Export_Table_In_PDF

from tkinter import *
from tkinter import filedialog

def Select_Path(Path):
    File_Path = filedialog.askdirectory()
    if(File_Path):
        Path.set(File_Path)

def Create_Window_Export_PDF(W_Export_As_File , Results_From_Single_Column , Results_From_Multiple_Column):
    def Back():
        for widget in W_Export_PDF.winfo_children():
            widget.destroy()
        W_Export_PDF.quit()
        W_Export_PDF.destroy()
        W_Export_As_File.state(newstate="normal")

    if(W_Export_As_File):
        W_Export_As_File.state(newstate="withdraw")
        W_Export_PDF = Toplevel(W_Export_As_File)
        W_Export_PDF.lift()
    else:
        W_Export_PDF = Tk()
    W_Export_PDF.geometry("700x180+430+350")
    W_Export_PDF.title("Exportar en PDF")
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
    W_Export_PDF.iconphoto(False , Icon)
    W_Export_PDF.protocol("WM_DELETE_WINDOW" , Back)
    W_Export_PDF.config(bg="#CDC4FF")

    File_Name = StringVar(W_Export_PDF)
    Path = StringVar(W_Export_PDF)

    Text_Input_File_Name = Label(W_Export_PDF , text="Ingrese el nombre del archivo (opcional):" , font=("Times New Roman" , 13) , bg="#CDC4FF")
    Text_Input_File_Name.place(x=20 , y=20)
    Input_File_Name = Entry(W_Export_PDF , font=("Courier New" , 13) , textvariable=File_Name)
    Input_File_Name.place(x=315 , y=20 , width=365)

    Text_Input_Path = Label(W_Export_PDF , text="Ingrese la ruta de exportacion:" , font=("Times New Roman" , 13) , bg="#CDC4FF")
    Text_Input_Path.place(x=20 , y=60)
    Input_Path = Entry(W_Export_PDF , font=("Courier New" , 13) , textvariable=Path)
    Input_Path.config(state="disabled")
    Input_Path.place(x=315 , y=60 , width=365)

    Btn_Search_Route = Button(W_Export_PDF , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_Path(Path) , bg="#EBF3F7")
    Btn_Search_Route.place(x=90 , y=90)

    Btn_Export_PDF = Button(W_Export_PDF , text="Exportar PDF" , font=("Times New Roman" , 13) , command= lambda: Export_Table_In_PDF(W_Export_As_File , W_Export_PDF , Results_From_Single_Column , Results_From_Multiple_Column , Path.get() , File_Name.get() , "") , bg="#FDA8C0")
    Btn_Export_PDF.place(x=300 , y=130)

    W_Export_PDF.mainloop()

if(__name__ == "__main__"):
    Create_Window_Export_PDF()