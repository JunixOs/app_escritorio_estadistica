from Calcs.Table_of_Frecuency.Graphs.For_Cualitative_Data import Graphs_For_Cualitative_Variable
from Calcs.Table_of_Frecuency.Graphs.For_Grouped_Data import Graphs_For_Grouped_Data
from Calcs.Table_of_Frecuency.Graphs.For_Not_Grouped_Data import Graphs_For_No_Grouped_Data
import copy
import pandas as pd

import threading

def Define_Axis_y_Title(Variable_Of_Frecuency):
    Axis_y_Title = []
    if(not isinstance(Variable_Of_Frecuency , list)):
        Variable_Of_Frecuency = list(Variable_Of_Frecuency)

    for variable_frecuency in Variable_Of_Frecuency:
        match(variable_frecuency):
            case "fi":
                Axis_y_Title.append("Frecuencia Absoluta (fi)")
            case "hi":
                Axis_y_Title.append("Frecuencia Relativa (hi)")
            case "hi_percent":
                Axis_y_Title.append("Frecuencia Relativa Porcentual (hi%)")
            case "Fi":
                Axis_y_Title.append("Frecuencia Absoluta Acumulada (Fi)")
            case "Hi":
                Axis_y_Title.append("Frecuencia Relativa Acumulada (Hi)")
            case "Hi_percent":
                Axis_y_Title.append("Frecuencias Relativa Porcentual Acumulada (HI%)")
            case _:
                Axis_y_Title.append("")

    return Axis_y_Title

def Create_Class_Generator_Of_Graphs(Class_Generator_Of_Graphs , Results_From_Calcs , Axis_x_Title):
    Class_Graph = None
    if(not Class_Generator_Of_Graphs):
        if("Frecuences_Cuant_Grouped" in Results_From_Calcs):
            Copy_Results_From_Calcs = copy.deepcopy(Results_From_Calcs["Frecuences_Cuant_Grouped"])
            All_Data_In_List = Results_From_Calcs["Variables_Cuant_Grouped"]["Data_List"]

            Copy_Results_From_Calcs = pd.DataFrame(Copy_Results_From_Calcs)
            Class_Graph = Graphs_For_Grouped_Data(Copy_Results_From_Calcs , All_Data_In_List , Axis_x_Title)
        elif("Frecuences_Cuant_Not_Grouped" in Results_From_Calcs):
            Copy_Results_From_Calcs = copy.deepcopy(Results_From_Calcs["Frecuences_Cuant_Not_Grouped"])

            Copy_Results_From_Calcs = pd.DataFrame(Copy_Results_From_Calcs)
            Class_Graph = Graphs_For_No_Grouped_Data(Copy_Results_From_Calcs , Axis_x_Title)

        elif("Frecuences_Cuali" in Results_From_Calcs):
            Copy_Results_From_Calcs = copy.deepcopy(Results_From_Calcs["Frecuences_Cuali"])

            Copy_Results_From_Calcs = pd.DataFrame(Copy_Results_From_Calcs)
            Class_Graph = Graphs_For_Cualitative_Variable(Copy_Results_From_Calcs , Axis_x_Title)
        else:
            Exception("No se encontro el tipo de dato adecuado.")

        Class_Generator_Of_Graphs.append(Class_Graph)


def Manage_All_Graphs_Draw(Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Figures , Class_Generator_Of_Graphs , Category_Graph , Variable_Of_Frecuency=None , W_Show_Graph=None , Class_Progress_Bar=None):
    #print(f"Thread {threading.get_ident()} empezando trabajo {Category_Graph}")
    Axis_y_Title = Define_Axis_y_Title(Variable_Of_Frecuency)

    Create_Class_Generator_Of_Graphs(Class_Generator_Of_Graphs , Results_From_Calcs , Axis_x_Title)
    for variable_frecuency , axis_y_title in zip(Variable_Of_Frecuency , Axis_y_Title):
        if("Frecuences_Cuant_Grouped" in Results_From_Calcs):
            Manage_Generation_Of_Graphs_For_Grouped_Data(Class_Generator_Of_Graphs , Dictionary_Of_Generated_Figures , variable_frecuency , axis_y_title , Category_Graph)

        elif("Frecuences_Cuant_Not_Grouped" in Results_From_Calcs):
            Manage_Generation_Of_Graphs_For_Not_Grouped_Data(Class_Generator_Of_Graphs , Dictionary_Of_Generated_Figures , variable_frecuency , axis_y_title , Category_Graph)

        elif("Frecuences_Cuali" in Results_From_Calcs):
            Manage_Generation_Of_Graphs_For_Cualitative_Data(Class_Generator_Of_Graphs , Dictionary_Of_Generated_Figures , variable_frecuency , axis_y_title , Category_Graph)

        else:
            raise Exception("No se pudo detectar el tipo de variable.")
    #print(f"Thread {threading.get_ident()} terminando trabajo {Category_Graph}")
    if(W_Show_Graph and Class_Progress_Bar):
        W_Show_Graph.after(0 , Class_Progress_Bar.Close_Progress_Bar)
        
