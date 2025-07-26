import sys
import os
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Tools import Get_Resource_Path , Get_Number_Of_Util_Threads_In_Device , Delete_Actual_Window , Check_Threads_Alive , Center_Window , Insert_Data_In_Log_File , Get_Detailed_Info_About_Error
from Calcs.Table_of_Frecuency.Graphs.Draw_Graphs import Manage_All_Graphs_Draw
from Views.Table_of_Frecuency.Exports.Window_Export_Graph import Create_Window_Export_Graphs
from Window_Create_Multiple_Graphs import Create_Window_Multiple_Graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Window_Progress_Bar import W_Progress_Bar

import threading

def Generate_Graph_For_Limited_Threads(W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures , Class_Generator_Of_Graphs , Info_For_Graphs):
    try:
        for category_graph , variable_frecuency_list in Info_For_Graphs.items():
            Manage_All_Graphs_Draw(W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures , Class_Generator_Of_Graphs , category_graph , variable_frecuency_list , None , None)
    except RuntimeError as e:
        W_Show_Graph.after(30 , messagebox.showerror("Error" , "Error al procesar en hilos\nError en tiempo de ejecucion.\nSi ocurre demasiadas veces reportelo."))
        W_Show_Graph.after(40 , Insert_Data_In_Log_File("Error al procesar en hilos. Error en tiempo de ejecucion. Si ocurre demasiadas veces reportelo." , "Error" , "Visualizacion de graficos" , Get_Detailed_Info_About_Error()))
        return

