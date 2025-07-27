import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..')))

from Tools import Get_Resource_Path , Delete_Actual_Window , Center_Window
from Views.Table_of_Frecuency.Exports.Window_Export_Excel import Create_Window_Export_Excel
from Views.Table_of_Frecuency.Exports.Window_Export_PDF import Create_Window_Export_PDF

from tkinter import *

def Create_Window_Export_As_File(W_Calc_Frecuences_Table , Results_From_Single_Column , Results_From_Multiple_Column , Type_Of_Variable_For_Single_Column , Type_Of_Variable_For_Multiple_Column):
    if(W_Calc_Frecuences_Table):
        W_Export_As_File = Toplevel(W_Calc_Frecuences_Table)
        Center_Window(W_Export_As_File , 700 , 500)
        W_Export_As_File.grab_set()
        W_Export_As_File.lift()
    else:
        W_Export_As_File = Tk()
        Center_Window(W_Export_As_File , 700 , 500)

    W_Export_As_File.title("Exportar Tabla")
    Icon = PhotoImage(master=W_Export_As_File , file=Get_Resource_Path("Images/icon.png"))
    W_Export_As_File.iconphoto(False , Icon)
    W_Export_As_File.resizable(False , False)
    W_Export_As_File.protocol("WM_DELETE_WINDOW" , lambda: Delete_Actual_Window(W_Calc_Frecuences_Table , W_Export_As_File))
    W_Export_As_File.config(bg="#CDC4FF")

    Btn_Export_In_Excel = Button(W_Export_As_File , text="Exportar como Excel" , font=("Times New Roman" , 13) , command= lambda: Create_Window_Export_Excel(W_Export_As_File , Results_From_Single_Column , Results_From_Multiple_Column , Type_Of_Variable_For_Single_Column , Type_Of_Variable_For_Multiple_Column) , bg="#FDA8C0")
    Btn_Export_In_Excel.place(x=100 , y=170 , width=500)

    Btn_Export_In_PDF = Button(W_Export_As_File , text="Exportar como PDF" , font=("Times New Roman" , 13) , command= lambda: Create_Window_Export_PDF(W_Export_As_File , Results_From_Single_Column , Results_From_Multiple_Column) , bg="#FDA8C0")
    Btn_Export_In_PDF.place(x=100 , y=270 , width=500)

    W_Export_As_File.mainloop()

if(__name__ == "__main__"):
    Create_Window_Export_As_File()