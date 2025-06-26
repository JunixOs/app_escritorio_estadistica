import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , '..')))

from tkinter import *

from Views.Table_of_Frecuency.Exports.Graphs_Classes.Handler_Widgets_Export import Handler_Actions , Container_For_Entry_Title_Widgets

class Entry_Widget_For_Export_Graphs_For_Grouped_Data(Container_For_Entry_Title_Widgets):
    def __init__(self , W_Export_Graph , Axis_x_Title):
        self.Title_For_Histogram_fi = StringVar(W_Export_Graph)
        self.Title_For_Histogram_hi = StringVar(W_Export_Graph)
        self.Title_For_Histogram_hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Frecuences_Polygon_fi = StringVar(W_Export_Graph)
        self.Title_For_Frecuences_Polygon_hi = StringVar(W_Export_Graph)
        self.Title_For_Frecuences_Polygon_hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Acumulate_Frecuences_Polygon_Fi = StringVar(W_Export_Graph)
        self.Title_For_Acumulate_Frecuences_Polygon_Hi = StringVar(W_Export_Graph)
        self.Title_For_Acumulate_Frecuences_Polygon_Hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Boxplot = StringVar(W_Export_Graph)

        Container_For_Entry_Title_Widgets.__init__(self , W_Export_Graph , Axis_x_Title)

        self.Frame_Section_Histograme = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Frecuences_Polygon = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Acumulate_Frecuences_Polygon = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Boxplot = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")

        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Histograme , text="Titulos para\nhistogramas")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Frecuences_Polygon , text="Titulos para\npoligonos de frecuencias")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Acumulate_Frecuences_Polygon , text="Titulos para\npoligonos de frecuencias acumuladas")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Boxplot , text="Titulo para\ngrafico de cajas")

    def Create_Entry_Widgets(self):
        self.Text_Entry_For_Histogram_fi = Label(self.Frame_Section_Histograme , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para fi" , justify=LEFT)
        self.Entry_For_Histogram_fi = Entry(self.Frame_Section_Histograme , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_fi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Histogram_fi.config(state="disabled")

        self.Text_Entry_For_Histogram_hi = Label(self.Frame_Section_Histograme , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi" , justify=LEFT)
        self.Entry_For_Histogram_hi = Entry(self.Frame_Section_Histograme , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Histogram_hi.config(state="disabled")

        self.Text_Entry_For_Histogram_hi_percent = Label(self.Frame_Section_Histograme , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi%" , justify=LEFT)
        self.Entry_For_Histogram_hi_percent = Entry(self.Frame_Section_Histograme , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi_percent , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Histogram_hi_percent.config(state="disabled")


        self.Text_Entry_For_Frecuences_Polygon_fi = Label(self.Frame_Section_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para fi" , justify=LEFT)
        self.Entry_For_Frecuences_Polygon_fi = Entry(self.Frame_Section_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_fi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Frecuences_Polygon_fi.config(state="disabled")

        self.Text_Entry_For_Frecuences_Polygon_hi = Label(self.Frame_Section_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi" , justify=LEFT)
        self.Entry_For_Frecuences_Polygon_hi = Entry(self.Frame_Section_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_hi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Frecuences_Polygon_hi.config(state="disabled")
        
        self.Text_Entry_For_Frecuences_Polygon_hi_percent = Label(self.Frame_Section_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi%" , justify=LEFT)
        self.Entry_For_Frecuences_Polygon_hi_percent = Entry(self.Frame_Section_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_hi_percent , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Frecuences_Polygon_hi_percent.config(state="disabled")


        self.Text_Entry_For_Acumulate_Frecuences_Polygon_Fi = Label(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para Fi" , justify=LEFT)
        self.Entry_For_Acumulate_Frecuences_Polygon_Fi = Entry(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Fi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Acumulate_Frecuences_Polygon_Fi.config(state="disabled")

        self.Text_Entry_For_Acumulate_Frecuences_Polygon_Hi = Label(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para Hi" , justify=LEFT)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi = Entry(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Hi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi.config(state="disabled")
        
        self.Text_Entry_For_Acumulate_Frecuences_Polygon_Hi_percent = Label(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para Hi%" , justify=LEFT)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi_percent = Entry(self.Frame_Section_Acumulate_Frecuences_Polygon , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Hi_percent , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi_percent.config(state="disabled")


        self.Text_Entry_For_Boxplot = Label(self.Frame_Section_Boxplot , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo grafico de cajas" , justify=LEFT)
        self.Entry_For_Boxplot = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Boxplot , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Boxplot.config(state="disabled")

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
            },
            "Frecuences_Polygon": {
                "Frecuences_Polygon_fi": self.Title_For_Frecuences_Polygon_fi,
                "Frecuences_Polygon_hi": self.Title_For_Frecuences_Polygon_hi,
                "Frecuences_Polygon_hi_percent": self.Title_For_Frecuences_Polygon_hi_percent,
            },
            "Acumulate_Frecuences_Polygon": {  
                "Acumulate_Frecuences_Polygon_Fi": self.Title_For_Acumulate_Frecuences_Polygon_Fi,
                "Acumulate_Frecuences_Polygon_Hi": self.Title_For_Acumulate_Frecuences_Polygon_Hi,
                "Acumulate_Frecuences_Polygon_Hi_percent": self.Title_For_Acumulate_Frecuences_Polygon_Hi_percent,
            },
            "Boxplot": {
                "Boxplot_All_Data": self.Title_For_Boxplot,
            }
        }
        
        self.Insert_Widgets_In_Container()


class Checkboxes_Export_Graphs_For_Grouped_Data(Handler_Actions , Entry_Widget_For_Export_Graphs_For_Grouped_Data):
    def __init__(self , W_Export_Graph , Axis_x_Title):
        self.W_Export_Graph = W_Export_Graph
        self.Axis_x_Title = Axis_x_Title

        self.Checked_Histogram = BooleanVar(self.W_Export_Graph)
        self.Checked_Histogram_fi = BooleanVar(self.W_Export_Graph)
        self.Checked_Histogram_hi = BooleanVar(self.W_Export_Graph)
        self.Checked_Histogram_hi_percent = BooleanVar(self.W_Export_Graph)

        self.Checked_Frecuences_Polygon = BooleanVar(self.W_Export_Graph)
        self.Checked_Frecuences_Polygon_fi = BooleanVar(self.W_Export_Graph)
        self.Checked_Frecuences_Polygon_hi = BooleanVar(self.W_Export_Graph)
        self.Checked_Frecuences_Polygon_hi_percent = BooleanVar(self.W_Export_Graph)

        self.Checked_Acumulate_Frecuences_Polygon = BooleanVar(self.W_Export_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Fi = BooleanVar(self.W_Export_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Hi = BooleanVar(self.W_Export_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Hi_percent = BooleanVar(self.W_Export_Graph)

        self.Checked_Boxplot = BooleanVar(self.W_Export_Graph)

        Handler_Actions.__init__(self , W_Export_Graph)
        Entry_Widget_For_Export_Graphs_For_Grouped_Data.__init__(self , W_Export_Graph , Axis_x_Title)

    def Create_Widgets(self):
        self.Checkbox_Histogram = Checkbutton(self.W_Export_Graph , text="Histograma" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Histogram , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Histogram"))
        self.Checkbox_Histogram_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Histogram_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Histogram" , "fi"))
        self.Checkbox_Histogram_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Histogram_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Histogram" , "hi"))
        self.Checkbox_Histogram_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Histogram_hi_percent , command=lambda: self.Check_And_Block_Single_Checkbox("Histogram" , "hi_percent"))

        self.Checkbox_Frecuences_Polygon = Checkbutton(self.W_Export_Graph , text="poligono de frecuencias" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Frecuences_Polygon , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Frecuences_Polygon"))
        self.Checkbox_Frecuences_Polygon_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Frecuences_Polygon_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "fi"))
        self.Checkbox_Frecuences_Polygon_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Frecuences_Polygon_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "hi"))
        self.Checkbox_Frecuences_Polygon_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Frecuences_Polygon_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "hi_percent"))

        self.Checkbox_Acumulate_Frecuences_Polygon = Checkbutton(self.W_Export_Graph , text="Poligono de frecuencias acumuladas" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Acumulate_Frecuences_Polygon , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Acumulate_Frecuences_Polygon"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Fi = Checkbutton(self.W_Export_Graph , text="Para Fi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Acumulate_Frecuences_Polygon_Fi , command= lambda: self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Fi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi = Checkbutton(self.W_Export_Graph , text="Para Hi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Acumulate_Frecuences_Polygon_Hi , command= lambda: self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Hi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi_percent = Checkbutton(self.W_Export_Graph , text="Para Hi%" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Acumulate_Frecuences_Polygon_Hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Hi_percent"))

        self.Checkbox_Boxplot = Checkbutton(self.W_Export_Graph , text="Grafico de cajas" , font=("Times New Roman" , 13) , variable=self.Checked_Boxplot , bg="#E7E4C1" , command= lambda: self.Check_And_Block_Single_Checkbox("Boxplot" , "All_Data"))

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
    
        self.Create_Entry_Widgets()