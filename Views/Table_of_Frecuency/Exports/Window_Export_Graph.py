import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..')))

from Tools import Get_Resource_Path , Delete_Actual_Window
from Calcs.Table_of_Frecuency.Exports.Export_Graph import Manage_Export_Of_Graphs
from Views.Table_of_Frecuency.Exports.Graphs_Classes.Widgets_For_Grouped_Data import Checkboxes_Export_Graphs_For_Grouped_Data
from Views.Table_of_Frecuency.Exports.Graphs_Classes.Widgets_For_Not_Grouped_Data import Checkboxes_Export_Graphs_For_Not_Grouped_Data
from Views.Table_of_Frecuency.Exports.Graphs_Classes.Widgets_For_Cualitative_Data import Checkboxes_Export_Graphs_For_Cualitative_Data

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
        self.Input_Name_Bar_Graph = Entry(self.W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Name_Bar_Graph)
        self.Input_Name_Bar_Graph.config(state="disabled")

        self.Input_Name_Píe_Graph = Entry(self.W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Name_Pie_Graph)
        self.Input_Name_Píe_Graph.config(state="disabled")

        if(self.There_Are_Boxplot):
            self.Input_Name_Boxplot_Graph = Entry(self.W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Name_Boxplot_Graph)
            self.Input_Name_Boxplot_Graph.config(state="disabled")
        else:
            self.Input_Name_Boxplot_Graph = None
    
    def Display_Widgets(self):
        self.Input_Name_Bar_Graph.place(x=250 , y=520 , width=630)

        self.Input_Name_Píe_Graph.place(x=250 , y=570 , width=630)

        if(self.Input_Name_Boxplot_Graph):
            self.Input_Name_Boxplot_Graph.place(x=250 , y=620 , width=630)

    def Hidden_Widgets(self):
        self.Input_Name_Bar_Graph.place_forget()

        self.Input_Name_Píe_Graph.place_forget()

        if(self.Input_Name_Boxplot_Graph):
            self.Input_Name_Boxplot_Graph.place_forget()
class Widget_Combobox_For_DPI_And_Format:
    def __init__(self , Root_Window):
        self.W_Export_Graph = Root_Window
        self.Resolutions = [72 , 96 , 150 , 300 , 600 , 1200 , 2000]
        self.Formats = [".jpg" , ".png" , ".svg"]
        self.Sizes_In_pX = ["980x700" , "1280x720" , "1920x1080" , "2560x1440"] # (Width x Height)

    def Create_Widgets(self):
        self.Input_dpi = ttk.Combobox(self.W_Export_Graph , values=self.Resolutions , font=("Times New Roman", 13), state="readonly" , width=5)
        self.Input_dpi.set(self.Resolutions[0])

        self.Input_Sizes = ttk.Combobox(self.W_Export_Graph , values=self.Sizes_In_pX , font=("Times New Roman" , 13) , state="readonly" , width=10)
        self.Input_Sizes.set(self.Sizes_In_pX[0])

        self.Input_Format = ttk.Combobox(self.W_Export_Graph , values=self.Formats , font=("Times New Roman", 13), state="readonly" , width=4)
        self.Input_Format.set(self.Formats[0])

    def Display_Widgets(self):
        self.Input_dpi.place(x=250 , y=150)
        # self.Input_Sizes.place(x=670 , y=150) # Importacion con tamaño personalizado, caracteristica sin terminar
        self.Input_Format.place(x=820 , y=39)

    def Hidden_Widgets(self):
        self.Input_dpi.place_forget()
        self.Input_Format.place_forget()

class Manage_Widgets_Export_Graphs_For_Grouped_Data(
    Checkboxes_Export_Graphs_For_Grouped_Data , Widget_Combobox_For_DPI_And_Format
):
    def __init__(self , W_Export_Graph , Axis_x_Title):
        Checkboxes_Export_Graphs_For_Grouped_Data.__init__(self , W_Export_Graph , Axis_x_Title)
        Widget_Combobox_For_DPI_And_Format.__init__(self , W_Export_Graph)

    def Create_All_Widgets(self):
        Checkboxes_Export_Graphs_For_Grouped_Data.Create_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Create_Widgets(self)

    def Display_All_Widgets(self):
        Checkboxes_Export_Graphs_For_Grouped_Data.Display_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Display_Widgets(self)

    def Hidden_All_Widgets(self):
        Checkboxes_Export_Graphs_For_Grouped_Data.Hidden_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Hidden_Widgets(self)

class Manage_Widgets_Export_Graphs_For_Not_Grouped_Data(
    Checkboxes_Export_Graphs_For_Not_Grouped_Data , Widget_Combobox_For_DPI_And_Format
):
    def __init__(self , W_Export_Graph , Axis_x_Title):
        Checkboxes_Export_Graphs_For_Not_Grouped_Data.__init__(self , W_Export_Graph , Axis_x_Title)
        Widget_Combobox_For_DPI_And_Format.__init__(self , W_Export_Graph)

    def Create_All_Widgets(self):
        Checkboxes_Export_Graphs_For_Not_Grouped_Data.Create_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Create_Widgets(self)

    def Display_All_Widgets(self):
        Checkboxes_Export_Graphs_For_Not_Grouped_Data.Display_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Display_Widgets(self)

    def Hidden_All_Widgets(self):
        Checkboxes_Export_Graphs_For_Not_Grouped_Data.Hidden_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Hidden_Widgets(self)

