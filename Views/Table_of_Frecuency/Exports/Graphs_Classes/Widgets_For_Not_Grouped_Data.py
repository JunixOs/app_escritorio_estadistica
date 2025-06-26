import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , '..')))

from tkinter import *

from Views.Table_of_Frecuency.Exports.Graphs_Classes.Handler_Widgets_Export import Handler_Actions , Container_For_Entry_Title_Widgets

class Entry_Widget_For_Export_Graphs_For_Not_Grouped_Data(Container_For_Entry_Title_Widgets):
    def __init__(self , W_Export_Graph , Axis_x_Title):
        self.Title_For_Bars_Graph_fi = StringVar(W_Export_Graph)
        self.Title_For_Bars_Graph_hi = StringVar(W_Export_Graph)
        self.Title_For_Bars_Graph_hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Stick_Graph_fi = StringVar(W_Export_Graph)
        self.Title_For_Stick_Graph_hi = StringVar(W_Export_Graph)
        self.Title_For_Stick_Graph_hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Step_Chart_Fi = StringVar(W_Export_Graph)
        self.Title_For_Step_Chart_Hi = StringVar(W_Export_Graph)
        self.Title_For_Step_Chart_Hi_percent = StringVar(W_Export_Graph)

        Container_For_Entry_Title_Widgets.__init__(self , W_Export_Graph , Axis_x_Title)

        self.Frame_Section_Bars_Graph = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Stick_Graph = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Step_Chart = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")

        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Bars_Graph , text="Titulos para\ngraficos de barras")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Stick_Graph , text="Titulos para\ngraficos de bastones")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Step_Chart , text="Titulos para\ngraficos de escalones")

    def Create_Entry_Widgets(self):        
        self.Text_Entry_For_Bars_Graph_fi = Label(self.Frame_Section_Bars_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para fi" , justify=LEFT)
        self.Entry_For_Bars_Graph_fi = Entry(self.Frame_Section_Bars_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Bars_Graph_fi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Bars_Graph_fi.config(state="disabled")

        self.Text_Entry_For_Bars_Graph_hi = Label(self.Frame_Section_Bars_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi" , justify=LEFT)
        self.Entry_For_Bars_Graph_hi = Entry(self.Frame_Section_Bars_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Bars_Graph_hi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Bars_Graph_hi.config(state="disabled")

        self.Text_Entry_For_Bars_Graph_hi_percent = Label(self.Frame_Section_Bars_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi%" , justify=LEFT)
        self.Entry_For_Bars_Graph_hi_percent = Entry(self.Frame_Section_Bars_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Bars_Graph_hi_percent , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Bars_Graph_hi_percent.config(state="disabled")


        self.Text_Entry_For_Stick_Graph_fi = Label(self.Frame_Section_Stick_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para fi" , justify=LEFT)
        self.Entry_For_Stick_Graph_fi = Entry(self.Frame_Section_Stick_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Stick_Graph_fi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Stick_Graph_fi.config(state="disabled")

        self.Text_Entry_For_Stick_Graph_hi = Label(self.Frame_Section_Stick_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi" , justify=LEFT)
        self.Entry_For_Stick_Graph_hi = Entry(self.Frame_Section_Stick_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Stick_Graph_hi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Stick_Graph_hi.config(state="disabled")
        
        self.Text_Entry_For_Stick_Graph_hi_percent = Label(self.Frame_Section_Stick_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para hi%" , justify=LEFT)
        self.Entry_For_Stick_Graph_hi_percent = Entry(self.Frame_Section_Stick_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Stick_Graph_hi_percent , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Stick_Graph_hi_percent.config(state="disabled")


        self.Text_Entry_For_Step_Chart_Fi = Label(self.Frame_Section_Step_Chart , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para Fi" , justify=LEFT)
        self.Entry_For_Step_Chart_Fi = Entry(self.Frame_Section_Step_Chart , font=("Courier New" , 13) , textvariable=self.Title_For_Step_Chart_Fi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Step_Chart_Fi.config(state="disabled")

        self.Text_Entry_For_Step_Chart_Hi = Label(self.Frame_Section_Step_Chart , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para Hi" , justify=LEFT)
        self.Entry_For_Step_Chart_Hi = Entry(self.Frame_Section_Step_Chart , font=("Courier New" , 13) , textvariable=self.Title_For_Step_Chart_Hi , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Step_Chart_Hi.config(state="disabled")
        
        self.Text_Entry_For_Step_Chart_Hi_percent = Label(self.Frame_Section_Step_Chart , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Para Hi%" , justify=LEFT)
        self.Entry_For_Step_Chart_Hi_percent = Entry(self.Frame_Section_Step_Chart , font=("Courier New" , 13) , textvariable=self.Title_For_Step_Chart_Hi_percent , border=1 , width=self.Width_For_Entry_Titles)
        self.Entry_For_Step_Chart_Hi_percent.config(state="disabled")


        self.Dictionary_Entry_Titles_Widgets = {
            "Bars_Graph": {
                "Bars_Graph_fi": [self.Text_Entry_For_Bars_Graph_fi , self.Entry_For_Bars_Graph_fi],
                "Bars_Graph_hi": [self.Text_Entry_For_Bars_Graph_hi , self.Entry_For_Bars_Graph_hi],
                "Bars_Graph_hi_percent": [self.Text_Entry_For_Bars_Graph_hi_percent , self.Entry_For_Bars_Graph_hi_percent],
            },
            "Stick_Graph": {
                "Stick_Graph_fi": [self.Text_Entry_For_Stick_Graph_fi , self.Entry_For_Stick_Graph_fi],
                "Stick_Graph_hi": [self.Text_Entry_For_Stick_Graph_hi , self.Entry_For_Stick_Graph_hi],
                "Stick_Graph_hi_percent": [self.Text_Entry_For_Stick_Graph_hi_percent , self.Entry_For_Stick_Graph_hi_percent],
            },
            "Step_Chart": {  
                "Step_Chart_Fi": [self.Text_Entry_For_Step_Chart_Fi , self.Entry_For_Step_Chart_Fi],
                "Step_Chart_Hi": [self.Text_Entry_For_Step_Chart_Hi , self.Entry_For_Step_Chart_Hi],
                "Step_Chart_Hi_percent": [self.Text_Entry_For_Step_Chart_Hi_percent , self.Entry_For_Step_Chart_Hi_percent],
            },
        }

        self.Dictionary_Entry_Titles_Values = {
            "Bars_Graph": {
                "Bars_Graph_fi": self.Title_For_Bars_Graph_fi,
                "Bars_Graph_hi": self.Title_For_Bars_Graph_hi,
                "Bars_Graph_hi_percent": self.Title_For_Bars_Graph_hi_percent,
            },
            "Stick_Graph": {
                "Stick_Graph_fi": self.Title_For_Stick_Graph_fi,
                "Stick_Graph_hi": self.Title_For_Stick_Graph_hi,
                "Stick_Graph_hi_percent": self.Title_For_Stick_Graph_hi_percent,
            },
            "Step_Chart": {  
                "Step_Chart_Fi": self.Title_For_Step_Chart_Fi,
                "Step_Chart_Hi": self.Title_For_Step_Chart_Hi,
                "Step_Chart_Hi_percent": self.Title_For_Step_Chart_Hi_percent,
            },
        }

        self.Insert_Widgets_In_Container()
        
class Checkboxes_Export_Graphs_For_Not_Grouped_Data(Handler_Actions , Entry_Widget_For_Export_Graphs_For_Not_Grouped_Data):
    def __init__(self , W_Export_Graph , Axis_x_Title):
        self.W_Export_Graph = W_Export_Graph
        self.Axis_x_Title = Axis_x_Title

        self.Checked_Bars_Graph = BooleanVar(self.W_Export_Graph)
        self.Checked_Bars_Graph_fi = BooleanVar(self.W_Export_Graph)
        self.Checked_Bars_Graph_hi = BooleanVar(self.W_Export_Graph)
        self.Checked_Bars_Graph_hi_percent = BooleanVar(self.W_Export_Graph)

        self.Checked_Stick_Graph = BooleanVar(self.W_Export_Graph)
        self.Checked_Stick_Graph_fi = BooleanVar(self.W_Export_Graph)
        self.Checked_Stick_Graph_hi = BooleanVar(self.W_Export_Graph)
        self.Checked_Stick_Graph_hi_percent = BooleanVar(self.W_Export_Graph)

        self.Checked_Step_Chart = BooleanVar(self.W_Export_Graph)
        self.Checked_Step_Chart_Fi = BooleanVar(self.W_Export_Graph)
        self.Checked_Step_Chart_Hi = BooleanVar(self.W_Export_Graph)
        self.Checked_Step_Chart_Hi_percent = BooleanVar(self.W_Export_Graph)

        Handler_Actions.__init__(self , W_Export_Graph)
        Entry_Widget_For_Export_Graphs_For_Not_Grouped_Data.__init__(self , W_Export_Graph , Axis_x_Title)

    def Create_Widgets(self):
        self.Checkbox_Bars_Graph = Checkbutton(self.W_Export_Graph , text="Graficos de barras" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Bars_Graph , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Bars_Graph"))
        self.Checkbox_Bars_Graph_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Bars_Graph_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Bars_Graph" , "fi"))
        self.Checkbox_Bars_Graph_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Bars_Graph_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Bars_Graph" , "hi"))
        self.Checkbox_Bars_Graph_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Bars_Graph_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Bars_Graph" , "hi_percent"))

        self.Checkbox_Stick_Graph = Checkbutton(self.W_Export_Graph , text="Graficos de bastones" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Stick_Graph , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Stick_Graph"))
        self.Checkbox_Stick_Graph_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Stick_Graph_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Stick_Graph" , "fi"))
        self.Checkbox_Stick_Graph_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Stick_Graph_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Stick_Graph" , "hi"))
        self.Checkbox_Stick_Graph_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Stick_Graph_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Stick_Graph" , "hi_percent"))

        self.Checkbox_Step_Chart = Checkbutton(self.W_Export_Graph , text="Graficos de escalones" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Step_Chart , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Step_Chart"))
        self.Checkbox_Step_Chart_Fi = Checkbutton(self.W_Export_Graph , text="Para Fi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Step_Chart_Fi , command= lambda: self.Check_And_Block_Single_Checkbox("Step_Chart" , "Fi"))
        self.Checkbox_Step_Chart_Hi = Checkbutton(self.W_Export_Graph , text="Para Hi" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Step_Chart_Hi , command= lambda: self.Check_And_Block_Single_Checkbox("Step_Chart" , "Hi"))
        self.Checkbox_Step_Chart_Hi_percent = Checkbutton(self.W_Export_Graph , text="Para Hi%" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Step_Chart_Hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Step_Chart" , "Hi_percent"))

        self.Dictionary_Main_Checkboxes_Values = {
            "Bars_Graph": self.Checked_Bars_Graph,
            "Stick_Graph": self.Checked_Stick_Graph,
            "Step_Chart": self.Checked_Step_Chart,
        }
        self.Dictionary_Subcheckboxes_Values = {
            "Bars_Graph": {
                "Bars_Graph_fi": self.Checked_Bars_Graph_fi,
                "Bars_Graph_hi": self.Checked_Bars_Graph_hi,
                "Bars_Graph_hi_percent": self.Checked_Bars_Graph_hi_percent,
            },
            "Stick_Graph": {
                "Stick_Graph_fi": self.Checked_Stick_Graph_fi,
                "Stick_Graph_hi": self.Checked_Stick_Graph_hi,
                "Stick_Graph_hi_percent": self.Checked_Stick_Graph_hi_percent,
            },
            "Step_Chart": {
                "Step_Chart_Fi": self.Checked_Step_Chart_Fi,
                "Step_Chart_Hi": self.Checked_Step_Chart_Hi,
                "Step_Chart_Hi_percent": self.Checked_Step_Chart_Hi_percent,
            },
        }

        self.Dictionary_Main_Checkboxes_Widgets = {
            "Bars_Graph": self.Checkbox_Bars_Graph,
            "Stick_Graph": self.Checkbox_Stick_Graph,
            "Step_Chart": self.Checkbox_Step_Chart,
        }
        self.Dictionary_Subcheckboxes_Widgets = {
            "Bars_Graph": {
                "Bars_Graph_fi": self.Checkbox_Bars_Graph_fi,
                "Bars_Graph_hi": self.Checkbox_Bars_Graph_hi,
                "Bars_Graph_hi_percent": self.Checkbox_Bars_Graph_hi_percent,
            },
            "Stick_Graph": {
                "Stick_Graph_fi": self.Checkbox_Stick_Graph_fi,
                "Stick_Graph_hi": self.Checkbox_Stick_Graph_hi,
                "Stick_Graph_hi_percent": self.Checkbox_Stick_Graph_hi_percent,
            },
            "Step_Chart": {
                "Step_Chart_Fi": self.Checkbox_Step_Chart_Fi,
                "Step_Chart_Hi": self.Checkbox_Step_Chart_Hi,
                "Step_Chart_Hi_percent": self.Checkbox_Step_Chart_Hi_percent,
            },
        }
    
        self.Create_Entry_Widgets()