def Manage_Generation_Of_Graphs_For_Grouped_Data(Class_Generator_Of_Graphs , Dictionary_Of_Generated_Figures , Variable_Of_Frecuency , Axis_y_Title , Category_Graph):
    Generator_Of_Graphs = Class_Generator_Of_Graphs[0]

    match(Category_Graph):
        case "Histogram":
            if(not F"Figure_Histogram_{Variable_Of_Frecuency}" in Dictionary_Of_Generated_Figures["Figure_Histogram"]):
                Figure_Histogram = Generator_Of_Graphs.Draw_Histograme(Variable_Of_Frecuency , Axis_y_Title)
                Dictionary_Of_Generated_Figures["Figure_Histogram"][f"Figure_Histogram_{Variable_Of_Frecuency}"] = Figure_Histogram
            
        case "Frecuences_Polygon":
            if(not f"Figure_Frecuences_Polygon_{Variable_Of_Frecuency}" in Dictionary_Of_Generated_Figures["Figure_Frecuences_Polygon"]):
                Figure_Frecuences_Polygon = Generator_Of_Graphs.Draw_Frecuences_Polygon(Variable_Of_Frecuency , Axis_y_Title)
                Dictionary_Of_Generated_Figures["Figure_Frecuences_Polygon"][f"Figure_Frecuences_Polygon_{Variable_Of_Frecuency}"] = Figure_Frecuences_Polygon
            
        case "Acumulate_Frecuences_Polygon":
            if(not F"Figure_Acumulate_Frecuences_Polygon_{Variable_Of_Frecuency}" in Dictionary_Of_Generated_Figures["Figure_Acumulate_Frecuences_Polygon"]):
                Figure_Acumulate_Frecuences_Polygon = Generator_Of_Graphs.Draw_Frecuences_Polygon(Variable_Of_Frecuency , Axis_y_Title , True)
                Dictionary_Of_Generated_Figures["Figure_Acumulate_Frecuences_Polygon"][f"Figure_Acumulate_Frecuences_Polygon_{Variable_Of_Frecuency}"] = Figure_Acumulate_Frecuences_Polygon

def Manage_Generation_Of_Graphs_For_Not_Grouped_Data(Class_Generator_Of_Graphs , Dictionary_Of_Generated_Figures , Variable_Of_Frecuency , Axis_y_Title , Category_Graph):
    Generator_Of_Graphs = Class_Generator_Of_Graphs[0]

    match(Category_Graph):
        case "Bars_Graph":
            if(not f"Figure_Bars_Graph_{Variable_Of_Frecuency}" in Dictionary_Of_Generated_Figures["Figure_Bars_Graph"]):

                Figure_Bars_Graph = Generator_Of_Graphs.Draw_Bars(Variable_Of_Frecuency , Axis_y_Title , 3)
                Dictionary_Of_Generated_Figures["Figure_Bars_Graph"][f"Figure_Bars_Graph_{Variable_Of_Frecuency}"] = Figure_Bars_Graph
            
        case "Stick_Graph":

            if(not f"Figure_Stick_Graph_{Variable_Of_Frecuency}" in Dictionary_Of_Generated_Figures["Figure_Stick_Graph"]):
                Figure_Stick_Graph = Generator_Of_Graphs.Draw_Bars(Variable_Of_Frecuency , Axis_y_Title , 3 , True)
                Dictionary_Of_Generated_Figures["Figure_Stick_Graph"][f"Figure_Stick_Graph_{Variable_Of_Frecuency}"] = Figure_Stick_Graph
            
        case "Step_Chart":

            if(not f"Figure_Step_Chart_{Variable_Of_Frecuency}" in Dictionary_Of_Generated_Figures["Figure_Step_Chart"]):
                Figure_Step_Chart = Generator_Of_Graphs.Draw_Step_Chart(Variable_Of_Frecuency , Axis_y_Title)
                Dictionary_Of_Generated_Figures["Figure_Step_Chart"][f"Figure_Step_Chart_{Variable_Of_Frecuency}"] = Figure_Step_Chart

def Manage_Generation_Of_Graphs_For_Cualitative_Data(Class_Generator_Of_Graphs , Dictionary_Of_Generated_Figures , Variable_Of_Frecuency , Axis_y_Title , Category_Graph):
    Generator_Of_Graphs = Class_Generator_Of_Graphs[0]

    match(Category_Graph):
        case "Simple_Bars":

            if(not f"Figure_Simple_Bars_{Variable_Of_Frecuency}" in Dictionary_Of_Generated_Figures["Figure_Simple_Bars"]):
                Figure_Simple_Bars_Graph = Generator_Of_Graphs.Draw_Simple_Bars(Variable_Of_Frecuency , 3 , Axis_y_Title)
                Dictionary_Of_Generated_Figures["Figure_Simple_Bars"][f"Figure_Simple_Bars_{Variable_Of_Frecuency}"] = Figure_Simple_Bars_Graph
                return Figure_Simple_Bars_Graph
            
        case "Pie":

            if(not f"Figure_Pie_{Variable_Of_Frecuency}" in Dictionary_Of_Generated_Figures["Figure_Pie"]):
                Figure_Pie_Graph = Generator_Of_Graphs.Draw_Pie_Graph()
                Dictionary_Of_Generated_Figures["Figure_Pie"][f"Figure_Pie_{Variable_Of_Frecuency}"] = Figure_Pie_Graph
                return Figure_Pie_Graph