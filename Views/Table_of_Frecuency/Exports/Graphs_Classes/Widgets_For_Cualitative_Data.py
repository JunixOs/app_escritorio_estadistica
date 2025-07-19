import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , '..')))

from tkinter import *

from Views.Table_of_Frecuency.Exports.Graphs_Classes.Handler_Widgets_Export import Handler_Actions , Notebox_Widget_Container

class Section_Graphs_Titles:
    def __init__(self , W_Export_Graph):
        self.Title_For_Simple_Bars_fi = StringVar(W_Export_Graph)
        self.Title_For_Simple_Bars_hi = StringVar(W_Export_Graph)
        self.Title_For_Simple_Bars_hi_percent = StringVar(W_Export_Graph)
        self.Title_For_Multiple_Simple_Bars_Graphs = StringVar(W_Export_Graph)
        self.Checked_Title_For_Multiple_Simple_Bars_Graphs = BooleanVar(W_Export_Graph)

        self.Title_For_Pie = StringVar(W_Export_Graph)

    def Create_Checkboxes_Widgets_For_Titles_For_Multiple_Graphs(self):
        self.Checkbox_Title_For_Multiple_Simple_Bars_Graphs = Checkbutton(self.Frame_Section_Simple_Bars , text="Colocar un mismo titulo a varios graficos" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Title_For_Multiple_Simple_Bars_Graphs , command= lambda: self.Checkbox_Multiple_Titles_Behavior("Simple_Bars"))
        self.Checkbox_Title_For_Multiple_Simple_Bars_Graphs.config(state="disabled")

    def Create_Entry_Widgets_For_Graphs_Titles(self):
        self.Text_Entry_For_Simple_Bars_fi = Label(self.Frame_Section_Simple_Bars , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico fi" , justify=LEFT)
        self.Entry_For_Simple_Bars_fi = Entry(self.Frame_Section_Simple_Bars , font=("Courier New" , 13) , textvariable=self.Title_For_Simple_Bars_fi , border=1)
        self.Entry_For_Simple_Bars_fi.config(state="disabled")

        self.Text_Entry_For_Simple_Bars_hi = Label(self.Frame_Section_Simple_Bars , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi" , justify=LEFT)
        self.Entry_For_Simple_Bars_hi = Entry(self.Frame_Section_Simple_Bars , font=("Courier New" , 13) , textvariable=self.Title_For_Simple_Bars_hi , border=1)
        self.Entry_For_Simple_Bars_hi.config(state="disabled")

        self.Text_Entry_For_Simple_Bars_hi_percent = Label(self.Frame_Section_Simple_Bars , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi%" , justify=LEFT)
        self.Entry_For_Simple_Bars_hi_percent = Entry(self.Frame_Section_Simple_Bars , font=("Courier New" , 13) , textvariable=self.Title_For_Simple_Bars_hi_percent , border=1)
        self.Entry_For_Simple_Bars_hi_percent.config(state="disabled")

        self.Text_Entry_Title_For_Multiple_Simple_Bars_Graphs = Label(self.Frame_Section_Simple_Bars , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para varios graficos" , justify=LEFT)
        self.Entry_Title_For_Multiple_Simple_Bars_Graphs = Entry(self.Frame_Section_Simple_Bars , font=("Courier New" , 13) , textvariable=self.Title_For_Multiple_Simple_Bars_Graphs , border=1)
        self.Entry_Title_For_Multiple_Simple_Bars_Graphs.config(state="disabled")


        self.Text_Entry_For_Pie = Label(self.Frame_Section_Pie , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico de pastel" , justify=LEFT)
        self.Entry_For_Pie = Entry(self.Frame_Section_Pie , font=("Courier New" , 13) , textvariable=self.Title_For_Pie , border=1)
        self.Entry_For_Pie.config(state="disabled")

    def Insert_Created_Widgets_Into_Dictionary(self):
        self.Dictionary_Entry_Titles_Widgets = {
            "Simple_Bars": {
                "Simple_Bars_fi": [self.Text_Entry_For_Simple_Bars_fi , self.Entry_For_Simple_Bars_fi],
                "Simple_Bars_hi": [self.Text_Entry_For_Simple_Bars_hi , self.Entry_For_Simple_Bars_hi],
                "Simple_Bars_hi_percent": [self.Text_Entry_For_Simple_Bars_hi_percent , self.Entry_For_Simple_Bars_hi_percent],
            },
            "Pie": {
                "Pie_hi_percent": [self.Text_Entry_For_Pie , self.Entry_For_Pie],
            },
        }
        self.Dictionary_Entry_Titles_Values = {
            "Simple_Bars": {
                "Simple_Bars_fi": self.Title_For_Simple_Bars_fi,
                "Simple_Bars_hi": self.Title_For_Simple_Bars_hi,
                "Simple_Bars_hi_percent": self.Title_For_Simple_Bars_hi_percent,
            },
            "Pie": {
                "Pie_hi_percent": self.Title_For_Pie,
            },
        }
        
        self.Dictionary_Entry_Multiple_Titles_Widgets = {
            "Simple_Bars": [self.Text_Entry_Title_For_Multiple_Simple_Bars_Graphs , self.Entry_Title_For_Multiple_Simple_Bars_Graphs],
        }
        self.Dictionary_Entry_Multiple_Titles_Values = {
            "Simple_Bars": self.Title_For_Multiple_Simple_Bars_Graphs,
        }

        self.Dictionary_Checkboxes_Multiple_Titles_Widgets = {
            "Simple_Bars": self.Checkbox_Title_For_Multiple_Simple_Bars_Graphs,
        }
        self.Dictionary_Checkboxes_Multiple_Titles_Values = {
            "Simple_Bars": self.Checked_Title_For_Multiple_Simple_Bars_Graphs,
        }

class Section_Checkboxes_For_Export_Graphs:
    def __init__(self , W_Export_Graph):
        self.Checked_Simple_Bars = BooleanVar(W_Export_Graph)
        self.Checked_Simple_Bars_fi = BooleanVar(W_Export_Graph)
        self.Checked_Simple_Bars_hi = BooleanVar(W_Export_Graph)
        self.Checked_Simple_Bars_hi_percent = BooleanVar(W_Export_Graph)

        self.Checked_Pie = BooleanVar(W_Export_Graph)

    def Create_Checkboxes_Widgets(self):
        self.Checkbox_Simple_Bars = Checkbutton(self.Frame_Section_Simple_Bars , text="Exportar todas los graficos de barras simples" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Simple_Bars , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Simple_Bars"))
        self.Checkbox_Simple_Bars_fi = Checkbutton(self.Frame_Section_Simple_Bars , text="Exportar grafico fi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Simple_Bars_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "fi"))
        self.Checkbox_Simple_Bars_hi = Checkbutton(self.Frame_Section_Simple_Bars , text="Exportar grafico hi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Simple_Bars_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "hi"))
        self.Checkbox_Simple_Bars_hi_percent = Checkbutton(self.Frame_Section_Simple_Bars , text="Exportar grafico hi%" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Simple_Bars_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "hi_percent"))

        self.Checkbox_Pie = Checkbutton(self.Frame_Section_Pie , text="Exportar grafico de pastel" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Pie , command= lambda: self.Check_And_Block_Single_Checkbox("Pie" , "hi_percent"))
        
    def Insert_Created_Widgets_Into_Dictionary(self):
        self.Dictionary_Main_Checkboxes_Values = {
            "Simple_Bars": self.Checked_Simple_Bars,
            "Pie": self.Checked_Pie,
        }
        self.Dictionary_Subcheckboxes_Values = {
            "Simple_Bars": {
                "Simple_Bars_fi": self.Checked_Simple_Bars_fi,
                "Simple_Bars_hi": self.Checked_Simple_Bars_hi,
                "Simple_Bars_hi_percent": self.Checked_Simple_Bars_hi_percent,
            },
            "Pie": {
                "Pie_hi_percent": self.Checked_Pie,
            },
        }

        self.Dictionary_Main_Checkboxes_Widgets = {
            "Simple_Bars": self.Checkbox_Simple_Bars,
            "Pie": self.Checkbox_Pie,
        }
        self.Dictionary_Subcheckboxes_Widgets = {
            "Simple_Bars": {
                "Simple_Bars_fi": self.Checkbox_Simple_Bars_fi,
                "Simple_Bars_hi": self.Checkbox_Simple_Bars_hi,
                "Simple_Bars_hi_percent": self.Checkbox_Simple_Bars_hi_percent,
            },
            "Pie": {
                "Pie_hi_percent": self.Checkbox_Pie,
            },
        }

class Section_Export_Graphs_For_Cualitative_Data(Notebox_Widget_Container , Handler_Actions , Section_Graphs_Titles , Section_Checkboxes_For_Export_Graphs):
    def __init__(self, W_Export_Graph, Axis_x_Title):
        self.W_Export_Graph = W_Export_Graph
        self.Axis_x_Title = Axis_x_Title

        self.Notebook_For_Entry_Titles_Section = None
        Notebox_Widget_Container.__init__(self , W_Export_Graph , Axis_x_Title)
        Handler_Actions.__init__(self , W_Export_Graph)

        self.Frame_Section_Simple_Bars = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Pie = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")

        self.Collection_Of_Frames = [self.Frame_Section_Simple_Bars , self.Frame_Section_Pie]

        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Simple_Bars , text="Titulos para\nbarras simples")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Pie , text="Titulo para\ngrafico de pastel")

        Section_Checkboxes_For_Export_Graphs.__init__(self , W_Export_Graph)

        Section_Graphs_Titles.__init__(self , W_Export_Graph)

    def Create_Widgets(self):
        Section_Checkboxes_For_Export_Graphs.Create_Checkboxes_Widgets(self)
        Section_Checkboxes_For_Export_Graphs.Insert_Created_Widgets_Into_Dictionary(self)

        Section_Graphs_Titles.Create_Entry_Widgets_For_Graphs_Titles(self)
        Section_Graphs_Titles.Create_Checkboxes_Widgets_For_Titles_For_Multiple_Graphs(self)
        Section_Graphs_Titles.Insert_Created_Widgets_Into_Dictionary(self)
        
        Notebox_Widget_Container.Insert_Widgets_In_Notebook_Container(self)
