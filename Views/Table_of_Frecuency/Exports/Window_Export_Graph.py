import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..')))

from Tools import Get_Resource_Path
from Calcs.Table_of_Frecuency.Exports.Export_Graph import Export_Graph_As_Image

from tkinter import *
from tkinter import filedialog
from tkinter import ttk

class Widget_Input_Name_For_Graphs:
    def __init__(self , Root_Window , There_Are_Boxplot):
        self.W_Export_Graph = Root_Window
        self.There_Are_Boxplot = There_Are_Boxplot

        self.Name_Bar_Graph = StringVar(self.W_Export_Graph)
        self.Name_Bar_Graph.set("")
        self.Name_Pie_Graph = StringVar(self.W_Export_Graph)
        self.Name_Bar_Graph.set("")
        self.Name_Boxplot_Graph = StringVar(self.W_Export_Graph)
        self.Name_Boxplot_Graph.set("")

    def Create_Widgets(self):
        self.Input_Name_Bar_Graph = Entry(self.W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Name_Bar_Graph)
        self.Input_Name_Bar_Graph.config(state="disabled")

        self.Input_Name_Píe_Graph = Entry(self.W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Name_Pie_Graph)
        self.Input_Name_Píe_Graph.config(state="disabled")

        if(self.There_Are_Boxplot):
            self.Input_Name_Boxplot_Graph = Entry(self.W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Name_Boxplot_Graph)
            self.Input_Name_Boxplot_Graph.config(state="disabled")
        else:
            self.Input_Name_Boxplot_Graph = None
    
    def Display_Widgets(self):
        self.Input_Name_Bar_Graph.place(x=250 , y=520 , width=630)

        self.Input_Name_Píe_Graph.place(x=250 , y=570 , width=630)

        if(self.Input_Name_Boxplot_Graph):
            self.Input_Name_Boxplot_Graph.place(x=250 , y=620 , width=630)

    def Hidden_Widgets(self):
        self.Input_Name_Bar_Graph.place_forget()

        self.Input_Name_Píe_Graph.place_forget()

        if(self.Input_Name_Boxplot_Graph):
            self.Input_Name_Boxplot_Graph.place_forget()

