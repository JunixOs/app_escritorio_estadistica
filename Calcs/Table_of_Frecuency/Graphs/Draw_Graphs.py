from Calcs.Table_of_Frecuency.Graphs.For_Cualitative_Data import Manage_Generation_Of_Graphs_For_Cualitative_Data
from Calcs.Table_of_Frecuency.Graphs.For_Grouped_Data import Manage_Generation_Of_Graphs_For_Grouped_Data
from Calcs.Table_of_Frecuency.Graphs.For_Not_Grouped_Data import Manage_Generation_Of_Graphs_For_Not_Grouped_Data
import copy
import pandas as pd


def Manage_All_Graphs_Draw(Results_From_Calcs , Axis_x_Title , Dictionary_Of_Generated_Graphs , Class_Generator_Of_Graphs , Checkbox_Graph , Variable_Of_Frecuency=None):
    match(Variable_Of_Frecuency):
        case "fi":
            Axis_y_Title = "Frecuencia Absoluta (fi)"
        case "hi":
            Axis_y_Title = "Frecuencia Relativa (hi)"
        case "hi_percent":
            Axis_y_Title = "Frecuencia Relativa Porcentual (hi%)"
        case "Fi":
            Axis_y_Title = "Frecuencia Absoluta Acumulada (Fi)"
        case "Hi":
            Axis_y_Title = "Frecuencia Relativa Acumulada (Hi)"
        case "Hi_percent":
            Axis_y_Title = "Frecuencias Relativa Porcentual Acumulada (HI%)"
        case _:
            Exception("Error al verificar la frecuencia.")

    if("Frecuences_Cuant_Grouped" in Results_From_Calcs):
        Manage_Generation_Of_Graphs_For_Grouped_Data(Results_From_Calcs , Class_Generator_Of_Graphs , Dictionary_Of_Generated_Graphs , Checkbox_Graph , Axis_y_Title=Axis_y_Title)

    elif("Frecuences_Cuant_Not_Grouped" in Results_From_Calcs):
        Manage_Generation_Of_Graphs_For_Not_Grouped_Data(Results_From_Calcs , Class_Generator_Of_Graphs , Dictionary_Of_Generated_Graphs , Checkbox_Graph , Axis_x_Title=Axis_x_Title , Axis_y_Title=Axis_y_Title , Variable_Of_Frecuency=Variable_Of_Frecuency)

    elif("Frecuences_Cuali" in Results_From_Calcs):
        Manage_Generation_Of_Graphs_For_Cualitative_Data(Results_From_Calcs , Class_Generator_Of_Graphs , Dictionary_Of_Generated_Graphs , Checkbox_Graph , Axis_x_Title=Axis_x_Title , Axis_y_Title=Axis_y_Title , Variable_Of_Frecuency=Variable_Of_Frecuency)

    else:
        raise Exception("No se pudo detectar el tipo de variable.")