class Handler_Of_States_And_Actions:
    def __init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures , Dictionary_Of_Generated_Widgets , Info_For_Generate_Graphs , Category_With_One_Checkbox=None):
        
        self.W_Show_Graph = W_Show_Graph

        self.Results_From_Calcs = Results_From_Calcs
        self.Axis_x_Title = Axis_x_Title

        self.Dictionary_Of_Generated_Figures = Dictionary_Of_Generated_Figures
        self.Dictionary_Of_Generated_Widgets = Dictionary_Of_Generated_Widgets
        self.Info_For_Generate_Graphs = Info_For_Generate_Graphs
        self.Total_Of_Works = len(Info_For_Generate_Graphs)

        self.Class_Generator_Of_Graphs = []

        self.Dictionary_Main_Checkboxes_Widgets = None
        self.Dictionary_Main_Checkboxes_Values = None
        self.Dictionary_SubCheckboxes_Widgets = None
        self.Dictionary_SubCheckboxes_Values = None

        if(Category_With_One_Checkbox):
            self.Category_With_One_Checkbox = Category_With_One_Checkbox
        else:
            self.Category_With_One_Checkbox = []

    def Get_Dictionary_Of_Graphs(self):
        return self.Dictionary_Of_Generated_Figures

    def Generate_Graphs(self , On_Finish=None):
        try:    
            if(all(list(self.Dictionary_Of_Generated_Figures.values()))):
                if(On_Finish):
                    On_Finish()
                return
            
            Number_Of_Threads = Get_Number_Of_Util_Threads_In_Device()
            Lock = threading.Lock()

            Class_Progress_Bar = W_Progress_Bar(self.W_Show_Graph)

            if(self.Axis_x_Title):
                Class_Progress_Bar.Start_Progress_Bar(f"Generando graficos para: {self.Axis_x_Title}...")
            else:
                Class_Progress_Bar.Start_Progress_Bar(f"Generando graficos...")

            Threads_List = []
            if(Number_Of_Threads > self.Total_Of_Works):
                for category_graph , variable_frecuency_list in self.Info_For_Generate_Graphs.items():
                    Thread = threading.Thread(target= lambda: Manage_All_Graphs_Draw(self.W_Show_Graph , self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , category_graph , variable_frecuency_list))
                    Threads_List.append(Thread)
                    Thread.start()
        
            elif(Number_Of_Threads > 2 and Number_Of_Threads <= self.Total_Of_Works):
                Chunks = [{} for i in range(Number_Of_Threads - 1)]
                
                idx = 0
                for key , value in self.Info_For_Generate_Graphs.items():
                    if(idx == Number_Of_Threads - 1):
                        idx = 0
                    else:
                        idx += 1
                    Chunks[idx][key] = value
                    
                for chunk in Chunks:
                    Thread = threading.Thread(target= lambda: Generate_Graph_For_Limited_Threads(self.W_Show_Graph , self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , chunk))
                    Threads_List.append(Thread)
                    Thread.start()

            elif(Number_Of_Threads == 2):
                def Work():
                    Generate_Graph_For_Limited_Threads(self.W_Show_Graph , self.Results_From_Calcs , self.Axis_x_Title , self.Dictionary_Of_Generated_Figures , self.Class_Generator_Of_Graphs , self.Info_For_Generate_Graphs)

                Thread = threading.Thread(target=Work)
                Threads_List.append(Thread)
                Thread.start()
            elif(Number_Of_Threads < 2):
                raise Exception("Error" , "No se puede ejecutar la generacion de graficos.\nSe detectaron menos de 2 nucleos de CPU\nen su dispositivo.")
            
            self.W_Show_Graph.after(500 , Check_Threads_Alive , Threads_List , self.W_Show_Graph , Class_Progress_Bar , On_Finish)

        except Exception as e:
            self.W_Show_Graph.after(30 , messagebox.showerror("Error" , f"{e}"))
            self.W_Show_Graph.after(40 , Insert_Data_In_Log_File(e , "Error" , "Creacion de graficos" , Get_Detailed_Info_About_Error()))
        else:
            self.W_Show_Graph.after(10 , Insert_Data_In_Log_File("La funcion de generacion de graficos se ejecuto e inicio los hilos correctamente." , "Operacion exitosa" , "Creacion de graficos"))

    def Generate_Widgets(self , Category_Graph , Variable_Of_Frecuency):
        if(not f"Widget_{Category_Graph}_{Variable_Of_Frecuency}" in self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"]):
            Widget_Figure = FigureCanvasTkAgg(self.Dictionary_Of_Generated_Figures[f"Figure_{Category_Graph}"][f"Figure_{Category_Graph}_{Variable_Of_Frecuency}"] , master=self.W_Show_Graph)
            Widget_Figure.draw()

            self.Dictionary_Of_Generated_Widgets[f"Widget_{Category_Graph}"][f"Widget_{Category_Graph}_{Variable_Of_Frecuency}"] = Widget_Figure

    def Block_Or_Activate_Checkboxes(self , Category_Graph , Is_Only_Main_Checkbox=False , Variable_Of_Frecuency=None):
        for category_name , main_checked_values , dict_with_subcheckboxes_values , dict_with_subcheckboxes_widgets in zip(self.Dictionary_Main_Checkboxes_Values.keys() , self.Dictionary_Main_Checkboxes_Values.values() , self.Dictionary_SubCheckboxes_Values.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
            if(category_name != Category_Graph or (category_name == Category_Graph and not main_checked_values.get())):
                main_checked_values.set(False)
                if(category_name in self.Category_With_One_Checkbox):
                    continue
                for checked_subwidget , checkbox_subwidget in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()):
                    checked_subwidget.set(False)
                    checkbox_subwidget.config(state="disabled")

            else:
                if(category_name in self.Category_With_One_Checkbox):
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

        self.Generate_Widgets(Category_Graph , Variable_Of_Frecuency)
        self.Display_Widgets_Graphs(Category_Graph , Variable_Of_Frecuency)

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
        if(self.Dictionary_Main_Checkboxes_Widgets and self.Dictionary_SubCheckboxes_Widgets):
            start_place = 140
            for (category_graph , main_checkbox) , dict_with_subcheckboxes in zip(self.Dictionary_Main_Checkboxes_Widgets.items() , self.Dictionary_SubCheckboxes_Widgets.values()):
                main_checkbox.place(x=20 , y=start_place)
                if(not category_graph in self.Category_With_One_Checkbox):
                    for subcheckboxes in dict_with_subcheckboxes.values():
                        start_place += 25
                        subcheckboxes.place(x=40 , y=start_place)
                start_place += 40

    def Hidden_Checkboxes(self):
        if(self.Dictionary_Main_Checkboxes_Values and self.Dictionary_SubCheckboxes_Values):
            for main_checkbox , dict_with_subcheckboxes in zip(self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_SubCheckboxes_Widgets.values()):
                main_checkbox.place_forget()
                for subcheckboxes in dict_with_subcheckboxes.values():
                    subcheckboxes.place_forget()

            self.Hidden_Widgets_Graphs()

class Checkboxes_For_Grouped_Data(Handler_Of_States_And_Actions):
    def __init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures):
        if(not Dictionary_Of_Generated_Figures):
            Dictionary_Of_Generated_Figures = {
                "Figure_Histogram": {},
                "Figure_Frecuences_Polygon": {},
                "Figure_Acumulate_Frecuences_Polygon": {},
                "Figure_Boxplot": {},
            }

        Dictionary_Of_Generated_Widgets = {
            "Widget_Histogram": {},
            "Widget_Frecuences_Polygon": {},
            "Widget_Acumulate_Frecuences_Polygon": {},
            "Widget_Boxplot": {},
        }
        
        Info_For_Generate_Graphs = {
            "Histogram": ["fi" , "hi" , "hi_percent"] , 
            "Frecuences_Polygon": ["fi" , "hi" , "hi_percent"] , 
            "Acumulate_Frecuences_Polygon": ["Fi" , "Hi" , "Hi_percent"],
            "Boxplot": ["All_Data"],
        }
        Category_With_One_Checkbox = ["Boxplot"]

        Handler_Of_States_And_Actions.__init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures , Dictionary_Of_Generated_Widgets , Info_For_Generate_Graphs , Category_With_One_Checkbox)

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

        self.Checked_Boxplot = BooleanVar(self.W_Show_Graph)

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

        self.Checkbox_Boxplot = Checkbutton(self.W_Show_Graph , text="Grafico de Cajas" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Boxplot ,  command= lambda: self.Block_Or_Activate_Checkboxes("Boxplot" , True , "All_Data"))

        self.Dictionary_Main_Checkboxes_Widgets = {
            "Histogram": self.Checkbox_Histogram,
            "Frecuences_Polygon": self.Checkbox_Frecuences_Polygon,
            "Acumulate_Frecuences_Polygon": self.Checkbox_Acumulate_Frecuences_Polygon,
            "Boxplot": self.Checkbox_Boxplot,
        }
        self.Dictionary_Main_Checkboxes_Values = {
            "Histogram": self.Checked_Histogram,
            "Frecuences_Polygon": self.Checked_Frecuences_Polygon,
            "Acumulate_Frecuences_Polygon": self.Checked_Acumulate_Frecuences_Polygon,
            "Boxplot": self.Checked_Boxplot,
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
            "Boxplot": {
                "Boxplot_All_Data": self.Checkbox_Boxplot,
            }
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
            "Boxplot": {
                "Boxplot_All_Data": self.Checked_Boxplot,
            }
        }

