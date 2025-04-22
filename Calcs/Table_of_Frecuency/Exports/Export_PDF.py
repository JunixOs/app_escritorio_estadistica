import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..')))

from Exceptions.Exception_Warning import Raise_Warning

import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet , ParagraphStyle
from reportlab.platypus import Table , Flowable

import copy
import os
from datetime import datetime
from tkinter import messagebox
import numpy as np

def Change_Key(dictionary, old_key, new_key):
    return {clave if clave != old_key else new_key: valor for clave, valor in dictionary.items()}

def Int_To_Roman(Int_Number):
    Val_In_Int = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    Symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    Roman_Number = ''
    for i in range(len(Val_In_Int)):
        while Int_Number >= Val_In_Int[i]:
            Roman_Number += Symbols[i]
            Int_Number -= Val_In_Int[i]
    return Roman_Number

class Export_Data:
    def __init__(self , Data_To_Export , File_Name , Route , Descriptions):
        self.Data_To_Export = Data_To_Export
        self.File_Name = File_Name
        self.Route = Route
        self.Descriptions = Descriptions

        self.PDF_Table_M_Central_Tendency_And_Dispersion_Style = None
        self.PDF_Table_M_Coefficient_Asymmetry_Style = None
        self.PDF_Table_Quartiles_Style = None
        self.PDF_Text_Styles = None

    def Create_Full_Route(self):
        time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        if(self.File_Name == ""):
            self.File_Name = f"{time}_Exported_PDF.pdf"
        elif(not self.File_Name.lower().endswith('.pdf')):
            self.File_Name += f"_{time}_" + ".pdf"
        
        if(not self.Route):
            raise Raise_Warning("No se ha ingresado ninguna ruta de exportacion.")
        
        if(not self.Route.endswith("/")):
            self.Route += "/"
        
        if(not os.path.exists(self.Route) or not os.path.isdir(self.Route)):
            raise Raise_Warning("Ruta de exportacion no valida.")

        return self.Route + self.File_Name
    
    def Create_Decorators(self , Length_Frecuences_Table):
        if(not(self.PDF_Table_M_Central_Tendency_And_Dispersion_Style or self.PDF_Table_M_Coefficient_Asymmetry_Style or self.PDF_Table_Quartiles_Style)):
            self.PDF_Text_Styles = getSampleStyleSheet()
            self.PDF_Text_Styles.add(ParagraphStyle(
                name="Heading2Left",
                parent=self.PDF_Text_Styles["Heading1"],
                alignment=TA_LEFT,
            ))
            self.PDF_Text_Styles.add(ParagraphStyle(
                name="Heading3Left",
                parent=self.PDF_Text_Styles["Heading2"],
                alignment=TA_LEFT,
            ))
            self.PDF_Table_M_Central_Tendency_And_Dispersion_Style = TableStyle([
                ("SPAN" , (0 , 0) , (-1 , 0)), # Combinar celdas encabezado
                ("VALIGN" , (0 , 0) , (-1 , 0) , "MIDDLE"),
                ("BACKGROUND" , (0 , 0) , (-1 , 0) , colors.lightgrey),
                ("TEXTCOLOR" , (0 , 0) , (-1 , 0) , colors.red),

                ("ALIGN" , (0 , 0) , (-1 , -1) , "CENTER"),

                ("FONTNAME", (0, 1), (0, -1), "Times-Bold"),
                ("BACKGROUND" , (0, 1), (0, -1), colors.lightgrey),

                ("FONTNAME" , (1 , 1) , (-1 , -1) , "Times-Roman"),

                ("FONTSIZE" , (0 , 0) , (-1 , -1) , 10),

                ("BOTTOMPADDING" , (0 , 0) , (-1 , 0) , 12),
                ("GRID" , (0 , 0) , (-1 , -1) , 1 , colors.black),
            ])
            self.PDF_Table_M_Coefficient_Asymmetry_Style = self.PDF_Table_M_Central_Tendency_And_Dispersion_Style
            self.PDF_Table_Quartiles_Style = self.PDF_Table_M_Central_Tendency_And_Dispersion_Style
            
        PDF_Table_Frecuences_Style = TableStyle([
            ("BACKGROUND" , (0 , 0) , (-1 , 0) , colors.lightgrey),
            ("VALIGN" , (0 , 0) , (-1 , 0) , "MIDDLE"),
            ("TEXTCOLOR" , (0 , 0) , (-1 , 0) , colors.black),

            ("ALIGN" , (0 , 0) , (-1 , -1) , "CENTER"),

            ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
            ("FONTNAME", (0, 1), (0, -1), "Times-Bold"),
            ("FONTNAME" , (0 , 1) , (-1 , -1) , "Times-Roman"),

            ("FONTSIZE" , (0 , 0) , (-1 , -1) , 10),

            ("BOTTOMPADDING" , (0 , 0) , (-1 , 0) , 12),
            ("GRID" , (0 , 0) , (-1 , -1) , 1 , colors.black),

            ("TEXTCOLOR" , (0 , Length_Frecuences_Table) , (-1 , Length_Frecuences_Table) , colors.red),
            ("FONTNAME" , (0 , Length_Frecuences_Table) , (-1 , Length_Frecuences_Table) , "Times-Bold"),
        ])

        return PDF_Table_Frecuences_Style

    def Process_Data_For_Frecuences_Table(self , Copy_Data):
        Frecuences_Table = None
        Total_Row_For_Frecuences_Table = None
        if("Frecuences_Cuant_Grouped" in Copy_Data):
            Frecuences_Table = Copy_Data["Frecuences_Cuant_Grouped"]

            for i in range(0 , len(Frecuences_Table["Intervals"])):
                Old_Text = str(Frecuences_Table["Intervals"][i]).replace("[" , "").replace("]" , "").split(",")
                Old_Text = " -".join(Old_Text)
                if(i < len(Frecuences_Table["Intervals"]) - 1):
                    Frecuences_Table["Intervals"][i] = "[ " + Old_Text + " >"
                else:
                    Frecuences_Table["Intervals"][i] = "[ " + Old_Text + " ]"

                Frecuences_Table["Intervals"][i] = Frecuences_Table["Intervals"][i].replace("np.float64(","").replace("np.int64(","").replace(")","")
                Frecuences_Table["xi"] = [round(xi , 13) for xi in Frecuences_Table["xi"]]

            Total_Row_For_Frecuences_Table = ["Total:" , "" , f"{np.sum(Frecuences_Table['fi'])}" , "" , f"{round(np.sum(Frecuences_Table['hi']) , 10)}" , "" , f"{round(np.sum(Frecuences_Table['hi_percent']) , 10)}"]
            
            Frecuences_Table = Change_Key(Frecuences_Table , "Intervals" , "[ Li - Ls >")

        elif("Frecuences_Cuant_Not_Grouped" in Copy_Data):
            Frecuences_Table = Copy_Data["Frecuences_Cuant_Not_Grouped"]

            Total_Row_For_Frecuences_Table = ["Total:" , f"{np.sum(Frecuences_Table['fi'])}" , "" , f"{round(np.sum(Frecuences_Table['hi']) , 10)}" , "" , f"{round(np.sum(Frecuences_Table['hi_percent']) , 10)}"]

        elif("Frecuences_Cuali" in Copy_Data):
            Frecuences_Table = Copy_Data["Frecuences_Cuali"]

            Total_Row_For_Frecuences_Table = ["Total:" , f"{np.sum(Frecuences_Table['fi'])}" , "" , f"{round(np.sum(Frecuences_Table['hi']) , 10)}" , "" , f"{round(np.sum(Frecuences_Table['hi_percent']) , 10)}"]
        
        Frecuences_Table["Hi"] = [round(Hi , 12) for Hi in Frecuences_Table["Hi"]]
        Frecuences_Table["hi_percent"] = [f"{round(hi_percent , 12)}%" for hi_percent in Frecuences_Table["hi_percent"]]
        Frecuences_Table["Hi_percent"] = [f"{round(Hi_percent , 12)}%" for Hi_percent in Frecuences_Table["Hi_percent"]]

        Frecuences_Table = Change_Key(Frecuences_Table , "hi_percent" , "hi%")
        Frecuences_Table = Change_Key(Frecuences_Table , "Hi_percent" , "Hi%")
        Frecuences_Table = pd.DataFrame(Frecuences_Table)

        Frecuences_Table = [Frecuences_Table.columns.to_list()] + Frecuences_Table.values.tolist() + [Total_Row_For_Frecuences_Table]
        Frecuences_Table_PDF = Table(Frecuences_Table)

        return Frecuences_Table_PDF , len(Frecuences_Table) - 1

    def Process_Data_For_Summary_Measures(self , Copy_Data):
        M_Central_Tendency_And_Dispersion = None
        M_Coefficient_Asymmetry = None
        Quartiles = None
        if("Summary_Measures_For_Grouped_Data" in Copy_Data):
            M_Central_Tendency_And_Dispersion = Copy_Data["Summary_Measures_For_Grouped_Data"]["Measures_Of_Central_Tendency_And_Dispersion"]
            M_Coefficient_Asymmetry = Copy_Data["Summary_Measures_For_Grouped_Data"]["Coefficient_Asymmetry"]
            Quartiles = Copy_Data["Summary_Measures_For_Grouped_Data"]["Quantiles"]["Cuartil"]

        elif("Summary_Measures_For_Not_Grouped_Data" in Copy_Data):
            M_Central_Tendency_And_Dispersion = Copy_Data["Summary_Measures_For_Not_Grouped_Data"]["Measures_Of_Central_Tendency_And_Dispersion"]
            M_Coefficient_Asymmetry = Copy_Data["Summary_Measures_For_Not_Grouped_Data"]["Coefficient_Asymmetry"]
            Quartiles = Copy_Data["Summary_Measures_For_Not_Grouped_Data"]["Quantiles"]["Cuartil"]

            if(len(M_Central_Tendency_And_Dispersion["Moda (Mo)"]) > 1):
                M_Central_Tendency_And_Dispersion["Moda (Mo)"] = [f"Mo_{i}: {mo}" for i , mo in enumerate(M_Central_Tendency_And_Dispersion["Moda (Mo)"] , start=1)]

        M_Central_Tendency_And_Dispersion = {
            key : [value] for key , value in M_Central_Tendency_And_Dispersion.items()
        }

        M_Coefficient_Asymmetry = {
            key : [value] for key , value in M_Coefficient_Asymmetry.items()
        }

        Quartiles = {
            f"Q_{i}" : [value] for i , value in enumerate(Quartiles , start=1)
        }

        M_Central_Tendency_And_Dispersion = pd.DataFrame(M_Central_Tendency_And_Dispersion)
        M_Coefficient_Asymmetry = pd.DataFrame(M_Coefficient_Asymmetry)
        Quartiles = pd.DataFrame(Quartiles)

        Data_Tables = []

        if(len(M_Central_Tendency_And_Dispersion["Moda (Mo)"][0]) > 1):
            for i , col in enumerate(M_Central_Tendency_And_Dispersion.columns):
                if(i == 3):
                    Mo_Section = [col , M_Central_Tendency_And_Dispersion.iloc[0][col][0]]
                    Data_Tables.append(Mo_Section)

                    for mo in M_Central_Tendency_And_Dispersion.iloc[0][col][1:]:
                        Data_Tables.append(["" , mo])
                else:
                    Data_Tables.append([col , M_Central_Tendency_And_Dispersion.iloc[0][col]])

            Start_Mo_Row = 4
            End_Mo_Row = Start_Mo_Row + len(M_Central_Tendency_And_Dispersion["Moda (Mo)"][0]) - 1

            self.PDF_Table_M_Central_Tendency_And_Dispersion_Style = TableStyle([
                ("SPAN" , (0 , 0) , (-1 , 0)), # Combinar celdas encabezado
                ("VALIGN" , (0 , 0) , (-1 , 0) , "MIDDLE"),
                ("BACKGROUND" , (0 , 0) , (-1 , 0) , colors.lightgrey),
                ("TEXTCOLOR" , (0 , 0) , (-1 , 0) , colors.red),

                ("ALIGN" , (0 , 0) , (-1 , -1) , "CENTER"),

                ("FONTNAME", (0, 1), (0, -1) , "Times-Bold"),
                ("BACKGROUND" , (0, 1), (0, -1) , colors.lightgrey),

                ("SPAN" , (0 , Start_Mo_Row) , (0 , End_Mo_Row)),
                ("VALIGN" , (0 , Start_Mo_Row) , (0 , End_Mo_Row) , "MIDDLE"),

                ("FONTNAME" , (1 , 1) , (-1 , -1) , "Times-Roman"),

                ("FONTSIZE" , (0 , 0) , (-1 , -1) , 10),

                ("BOTTOMPADDING" , (0 , 0) , (-1 , 0) , 12),
                ("GRID" , (0 , 0) , (-1 , -1) , 1 , colors.black),
            ])
        else:
            for i , col in enumerate(M_Central_Tendency_And_Dispersion.columns):
                if(i == 3):
                    Mo_Section = [col , M_Central_Tendency_And_Dispersion.iloc[0][col][0]]
                    Data_Tables.append(Mo_Section)
                else:
                    Data_Tables.append([col , M_Central_Tendency_And_Dispersion.iloc[0][col]])

        Table_M_Central_Tendency_And_Dispersion = [["Medidas de Tendencia Central y de Dispersion"]] + Data_Tables

        Table_M_Central_Tendency_And_Dispersion_PDF = Table(Table_M_Central_Tendency_And_Dispersion , colWidths=['*' , '*'])

        Table_M_Coefficient_Asymmetry = [["Coeficientes de Asimetria"]] + [[col , M_Coefficient_Asymmetry.iloc[0][col]] for col in M_Coefficient_Asymmetry.columns]
        Table_M_Coefficient_Asymmetry_PDF = Table(Table_M_Coefficient_Asymmetry , colWidths=['*' , '*'])

        Table_Quartiles = [["Cuartiles"]] + [[col , Quartiles.iloc[0][col]] for col in Quartiles.columns]
        Table_Quartiles_PDF = Table(Table_Quartiles , colWidths=['*' , '*'])

        return Table_M_Central_Tendency_And_Dispersion_PDF , Table_M_Coefficient_Asymmetry_PDF , Table_Quartiles_PDF

    def Export_PDF_With_Single_Table(self):
        Key_Data_To_Export = None
        Values_Data_To_Export = None
        Copy_Data = None

        Export_Route = self.Create_Full_Route()
        PDF_Document = SimpleDocTemplate(f"{Export_Route}" , pagesize=A4)
        Elements_In_PDF_Dcoument = []

        if(len(self.Data_To_Export) == 1):
            Key_Data_To_Export , Values_Data_To_Export = next(iter(self.Data_To_Export.items()))
            Copy_Data = copy.deepcopy(Values_Data_To_Export)
        else:
            Copy_Data = copy.deepcopy(self.Data_To_Export)

        Frecuences_Table_PDF = None
        Frecuences_Table_PDF , Length_Frecuences_Table = self.Process_Data_For_Frecuences_Table(Copy_Data)
        PDF_Table_Frecuences_Style = self.Create_Decorators(Length_Frecuences_Table)

        Table_M_Central_Tendency_And_Dispersion_PDF = None
        Table_M_Coefficient_Asymmetry_PDF = None
        Table_Quartiles_PDF = None
        if("Summary_Measures_For_Grouped_Data" in Copy_Data or "Summary_Measures_For_Not_Grouped_Data" in Copy_Data):
            Table_M_Central_Tendency_And_Dispersion_PDF , Table_M_Coefficient_Asymmetry_PDF , Table_Quartiles_PDF = self.Process_Data_For_Summary_Measures(Copy_Data)


        Frecuences_Table_PDF.setStyle(PDF_Table_Frecuences_Style)
        if("Summary_Measures_For_Grouped_Data" in Copy_Data or "Summary_Measures_For_Not_Grouped_Data" in Copy_Data):
            Table_M_Central_Tendency_And_Dispersion_PDF.setStyle(self.PDF_Table_M_Central_Tendency_And_Dispersion_Style)
            Table_M_Coefficient_Asymmetry_PDF.setStyle(self.PDF_Table_M_Coefficient_Asymmetry_Style)
            Table_Quartiles_PDF.setStyle(self.PDF_Table_Quartiles_Style)

        Data_For_PDF = [
            ("Tabla de Frecuencias" , Frecuences_Table_PDF) , 
            ("Medidas de Tendencia Central y Dispercion" , Table_M_Central_Tendency_And_Dispersion_PDF) , 
            ("Coeficientes de Asimetria" , Table_M_Coefficient_Asymmetry_PDF),
            ("Cuartiles" , Table_Quartiles_PDF),
        ]

        if(Key_Data_To_Export):
            Elements_In_PDF_Dcoument.append(Paragraph(f"{Int_To_Roman(1)}. Resultados para {Key_Data_To_Export}" , self.PDF_Text_Styles["Heading1"]))

        for i , (title_table , table) in enumerate(Data_For_PDF , start=1):
            if(isinstance(table , Table) or isinstance(table , Flowable)):
                if(Key_Data_To_Export):
                    Elements_In_PDF_Dcoument.append(Paragraph(f"{i}. {title_table}" , self.PDF_Text_Styles["Heading3"]))
                else:
                    Elements_In_PDF_Dcoument.append(Paragraph(f"{i}. {title_table}" , self.PDF_Text_Styles["Heading2"]))

                Elements_In_PDF_Dcoument.append(Spacer(1 , 12))

                Elements_In_PDF_Dcoument.append(table)

        PDF_Document.build(Elements_In_PDF_Dcoument)

    def Export_PDF_With_Multiple_Tables(self , Columns_To_Export):
        Export_Route = self.Create_Full_Route()
        PDF_Document = SimpleDocTemplate(f"{Export_Route}" , pagesize=A4)
        Elements_In_PDF_Dcoument = []

        Copy_Data = copy.deepcopy(self.Data_To_Export)

        roman_index = 1
        for variable_name , variable_data_results in Copy_Data.items():
            if(not Columns_To_Export[variable_name].get()):
                continue

            Frecuences_Table_PDF = None
            Frecuences_Table_PDF , Length_Frecuences_Table = self.Process_Data_For_Frecuences_Table(variable_data_results)

            PDF_Table_Frecuences_Style = self.Create_Decorators(Length_Frecuences_Table)

            Table_M_Central_Tendency_And_Dispersion_PDF = None
            Table_M_Coefficient_Asymmetry_PDF = None
            Table_Quartiles_PDF = None
            if("Summary_Measures_For_Grouped_Data" in variable_data_results or "Summary_Measures_For_Not_Grouped_Data" in variable_data_results):
                Table_M_Central_Tendency_And_Dispersion_PDF , Table_M_Coefficient_Asymmetry_PDF , Table_Quartiles_PDF = self.Process_Data_For_Summary_Measures(variable_data_results)


            Frecuences_Table_PDF.setStyle(PDF_Table_Frecuences_Style)
            if("Summary_Measures_For_Grouped_Data" in variable_data_results or "Summary_Measures_For_Not_Grouped_Data" in variable_data_results):
                Table_M_Central_Tendency_And_Dispersion_PDF.setStyle(self.PDF_Table_M_Central_Tendency_And_Dispersion_Style)
                Table_M_Coefficient_Asymmetry_PDF.setStyle(self.PDF_Table_M_Coefficient_Asymmetry_Style)
                Table_Quartiles_PDF.setStyle(self.PDF_Table_Quartiles_Style)

            Data_For_PDF = [
                ("Tabla de Frecuencias" , Frecuences_Table_PDF) , 
                ("Medidas de Tendencia Central y Dispercion" , Table_M_Central_Tendency_And_Dispersion_PDF) , 
                ("Coeficientes de Asimetria" , Table_M_Coefficient_Asymmetry_PDF),
                ("Cuartiles" , Table_Quartiles_PDF),
            ]

            if(variable_name):
                Elements_In_PDF_Dcoument.append(Paragraph(f"{Int_To_Roman(roman_index)}. Resultados para {variable_name}" , self.PDF_Text_Styles["Heading1"]))

            for i , (title_table , table) in enumerate(Data_For_PDF , start=1):
                if(isinstance(table , Table) or isinstance(table , Flowable)):
                    if(variable_name):
                        Elements_In_PDF_Dcoument.append(Paragraph(f"{i}. {title_table}" , self.PDF_Text_Styles["Heading3"]))
                    else:
                        Elements_In_PDF_Dcoument.append(Paragraph(f"{i}. {title_table}" , self.PDF_Text_Styles["Heading2"]))

                    Elements_In_PDF_Dcoument.append(Spacer(1 , 12))

                    Elements_In_PDF_Dcoument.append(table)
            Elements_In_PDF_Dcoument.append(Spacer(1 , 12))

            roman_index += 1
        
        PDF_Document.build(Elements_In_PDF_Dcoument)

