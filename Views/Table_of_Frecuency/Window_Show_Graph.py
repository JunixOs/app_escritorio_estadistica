import sys
import os
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Tools import Get_Resource_Path
from Calcs.Table_of_Frecuency.Graphs.Draw_Graphs import Manage_All_Graphs_Draw
from Views.Table_of_Frecuency.Exports.Window_Export_Graph import Create_Windows_Export_Graphs
from Window_Create_Multiple_Graphs import Create_Window_Multiple_Graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Checkboxes_For_Grouped_Data:
    def __init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , For_Multiple_Variables):

        self.W_Show_Graph = W_Show_Graph

        self.Results_From_Calcs = Results_From_Calcs
        self.For_Multiple_Variables = For_Multiple_Variables
        self.Axis_x_Title = Axis_x_Title

        self.Checked_Histogram = BooleanVar(self.W_Show_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Graph = BooleanVar(self.W_Show_Graph)
        self.Checked_Frecuences_Polygon_Graph = BooleanVar(self.W_Show_Graph)

        self.Dictionary_Of_Generated_Graphs = {}
        self.Dictionary_Of_Generated_Widgets = {}
        
        self.Class_Generator_Of_Graphs = None

    def Get_Dictionary_Of_Graphs(self):
        return self.Dictionary_Of_Graphs

    def Generate_Widgets(self , Name_Graph):
        if(not self.Dictionary_Of_Generated_Widgets[Name_Graph]):
            Widget_Figure = FigureCanvasTkAgg(self.Dictionary_Of_Generated_Graphs[Name_Graph] , master=self.W_Show_Graph)
            Widget_Figure.draw()
            self.Dictionary_Of_Generated_Widgets[Name_Graph] = Widget_Figure

    def Generate_Graphs(self , Checkbox_Graph):
        Manage_All_Graphs_Draw(
            self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Graphs , self.Class_Generator_Of_Graphs ,
            Checkbox_Graph
        )

    def Only_Check_Single_Option(self , Name_Graph):
        if(self.Dictionary_Checkboxes_Values):
            for key , check in self.Dictionary_Checkboxes_Values.items():
                if(key != Name_Graph):
                    check.set(False)
            self.Generate_Graphs([f"{Name_Graph}" , self.Dictionary_Checkboxes_Values[Name_Graph]])
            self.Generate_Widgets(Name_Graph)
            self.Display_Widgets_Graphs(Name_Graph)

    def Generate_Checkboxes(self):
        self.Checkbox_Histogram = Checkbutton(self.W_Show_Graph , text="Histograma" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Histogram ,  command= lambda: self.Only_Check_Single_Option("Histogram"))
        self.Checkbox_Frecuences_Polygon_Graph = Checkbutton(self.W_Show_Graph , text="Poligono de Frecuencias Acumuladas" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Frecuences_Polygon_Graph ,  command= lambda: self.Only_Check_Single_Option("Frecuences_Polygon_Graph"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Graph = Checkbutton(self.W_Show_Graph , text="Poligono de Frecuencias" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Acumulate_Frecuences_Polygon_Graph ,  command= lambda: self.Only_Check_Single_Option("Acumulate_Frecuences_Polygon_Graph"))

        self.Dictionary_Checkboxes_Values = dict([
            ("Histogram" , self.Checked_Histogram),
            ("Frecuences_Polygon_Graph" , self.Checked_Frecuences_Polygon_Graph),
            ("Acumulate_Frecuences_Polygon_Graph" , self.Checked_Acumulate_Frecuences_Polygon_Graph),
        ])

    def Display_Widgets_Graphs(self , Name_Graph):
        self.Hidden_Widgets_Graphs()

        if(self.Dictionary_Checkboxes_Values[Name_Graph].get()):
            self.Dictionary_Of_Generated_Widgets[Name_Graph].get_tk_widget().place(x=320 , y=0)
    
    def Hidden_Widgets_Graphs(self):
        if(self.Dictionary_Of_Generated_Widgets):
            for widget in self.Dictionary_Of_Generated_Widgets.values():
                widget.get_tk_widget().place_forget()
    
    def Display_Checkboxes(self):
        self.Checkbox_Histogram.place(x=60 , y=220)
        self.Checkbox_Frecuences_Polygon_Graph.place(x=60 , y=260)
        self.Checkbox_Acumulate_Frecuences_Polygon_Graph.place(x=60 , y=300)

    def Hidden_Checkboxes(self):
        self.Checkbox_Histogram.place_forget()
        self.Checkbox_Frecuences_Polygon_Graph.place_forget()
        self.Checkbox_Acumulate_Frecuences_Polygon_Graph.place_forget()

class Checkboxes_For_Not_Grouped_Data:
    def __init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , For_Multiple_Variables):

        self.W_Show_Graph = W_Show_Graph

        self.Results_From_Calcs = Results_From_Calcs
        self.For_Multiple_Variables = For_Multiple_Variables
        self.Axis_x_Title = Axis_x_Title

        self.Checked_Bars_Graph = BooleanVar(self.W_Show_Graph)
        self.Checked_Bars_Graph_fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Bars_Graph_hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Bars_Graph_hi_percent = BooleanVar(self.W_Show_Graph)

        self.Checked_Stick_Graph = BooleanVar(self.W_Show_Graph)
        self.Checked_Stick_Graph_fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Stick_Graph_hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Stick_Graph_hi_percent = BooleanVar(self.W_Show_Graph)

        self.Checked_Step_Chart = BooleanVar(self.W_Show_Graph)
        self.Checked_Step_Chart_fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Step_Chart_hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Step_Chart_hi_percent = BooleanVar(self.W_Show_Graph)

        self.Checked_Acumulate_Frecuences_Polygon_Graph = BooleanVar(self.W_Show_Graph)
        self.Checked_Frecuences_Polygon_Graph = BooleanVar(self.W_Show_Graph)

        self.Dictionary_Of_Generated_Graphs = {
            "Figure_Bars_Graph": {},
            "Figure_Stick_Graph": {},
            "Figure_Step_Chart": {},
        }
        self.Dictionary_Of_Generated_Widgets = {
            "Widget_Bars_Graph": {},
            "Widget_Stick_Graph": {},
            "Widget_Step_Chart": {},
        }
        
        self.Class_Generator_Of_Graphs = None

    def Get_Dictionary_Of_Graphs(self):
        return self.Dictionary_Of_Graphs

    def Generate_Widgets(self , Category_Graph , Name_Graph):
        if(Name_Graph in self.Dictionary_Of_Generated_Widgets[Category_Graph]):
            Widget_Figure = FigureCanvasTkAgg(self.Dictionary_Of_Generated_Graphs[f"Figure_{Category_Graph}"][f"Figure_{Name_Graph}"] , master=self.W_Show_Graph)
            Widget_Figure.draw()
            self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"][f"Widget_{Name_Graph}"] = Widget_Figure

    def Generate_Graphs(self , Checkbox_Graph , Variable_Of_Frecuency):
        Manage_All_Graphs_Draw(
            self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Graphs , self.Class_Generator_Of_Graphs ,
            Checkbox_Graph , Variable_Of_Frecuency
        )

    def Only_Check_Single_Option_SubCheckboxes(self , Name_Graph , Variable_Of_Frecuency , Category_Graph):
        for key , value in self.Dictionary_Checkboxes_Values.items():
            if(key == Category_Graph):
                for name_graph , checkbox_value in value.items():
                    if(name_graph != Name_Graph):
                        checkbox_value.set(False)
            self.Generate_Graphs([f"{Name_Graph}" , self.Dictionary_Checkboxes_Values[Name_Graph]] , Variable_Of_Frecuency)
            self.Generate_Widgets(Name_Graph)
            self.Diplay_Widgets_Graphs(Category_Graph , Name_Graph)

    def Block_Or_Activate_Checkboxes(self , Category):
        for category_name , main_checked , main_checkbox_widget , checked_subwidget_dict , checkbox_subwidget_dict in zip(self.Dictionary_Main_Checkboxes_Values.items() , self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_Checkboxes_Values.values() , self.Dictionary_Checkboxes_Widgets.values()):
            if(category_name != Category and self.Dictionary_Main_Checkboxes_Values[Category].get()):
                main_checked.set(False)
                main_checkbox_widget.config(state="disabled")

                for checked_subwidget , checkbox_subwidget in checked_subwidget_dict , checkbox_subwidget_dict:
                    checked_subwidget.set(False)
                    checkbox_subwidget.config(state="disabled")

            elif(category_name != Category):
                main_checked.set(False)
                main_checkbox_widget.config(state="normal")

                for checked_subwidget , checkbox_subwidget in checked_subwidget_dict , checkbox_subwidget_dict:
                    checked_subwidget.set(False)
                    checkbox_subwidget.config(state="normal")

        self.Hidden_Widgets_Graphs(Category)

    def Generate_Checkboxes(self):
        self.Checkbox_Bars_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de Barras" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checkbox_Bars_Graph ,  command= lambda: self.Block_Or_Activate_Checkboxes("Bars_Graph"))
        self.Checkbox_Bars_Graph_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph_fi , command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Step_Chart_fi" , "fi" , "Step_Chart"))
        self.Checkbox_Bars_Graph_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph_hi , command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Step_Chart_hi" , "hi" , "Step_Chart"))
        self.Checkbox_Bars_Graph_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph_hi_percent , command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Step_Chart_hi" , "hi" , "Step_Chart"))

        self.Checkbox_Stick_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de Bastones" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checkbox_Bars_Graph ,  command= lambda: self.Block_Or_Activate_Checkboxes("Stick_Graph"))
        self.Checkbox_Stick_Graph_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checkbox_Bars_Graph ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Stick_Graph_fi" , "fi" , "Stick_Graph"))
        self.Checkbox_Stick_Graph_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checkbox_Bars_Graph ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Stick_Graph_hi" , "hi" , "Stick_Graph"))
        self.Checkbox_Stick_Graph_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checkbox_Bars_Graph ,  command= lambda: self.Only_Check_Single_Option("Stick_Graph_hi_percent" , "hi_percent" , "Stick_Graph"))

        self.Checkbox_Step_Chart = Checkbutton(self.W_Show_Graph , text="Grafico de Escalones" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart ,  command= lambda: self.Block_Or_Activate_Checkboxes("Step_Chart"))
        self.Checkbox_Step_Chart_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart_fi ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Step_Chart_fi" , "fi" , "Step_Chart"))
        self.Checkbox_Step_Chart_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart_hi ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Step_Chart_hi" , "hi" , "Step_Chart"))
        self.Checkbox_Step_Chart_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart_hi_percent ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Step_Chart_hi_percent" , "hi_percent" , "Step_Chart"))

        self.Dictionary_Checkboxes_Widgets = {
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
                "Step_Chart_fi": self.Checkbox_Step_Chart_fi,
                "Step_Chart_hi": self.Checkbox_Step_Chart_hi,
                "Step_Chart_hi_percent": self.Checkbox_Step_Chart_hi_percent,
            },
        }

        self.Dictionary_Checkboxes_Values = {
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
                "Step_Chart_fi": self.Checked_Step_Chart_fi,
                "Step_Chart_hi": self.Checked_Step_Chart_hi,
                "Step_Chart_hi_percent": self.Checked_Step_Chart_hi_percent,
            },
        }
        self.Dictionary_Main_Checkboxes_Values = {
            "Bars_Graph": self.Checked_Bars_Graph,
            "Stick_Graph": self.Checked_Stick_Graph,
            "Step_Chart": self.Checked_Stick_Graph,
        }

        self.Dictionary_Main_Checkboxes_Widgets = {
            "Bars_Graph": self.Checkbox_Bars_Graph,
            "Stick_Graph": self.Checkbox_Stick_Graph,
            "Step_Chart": self.Checkbox_Step_Chart,
        }

    def Diplay_Widgets_Graphs(self , Category_Graph , Name_Graph):
        if(self.Dictionary_Checkboxes_Values[Category_Graph][Name_Graph].get()):
            self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"][f"Widget_{Name_Graph}"].get_tk_widget().place(x=320 , y=0)

    def Hidden_Widgets_Graphs(self):
        if(self.Dictionary_Of_Generated_Widgets):
            for dict_with_graphs in self.Dictionary_Of_Generated_Widgets.values():
                for widget in dict_with_graphs.values():
                    widget.get_tk_widget().place_forget()

    def Display_Checkboxes(self):
        for i , subwidgets_dict in self.Dictionary_Checkboxes_Values.values():

            self.Checkbox_Histogram.place(x=60 , y=220)
            self.Checkbox_Frecuences_Polygon_Graph.place(x=60 , y=260)
            self.Checkbox_Acumulate_Frecuences_Polygon_Graph.place(x=60 , y=300)

    def Hidden_Checkboxes(self):
        self.Checkbox_Histogram.place_forget()
        self.Checkbox_Frecuences_Polygon_Graph.place_forget()
        self.Checkbox_Acumulate_Frecuences_Polygon_Graph.place_forget()

