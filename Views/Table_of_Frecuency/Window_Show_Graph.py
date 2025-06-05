import sys
import os
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Tools import Get_Resource_Path , Get_Number_Of_Util_Threads_In_Device , Delete_Actual_Window
from Calcs.Table_of_Frecuency.Graphs.Draw_Graphs import Manage_All_Graphs_Draw
from Views.Table_of_Frecuency.Exports.Window_Export_Graph import Create_Windows_Export_Graphs
from Window_Create_Multiple_Graphs import Create_Window_Multiple_Graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Window_Progress_Bar import W_Progress_Bar

import threading

def Check_Threads_Alive(Threads_List , W_Show_Graph, Class_Progress_Bar):
    # Verifica si todos los hilos terminaron
    alive_states = [t.is_alive() for t in Threads_List]
    print(f"Hilos vivos: {alive_states}")
    if all(not t.is_alive() for t in Threads_List):
        print("Todos los hilos terminaron")
        Class_Progress_Bar.Close_Progress_Bar()
    else:
        W_Show_Graph.after(500, Check_Threads_Alive, Threads_List, W_Show_Graph, Class_Progress_Bar)

def Generate_Graph_With_One_Or_Any_Thread(Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures , Class_Generator_Of_Graphs , Info_For_Graphs , W_Show_Graph , Class_Progress_Bar):
    for category_graph , variable_frecuency_list in Info_For_Graphs.items():
        Manage_All_Graphs_Draw(Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures , Class_Generator_Of_Graphs , category_graph , variable_frecuency_list , None , None , W_Show_Graph , Class_Progress_Bar)

def Change_Key_From_Intervals_List(Results_From_Calcs):
    Intervals_Formatted = []
    for a in range(0 , len(Results_From_Calcs["Frecuences_Cuant_Grouped"]["Intervals"])):
        Intervals_Formatted.append("[ " + str(Results_From_Calcs["Frecuences_Cuant_Grouped"]["Intervals"][a][0]) +" , " + str(Results_From_Calcs["Frecuences_Cuant_Grouped"]["Intervals"][a][1]) +" >")

        # Lo de abajo servia cuando el limite superior del ultimo intervalo si se tomaba 
        """ if(a != len(self.Results["Frecuences_Cuant_Grouped"]["Intervals"]) - 1):
            self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a] = "[ " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][0]) +" , " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][1]) +" >"
        else:
            self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a] = "[ " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][0]) +" , " + str(self.Results["Frecuences_Cuant_Grouped"]["Intervals"][a][1]) +" ]" """
    return Intervals_Formatted

class Counter_For_Threads:
    def __init__(self , Lock):
        self.Lock = Lock
        self.Value = 0
    def Increment(self):
        with self.Lock:
            self.Value += 1
            print(f"Nuevo valor: {self.Value}")
    def __repr__(self):
            return f"<Counter_For_Threads Value={self.Value}>"
