import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy

def pixels_to_inches(pixels, dpi=72):
    return pixels / dpi

class Graphs_For_No_Grouped_Data:
    def __init__(self , Copy_Results_From_Calcs , Axis_x_Title , Axis_y_Title):
        self.Copy_Results_From_Calcs = Copy_Results_From_Calcs

        self.Bar_Title = ""

        self.Pie_Title = ""
        self.Axis_x_Title = Axis_x_Title
        self.Axis_y_Title = Axis_y_Title

        if(not self.Axis_x_Title):
            self.Axis_x_Title = "Variables Observadas (xi)"
        
        self.Fig_Height = pixels_to_inches(700)
        self.Fig_Width = pixels_to_inches(980)

    def Draw_Bars(self , Variable_Of_Frecuency , Precision , Draw_Stick_Graph=False):
        figure_bars = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)

        ax_Bars = figure_bars.add_subplot(111)
        figure_bars.subplots_adjust(bottom=0.15)
        
        if(Draw_Stick_Graph):
            Widht_Bars = 0.1
        else:
            Widht_Bars = 0.6

        Bars = ax_Bars.bar(self.Copy_Results_From_Calcs["xi"].astype(str) , self.Copy_Results_From_Calcs[f"{Variable_Of_Frecuency}"] , color="#69b3a2", edgecolor="black", width=Widht_Bars)

        ax_Bars.set_xticks(range(len(self.Copy_Results_From_Calcs["xi"])))
        ax_Bars.set_xticklabels(self.Copy_Results_From_Calcs["xi"] , fontsize=8 , rotation=30 , rotation_mode="anchor" , ha="right")

        ax_Bars.set_title(self.Bar_Title)

        ax_Bars.set_xlabel(f"{self.Axis_x_Title}")
        ax_Bars.set_ylabel(f"{self.Axis_y_Title}")

        ax_Bars.grid(axis="y", linestyle="--", alpha=0.5)

        for Bar in Bars:
            height = Bar.get_height()
            if Variable_Of_Frecuency == "fi":
                ax_Bars.text(Bar.get_x() + (Bar.get_width() / 2), height + (height * 0.01), f"{int(height)}" , ha="center", va="bottom", fontsize=10)
            elif Variable_Of_Frecuency == "hi":
                ax_Bars.text(Bar.get_x() + (Bar.get_width() / 2), height + (height * 0.01), f"{height:.{Precision}f}" , ha="center", va="bottom", fontsize=10)
            elif Variable_Of_Frecuency == "hi_percent":
                ax_Bars.text(Bar.get_x() + (Bar.get_width() / 2), height + (height * 0.01), f"{height:.{Precision}f}%" , ha="center", va="bottom", fontsize=10)
            
            Bar.set_zorder(2)
            # Agregar una sombra (simulando un desplazamiento)
            ax_Bars.bar(Bar.get_x() + 0.24, height - (height * 0.01), width=Bar.get_width(), bottom=0, color='gray', alpha=0.5, zorder=1)

        for Spine in ["top", "right"]:
            figure_bars.gca().spines[Spine].set_visible(False)
        figure_bars.tight_layout()

        return figure_bars

    def Draw_Step_Chart(self , Variable_Of_Frecuency):
        pass
        
def Manage_Generation_Of_Graphs_For_Not_Grouped_Data(Results_From_Calcs , Class_Generator_Of_Graphs , Generated_Graphs , Checkbox_Graphs , **Extra_Params):
    Name_Graph , Checkbox_Value = next(iter(Checkbox_Graphs.items()))

    if(not Class_Generator_Of_Graphs):
        Copy_Results_From_Calcs = copy.deepcopy(Results_From_Calcs["Frecuences_Cuant_Not_Grouped"])
        Copy_Results_From_Calcs = pd.DataFrame(Copy_Results_From_Calcs)

        Class_Graph = Graphs_For_No_Grouped_Data(Copy_Results_From_Calcs , Extra_Params["Axis_x_Title"] , Extra_Params["Axis_y_Title"])
        Class_Generator_Of_Graphs.append(Class_Graph)

    match(Name_Graph):
        case "Bars_Graph":
            if(not "Bars_Graph" in Generated_Graphs and Checkbox_Value.get()):

                Figure_Bars_Graph = Class_Generator_Of_Graphs[0].Draw_Bars(Extra_Params["Variable_Of_Frecuency"] , 3)
                Generated_Graphs["Figure_Bars_Graph"][f"Figure_Bars_Graph_{Extra_Params['Variable_Of_Frecuency']}"] = Figure_Bars_Graph
                return Figure_Bars_Graph
            
        case "Stick_Graph":

            if(not "Stick_Graph" in Generated_Graphs and Checkbox_Value.get()):
                Figure_Stick_Graph = Class_Generator_Of_Graphs[0].Draw_Bars(Extra_Params["Variable_Of_Frecuency"] , 3 , True)
                Generated_Graphs["Figure_Stick_Graph"][f"Figure_Stick_Graph_{Extra_Params['Variable_Of_Frecuency']}"] = Figure_Stick_Graph
                return Figure_Stick_Graph
            
        case "Step_Chart":

            if(not "Step_Chart" in Generated_Graphs and Checkbox_Value.get()):
                Figure_Step_Chart = Class_Generator_Of_Graphs[0].Draw_Step_Chart()
                Generated_Graphs["Figure_Step_Chart"][f"Figure_Step_Chart_{Extra_Params['Variable_Of_Frecuency']}"] = Figure_Step_Chart
                return Figure_Step_Chart