class Widgets_For_Graphs:
    def __init__(self , W_Show_Graph , Graphs , Variable_Name , For_Multiple_Columns):
        self.W_Show_Graph = W_Show_Graph
        self.Graphs = Graphs
        self.Variable_Name = Variable_Name
        self.For_Multiple_Columns = For_Multiple_Columns

    def Generate_Widgets(self , Widgets_Collection):
        if(self.Graphs):
            Widget_bar_fi = FigureCanvasTkAgg(self.Graphs["bar_fi"] , master=self.W_Show_Graph)
            Widget_bar_fi.draw()
            Widget_bar_hi = FigureCanvasTkAgg(self.Graphs["bar_hi"] , master=self.W_Show_Graph)
            Widget_bar_hi.draw()
            Widget_bar_hi_percent = FigureCanvasTkAgg(self.Graphs["bar_hi_percent"] , master=self.W_Show_Graph)
            Widget_bar_hi_percent.draw()
            Widget_pie_graph = FigureCanvasTkAgg(self.Graphs["pie_graph"] , master=self.W_Show_Graph)
            Widget_pie_graph.draw()

            Widget_boxplot_graph = None
            if("boxplot_graph" in self.Graphs):
                Widget_boxplot_graph = FigureCanvasTkAgg(self.Graphs["boxplot_graph"] , master=self.W_Show_Graph)
                Widget_boxplot_graph.draw()
            
            if(self.For_Multiple_Columns):
                if(Widget_boxplot_graph):
                    Widgets_Collection[f"{self.Variable_Name}"] = {
                        "bar_fi" : Widget_bar_fi,
                        "bar_hi" : Widget_bar_hi,
                        "bar_hi_percent" : Widget_bar_hi_percent,
                        "pie_graph" : Widget_pie_graph,
                        "boxplot_graph" : Widget_boxplot_graph,
                    }
                else:
                    Widgets_Collection[f"{self.Variable_Name}"] = {
                        "bar_fi" : Widget_bar_fi,
                        "bar_hi" : Widget_bar_hi,
                        "bar_hi_percent" : Widget_bar_hi_percent,
                        "pie_graph" : Widget_pie_graph,
                    }
            else:
                Widgets_Collection["bar_fi"] = Widget_bar_fi
                Widgets_Collection["bar_hi"] = Widget_bar_hi
                Widgets_Collection["bar_hi_percent"] = Widget_bar_hi_percent
                Widgets_Collection["pie_graph"] = Widget_pie_graph

                if(Widget_boxplot_graph):
                    Widgets_Collection["boxplot_graph"] = Widget_boxplot_graph

