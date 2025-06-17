import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , '..')))

from tkinter import *; from tkinter import ttk

from Views.Table_of_Frecuency.Exports.Graphs_Classes.Handler_Widgets_Export import Handler_Actions

class Entry_Widget_For_Export_Graphs_For_Grouped_Data:
    def __init__(self , W_Export_Graph):
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

        self.Title_For_Axis_x = StringVar(W_Export_Graph)

        self.Main_Container = Label(W_Export_Graph , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)

        self.Frame_Sets = Frame(W_Export_Graph , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)

        self.Canvas_Set = Canvas(self.Frame_Sets, width=1220, height=100)

        self.ScrollBar_Frame = ttk.Scrollbar(self.Frame_Sets, orient="vertical", command=self.Canvas_Set.yview)

        self.Canvas_Set.configure(yscrollcommand=self.ScrollBar_Frame.set)

        self.Content_Frame_Sets = Frame(self.Canvas_Set, width=1240 , bg="#CDC4FF")

        self.Canvas_Set.create_window((0, 0), window=self.Content_Frame_Sets, anchor="nw")

    def Create_Entry_Widgets(self , Axis_x_title):
        self.Text_Entry_For_Histogram_fi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo histograma fi")
        self.Entry_For_Histogram_fi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_fi)
        
        self.Text_Entry_For_Histogram_hi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo histograma hi")
        self.Entry_For_Histogram_hi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi)
        
        self.Text_Entry_For_Histogram_hi_percent = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo histograma hi%")
        self.Entry_For_Histogram_hi_percent = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi_percent)

        self.Text_Entry_For_Frecuences_Polygon_fi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo poligono frecuencias fi")
        self.Entry_For_Frecuences_Polygon_fi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_fi)
        
        self.Text_Entry_For_Frecuences_Polygon_hi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo poligono frecuencias hi")
        self.Entry_For_Frecuences_Polygon_hi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_hi)
        
        self.Text_Entry_For_Frecuences_Polygon_hi_percent = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo poligono frecuencias hi%")
        self.Entry_For_Frecuences_Polygon_hi_percent = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_hi_percent)

        self.Text_Entry_For_Acumulate_Frecuences_Polygon_Fi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo ojivas Fi")
        self.Entry_For_Acumulate_Frecuences_Polygon_Fi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Fi)

        self.Text_Entry_For_Acumulate_Frecuences_Polygon_Hi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo ojivas Hi")
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Hi)
        
        self.Text_Entry_For_Acumulate_Frecuences_Polygon_Hi_percent = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo ojivas Hi%")
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi_percent = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Hi_percent)

        self.Text_Entry_For_Boxplot = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de cajas")
        self.Entry_For_Boxplot = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Boxplot)

        self.Title_For_Axis_x.set(Axis_x_title)
        self.Text_Entry_For_Axis_x = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo eje x")
        self.Entry_For_Axis_x = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Axis_x)

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
        for dict_with_entry_widgets in self.Dictionary_Entry_Titles_Widgets.values():
            for idx , entry_titles_widget in enumerate(dict_with_entry_widgets.values()):
                entry_titles_widget[0].grid(row=idx*2, column=0, padx=10, pady=10, sticky="w")
                entry_titles_widget[1].grid(row=idx*2, column=1, padx=10, pady=10, sticky="w")

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
        Entry_Widget_For_Export_Graphs_For_Grouped_Data.__init__(self , W_Export_Graph)

    def Create_Widgets(self):
        self.Checkbox_Histogram = Checkbutton(self.W_Export_Graph , text="Exportar Histograma" , font=("Times New Roman" , 13) , variable=self.Checked_Histogram , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Histogram"))
        self.Checkbox_Histogram_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , variable=self.Checked_Histogram_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Histogram" , "fi"))
        self.Checkbox_Histogram_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , variable=self.Checked_Histogram_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Histogram" , "hi"))
        self.Checkbox_Histogram_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Histogram_hi_percent , command=lambda: self.Check_And_Block_Single_Checkbox("Histogram" , "hi_percent"))

        self.Checkbox_Frecuences_Polygon = Checkbutton(self.W_Export_Graph , text="Exportar Poligono de Frecuencias" , font=("Times New Roman" , 13) , variable=self.Checked_Frecuences_Polygon , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Frecuences_Polygon"))
        self.Checkbox_Frecuences_Polygon_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , variable=self.Checked_Frecuences_Polygon_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "fi"))
        self.Checkbox_Frecuences_Polygon_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , variable=self.Checked_Frecuences_Polygon_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "hi"))
        self.Checkbox_Frecuences_Polygon_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Frecuences_Polygon_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "hi_percent"))

        self.Checkbox_Acumulate_Frecuences_Polygon = Checkbutton(self.W_Export_Graph , text="Exportar Poligono de Frecuencias Acumuladas" , font=("Times New Roman" , 13) , variable=self.Checked_Acumulate_Frecuences_Polygon , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Acumulate_Frecuences_Polygon"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Fi = Checkbutton(self.W_Export_Graph , text="Para Fi" , font=("Times New Roman" , 13) , variable=self.Checked_Acumulate_Frecuences_Polygon , command= lambda: self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Fi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi = Checkbutton(self.W_Export_Graph , text="Para Hi" , font=("Times New Roman" , 13) , variable=self.Checked_Acumulate_Frecuences_Polygon , command= lambda: self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Hi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi_percent = Checkbutton(self.W_Export_Graph , text="Para Hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Acumulate_Frecuences_Polygon , command= lambda: self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Hi_percent"))

        self.Checkbox_Boxplot = Checkbutton(self.W_Export_Graph , text="Exportar grafico de cajas" , font=("Times New Roman" , 13) , variable=self.Checked_Step_Chart , command= lambda: self.Check_And_Block_Single_Checkbox("Boxplot" , "All_Data"))

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
    
        self.Create_Entry_Widgets(self.Axis_x_Title)