class Checkboxes_For_Grouped_Data:
    def __init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures):

        self.W_Show_Graph = W_Show_Graph

        self.Results_From_Calcs = Results_From_Calcs
        self.Axis_x_Title = Axis_x_Title

        self.Checked_Histogram = BooleanVar(self.W_Show_Graph)
        self.Checked_Histogram_fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Histogram_hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Histogram_hi_percent = BooleanVar(self.W_Show_Graph)

        self.Checked_Frecuences_Polygon = BooleanVar(self.W_Show_Graph)
        self.Checked_Frecuences_Polygon_fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Frecuences_Polygon_hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Frecuences_Polygon_hi_percent = BooleanVar(self.W_Show_Graph)

        self.Checked_Acumulate_Frecuences_Polygon = BooleanVar(self.W_Show_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Acumulate_Frecuences_Polygon_Hi_percent = BooleanVar(self.W_Show_Graph)


        if(Dictionary_Of_Generated_Figures):
            self.Dictionary_Of_Generated_Figures = Dictionary_Of_Generated_Figures
        else:
            self.Dictionary_Of_Generated_Figures = {
                "Figure_Histogram": {},
                "Figure_Frecuences_Polygon": {},
                "Figure_Acumulate_Frecuences_Polygon": {}
            }

        self.Dictionary_Of_Generated_Widgets = {
            "Widget_Histogram": {},
            "Widget_Frecuences_Polygon": {},
            "Widget_Acumulate_Frecuences_Polygon": {},
        }
        
        self.Class_Generator_Of_Graphs = []

    def Get_Dictionary_Of_Graphs(self):
        return self.Dictionary_Of_Generated_Figures

    def Generate_Widgets(self , Category_Graph , Variable_Of_Frecuency):
        if(not f"Widget_{Category_Graph}_{Variable_Of_Frecuency}" in self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"]):
            Widget_Figure = FigureCanvasTkAgg(self.Dictionary_Of_Generated_Figures[f"Figure_{Category_Graph}"][f"Figure_{Category_Graph}_{Variable_Of_Frecuency}"] , master=self.W_Show_Graph)
            Widget_Figure.draw()

            self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"][f"Widget_{Category_Graph}_{Variable_Of_Frecuency}"] = Widget_Figure

    def Generate_Graphs(self):
        if(all(list(self.Dictionary_Of_Generated_Figures.values()))):
            return 0

        Info_For_Graphs = {
            "Histogram": ["fi" , "hi" , "hi_percent"] , 
            "Frecuences_Polygon": ["fi" , "hi" , "hi_percent"] , 
            "Acumulate_Frecuences_Polygon": ["Fi" , "Hi" , "Hi_percent"],
        }
        
        Number_Of_Threads = Get_Number_Of_Util_Threads_In_Device()
        Total_Works = 3
        Lock = threading.Lock()
        
        Class_Progress_Bar = W_Progress_Bar(self.W_Show_Graph)
        Class_Progress_Bar.Start_Progress_Bar()

        if(Number_Of_Threads > Total_Works):
            Threads_List = []
            for category_graph , variable_frecuency_list in Info_For_Graphs.items():
                Thread = threading.Thread(target= lambda: Manage_All_Graphs_Draw(self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , category_graph , variable_frecuency_list , None , None))
                Threads_List.append(Thread)
                Thread.start()
            
            self.W_Show_Graph.after(500 , Check_Threads_Alive , Threads_List , self.W_Show_Graph , Class_Progress_Bar)
        elif(Number_Of_Threads > 1):
            threading.Thread(target=Generate_Graph_With_One_Or_Any_Thread , args=(self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , Info_For_Graphs , self.W_Show_Graph , Class_Progress_Bar)).start()
        elif(Number_Of_Threads == 1):
            Generate_Graph_With_One_Or_Any_Thread(self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , Info_For_Graphs)
                        
    def Block_Or_Activate_Checkboxes(self , Category_Graph):
        for category_name , main_checked_values , dict_with_subcheckboxes_values , dict_with_subcheckboxes_widgets in zip(self.Dictionary_Main_Checkboxes_Values.keys() , self.Dictionary_Main_Checkboxes_Values.values() , self.Dictionary_SubCheckboxes_Values.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            if(category_name != Category_Graph or (category_name == Category_Graph and not main_checked_values.get())):
                main_checked_values.set(False)

                for checked_subwidget , checkbox_subwidget in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()):
                    checked_subwidget.set(False)
                    checkbox_subwidget.config(state="disabled")

            else:
                for checked_subwidget , checkbox_subwidget in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()):
                    checked_subwidget.set(False)
                    checkbox_subwidget.config(state="normal")

        self.Hidden_Widgets_Graphs()

    def Only_Check_Single_Option_Subcheckboxes(self , Category_Graph , Variable_Of_Frecuency):
        for category_graph , dict_with_subcheckboxes in self.Dictionary_SubCheckboxes_Values.items():
            if(category_graph == Category_Graph):
                for name_graph , subcheckbox_value in dict_with_subcheckboxes.items():
                    if(name_graph != f"{Category_Graph}_{Variable_Of_Frecuency}"):
                        subcheckbox_value.set(False)

        #self.Generate_Graphs()
        self.Generate_Widgets(Category_Graph , Variable_Of_Frecuency)
        self.Display_Widgets_Graphs(Category_Graph , Variable_Of_Frecuency)

    def Generate_Checkboxes(self):
        self.Checkbox_Histogram = Checkbutton(self.W_Show_Graph , text="Histograma" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Histogram ,  command= lambda: self.Block_Or_Activate_Checkboxes("Histogram"))
        self.Checkbox_Histogram_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Histogram_fi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Histogram" , "fi"))
        self.Checkbox_Histogram_fi.config(state="disabled")
        self.Checkbox_Histogram_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Histogram_hi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Histogram" , "hi"))
        self.Checkbox_Histogram_hi.config(state="disabled")
        self.Checkbox_Histogram_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Histogram_hi_percent ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Histogram" , "hi_percent"))
        self.Checkbox_Histogram_hi_percent.config(state="disabled")

        self.Checkbox_Frecuences_Polygon = Checkbutton(self.W_Show_Graph , text="Poligono de Frecuencias" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Frecuences_Polygon ,  command= lambda: self.Block_Or_Activate_Checkboxes("Frecuences_Polygon"))
        self.Checkbox_Frecuences_Polygon_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Frecuences_Polygon_fi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Frecuences_Polygon" , "fi"))
        self.Checkbox_Frecuences_Polygon_fi.config(state="disabled")
        self.Checkbox_Frecuences_Polygon_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Frecuences_Polygon_hi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Frecuences_Polygon" , "hi"))
        self.Checkbox_Frecuences_Polygon_hi.config(state="disabled")
        self.Checkbox_Frecuences_Polygon_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Frecuences_Polygon_hi_percent ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Frecuences_Polygon" , "hi_percent"))
        self.Checkbox_Frecuences_Polygon_hi_percent.config(state="disabled")

        self.Checkbox_Acumulate_Frecuences_Polygon = Checkbutton(self.W_Show_Graph , text="Poligono de Frecuencias Acumuladas" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Acumulate_Frecuences_Polygon ,  command= lambda: self.Block_Or_Activate_Checkboxes("Acumulate_Frecuences_Polygon"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Fi = Checkbutton(self.W_Show_Graph , text="Para Fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Acumulate_Frecuences_Polygon_Fi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Acumulate_Frecuences_Polygon" , "Fi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Fi.config(state="disabled")
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi = Checkbutton(self.W_Show_Graph , text="Para Hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Acumulate_Frecuences_Polygon_Hi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Acumulate_Frecuences_Polygon" , "Hi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi.config(state="disabled")
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi_percent = Checkbutton(self.W_Show_Graph , text="Para Hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Acumulate_Frecuences_Polygon_Hi_percent ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Acumulate_Frecuences_Polygon" , "Hi_percent"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi_percent.config(state="disabled")

        self.Dictionary_Main_Checkboxes_Widgets = {
            "Histogram": self.Checkbox_Histogram,
            "Frecuences_Polygon": self.Checkbox_Frecuences_Polygon,
            "Acumulate_Frecuences_Polygon": self.Checkbox_Acumulate_Frecuences_Polygon,
        }
        self.Dictionary_Main_Checkboxes_Values = {
            "Histogram": self.Checked_Histogram,
            "Frecuences_Polygon": self.Checked_Frecuences_Polygon,
            "Acumulate_Frecuences_Polygon": self.Checked_Acumulate_Frecuences_Polygon,
        }
        

        self.Dictionary_SubCheckboxes_Widgets = {
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
        }
        self.Dictionary_SubCheckboxes_Values = {
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
        }

    def Display_Widgets_Graphs(self , Category_Graph , Variable_Of_Frecuency):
        self.Hidden_Widgets_Graphs()

        if(self.Dictionary_SubCheckboxes_Values[Category_Graph][f"{Category_Graph}_{Variable_Of_Frecuency}"].get()):
            self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"][f"Widget_{Category_Graph}_{Variable_Of_Frecuency}"].get_tk_widget().place(x=320 , y=0)
    
    def Hidden_Widgets_Graphs(self):
        for dict_with_widgets in self.Dictionary_Of_Generated_Widgets.values():
            for widget in dict_with_widgets.values():
                if(widget):
                    widget.get_tk_widget().place_forget()
    
    def Display_Checkboxes(self):
        start_place = 140
        for main_checkbox , dict_with_subcheckboxes in zip(self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            main_checkbox.place(x=20 , y=start_place)
            for subcheckboxes in dict_with_subcheckboxes.values():
                start_place += 25
                subcheckboxes.place(x=40 , y=start_place)
            start_place += 40

    def Hidden_Checkboxes(self):
        for main_checkbox , dict_with_subcheckboxes in zip(self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            main_checkbox.place_forget()
            for subcheckboxes in dict_with_subcheckboxes.values():
                subcheckboxes.place_forget()

        self.Hidden_Widgets_Graphs()

class Checkboxes_For_Not_Grouped_Data:
    def __init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures):

        self.W_Show_Graph = W_Show_Graph

        self.Results_From_Calcs = Results_From_Calcs
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
        self.Checked_Step_Chart_Fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Step_Chart_Hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Step_Chart_Hi_percent = BooleanVar(self.W_Show_Graph)

        self.Checked_Acumulate_Frecuences_Polygon_Graph = BooleanVar(self.W_Show_Graph)
        self.Checked_Frecuences_Polygon_Graph = BooleanVar(self.W_Show_Graph)

        if(Dictionary_Of_Generated_Figures):
            self.Dictionary_Of_Generated_Figures = Dictionary_Of_Generated_Figures
        else:
            self.Dictionary_Of_Generated_Figures = {
                "Figure_Bars_Graph": {},
                "Figure_Stick_Graph": {},
                "Figure_Step_Chart": {},
            }

        self.Dictionary_Of_Generated_Widgets = {
            "Widget_Bars_Graph": {},
            "Widget_Stick_Graph": {},
            "Widget_Step_Chart": {},
        }
        
        self.Class_Generator_Of_Graphs = []

    def Get_Dictionary_Of_Graphs(self):
        return self.Dictionary_Of_Generated_Figures

    def Generate_Widgets(self , Category_Graph , Variable_Of_Frecuency):
        if(not f"Widget_{Category_Graph}_{Variable_Of_Frecuency}" in self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"]):
            Widget_Figure = FigureCanvasTkAgg(self.Dictionary_Of_Generated_Figures[f"Figure_{Category_Graph}"][f"Figure_{Category_Graph}_{Variable_Of_Frecuency}"] , master=self.W_Show_Graph)
            Widget_Figure.draw()
            self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"][f"Widget_{Category_Graph}_{Variable_Of_Frecuency}"] = Widget_Figure

    def Generate_Graphs(self):
        if(all(list(self.Dictionary_Of_Generated_Figures.values()))):
            return 0

        Info_For_Graphs = {
            "Bars_Graph": ["fi" , "hi" , "hi_percent"],
            "Stick_Graph": ["fi" , "hi" , "hi_percent"],
            "Step_Chart": ["Fi" , "Hi" , "Hi_percent"],
        }
        Number_Of_Threads = Get_Number_Of_Util_Threads_In_Device()
        Total_Works = 3
        Lock = threading.Lock()

        Class_Progress_Bar = W_Progress_Bar(self.W_Show_Graph)
        Class_Progress_Bar.Start_Progress_Bar()

        if(Number_Of_Threads > Total_Works):
            Threads_List = []
            for category_graph , variable_frecuency_list in Info_For_Graphs.items():
                Thread = threading.Thread(target= lambda: Manage_All_Graphs_Draw(self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , category_graph , variable_frecuency_list , None , None))
                Threads_List.append(Thread)
                Thread.start()
            
            self.W_Show_Graph.after(500 , Check_Threads_Alive , Threads_List , self.W_Show_Graph , Class_Progress_Bar)
        elif(Number_Of_Threads > 1):
            threading.Thread(target=Generate_Graph_With_One_Or_Any_Thread , args=(self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , Info_For_Graphs , self.W_Show_Graph , Class_Progress_Bar))
        elif(Number_Of_Threads == 1):
            Generate_Graph_With_One_Or_Any_Thread(self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , Info_For_Graphs)

    def Only_Check_Single_Option_SubCheckboxes(self , Variable_Of_Frecuency , Category_Graph):
        for category_graph , dict_with_subcheckboxes in self.Dictionary_SubCheckboxes_Values.items():
            if(category_graph == Category_Graph):
                for name_graph , subcheckbox_value in dict_with_subcheckboxes.items():
                    if(name_graph != f"{Category_Graph}_{Variable_Of_Frecuency}"):
                        subcheckbox_value.set(False)

        #self.Generate_Graphs()
        self.Generate_Widgets(Category_Graph , Variable_Of_Frecuency)
        self.Display_Widgets_Graphs(Category_Graph , Variable_Of_Frecuency)

    def Block_Or_Activate_Checkboxes(self , Category_Graph):
        for category_name , main_checked_values , dict_with_subcheckboxes_values , dict_with_subcheckboxes_widgets in zip(self.Dictionary_Main_Checkboxes_Values.keys() , self.Dictionary_Main_Checkboxes_Values.values() , self.Dictionary_SubCheckboxes_Values.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            if(category_name != Category_Graph or (category_name == Category_Graph and not main_checked_values.get())):
                main_checked_values.set(False)

                for checked_subwidget , checkbox_subwidget in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()):
                    checked_subwidget.set(False)
                    checkbox_subwidget.config(state="disabled")

            else:
                for checked_subwidget , checkbox_subwidget in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()):
                    checked_subwidget.set(False)
                    checkbox_subwidget.config(state="normal")

        self.Hidden_Widgets_Graphs()

    def Generate_Checkboxes(self):
        self.Checkbox_Bars_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de Barras" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph ,  command= lambda: self.Block_Or_Activate_Checkboxes("Bars_Graph"))
        self.Checkbox_Bars_Graph_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph_fi , command= lambda: self.Only_Check_Single_Option_SubCheckboxes("fi" , "Bars_Graph"))
        self.Checkbox_Bars_Graph_fi.config(state="disabled")
        self.Checkbox_Bars_Graph_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph_hi , command= lambda: self.Only_Check_Single_Option_SubCheckboxes("hi" , "Bars_Graph"))
        self.Checkbox_Bars_Graph_hi.config(state="disabled")
        self.Checkbox_Bars_Graph_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph_hi_percent , command= lambda: self.Only_Check_Single_Option_SubCheckboxes("hi_percent" , "Bars_Graph"))
        self.Checkbox_Bars_Graph_hi_percent.config(state="disabled")

        self.Checkbox_Stick_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de Bastones" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Stick_Graph ,  command= lambda: self.Block_Or_Activate_Checkboxes("Stick_Graph"))
        self.Checkbox_Stick_Graph_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Stick_Graph_fi ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("fi" , "Stick_Graph"))
        self.Checkbox_Stick_Graph_fi.config(state="disabled")
        self.Checkbox_Stick_Graph_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Stick_Graph_hi ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("hi" , "Stick_Graph"))
        self.Checkbox_Stick_Graph_hi.config(state="disabled")
        self.Checkbox_Stick_Graph_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Stick_Graph_hi_percent ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("hi_percent" , "Stick_Graph"))
        self.Checkbox_Stick_Graph_hi_percent.config(state="disabled")

        self.Checkbox_Step_Chart = Checkbutton(self.W_Show_Graph , text="Grafico de Escalones" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart ,  command= lambda: self.Block_Or_Activate_Checkboxes("Step_Chart"))
        self.Checkbox_Step_Chart_Fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart_Fi ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Fi" , "Step_Chart"))
        self.Checkbox_Step_Chart_Fi.config(state="disabled")
        self.Checkbox_Step_Chart_Hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart_Hi ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Hi" , "Step_Chart"))
        self.Checkbox_Step_Chart_Hi.config(state="disabled")
        self.Checkbox_Step_Chart_Hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart_Hi_percent ,  command= lambda: self.Only_Check_Single_Option_SubCheckboxes("Hi_percent" , "Step_Chart"))
        self.Checkbox_Step_Chart_Hi_percent.config(state="disabled")

        self.Dictionary_SubCheckboxes_Widgets = {
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
        self.Dictionary_SubCheckboxes_Values = {
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

        self.Dictionary_Main_Checkboxes_Values = {
            "Bars_Graph": self.Checked_Bars_Graph,
            "Stick_Graph": self.Checked_Stick_Graph,
            "Step_Chart": self.Checked_Step_Chart,
        }
        self.Dictionary_Main_Checkboxes_Widgets = {
            "Bars_Graph": self.Checkbox_Bars_Graph,
            "Stick_Graph": self.Checkbox_Stick_Graph,
            "Step_Chart": self.Checkbox_Step_Chart,
        }

    def Display_Widgets_Graphs(self , Category_Graph , Variable_Of_Frecuency):
        self.Hidden_Widgets_Graphs()

        if(self.Dictionary_SubCheckboxes_Values[Category_Graph][f"{Category_Graph}_{Variable_Of_Frecuency}"].get()):
            self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"][f"Widget_{Category_Graph}_{Variable_Of_Frecuency}"].get_tk_widget().place(x=320 , y=0)

    def Hidden_Widgets_Graphs(self):
        for dict_with_graphs in self.Dictionary_Of_Generated_Widgets.values():
            for widget in dict_with_graphs.values():
                if(widget):
                    widget.get_tk_widget().place_forget()

    def Display_Checkboxes(self):
        start_place = 140
        for main_checkbox , dict_with_subcheckboxes in zip(self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            main_checkbox.place(x=20 , y=start_place)
            for subcheckboxes in dict_with_subcheckboxes.values():
                start_place += 25
                subcheckboxes.place(x=40 , y=start_place)
            start_place += 40

    def Hidden_Checkboxes(self):
        for main_checkbox , dict_with_subcheckboxes in zip(self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            main_checkbox.place_forget()
            for subcheckboxes in dict_with_subcheckboxes.values():
                subcheckboxes.place_forget()

        self.Hidden_Widgets_Graphs()

class Checkboxes_For_Cualitative_Data:
    def __init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures):

        self.W_Show_Graph = W_Show_Graph

        self.Results_From_Calcs = Results_From_Calcs
        self.Axis_x_Title = Axis_x_Title

        self.Checked_Simple_Bars = BooleanVar(self.W_Show_Graph)
        self.Checked_Simple_Bars_fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Simple_Bars_hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Simple_Bars_hi_percent = BooleanVar(self.W_Show_Graph)

        self.Checked_Pie = BooleanVar(self.W_Show_Graph)

        if(Dictionary_Of_Generated_Figures):
            self.Dictionary_Of_Generated_Figures = Dictionary_Of_Generated_Figures
        else:
            self.Dictionary_Of_Generated_Figures = {
                "Figure_Simple_Bars": {},
                "Figure_Pie": {},
            }

        self.Dictionary_Of_Generated_Widgets = {
            "Widget_Simple_Bars": {},
            "Widget_Pie": {},
        }
        
        self.Class_Generator_Of_Graphs = []

    def Get_Dictionary_Of_Graphs(self):
        return self.Dictionary_Of_Generated_Figures

    def Generate_Widgets(self , Category_Graph , Variable_Of_Frecuency):
        if(not f"Widget_{Category_Graph}_{Variable_Of_Frecuency}" in self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"]):
            Widget_Figure = FigureCanvasTkAgg(self.Dictionary_Of_Generated_Figures[f"Figure_{Category_Graph}"][f"Figure_{Category_Graph}_{Variable_Of_Frecuency}"] , master=self.W_Show_Graph)
            Widget_Figure.draw()

            self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"][f"Widget_{Category_Graph}_{Variable_Of_Frecuency}"] = Widget_Figure

    def Generate_Graphs(self):
        if(all(list(self.Dictionary_Of_Generated_Figures.values()))):
            return 0

        Info_For_Graphs = {
            "Simple_Bars": ["fi" , "hi" , "hi_percent"] , 
            "Pie": ["hi_percent"],
        }
        
        Number_Of_Threads = Get_Number_Of_Util_Threads_In_Device()
        Total_Works = 2
        Lock = threading.Lock()
        
        Class_Progress_Bar = W_Progress_Bar(self.W_Show_Graph)
        Class_Progress_Bar.Start_Progress_Bar()

        if(Number_Of_Threads > Total_Works):
            Threads_List = []
            for category_graph , variable_frecuency_list in Info_For_Graphs.items():
                Thread = threading.Thread(target= lambda: Manage_All_Graphs_Draw(self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , category_graph , variable_frecuency_list , None , None))
                Threads_List.append(Thread)
                Thread.start()
            
            self.W_Show_Graph.after(500 , Check_Threads_Alive , Threads_List , self.W_Show_Graph , Class_Progress_Bar)
        elif(Number_Of_Threads > 1):
            threading.Thread(target=Generate_Graph_With_One_Or_Any_Thread , args=(self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , Info_For_Graphs , self.W_Show_Graph , Class_Progress_Bar)).start()
        elif(Number_Of_Threads == 1):
            Generate_Graph_With_One_Or_Any_Thread(self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , Info_For_Graphs)
                        
    def Block_Or_Activate_Checkboxes(self , Category_Graph , Is_Only_Main_Checkbox=False , Variable_Of_Frecuency=None):
        Category_With_One_Checkbox = ["Pie"]

        for category_name , main_checked_values , dict_with_subcheckboxes_values , dict_with_subcheckboxes_widgets in zip(self.Dictionary_Main_Checkboxes_Values.keys() , self.Dictionary_Main_Checkboxes_Values.values() , self.Dictionary_SubCheckboxes_Values.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            if(category_name != Category_Graph or (category_name == Category_Graph and not main_checked_values.get())):
                main_checked_values.set(False)
                if(category_name in Category_With_One_Checkbox):
                    continue
                for checked_subwidget , checkbox_subwidget in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()):
                    checked_subwidget.set(False)
                    checkbox_subwidget.config(state="disabled")

            else:
                if(category_name in Category_With_One_Checkbox):
                    continue
                for checked_subwidget , checkbox_subwidget in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()):
                    checked_subwidget.set(False)
                    checkbox_subwidget.config(state="normal")

        self.Hidden_Widgets_Graphs()

        if(Is_Only_Main_Checkbox):
            self.Generate_Widgets(Category_Graph , Variable_Of_Frecuency)
            self.Display_Widgets_Graphs(Category_Graph , Variable_Of_Frecuency)

    def Only_Check_Single_Option_Subcheckboxes(self , Category_Graph , Variable_Of_Frecuency):
        for category_graph , dict_with_subcheckboxes in self.Dictionary_SubCheckboxes_Values.items():
            if(category_graph == Category_Graph):
                for name_graph , subcheckbox_value in dict_with_subcheckboxes.items():
                    if(name_graph != f"{Category_Graph}_{Variable_Of_Frecuency}"):
                        subcheckbox_value.set(False)

            #self.Generate_Graphs()
        self.Generate_Widgets(Category_Graph , Variable_Of_Frecuency)
        self.Display_Widgets_Graphs(Category_Graph , Variable_Of_Frecuency)

    def Generate_Checkboxes(self):
        self.Checkbox_Simple_Bars = Checkbutton(self.W_Show_Graph , text="Grafico de Barras Simples" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Simple_Bars ,  command= lambda: self.Block_Or_Activate_Checkboxes("Simple_Bars"))
        self.Checkbox_Simple_Bars_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Simple_Bars_fi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Simple_Bars" , "fi"))
        self.Checkbox_Simple_Bars_fi.config(state="disabled")
        self.Checkbox_Simple_Bars_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Simple_Bars_hi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Simple_Bars" , "hi"))
        self.Checkbox_Simple_Bars_hi.config(state="disabled")
        self.Checkbox_Simple_Bars_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Simple_Bars_hi_percent ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Simple_Bars" , "hi_percent"))
        self.Checkbox_Simple_Bars_hi_percent.config(state="disabled")

        self.Checkbox_Pie = Checkbutton(self.W_Show_Graph , text="Grafico de Pastel" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Pie ,  command= lambda: self.Block_Or_Activate_Checkboxes("Pie" , True , "hi_percent"))

        self.Dictionary_Main_Checkboxes_Widgets = {
            "Simple_Bars": self.Checkbox_Simple_Bars,
            "Pie": self.Checkbox_Pie,
        }
        self.Dictionary_Main_Checkboxes_Values = {
            "Simple_Bars": self.Checked_Simple_Bars,
            "Pie": self.Checked_Pie,
        }
        

        self.Dictionary_SubCheckboxes_Widgets = {
            "Simple_Bars": {
                "Simple_Bars_fi": self.Checkbox_Simple_Bars_fi,
                "Simple_Bars_hi": self.Checkbox_Simple_Bars_hi,
                "Simple_Bars_hi_percent": self.Checkbox_Simple_Bars_hi_percent,
            },
            "Pie": {
                "Pie_hi_percent": self.Checkbox_Pie,
            },
        }
        self.Dictionary_SubCheckboxes_Values = {
            "Simple_Bars": {
                "Simple_Bars_fi": self.Checked_Simple_Bars_fi,
                "Simple_Bars_hi": self.Checked_Simple_Bars_hi,
                "Simple_Bars_hi_percent": self.Checked_Simple_Bars_hi_percent,
            },
            "Pie": {
                "Pie_hi_percent": self.Checked_Pie,
            },
        }

    def Display_Widgets_Graphs(self , Category_Graph , Variable_Of_Frecuency):
        self.Hidden_Widgets_Graphs()

        if(self.Dictionary_SubCheckboxes_Values[Category_Graph][f"{Category_Graph}_{Variable_Of_Frecuency}"].get()):
            self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"][f"Widget_{Category_Graph}_{Variable_Of_Frecuency}"].get_tk_widget().place(x=320 , y=0)
    
    def Hidden_Widgets_Graphs(self):
        for dict_with_widgets in self.Dictionary_Of_Generated_Widgets.values():
            for widget in dict_with_widgets.values():
                if(widget):
                    widget.get_tk_widget().place_forget()
    
    def Display_Checkboxes(self):
        start_place = 140
        for category_graph , main_checkbox , dict_with_subcheckboxes in zip(self.Dictionary_Main_Checkboxes_Widgets.keys() , self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            main_checkbox.place(x=20 , y=start_place)
            if(category_graph == "Pie"):
                continue

            for subcheckboxes in dict_with_subcheckboxes.values():
                start_place += 25
                subcheckboxes.place(x=40 , y=start_place)
            start_place += 40

    def Hidden_Checkboxes(self):
        for main_checkbox , dict_with_subcheckboxes in zip(self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            main_checkbox.place_forget()
            for subcheckboxes in dict_with_subcheckboxes.values():
                subcheckboxes.place_forget()

        self.Hidden_Widgets_Graphs()


def Create_Window_Show_Graph(W_Calc_Frecuences_Table , Results_From_Single_Column , Results_From_Multiple_Columns , Precision , Dictionary_Of_Generated_Figures):
    def Change_To_Different_Variable_Graph(Event = None):
        if(Checkboxes_Class_Collection):
            Selection = Combobox_For_Variable_Names.get()
            for check in Checkboxes_Class_Collection.values():
                check.Hidden_Checkboxes()
                check.Hidden_Widgets_Graphs()

            Checkboxes_Class_Collection[f"{Selection}"].Display_Checkboxes()

            Info_For_Checked_Checkbox = None
            Category_Graph = None
            for category_name , Subcheckboxes in Checkboxes_Class_Collection[f"{Selection}"].Dictionary_SubCheckboxes_Values.items():
                Info_For_Checked_Checkbox = {key: value for key , value in Subcheckboxes.items() if value.get() == True}
                if(Info_For_Checked_Checkbox):
                    Category_Graph = category_name
                    break
            
            if(Info_For_Checked_Checkbox):
                Name_Graph = next(iter(Info_For_Checked_Checkbox.keys()))
                Variable_Of_Frecuency = Name_Graph.replace(Category_Graph , "")
                Variable_Of_Frecuency = "".join(val for i , val in enumerate(Variable_Of_Frecuency) if i > 0)

                Checkboxes_Class_Collection[f"{Selection}"].Display_Widgets_Graphs(Category_Graph , Variable_Of_Frecuency)

    W_Show_Graph = Toplevel(W_Calc_Frecuences_Table)
    W_Show_Graph.title("Ver graficos")
    W_Show_Graph.geometry("1300x700+105+105")
    W_Show_Graph.grab_set()
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
    W_Show_Graph.iconphoto(False , Icon)
    W_Show_Graph.config(bg="#F8D9AB")

    Checkboxes_Class_Collection = {} # Solo se usa para gestionar graficos de multiples variables

    W_Show_Graph.protocol("WM_DELETE_WINDOW", lambda: Delete_Actual_Window(W_Calc_Frecuences_Table , W_Show_Graph))

    Section_Graphs = Label(W_Show_Graph , bg="#ffffff" , text="Selecciona un grafico y se mostrara aqui" , font=("Times New Roman" , 13) , anchor="center")
    Section_Graphs.place(x=320 , y=0 , width=980 , height=700)

    List_Of_Variable_Names = []
    Combobox_For_Variable_Names = ttk.Combobox(W_Show_Graph , values=List_Of_Variable_Names , font=("Courier New" , 13) , width=25 , state="readonly")

    try:
        if(Results_From_Single_Column):
            Intervals_Formatted = None
            Copy_Results = copy.deepcopy(Results_From_Single_Column)

            if(len(Copy_Results) == 1):
                Variable_Name , Results_From_Calcs = next(iter(Copy_Results.items()))
            else:
                Results_From_Calcs = Copy_Results
                Variable_Name = None

            if("Frecuences_Cuant_Grouped" in Results_From_Calcs):
                Intervals_Formatted = Change_Key_From_Intervals_List(Results_From_Calcs)
                Class_For_Checkboxes = Checkboxes_For_Grouped_Data(W_Show_Graph , Results_From_Calcs , Variable_Name , Dictionary_Of_Generated_Figures)

            elif("Frecuences_Cuant_Not_Grouped" in Results_From_Calcs):
                Class_For_Checkboxes = Checkboxes_For_Not_Grouped_Data(W_Show_Graph , Results_From_Calcs , Variable_Name , Dictionary_Of_Generated_Figures)

            elif("Frecuences_Cuali" in Results_From_Calcs):
                Class_For_Checkboxes = Checkboxes_For_Cualitative_Data(W_Show_Graph , Results_From_Calcs , Variable_Name , Dictionary_Of_Generated_Figures)

            Class_For_Checkboxes.Generate_Graphs()

            Class_For_Checkboxes.Generate_Checkboxes()
            Class_For_Checkboxes.Display_Checkboxes()
            
            Figures_Graphs = Class_For_Checkboxes.Get_Dictionary_Of_Graphs()
            for key_dict_figures , val_dict_figures in Figures_Graphs.items():
                Dictionary_Of_Generated_Figures[key_dict_figures] = val_dict_figures

        elif(Results_From_Multiple_Columns):
            Copy_Results = copy.deepcopy(Results_From_Multiple_Columns)

            for variable_name , results_from_calcs in Copy_Results.items():
                if("Frecuences_Cuant_Grouped" in results_from_calcs):
                    Intervals_Formatted = None
                    Intervals_Formatted = Change_Key_From_Intervals_List(results_from_calcs)
                    if(variable_name in Dictionary_Of_Generated_Figures):
                        Class_For_Checkboxes = Checkboxes_For_Grouped_Data(W_Show_Graph , results_from_calcs , variable_name , Dictionary_Of_Generated_Figures[variable_name])
                    else:
                        Class_For_Checkboxes = Checkboxes_For_Grouped_Data(W_Show_Graph , results_from_calcs , variable_name , None)

                elif("Frecuences_Cuant_Not_Grouped" in results_from_calcs):
                    if(variable_name in Dictionary_Of_Generated_Figures):
                        Class_For_Checkboxes = Checkboxes_For_Not_Grouped_Data(W_Show_Graph , results_from_calcs , variable_name , Dictionary_Of_Generated_Figures[variable_name])
                    else:
                        Class_For_Checkboxes = Checkboxes_For_Not_Grouped_Data(W_Show_Graph , results_from_calcs , variable_name , None)

                elif("Frecuences_Cuali" in results_from_calcs):
                    if(variable_name in Dictionary_Of_Generated_Figures):
                        Class_For_Checkboxes = Checkboxes_For_Cualitative_Data(W_Show_Graph , results_from_calcs , variable_name , Dictionary_Of_Generated_Figures[variable_name])
                    else:
                        Class_For_Checkboxes = Checkboxes_For_Cualitative_Data(W_Show_Graph , results_from_calcs , variable_name , None)

                Class_For_Checkboxes.Generate_Graphs()

                Class_For_Checkboxes.Generate_Checkboxes()
                Class_For_Checkboxes.Display_Checkboxes()

                Figures_Graphs = Class_For_Checkboxes.Get_Dictionary_Of_Graphs()
                Dictionary_Of_Generated_Figures[variable_name] = Figures_Graphs

                Checkboxes_Class_Collection[f"{variable_name}"] = Class_For_Checkboxes

                List_Of_Variable_Names.append(variable_name)

            Combobox_For_Variable_Names["values"] = List_Of_Variable_Names
            Combobox_For_Variable_Names.set(List_Of_Variable_Names[0])
            Combobox_For_Variable_Names.place(x=20 , y=50)
            Combobox_For_Variable_Names.bind('<<ComboboxSelected>>' , Change_To_Different_Variable_Graph)

            Change_To_Different_Variable_Graph()
        else:
            raise Exception("No se encontraron los datos necesarios para generar los graficos.")

    except Exception as e:
        messagebox.showerror("Error" , f"{e}")

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar graficos" , font=("Times New Roman" , 13) , width=15 , bg="#FDA8C0" , )
    Btn_Export_Graph.place(x=90 , y=520)

    """ Btn_Create_And_Export_Multiple_Graphs = Button(W_Show_Graph , text="Crear y Exportar\nMultiples Graficos" , font=("Times New Roman" , 13) , width=24  , bg="#FDA8C0" , justify="center" , command= lambda: Create_Window_Multiple_Graphs(W_Show_Graph))
    Btn_Create_And_Export_Multiple_Graphs.place(x=50 , y=560) """

    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()