class Manage_Widgets_Export_Graphs_For_Cualitative_Data(
    Checkboxes_Export_Graphs_For_Cualitative_Data , Widget_Combobox_For_DPI_And_Format
):
    def __init__(self , W_Export_Graph , Axis_x_Title):
        Checkboxes_Export_Graphs_For_Cualitative_Data.__init__(self , W_Export_Graph , Axis_x_Title)
        Widget_Combobox_For_DPI_And_Format.__init__(self , W_Export_Graph)

    def Create_All_Widgets(self):
        Checkboxes_Export_Graphs_For_Cualitative_Data.Create_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Create_Widgets(self)

    def Display_All_Widgets(self):
        Checkboxes_Export_Graphs_For_Cualitative_Data.Display_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Display_Widgets(self)

    def Hidden_All_Widgets(self):
        Checkboxes_Export_Graphs_For_Cualitative_Data.Hidden_Widgets(self)
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

def Create_Window_Export_Graphs(W_Show_Graph , Dictionary_Of_Generated_Figures , Type_Of_Calc , Axis_x_Title , Type_Of_Variable):
    
    def Hidden_All_Widgets():
        for Classes in Collection_Classes_For_Create_Widgets.values():
            Classes.Hidden_All_Widgets()

    def Display_Widgets_Acoording_Column_Name(Event = None):
        Selection = Select_Column.get()
        Hidden_All_Widgets()
        Collection_Classes_For_Create_Widgets[f"{Selection}"].Display_All_Widgets()

    W_Export_Graph = Toplevel(W_Show_Graph)
    W_Show_Graph.state(newstate="withdraw")

    W_Export_Graph.title("Exportar Graficos")
    W_Export_Graph.geometry("900x700+310+90")
    W_Export_Graph.lift()
    W_Export_Graph.grab_set()
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
    W_Export_Graph.iconphoto(False , Icon)
    W_Export_Graph.protocol("WM_DELETE_WINDOW" , lambda: Delete_Actual_Window(W_Show_Graph , W_Export_Graph , True))

    File_Name = StringVar(W_Export_Graph)
    Path = StringVar(W_Export_Graph)
    Path.set("")
    Columns_Name = []
    Collection_Classes_For_Create_Widgets = {}
    Collection_Subcheckboxes_With_Selected_Graphs = {}
    Collection_Entry_Titles_For_Graphs = {}

    Collection_Formats = {}
    Collection_DPIs = {}
    Collection_Axis_x_Titles_For_Graphs = {}

    Section_1 = Label(W_Export_Graph , bg="#E4DBD5" , width=128 , height=14 , borderwidth=2 , relief="solid")
    Section_1.place(x=0 , y=0)

    Label_Input_File_Name = Label(W_Export_Graph , text="Nombre de la imagen (opcional): " , font=("Times New Roman" , 13) , bg="#E4DBD5")
    Label_Input_File_Name.place(x=20 , y=40)
    Input_File_Name = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=File_Name)
    Input_File_Name.place(x=250 , y=40 , width=560)
    Input_File_Name.focus()

    Label_Input_Páth = Label(W_Export_Graph , text="Ruta de exportacion: " , font=("Times New Roman" , 13) , bg="#E4DBD5")
    Label_Input_Páth.place(x=20 , y=80)
    Input_Path = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Path , state="readonly")
    Input_Path.place(x=250 , y=80 , width=630)
    Btn_Examine = Button(W_Export_Graph , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_Path(W_Export_Graph , Path , Btn_Examine) , bg="#F3F3E9")
    Btn_Examine.place(x=40 , y=110)

    Label_Input_dpi = Label(W_Export_Graph ,text="Resolucion de la imagen (DPI): \n96 resolucion estandar \n>300 alta resolucion" , font=("Times New Roman" , 13) , justify=LEFT , bg="#E4DBD5")
    Label_Input_dpi.place(x=20 , y=150)

    Label_Input_Size = Label(W_Export_Graph , text="Tamaño de la imagen (px):\nOriginal 980x700" , font=("Times New Roman" , 13) , justify=LEFT , bg="#E4DBD5")
    # Label_Input_Size.place(x=470 , y=150)

    Section_2 = Label(W_Export_Graph , bg="#E7E4C1" , width=129 , height=32 , borderwidth=2 , relief="solid")
    Section_2.place(x=0 , y=214)

    Label_Download_Graphs = Label(W_Export_Graph , bg="#E7E4C1" , font=("Times New Roman" , 13) , text="Seleccione los graficos a exportar" , justify=CENTER)
    Label_Download_Graphs.place(x=200 , y=230 , width=500)

    Class_For_Create_Widgets = None
    if(Type_Of_Calc == "Single_Column"):
        match(Type_Of_Variable):
            case "Cuantitative_Grouped":
                Class_For_Create_Widgets = Manage_Widgets_Export_Graphs_For_Grouped_Data(W_Export_Graph , Axis_x_Title if Axis_x_Title else "Intervalos de Clase")
            case "Cuantitative_Not_Grouped":
                Class_For_Create_Widgets = Manage_Widgets_Export_Graphs_For_Not_Grouped_Data(W_Export_Graph , Axis_x_Title if Axis_x_Title else "Variables Observadas (xi)")
            case "Cualitative":
                Class_For_Create_Widgets = Manage_Widgets_Export_Graphs_For_Cualitative_Data(W_Export_Graph , Axis_x_Title if Axis_x_Title else "Variables Observadas (ai)")
        
        Class_For_Create_Widgets.Create_All_Widgets()
        Class_For_Create_Widgets.Display_All_Widgets()

        Collection_Subcheckboxes_With_Selected_Graphs = Class_For_Create_Widgets.Dictionary_Subcheckboxes_Values
        Collection_Entry_Titles_For_Graphs = Class_For_Create_Widgets.Dictionary_Entry_Titles_Values

        Collection_Formats = Class_For_Create_Widgets.Input_Format
        Collection_DPIs = Class_For_Create_Widgets.Input_dpi
        Collection_Axis_x_Titles_For_Graphs = Class_For_Create_Widgets.Title_For_Axis_x

        #Btn_Download_Graphs.config(command= lambda: Export_Graph_As_Image(W_Show_Graph , W_Export_Graph , Graphs , File_Name.get() , Path.get() , Widgets_W_Export_Graph , Widgets_W_Export_Graph.Dictionary_Checkboxes , Variable_Name))

    elif(Type_Of_Calc == "Multiple_Columns"):
        Label_Select_Column = Label(W_Export_Graph , text="Seleccione la columna: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E4DBD5") 
        Label_Select_Column.place(x=20 , y=10)

        Select_Column = ttk.Combobox(W_Export_Graph , values=Columns_Name , font=("Courier New" , 13) , width=25 , state="readonly")
        
        for type_of_variable , axis_x_title in zip(Type_Of_Variable.values() , Axis_x_Title):
            Columns_Name.append(axis_x_title)
            match(type_of_variable):
                case "Cuantitative_Grouped":
                    Class_For_Create_Widgets = Manage_Widgets_Export_Graphs_For_Grouped_Data(W_Export_Graph , axis_x_title)
                case "Cuantitative_Not_Grouped":
                    Class_For_Create_Widgets = Manage_Widgets_Export_Graphs_For_Not_Grouped_Data(W_Export_Graph , axis_x_title)
                case "Cualitative":
                    Class_For_Create_Widgets = Manage_Widgets_Export_Graphs_For_Cualitative_Data(W_Export_Graph , axis_x_title)

            Class_For_Create_Widgets.Create_All_Widgets()

            Collection_Classes_For_Create_Widgets[f"{axis_x_title}"] = Class_For_Create_Widgets

            Collection_Subcheckboxes_With_Selected_Graphs[f"{axis_x_title}"] = Class_For_Create_Widgets.Dictionary_Subcheckboxes_Values
            Collection_Entry_Titles_For_Graphs[f"{axis_x_title}"] = Class_For_Create_Widgets.Dictionary_Entry_Titles_Values

            Collection_Formats[f"{axis_x_title }"] = Class_For_Create_Widgets.Input_Format
            Collection_DPIs[f"{axis_x_title}"] = Class_For_Create_Widgets.Input_dpi
            Collection_Axis_x_Titles_For_Graphs[f"{axis_x_title}"] = Class_For_Create_Widgets.Title_For_Axis_x

        Select_Column["values"] = Columns_Name
        Select_Column.set(Columns_Name[0])
        Select_Column.bind('<<ComboboxSelected>>' , Display_Widgets_Acoording_Column_Name)
        Select_Column.place(x=200 , y=10)

        Display_Widgets_Acoording_Column_Name()

        #Btn_Export_Graph.config(command= lambda: Export_Graph_As_Image(W_Show_Graph , W_Export_Graph , Graphs , File_Name.get() , Path.get() , Collection_Classes_For_Create_Widgets , Collection_Checkboxes))
    else:
        raise Exception("Hubo un error al identificar el tipo de calculo.")

    Btn_Download_Graphs = Button(W_Export_Graph , text="Descargar graficos" , font=("Times New Roman" , 13) , width=30 , bg="#E4DBD5" , command= lambda: Manage_Export_Of_Graphs(W_Show_Graph , W_Export_Graph , File_Name.get() , Input_Path.get() , Collection_Formats , Collection_DPIs , Collection_Axis_x_Titles_For_Graphs , Dictionary_Of_Generated_Figures , Collection_Subcheckboxes_With_Selected_Graphs , Collection_Entry_Titles_For_Graphs , False if Type_Of_Calc == "Multiple_Columns" else True))
    Btn_Download_Graphs.place(x=300 , y=660)

    W_Export_Graph.resizable(False , False)
    W_Export_Graph.mainloop()

if __name__ == "__main__":
    Create_Window_Export_Graphs(None , None)