class Checkboxes_For_Not_Grouped_Data(Handler_Of_States_And_Actions):
    def __init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures):
        if(not Dictionary_Of_Generated_Figures):
            Dictionary_Of_Generated_Figures = {
                "Figure_Bars_Graph": {},
                "Figure_Stick_Graph": {},
                "Figure_Step_Chart": {},
            }

        Dictionary_Of_Generated_Widgets = {
            "Widget_Bars_Graph": {},
            "Widget_Stick_Graph": {},
            "Widget_Step_Chart": {},
        }

        Info_For_Generate_Graphs = {
            "Bars_Graph": ["fi" , "hi" , "hi_percent"],
            "Stick_Graph": ["fi" , "hi" , "hi_percent"],
            "Step_Chart": ["Fi" , "Hi" , "Hi_percent"],
        }

        Handler_Of_States_And_Actions.__init__(self, W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures , Dictionary_Of_Generated_Widgets , Info_For_Generate_Graphs)

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

    def Generate_Checkboxes(self):
        self.Checkbox_Bars_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de Barras" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph ,  command= lambda: self.Block_Or_Activate_Checkboxes("Bars_Graph"))
        self.Checkbox_Bars_Graph_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph_fi , command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Bars_Graph" , "fi"))
        self.Checkbox_Bars_Graph_fi.config(state="disabled")
        self.Checkbox_Bars_Graph_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph_hi , command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Bars_Graph" , "hi"))
        self.Checkbox_Bars_Graph_hi.config(state="disabled")
        self.Checkbox_Bars_Graph_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Bars_Graph_hi_percent , command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Bars_Graph" , "hi_percent"))
        self.Checkbox_Bars_Graph_hi_percent.config(state="disabled")

        self.Checkbox_Stick_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de Bastones" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Stick_Graph ,  command= lambda: self.Block_Or_Activate_Checkboxes("Stick_Graph"))
        self.Checkbox_Stick_Graph_fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Stick_Graph_fi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Stick_Graph" , "fi"))
        self.Checkbox_Stick_Graph_fi.config(state="disabled")
        self.Checkbox_Stick_Graph_hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Stick_Graph_hi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Stick_Graph" , "hi"))
        self.Checkbox_Stick_Graph_hi.config(state="disabled")
        self.Checkbox_Stick_Graph_hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Stick_Graph_hi_percent ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Stick_Graph" , "hi_percent"))
        self.Checkbox_Stick_Graph_hi_percent.config(state="disabled")

        self.Checkbox_Step_Chart = Checkbutton(self.W_Show_Graph , text="Grafico de Escalones" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart ,  command= lambda: self.Block_Or_Activate_Checkboxes("Step_Chart"))
        self.Checkbox_Step_Chart_Fi = Checkbutton(self.W_Show_Graph , text="Para fi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart_Fi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Step_Chart" , "Fi"))
        self.Checkbox_Step_Chart_Fi.config(state="disabled")
        self.Checkbox_Step_Chart_Hi = Checkbutton(self.W_Show_Graph , text="Para hi" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart_Hi ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Step_Chart" , "Hi"))
        self.Checkbox_Step_Chart_Hi.config(state="disabled")
        self.Checkbox_Step_Chart_Hi_percent = Checkbutton(self.W_Show_Graph , text="Para hi%" , font=("Times New Roman" , 13) , bg="#F8D9AB" , variable=self.Checked_Step_Chart_Hi_percent ,  command= lambda: self.Only_Check_Single_Option_Subcheckboxes("Step_Chart" , "Hi_percent"))
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

class Checkboxes_For_Cualitative_Data(Handler_Of_States_And_Actions):
    def __init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures):
        if(not Dictionary_Of_Generated_Figures):
            Dictionary_Of_Generated_Figures = {
                "Figure_Simple_Bars": {},
                "Figure_Pie": {},
            }

        Dictionary_Of_Generated_Widgets = {
            "Widget_Simple_Bars": {},
            "Widget_Pie": {},
        }
        Info_For_Generate_Graphs = {
            "Simple_Bars": ["fi" , "hi" , "hi_percent"] , 
            "Pie": ["hi_percent"],
        }

        Category_With_One_Checkbox = ["Pie"]

        Handler_Of_States_And_Actions.__init__(self , W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures , Dictionary_Of_Generated_Widgets , Info_For_Generate_Graphs , Category_With_One_Checkbox)

        self.Checked_Simple_Bars = BooleanVar(self.W_Show_Graph)
        self.Checked_Simple_Bars_fi = BooleanVar(self.W_Show_Graph)
        self.Checked_Simple_Bars_hi = BooleanVar(self.W_Show_Graph)
        self.Checked_Simple_Bars_hi_percent = BooleanVar(self.W_Show_Graph)

        self.Checked_Pie = BooleanVar(self.W_Show_Graph)

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

