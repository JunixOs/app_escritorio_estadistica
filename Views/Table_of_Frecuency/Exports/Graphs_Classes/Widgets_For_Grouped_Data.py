import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , '..')))

from tkinter import *

from Views.Table_of_Frecuency.Exports.Graphs_Classes.Handler_Widgets_Export import Handler_Actions , Notebox_Widget_Container

class Section_Graphs_Titles:
    def __init__(self , W_Export_Graph):
        self.Title_For_Histogram_fi = StringVar(W_Export_Graph)
        self.Title_For_Histogram_hi = StringVar(W_Export_Graph)
        self.Title_For_Histogram_hi_percent = StringVar(W_Export_Graph)
        self.Title_For_Multiple_Histograme_Graphs = StringVar(W_Export_Graph)
        self.Checked_Title_For_Multiple_Histograme_Graphs = BooleanVar(W_Export_Graph)


        self.Title_For_Frecuences_Polygon_fi = StringVar(W_Export_Graph)
        self.Title_For_Frecuences_Polygon_hi = StringVar(W_Export_Graph)
        self.Title_For_Frecuences_Polygon_hi_percent = StringVar(W_Export_Graph)
        self.Title_For_Multiple_Frecuences_Polygon_Graphs = StringVar(W_Export_Graph)
        self.Checked_Title_For_Multiple_Frecuences_Polygon_Graphs = BooleanVar(W_Export_Graph)


        self.Title_For_Acumulate_Frecuences_Polygon_Fi = StringVar(W_Export_Graph)
        self.Title_For_Acumulate_Frecuences_Polygon_Hi = StringVar(W_Export_Graph)
        self.Title_For_Acumulate_Frecuences_Polygon_Hi_percent = StringVar(W_Export_Graph)
        self.Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs = StringVar(W_Export_Graph)
        self.Checked_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs = BooleanVar(W_Export_Graph)

        self.Title_For_Boxplot = StringVar(W_Export_Graph)

    def Create_Checkboxes_Widgets_For_Titles_For_Multiple_Graphs(self):
        self.Checkbox_Title_For_Multiple_Histograme_Graphs = Checkbutton(self.Frame_Section_Histograme , text="Colocar un mismo titulo a varios graficos" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Title_For_Multiple_Histograme_Graphs , command= lambda: self.Checkbox_Multiple_Titles_Behavior("Histogram"))
        self.Checkbox_Title_For_Multiple_Histograme_Graphs.config(state="disabled")

        self.Checkbox_Title_For_Multiple_Frecuences_Polygon_Graphs = Checkbutton(self.Frame_Section_Frecuences_Polygon , text="Colocar un mismo titulo a varios graficos" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Title_For_Multiple_Frecuences_Polygon_Graphs , command= lambda: self.Checkbox_Multiple_Titles_Behavior("Frecuences_Polygon"))
        self.Checkbox_Title_For_Multiple_Frecuences_Polygon_Graphs.config(state="disabled")

        self.Checkbox_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs = Checkbutton(self.Frame_Section_Acumulate_Frecuences_Polygon , text="Colocar un mismo titulo a varios graficos" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs , command= lambda: self.Checkbox_Multiple_Titles_Behavior("Acumulate_Frecuences_Polygon"))
        self.Checkbox_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs.config(state="disabled")

    def Create_Entry_Widgets_For_Graphs_Titles(self):
        self.Text_Entry_For_Histogram_fi = Label(self.Frame_Section_Histograme , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico fi" , justify=LEFT)
        self.Entry_For_Histogram_fi = Entry(self.Frame_Section_Histograme , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_fi , border=1)
        self.Entry_For_Histogram_fi.config(state="disabled")

        self.Text_Entry_For_Histogram_hi = Label(self.Frame_Section_Histograme , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi" , justify=LEFT)
        self.Entry_For_Histogram_hi = Entry(self.Frame_Section_Histograme , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi , border=1)
        self.Entry_For_Histogram_hi.config(state="disabled")

        self.Text_Entry_For_Histogram_hi_percent = Label(self.Frame_Section_Histograme , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi%" , justify=LEFT)
        self.Entry_For_Histogram_hi_percent = Entry(self.Frame_Section_Histograme , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi_percent , border=1)
        self.Entry_For_Histogram_hi_percent.config(state="disabled")

        self.Text_Entry_Title_For_Multiple_Histograme_Graphs = Label(self.Frame_Section_Histograme , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para varios graficos" , justify=LEFT)
        self.Entry_Title_For_Multiple_Histograme_Graphs = Entry(self.Frame_Section_Histograme , font=("Courier New" , 13) , textvariable=self.Title_For_Multiple_Histograme_Graphs , border=1)
        self.Entry_Title_For_Multiple_Histograme_Graphs.config(state="disabled")


        self.Text_Entry_For_Frecuences_Polygon_fi = Label(self.Frame_Section_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico fi" , justify=LEFT)
        self.Entry_For_Frecuences_Polygon_fi = Entry(self.Frame_Section_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_fi , border=1)
        self.Entry_For_Frecuences_Polygon_fi.config(state="disabled")

        self.Text_Entry_For_Frecuences_Polygon_hi = Label(self.Frame_Section_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi" , justify=LEFT)
        self.Entry_For_Frecuences_Polygon_hi = Entry(self.Frame_Section_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_hi , border=1)
        self.Entry_For_Frecuences_Polygon_hi.config(state="disabled")
        
        self.Text_Entry_For_Frecuences_Polygon_hi_percent = Label(self.Frame_Section_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi%" , justify=LEFT)
        self.Entry_For_Frecuences_Polygon_hi_percent = Entry(self.Frame_Section_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_hi_percent , border=1)
        self.Entry_For_Frecuences_Polygon_hi_percent.config(state="disabled")

        self.Text_Entry_Title_For_Multiple_Frecuences_Polygon_Graphs = Label(self.Frame_Section_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Mismo titulo para varios gráficos" , justify=LEFT)
        self.Entry_Title_For_Multiple_Frecuences_Polygon_Graphs = Entry(self.Frame_Section_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Multiple_Frecuences_Polygon_Graphs , border=1)
        self.Entry_Title_For_Multiple_Frecuences_Polygon_Graphs.config(state="disabled")
        

        self.Text_Entry_For_Acumulate_Frecuences_Polygon_Fi = Label(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico Fi" , justify=LEFT)
        self.Entry_For_Acumulate_Frecuences_Polygon_Fi = Entry(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Fi , border=1)
        self.Entry_For_Acumulate_Frecuences_Polygon_Fi.config(state="disabled")

        self.Text_Entry_For_Acumulate_Frecuences_Polygon_Hi = Label(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico Hi" , justify=LEFT)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi = Entry(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Hi , border=1)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi.config(state="disabled")
        
        self.Text_Entry_For_Acumulate_Frecuences_Polygon_Hi_percent = Label(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico Hi%" , justify=LEFT)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi_percent = Entry(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Hi_percent , border=1)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi_percent.config(state="disabled")

        self.Text_Entry_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs = Label(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico Hi%" , justify=LEFT)
        self.Entry_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs = Entry(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs , border=1)
        self.Entry_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs.config(state="disabled")


        self.Text_Entry_For_Boxplot = Label(self.Frame_Section_Boxplot , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico de cajas" , justify=LEFT)
        self.Entry_For_Boxplot = Entry(self.Frame_Section_Boxplot , font=("Courier New" , 13) , textvariable=self.Title_For_Boxplot , border=1)
        self.Entry_For_Boxplot.config(state="disabled")

    def Insert_Created_Widgets_Into_Dictionary(self):
        self.Dictionary_Entry_Titles_Widgets = {
            "Histogram": {
                "Histogram_fi": [self.Text_Entry_For_Histogram_fi , self.Entry_For_Histogram_fi],
                "Histogram_hi": [self.Text_Entry_For_Histogram_hi , self.Entry_For_Histogram_hi],
                "Histogram_hi_percent": [self.Text_Entry_For_Histogram_hi_percent , self.Entry_For_Histogram_hi_percent],
            },
            "Frecuences_Polygon": {
                "Frecuences_Polygon_fi": [self.Text_Entry_For_Frecuences_Polygon_fi , self.Entry_For_Frecuences_Polygon_fi],
                "Frecuences_Polygon_hi": [self.Text_Entry_For_Frecuences_Polygon_hi , self.Entry_For_Frecuences_Polygon_hi],
                "Frecuences_Polygon_hi_percent": [self.Text_Entry_For_Frecuences_Polygon_hi_percent , self.Entry_For_Frecuences_Polygon_hi_percent],
            },
            "Acumulate_Frecuences_Polygon": {  
                "Acumulate_Frecuences_Polygon_Fi": [self.Text_Entry_For_Acumulate_Frecuences_Polygon_Fi , self.Entry_For_Acumulate_Frecuences_Polygon_Fi],
                "Acumulate_Frecuences_Polygon_Hi": [self.Text_Entry_For_Acumulate_Frecuences_Polygon_Hi , self.Entry_For_Acumulate_Frecuences_Polygon_Hi],
                "Acumulate_Frecuences_Polygon_Hi_percent": [self.Text_Entry_For_Acumulate_Frecuences_Polygon_Hi_percent , self.Entry_For_Acumulate_Frecuences_Polygon_Hi_percent],
            },
            "Boxplot": {
                "Boxplot_All_Data": [self.Text_Entry_For_Boxplot , self.Entry_For_Boxplot],
            }
        }
        self.Dictionary_Entry_Titles_Values = {
            "Histogram": {
                "Histogram_fi": self.Title_For_Histogram_fi,
                "Histogram_hi": self.Title_For_Histogram_hi,
                "Histogram_hi_percent": self.Title_For_Histogram_hi_percent,
                "Title_For_Multiple_Histogram_Graphs": self.Title_For_Multiple_Histograme_Graphs,
            },
            "Frecuences_Polygon": {
                "Frecuences_Polygon_fi": self.Title_For_Frecuences_Polygon_fi,
                "Frecuences_Polygon_hi": self.Title_For_Frecuences_Polygon_hi,
                "Frecuences_Polygon_hi_percent": self.Title_For_Frecuences_Polygon_hi_percent,
                "Title_For_Multiple_Frecuences_Polygon_Graphs": self.Title_For_Multiple_Frecuences_Polygon_Graphs,
            },
            "Acumulate_Frecuences_Polygon": {  
                "Acumulate_Frecuences_Polygon_Fi": self.Title_For_Acumulate_Frecuences_Polygon_Fi,
                "Acumulate_Frecuences_Polygon_Hi": self.Title_For_Acumulate_Frecuences_Polygon_Hi,
                "Acumulate_Frecuences_Polygon_Hi_percent": self.Title_For_Acumulate_Frecuences_Polygon_Hi_percent,
                "Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs": self.Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs,
            },
            "Boxplot": {
                "Boxplot_All_Data": self.Title_For_Boxplot,
            }
        }

        self.Dictionary_Entry_Multiple_Titles_Widgets = {
            "Histogram": [self.Text_Entry_Title_For_Multiple_Histograme_Graphs , self.Entry_Title_For_Multiple_Histograme_Graphs],
            "Frecuences_Polygon": [self.Text_Entry_Title_For_Multiple_Frecuences_Polygon_Graphs , self.Entry_Title_For_Multiple_Frecuences_Polygon_Graphs],
            "Acumulate_Frecuences_Polygon": [self.Text_Entry_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs , self.Entry_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs],
        }
        self.Dictionary_Entry_Multiple_Titles_Values = {
            "Histogram": self.Title_For_Multiple_Histograme_Graphs,
            "Frecuences_Polygon": self.Title_For_Multiple_Frecuences_Polygon_Graphs,
            "Acumulate_Frecuences_Polygon": self.Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs,
        }

        self.Dictionary_Checkboxes_Multiple_Titles_Widgets = {
            "Histogram": self.Checkbox_Title_For_Multiple_Histograme_Graphs,
            "Frecuences_Polygon": self.Checkbox_Title_For_Multiple_Frecuences_Polygon_Graphs,
            "Acumulate_Frecuences_Polygon": self.Checkbox_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs,
        }
        self.Dictionary_Checkboxes_Multiple_Titles_Values = {
            "Histogram": self.Checked_Title_For_Multiple_Histograme_Graphs,
            "Frecuences_Polygon": self.Checked_Title_For_Multiple_Frecuences_Polygon_Graphs,
            "Acumulate_Frecuences_Polygon": self.Checked_Title_For_Multiple_Acumulate_Frecuences_Polygon_Graphs,
        }


class Section_Checkboxes_For_Export_Graphs:
    def __init__(self , W_Export_Graph):
        self.Checked_Histogram = BooleanVar(W_Export_Graph)
        self.Checked_Histogram_fi = BooleanVar(W_Export_Graph)
        self.Checked_Histogram_hi = BooleanVar(W_Export_Graph)
        self.Checked_Histogram_hi_percent = BooleanVar(W_Export_Graph)

        self.Checked_Frecuences_Polygon = BooleanVar(W_Export_Graph)
        self.Checked_Frecuences_Polygon_fi = BooleanVar(W_Export_Graph)
        self.Checked_Frecuences_Polygon_hi = BooleanVar(W_Export_Graph)
        self.Checked_Frecuences_Polygon_hi_percent = BooleanVar(W_Export_Graph)

        self.Checked_Acumulate_Frecuences_Polygon = BooleanVar(W_Export_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Fi = BooleanVar(W_Export_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Hi = BooleanVar(W_Export_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Hi_percent = BooleanVar(W_Export_Graph)

        self.Checked_Boxplot = BooleanVar(W_Export_Graph)

    def Create_Checkboxes_Widgets(self):
        self.Checkbox_Histogram = Checkbutton(self.Frame_Section_Histograme , text="Exportar todos los histogramas" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Histogram , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Histogram"))
        self.Checkbox_Histogram_fi = Checkbutton(self.Frame_Section_Histograme , text="Exportar grafico fi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Histogram_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Histogram" , "fi"))
        self.Checkbox_Histogram_hi = Checkbutton(self.Frame_Section_Histograme , text="Exportar grafico hi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Histogram_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Histogram" , "hi"))
        self.Checkbox_Histogram_hi_percent = Checkbutton(self.Frame_Section_Histograme , text="Exportar grafico  hi%" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Histogram_hi_percent , command=lambda: self.Check_And_Block_Single_Checkbox("Histogram" , "hi_percent"))

        self.Checkbox_Frecuences_Polygon = Checkbutton(self.Frame_Section_Frecuences_Polygon , text="Exportar todos los poligonos de frecuencias" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Frecuences_Polygon , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Frecuences_Polygon"))
        self.Checkbox_Frecuences_Polygon_fi = Checkbutton(self.Frame_Section_Frecuences_Polygon , text="Exportar grafico fi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Frecuences_Polygon_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "fi"))
        self.Checkbox_Frecuences_Polygon_hi = Checkbutton(self.Frame_Section_Frecuences_Polygon , text="Exportar grafico hi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Frecuences_Polygon_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "hi"))
        self.Checkbox_Frecuences_Polygon_hi_percent = Checkbutton(self.Frame_Section_Frecuences_Polygon , text="Exportar grafico hi%" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Frecuences_Polygon_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "hi_percent"))

        self.Checkbox_Acumulate_Frecuences_Polygon = Checkbutton(self.Frame_Section_Acumulate_Frecuences_Polygon , text="Exportar todos los poligonos de frecuencias acumuladas" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Acumulate_Frecuences_Polygon , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Acumulate_Frecuences_Polygon"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Fi = Checkbutton(self.Frame_Section_Acumulate_Frecuences_Polygon , text="Exportar grafico Fi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Acumulate_Frecuences_Polygon_Fi , command= lambda: self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Fi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi = Checkbutton(self.Frame_Section_Acumulate_Frecuences_Polygon , text="Exportar grafico Hi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Acumulate_Frecuences_Polygon_Hi , command= lambda: self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Hi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi_percent = Checkbutton(self.Frame_Section_Acumulate_Frecuences_Polygon , text="Exportar grafico Hi%" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Acumulate_Frecuences_Polygon_Hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Hi_percent"))

        self.Checkbox_Boxplot = Checkbutton(self.Frame_Section_Boxplot , text="Exportar el grafico de cajas" , font=("Times New Roman" , 13) , variable=self.Checked_Boxplot , bg="#F7F5DC" , command= lambda: self.Check_And_Block_Single_Checkbox("Boxplot" , "All_Data"))

    def Insert_Created_Widgets_Into_Dictionary(self):
        self.Dictionary_Main_Checkboxes_Values = {
            "Histogram": self.Checked_Histogram,
            "Frecuences_Polygon": self.Checked_Frecuences_Polygon,
            "Acumulate_Frecuences_Polygon": self.Checked_Acumulate_Frecuences_Polygon,
            "Boxplot": self.Checked_Boxplot,
        }
        self.Dictionary_Subcheckboxes_Values = {
            "Histogram": {
                "Histogram_fi": self.Checked_Histogram_fi,
                "Histogram_hi": self.Checked_Histogram_hi,
                "Histogram_hi_percent": self.Checked_Histogram_hi_percent,
            },
            "Frecuences_Polygon": {
                "Frecuences_Polygon_fi": self.Checked_Frecuences_Polygon_fi,
                "Frecuences_Polygon_hi": self.Checked_Frecuences_Polygon_hi,
                "Frecuences_Polygon_hi_percent": self.Checked_Frecuences_Polygon_hi_percent,
            },
            "Acumulate_Frecuences_Polygon": {
                "Acumulate_Frecuences_Polygon_Fi": self.Checked_Acumulate_Frecuences_Polygon_Fi,
                "Acumulate_Frecuences_Polygon_Hi": self.Checked_Acumulate_Frecuences_Polygon_Hi,
                "Acumulate_Frecuences_Polygon_Hi_percent": self.Checked_Acumulate_Frecuences_Polygon_Hi_percent,
            },
            "Boxplot": {
                "Boxplot_All_Data": self.Checked_Boxplot,
            }
        }

        self.Dictionary_Main_Checkboxes_Widgets = {
            "Histogram": self.Checkbox_Histogram,
            "Frecuences_Polygon": self.Checkbox_Frecuences_Polygon,
            "Acumulate_Frecuences_Polygon": self.Checkbox_Acumulate_Frecuences_Polygon,
            "Boxplot": self.Checkbox_Boxplot,
        }
        self.Dictionary_Subcheckboxes_Widgets = {
            "Histogram": {
                "Histogram_fi": self.Checkbox_Histogram_fi,
                "Histogram_hi": self.Checkbox_Histogram_hi,
                "Histogram_hi_percent": self.Checkbox_Histogram_hi_percent,
            },
            "Frecuences_Polygon": {
                "Frecuences_Polygon_fi": self.Checkbox_Frecuences_Polygon_fi,
                "Frecuences_Polygon_hi": self.Checkbox_Frecuences_Polygon_hi,
                "Frecuences_Polygon_hi_percent": self.Checkbox_Frecuences_Polygon_hi_percent,
            },
            "Acumulate_Frecuences_Polygon": {
                "Acumulate_Frecuences_Polygon_Fi": self.Checkbox_Acumulate_Frecuences_Polygon_Fi,
                "Acumulate_Frecuences_Polygon_Hi": self.Checkbox_Acumulate_Frecuences_Polygon_Hi,
                "Acumulate_Frecuences_Polygon_Hi_percent": self.Checkbox_Acumulate_Frecuences_Polygon_Hi_percent,
            },
            "Boxplot": {
                "Boxplot_All_Data": self.Checkbox_Boxplot,
            }
        }

class Section_Export_Graphs_For_Grouped_Data(Notebox_Widget_Container , Handler_Actions , Section_Graphs_Titles , Section_Checkboxes_For_Export_Graphs):
    def __init__(self, W_Export_Graph, Axis_x_Title):
        self.W_Export_Graph = W_Export_Graph
        self.Axis_x_Title = Axis_x_Title

        self.Notebook_For_Entry_Titles_Section = None
        Notebox_Widget_Container.__init__(self , W_Export_Graph , Axis_x_Title)
        Handler_Actions.__init__(self , W_Export_Graph)

        self.Frame_Section_Histograme = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Frecuences_Polygon = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Acumulate_Frecuences_Polygon = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Boxplot = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")

        self.Collection_Of_Frames = [self.Frame_Section_Histograme , self.Frame_Section_Frecuences_Polygon , self.Frame_Section_Acumulate_Frecuences_Polygon , self.Frame_Section_Boxplot]

        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Histograme , text="Seccion\nhistogramas")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Frecuences_Polygon , text="Seccion\npoligonos de frecuencias")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Acumulate_Frecuences_Polygon , text="Seccion\npoligonos de frecuencias acumuladas")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Boxplot , text="Seccion\ngrafico de cajas")


        Section_Checkboxes_For_Export_Graphs.__init__(self , W_Export_Graph)

        Section_Graphs_Titles.__init__(self , W_Export_Graph)

    def Create_Widgets(self):
        Section_Checkboxes_For_Export_Graphs.Create_Checkboxes_Widgets(self)
        Section_Checkboxes_For_Export_Graphs.Insert_Created_Widgets_Into_Dictionary(self)

        Section_Graphs_Titles.Create_Entry_Widgets_For_Graphs_Titles(self)
        Section_Graphs_Titles.Create_Checkboxes_Widgets_For_Titles_For_Multiple_Graphs(self)
        Section_Graphs_Titles.Insert_Created_Widgets_Into_Dictionary(self)
        
        Notebox_Widget_Container.Insert_Widgets_In_Notebook_Container(self)