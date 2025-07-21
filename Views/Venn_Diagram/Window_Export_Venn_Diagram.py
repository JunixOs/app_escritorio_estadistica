import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..')))

from Tools import Get_Resource_Path , Center_Window
from Calcs.Venn.Export_Venn_Diagram import Export_Venn_Diagram_As_Image

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def Select_Path(W_Export_Venn_Diagram , File_Path , Btn_Examine):
    Btn_Examine.config(state="disabled")
    Path = filedialog.askdirectory(title="Seleccione una carpeta")
    if(os.path.isdir(Path) and Path):
        if(File_Path):
            File_Path.set("")
        File_Path.set(Path)
    
    Btn_Examine.config(state="normal")
    W_Export_Venn_Diagram.lift()

def Create_Window_Export_Diagram(W_Create_Venn_Diagram , Figure_Venn_Graph):
    def Back():
        for widgets in W_Export_Venn_Diagram.winfo_children():
            widgets.destroy()

        W_Export_Venn_Diagram.quit()
        W_Export_Venn_Diagram.destroy()

        W_Create_Venn_Diagram.lift()

    if(__name__ == "__main__"):
        W_Export_Venn_Diagram = Tk()
    else:
        W_Export_Venn_Diagram = Toplevel(W_Create_Venn_Diagram)
        W_Export_Venn_Diagram.grab_set()
        W_Export_Venn_Diagram.lift()
        W_Export_Venn_Diagram.protocol("WM_DELETE_WINDOW" , Back)

    Center_Window(W_Export_Venn_Diagram , 800 , 300)
    
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
    W_Export_Venn_Diagram.iconphoto(False , Icon)
    W_Export_Venn_Diagram.title("Exportar Diagrama de Venn")
    W_Export_Venn_Diagram.config(bg="#FFD9FA")

    File_Name = StringVar(W_Export_Venn_Diagram)
    File_Name.set("")
    File_Path = StringVar(W_Export_Venn_Diagram)
    Graph_Title = StringVar(W_Export_Venn_Diagram)
    Graph_Title.set("")
    Formats = [".jpg" , ".png" , ".svg"]
    Resolutions = [72 , 96 , 150 , 300 , 600 , 1200 , 2000]

    Text_Input_File_Name = Label(W_Export_Venn_Diagram , text="Nombre de la imagen (opcional): " , font=("Times New Roman" , 13) , justify=LEFT , bg="#FFD9FA")
    Text_Input_File_Name.place(x=20 , y=20)
    Input_File_Name = Entry(W_Export_Venn_Diagram , font=("Courier New" , 13) , textvariable=File_Name)
    Input_File_Name.place(x=270 , y=20 , width=440)
    Input_File_Name.focus()
    Input_Format = ttk.Combobox(W_Export_Venn_Diagram , values=Formats , font=("Times New Roman" , 13) , width=4 , state="readonly")
    Input_Format.place(x=720 , y=20)
    Input_Format.set(Formats[0])

    Text_Input_File_Path = Label(W_Export_Venn_Diagram , text="Ruta de exportacion: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#FFD9FA")
    Text_Input_File_Path.place(x=20 , y=60)
    Input_File_Path = Entry(W_Export_Venn_Diagram , font=("Courier New" , 13) , textvariable=File_Path , state="readonly")
    Input_File_Path.place(x=270 , y=60 , width=500)

    Btn_Examine = Button(W_Export_Venn_Diagram , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_Path(W_Export_Venn_Diagram , File_Path , Btn_Examine) , bg="#F9FFD1")
    Btn_Examine.place(x=40 , y=90)

    Text_Input_Resolution = Label(W_Export_Venn_Diagram , text="Resolucion de la imagen (DPI):\n96 resolucion estandar \n>300 alta resolucion" , font=("Times New Roman" , 13) , justify=LEFT , bg="#FFD9FA")
    Text_Input_Resolution.place(x=20 , y=130)
    Input_Resolution = ttk.Combobox(W_Export_Venn_Diagram , values=Resolutions , font=("Times New Roman" , 13) , width=5 , state="readonly")
    Input_Resolution.place(x=270 , y=135)
    Input_Resolution.set(Resolutions[0])

    Text_Input_Venn_Graph_Title = Label(W_Export_Venn_Diagram , text="Titulo para el diagrama de Venn:" , font=("Times New Roman" , 13) , justify=LEFT , bg="#FFD9FA")
    Text_Input_Venn_Graph_Title.place(x=20 , y=210)
    Input_Venn_Graph_Title = Entry(W_Export_Venn_Diagram , font=("Courier New" , 13) , textvariable=Graph_Title)
    Input_Venn_Graph_Title.place(x=270 , y=210 , width=500)

    Btn_Export = Button(W_Export_Venn_Diagram , text="Exportar" , font=("Times New Roman" , 13) , bg="#FFD9FA" , command= lambda: Export_Venn_Diagram_As_Image(W_Export_Venn_Diagram , Figure_Venn_Graph , File_Name.get() , File_Path.get() , Input_Format.get() , int(Input_Resolution.get()) , Graph_Title.get()))
    Btn_Export.place(x=320 , y=260 , width=150)

    W_Export_Venn_Diagram.resizable(False , False)
    W_Export_Venn_Diagram.mainloop()

if(__name__ == "__main__"):
    Create_Window_Export_Diagram(None , None)