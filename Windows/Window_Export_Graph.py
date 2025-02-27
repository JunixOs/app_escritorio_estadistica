import sys
import os
import copy
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Calcs.Exports.Export_Graph import Export_Graph_As_Image

from tkinter import *
from tkinter import filedialog
from tkinter import ttk

class Widget_Input_Name_For_Graphs:
    def __init__(self , Root_Window , There_Are_Boxplot):
        self.W_Export_Graph = Root_Window
        self.There_Are_Boxplot = There_Are_Boxplot

        self.Name_Bar_Graph = StringVar(self.W_Export_Graph)
        self.Name_Bar_Graph.set("")
        self.Name_Pie_Graph = StringVar(self.W_Export_Graph)
        self.Name_Bar_Graph.set("")
        self.Name_Boxplot_Graph = StringVar(self.W_Export_Graph)
        self.Name_Boxplot_Graph.set("")

    def Create_Widgets(self):
        self.Input_Name_Bar_Graph = Entry(self.W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Name_Bar_Graph , width=58)
        self.Input_Name_Bar_Graph.config(state="disabled")

        self.Input_Name_Píe_Graph = Entry(self.W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Name_Pie_Graph , width=58)
        self.Input_Name_Píe_Graph.config(state="disabled")

        if(self.There_Are_Boxplot):
            self.Input_Name_Boxplot_Graph = Entry(self.W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Name_Boxplot_Graph , width=58)
            self.Input_Name_Boxplot_Graph.config(state="disabled")
        else:
            self.Input_Name_Boxplot_Graph = None
    
    def Display_Widgets(self):
        self.Input_Name_Bar_Graph.place(x=200 , y=520)

        self.Input_Name_Píe_Graph.place(x=200 , y=570)

        if(self.Input_Name_Boxplot_Graph):
            self.Input_Name_Boxplot_Graph.place(x=200 , y=620)

    def Hidden_Widgets(self):
        self.Input_Name_Bar_Graph.place_forget()

        self.Input_Name_Píe_Graph.place_forget()

        if(self.Input_Name_Boxplot_Graph):
            self.Input_Name_Boxplot_Graph.place_forget()
