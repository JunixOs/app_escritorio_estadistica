import sys
import os
import copy
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Calcs.Exports.Export_Graph import Export_Graph_As_Image

from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def Select_Path(Root_Window , Path):
    File_Path = filedialog.askdirectory(title="Seleccione una carpeta")
    if File_Path:
        if(Path):
            Path.set("")
            Path.set(File_Path)
        else:
            Path.set(File_Path)
    Root_Window.lift()

def Create_Window_Export_Graph(Father_Window , Graphs):

    if __name__ == "__main__":
        W_Export_Graph = Tk()
    else:
        W_Export_Graph = Toplevel(Father_Window)

    def Check_Export_All():
        if(Checked_Export_All.get()):
            Export_All_Bar_Graphs.config(state="disabled")
            Checked_Export_All_Bars.set(True)

            Export_bar_fi.config(state="disabled")
            Checked_Export_Bar_fi.set(True)

            Export_bar_hi.config(state="disabled")
            Checked_Export_Bar_hi.set(True)

            Export_bar_hi_percent.config(state="disabled")
            Checked_Export_Bar_hi_percent.set(True)

            Export_pie.config(state="disabled")
            Checked_Export_Pie.set(True)

            Input_Name_Bar_Graph.config(state="normal")
            Input_Name_Píe_Graph.config(state="normal")
        else:
            Export_All_Bar_Graphs.config(state="normal")
            Checked_Export_All_Bars.set(False)

            Export_bar_fi.config(state="normal")
            Checked_Export_Bar_fi.set(False)

            Export_bar_hi.config(state="normal")
            Checked_Export_Bar_hi.set(False)

            Export_bar_hi_percent.config(state="normal")
            Checked_Export_Bar_hi_percent.set(False)

            Export_pie.config(state="normal")
            Checked_Export_Pie.set(False)

            Input_Name_Bar_Graph.config(state="disabled")
            Name_Bar_Graph.set("")
            Input_Name_Píe_Graph.config(state="disabled")
            Name_Pie_Graph.set("")
    
    def Check_Export_All_Bars():
        if(Checked_Export_All_Bars.get()):
            Export_bar_fi.config(state="disabled")
            Checked_Export_Bar_fi.set(True)

            Export_bar_hi.config(state="disabled")
            Checked_Export_Bar_hi.set(True)

            Export_bar_hi_percent.config(state="disabled")
            Checked_Export_Bar_hi_percent.set(True)

            Input_Name_Bar_Graph.config(state="normal")
        else:
            Export_All_Bar_Graphs.config(state="normal")
            Checked_Export_All_Bars.set(False)

            Export_bar_fi.config(state="normal")
            Checked_Export_Bar_fi.set(False)

            Export_bar_hi.config(state="normal")
            Checked_Export_Bar_hi.set(False)

            Export_bar_hi_percent.config(state="normal")
            Checked_Export_Bar_hi_percent.set(False)

            Input_Name_Bar_Graph.config(state="disabled")
            Name_Bar_Graph.set("")

    def Checked_Bar_And_Pie():
        if(Checked_Export_Bar_fi.get() and Checked_Export_Bar_hi.get() and Checked_Export_Bar_hi_percent.get()):
            Checked_Export_All_Bars.set(True)
            Export_All_Bar_Graphs.config(state="disabled")
        else:
            Checked_Export_All_Bars.set(False)
            Export_All_Bar_Graphs.config(state="normal")

        if(Checked_Export_All_Bars.get() and Checked_Export_Pie.get()):
            Checked_Export_All.set(True)
            Export_All.config(state="disabled")
        else:
            Checked_Export_All.set(False)
            Export_All.config(state="normal")

        if(Checked_Export_Bar_fi.get() or Checked_Export_Bar_hi.get() or Checked_Export_Bar_hi_percent.get()):
            Input_Name_Bar_Graph.config(state="normal")
        else:
            Input_Name_Bar_Graph.config(state="disabled")
            Name_Bar_Graph.set("")
        if(Checked_Export_Pie.get()):
            Input_Name_Píe_Graph.config(state="normal")
        else:
            Input_Name_Píe_Graph.config(state="disabled")
            Name_Pie_Graph.set("")

    def Back():
        W_Export_Graph.destroy()
        Father_Window.state(newstate="normal")
        Father_Window.lift()
        Father_Window.lift()
        Father_Window.grab_set()
    if __name__ != "__main__":
        Father_Window.state(newstate="withdraw")

    W_Export_Graph.title("Exportar Graficos")
    W_Export_Graph.geometry("900x650+310+110")
    W_Export_Graph.lift()
    W_Export_Graph.grab_set()
    Icon = PhotoImage(file="Images/icon.png")
    W_Export_Graph.iconphoto(False , Icon)
    W_Export_Graph.protocol("WM_DELETE_WINDOW" , Back)

    Name_Bar_Graph = StringVar(W_Export_Graph)
    Name_Bar_Graph.set("")
    Name_Pie_Graph = StringVar(W_Export_Graph)
    Name_Bar_Graph.set("")
    File_Name = StringVar(W_Export_Graph)
    Path = StringVar(W_Export_Graph)
    Path.set("")

    Formats = [".jpg" , ".png" , ".svg"]
    Resolutions = [72 , 96 , 150 , 300 , 600 , 1200]

    Checked_Export_All = BooleanVar(W_Export_Graph)
    Checked_Export_All_Bars = BooleanVar(W_Export_Graph)
    Checked_Export_Bar_fi = BooleanVar(W_Export_Graph)
    Checked_Export_Bar_hi = BooleanVar(W_Export_Graph)
    Checked_Export_Bar_hi_percent = BooleanVar(W_Export_Graph)
    Checked_Export_Pie = BooleanVar(W_Export_Graph)

    Section_1 = Label(W_Export_Graph , bg="#E4DBD5" , width=128 , height=14 , borderwidth=2 , relief="solid")
    Section_1.place(x=0 , y=0)
    Label_Input_File_Name = Label(W_Export_Graph , text="Nombre de la Imagen: " , font=("Times New Roman" , 13) , bg="#E4DBD5")
    Label_Input_File_Name.place(x=20 , y=20)
    Input_File_Name = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=File_Name , width=58)
    Input_File_Name.place(x=200 , y=20)
    Input_File_Name.focus()

    Input_Format = ttk.Combobox(W_Export_Graph , values=Formats , font=("Times New Roman", 13), state="readonly" , width=4)
    Input_Format.place(x=800 , y=17)
    Input_Format.set(Formats[0])

    Label_Input_Páth = Label(W_Export_Graph , text="Ruta de destino: " , font=("Times New Roman" , 13) , bg="#E4DBD5")
    Label_Input_Páth.place(x=20 , y=60)
    Input_Path = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Path , width=58)
    Input_Path.place(x=200 , y=60)
    Btn_Examine = Button(W_Export_Graph , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_Path(W_Export_Graph , Path) , bg="#F3F3E9")
    Btn_Examine.place(x=40 , y=90)

    Label_Input_dpi = Label(W_Export_Graph ,text="Resolucion de la imagen (DPI): \n96 resolucion estandar \n>300 alta resolucion" , font=("Times New Roman" , 13) , justify=LEFT , bg="#E4DBD5")
    Label_Input_dpi.place(x=20 , y=130)
    Input_dpi = ttk.Combobox(W_Export_Graph , values=Resolutions , font=("Times New Roman", 13), state="readonly")
    Input_dpi.place(x=250 , y=127)
    Input_dpi.set(Resolutions[0])

    Section_2 = Label(W_Export_Graph , bg="#E7E4C1" , width=129 , height=29 , borderwidth=2 , relief="solid")
    Section_2.place(x=0 , y=214)

    Texto_Exportar_Graficos = Label(W_Export_Graph , text="Seleccione los graficos que exportara" , font=("Times New Roman" , 13) , bg="#E7E4C1")
    Texto_Exportar_Graficos.place(x=310 , y=219)
    Export_All = Checkbutton(W_Export_Graph , text="Exportar todo" , font=("Times New Roman" , 13) , variable=Checked_Export_All , command=Check_Export_All , bg="#E7E4C1")
    Export_All.place(x=310 , y=250)

    Export_All_Bar_Graphs = Checkbutton(W_Export_Graph , text="Exportar todos los graficos de barras" , font=("Times New Roman" , 13) , variable=Checked_Export_All_Bars , command=Check_Export_All_Bars , bg="#E7E4C1")
    Export_All_Bar_Graphs.place(x=350 , y=290)
    Export_bar_fi = Checkbutton(W_Export_Graph , text="Exportar grafico de barras de fi" , font=("Times New Roman" , 13) , variable=Checked_Export_Bar_fi , bg="#E7E4C1" , command=Checked_Bar_And_Pie)
    Export_bar_fi.place(x=380 , y=330)
    Export_bar_hi = Checkbutton(W_Export_Graph , text="Exportar grafico de barras de hi" , font=("Times New Roman" , 13) , variable=Checked_Export_Bar_hi , bg="#E7E4C1" , command=Checked_Bar_And_Pie)
    Export_bar_hi.place(x=380 , y=365)
    Export_bar_hi_percent = Checkbutton(W_Export_Graph , text="Exportar grafico de barras de hi%" , font=("Times New Roman" , 13) , variable=Checked_Export_Bar_hi_percent , bg="#E7E4C1" , command=Checked_Bar_And_Pie)
    Export_bar_hi_percent.place(x=380 , y=400)

    Export_pie = Checkbutton(W_Export_Graph , text="Exportar grafico de pastel" , font=("Times New Roman" , 13) , variable=Checked_Export_Pie , bg="#E7E4C1" , command=Checked_Bar_And_Pie)
    Export_pie.place(x=350 , y=450)

    Text_Change_Name_Bar_Graph = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de barras: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Bar_Graph.place(x=20 , y=490)
    Input_Name_Bar_Graph = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Name_Bar_Graph , width=58)
    Input_Name_Bar_Graph.place(x=200 , y=500)
    Input_Name_Bar_Graph.config(state="disabled")

    Text_Change_Name_Pie_Graph = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de pastel: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Pie_Graph.place(x=20 , y=560)
    Input_Name_Píe_Graph = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Name_Pie_Graph , width=58)
    Input_Name_Píe_Graph.place(x=200 , y=570)
    Input_Name_Píe_Graph.config(state="disabled")

    Btn_Export_Graph = Button(
        W_Export_Graph , 
        text="Exportar Graficos" , 
        font=("Times New Roman" , 13) , 
        width=30 , 
        bg="#E4DBD5" , 
        command= lambda: Export_Graph_As_Image(
            Father_Window ,
            W_Export_Graph ,
            Graphs , 
            File_Name.get() , 
            Path.get() , 
            Input_dpi.get() , 
            Input_Format.get() , 
            Name_Bar_Graph.get() , 
            Name_Pie_Graph.get() ,       
            Export_All = Checked_Export_All.get(),
            Export_All_Bars = Checked_Export_All_Bars.get(),
            Export_Bar_fi = Checked_Export_Bar_fi.get(),
            Export_Bar_hi = Checked_Export_Bar_hi.get(),
            Export_Bar_hi_percent = Checked_Export_Bar_hi_percent.get(),
            Export_Pie = Checked_Export_Pie.get(),
            ))
    Btn_Export_Graph.place(x=300 , y=610)

    W_Export_Graph.resizable(False , False)
    W_Export_Graph.mainloop()

if __name__ == "__main__":
    Create_Window_Export_Graph(None , None)