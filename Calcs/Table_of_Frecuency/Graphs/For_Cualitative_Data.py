import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy

def pixels_to_inches(pixels, dpi=72):
    return pixels / dpi

class Graphs_For_Cualitative_Variable:
    def __init__(self , Copy_Results_From_Calcs , Axis_x_Title , Axis_y_Title):
        self.Copy_Results_From_Calcs = Copy_Results_From_Calcs

        self.Bar_Title = ""

        self.Pie_Title = ""
        self.Axis_x_Title = Axis_x_Title
        self.Axis_y_Title = Axis_y_Title

        if(not self.Axis_x_Title):
            self.Axis_x_Title = "Variables Observadas (ai)"

        self.Fig_Height = pixels_to_inches(700)
        self.Fig_Width = pixels_to_inches(980)

    def Draw_Simple_Bars(self , Variable_Of_Frecuency , Precision):
        figure_bars = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)

        ax_Bars = figure_bars.add_subplot(111)
        figure_bars.subplots_adjust(bottom=0.15)
        

        Bars = ax_Bars.bar(self.Copy_Results_From_Calcs["ai"].astype(str) , self.Copy_Results_From_Calcs[f"{Variable_Of_Frecuency}"] , color="#69b3a2", edgecolor="black", width=0.6)

        ax_Bars.set_xticks(range(len(self.Copy_Results_From_Calcs["ai"])))
        ax_Bars.set_xticklabels(self.Copy_Results_From_Calcs["ai"] , fontsize=8 , rotation=30 , rotation_mode="anchor" , ha="right")

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

    def Draw_Pie_Graph(self):
        """ Modificar para que los datos se muestren de mejor manera. """
        figure_pie = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)
        ax_pie = figure_pie.add_subplot(111)

        values = self.Copy_Results_From_Calcs["hi_percent"]

        # Ajuste de las porciones más pequeñas
        explode = [0.12 if v < max(values) * 0.1 else 0.04 for v in values]

        # Agregar el gráfico de pastel
        wedges, texts, autotexts = ax_pie.pie(
            values,
            labels=self.Copy_Results_From_Calcs["ai"],
            autopct="%1.1f%%",
            startangle=90,
            labeldistance=1.1,  # Aleja las etiquetas de los centro
            explode=explode,  # Separar las porciones
            shadow= True,
            pctdistance=0.85,   # Distancia de los porcentajes del centro
            wedgeprops={"edgecolor": "black"},
            textprops={"fontsize": 10}
        )
        max_w = len(wedges) + 1
        for i, wedge in enumerate(wedges):
            # Obtenemos el centro de cada wedge, sin necesidad de calcular ángulos.
            center_x, center_y = wedge.center

            arrow_x = center_x * 24.5
            arrow_y = center_y * 24.5

            angle_start, angle_end = wedge.theta1, wedge.theta2

            # Calcular el ángulo central
            angle = (angle_start + angle_end) / 2

            # Convertir el ángulo a radianes
            angle_rad = np.deg2rad(angle)

            # La longitud de la etiqueta para determinar el desplazamiento
            label_text = texts[i].get_text()
            label_length = len(label_text)
            
            # Ajuste dinámico de la distancia en función de la longitud de la etiqueta
            
            label_distance = 1.20 + (np.log10(2*label_length/11) * 0.001)  # Ajusta este factor si es necesario

            # Calculamos las coordenadas x, y de la etiqueta basándonos en el ángulo central
            if(center_x > 0):
                label_x = label_distance * np.cos(angle_rad)
                label_y = label_distance * np.sin(angle_rad)
            else:
                if(label_length <= 20):
                    label_x = (label_distance * np.cos(angle_rad)) - ((label_length + 1.7)/(35 * np.log10(label_length + 1.7))-0.08)
                elif(label_length > 20 and label_length < 30):
                    label_x = (label_distance * np.cos(angle_rad)) - ((label_length + 1.7)/(33 * np.log10(label_length + 1.7))-0.08)
                else:
                    label_x = (label_distance * np.cos(angle_rad)) - ((label_length + 1.7)/(27 * np.log10(label_length + 1.7))-0.08)
                label_y = (label_distance * np.sin(angle_rad)) - (max_w/8000)

            # Ahora usamos `annotate` para crear la línea de conexión desde el centro de cada wedge hacia la etiqueta.
            ax_pie.annotate(
                label_text,  # El texto de la etiqueta
                xy=(arrow_x , arrow_y),  # Coordenadas del centro del pedazo del pastel (wedge)
                xytext=(label_x, label_y),  # Las coordenadas de la etiqueta fuera del gráfico
                textcoords='data',  # Usamos coordenadas de datos para las etiquetas fuera del gráfico
                arrowprops=dict(arrowstyle="->", color="black", lw=1),  # Línea de conexión
                fontsize=10
            )

        for text in texts:
            text.set_visible(False)

        ax_pie.set_facecolor('lightgray')
        ax_pie.set_title(self.Pie_Title)

        plt.tight_layout()

        ax_pie.axis("equal")

        return figure_pie
    
def Manage_Generation_Of_Graphs_For_Cualitative_Data(Results_From_Calcs , Class_Generator_Of_Graphs , Generated_Graphs , Checkbox_Graphs , **Extra_Params):
    Name_Graph , Checkbox_Value = next(iter(Checkbox_Graphs.items()))

    if(not Class_Generator_Of_Graphs):
        Copy_Results_From_Calcs = copy.deepcopy(Results_From_Calcs["Frecuences_Cuant_Not_Grouped"])
        Copy_Results_From_Calcs = pd.DataFrame(Copy_Results_From_Calcs)

        Class_Graph = Graphs_For_Cualitative_Variable(Copy_Results_From_Calcs , Extra_Params["Axis_x_Title"] , Extra_Params["Axis_y_Title"])
        Class_Generator_Of_Graphs.append(Class_Graph)

    match(Name_Graph):
        case "Simple_Bars_Graph":

            if(not "Simple_Bars_Graph" in Generated_Graphs and Checkbox_Value.get()):
                Figure_Simple_Bars_Graph = Class_Generator_Of_Graphs[0].Draw_Simple_Bars(Extra_Params["Variable_Of_Frecuency"] , 3)
                Generated_Graphs["Figure_Simple_Bars_Graph"] = Figure_Simple_Bars_Graph
                return Figure_Simple_Bars_Graph
            
        case "Pie_Graph":

            if(not "Pie_Graph" in Generated_Graphs and Checkbox_Value.get()):
                Figure_Pie_Graph = Class_Generator_Of_Graphs[0].Draw_Pie_Graph()
                Generated_Graphs["Figure_Pie_Graph"] = Figure_Pie_Graph
                return Figure_Pie_Graph