class Checkboxes_For_Export_Graphs(Widget_Input_Name_For_Graphs):
    def __init__(self , Root_Window , There_Are_Boxplot):
        Widget_Input_Name_For_Graphs.__init__(self , Root_Window , There_Are_Boxplot)
        self.W_Export_Graph = Root_Window
        self.There_Are_Boxplot = There_Are_Boxplot

        self.Checked_Export_All = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_All_Bars = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Bar_fi = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Bar_hi = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Bar_hi_percent = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Pie = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Boxplot = BooleanVar(self.W_Export_Graph)

    def Check_Export_All(self):
        if(self.Dictionary_Checkboxes):
            match(self.Dictionary_Checkboxes["All"][1].get()):
                case True:
                    for key , value in self.Dictionary_Checkboxes.items():
                        if(key != "All"):
                            value[0].config(state="disabled")
                            value[1].set(True)

                    self.Input_Name_Bar_Graph.config(state="normal")
                    self.Input_Name_Píe_Graph.config(state="normal")
                    if(self.Input_Name_Boxplot_Graph):
                        self.Input_Name_Boxplot_Graph.config(state="normal")
                case False:
                    for key , value in self.Dictionary_Checkboxes.items():
                        if(key != "All"):
                            value[0].config(state="normal")
                            value[1].set(False)
                        
                    self.Input_Name_Bar_Graph.config(state="disabled")
                    self.Name_Bar_Graph.set("")
                    self.Input_Name_Píe_Graph.config(state="disabled")
                    self.Name_Pie_Graph.set("")
                    if(self.Input_Name_Boxplot_Graph):
                        self.Input_Name_Boxplot_Graph.config(state="disabled")
                        self.Name_Boxplot_Graph.set("")

    def Checked_All_For_Inverse(self):
        All_Graphs = [checked[1].get() for i , checked in enumerate(self.Dictionary_Checkboxes.values()) if (i > 1)]
        if(all(All_Graphs)):
            self.Dictionary_Checkboxes["All"][0].config(state="disabled")
            self.Dictionary_Checkboxes["All"][1].set(True)
        else:
            self.Dictionary_Checkboxes["All"][0].config(state="normal")
            self.Dictionary_Checkboxes["All"][1].set(False)

    def Check_Export_All_Bars(self):
        if(self.Dictionary_Checkboxes):
            match(self.Dictionary_Checkboxes["All_Bars"][1].get()):
                case True:
                    for i , value in enumerate(self.Dictionary_Checkboxes.values()):
                        if(i > 1 and i < 5):
                            value[0].config(state="disabled")
                            value[1].set(True)

                    self.Input_Name_Bar_Graph.config(state="normal")
                case False:
                    for i , value in enumerate(self.Dictionary_Checkboxes.values()):
                        if(i > 1 and i < 5):
                            value[0].config(state="normal")
                            value[1].set(False)
                    self.Input_Name_Bar_Graph.config(state="disabled")
                    self.Name_Bar_Graph.set("")

            self.Checked_All_For_Inverse()

    def Check_Bars(self):
        Only_Bars = [checked[1].get() for i , checked in enumerate(self.Dictionary_Checkboxes.values()) if (i > 1 and i < 5)]
        if(all(Only_Bars)):
            self.Dictionary_Checkboxes["All_Bars"][0].config(state="disabled")
            self.Dictionary_Checkboxes["All_Bars"][1].set(True)
        else:
            self.Dictionary_Checkboxes["All_Bars"][0].config(state="normal")
            self.Dictionary_Checkboxes["All_Bars"][1].set(False)

        if(any(Only_Bars)):
            self.Input_Name_Bar_Graph.config(state="normal")
        else:
            self.Input_Name_Bar_Graph.config(state="disabled")
            self.Name_Bar_Graph.set("")

        self.Checked_All_For_Inverse()

    def Check_Pie(self):
        if(self.Dictionary_Checkboxes["Pie"][1].get()):
            self.Input_Name_Píe_Graph.config(state="normal")
        else:
            self.Input_Name_Píe_Graph.config(state="disabled")
            self.Name_Pie_Graph.set("")
        self.Checked_All_For_Inverse()

    def Check_Boxplot(self):
        if(self.Dictionary_Checkboxes["Boxplot"][1].get()):
            self.Input_Name_Boxplot_Graph.config(state="normal")
        else:
            self.Input_Name_Boxplot_Graph.config(state="disabled")
            self.Name_Boxplot_Graph.set("")
        self.Checked_All_For_Inverse()

    def Create_Widgets(self):
        Widget_Input_Name_For_Graphs.Create_Widgets(self)

        self.Checkbox_Export_All = Checkbutton(self.W_Export_Graph , text="Exportar todo" , font=("Times New Roman" , 13) , variable=self.Checked_Export_All , command=self.Check_Export_All , bg="#E7E4C1")
        self.Checkbox_Export_All_Bar_Graphs = Checkbutton(self.W_Export_Graph , text="Exportar todos los graficos de barras" , font=("Times New Roman" , 13) , variable=self.Checked_Export_All_Bars , command=self.Check_Export_All_Bars , bg="#E7E4C1")

        self.Checkbox_Export_bar_fi = Checkbutton(self.W_Export_Graph , text="Exportar grafico de barras de fi" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Bar_fi , bg="#E7E4C1" , command=self.Check_Bars)
        self.Checkbox_Export_bar_hi = Checkbutton(self.W_Export_Graph , text="Exportar grafico de barras de hi" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Bar_hi , bg="#E7E4C1" , command=self.Check_Bars)
        self.Checkbox_Export_bar_hi_percent = Checkbutton(self.W_Export_Graph , text="Exportar grafico de barras de hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Bar_hi_percent , bg="#E7E4C1" , command=self.Check_Bars)

        self.Checkbox_Export_pie = Checkbutton(self.W_Export_Graph , text="Exportar grafico de pastel" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Pie , bg="#E7E4C1" , command=self.Check_Pie)

        if(self.There_Are_Boxplot):
            self.Checked_Export_Boxplot.set(False)
            self.Checkbox_Export_Boxplot = Checkbutton(self.W_Export_Graph , text="Exportar grafico de cajas" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Boxplot , command=self.Check_Boxplot , bg="#E7E4C1")
        else:
            self.Checkbox_Export_Boxplot = None
            self.Checked_Export_Boxplot.set(True)

        self.Dictionary_Checkboxes = dict([
            ("All" , [self.Checkbox_Export_All , self.Checked_Export_All]),
            ("All_Bars" , [self.Checkbox_Export_All_Bar_Graphs , self.Checked_Export_All_Bars]),
            ("Bars_fi" , [self.Checkbox_Export_bar_fi , self.Checked_Export_Bar_fi]),
            ("Bar_hi" , [self.Checkbox_Export_bar_hi , self.Checked_Export_Bar_hi]),
            ("Bar_hi_percent" , [self.Checkbox_Export_bar_hi_percent , self.Checked_Export_Bar_hi_percent]),
            ("Pie" , [self.Checkbox_Export_pie , self.Checked_Export_Pie]),
            ("Boxplot" , [self.Checkbox_Export_Boxplot , self.Checked_Export_Boxplot])
        ])

    def Display_Widgets(self):
        self.Checkbox_Export_All.place(x=310 , y=260)
        self.Checkbox_Export_All_Bar_Graphs.place(x=350 , y=290)

        self.Checkbox_Export_bar_fi.place(x=380 , y=320)
        self.Checkbox_Export_bar_hi.place(x=380 , y=350)
        self.Checkbox_Export_bar_hi_percent.place(x=380 , y=380)

        self.Checkbox_Export_pie.place(x=350 , y=430)

        if(self.Checkbox_Export_Boxplot):
            self.Checkbox_Export_Boxplot.place(x=350 , y=460)

        Widget_Input_Name_For_Graphs.Display_Widgets(self)

    def Hidden_Widgets(self):
        self.Checkbox_Export_All.place_forget()
        self.Checkbox_Export_All_Bar_Graphs.place_forget()

        self.Checkbox_Export_bar_fi.place_forget()
        self.Checkbox_Export_bar_hi.place_forget()
        self.Checkbox_Export_bar_hi_percent.place_forget()

        self.Checkbox_Export_pie.place_forget()

        if(self.Checkbox_Export_Boxplot):
            self.Checkbox_Export_Boxplot.place_forget()

        Widget_Input_Name_For_Graphs.Hidden_Widgets(self)
class Widget_Combobox_For_DPI_And_Format():
    def __init__(self , Root_Window):
        self.W_Export_Graph = Root_Window
        self.Resolutions = [72 , 96 , 150 , 300 , 600 , 1200]
        self.Formats = [".jpg" , ".png" , ".svg"]
    
    def Create_Widgets(self):
        self.Input_dpi = ttk.Combobox(self.W_Export_Graph , values=self.Resolutions , font=("Times New Roman", 13), state="readonly")
        self.Input_dpi.set(self.Resolutions[0])

        self.Input_Format = ttk.Combobox(self.W_Export_Graph , values=self.Formats , font=("Times New Roman", 13), state="readonly" , width=4)
        self.Input_Format.set(self.Formats[0])

    def Display_Widgets(self):
        self.Input_dpi.place(x=250 , y=147)
        self.Input_Format.place(x=800 , y=37)

    def Hidden_Widgets(self):
        self.Input_dpi.place_forget()
        self.Input_Format.place_forget()

class Widgets_For_W_Export_Graphs(Checkboxes_For_Export_Graphs , Widget_Combobox_For_DPI_And_Format):
    """ Nombres de Clases con CamelCase y de metodos con snake_case """
    def __init__(self , Root_Window , There_Are_Boxplot):
        Checkboxes_For_Export_Graphs.__init__(self , Root_Window , There_Are_Boxplot)
        Widget_Combobox_For_DPI_And_Format.__init__(self , Root_Window)

    def Create_All_Widgets(self):
        Checkboxes_For_Export_Graphs.Create_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Create_Widgets(self)

    def Display_All_Widgets(self):
        Checkboxes_For_Export_Graphs.Display_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Display_Widgets(self)

    def Hidden_All_Widgets(self):
        Checkboxes_For_Export_Graphs.Hidden_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Hidden_Widgets(self)

def Select_Path(W_Export_Graph , Path , Btn_Examine):
    Btn_Examine.config(state="disabled")
    File_Path = filedialog.askdirectory(title="Seleccione una carpeta")
    if File_Path:
        if(Path):
            Path.set("")
            Path.set(File_Path)
        else:
            Path.set(File_Path)

    W_Export_Graph.lift()
    Btn_Examine.config(state="normal")

def Create_Windows_Export_Graphs(W_Show_Graph , Graphs , Results_From_Single_Column , Results_From_Multiple_Columns):
    
    def Back_To_W_Show_Graph():
        Collection_Widgets_W_Export_Graph.clear()

        for widgets in W_Export_Graph.winfo_children():
            widgets.destroy()

        W_Export_Graph.grab_release()
        W_Export_Graph.quit()
        W_Export_Graph.destroy()

        W_Show_Graph.state(newstate="normal")
        W_Show_Graph.lift()
        W_Show_Graph.lift()
        W_Show_Graph.grab_set()

    def Hidden_All_Widgets():
        for Wid in Collection_Widgets_W_Export_Graph.values():
            Wid.Hidden_All_Widgets()

    def Display_Widgets_Acoording_Column_Name(Event = None):
        Selection = Select_Column.get()
        Hidden_All_Widgets()
        Collection_Widgets_W_Export_Graph[f"{Selection}"].Display_All_Widgets()

    W_Export_Graph = Toplevel(W_Show_Graph)
    W_Show_Graph.state(newstate="withdraw")

    W_Export_Graph.title("Exportar Graficos")
    W_Export_Graph.geometry("900x700+310+90")
    W_Export_Graph.lift()
    W_Export_Graph.grab_set()
    Icon = PhotoImage(file="Images/icon.png")
    W_Export_Graph.iconphoto(False , Icon)
    W_Export_Graph.protocol("WM_DELETE_WINDOW" , Back_To_W_Show_Graph)

    File_Name = StringVar(W_Export_Graph)
    Path = StringVar(W_Export_Graph)
    Path.set("")
    Columns_Name = []
    Collection_Widgets_W_Export_Graph = {}
    
    Section_1 = Label(W_Export_Graph , bg="#E4DBD5" , width=128 , height=14 , borderwidth=2 , relief="solid")
    Section_1.place(x=0 , y=0)

    Label_Input_File_Name = Label(W_Export_Graph , text="Nombre de la Imagen: " , font=("Times New Roman" , 13) , bg="#E4DBD5")
    Label_Input_File_Name.place(x=20 , y=40)
    Input_File_Name = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=File_Name , width=58)
    Input_File_Name.place(x=200 , y=40)
    Input_File_Name.focus()

    Label_Input_Páth = Label(W_Export_Graph , text="Ruta de destino: " , font=("Times New Roman" , 13) , bg="#E4DBD5")
    Label_Input_Páth.place(x=20 , y=80)
    Input_Path = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Path , width=58 , state="readonly")
    Input_Path.place(x=200 , y=80)
    Btn_Examine = Button(W_Export_Graph , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_Path(W_Export_Graph , Path , Btn_Examine) , bg="#F3F3E9")
    Btn_Examine.place(x=40 , y=110)

    Label_Input_dpi = Label(W_Export_Graph ,text="Resolucion de la imagen (DPI): \n96 resolucion estandar \n>300 alta resolucion" , font=("Times New Roman" , 13) , justify=LEFT , bg="#E4DBD5")
    Label_Input_dpi.place(x=20 , y=150)

    Section_2 = Label(W_Export_Graph , bg="#E7E4C1" , width=129 , height=32 , borderwidth=2 , relief="solid")
    Section_2.place(x=0 , y=214)

    Texto_Exportar_Graficos = Label(W_Export_Graph , text="Seleccione los graficos que exportara" , font=("Times New Roman" , 13) , bg="#E7E4C1")
    Texto_Exportar_Graficos.place(x=310 , y=239)

    Text_Change_Name_Bar_Graph = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de barras: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Bar_Graph.place(x=20 , y=510)

    Text_Change_Name_Pie_Graph = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de pastel: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Pie_Graph.place(x=20 , y=560)

    Text_Change_Name_Boxplot = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de cajas: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Boxplot.place(x=20 , y=610)

    Btn_Export_Graph = Button(W_Export_Graph , text="Descargar Graficos" , font=("Times New Roman" , 13) , width=30 , bg="#E4DBD5")
    Btn_Export_Graph.place(x=300 , y=660)
    if(Results_From_Single_Column):
        There_Are_Boxplot = "boxplot_graph" in Graphs
        Widgets_W_Export_Graph = Widgets_For_W_Export_Graphs(W_Export_Graph , There_Are_Boxplot)

        Widgets_W_Export_Graph.Create_All_Widgets()
        Widgets_W_Export_Graph.Display_All_Widgets()

        Btn_Export_Graph.config(command= lambda: Export_Graph_As_Image(W_Show_Graph , W_Export_Graph , Graphs , File_Name.get() , Path.get() , Widgets_W_Export_Graph))

    elif(Results_From_Multiple_Columns):
        Label_Select_Column = Label(W_Export_Graph , text="Seleccione la columna: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1") 
        Label_Select_Column.place(x=20 , y=10)
        Widgets_W_Export_Graph = None
        There_Are_Boxplot = [True if "boxplot_graph" in value else False for value in Graphs.values()]

        Select_Column = ttk.Combobox(W_Export_Graph , values=Columns_Name , font=("Courier New" , 13) , width=25 , state="readonly")
        
        for i , key in enumerate(Results_From_Multiple_Columns.keys()):
            Columns_Name.append(key)
            Widgets_W_Export_Graph = Widgets_For_W_Export_Graphs(W_Export_Graph , There_Are_Boxplot[i])
            Widgets_W_Export_Graph.Create_All_Widgets()

            Collection_Widgets_W_Export_Graph[f"{key}"] = Widgets_W_Export_Graph

        Select_Column["values"] = Columns_Name
        Select_Column.set(Columns_Name[0])
        Select_Column.bind('<<ComboboxSelected>>' , Display_Widgets_Acoording_Column_Name)
        Select_Column.place(x=200 , y=10)

        Display_Widgets_Acoording_Column_Name()
    else:
        raise Exception("No se pudieron encontrar los resultados.")


    W_Export_Graph.resizable(False , False)
    W_Export_Graph.mainloop()

