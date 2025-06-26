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

        self.Title_For_Axis_x = StringVar(W_Export_Graph)

        Container_For_Entry_Title_Widgets.__init__(self , W_Export_Graph , Axis_x_Title)

    def Create_Entry_Widgets(self):
        self.Text_Section_Simple_Bars = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulos para barras simples" , justify=CENTER)
        self.Text_Entry_For_Simple_Bars_fi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para fi" , justify=LEFT)
        self.Entry_For_Simple_Bars_fi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Simple_Bars_fi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Simple_Bars_fi.config(state="disabled")

        self.Text_Entry_For_Simple_Bars_hi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi" , justify=LEFT)
        self.Entry_For_Simple_Bars_hi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Simple_Bars_hi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Simple_Bars_hi.config(state="disabled")

        self.Text_Entry_For_Simple_Bars_hi_percent = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi%" , justify=LEFT)
        self.Entry_For_Simple_Bars_hi_percent = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Simple_Bars_hi_percent , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Simple_Bars_hi_percent.config(state="disabled")

        self.Text_Entry_For_Pie = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo grafico de pastel" , justify=LEFT)
        self.Entry_For_Pie = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Pie , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Pie.config(state="disabled")

        self.Dictionary_Text_Sections = {
            "Simple_Bars": self.Text_Section_Simple_Bars,
            "Pie": None,
        }

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

        self.Insert_Widgets_In_Container()
        

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
        self.Checkbox_Simple_Bars = Checkbutton(self.W_Export_Graph , text="Barras simples" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Simple_Bars , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Simple_Bars"))
        self.Checkbox_Simple_Bars_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Simple_Bars_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "fi"))
        self.Checkbox_Simple_Bars_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Simple_Bars_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "hi"))
        self.Checkbox_Simple_Bars_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Simple_Bars_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "hi_percent"))

        self.Checkbox_Pie = Checkbutton(self.W_Export_Graph , text="Grafico de pastel" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Pie , command= lambda: self.Check_And_Block_Single_Checkbox("Pie" , "hi_percent"))
        
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