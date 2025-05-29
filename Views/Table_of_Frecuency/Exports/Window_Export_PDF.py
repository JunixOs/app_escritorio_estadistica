import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..')))

from Tools import Get_Resource_Path
from Calcs.Table_of_Frecuency.Exports.Export_PDF import Export_Table_In_PDF
from Calcs.Center_Window import Center

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
    Columns_To_Export = {}

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

    
    Text_Columns_To_Export = Label(W_Export_PDF , text="Seleccione las tablas a exportar" , font=("Times New Roman" , 13) , bg="#CDC4FF")
    
    if(Results_From_Multiple_Column):
        Text_Columns_To_Export.place(x=200 , y=130 , width=300)
        Max_Height = 0
        for i , variable_name in enumerate(Results_From_Multiple_Column.keys()):
            y_pos = 190 + (i*30)

            Checked_Variable_To_Export = BooleanVar(W_Export_PDF)
            Checkbox_Variable_To_Export = Checkbutton(W_Export_PDF , text=f"{variable_name}" , font=("Times New Roman" , 13) , bg="#CDC4FF" , variable=Checked_Variable_To_Export)
            if(i > 6):
                y_pos -= 210
                Checkbox_Variable_To_Export.place(x=425 , y=y_pos)
            else:
                Checkbox_Variable_To_Export.place(x=20 , y=y_pos)

            Max_Height = y_pos
            Columns_To_Export[f"{variable_name}"] = Checked_Variable_To_Export

        W_Export_PDF.geometry(f"700x{Max_Height + 100}")
        Center(W_Export_PDF , 700 , Max_Height + 100)

    Btn_Export_PDF = Button(W_Export_PDF , text="Exportar PDF" , font=("Times New Roman" , 13) , command= lambda: Export_Table_In_PDF(W_Export_As_File , W_Export_PDF , Results_From_Single_Column , Results_From_Multiple_Column , Path.get() , File_Name.get() , "" , Columns_To_Export) , bg="#FDA8C0")
    Btn_Export_PDF.pack(side=BOTTOM)

    W_Export_PDF.resizable(False , False)
    W_Export_PDF.mainloop()

if(__name__ == "__main__"):
    Create_Window_Export_PDF()