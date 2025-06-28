import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , '..')))

from tkinter import *

from Views.Table_of_Frecuency.Exports.Graphs_Classes.Handler_Widgets_Export import Handler_Actions , Container_For_Entry_Title_Widgets

class Entry_Widget_For_Export_Graphs_For_Cualitative_Data(Container_For_Entry_Title_Widgets):
    def __init__(self , W_Export_Graph , Axis_x_Title):
        self.Title_For_Simple_Bars_fi = StringVar(W_Export_Graph)
        self.Title_For_Simple_Bars_hi = StringVar(W_Export_Graph)
        self.Title_For_Simple_Bars_hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Pie = StringVar(W_Export_Graph)

        Container_For_Entry_Title_Widgets.__init__(self , W_Export_Graph , Axis_x_Title)

        self.Frame_Section_Simple_Bars = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Pie = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")

        self.Collection_Of_Frames = [self.Frame_Section_Simple_Bars , self.Frame_Section_Pie]

        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Simple_Bars , text="Titulos para\nbarras simples")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Pie , text="Titulo para\ngrafico de pastel")


    def Create_Entry_Widgets(self):
        self.Text_Entry_For_Simple_Bars_fi = Label(self.Frame_Section_Simple_Bars , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico fi" , justify=LEFT)
        self.Entry_For_Simple_Bars_fi = Entry(self.Frame_Section_Simple_Bars , font=("Courier New" , 13) , textvariable=self.Title_For_Simple_Bars_fi , border=1)
        self.Entry_For_Simple_Bars_fi.config(state="disabled")

        self.Text_Entry_For_Simple_Bars_hi = Label(self.Frame_Section_Simple_Bars , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi" , justify=LEFT)
        self.Entry_For_Simple_Bars_hi = Entry(self.Frame_Section_Simple_Bars , font=("Courier New" , 13) , textvariable=self.Title_For_Simple_Bars_hi , border=1)
        self.Entry_For_Simple_Bars_hi.config(state="disabled")

        self.Text_Entry_For_Simple_Bars_hi_percent = Label(self.Frame_Section_Simple_Bars , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi%" , justify=LEFT)
        self.Entry_For_Simple_Bars_hi_percent = Entry(self.Frame_Section_Simple_Bars , font=("Courier New" , 13) , textvariable=self.Title_For_Simple_Bars_hi_percent , border=1)
        self.Entry_For_Simple_Bars_hi_percent.config(state="disabled")

        self.Text_Entry_For_Pie = Label(self.Frame_Section_Pie , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico de pastel" , justify=LEFT)
        self.Entry_For_Pie = Entry(self.Frame_Section_Pie , font=("Courier New" , 13) , textvariable=self.Title_For_Pie , border=1)
        self.Entry_For_Pie.config(state="disabled")

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
        

class Checkboxes_Export_Graphs_For_Cualitative_Data(Handler_Actions , Entry_Widget_For_Export_Graphs_For_Cualitative_Data):
    def __init__(self , W_Export_Graph , Axis_x_Title):
        self.W_Export_Graph = W_Export_Graph
        self.Axis_x_Title = Axis_x_Title

        self.Checked_Simple_Bars = BooleanVar(self.W_Export_Graph)
        self.Checked_Simple_Bars_fi = BooleanVar(self.W_Export_Graph)
        self.Checked_Simple_Bars_hi = BooleanVar(self.W_Export_Graph)
        self.Checked_Simple_Bars_hi_percent = BooleanVar(self.W_Export_Graph)

        self.Checked_Pie = BooleanVar(self.W_Export_Graph)

        Handler_Actions.__init__(self , W_Export_Graph)
        Entry_Widget_For_Export_Graphs_For_Cualitative_Data.__init__(self , W_Export_Graph , Axis_x_Title)

    def Create_Widgets(self):
        self.Checkbox_Simple_Bars = Checkbutton(self.Frame_Section_Simple_Bars , text="Exportar todas los graficos de barras simples" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Simple_Bars , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Simple_Bars"))
        self.Checkbox_Simple_Bars_fi = Checkbutton(self.Frame_Section_Simple_Bars , text="Exportar grafico fi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Simple_Bars_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "fi"))
        self.Checkbox_Simple_Bars_hi = Checkbutton(self.Frame_Section_Simple_Bars , text="Exportar grafico hi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Simple_Bars_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "hi"))
        self.Checkbox_Simple_Bars_hi_percent = Checkbutton(self.Frame_Section_Simple_Bars , text="Exportar grafico hi%" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Simple_Bars_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "hi_percent"))

        self.Checkbox_Pie = Checkbutton(self.Frame_Section_Pie , text="Exportar grafico de pastel" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Pie , command= lambda: self.Check_And_Block_Single_Checkbox("Pie" , "hi_percent"))
        
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
    
        self.Create_Entry_Widgets()

        self.Insert_Widgets_In_Notebook_Container(self.Dictionary_Main_Checkboxes_Widgets , self.Dictionary_Subcheckboxes_Widgets , self.Categories_With_Single_Main_Checkbox , self.Collection_Of_Frames)