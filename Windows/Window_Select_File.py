from tkinter import *
from tkinter import filedialog
from Windows_Errors import Frecuences_Error
import pandas as pd # type: ignore
def Create_Window_Sucess(Window_Root):

    Window_Sucess = Toplevel(Window_Root)
    Window_Sucess.geometry("400x170+550+220")
    Window_Sucess.title("Informacion")
    Icon = PhotoImage(file="Images/icon.png")
    Window_Sucess.iconphoto(False , Icon)
    def Volver():
        Window_Sucess.destroy()
        Window_Root.destroy()

    Text_Suecess = Label(Window_Sucess , text="Datos procesados con exito. \n \n Seleccione \"Volver\" para salir de la seleccion de archivos \n Seleccione \"Ok\" para cerrar solo esta ventana" , font=("Times New Roman" , 13))
    Text_Suecess.pack(side=TOP , fill=BOTH)

    Btn_Volver = Button(Window_Sucess , text="Volver" , font=("Times New Roman" , 13) , command= Volver , width=15)
    Btn_Volver.place(x=17 , y=120)

    Btn_Ok = Button(Window_Sucess , text="Ok" , font=("Times New Roman" , 13) , command= Window_Sucess.destroy , width=15)
    Btn_Ok.place(x=240 , y=120)

    Window_Sucess.resizable(False , False)
    Window_Sucess.mainloop()
def Process_File_Data(Window_Root , File_Path , Cell_Range , Preview , Data , Input_Data , Btn_Select_File):
    try:
        Excel = pd.read_excel(File_Path.get())
        First_Pair, Last_Pair = Cell_Range.get().split(':') # Si ingreso C10:D100 lo separa a "C10" y "D100"
        column_start = First_Pair[0] # Agarro C
        column_end = Last_Pair[0] # Agarro D

        # Convertir la letra de columna en índice (0 = A, 1 = B, 2 = C, etc.)
        start_col_index = ord(column_start.upper()) - ord('A')
        end_col_index = ord(column_end.upper()) - ord('A')

        start_row = int(First_Pair[1:])  # El inicio de la fila (por ejemplo, '10')
        end_row = int(Last_Pair[1:])  # El fin de la fila (por ejemplo, '100')

        # Filtrar la columna deseada
        data = Excel.iloc[start_row-2:end_row-1, start_col_index:end_col_index+1]
        data.dropna()

        Preview.delete("1.0" , END)
        Preview.insert(END , data)
        
        list_of_data = ""
        values = data.values
        if __name__ != "__main__":
            for a in values:
                list_of_data += " " + str(a[0])
            Data.set(list_of_data) # Aqui accedo solamente a los valores dentro de las celdas

    except FileNotFoundError as e:
        Win_err = Frecuences_Error("ERROR NOTFOUNDDILE" , "Archivo no encontrado")
        Win_err.Create_Window(Window_Root)
    except Frecuences_Error as e:
        e.Create_Window(Window_Root)
    else:
        Input_Data.config(state="disabled")
        Btn_Select_File.config(state="disabled")
        Create_Window_Sucess(Window_Root)

    return data

def Select_File(Path):
    Path_File = filedialog.askopenfilename(filetypes=[("Archivos Excel" , "*.xlsx")])
    if Path_File:
        Path.set(Path_File)

def Create_Window_Select_File(Father_Window , Data , Input_Data , Btn_Select_File_Father_Window):
    if __name__ == "__main__":
        Window_Root = Tk()
    else:
        Window_Root = Toplevel(Father_Window)

    Icon = PhotoImage(file="Images/icon.png")

    Window_Root.grab_set()
    Window_Root.geometry("700x500+400+220")
    Window_Root.title("Seleccionar Archivo")
    Window_Root.config(bg="#d1e7d2")
    Window_Root.iconphoto(False , Icon)
    
    Path = StringVar(Window_Root)
    Cell_Range = StringVar(Window_Root)

    Text_Input_Path_File = Label(Window_Root , text="Ingrese la ruta del archivo: " , bg="#d1e7d2" , font=("Times New Roman" , 12))
    Text_Input_Path_File.place(x=20 , y=20)
    Path_File = Entry(Window_Root , font=("Courier New" , 11) , textvariable=Path , width=52)
    Path_File.place(x=210 , y=22)
    Btn_Select_File = Button(Window_Root , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_File(Path) , width=10 , bg="#ffe3d4")
    Btn_Select_File.place(x=50 , y=50)

    Text_Input_Cells_Range = Label(Window_Root , text="Ingrese el rango de celdas: " , bg="#d1e7d2" , font=("Times New Roman" , 13))
    Text_Input_Cells_Range.place(x=20 , y=100)
    Cells_Range = Entry(Window_Root , font=("Courier New" , 13) , textvariable=Cell_Range , width=47)
    Cells_Range.place(x=210 , y=100)

    Preview_Data = Frame(Window_Root)
    Preview_Data.place(x=20 , y=150)

    Text_Preview_Data = Text(Preview_Data , wrap=WORD , height=16 , width=72) # Aqui no puedo usar StingVar(), solo usar los metodos get() y set()
    Text_Preview_Data.pack(side=LEFT, fill=BOTH, expand=True)

    Scroll = Scrollbar(Preview_Data , command=Text_Preview_Data.yview)
    Scroll.pack(side=RIGHT , fill=Y)

    Text_Preview_Data.config(yscrollcommand=Scroll.set)
    Text_Preview_Data.insert(END , "Una vez procesado tu archivo, tus datos se mostraran aqui...")
    Text_Preview_Data.config(font=("Times New Roman" , 13))

    Btn_Process_Data = Button(Window_Root , text="Procesar Archivo" , font=("Times New Roman" , 13) , width=25 , bg="#ffe3d4" , command=lambda: Process_File_Data(Window_Root , Path , Cell_Range , Text_Preview_Data , Data , Input_Data , Btn_Select_File_Father_Window))
    Btn_Process_Data.pack(side=BOTTOM)

    Window_Root.resizable(False,False)
    Window_Root.mainloop()

if __name__ == "__main__":
    Create_Window_Select_File(None , "" , "")