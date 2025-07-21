import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def pixels_to_inches(pixels, dpi=72):
    return pixels / dpi

class Graphs_For_Grouped_Data:
    def __init__(self , Copy_Results_From_Calcs , All_Data_In_List , Axis_x_Title):
        self.Copy_Results_From_Calcs = Copy_Results_From_Calcs
        self.All_Data_In_List = All_Data_In_List

        self.Bar_Title = ""

        self.Pie_Title = ""
        self.Axis_x_Title = Axis_x_Title

        if(not self.Axis_x_Title):
            self.Axis_x_Title = "Intervalos de Clase"

        self.Fig_Height = pixels_to_inches(700)
        self.Fig_Width = pixels_to_inches(980)

    def Draw_Histograme(self , Variable_Of_Frecuency , Axis_y_Title):
        plt.style.use('ggplot')

        Is_Relative_Frecuence = False
        Is_Percent = False
        weights = None
        total = len(self.All_Data_In_List)
        match(Variable_Of_Frecuency):
            case "hi":
                weights = (np.ones_like(self.All_Data_In_List) / total)
                Is_Relative_Frecuence = True
            case "hi_percent":
                weights = (np.ones_like(self.All_Data_In_List) / total) * 100
                Is_Relative_Frecuence = True
                Is_Percent = True

        Inferior_Limits = [limit[0] for limit in self.Copy_Results_From_Calcs["Intervals"]]
        N_Intervals = len(self.Copy_Results_From_Calcs["Intervals"])
        Inferior_Limits.append(self.Copy_Results_From_Calcs["Intervals"][N_Intervals - 1][1])

        Figure_Histogram= plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)
        Axis = Figure_Histogram.add_subplot(111)
    
        Frecuences , Edges , _ = Axis.hist(
            self.All_Data_In_List,
            bins=Inferior_Limits, 
            edgecolor='white',       # Borde blanco moderno
            align='mid', 
            rwidth=1,              # Ajuste fino del ancho de barra
            color='#69b3a2',         # Color suave y moderno
            alpha=0.8,
            weights=weights,
        )

        for i in range(len(Frecuences)):
            Height = Frecuences[i]
            Center = (Edges[i] + Edges[i + 1]) / 2
            if(Is_Percent):
                Label = f"{Height:.3f}%"
            elif(Is_Relative_Frecuence):
                Label = f"{Height:.3}"
            else:
                Label = str(int(Height))
            Axis.text(
                Center,
                Height + (Height * 0.02),
                Label,
                ha="center",
                va="bottom",
            )
        Axis.set_xticks(Inferior_Limits)
        # Opcional: Etiquetas y estilo
        Axis.set_xlabel(self.Axis_x_Title , labelpad=8 , fontweight='bold')
        Axis.set_ylabel(Axis_y_Title , labelpad=10 , fontweight='bold')

        Axis.set_xticks(Inferior_Limits)
        Axis.set_xticklabels(
            Inferior_Limits, rotation=35, rotation_mode="anchor", ha="right"
        )

        for Spine in ["top", "right"]:
            Figure_Histogram.gca().spines[Spine].set_visible(False)

        Axis.grid(axis="y", linestyle="--", alpha=0.4)
        Figure_Histogram.tight_layout()

        return Figure_Histogram

    def Draw_Frecuences_Polygon(self , Variable_Of_Frecuency , Axis_y_Title , Draw_Cumulative_Graph=False):
        plt.style.use('ggplot')

        Inferior_Limits = [limit[0] for limit in self.Copy_Results_From_Calcs["Intervals"]]
        N_Intervals = len(self.Copy_Results_From_Calcs["Intervals"])
        Inferior_Limits.append(self.Copy_Results_From_Calcs["Intervals"][N_Intervals - 1][1])

        Figure_Frecuences_Polygon = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)
        Axis = Figure_Frecuences_Polygon.add_subplot(111)

        weights = None
        Is_Relative_Frecuence = False
        Is_Percent = False
        total = len(self.All_Data_In_List)
        if(Draw_Cumulative_Graph):
            match(Variable_Of_Frecuency):
                case "Hi":
                    weights = (np.ones_like(self.All_Data_In_List) / total)
                    Is_Relative_Frecuence = True
                case "Hi_percent":
                    weights = (np.ones_like(self.All_Data_In_List) / total) * 100
                    Is_Relative_Frecuence = True
                    Is_Percent = True
        else:
            match(Variable_Of_Frecuency):
                case "hi":
                    weights = (np.ones_like(self.All_Data_In_List) / total)
                    Is_Relative_Frecuence = True
                case "hi_percent":
                    weights = (np.ones_like(self.All_Data_In_List) / total) * 100
                    Is_Relative_Frecuence = True
                    Is_Percent = True

        Frecuences , Edges , _ = Axis.hist(
            self.All_Data_In_List, 
            bins=Inferior_Limits,
            cumulative=Draw_Cumulative_Graph, 
            edgecolor='white',       # Borde blanco moderno
            align='mid', 
            rwidth=1,              # Ajuste fino del ancho de barra
            color='#69b3a2',         # Color suave y moderno
            alpha=0.8,
            weights=weights,
        )

        Middle_Points = 0.5 * (Edges[:-1] + Edges[1:])
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
            if(Is_Percent):
                Label = f"{Height:.3f}%"
            elif(Is_Relative_Frecuence):
                Label = f"{Height:.3f}"
            else:
                Label = str(int(Height))
            Axis.text(
                Middle_Points[i],
                Height + (Height * 0.02),
                Label,
                ha="center",
                va="bottom",
            )

        Axis.set_xticks(Inferior_Limits)
        # Opcional: Etiquetas y estilo
        Axis.set_xlabel(self.Axis_x_Title , labelpad=8 , fontweight='bold')
        Axis.set_ylabel(Axis_y_Title , labelpad=10 , fontweight='bold')

        Axis.set_xticks(Inferior_Limits)
        Axis.set_xticklabels(
            Inferior_Limits, rotation=35, rotation_mode="anchor", ha="right"
        )

        for Spine in ["top", "right"]:
            Figure_Frecuences_Polygon.gca().spines[Spine].set_visible(False)

        Axis.grid(axis="y", linestyle="--", alpha=0.4)
        Figure_Frecuences_Polygon.tight_layout()

        return Figure_Frecuences_Polygon

    def Draw_Boxplot_Graph(self):
        sns.set_theme(style="whitegrid")

        Figure_Boxplot = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)
        Axis = Figure_Boxplot.add_subplot(111)

        Box = Axis.boxplot(self.All_Data_In_List , patch_artist=True , flierprops=dict(markerfacecolor='red', marker='o', markersize=8))

        Colors = ['skyblue', 'lightgreen', 'lightcoral', 'khaki', 'plum']

        for patch , color in zip(Box['boxes'], Colors):
            patch.set_facecolor(color)

        # Cambiar el color de la mediana, bigotes y caps (opcional)
        for median in Box['medians']:
            median.set_color('black')

        for whisker in Box['whiskers']:
            whisker.set_color('gray')

        for cap in Box['caps']:
            cap.set_color('gray')

        Axis.set_xlabel(self.Axis_x_Title, fontsize=10 , labelpad=8 , fontweight='bold')
        Axis.set_ylabel("Valores de los datos", fontsize=10 , labelpad=10 , fontweight='bold')

        Figure_Boxplot.tight_layout()

        return Figure_Boxplot