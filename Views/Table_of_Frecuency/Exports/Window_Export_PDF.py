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
    W_Export_PDF.geometry("700x300")
    W_Export_PDF.title("Exportar en PDF")
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
    W_Export_PDF.iconphoto(False , Icon)
    W_Export_PDF.protocol("WM_DELETE_WINDOW" , Back)

    File_Name = StringVar(W_Export_PDF)
    Path = StringVar(W_Export_PDF)

    Text_Input_File_Name = Label(W_Export_PDF , text="Nombre del archivo:" , font=("Times New Roman" , 13))
    Text_Input_File_Name.place(x=20 , y=20)
    Input_File_Name = Entry(W_Export_PDF , font=("Courier New" , 13) , textvariable=File_Name)
    Input_File_Name.place(x=250 , y=20)

    Text_Input_Path = Label(W_Export_PDF , text="Ruta de exportacion:" , font=("Times New Roman" , 13))
    Text_Input_Path.place(x=20 , y=60)
    Input_Path = Entry(W_Export_PDF , font=("Courier New" , 13) , textvariable=Path)
    Input_Path.config(state="disabled")
    Input_Path.place(x=250 , y=60)

    Btn_Examine = Button(W_Export_PDF , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_Path(Path))
    Btn_Examine.place(x=100 , y=80)

    Btn_Export_PDF = Button(W_Export_PDF , text="Exportar PDF" , font=("Times New Roman" , 13) , command= lambda: Export_Table_In_PDF(W_Export_As_File , W_Export_PDF , Results_From_Single_Column , Results_From_Multiple_Column , Path.get() , File_Name.get() , ""))
    Btn_Export_PDF.place(x=300 , y=120)

    W_Export_PDF.mainloop()

if(__name__ == "__main__"):
    Create_Window_Export_PDF()