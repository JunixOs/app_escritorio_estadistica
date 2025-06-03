import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy

def pixels_to_inches(pixels, dpi=72):
    return pixels / dpi

class Graphs_For_Grouped_Data:
    def __init__(self , Copy_Results_From_Calcs , All_Data_In_List , Axis_x_Title , Axis_y_Title):
        self.Copy_Results_From_Calcs = Copy_Results_From_Calcs
        self.All_Data_In_list = All_Data_In_List

        self.Bar_Title = ""

        self.Pie_Title = ""
        self.Axis_x_Title = Axis_x_Title
        self.Axis_y_Title = Axis_y_Title

        if(not self.Axis_x_Title):
            self.Axis_x_Title = "Intervalos de Clase"

        self.Fig_Height = pixels_to_inches(700)
        self.Fig_Width = pixels_to_inches(980)

    def Draw_Histograme(self):
        plt.style.use('ggplot')

        Inferior_Limits = [li for li in self.Copy_Results_From_Calcs["Intervals"]]

        Figure_Histogram= plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)
        Axis = Figure_Histogram.add_subplot(111)

        Frecuences , Edges , _ = Axis.hist(
            self.All_Data_In_List,
            bins=self.Copy_Results_From_Calcs["Intervals"], 
            edgecolor='white',       # Borde blanco moderno
            align='mid', 
            rwidth=1,              # Ajuste fino del ancho de barra
            color='#69b3a2',         # Color suave y moderno
            alpha=0.8
        )

        for i in range(len(Frecuences)):
            Height = Frecuences[i]
            Center = (Edges[i] + Edges[i + 1]) / 2
            Axis.text(
                Center,
                Height + (Height * 0.02),
                str(int(Height)),
                ha="center",
                va="bottom",
            )
        Axis.set_xticks(Inferior_Limits)
        # Opcional: Etiquetas y estilo
        Axis.set_xlabel(self.Axis_x_Title)
        Axis.set_ylabel("Frecuencia")

        Axis.set_xticks(Inferior_Limits)
        Axis.set_xticklabels(
            Inferior_Limits, rotation=30, rotation_mode="anchor", ha="right"
        )

        for Spine in ["top", "right"]:
            Figure_Histogram.gca().spines[Spine].set_visible(False)

        Axis.grid(axis="y", linestyle="--", alpha=0.4)
        Figure_Histogram.tight_layout()

        return Figure_Histogram

    def Draw_Frecuences_Polygon(self , Draw_Cumulative_Graph=False):
        plt.style.use('ggplot')

        Inferior_Limits = [li for li in self.Copy_Results_From_Calcs["Intervals"]]

        Figure_Frecuences_Polygon = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)
        Axis = Figure_Frecuences_Polygon.add_subplot(111)

        Frecuences , Edges , _ = Axis.hist(
            self.All_Data_In_List, 
            bins=self.Copy_Results_From_Calcs["Intervals"],
            cumulative=Draw_Cumulative_Graph, 
            edgecolor='white',       # Borde blanco moderno
            align='mid', 
            rwidth=1,              # Ajuste fino del ancho de barra
            color='#69b3a2',         # Color suave y moderno
            alpha=0.8
        )

        Middle_Points = 0.5 * (Edges[:-1] + Edges[1:])
        if(Draw_Cumulative_Graph):
            Data_For_Line_Graph = np.cumsum(Frecuences)
        else:
            Data_For_Line_Graph = Frecuences
        
        Axis.plot(
            Middle_Points, 
            Data_For_Line_Graph,
            color='crimson', 
            linewidth=2, 
            marker='o', 
            markersize=6,
            markerfacecolor='white',
            markeredgewidth=2
        )

        for i in range(len(Frecuences)):
            Height = Frecuences[i]
            Axis.text(
                Middle_Points[i],
                Height + (Height * 0.02),
                str(int(Height)),
                ha="center",
                va="bottom",
            )


        Axis.set_xticks(Inferior_Limits)
        # Opcional: Etiquetas y estilo
        Axis.set_xlabel(self.Axis_x_Title)
        Axis.set_ylabel("Frecuencia")

        Axis.set_xticks(Inferior_Limits)
        Axis.set_xticklabels(
            Inferior_Limits, rotation=30, rotation_mode="anchor", ha="right"
        )

        for Spine in ["top", "right"]:
            Figure_Frecuences_Polygon.gca().spines[Spine].set_visible(False)

        Axis.grid(axis="y", linestyle="--", alpha=0.4)
        Figure_Frecuences_Polygon.tight_layout()

        return Figure_Frecuences_Polygon

def Manage_Generation_Of_Graphs_For_Grouped_Data(Results_From_Calcs , Class_Generator_Of_Graphs , Dictionary_Of_Generated_Graphs , Checkbox_Graph , **Extra_Params):
    Name_Graph , Checkbox_Value = Checkbox_Graph[0] , Checkbox_Graph[1]

    if(not Class_Generator_Of_Graphs):
        Copy_Results_From_Calcs = copy.deepcopy(Results_From_Calcs["Frecuences_Cuant_Grouped"])
        All_Data_In_List = Results_From_Calcs["Variables_Cuant_Grouped"]["Data_List"]
        Copy_Results_From_Calcs = pd.DataFrame(Copy_Results_From_Calcs)

        Class_Graph = Graphs_For_Grouped_Data(Copy_Results_From_Calcs , All_Data_In_List , Extra_Params["Axis_x_Title"] , Extra_Params["Axis_y_Title"])
        Class_Generator_Of_Graphs.append(Class_Graph)
    
    match(Name_Graph):
        case "Histogram":

            if(not "Histogram" in Dictionary_Of_Generated_Graphs and Checkbox_Value.get()):
                Figure_Histograme = Class_Generator_Of_Graphs[0].Draw_Histograme()
                Dictionary_Of_Generated_Graphs["Figure_Histograme"] = Figure_Histograme
                return Figure_Histograme
            
        case "Frecuences_Polygon_Graph":
            
            if(not "Frecuences_Polygon" in Dictionary_Of_Generated_Graphs and Checkbox_Value.get()):
                Figure_Frecuences_Polygon = Class_Generator_Of_Graphs[0].Draw_Frecuences_Polygon()
                Dictionary_Of_Generated_Graphs["Figure_Frecuences_Polygon"] = Figure_Frecuences_Polygon
                return Figure_Frecuences_Polygon
            
        case "Acumulate_Frecuences_Polygon_Graph":

            if(not "Acumulate_Frecuences_Polygon" in Dictionary_Of_Generated_Graphs and Checkbox_Value.get()):
                Figure_Acumulate_Frecuences_Polygon = Class_Generator_Of_Graphs[0].Draw_Frecuences_Polygon(True)
                Dictionary_Of_Generated_Graphs["Figure_Acumulate_Frecuences_Polygon"] = Figure_Acumulate_Frecuences_Polygon
                return Figure_Acumulate_Frecuences_Polygon