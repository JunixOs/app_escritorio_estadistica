import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , '..')))

from tkinter import *

from Views.Table_of_Frecuency.Exports.Graphs_Classes.Handler_Widgets_Export import Handler_Actions , Notebox_Widget_Container

class Section_Graphs_Titles:
    def __init__(self , W_Export_Graph):
        self.Title_For_Bars_Graph_fi = StringVar(W_Export_Graph)
        self.Title_For_Bars_Graph_hi = StringVar(W_Export_Graph)
        self.Title_For_Bars_Graph_hi_percent = StringVar(W_Export_Graph)
        self.Title_For_Multiple_Bars_Graphs = StringVar(W_Export_Graph)
        self.Checked_Title_For_Multiple_Bars_Graphs = BooleanVar(W_Export_Graph)

        self.Title_For_Stick_Graph_fi = StringVar(W_Export_Graph)
        self.Title_For_Stick_Graph_hi = StringVar(W_Export_Graph)
        self.Title_For_Stick_Graph_hi_percent = StringVar(W_Export_Graph)
        self.Title_For_Multiple_Stick_Graphs = StringVar(W_Export_Graph)
        self.Checked_Title_For_Multiple_Stick_Graphs = BooleanVar(W_Export_Graph)

        self.Title_For_Step_Chart_Fi = StringVar(W_Export_Graph)
        self.Title_For_Step_Chart_Hi = StringVar(W_Export_Graph)
        self.Title_For_Step_Chart_Hi_percent = StringVar(W_Export_Graph)
        self.Title_For_Multiple_Step_Chart_Graphs = StringVar(W_Export_Graph)
        self.Checked_Title_For_Multiple_Step_Chart_Graphs = BooleanVar(W_Export_Graph)

    def Create_Checkboxes_Widgets_For_Titles_For_Multiple_Graphs(self):
        self.Checkbox_Title_For_Multiple_Bars_Graphs = Checkbutton(self.Frame_Section_Bars_Graph , text="Colocar un mismo titulo a varios graficos" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Title_For_Multiple_Bars_Graphs , command= lambda: self.Checkbox_Multiple_Titles_Behavior("Bars_Graph"))
        self.Checkbox_Title_For_Multiple_Bars_Graphs.config(state="disabled")

        self.Checkbox_Title_For_Multiple_Stick_Graphs = Checkbutton(self.Frame_Section_Stick_Graph , text="Colocar un mismo titulo a varios graficos" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Title_For_Multiple_Stick_Graphs , command= lambda: self.Checkbox_Multiple_Titles_Behavior("Stick_Graph"))
        self.Checkbox_Title_For_Multiple_Stick_Graphs.config(state="disabled")

        self.Checkbox_Title_For_Multiple_Step_Chart_Graphs = Checkbutton(self.Frame_Section_Step_Chart , text="Colocar un mismo titulo a varios graficos" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Title_For_Multiple_Step_Chart_Graphs , command= lambda: self.Checkbox_Multiple_Titles_Behavior("Step_Chart"))
        self.Checkbox_Title_For_Multiple_Step_Chart_Graphs.config(state="disabled")

    def Create_Entry_Widgets_For_Graphs_Titles(self):        
        self.Text_Entry_For_Bars_Graph_fi = Label(self.Frame_Section_Bars_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico fi" , justify=LEFT)
        self.Entry_For_Bars_Graph_fi = Entry(self.Frame_Section_Bars_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Bars_Graph_fi , border=1)
        self.Entry_For_Bars_Graph_fi.config(state="disabled")

        self.Text_Entry_For_Bars_Graph_hi = Label(self.Frame_Section_Bars_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi" , justify=LEFT)
        self.Entry_For_Bars_Graph_hi = Entry(self.Frame_Section_Bars_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Bars_Graph_hi , border=1)
        self.Entry_For_Bars_Graph_hi.config(state="disabled")

        self.Text_Entry_For_Bars_Graph_hi_percent = Label(self.Frame_Section_Bars_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi%" , justify=LEFT)
        self.Entry_For_Bars_Graph_hi_percent = Entry(self.Frame_Section_Bars_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Bars_Graph_hi_percent , border=1)
        self.Entry_For_Bars_Graph_hi_percent.config(state="disabled")

        self.Text_Entry_Title_For_Multiple_Bars_Graphs = Label(self.Frame_Section_Bars_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para varios graficos" , justify=LEFT)
        self.Entry_Title_For_Multiple_Bars_Graphs = Entry(self.Frame_Section_Bars_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Multiple_Bars_Graphs , border=1)
        self.Entry_Title_For_Multiple_Bars_Graphs.config(state="disabled")


        self.Text_Entry_For_Stick_Graph_fi = Label(self.Frame_Section_Stick_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico fi" , justify=LEFT)
        self.Entry_For_Stick_Graph_fi = Entry(self.Frame_Section_Stick_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Stick_Graph_fi , border=1)
        self.Entry_For_Stick_Graph_fi.config(state="disabled")

        self.Text_Entry_For_Stick_Graph_hi = Label(self.Frame_Section_Stick_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi" , justify=LEFT)
        self.Entry_For_Stick_Graph_hi = Entry(self.Frame_Section_Stick_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Stick_Graph_hi , border=1)
        self.Entry_For_Stick_Graph_hi.config(state="disabled")
        
        self.Text_Entry_For_Stick_Graph_hi_percent = Label(self.Frame_Section_Stick_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico hi%" , justify=LEFT)
        self.Entry_For_Stick_Graph_hi_percent = Entry(self.Frame_Section_Stick_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Stick_Graph_hi_percent , border=1)
        self.Entry_For_Stick_Graph_hi_percent.config(state="disabled")

        self.Text_Entry_Title_For_Multiple_Stick_Graphs = Label(self.Frame_Section_Stick_Graph , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para varios graficos" , justify=LEFT)
        self.Entry_Title_For_Multiple_Stick_Graphs = Entry(self.Frame_Section_Stick_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Multiple_Stick_Graphs , border=1)
        self.Entry_Title_For_Multiple_Stick_Graphs.config(state="disabled")


        self.Text_Entry_For_Step_Chart_Fi = Label(self.Frame_Section_Step_Chart , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico Fi" , justify=LEFT)
        self.Entry_For_Step_Chart_Fi = Entry(self.Frame_Section_Step_Chart , font=("Courier New" , 13) , textvariable=self.Title_For_Step_Chart_Fi , border=1)
        self.Entry_For_Step_Chart_Fi.config(state="disabled")

        self.Text_Entry_For_Step_Chart_Hi = Label(self.Frame_Section_Step_Chart , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico Hi" , justify=LEFT)
        self.Entry_For_Step_Chart_Hi = Entry(self.Frame_Section_Step_Chart , font=("Courier New" , 13) , textvariable=self.Title_For_Step_Chart_Hi , border=1)
        self.Entry_For_Step_Chart_Hi.config(state="disabled")
        
        self.Text_Entry_For_Step_Chart_Hi_percent = Label(self.Frame_Section_Step_Chart , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para grafico Hi%" , justify=LEFT)
        self.Entry_For_Step_Chart_Hi_percent = Entry(self.Frame_Section_Step_Chart , font=("Courier New" , 13) , textvariable=self.Title_For_Step_Chart_Hi_percent , border=1)
        self.Entry_For_Step_Chart_Hi_percent.config(state="disabled")

        self.Text_Entry_Title_For_Multiple_Step_Chart_Graphs = Label(self.Frame_Section_Step_Chart , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo para varios graficos" , justify=LEFT)
        self.Entry_Title_For_Multiple_Step_Chart_Graphs = Entry(self.Frame_Section_Step_Chart , font=("Courier New" , 13) , textvariable=self.Title_For_Multiple_Step_Chart_Graphs , border=1)
        self.Entry_Title_For_Multiple_Step_Chart_Graphs.config(state="disabled")

    def Insert_Created_Widgets_Into_Dictionary(self):
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

        self.Dictionary_Entry_Multiple_Titles_Widgets = {
            "Bars_Graph": [self.Text_Entry_Title_For_Multiple_Bars_Graphs , self.Entry_Title_For_Multiple_Bars_Graphs],
            "Stick_Graph": [self.Text_Entry_Title_For_Multiple_Stick_Graphs , self.Entry_Title_For_Multiple_Stick_Graphs],
            "Step_Chart": [self.Text_Entry_Title_For_Multiple_Step_Chart_Graphs , self.Entry_Title_For_Multiple_Step_Chart_Graphs],
        }
        self.Dictionary_Entry_Multiple_Titles_Values = {
            "Bars_Graph": self.Title_For_Multiple_Bars_Graphs,
            "Stick_Graph": self.Title_For_Multiple_Stick_Graphs,
            "Step_Chart": self.Title_For_Multiple_Step_Chart_Graphs,
        }

        self.Dictionary_Checkboxes_Multiple_Titles_Widgets = {
            "Bars_Graph": self.Checkbox_Title_For_Multiple_Bars_Graphs,
            "Stick_Graph": self.Checkbox_Title_For_Multiple_Stick_Graphs,
            "Step_Chart": self.Checkbox_Title_For_Multiple_Step_Chart_Graphs,
        }
        self.Dictionary_Checkboxes_Multiple_Titles_Values = {
            "Bars_Graph": self.Checked_Title_For_Multiple_Bars_Graphs,
            "Stick_Graph": self.Checked_Title_For_Multiple_Stick_Graphs,
            "Step_Chart": self.Checked_Title_For_Multiple_Step_Chart_Graphs,
        }
        
class Section_Checkboxes_For_Export_Graphs:
    def __init__(self , W_Export_Graph):

        self.Checked_Bars_Graph = BooleanVar(W_Export_Graph)
        self.Checked_Bars_Graph_fi = BooleanVar(W_Export_Graph)
        self.Checked_Bars_Graph_hi = BooleanVar(W_Export_Graph)
        self.Checked_Bars_Graph_hi_percent = BooleanVar(W_Export_Graph)

        self.Checked_Stick_Graph = BooleanVar(W_Export_Graph)
        self.Checked_Stick_Graph_fi = BooleanVar(W_Export_Graph)
        self.Checked_Stick_Graph_hi = BooleanVar(W_Export_Graph)
        self.Checked_Stick_Graph_hi_percent = BooleanVar(W_Export_Graph)

        self.Checked_Step_Chart = BooleanVar(W_Export_Graph)
        self.Checked_Step_Chart_Fi = BooleanVar(W_Export_Graph)
        self.Checked_Step_Chart_Hi = BooleanVar(W_Export_Graph)
        self.Checked_Step_Chart_Hi_percent = BooleanVar(W_Export_Graph)

    def Create_Checkboxes_Widgets(self):
        self.Checkbox_Bars_Graph = Checkbutton(self.Frame_Section_Bars_Graph , text="Exportar todos los graficos de barras" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Bars_Graph , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Bars_Graph"))
        self.Checkbox_Bars_Graph_fi = Checkbutton(self.Frame_Section_Bars_Graph , text="Exportar grafico fi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Bars_Graph_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Bars_Graph" , "fi"))
        self.Checkbox_Bars_Graph_hi = Checkbutton(self.Frame_Section_Bars_Graph , text="Exportar grafico hi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Bars_Graph_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Bars_Graph" , "hi"))
        self.Checkbox_Bars_Graph_hi_percent = Checkbutton(self.Frame_Section_Bars_Graph , text="Exportar grafico hi%" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Bars_Graph_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Bars_Graph" , "hi_percent"))

        self.Checkbox_Stick_Graph = Checkbutton(self.Frame_Section_Stick_Graph , text="Exportar todos los graficos de bastones" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Stick_Graph , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Stick_Graph"))
        self.Checkbox_Stick_Graph_fi = Checkbutton(self.Frame_Section_Stick_Graph , text="Exportar grafico fi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Stick_Graph_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Stick_Graph" , "fi"))
        self.Checkbox_Stick_Graph_hi = Checkbutton(self.Frame_Section_Stick_Graph , text="Exportar grafico hi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Stick_Graph_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Stick_Graph" , "hi"))
        self.Checkbox_Stick_Graph_hi_percent = Checkbutton(self.Frame_Section_Stick_Graph , text="Exportar grafico hi%" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Stick_Graph_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Stick_Graph" , "hi_percent"))

        self.Checkbox_Step_Chart = Checkbutton(self.Frame_Section_Step_Chart , text="Exportar todos los graficos de escalones" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Step_Chart , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Step_Chart"))
        self.Checkbox_Step_Chart_Fi = Checkbutton(self.Frame_Section_Step_Chart , text="Exportar grafico Fi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Step_Chart_Fi , command= lambda: self.Check_And_Block_Single_Checkbox("Step_Chart" , "Fi"))
        self.Checkbox_Step_Chart_Hi = Checkbutton(self.Frame_Section_Step_Chart , text="Exportar grafico Hi" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Step_Chart_Hi , command= lambda: self.Check_And_Block_Single_Checkbox("Step_Chart" , "Hi"))
        self.Checkbox_Step_Chart_Hi_percent = Checkbutton(self.Frame_Section_Step_Chart , text="Exportar grafico Hi%" , font=("Times New Roman" , 13) , bg="#F7F5DC" , variable=self.Checked_Step_Chart_Hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Step_Chart" , "Hi_percent"))

    def Insert_Created_Widgets_Into_Dictionary(self):
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

class Section_Export_Graphs_For_Not_Grouped_Data(Notebox_Widget_Container , Handler_Actions , Section_Graphs_Titles , Section_Checkboxes_For_Export_Graphs):
    def __init__(self, W_Export_Graph, Axis_x_Title):
        self.W_Export_Graph = W_Export_Graph
        self.Axis_x_Title = Axis_x_Title

        self.Notebook_For_Entry_Titles_Section = None
        Notebox_Widget_Container.__init__(self , W_Export_Graph , Axis_x_Title)
        Handler_Actions.__init__(self , W_Export_Graph)

        self.Frame_Section_Bars_Graph = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Stick_Graph = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")
        self.Frame_Section_Step_Chart = Frame(self.Notebook_For_Entry_Titles_Section , bg="#F7F5DC")

        self.Collection_Of_Frames = [self.Frame_Section_Bars_Graph , self.Frame_Section_Stick_Graph , self.Frame_Section_Step_Chart]

        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Bars_Graph , text="Titulos para\ngraficos de barras")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Stick_Graph , text="Titulos para\ngraficos de bastones")
        self.Notebook_For_Entry_Titles_Section.add(self.Frame_Section_Step_Chart , text="Titulos para\ngraficos de escalones")

        Section_Checkboxes_For_Export_Graphs.__init__(self , W_Export_Graph)

        Section_Graphs_Titles.__init__(self , W_Export_Graph)

    def Create_Widgets(self):
        Section_Checkboxes_For_Export_Graphs.Create_Checkboxes_Widgets(self)
        Section_Checkboxes_For_Export_Graphs.Insert_Created_Widgets_Into_Dictionary(self)

        Section_Graphs_Titles.Create_Entry_Widgets_For_Graphs_Titles(self)
        Section_Graphs_Titles.Create_Checkboxes_Widgets_For_Titles_For_Multiple_Graphs(self)
        Section_Graphs_Titles.Insert_Created_Widgets_Into_Dictionary(self)
        
        Notebox_Widget_Container.Insert_Widgets_In_Notebook_Container(self)