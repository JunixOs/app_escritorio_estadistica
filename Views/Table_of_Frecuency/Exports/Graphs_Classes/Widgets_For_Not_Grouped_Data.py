import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..' , '..')))

from tkinter import *; from tkinter import ttk

from Views.Table_of_Frecuency.Exports.Graphs_Classes.Handler_Widgets_Export import Handler_Actions

class Entry_Widget_For_Export_Graphs_For_Not_Grouped_Data:
    def __init__(self , W_Export_Graph):
        self.Title_For_Bars_Graph_fi = StringVar(W_Export_Graph)
        self.Title_For_Bars_Graph_hi = StringVar(W_Export_Graph)
        self.Title_For_Bars_Graph_hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Stick_Graph_fi = StringVar(W_Export_Graph)
        self.Title_For_Stick_Graph_hi = StringVar(W_Export_Graph)
        self.Title_For_Stick_Graph_hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Step_Chart_Fi = StringVar(W_Export_Graph)
        self.Title_For_Step_Chart_Hi = StringVar(W_Export_Graph)
        self.Title_For_Step_Chart_Hi_percent = StringVar(W_Export_Graph)

        self.Title_For_Axis_x = StringVar(W_Export_Graph)

        self.Main_Container = Label(W_Export_Graph , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)

        self.Frame_Sets = Frame(W_Export_Graph , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)

        self.Canvas_Set = Canvas(self.Frame_Sets, width=1220, height=100)

        self.ScrollBar_Frame = ttk.Scrollbar(self.Frame_Sets, orient="vertical", command=self.Canvas_Set.yview)

        self.Canvas_Set.configure(yscrollcommand=self.ScrollBar_Frame.set)

        self.Content_Frame_Sets = Frame(self.Canvas_Set, width=1240 , bg="#CDC4FF")

        self.Canvas_Set.create_window((0, 0), window=self.Content_Frame_Sets, anchor="nw")

    def Create_Entry_Widgets(self , Axis_x_title):
        self.Text_Entry_For_Bars_Graph_fi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de barras fi")
        self.Entry_For_Bars_Graph_fi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Bars_Graph_fi)
        
        self.Text_Entry_For_Bars_Graph_hi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de barras hi")
        self.Entry_For_Bars_Graph_hi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Bars_Graph_hi)
        
        self.Text_Entry_For_Bars_Graph_hi_percent = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de barras hi%")
        self.Entry_For_Bars_Graph_hi_percent = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Bars_Graph_hi_percent)

        self.Text_Entry_For_Stick_Graph_fi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de bastones fi")
        self.Entry_For_Stick_Graph_fi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Stick_Graph_fi)
        
        self.Text_Entry_For_Stick_Graph_hi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de bastones hi")
        self.Entry_For_Stick_Graph_hi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Stick_Graph_hi)
        
        self.Text_Entry_For_Stick_Graph_hi_percent = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de bastones hi%")
        self.Entry_For_Stick_Graph_hi_percent = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Stick_Graph_hi_percent)

        self.Text_Entry_For_Step_Chart_Fi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de escalones Fi")
        self.Entry_For_Step_Chart_Fi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Step_Chart_Fi)

        self.Text_Entry_For_Step_Chart_Hi = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de escalones Hi")
        self.Entry_For_Step_Chart_Hi = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Step_Chart_Hi)
        
        self.Text_Entry_For_Step_Chart_Hi_percent = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo grafico de escalones Hi%")
        self.Entry_For_Step_Chart_Hi_percent = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Step_Chart_Hi_percent)

        self.Title_For_Axis_x.set(Axis_x_title)
        self.Text_Entry_For_Axis_x = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , text="Titulo eje x")
        self.Entry_For_Axis_x = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Axis_x)

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
        for dict_with_entry_widgets in self.Dictionary_Entry_Titles_Widgets.values():
            for idx , entry_titles_widget in enumerate(dict_with_entry_widgets.values()):
                entry_titles_widget[0].grid(row=idx*2, column=0, padx=10, pady=10, sticky="w")
                entry_titles_widget[1].grid(row=idx*2, column=1, padx=10, pady=10, sticky="w")

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
        Entry_Widget_For_Export_Graphs_For_Not_Grouped_Data.__init__(self , W_Export_Graph)

    def Create_Widgets(self):
        self.Checkbox_Bars_Graph = Checkbutton(self.W_Export_Graph , text="Exportar graficos de barras" , font=("Times New Roman" , 13) , variable=self.Checked_Bars_Graph , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Bars_Graph"))
        self.Checkbox_Bars_Graph_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , variable=self.Checked_Bars_Graph_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Bars_Graph" , "fi"))
        self.Checkbox_Bars_Graph_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , variable=self.Checked_Bars_Graph_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Bars_Graph" , "hi"))
        self.Checkbox_Bars_Graph_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Bars_Graph_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Bars_Graph" , "hi_percent"))

        self.Checkbox_Stick_Graph = Checkbutton(self.W_Export_Graph , text="Exportar graficos de bastones" , font=("Times New Roman" , 13) , variable=self.Checked_Stick_Graph , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Stick_Graph"))
        self.Checkbox_Stick_Graph_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , variable=self.Checked_Stick_Graph_fi , command= lambda: self.Check_And_Block_Single_Checkbox("Stick_Graph" , "fi"))
        self.Checkbox_Stick_Graph_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , variable=self.Checked_Stick_Graph_hi , command= lambda: self.Check_And_Block_Single_Checkbox("Stick_Graph" , "hi"))
        self.Checkbox_Stick_Graph_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Stick_Graph_hi_percent , command= lambda: self.Check_And_Block_Single_Checkbox("Stick_Graph" , "hi_percent"))

        self.Checkbox_Step_Chart = Checkbutton(self.W_Export_Graph , text="Exportar graficos de escalones" , font=("Times New Roman" , 13) , variable=self.Checked_Step_Chart , command= lambda: self.Check_And_Block_Multiple_Checkboxes("Step_Chart"))
        self.Checkbox_Step_Chart_Fi = Checkbutton(self.W_Export_Graph , text="Para Fi" , font=("Times New Roman" , 13) , variable=self.Checked_Step_Chart , command= lambda: self.Check_And_Block_Single_Checkbox("Step_Chart" , "Fi"))
        self.Checkbox_Step_Chart_Hi = Checkbutton(self.W_Export_Graph , text="Para Hi" , font=("Times New Roman" , 13) , variable=self.Checked_Step_Chart , command= lambda: self.Check_And_Block_Single_Checkbox("Step_Chart" , "Hi"))
        self.Checkbox_Step_Chart_Hi_percent = Checkbutton(self.W_Export_Graph , text="Para Hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Step_Chart , command= lambda: self.Check_And_Block_Single_Checkbox("Step_Chart" , "Hi_percent"))

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
    
        self.Create_Entry_Widgets(self.Axis_x_Title)