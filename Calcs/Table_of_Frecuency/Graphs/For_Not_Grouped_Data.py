import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy

def pixels_to_inches(pixels, dpi=72):
    return pixels / dpi

class Graphs_For_No_Grouped_Data:
    def __init__(self , Copy_Results_From_Calcs , Axis_x_Title):
        self.Copy_Results_From_Calcs = Copy_Results_From_Calcs

        self.Bar_Title = ""

        self.Pie_Title = ""
        self.Axis_x_Title = Axis_x_Title

        if(not self.Axis_x_Title):
            self.Axis_x_Title = "Variables Observadas (xi)"
        
        self.Fig_Height = pixels_to_inches(700)
        self.Fig_Width = pixels_to_inches(980)

    def Draw_Bars(self , Variable_Of_Frecuency , Axis_y_Title , Precision , Draw_Stick_Graph=False):
        Figure_Bars = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)

        ax_Bars = Figure_Bars.add_subplot(111)
        Figure_Bars.subplots_adjust(bottom=0.15)
        
        if(Draw_Stick_Graph):
            Widht_Bars = 0.2
        else:
            Widht_Bars = 0.6

        Bars = ax_Bars.bar(self.Copy_Results_From_Calcs["xi"].astype(str) , self.Copy_Results_From_Calcs[f"{Variable_Of_Frecuency}"] , color="#69b3a2", edgecolor="black", width=Widht_Bars)

        ax_Bars.set_xticks(range(len(self.Copy_Results_From_Calcs["xi"])))
        ax_Bars.set_xticklabels(self.Copy_Results_From_Calcs["xi"] , fontsize=8 , rotation=35 , rotation_mode="anchor" , ha="right")

        ax_Bars.set_title(self.Bar_Title)

        ax_Bars.set_xlabel(f"{self.Axis_x_Title}" , labelpad=8)
        ax_Bars.set_ylabel(f"{Axis_y_Title}" , labelpad=10)

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
            if(Draw_Stick_Graph):
                ax_Bars.bar(Bar.get_x() + 0.24, height - (height * 0.001), width=Bar.get_width(), bottom=0, color='gray', alpha=0.5, zorder=1)
            else:
                ax_Bars.bar(Bar.get_x() + 0.24, height - (height * 0.01), width=Bar.get_width(), bottom=0, color='gray', alpha=0.5, zorder=1)

        for Spine in ["top", "right"]:
            Figure_Bars.gca().spines[Spine].set_visible(False)
        Figure_Bars.tight_layout()

        return Figure_Bars

    def Draw_Step_Chart(self , Variable_Of_Frecuency , Axis_y_label):
        Figure_Step_Chart = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)
        Axis = Figure_Step_Chart.add_subplot(111)

        Data_For_Graph = None
        Label_Format = None
        match(Variable_Of_Frecuency):
            case "Fi":
                Data_For_Graph = self.Copy_Results_From_Calcs["Fi"]
                Label_Format = "{:.0f}"
            case "Hi":
                Data_For_Graph = self.Copy_Results_From_Calcs["Hi"]
                Label_Format = "{:.3f}"
            case "Hi_percent":
                Data_For_Graph = self.Copy_Results_From_Calcs["Hi_percent"]
                Label_Format = "{:.3f}%"

        Axis.step(self.Copy_Results_From_Calcs["xi"] , Data_For_Graph , where="mid" , color="royalblue" , linewidth=2)
        Axis.plot(self.Copy_Results_From_Calcs["xi"] , Data_For_Graph , "o" , color="royalblue")

        for x , y in zip(self.Copy_Results_From_Calcs["xi"] , Data_For_Graph):
            Axis.text(x , y + max(Data_For_Graph)*0.02 , Label_Format.format(y) , ha="center" , va="bottom" , fontsize=10)

        Axis.set_xlabel(self.Axis_x_Title , labelpad=8)
        Axis.set_ylabel(Axis_y_label , labelpad=10)
        Axis.set_xticks(self.Copy_Results_From_Calcs["xi"])

        Axis.grid(axis='y', linestyle='--', alpha=0.5)

        for Spine in ["top" , "right"]:
            Figure_Step_Chart.gca().spines[Spine].set_visible(False)

        Figure_Step_Chart.tight_layout()

        return Figure_Step_Chart