def Create_Window_Show_Graph(W_Calc_Frecuences_Table , Results_From_Single_Column , Results_From_Multiple_Columns , Precision , Dictionary_Of_Generated_Figures , Type_Of_Variable):
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

    def Process_Multiple_Column_Graphs(Index=0):
        """
            =========================================================================================
            Procesamiento Asincrono para la generacion de graficos, como maximo se usan 3 hilos para
            cada tanda de graficos (correspondientes a una variable en particular), todo comienza con
            esta funcion.
            1.  Ejecutar Process_Multiple_Column_Graphs(index) // index=0

            2.  Se generan los graficos correspondientes a la variable del index. 
                Se pasa el callback a la funcion Process_Multiple_Column_Graphs 
                (el callback es la funcion Continue_Processing_Of_Columns_Graphs), 
                este se ejecutara cuando los 3 primeros hilos terminen, 
                asegurandose asi que se los hilos se ejecuten de 3 en 3.

            3.  En la funcion Generate_Graphs(), la funcion Check_Threads_Alive() detectara que los
                hilos terminaron su ejecucion y llamara al Callback
                (la funcion Continue_Processing_Of_Columns_Graphs).

            4.  En la funcion Continue_Processing_Of_Columns_Graphs se generan los checkboxes, se
                guardan los graficos y se vuelve a ejecutar Process_Multiple_Column_Graphs pero
                con index=1 (pasando asi a la siguiente variable), se repiten los pasos 1 a 4
                hasta que index sea mayor al numero de variables a procesar.

            5.  Al finalizar toda la ejecucion, se crea el Combobox con el nombre de todas las 
                variables y se muestran los Checkboxes.
            =========================================================================================
        """
        try:
            Variables_To_Process = list(Copy_Results.keys())
            if(Index >= len(Variables_To_Process)):
                Finish_Process()
                return

            variable_name = Variables_To_Process[Index]
            results_from_calcs = Copy_Results[variable_name]
            type_of_variable = Type_Of_Variable[variable_name]
            match(type_of_variable):
                case "Cuantitative_Grouped":
                    if(variable_name in Dictionary_Of_Generated_Figures):
                        Class_For_Checkboxes = Checkboxes_For_Grouped_Data(W_Show_Graph , results_from_calcs , variable_name , Dictionary_Of_Generated_Figures[variable_name])
                    else:
                        Class_For_Checkboxes = Checkboxes_For_Grouped_Data(W_Show_Graph , results_from_calcs , variable_name , None)
                case "Cuantitative_Not_Grouped":
                    if(variable_name in Dictionary_Of_Generated_Figures):
                        Class_For_Checkboxes = Checkboxes_For_Not_Grouped_Data(W_Show_Graph , results_from_calcs , variable_name , Dictionary_Of_Generated_Figures[variable_name])
                    else:
                        Class_For_Checkboxes = Checkboxes_For_Not_Grouped_Data(W_Show_Graph , results_from_calcs , variable_name , None)
                case "Cualitative":
                    if(variable_name in Dictionary_Of_Generated_Figures):
                        Class_For_Checkboxes = Checkboxes_For_Cualitative_Data(W_Show_Graph , results_from_calcs , variable_name , Dictionary_Of_Generated_Figures[variable_name])
                    else:
                        Class_For_Checkboxes = Checkboxes_For_Cualitative_Data(W_Show_Graph , results_from_calcs , variable_name , None)

            Checkboxes_Class_Collection[f"{variable_name}"] = Class_For_Checkboxes
            List_Of_Variable_Names.append(variable_name)

            Class_For_Checkboxes.Generate_Graphs(On_Finish=lambda: Continue_Processing_Of_Columns_Graphs(Class_For_Checkboxes , variable_name , Index))
        except Exception as e:
            messagebox.showerror("Error" , f"{e}")
            Insert_Data_In_Log_File(e , "Error" , "Visualizacion de graficos" , Get_Detailed_Info_About_Error())

    def Continue_Processing_Of_Columns_Graphs(class_checkbox , variable_name , index):
        class_checkbox.Generate_Checkboxes()

        Figures_Graphs = class_checkbox.Get_Dictionary_Of_Graphs()
        Dictionary_Of_Generated_Figures[variable_name] = Figures_Graphs

        Insert_Data_In_Log_File(f"Todos los elementos y graficos para \"{variable_name if variable_name else 'una variable'}\" se generaron con exito." , "Operacion exitosa" , "Visualizacion de graficos")

        Process_Multiple_Column_Graphs(index + 1)

    def Finish_Process():
        Combobox_For_Variable_Names["values"] = List_Of_Variable_Names
        Combobox_For_Variable_Names.set(List_Of_Variable_Names[0])
        Combobox_For_Variable_Names.place(x=20 , y=50)
        Combobox_For_Variable_Names.bind('<<ComboboxSelected>>' , Change_To_Different_Variable_Graph)

        Change_To_Different_Variable_Graph()

        Insert_Data_In_Log_File("Todos los elementos y graficos se generaron con exito." , "Operacion exitosa" , "Visualizacion de graficos")

    W_Show_Graph = Toplevel(W_Calc_Frecuences_Table)
    W_Show_Graph.title("Ver graficos")
    # W_Show_Graph.geometry("1300x700+105+105")
    Center_Window(W_Show_Graph , 1300 , 700)
    W_Show_Graph.grab_set()
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
    W_Show_Graph.iconphoto(False , Icon)
    W_Show_Graph.config(bg="#F8D9AB")

    Checkboxes_Class_Collection = {} # Solo se usa para gestionar graficos de multiples variables
    Axis_x_Title = None

    W_Show_Graph.protocol("WM_DELETE_WINDOW", lambda: Delete_Actual_Window(W_Calc_Frecuences_Table , W_Show_Graph))

    Section_Graphs = Label(W_Show_Graph , bg="#ffffff" , text="Selecciona un grafico y se mostrara aqui" , font=("Times New Roman" , 13) , anchor="center")
    Section_Graphs.place(x=320 , y=0 , width=980 , height=700)

    List_Of_Variable_Names = []
    Combobox_For_Variable_Names = ttk.Combobox(W_Show_Graph , values=List_Of_Variable_Names , font=("Courier New" , 13) , width=25 , state="readonly")

    try:
        if(Results_From_Single_Column):
            #Intervals_Formatted = None
            Copy_Results = copy.deepcopy(Results_From_Single_Column)

            if(len(Copy_Results) == 1):
                Axis_x_Title , Results_From_Calcs = next(iter(Copy_Results.items()))
            else:
                Results_From_Calcs = Copy_Results

            match(Type_Of_Variable):
                case "Cuantitative_Grouped":
                    Class_For_Checkboxes = Checkboxes_For_Grouped_Data(W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures)
                case "Cuantitative_Not_Grouped":
                    Class_For_Checkboxes = Checkboxes_For_Not_Grouped_Data(W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures)
                case "Cualitative":
                    Class_For_Checkboxes = Checkboxes_For_Cualitative_Data(W_Show_Graph , Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures)

            Class_For_Checkboxes.Generate_Graphs()

            Class_For_Checkboxes.Generate_Checkboxes()
            Class_For_Checkboxes.Display_Checkboxes()
            
            Figures_Graphs = Class_For_Checkboxes.Get_Dictionary_Of_Graphs()
            for key_dict_figures , val_dict_figures in Figures_Graphs.items():
                Dictionary_Of_Generated_Figures[key_dict_figures] = val_dict_figures

        elif(Results_From_Multiple_Columns):
            Copy_Results = copy.deepcopy(Results_From_Multiple_Columns)
            Axis_x_Title = list(Copy_Results.keys())
            Process_Multiple_Column_Graphs()
        else:
            raise Exception("No se encontraron los datos necesarios para generar los graficos.")

    except Exception as e:
        messagebox.showerror("Error" , f"{e}")
        Insert_Data_In_Log_File(e , "Error" , "Visualizacion de graficos" , Get_Detailed_Info_About_Error())
    else:
        Insert_Data_In_Log_File("Ventana de visualizacion de graficos generada con exito." , "Operacion exitosa" , "Visualizacion de graficos")

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar graficos" , font=("Times New Roman" , 13) , width=15 , bg="#FDA8C0" , command= lambda: Create_Window_Export_Graphs(W_Show_Graph , Dictionary_Of_Generated_Figures , "Single_Column" if Results_From_Single_Column else "Multiple_Columns" , Axis_x_Title , Type_Of_Variable))
    Btn_Export_Graph.place(x=90 , y=520)

    """ Btn_Create_And_Export_Multiple_Graphs = Button(W_Show_Graph , text="Crear y Exportar\nMultiples Graficos" , font=("Times New Roman" , 13) , width=24  , bg="#FDA8C0" , justify="center" , command= lambda: Create_Window_Multiple_Graphs(W_Show_Graph))
    Btn_Create_And_Export_Multiple_Graphs.place(x=50 , y=560) """

    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()