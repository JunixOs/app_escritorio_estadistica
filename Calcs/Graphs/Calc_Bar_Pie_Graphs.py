import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def pixels_to_inches(pixels, dpi=96):
    return pixels / dpi

class Draw_Graph_for_Each_Variable:
    def __init__(self , Data , Precision , Axis_x_Title):
        self.Data = Data
        self.Precision = Precision

        self.Bar_Title = "Grafico de Barras"

        self.Pie_Title = "Grafico de Pastel"
        self.Axis_x_Title = Axis_x_Title
        self.Axis_y_Title = None

        self.Fig_Height = pixels_to_inches(700)
        self.Fig_Width = pixels_to_inches(680)

    def Draw_Bars(self , Copy_Data , Variable_Of_Frecuency , Variable_To_Access):
        figure_bars = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=96)

        ax_Bars = figure_bars.add_subplot(111)  
        figure_bars.subplots_adjust(bottom=0.15)
        if(Variable_To_Access == "Intervals"):
            Bars = ax_Bars.bar(Copy_Data[f"{Variable_To_Access}"].astype(str) , Copy_Data[f"{Variable_Of_Frecuency}"] , color="skyblue" , width=0.6)
        else:
            Bars = ax_Bars.bar(Copy_Data[f"{Variable_To_Access}"] , Copy_Data[f"{Variable_Of_Frecuency}"] , color="skyblue" , width=0.6)

        ax_Bars.set_xticks(range(len(Copy_Data[f"{Variable_To_Access}"])))
        ax_Bars.set_xticklabels(Copy_Data[f"{Variable_To_Access}"] , fontsize=8 , rotation=30 , rotation_mode="anchor" , ha="right")

        ax_Bars.set_title(self.Bar_Title)

        ax_Bars.set_xlabel(f"{self.Axis_x_Title}")
        ax_Bars.set_ylabel(f"{self.Axis_y_Title}")

        for Bar in Bars:
            height = Bar.get_height()
            if(Variable_Of_Frecuency == "fi"):
                ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{int(height)}" , ha="center" , va="bottom" , fontsize=10)
            elif(Variable_Of_Frecuency == "hi"):
                ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{height:.{self.Precision}f}" , ha="center" , va="bottom" , fontsize=10)
            elif(Variable_Of_Frecuency == "hi_percent"):
                ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{height:.{self.Precision}f}%" , ha="center" , va="bottom" , fontsize=10)

        return figure_bars

    def Draw_Pie(self , Copy_Data , Variable_Of_Frecuency , Variable_To_Access):

        figure_pie = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=96)
        ax_pie = figure_pie.add_subplot(111)

        values = Copy_Data[f"{Variable_Of_Frecuency}"]
        angles = np.cumsum(values)  # Ángulos acumulados

        # Agregar el gráfico de pastel
        wedges, texts, autotexts = ax_pie.pie(
            values,
            labels=Copy_Data[f"{Variable_To_Access}"],
            autopct="%1.1f%%",
            startangle=90,
            labeldistance=1.1,  # Aleja las etiquetas de los centro
            explode=[0.05]*len(values),  # Separar las porciones
            shadow= False,
            pctdistance=0.85,   # Distancia de los porcentajes del centro
            wedgeprops={"edgecolor": "black"},
        )

        for i, text in enumerate(texts):
            angle = angles[i] - (values[i] / 2)  # Ajustar la posición de la etiqueta
            text.set_rotation(angle)  # Rotar la etiqueta según su ángulo

        ax_pie.set_facecolor('lightgray')
        ax_pie.set_title(self.Pie_Title)

        plt.tight_layout()

        ax_pie.axis("equal")
        return figure_pie

    def Draw_Graph(self , Variable_Of_Frecuency):
        if(Variable_Of_Frecuency != "fi" and Variable_Of_Frecuency != "hi" and Variable_Of_Frecuency != "hi_percent"):
            raise Exception("Error al verificar la frecuencia.")

        figure_bars = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=96)
        
        if(Variable_Of_Frecuency == "fi"):
            self.Axis_y_Title = "Frecuencia Absoluta (fi)"
        elif(Variable_Of_Frecuency == "hi"):
            self.Axis_y_Title = "Frecuencia Relativa (hi)"
        elif(Variable_Of_Frecuency == "hi_percent"):
            self.Axis_y_Title = "Frecuencia Relativa Porcentual (hi%)"
        
        if ("Frecuences_Cuant_For_Many_Values" in self.Data):
            Copy_Data = self.Data["Frecuences_Cuant_For_Many_Values"].copy()
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