class Handler_Actions:
    def __init__(self , W_Export_Graph):
        self.Dictionary_Of_Main_Checkboxes_Values = None
        self.Dictionary_Of_Subcheckboxes_Values = None
        self.Dictionary_Of_Main_Checkboxes_Widgets = None
        self.Dictionary_Of_Subcheckboxes_Widgets = None

        self.Dictionary_Of_Entry_Titles_Widgets = None
        self.Dictionary_Of_Entry_Titles_Values = None

        self.Checked_Export_All_Graphs = BooleanVar(W_Export_Graph)
        self.Checkbox_Export_All_Graphs = Checkbutton(W_Export_Graph , text="Exportar todos los graficos" , font=("Times New Roman" , 13) , textvariable=self.Checked_Export_All_Graphs , command=self.Check_All_Checkboxes)

    def Hidden_Widgets(self):
        for main_checkbox_widget , subcheckbox_dict in zip(self.Dictionary_Of_Main_Checkboxes_Widgets.values() , self.Dictionary_Of_Subcheckboxes_Widgets.values()):
            main_checkbox_widget.place_forget()
            for subcheckbox_widget in subcheckbox_dict.values():
                subcheckbox_widget.place_forget()

    def Display_Widgets(self):
        self.Checkbox_Export_All_Graphs.place(x=50 , y=260)
        x_pos_checkboxes = 50

        for main_checkbox_widget , subcheckbox_dict in zip(self.Dictionary_Of_Main_Checkboxes_Widgets.values() , self.Dictionary_Of_Subcheckboxes_Widgets.values()):
            y_pos_checkboxes = 290
            x_pos_checkboxes += 170
            main_checkbox_widget.place(x=x_pos_checkboxes , y=y_pos_checkboxes)
            for subcheckbox_widget in subcheckbox_dict.values():
                y_pos_checkboxes += 30
                subcheckbox_widget.place(x=x_pos_checkboxes , y=y_pos_checkboxes)

        for dict_with_entry_widgets in self.Dictionary_Of_Entry_Titles_Widgets.values():
            for entry_titles_widget in dict_with_entry_widgets.values():
                entry_titles_widget
                #x=250 , y=520 , width=630

    def Check_And_Block_Single_Checkbox(self , Category_Graph , Variable_Of_Frecuency):
        for (category_graph , main_checkbox_value) , main_checkbox_widget , dict_with_subcheckboxes , dict_with_entry_titles_values , dict_with_entry_widgets in zip(self.Dictionary_Of_Main_Checkboxes_Values.values.items() , self.Dictionary_Of_Main_Checkboxes_Widgets.values() , self.Dictionary_Of_Subcheckboxes_Values.values() , self.Dictionary_Of_Entry_Titles_Values.values() , self.Dictionary_Of_Entry_Titles_Widgets.values()):
            if(category_graph == Category_Graph):
                Is_All_Checked = all(value.get() for value in dict_with_subcheckboxes.values())

                if(dict_with_subcheckboxes[f"{Category_Graph}_{Variable_Of_Frecuency}"].get()):
                    dict_with_entry_titles_values[f"{Category_Graph}_{Variable_Of_Frecuency}"].set("")
                    dict_with_entry_widgets[f"{Category_Graph}_{Variable_Of_Frecuency}"].config(state="normal")
                else:
                    dict_with_entry_titles_values[f"{Category_Graph}_{Variable_Of_Frecuency}"].set("")
                    dict_with_entry_widgets[f"{Category_Graph}_{Variable_Of_Frecuency}"].config(state="disabled")

                if(Is_All_Checked):
                    main_checkbox_value.set(True)
                    main_checkbox_widget.config(state="disabled")
                else:
                    main_checkbox_value.set(False)
                    main_checkbox_widget.config(state="normal")

    def Check_And_Block_Multiple_Checkboxes(self , Category_Graph):
        for category_name , dict_with_subcheckboxes_values , dict_with_subcheckboxes_widgets , dict_with_entry_titles_values , dict_with_entry_widgets in zip(self.Dictionary_Main_Checkboxes_Values.keys() , self.Dictionary_SubCheckboxes_Values.values() , self.Dictionary_SubCheckboxes_Widgets.values() , self.Dictionary_Of_Entry_Titles_Values.values() , self.Dictionary_Of_Entry_Titles_Widgets.values()):
            for subcheckboxes_values , subcheckboxes_widgets , entry_titles_values , entry_widgets in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values() , dict_with_entry_titles_values.values() , dict_with_entry_widgets.values()):
                if(category_name == Category_Graph):
                    subcheckboxes_values.set(True)
                    subcheckboxes_widgets.config(state="disabled")

                    entry_titles_values.set("")
                    entry_widgets.config(state="normal")
                else:
                    subcheckboxes_values.set(False)
                    subcheckboxes_widgets.config(state="normal")

                    entry_titles_values.set("")
                    entry_widgets.config(state="disabled")

    def Check_All_Checkboxes(self):
        for main_checkbox_value , main_checkbox_widget , dict_with_subcheckboxes_values , dict_with_subcheckboxes_widgets in zip(self.Dictionary_Of_Main_Checkboxes_Values.values() , self.Dictionary_Of_Main_Checkboxes_Widgets.values() , self.Dictionary_Of_Subcheckboxes_Values.values() , self.Dictionary_Of_Subcheckboxes_Widgets.values()):
            if(self.Checked_Export_All_Graphs.get()):
                main_checkbox_value.set(True)
                main_checkbox_widget.config(state="disabled")
                for subcheckboxes_values , subcheckboxes_widgets in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()): 
                    subcheckboxes_values.set(True)
                    subcheckboxes_widgets.config(state="disabled")
            else:
                main_checkbox_value.set(False)
                main_checkbox_widget.config(state="normal")
                for subcheckboxes_values , subcheckboxes_widgets in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()): 
                    subcheckboxes_values.set(False)
                    subcheckboxes_widgets.config(state="normal")

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

        self.Title_For_Axis_x = StringVar(W_Export_Graph)

        self.Main_Container = Label(W_Export_Graph , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)
        self.Main_Container.place(x=20 , y=500 , width=1240 , height=160)

        self.Frame_Sets = Frame(W_Export_Graph , bg="#CDC4FF" , highlightbackground="#000000" , highlightthickness=1)
        self.Frame_Sets.place(x=20 , y=500 , width=1240 , height=100)

        self.Canvas_Set = Canvas(self.Frame_Sets, width=1220, height=100)
        self.Canvas_Set.grid(row=0, column=0, sticky="nsew")

        self.ScrollBar_Frame = ttk.Scrollbar(self.Frame_Sets, orient="vertical", command=self.Canvas_Set.yview)
        self.ScrollBar_Frame.grid(row=0, column=1, sticky="ns")

        self.Canvas_Set.configure(yscrollcommand=self.ScrollBar_Frame.set)

        self.Content_Frame_Sets = Frame(self.Canvas_Set, width=1240 , bg="#CDC4FF")

        self.Canvas_Set.create_window((0, 0), window=self.Content_Frame_Sets, anchor="nw")

    def Create_Entry_Widgets(self , W_Export_Graph , Axis_x_title):
        self.Entry_For_Histogram_fi = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_fi)
        self.Entry_For_Histogram_hi = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi)
        self.Entry_For_Histogram_hi_percent = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Histogram_hi_percent)

        self.Entry_For_Frecuences_Polygon_fi = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_fi)
        self.Entry_For_Frecuences_Polygon_hi = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_hi)
        self.Entry_For_Frecuences_Polygon_hi_percent = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Frecuences_Polygon_hi_percent)

        self.Entry_For_Acumulate_Frecuences_Polygon_Fi = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Fi)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Hi)
        self.Entry_For_Acumulate_Frecuences_Polygon_Hi_percent = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Acumulate_Frecuences_Polygon_Hi_percent)

        self.Title_For_Axis_x.set(Axis_x_title)
        self.Entry_For_Axis_x = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Axis_x)

        self.Dictionary_Of_Entry_Titles_Widgets = {
            "Histogram": {
                "Histogram_fi": self.Entry_For_Histogram_fi,
                "Histogram_hi": self.Entry_For_Histogram_hi,
                "Histogram_hi_percent": self.Entry_For_Histogram_hi_percent,
            },
            "Frecuences_Polygon": {
                "Frecuences_Polygon_fi": self.Entry_For_Frecuences_Polygon_fi,
                "Frecuences_Polygon_hi": self.Entry_For_Frecuences_Polygon_hi,
                "Frecuences_Polygon_hi_percent": self.Entry_For_Frecuences_Polygon_hi_percent,
            },
            "Acumulate_Frecuences_Polygon": {  
                "Acumulate_Frecuences_Polygon_Fi": self.Entry_For_Acumulate_Frecuences_Polygon_Fi,
                "Acumulate_Frecuences_Polygon_Hi": self.Entry_For_Acumulate_Frecuences_Polygon_Hi,
                "Acumulate_Frecuences_Polygon_Hi_percent": self.Entry_For_Acumulate_Frecuences_Polygon_Hi_percent,
            },
        }

        self.Dictionary_Of_Entry_Titles_Values = {
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
        }


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

        Handler_Actions.__init__(self , W_Export_Graph)
        Entry_Widget_For_Export_Graphs_For_Grouped_Data.__init__(self , W_Export_Graph)

    def Create_Checkboxes(self):
        self.Checkbox_Histogram = Checkbutton(self.W_Export_Graph , text="Exportar Histograma" , font=("Times New Roman" , 13) , textvariable=self.Checked_Histogram , command=self.Check_And_Block_Multiple_Checkboxes("Histogram"))
        self.Checkbox_Histogram_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , textvariable=self.Checked_Histogram_fi , command=self.Check_And_Block_Single_Checkbox("Histogram" , "fi"))
        self.Checkbox_Histogram_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , textvariable=self.Checked_Histogram_hi , command=self.Check_And_Block_Single_Checkbox("Histogram" , "hi"))
        self.Checkbox_Histogram_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , textvariable=self.Checked_Histogram_hi_percent , command=self.Check_And_Block_Single_Checkbox("Histogram" , "hi_percent"))

        self.Checkbox_Frecuences_Polygon = Checkbutton(self.W_Export_Graph , text="Exportar Poligono de Frecuencias" , font=("Times New Roman" , 13) , textvariable=self.Checked_Frecuences_Polygon , command=self.Check_And_Block_Multiple_Checkboxes("Frecuences_Polygon"))
        self.Checkbox_Frecuences_Polygon_fi = Checkbutton(self.W_Export_Graph , text="Para fi" , font=("Times New Roman" , 13) , textvariable=self.Checked_Frecuences_Polygon_fi , command=self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "fi"))
        self.Checkbox_Frecuences_Polygon_hi = Checkbutton(self.W_Export_Graph , text="Para hi" , font=("Times New Roman" , 13) , textvariable=self.Checked_Frecuences_Polygon_hi , command=self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "hi"))
        self.Checkbox_Frecuences_Polygon_hi_percent = Checkbutton(self.W_Export_Graph , text="Para hi%" , font=("Times New Roman" , 13) , textvariable=self.Checked_Frecuences_Polygon_hi_percent , command=self.Check_And_Block_Single_Checkbox("Frecuences_Polygon" , "hi_percent"))

        self.Checkbox_Acumulate_Frecuences_Polygon = Checkbutton(self.W_Export_Graph , text="Export Poligono de Frecuencias Acumuladas" , font=("Times New Roman" , 13) , textvariable=self.Checked_Acumulate_Frecuences_Polygon , command=self.Check_And_Block_Multiple_Checkboxes("Acumulate_Frecuences_Polygon"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Fi = Checkbutton(self.W_Export_Graph , text="Export Poligono de Frecuencias Acumuladas" , font=("Times New Roman" , 13) , textvariable=self.Checked_Acumulate_Frecuences_Polygon , command=self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Fi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi = Checkbutton(self.W_Export_Graph , text="Export Poligono de Frecuencias Acumuladas" , font=("Times New Roman" , 13) , textvariable=self.Checked_Acumulate_Frecuences_Polygon , command=self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Hi"))
        self.Checkbox_Acumulate_Frecuences_Polygon_Hi_percent = Checkbutton(self.W_Export_Graph , text="Export Poligono de Frecuencias Acumuladas" , font=("Times New Roman" , 13) , textvariable=self.Checked_Acumulate_Frecuences_Polygon , command=self.Check_And_Block_Single_Checkbox("Acumulate_Frecuences_Polygon" , "Hi_percent"))

        self.Dictionary_Of_Main_Checkboxes_Values = {
            "Histogram": self.Checked_Histogram,
            "Frecuences_Polygon": self.Checked_Frecuences_Polygon,
            "Acumulate_Frecuences_Polygon": self.Checked_Acumulate_Frecuences_Polygon,
        }
        self.Dictionary_Of_Subcheckboxes_Values = {
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

        self.Dictionary_Of_Main_Checkboxes_Widgets = {
            "Histogram": self.Checkbox_Histogram,
            "Frecuences_Polygon": self.Checkbox_Frecuences_Polygon,
            "Acumulate_Frecuences_Polygon": self.Checkbox_Acumulate_Frecuences_Polygon,
        }
        self.Dictionary_Of_Subcheckboxes_Widgets = {
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
    
        self.Create_Entry_Widgets(self.W_Export_Graph, self.Axis_x_Title)


class Widgets_Checkboxes_For_Export_Graphs(Widget_Input_Name_For_Graphs):
    def __init__(self , Root_Window , There_Are_Boxplot):
        Widget_Input_Name_For_Graphs.__init__(self , Root_Window , There_Are_Boxplot)
        self.W_Export_Graph = Root_Window
        self.There_Are_Boxplot = There_Are_Boxplot

        self.Checked_Export_All = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_All_Bars = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Bar_fi = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Bar_hi = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Bar_hi_percent = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Pie = BooleanVar(self.W_Export_Graph)
        self.Checked_Export_Boxplot = BooleanVar(self.W_Export_Graph)

    def Check_Export_All(self):
        if(self.Dictionary_Checkboxes):
            match(self.Dictionary_Checkboxes["All"][1].get()):
                case True:
                    for key , value in self.Dictionary_Checkboxes.items():
                        if(key != "All"):
                            value[0].config(state="disabled")
                            value[1].set(True)

                    self.Input_Name_Bar_Graph.config(state="normal")
                    self.Input_Name_Píe_Graph.config(state="normal")
                    if(self.Input_Name_Boxplot_Graph):
                        self.Input_Name_Boxplot_Graph.config(state="normal")
                case False:
                    for key , value in self.Dictionary_Checkboxes.items():
                        if(key != "All"):
                            value[0].config(state="normal")
                            value[1].set(False)
                        
                    self.Input_Name_Bar_Graph.config(state="disabled")
                    self.Name_Bar_Graph.set("")
                    self.Input_Name_Píe_Graph.config(state="disabled")
                    self.Name_Pie_Graph.set("")
                    if(self.Input_Name_Boxplot_Graph):
                        self.Input_Name_Boxplot_Graph.config(state="disabled")
                        self.Name_Boxplot_Graph.set("")

    def Checked_All_For_Inverse(self):
        All_Graphs = [checked[1].get() for i , checked in enumerate(self.Dictionary_Checkboxes.values()) if (i > 1)]
        if(all(All_Graphs)):
            self.Dictionary_Checkboxes["All"][0].config(state="disabled")
            self.Dictionary_Checkboxes["All"][1].set(True)
        else:
            self.Dictionary_Checkboxes["All"][0].config(state="normal")
            self.Dictionary_Checkboxes["All"][1].set(False)

    def Check_Export_All_Bars(self):
        if(self.Dictionary_Checkboxes):
            match(self.Dictionary_Checkboxes["All_Bars"][1].get()):
                case True:
                    for i , value in enumerate(self.Dictionary_Checkboxes.values()):
                        if(i > 1 and i < 5):
                            value[0].config(state="disabled")
                            value[1].set(True)

                    self.Input_Name_Bar_Graph.config(state="normal")
                case False:
                    for i , value in enumerate(self.Dictionary_Checkboxes.values()):
                        if(i > 1 and i < 5):
                            value[0].config(state="normal")
                            value[1].set(False)
                    self.Input_Name_Bar_Graph.config(state="disabled")
                    self.Name_Bar_Graph.set("")

            self.Checked_All_For_Inverse()

    def Check_Bars(self):
        Only_Bars = [checked[1].get() for i , checked in enumerate(self.Dictionary_Checkboxes.values()) if (i > 1 and i < 5)]
        if(all(Only_Bars)):
            self.Dictionary_Checkboxes["All_Bars"][0].config(state="disabled")
            self.Dictionary_Checkboxes["All_Bars"][1].set(True)
        else:
            self.Dictionary_Checkboxes["All_Bars"][0].config(state="normal")
            self.Dictionary_Checkboxes["All_Bars"][1].set(False)

        if(any(Only_Bars)):
            self.Input_Name_Bar_Graph.config(state="normal")
        else:
            self.Input_Name_Bar_Graph.config(state="disabled")
            self.Name_Bar_Graph.set("")

        self.Checked_All_For_Inverse()

    def Check_Pie(self):
        if(self.Dictionary_Checkboxes["Pie"][1].get()):
            self.Input_Name_Píe_Graph.config(state="normal")
        else:
            self.Input_Name_Píe_Graph.config(state="disabled")
            self.Name_Pie_Graph.set("")
        self.Checked_All_For_Inverse()

    def Check_Boxplot(self):
        if(self.Dictionary_Checkboxes["Boxplot"][1].get()):
            self.Input_Name_Boxplot_Graph.config(state="normal")
        else:
            self.Input_Name_Boxplot_Graph.config(state="disabled")
            self.Name_Boxplot_Graph.set("")
        self.Checked_All_For_Inverse()

    def Create_Widgets(self):
        Widget_Input_Name_For_Graphs.Create_Widgets(self)

        self.Checkbox_Export_All = Checkbutton(self.W_Export_Graph , text="Exportar todo" , font=("Times New Roman" , 13) , variable=self.Checked_Export_All , command=self.Check_Export_All , bg="#E7E4C1")
        self.Checkbox_Export_All_Bar_Graphs = Checkbutton(self.W_Export_Graph , text="Exportar todos los graficos de barras" , font=("Times New Roman" , 13) , variable=self.Checked_Export_All_Bars , command=self.Check_Export_All_Bars , bg="#E7E4C1")

        self.Checkbox_Export_bar_fi = Checkbutton(self.W_Export_Graph , text="Exportar grafico de barras de fi" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Bar_fi , bg="#E7E4C1" , command=self.Check_Bars)
        self.Checkbox_Export_bar_hi = Checkbutton(self.W_Export_Graph , text="Exportar grafico de barras de hi" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Bar_hi , bg="#E7E4C1" , command=self.Check_Bars)
        self.Checkbox_Export_bar_hi_percent = Checkbutton(self.W_Export_Graph , text="Exportar grafico de barras de hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Bar_hi_percent , bg="#E7E4C1" , command=self.Check_Bars)

        self.Checkbox_Export_pie = Checkbutton(self.W_Export_Graph , text="Exportar grafico de pastel" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Pie , bg="#E7E4C1" , command=self.Check_Pie)

        if(self.There_Are_Boxplot):
            self.Checked_Export_Boxplot.set(False)
            self.Checkbox_Export_Boxplot = Checkbutton(self.W_Export_Graph , text="Exportar grafico de cajas" , font=("Times New Roman" , 13) , variable=self.Checked_Export_Boxplot , command=self.Check_Boxplot , bg="#E7E4C1")
            
            self.Dictionary_Checkboxes = dict([
                ("All" , [self.Checkbox_Export_All , self.Checked_Export_All]),
                ("All_Bars" , [self.Checkbox_Export_All_Bar_Graphs , self.Checked_Export_All_Bars]),
                ("Bars_fi" , [self.Checkbox_Export_bar_fi , self.Checked_Export_Bar_fi]),
                ("Bar_hi" , [self.Checkbox_Export_bar_hi , self.Checked_Export_Bar_hi]),
                ("Bar_hi_percent" , [self.Checkbox_Export_bar_hi_percent , self.Checked_Export_Bar_hi_percent]),
                ("Pie" , [self.Checkbox_Export_pie , self.Checked_Export_Pie]),
                ("Boxplot" , [self.Checkbox_Export_Boxplot , self.Checked_Export_Boxplot])
            ])
        else:
            self.Checkbox_Export_Boxplot = None
            self.Checked_Export_Boxplot.set(True)

            self.Dictionary_Checkboxes = dict([
                ("All" , [self.Checkbox_Export_All , self.Checked_Export_All]),
                ("All_Bars" , [self.Checkbox_Export_All_Bar_Graphs , self.Checked_Export_All_Bars]),
                ("Bars_fi" , [self.Checkbox_Export_bar_fi , self.Checked_Export_Bar_fi]),
                ("Bar_hi" , [self.Checkbox_Export_bar_hi , self.Checked_Export_Bar_hi]),
                ("Bar_hi_percent" , [self.Checkbox_Export_bar_hi_percent , self.Checked_Export_Bar_hi_percent]),
                ("Pie" , [self.Checkbox_Export_pie , self.Checked_Export_Pie]),
            ])



    def Display_Widgets(self):
        self.Checkbox_Export_All.place(x=310 , y=260)
        self.Checkbox_Export_All_Bar_Graphs.place(x=350 , y=290)

        self.Checkbox_Export_bar_fi.place(x=380 , y=320)
        self.Checkbox_Export_bar_hi.place(x=380 , y=350)
        self.Checkbox_Export_bar_hi_percent.place(x=380 , y=380)

        self.Checkbox_Export_pie.place(x=350 , y=430)

        if(self.Checkbox_Export_Boxplot):
            self.Checkbox_Export_Boxplot.place(x=350 , y=460)

        Widget_Input_Name_For_Graphs.Display_Widgets(self)

    def Hidden_Widgets(self):
        self.Checkbox_Export_All.place_forget()
        self.Checkbox_Export_All_Bar_Graphs.place_forget()

        self.Checkbox_Export_bar_fi.place_forget()
        self.Checkbox_Export_bar_hi.place_forget()
        self.Checkbox_Export_bar_hi_percent.place_forget()

        self.Checkbox_Export_pie.place_forget()

        if(self.Checkbox_Export_Boxplot):
            self.Checkbox_Export_Boxplot.place_forget()

        Widget_Input_Name_For_Graphs.Hidden_Widgets(self)
class Widget_Combobox_For_DPI_And_Format():
    def __init__(self , Root_Window):
        self.W_Export_Graph = Root_Window
        self.Resolutions = [72 , 96 , 150 , 300 , 600 , 1200 , 2000]
        self.Formats = [".jpg" , ".png" , ".svg"]
        self.Sizes_In_pX = ["980x700" , "1280x720" , "1920x1080" , "2560x1440"] # (Width x Height)

    def Create_Widgets(self):
        self.Input_dpi = ttk.Combobox(self.W_Export_Graph , values=self.Resolutions , font=("Times New Roman", 13), state="readonly" , width=5)
        self.Input_dpi.set(self.Resolutions[0])

        self.Input_Sizes = ttk.Combobox(self.W_Export_Graph , values=self.Sizes_In_pX , font=("Times New Roman" , 13) , state="readonly" , width=10)
        self.Input_Sizes.set(self.Sizes_In_pX[0])

        self.Input_Format = ttk.Combobox(self.W_Export_Graph , values=self.Formats , font=("Times New Roman", 13), state="readonly" , width=4)
        self.Input_Format.set(self.Formats[0])

    def Display_Widgets(self):
        self.Input_dpi.place(x=250 , y=150)
        # self.Input_Sizes.place(x=670 , y=150) # Importacion con tamaño personalizado, caracteristica sin terminar
        self.Input_Format.place(x=820 , y=39)

    def Hidden_Widgets(self):
        self.Input_dpi.place_forget()
        self.Input_Format.place_forget()

class Widgets_For_W_Export_Graphs(Widgets_Checkboxes_For_Export_Graphs , Widget_Combobox_For_DPI_And_Format):
    def __init__(self , Root_Window , There_Are_Boxplot):
        Widgets_Checkboxes_For_Export_Graphs.__init__(self , Root_Window , There_Are_Boxplot)
        Widget_Combobox_For_DPI_And_Format.__init__(self , Root_Window)

    def Create_All_Widgets(self):
        Widgets_Checkboxes_For_Export_Graphs.Create_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Create_Widgets(self)

    def Display_All_Widgets(self):
        Widgets_Checkboxes_For_Export_Graphs.Display_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Display_Widgets(self)

    def Hidden_All_Widgets(self):
        Widgets_Checkboxes_For_Export_Graphs.Hidden_Widgets(self)
        Widget_Combobox_For_DPI_And_Format.Hidden_Widgets(self)

def Select_Path(W_Export_Graph , Path , Btn_Examine):
    Btn_Examine.config(state="disabled")
    File_Path = filedialog.askdirectory(title="Seleccione una carpeta")
    if File_Path:
        if(Path):
            Path.set("")
            Path.set(File_Path)
        else:
            Path.set(File_Path)

    W_Export_Graph.lift()
    Btn_Examine.config(state="normal")

def Create_Windows_Export_Graphs(W_Show_Graph , Graphs , Results_From_Single_Column , Results_From_Multiple_Columns):
    
    def Back_To_W_Show_Graph():
        Collection_Widgets_W_Export_Graph.clear()

        for widgets in W_Export_Graph.winfo_children():
            widgets.destroy()

        W_Export_Graph.grab_release()
        W_Export_Graph.quit()
        W_Export_Graph.destroy()

        W_Show_Graph.state(newstate="normal")
        W_Show_Graph.lift()
        W_Show_Graph.lift()
        W_Show_Graph.grab_set()

    def Hidden_All_Widgets():
        for Wid in Collection_Widgets_W_Export_Graph.values():
            Wid.Hidden_All_Widgets()

    def Display_Widgets_Acoording_Column_Name(Event = None):
        Selection = Select_Column.get()
        Hidden_All_Widgets()
        Collection_Widgets_W_Export_Graph[f"{Selection}"].Display_All_Widgets()
        if("boxplot_graph" in Graphs[f"{Selection}"]):
            Text_Change_Name_Boxplot.place(x=20 , y=610)
        else:
            Text_Change_Name_Boxplot.place_forget()

    W_Export_Graph = Toplevel(W_Show_Graph)
    W_Show_Graph.state(newstate="withdraw")

    W_Export_Graph.title("Exportar Graficos")
    W_Export_Graph.geometry("900x700+310+90")
    W_Export_Graph.lift()
    W_Export_Graph.grab_set()
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
    W_Export_Graph.iconphoto(False , Icon)
    W_Export_Graph.protocol("WM_DELETE_WINDOW" , Back_To_W_Show_Graph)

    File_Name = StringVar(W_Export_Graph)
    Path = StringVar(W_Export_Graph)
    Path.set("")
    Columns_Name = []
    Collection_Widgets_W_Export_Graph = {}
    Collection_Checkboxes = {}
    
    Section_1 = Label(W_Export_Graph , bg="#E4DBD5" , width=128 , height=14 , borderwidth=2 , relief="solid")
    Section_1.place(x=0 , y=0)

    Label_Input_File_Name = Label(W_Export_Graph , text="Nombre de la imagen (opcional): " , font=("Times New Roman" , 13) , bg="#E4DBD5")
    Label_Input_File_Name.place(x=20 , y=40)
    Input_File_Name = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=File_Name)
    Input_File_Name.place(x=250 , y=40 , width=560)
    Input_File_Name.focus()

    Label_Input_Páth = Label(W_Export_Graph , text="Ruta de exportacion: " , font=("Times New Roman" , 13) , bg="#E4DBD5")
    Label_Input_Páth.place(x=20 , y=80)
    Input_Path = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=Path , state="readonly")
    Input_Path.place(x=250 , y=80 , width=630)
    Btn_Examine = Button(W_Export_Graph , text="Examinar" , font=("Times New Roman" , 13) , command= lambda: Select_Path(W_Export_Graph , Path , Btn_Examine) , bg="#F3F3E9")
    Btn_Examine.place(x=40 , y=110)

    Label_Input_dpi = Label(W_Export_Graph ,text="Resolucion de la imagen (DPI): \n96 resolucion estandar \n>300 alta resolucion" , font=("Times New Roman" , 13) , justify=LEFT , bg="#E4DBD5")
    Label_Input_dpi.place(x=20 , y=150)

    Label_Input_Size = Label(W_Export_Graph , text="Tamaño de la imagen (px):\nOriginal 980x700" , font=("Times New Roman" , 13) , justify=LEFT , bg="#E4DBD5")
    # Label_Input_Size.place(x=470 , y=150)

    Section_2 = Label(W_Export_Graph , bg="#E7E4C1" , width=129 , height=32 , borderwidth=2 , relief="solid")
    Section_2.place(x=0 , y=214)

    Texto_Exportar_Graficos = Label(W_Export_Graph , text="Seleccione los graficos que exportara" , font=("Times New Roman" , 13) , bg="#E7E4C1")
    Texto_Exportar_Graficos.place(x=310 , y=239)

    Text_Change_Name_Bar_Graph = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de barras (opcional): " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Bar_Graph.place(x=20 , y=510)

    Text_Change_Name_Pie_Graph = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de pastel (opcional): " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")
    Text_Change_Name_Pie_Graph.place(x=20 , y=560)

    Text_Change_Name_Boxplot = Label(W_Export_Graph , text="Ingrese un titulo para el \ngrafico de cajas (opcional): " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E7E4C1")

    Btn_Export_Graph = Button(W_Export_Graph , text="Descargar graficos" , font=("Times New Roman" , 13) , width=30 , bg="#E4DBD5")
    Btn_Export_Graph.place(x=300 , y=660)
    if(Results_From_Single_Column):
        if(len(Results_From_Single_Column) == 1):
            Variable_Name , value = next(iter(Results_From_Single_Column.items()))
        else:
            Variable_Name = ""
        There_Are_Boxplot = "boxplot_graph" in Graphs

        if(There_Are_Boxplot):
            Text_Change_Name_Boxplot.place(x=20 , y=610)
        else:
            Text_Change_Name_Boxplot.place_forget()

        Widgets_W_Export_Graph = Widgets_For_W_Export_Graphs(W_Export_Graph , There_Are_Boxplot)

        Widgets_W_Export_Graph.Create_All_Widgets()
        Widgets_W_Export_Graph.Display_All_Widgets()

        Btn_Export_Graph.config(command= lambda: Export_Graph_As_Image(W_Show_Graph , W_Export_Graph , Graphs , File_Name.get() , Path.get() , Widgets_W_Export_Graph , Widgets_W_Export_Graph.Dictionary_Checkboxes , Variable_Name))

    elif(Results_From_Multiple_Columns):
        Label_Select_Column = Label(W_Export_Graph , text="Seleccione la columna: " , font=("Times New Roman" , 13) , justify=LEFT , bg="#E4DBD5") 
        Label_Select_Column.place(x=20 , y=10)
        Widgets_W_Export_Graph = None
        There_Are_Boxplot = [True if "boxplot_graph" in value else False for value in Graphs.values()]

        Select_Column = ttk.Combobox(W_Export_Graph , values=Columns_Name , font=("Courier New" , 13) , width=25 , state="readonly")
        
        for i , key in enumerate(Results_From_Multiple_Columns.keys()):
            Columns_Name.append(key)
            Widgets_W_Export_Graph = Widgets_For_W_Export_Graphs(W_Export_Graph , There_Are_Boxplot[i])
            Widgets_W_Export_Graph.Create_All_Widgets()

            Collection_Widgets_W_Export_Graph[f"{key}"] = Widgets_W_Export_Graph
            Collection_Checkboxes[f"{key}"] = Widgets_W_Export_Graph.Dictionary_Checkboxes

        Select_Column["values"] = Columns_Name
        Select_Column.set(Columns_Name[0])
        Select_Column.bind('<<ComboboxSelected>>' , Display_Widgets_Acoording_Column_Name)
        Select_Column.place(x=200 , y=10)

        Display_Widgets_Acoording_Column_Name()

        Btn_Export_Graph.config(command= lambda: Export_Graph_As_Image(W_Show_Graph , W_Export_Graph , Graphs , File_Name.get() , Path.get() , Collection_Widgets_W_Export_Graph , Collection_Checkboxes))
    else:
        raise Exception("No se pudieron encontrar los resultados.")

    W_Export_Graph.resizable(False , False)
    W_Export_Graph.mainloop()

if __name__ == "__main__":
    Create_Windows_Export_Graphs(None , None)