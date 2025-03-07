import sys
import os
import copy
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Calcs.Graphs.Calc_Bar_Pie_Graphs import Draw_Graph_for_Each_Variable
from Calcs.Graphs.Calc_Boxplot import Draw_Boxplot_For_Single_Column_Data
from Window_Export_Graph import Create_Windows_Export_Graphs
from Window_Create_Multiple_Graphs import Create_Window_Multiple_Graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        if("Frecuences_Cuant_For_Many_Values" in self.Results):
            for a in range(0 , len(self.Results["Frecuences_Cuant_For_Many_Values"]["Intervals"])):
                if(a != len(self.Results["Frecuences_Cuant_For_Many_Values"]["Intervals"]) - 1):
                    self.Results["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(self.Results["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(self.Results["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" >"
                else:
                    self.Results["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(self.Results["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(self.Results["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" ]"

    def Generate_Graphs(self , Graphs):
        self.Modify_Intervals_Key()

        Graph = Draw_Graph_for_Each_Variable(self.Results , self.Precision , self.Variable_Name)

        bar_fi , pie_graph = Graph.Draw_Graph("fi")
        bar_hi = Graph.Draw_Graph("hi")
        bar_hi_percent = Graph.Draw_Graph("hi_percent")
        boxplot_graph = None

        if("Frecuences_Cuant_For_Many_Values" in self.Results):
            boxplot_graph = Draw_Boxplot_For_Single_Column_Data(self.Results["Variables_Cuant_For_Many_Values"]["Data_List"] , self.Variable_Name)

        elif("Frecuences_Cuant_Normal_Extended" in self.Results):
            boxplot_graph = Draw_Boxplot_For_Single_Column_Data(self.Results["Variables_Cuant_Normal_Extended"]["Data_List"] , self.Variable_Name)
        
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
        self.Checkbox_Show_Bar_fi = Checkbutton(self.W_Show_Graph , text="Segun fi" , font=("Times New Roman" , 13) , variable=self.Checked_Bar_fi ,  command= lambda: self.Only_Check_Single_Option("fi"))
        self.Checkbox_Show_Bar_hi = Checkbutton(self.W_Show_Graph , text="Segun hi" , font=("Times New Roman" , 13) , variable=self.Checked_Bar_hi , command= lambda: self.Only_Check_Single_Option("hi"))
        self.Checkbox_Show_Bar_hi_percent = Checkbutton(self.W_Show_Graph , text="Segun hi%" , font=("Times New Roman" , 13) , variable=self.Checked_Bar_hi_percent , command= lambda: self.Only_Check_Single_Option("hi_percent"))

        self.Checkbox_Pie_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de pastel" , font=("Times New Roman" , 13) , variable=self.Checked_Pie_Graph , command= lambda: self.Only_Check_Single_Option("pie"))

        self.Checkbox_Boxplot_Graph = None
        if(self.There_Are_Boxplot):
            self.Checkbox_Boxplot_Graph = Checkbutton(self.W_Show_Graph , text="Grafico de cajas" , font=("Times New Roman" , 13) , variable=self.Checked_Boxplot_Graph , command= lambda: self.Only_Check_Single_Option("boxplot"))

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
    
def Change_Key(dictionary, old_key, new_key):
    """ No modifica el diccionarrio, sino que genera uno nuevo , pero con las claves moficiadas """
    return {clave if clave != old_key else new_key: valor for clave, valor in dictionary.items()}

def Create_Window_Show_Graph(Father_Window , Results_From_Single_Column , Results_From_Multiple_Columns , Precision , Graphs):
    """ Esta es la funcion principal del modulo """
    def Back(W_Show_Graph):
        if(Results_From_Single_Column):
            if(len(Results_From_Single_Column) == 1):
                var_name , value = next(iter(Results_From_Single_Column.items()))
                if("Frecuences_Cuant_For_Many_Values" in value or "Frecuences_Cuant_Normal_Extended" in value):
                    Graphs.clear()
            elif("Frecuences_Cuant_For_Many_Values" in Results_From_Single_Column or "Frecuences_Cuant_Normal_Extended" in Results_From_Single_Column):
                Graphs.clear()

        elif(Results_From_Multiple_Columns):
            for var_name , value in Results_From_Multiple_Columns.items():
                if("Frecuences_Cuant_For_Many_Values" in value or "Frecuences_Cuant_Normal_Extended" in value):
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

    W_Show_Graph = Toplevel(Father_Window)
    W_Show_Graph.title("Ver graficos")
    W_Show_Graph.geometry("1300x700+105+105")
    W_Show_Graph.grab_set()
    Icon = PhotoImage(file="Images/icon.png")
    W_Show_Graph.iconphoto(False , Icon)

    Widgets_Collection = {}
    Checkboxes_Collection = {}

    W_Show_Graph.protocol("WM_DELETE_WINDOW", lambda: Back(W_Show_Graph))

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
                if(len(Results_From_Single_Column) == 1):
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
                There_Are_Graphics = True if Graphs else False

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

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar Graficos" , font=("Times New Roman" , 13) , width=15 , command= lambda: Create_Windows_Export_Graphs(W_Show_Graph , Graphs , Results_From_Single_Column , Results_From_Multiple_Columns))
    Btn_Export_Graph.place(x=90 , y=440)

    Btn_Create_And_Export_Multiple_Graphs = Button(W_Show_Graph , text="Crear y Exportar\nMultiples Graficos" , font=("Times New Roman" , 13) , width=24 , justify="center" , command= lambda: Create_Window_Multiple_Graphs(W_Show_Graph))
    Btn_Create_And_Export_Multiple_Graphs.place(x=50 , y=480)
    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()