def W_For_Single_Column_Data(Father_Window , Graphs):

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

            Export_Boxplot.config(state="disabled")
            Checked_Export_Boxplot.set(True)

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

            Export_Boxplot.config(state="normal")
            Checked_Export_Boxplot.set(False)

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

        if(Checked_Export_All_Bars.get() and Checked_Export_Pie.get() and Checked_Export_Boxplot.get()):
            Checked_Export_All.set(True)
            Export_All.config(state="disabled")
        else:
            Checked_Export_All.set(False)
            Export_All.config(state="normal")

    def Checked_Bars():
        if(Checked_Export_Bar_fi.get() and Checked_Export_Bar_hi.get() and Checked_Export_Bar_hi_percent.get()):
            Checked_Export_All_Bars.set(True)
            Export_All_Bar_Graphs.config(state="disabled")
        else:
            Checked_Export_All_Bars.set(False)
            Export_All_Bar_Graphs.config(state="normal")

        if(Checked_Export_All_Bars.get() and Checked_Export_Pie.get() and Checked_Export_Boxplot.get()):
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

    def Checked_Pie():
        if(Checked_Export_Pie.get()):
            Input_Name_Píe_Graph.config(state="normal")
        else:
            Input_Name_Píe_Graph.config(state="disabled")
            Name_Pie_Graph.set("")
        if(Checked_Export_All_Bars.get() and Checked_Export_Pie.get() and Checked_Export_Boxplot.get()):
            Checked_Export_All.set(True)
            Export_All.config(state="disabled")
        else:
            Checked_Export_All.set(False)
            Export_All.config(state="normal")
    def Checked_Boxplot():
        if(Checked_Export_Boxplot.get()):
            Input_Name_Boxplot_Graph.config(state="normal")
        else:
            Input_Name_Boxplot_Graph.config(state="disabled")
            Name_Boxplot_Graph.set("")
        if(Checked_Export_All_Bars.get() and Checked_Export_Pie.get() and Checked_Export_Boxplot.get()):
            Checked_Export_All.set(True)
            Export_All.config(state="disabled")
        else:
            Checked_Export_All.set(False)
            Export_All.config(state="normal")

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
    Name_Boxplot_Graph = StringVar(W_Export_Graph)
    Name_Boxplot_Graph.set("")
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
    Checked_Export_Boxplot = BooleanVar(W_Export_Graph)

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
    Input_Path = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Path , width=58 , state="readonly")
    Input_Path.place(x=200 , y=60)
    Btn_Examine = Button(W_Export_Graph , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_Path(W_Export_Graph , Path , Btn_Examine) , bg="#F3F3E9")
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
    Export_All.place(x=310 , y=240)

    Export_All_Bar_Graphs = Checkbutton(W_Export_Graph , text="Exportar todos los graficos de barras" , font=("Times New Roman" , 13) , variable=Checked_Export_All_Bars , command=Check_Export_All_Bars , bg="#E7E4C1")
    Export_All_Bar_Graphs.place(x=350 , y=270)
    Export_bar_fi = Checkbutton(W_Export_Graph , text="Exportar grafico de barras de fi" , font=("Times New Roman" , 13) , variable=Checked_Export_Bar_fi , bg="#E7E4C1" , command=Checked_Bars)
    Export_bar_fi.place(x=380 , y=300)
    Export_bar_hi = Checkbutton(W_Export_Graph , text="Exportar grafico de barras de hi" , font=("Times New Roman" , 13) , variable=Checked_Export_Bar_hi , bg="#E7E4C1" , command=Checked_Bars)
    Export_bar_hi.place(x=380 , y=330)
    Export_bar_hi_percent = Checkbutton(W_Export_Graph , text="Exportar grafico de barras de hi%" , font=("Times New Roman" , 13) , variable=Checked_Export_Bar_hi_percent , bg="#E7E4C1" , command=Checked_Bars)
    Export_bar_hi_percent.place(x=380 , y=360)

    Export_pie = Checkbutton(W_Export_Graph , text="Exportar grafico de pastel" , font=("Times New Roman" , 13) , variable=Checked_Export_Pie , bg="#E7E4C1" , command=Checked_Pie)
    Export_pie.place(x=350 , y=410)

    if("boxplot_graph" in Graphs):
        Checked_Export_Boxplot.set(False)
        Export_Boxplot = Checkbutton(W_Export_Graph , text="Exportar grafico de cajas" , font=("Times New Roman" , 13) , variable=Checked_Export_Boxplot , command=Checked_Boxplot , bg="#E7E4C1")
        Export_Boxplot.place(x=350 , y=440)
    else:
        Checked_Export_Boxplot.set(True)

    Text_Change_Name_Bar_Graph = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de barras: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Bar_Graph.place(x=20 , y=490)
    Input_Name_Bar_Graph = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Name_Bar_Graph , width=58)
    Input_Name_Bar_Graph.place(x=200 , y=500)
    Input_Name_Bar_Graph.config(state="disabled")

    Text_Change_Name_Pie_Graph = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de pastel: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Pie_Graph.place(x=20 , y=540)
    Input_Name_Píe_Graph = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Name_Pie_Graph , width=58)
    Input_Name_Píe_Graph.place(x=200 , y=550)
    Input_Name_Píe_Graph.config(state="disabled")

    Text_Change_Name_Boxplot = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de cajas: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Boxplot.place(x=20 , y=590)
    Input_Name_Boxplot_Graph = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Name_Boxplot_Graph , width=58)
    Input_Name_Boxplot_Graph.place(x=200 , y=600)
    Input_Name_Boxplot_Graph.config(state="disabled")

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
            Name_Boxplot_Graph.get(),
            Export_All = Checked_Export_All.get(),
            Export_All_Bars = Checked_Export_All_Bars.get(),
            Export_Bar_fi = Checked_Export_Bar_fi.get(),
            Export_Bar_hi = Checked_Export_Bar_hi.get(),
            Export_Bar_hi_percent = Checked_Export_Bar_hi_percent.get(),
            Export_Pie = Checked_Export_Pie.get(),
            Export_Boxplot = Checked_Export_Boxplot.get()))
    Btn_Export_Graph.place(x=300 , y=610)

    W_Export_Graph.resizable(False , False)
    W_Export_Graph.mainloop()

def W_For_Mutiple_Column_Data(Father_Window , Graphs):
    pass
if __name__ == "__main__":
    Create_Windows_Export_Graphs(None , None)