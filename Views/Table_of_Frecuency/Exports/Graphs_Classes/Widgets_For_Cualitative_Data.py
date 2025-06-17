import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , '..')))

from tkinter import *; from tkinter import ttk

from Views.Table_of_Frecuency.Exports.Graphs_Classes.Handler_Widgets_Export import Handler_Actions

class Entry_Widget_For_Export_Graphs_For_Cualitative_Data:
    def __init__(self , W_Export_Graph):
        self.Title_For_Simple_Bars_fi = StringVar(W_Export_Graph)
        self.Title_For_Simple_Bars_hi = StringVar(W_Export_Graph)
        self.Title_For_Simple_Bars_hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Pie = StringVar(W_Export_Graph)

        self.Title_For_Axis_x = StringVar(W_Export_Graph)

        self.Main_Container = Label(W_Export_Graph , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)

        self.Frame_Sets = Frame(W_Export_Graph , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)

        self.Canvas_Set = Canvas(self.Frame_Sets, width=1220, height=100)

        self.ScrollBar_Frame = ttk.Scrollbar(self.Frame_Sets, orient="vertical", command=self.Canvas_Set.yview)

        self.Canvas_Set.configure(yscrollcommand=self.ScrollBar_Frame.set)

        self.Content_Frame_Sets = Frame(self.Canvas_Set, width=1240 , bg="#CDC4FF")

        self.Canvas_Set.create_window((0, 0), window=self.Content_Frame_Sets, anchor="nw")

    def Create_Entry_Widgets(self , Axis_x_title):
        self.Text_Entry_For_Simple_Bars_fi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo barras simples fi")
        self.Entry_For_Simple_Bars_fi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_fi)
        
        self.Text_Entry_For_Simple_Bars_hi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo barras simples hi")
        self.Entry_For_Simple_Bars_hi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi)
        
        self.Text_Entry_For_Simple_Bars_hi_percent = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo barras simples hi%")
        self.Entry_For_Simple_Bars_hi_percent = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi_percent)

        self.Text_Entry_For_Pie = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo para grafico de pastel")
        self.Entry_For_Pie = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_fi)

        self.Title_For_Axis_x.set(Axis_x_title)
        self.Text_Entry_For_Axis_x = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo eje x")
        self.Entry_For_Axis_x = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Axis_x)

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
        for dict_with_entry_widgets in self.Dictionary_Entry_Titles_Widgets.values():
            for idx , entry_titles_widget in enumerate(dict_with_entry_widgets.values()):
                entry_titles_widget[0].grid(row=idx*2, column=0, padx=10, pady=10, sticky="w")
                entry_titles_widget[1].grid(row=idx*2, column=1, padx=10, pady=10, sticky="w")

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
        Entry_Widget_For_Export_Graphs_For_Cualitative_Data.__init__(self , W_Export_Graph)

    def Create_Widgets(self):
        self.Checkbox_Simple_Bars = Checkbutton(self.W_Export_Graph , text="Exportar Histograma" , font=("Times New Roman" , 13) , variable=self.Checked_Histogram , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Simple_Bars"))
        self.Checkbox_Simple_Bars_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , variable=self.Checked_Histogram_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "fi"))
        self.Checkbox_Simple_Bars_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , variable=self.Checked_Histogram_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "hi"))
        self.Checkbox_Simple_Bars_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Histogram_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Simple_Bars" , "hi_percent"))

        self.Checkbox_Pie = Checkbutton(self.W_Export_Graph , text="Exportar Poligono de Frecuencias" , font=("Times New Roman" , 13) , variable=self.Checked_Frecuences_Polygon , command= lambda: self.Check_And_Block_Single_Checkbox("Pie" , "hi_percent"))
        
        self.Dictionary_Main_Checkboxes_Values = {
            "Simple_Bars": self.Checked_Simple_Bars,
            "Pie": self.Checked_Pie,
        }
        self.Dictionary_Of_Subcheckboxes_Values = {
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
    
        self.Create_Entry_Widgets(self.Axis_x_Title)