class Graphs_For_Frecuences:
    def __init__(self , Results , Precision , Variable_Name , For_Multiple_Columns):
        self.Results = Results
        self.Precision = Precision
        self.Variable_Name = Variable_Name
        self.For_Multiple_Columns = For_Multiple_Columns

    def Modify_Intervals_Key(self):
        if("Frecuences_Cuant_Grouped" in self.Results):
            for a in range(0 , len(self.Results["Frecuences_Cuant_Grouped"]["Intervals"])):
                self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a] = "[ " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][0]) +" , " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][1]) +" >"

                # Lo de abajo servia cuando el limite superior del ultimo intervalo si se tomaba 
                """ if(a != len(self.Results["Frecuences_Cuant_Grouped"]["Intervals"]) - 1):
                    self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a] = "[ " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][0]) +" , " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][1]) +" >"
                else:
                    self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a] = "[ " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][0]) +" , " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][1]) +" ]" """

    def Generate_Graphs(self , Graphs):
        self.Modify_Intervals_Key()

        Graph = Draw_Graph_for_Each_Variable(self.Results , self.Precision , self.Variable_Name)

        bar_fi , pie_graph = Graph.Draw_Graph("fi")
        bar_hi = Graph.Draw_Graph("hi")
        bar_hi_percent = Graph.Draw_Graph("hi_percent")
        boxplot_graph = None

        if("Frecuences_Cuant_Grouped" in self.Results):
            boxplot_graph = Draw_Boxplot_For_Single_Column_Data(self.Results["Variables_Cuant_Grouped"]["Data_List"] , self.Variable_Name)

        elif("Frecuences_Cuant_Not_Grouped" in self.Results):
            boxplot_graph = Draw_Boxplot_For_Single_Column_Data(self.Results["Variables_Cuant_Not_Grouped"]["Data_List"] , self.Variable_Name)
        
        if(self.For_Multiple_Columns):
            if(boxplot_graph):
                Graphs[f"{self.Variable_Name}"] = {
                    "bar_fi" : bar_fi,
                    "bar_hi" : bar_hi,
                    "bar_hi_percent" : bar_hi_percent,
                    "pie_graph" : pie_graph,
                    "boxplot_graph" : boxplot_graph,
                }
            else:
                Graphs[f"{self.Variable_Name}"] = {
                    "bar_fi" : bar_fi,
                    "bar_hi" : bar_hi,
                    "bar_hi_percent" : bar_hi_percent,
                    "pie_graph" : pie_graph,
                }
        else:
            Graphs["bar_fi"] = bar_fi
            Graphs["bar_hi"] = bar_hi
            Graphs["bar_hi_percent"] = bar_hi_percent
            Graphs["pie_graph"] = pie_graph

            if(boxplot_graph):
                Graphs["boxplot_graph"] = boxplot_graph

