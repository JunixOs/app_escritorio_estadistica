import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy

def pixels_to_inches(pixels, dpi=72):
    return pixels / dpi

class Draw_Graph_for_Each_Variable:
    def __init__(self , Data , Precision , Axis_x_Title):
        self.Data = Data
        self.Precision = Precision

        self.Bar_Title = ""

        self.Pie_Title = ""
        self.Axis_x_Title = Axis_x_Title
        self.Axis_y_Title = None

        self.Fig_Height = pixels_to_inches(700)
        self.Fig_Width = pixels_to_inches(980)

    def Draw_Bars(self , Copy_Data , Variable_Of_Frecuency , Variable_To_Access):
        figure_bars = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)

        ax_Bars = figure_bars.add_subplot(111)  
        figure_bars.subplots_adjust(bottom=0.15)

        Bars = ax_Bars.bar(Copy_Data[f"{Variable_To_Access}"].astype(str) , Copy_Data[f"{Variable_Of_Frecuency}"] , color="skyblue" , width=0.6)

        ax_Bars.set_xticks(range(len(Copy_Data[f"{Variable_To_Access}"])))
        ax_Bars.set_xticklabels(Copy_Data[f"{Variable_To_Access}"] , fontsize=8 , rotation=30 , rotation_mode="anchor" , ha="right")

        ax_Bars.set_title(self.Bar_Title)

        ax_Bars.set_xlabel(f"{self.Axis_x_Title}")
        ax_Bars.set_ylabel(f"{self.Axis_y_Title}")

        for Bar in Bars:
            height = Bar.get_height()
            if Variable_Of_Frecuency == "fi":
                ax_Bars.text(Bar.get_x() + (Bar.get_width() / 2), height + (height * 0.01), f"{int(height)}" , ha="center", va="bottom", fontsize=10)
            elif Variable_Of_Frecuency == "hi":
                ax_Bars.text(Bar.get_x() + (Bar.get_width() / 2), height + (height * 0.01), f"{height:.{self.Precision}f}" , ha="center", va="bottom", fontsize=10)
            elif Variable_Of_Frecuency == "hi_percent":
                ax_Bars.text(Bar.get_x() + (Bar.get_width() / 2), height + (height * 0.01), f"{height:.{self.Precision}f}%" , ha="center", va="bottom", fontsize=10)
            
            Bar.set_zorder(2)
            # Agregar una sombra (simulando un desplazamiento)
            ax_Bars.bar(Bar.get_x() + 0.24, height - (height * 0.01), width=Bar.get_width(), bottom=0, color='gray', alpha=0.5, zorder=1)
        return figure_bars

    def Draw_Pie(self , Copy_Data , Variable_Of_Frecuency , Variable_To_Access):
        """ Modificar para que los datos se muestren de mejor manera. """
        figure_pie = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=72)
        ax_pie = figure_pie.add_subplot(111)

        values = Copy_Data[f"{Variable_Of_Frecuency}"]

        # Ajuste de las porciones más pequeñas
        explode = [0.12 if v < max(values) * 0.1 else 0.04 for v in values]

        # Agregar el gráfico de pastel
        wedges, texts, autotexts = ax_pie.pie(
            values,
            labels=Copy_Data[f"{Variable_To_Access}"],
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

    def Draw_Graph(self , Variable_Of_Frecuency):
        if(Variable_Of_Frecuency != "fi" and Variable_Of_Frecuency != "hi" and Variable_Of_Frecuency != "hi_percent"):
            raise Exception("Error al verificar la frecuencia.")
        
        if(Variable_Of_Frecuency == "fi"):
            self.Axis_y_Title = "Frecuencia Absoluta (fi)"
        elif(Variable_Of_Frecuency == "hi"):
            self.Axis_y_Title = "Frecuencia Relativa (hi)"
        elif(Variable_Of_Frecuency == "hi_percent"):
            self.Axis_y_Title = "Frecuencia Relativa Porcentual (hi%)"
        
        if ("Frecuences_Cuant_For_Many_Values" in self.Data):
            Copy_Data = copy.deepcopy(self.Data["Frecuences_Cuant_For_Many_Values"])
            Copy_Data = pd.DataFrame(Copy_Data)

            if(not self.Axis_x_Title):
                self.Axis_x_Title = "Intervalos de Clase"
            
            figure_bars = self.Draw_Bars(Copy_Data , Variable_Of_Frecuency , "Intervals")

            """ Pie """
            if(Variable_Of_Frecuency == "fi"):
                figure_pie = self.Draw_Pie(Copy_Data , Variable_Of_Frecuency , "Intervals")
                return figure_bars , figure_pie

            return figure_bars

        elif("Frecuences_Cuant_Normal_Extended" in self.Data):
            Copy_Data = self.Data["Frecuences_Cuant_Normal_Extended"].copy()
            Copy_Data = pd.DataFrame(Copy_Data)
            
            if(not self.Axis_x_Title):
                self.Axis_x_Title = "Variables Observadas (xi)"

            figure_bars = self.Draw_Bars(Copy_Data , Variable_Of_Frecuency , "xi")

            if(Variable_Of_Frecuency == "fi"):
                figure_pie = self.Draw_Pie(Copy_Data , Variable_Of_Frecuency , "xi")
                return figure_bars , figure_pie
            return figure_bars

        elif("Frecuences_Cuali_Normal_Extended" in self.Data):
            Copy_Data = self.Data["Frecuences_Cuali_Normal_Extended"].copy()
            Copy_Data = pd.DataFrame(Copy_Data)

            if(not self.Axis_x_Title):
                self.Axis_x_Title = "Variables Observadas (ai)"

            figure_bars = self.Draw_Bars(Copy_Data , Variable_Of_Frecuency , "ai")

            if(Variable_Of_Frecuency == "fi"):
                figure_pie = self.Draw_Pie(Copy_Data , Variable_Of_Frecuency , "ai")
                return figure_bars , figure_pie

            return figure_bars

        else:
            raise Exception("Error al procesar los datos.")