def Export_Table_In_PDF(W_Export_As_File , W_Export_PDF , Results_From_Single_Column , Results_From_Multiple_Column , Route , File_Name = "" , Descriptions = "" , Columns_To_Export = None):
    try:
        if(Results_From_Single_Column):
            Export = Export_Data(Results_From_Single_Column , File_Name , Route , Descriptions)
            Export.Export_PDF_With_Single_Table()

        elif(Results_From_Multiple_Column):
            if(all(export.get() == False for export in Columns_To_Export.values())):
                raise Raise_Warning("No se ha seleccionado ninguna tabla a exportar.")
            
            Export = Export_Data(Results_From_Multiple_Column , File_Name , Route , Descriptions)
            Export.Export_PDF_With_Multiple_Tables(Columns_To_Export)
        else:
            raise Exception("No se encontraron los datos a exportar.")
    except Raise_Warning as e:
        messagebox.showwarning("Advertencia" , f"{e}")
    except Exception as e:
        messagebox.showerror("Error" , f"{e}")
    else:
        messagebox.showinfo("Success" , f"PDF exportado con exito a {Route}")
        
        W_Export_PDF.quit()
        W_Export_PDF.destroy()

        W_Export_As_File.state(newstate="normal")
        W_Export_As_File.lift()

if(__name__ == "__main__"):
    data = {
        "Frecuences_Cuant_Grouped":{
            'Nombre': ['Ana', 'Luis', 'Carlos'],
            'Edad': [23, 34, 45],
            'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']
        },
        "Casa":{
            'Curso': ['Python', 'Excel', 'SQL'],
            'Duración (hrs)': [30, 20, 25],
            'Nivel': ['Básico', 'Intermedio', 'Avanzado']
        }
    }
    export_pdf = Export_Data(data , "Archivo" , "C:/Users/yonel/Downloads" , "")
    export_pdf.Export_PDF_With_Single_Table()
    print("Exportado Correctamente")