class Checkboxes_Selection_Graphs:
    def __init__(self , W_Show_Graph , There_Are_Boxplot , Widgets):
        self.W_Show_Graph = W_Show_Graph
        self.There_Are_Boxplot = There_Are_Boxplot
        self.Widgets = Widgets

        self.Checked_Bar_fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Bar_hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Bar_hi_percent = BooleanVar(self.W_Show_Graph)

        self.Checked_Pie_Graph = BooleanVar(self.W_Show_Graph)
        self.Checked_Boxplot_Graph = BooleanVar(self.W_Show_Graph)
        self.Checked_Boxplot_Graph.set(False)
        self.Dictionary_Checkboxes_Values = {}

    def Hidden_Widgets_Graphs(self):
        if(self.Widgets):
            for widget in self.Widgets.values():
                widget.get_tk_widget().place_forget()

    def Diplay_Widgets_Graphs(self):
        self.Hidden_Widgets_Graphs()

        if(self.Checked_Bar_fi.get()):
            self.Widgets["bar_fi"].get_tk_widget().place(x=320 , y=0)
        elif(self.Checked_Bar_hi.get()):
            self.Widgets["bar_hi"].get_tk_widget().place(x=320 , y=0)
        elif(self.Checked_Bar_hi_percent.get()):
            self.Widgets["bar_hi_percent"].get_tk_widget().place(x=320 , y=0)
        elif(self.Checked_Pie_Graph.get()):
            self.Widgets["pie_graph"].get_tk_widget().place(x=320 , y=0)
        elif(self.Checked_Boxplot_Graph.get()):
            self.Widgets["boxplot_graph"].get_tk_widget().place(x=320 , y=0)


    def Only_Check_Single_Option(self , Name_Graph):
        if(self.Dictionary_Checkboxes_Values):
            for key , check in self.Dictionary_Checkboxes_Values.items():
                if(key != Name_Graph):
                    check.set(False)
            self.Diplay_Widgets_Graphs()

    def Generate_Checkboxes(self):
        self.Checkbox_Show_Bar_fi = Checkbutton(self.W_Show_Graph , text="Grafico para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bar_fi ,  command= lambda: self.Only_Check_Single_Option("fi"))
        self.Checkbox_Show_Bar_hi = Checkbutton(self.W_Show_Graph , text="Grafico para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bar_hi , command= lambda: self.Only_Check_Single_Option("hi"))
        self.Checkbox_Show_Bar_hi_percent = Checkbutton(self.W_Show_Graph , text="Grafico para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bar_hi_percent , command= lambda: self.Only_Check_Single_Option("hi_percent"))

        self.Checkbox_Pie_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de pastel" , font=("Times New Roman" , 13) , bg="#F8D9AB" ,  variable=self.Checked_Pie_Graph , command= lambda: self.Only_Check_Single_Option("pie"))

        self.Checkbox_Boxplot_Graph = None
        if(self.There_Are_Boxplot):
            self.Checkbox_Boxplot_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de cajas" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Boxplot_Graph , command= lambda: self.Only_Check_Single_Option("boxplot"))

        self.Dictionary_Checkboxes_Values = dict([
            ("fi" , self.Checked_Bar_fi),
            ("hi" , self.Checked_Bar_hi),
            ("hi_percent" , self.Checked_Bar_hi_percent),
            ("pie" , self.Checked_Pie_Graph),
            ("boxplot" , self.Checked_Boxplot_Graph),
        ])

    def Display_Checkboxes(self):
        self.Checkbox_Show_Bar_fi.place(x=60 , y=220)
        self.Checkbox_Show_Bar_hi.place(x=60 , y=260)
        self.Checkbox_Show_Bar_hi_percent.place(x=60 , y=300)
        self.Checkbox_Pie_Graph.place(x=60 , y=340)

        if(self.Checkbox_Boxplot_Graph):
            self.Checkbox_Boxplot_Graph.place(x=60 , y=380)

    def Hidden_Checkboxes(self):
        self.Checkbox_Show_Bar_fi.place_forget()
        self.Checkbox_Show_Bar_hi.place_forget()
        self.Checkbox_Show_Bar_hi_percent.place_forget()
        self.Checkbox_Pie_Graph.place_forget()

        if(self.Checkbox_Boxplot_Graph):
            self.Checkbox_Boxplot_Graph.place_forget()

def Create_Window_Show_Graph(W_Calc_Frecuences_Table , Results_From_Single_Column , Results_From_Multiple_Columns , Precision , Graphs):
    def Back(W_Show_Graph):
        if(Results_From_Single_Column):
            if(len(Results_From_Single_Column) == 1):
                var_name , value = next(iter(Results_From_Single_Column.items()))
                if("Frecuences_Cuant_Grouped" in value or "Frecuences_Cuant_Not_Grouped" in value):
                    Graphs.clear()
                
            elif("Frecuences_Cuant_Grouped" in Results_From_Single_Column or "Frecuences_Cuant_Not_Grouped" in Results_From_Single_Column):
                Graphs.clear()

        elif(Results_From_Multiple_Columns):
            for var_name , value in Results_From_Multiple_Columns.items():
                if("Frecuences_Cuant_Grouped" in value or "Frecuences_Cuant_Not_Grouped" in value):
                    Graphs[f"{var_name}"].clear()

        Widgets_Collection.clear()
        Checkboxes_Collection.clear()
        W_Show_Graph.grab_release()
        for widget in W_Show_Graph.winfo_children():
            widget.destroy()
    
        W_Show_Graph.quit()
        W_Show_Graph.destroy()

    def Change_To_Different_Variable_Graph(Event = None):
        if(Checkboxes_Collection):
            Selection = Column_Select.get()
            for check in Checkboxes_Collection.values():
                check.Hidden_Checkboxes()
                check.Hidden_Widgets_Graphs()

            Checkboxes_Collection[f"{Selection}"].Display_Checkboxes()
            Checkboxes_Collection[f"{Selection}"].Diplay_Widgets_Graphs()

    W_Show_Graph = Toplevel(W_Calc_Frecuences_Table)
    W_Show_Graph.title("Ver graficos")
    W_Show_Graph.geometry("1300x700+105+105")
    W_Show_Graph.grab_set()
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
    W_Show_Graph.iconphoto(False , Icon)
    W_Show_Graph.config(bg="#F8D9AB")

    Widgets_Collection = {}
    Checkboxes_Collection = {}

    W_Show_Graph.protocol("WM_DELETE_WINDOW", lambda: Back(W_Show_Graph))

    Section_Graphs = Label(W_Show_Graph , bg="#ffffff" , text="Selecciona un grafico y se mostrara aqui" , font=("Times New Roman" , 13) , anchor="center")
    Section_Graphs.place(x=320 , y=0 , width=980 , height=700)

    Column_Name = []
    Column_Select = ttk.Combobox(W_Show_Graph , values=Column_Name , font=("Courier New" , 13) , width=25 , state="readonly")

    if(Precision > 3):
        Precision = 3

    try:
        if(Results_From_Single_Column):
            Gen_Graphs = None
            Gen_Widgets = None
            Results = copy.deepcopy(Results_From_Single_Column)

            if(not Graphs):
                if(len(Results) == 1):
                    key , value = next(iter(Results.items()))
                    Gen_Graphs = Graphs_For_Frecuences(value , Precision , key , False)
                else:
                    Gen_Graphs = Graphs_For_Frecuences(Results , Precision , None , False)
                Gen_Graphs.Generate_Graphs(Graphs)

            Gen_Widgets = Widgets_For_Graphs(W_Show_Graph , Graphs , None , False)
            Gen_Widgets.Generate_Widgets(Widgets_Collection)

            There_Are_Boxplot = "boxplot_graph" in Graphs

            Checkboxes = Checkboxes_Selection_Graphs(W_Show_Graph , There_Are_Boxplot , Widgets_Collection)
            Checkboxes.Generate_Checkboxes()
            Checkboxes.Display_Checkboxes()

        elif(Results_From_Multiple_Columns):
            Results = copy.deepcopy(Results_From_Multiple_Columns)

            if(Graphs):
                There_Are_Graphics = [True if val else False for val in Graphs.values()]
            else:
                There_Are_Graphics = False

            for i , (key , value) in enumerate(Results.items()):
                Gen_Graphs = None
                Gen_Widgets = None

                match(isinstance(There_Are_Graphics , list)):
                    case True:
                        if(not There_Are_Graphics[i]):
                            Gen_Graphs = Graphs_For_Frecuences(value , Precision , key , True)
                            Gen_Graphs.Generate_Graphs(Graphs)
                    case False:
                        if(not There_Are_Graphics):
                            Gen_Graphs = Graphs_For_Frecuences(value , Precision , key , True)
                            Gen_Graphs.Generate_Graphs(Graphs)

                Gen_Widgets = Widgets_For_Graphs(W_Show_Graph , Graphs[f"{key}"] , key , True)
                Gen_Widgets.Generate_Widgets(Widgets_Collection)

                There_Are_Boxplot = "boxplot_graph" in Graphs[f"{key}"]

                Checkboxes = Checkboxes_Selection_Graphs(W_Show_Graph , There_Are_Boxplot , Widgets_Collection[f"{key}"])
                Checkboxes.Generate_Checkboxes()

                Checkboxes_Collection[f"{key}"] = Checkboxes

                Column_Name.append(key)

            Column_Select["values"] = Column_Name
            Column_Select.set(Column_Name[0])
            Column_Select.place(x=20 , y=50)
            Column_Select.bind('<<ComboboxSelected>>' , Change_To_Different_Variable_Graph)

            Change_To_Different_Variable_Graph()

        else:
            raise Exception("No se encontraron los datos necesarios para generar los graficos.")

    except Exception as e:
        messagebox.showerror("Error" , f"{e}")

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar graficos" , font=("Times New Roman" , 13) , width=15 , bg="#FDA8C0" , command= lambda: Create_Windows_Export_Graphs(W_Show_Graph , Graphs , Results_From_Single_Column , Results_From_Multiple_Columns))
    Btn_Export_Graph.place(x=90 , y=480)

    """ Btn_Create_And_Export_Multiple_Graphs = Button(W_Show_Graph , text="Crear y Exportar\nMultiples Graficos" , font=("Times New Roman" , 13) , width=24  , bg="#FDA8C0" , justify="center" , command= lambda: Create_Window_Multiple_Graphs(W_Show_Graph))
    Btn_Create_And_Export_Multiple_Graphs.place(x=50 , y=560) """

    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()