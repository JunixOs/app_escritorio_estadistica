import matplotlib.pyplot as plt
import pandas as pd

def pixels_to_inches(pixels, dpi=96):
    return pixels / dpi

class Draw_Graph_for_Each_Variable:
    def __init__(self , Data , Precision):
        self.Data = Data
        self.Precision = Precision

        self.Bar_Title = "Grafico de Barras"

        self.Pie_Title = "Grafico de Pastel"

        self.Fig_Height = pixels_to_inches(700)
        self.Fig_Width = pixels_to_inches(680)

    def Draw_Graph(self , Variable_Of_Frecuency):
        if(Variable_Of_Frecuency != "fi" and Variable_Of_Frecuency != "hi" and Variable_Of_Frecuency != "hi_percent"):
            raise Exception("Error interno")

        figure_bars = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=96)
        figure_pie = plt.Figure(figsize=(self.Fig_Width , self.Fig_Height) , dpi=96)

        Axis_y_Title = None
        if(Variable_Of_Frecuency == "fi"):
            Axis_y_Title = "Frecuencia Absoluta (fi)"
        elif(Variable_Of_Frecuency == "hi"):
            Axis_y_Title = "Frecuencia Relativa (hi)"
        elif(Variable_Of_Frecuency == "hi_percent"):
            Axis_y_Title = "Frecuencia Relativa Porcentual (hi%)"
        
        if ("Frecuences_Cuant_For_Many_Values" in self.Data):
            Copy_Data = self.Data["Frecuences_Cuant_For_Many_Values"].copy()

            Copy_Data = pd.DataFrame(Copy_Data)

            ax_Bars = figure_bars.add_subplot(111)
            figure_bars.subplots_adjust(bottom=0.15)
            Bars = ax_Bars.bar(Copy_Data["Intervals"].astype(str) , Copy_Data[f"{Variable_Of_Frecuency}"] , color="skyblue" , width=0.5)

            ax_Bars.set_xticks(range(len(Copy_Data["Intervals"])))
            ax_Bars.set_xticklabels(Copy_Data["Intervals"] , fontsize=7 , rotation=30 , rotation_mode="anchor" , ha="right")

            ax_Bars.set_title(self.Bar_Title)
            ax_Bars.set_xlabel("Intervalos de Clase")
            ax_Bars.set_ylabel(f"{Axis_y_Title}")
            
            for Bar in Bars:
                height = Bar.get_height()
                if(Variable_Of_Frecuency == "fi"):
                    ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{int(height)}" , ha="center" , va="bottom" , fontsize=10)
                elif(Variable_Of_Frecuency == "hi"):
                    ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{height:.{self.Precision}f}" , ha="center" , va="bottom" , fontsize=10)
                elif(Variable_Of_Frecuency == "hi_percent"):
                    ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{height:.{self.Precision}f}%" , ha="center" , va="bottom" , fontsize=10)

            """ Pie """
            ax_pie = figure_pie.add_subplot(111)
            ax_pie.pie(Copy_Data[f"{Variable_Of_Frecuency}"] , labels=Copy_Data["Intervals"].astype(str) , autopct="%1.1f%%" , startangle=90)
            ax_pie.set_title(self.Pie_Title)
            ax_pie.axis("equal")

            return figure_bars , figure_pie

        elif("Frecuences_Cuant_Normal_Extended" in self.Data):
            Copy_Data = self.Data["Frecuences_Cuant_Normal_Extended"].copy()
            Copy_Data = pd.DataFrame(Copy_Data)

            ax_Bars = figure_bars.add_subplot(111)
            figure_bars.subplots_adjust(bottom=0.15)
            Bars = ax_Bars.bar(Copy_Data["xi"] , Copy_Data[f"{Variable_Of_Frecuency}"] , color="skyblue" , width=0.6)

            ax_Bars.set_xticks(range(len(Copy_Data["xi"])))
            ax_Bars.set_xticklabels(Copy_Data["xi"] , fontsize=8 , rotation=30 , rotation_mode="anchor" , ha="right")

            ax_Bars.set_title(self.Bar_Title)   
            ax_Bars.set_xlabel("Variables Observadas (xi)")
            ax_Bars.set_ylabel(f"{Axis_y_Title}")

            for Bar in Bars:
                height = Bar.get_height()
                if(Variable_Of_Frecuency == "fi"):
                    ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{int(height)}" , ha="center" , va="bottom" , fontsize=10)
                elif(Variable_Of_Frecuency == "hi"):
                    ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{height:.{self.Precision}f}" , ha="center" , va="bottom" , fontsize=10)
                elif(Variable_Of_Frecuency == "hi_percent"):
                    ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{height:.{self.Precision}f}%" , ha="center" , va="bottom" , fontsize=10)

            """ Pie """
            ax_pie = figure_pie.add_subplot(111)
            ax_pie.pie(Copy_Data[f"{Variable_Of_Frecuency}"] , labels=Copy_Data["xi"] , autopct="%1.1f%%" , startangle=90)
            ax_pie.set_title(self.Pie_Title)
            ax_pie.axis("equal")

            return figure_bars , figure_pie

        elif("Frecuences_Cuali_Normal_Extended" in self.Data):
            Copy_Data = self.Data["Frecuences_Cuali_Normal_Extended"].copy()
            Copy_Data = pd.DataFrame(Copy_Data)

            ax_Bars = figure_bars.add_subplot(111)
            figure_bars.subplots_adjust(bottom=0.15)
            Bars = ax_Bars.bar(Copy_Data["ai"] , Copy_Data[f"{Variable_Of_Frecuency}"] , color="skyblue" , width=0.6)

            ax_Bars.set_xticks(range(len(Copy_Data["ai"])))
            ax_Bars.set_xticklabels(Copy_Data["ai"] , fontsize=8 , rotation=30 , rotation_mode="anchor" , ha="right")

            ax_Bars.set_title(self.Bar_Title)   
            ax_Bars.set_xlabel("Variables Observadas (ai)")
            ax_Bars.set_ylabel(f"{Axis_y_Title}")

            for Bar in Bars:
                height = Bar.get_height()
                if(Variable_Of_Frecuency == "fi"):
                    ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{int(height)}" , ha="center" , va="bottom" , fontsize=10)
                elif(Variable_Of_Frecuency == "hi"):
                    ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{height:.{self.Precision}f}" , ha="center" , va="bottom" , fontsize=10)
                elif(Variable_Of_Frecuency == "hi_percent"):
                    ax_Bars.text(Bar.get_x() + Bar.get_width() / 2 , height , f"{height:.{self.Precision}f}%" , ha="center" , va="bottom" , fontsize=10)

            """ Pie """
            ax_pie = figure_pie.add_subplot(111)
            ax_pie.pie(Copy_Data[f"{Variable_Of_Frecuency}"] , labels=Copy_Data["ai"] , autopct="%1.1f%%" , startangle=90)
            ax_pie.set_title(self.Pie_Title)
            ax_pie.axis("equal")

            return figure_bars , figure_pie
        else:
            raise Exception("Error al procesar los datos")