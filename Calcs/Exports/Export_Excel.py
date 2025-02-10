from tkinter import messagebox
from datetime import datetime
import os
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

def Export_Table_In_Excel(Main_Window , Data , Type_Of_Variable , route , file_name = ""):
    try:
        if(file_name == ""):
            time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            file_name = f"frecuences_{time}.xlsx"
        elif(not file_name.lower().endswith('.xlsx')):
            file_name += '.xlsx'

        if not route.endswith("/"):
            route += "/"

        if(not os.path.exists(route) or not os.path.isdir(route)):
            raise Exception("Ruta de exportacion no valida")
        
        full_path = route + file_name  #la ruta debe ser completa con la ubicacion y el nombre del archvo .xlsx
        
        match(Type_Of_Variable):
            case "Cuantitative":
                if(Data["Frecuences_Cuant_Normal_Extended"] != None):
                    F_Cuant_Norm_Extend = pd.DataFrame(Data["Frecuences_Cuant_Normal_Extended"])
                    F_Cuant_For_Many_Values = pd.DataFrame(Data["Frecuences_Cuant_For_Many_Values"])

                    with pd.ExcelWriter(full_path) as writer:
                        F_Cuant_Norm_Extend.to_excel(writer , sheet_name = 'Hoja1' , index=False , startcol=3 , startrow=3)

                        F_Cuant_For_Many_Values.to_excel(writer , sheet_name='Hoja2' , index=False , startcol=3 ,startrow=3)

                        workbook = writer.book  #Acceder al excel
                        worksheet_hoja1 = workbook['Hoja1'] #Acceder a Hoja 1
                        worksheet_hoja2 = workbook['Hoja2'] #Acceder a Hoja 2

                        # Centrar texto en la columna A de la Hoja1
                        for col in ["D" , "E" , "F" , "G" , "H" , "I" , "J"]:
                            for row in worksheet_hoja1[col]:
                                row.alignment = Alignment(horizontal="center", vertical="center")
                            
                            cell = worksheet_hoja1[f"{col}4"] # Accedo a por ejemplo A4 o D4
                            cell.font = Font(bold=True , color="FF0000")

                            if(col == "D"):
                                for row in range(5 , worksheet_hoja1.max_row + 1):
                                    cell = worksheet_hoja1[f"{col}{row}"]
                                    cell.font = Font(bold=True)

                        for col in ["D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L"]:
                            for row in worksheet_hoja2[col]:
                                row.alignment = Alignment(horizontal="center", vertical="center")
                            
                            cell = worksheet_hoja2[f"{col}4"]
                            cell.font = Font(bold=True , color="FF0000")

                            if(col == "D"):
                                for row in range(5 , worksheet_hoja2.max_row + 1):
                                    cell = worksheet_hoja2[f"{col}{row}"]
                                    cell.font = Font(bold=True)
                        
                        for col in worksheet_hoja1.columns:
                            max_length = 0
                            column = col[0].column_letter  # Obtener la letra de la columna
                            for cell in col:
                                try:
                                    if len(str(cell.value)) > max_length:
                                        max_length = len(cell.value)
                                except:
                                    pass
                            adjusted_width = (max_length + 2)
                            worksheet_hoja1.column_dimensions[column].width = adjusted_width

                        for col in worksheet_hoja2.columns:
                            max_length = 0
                            column = col[0].column_letter  # Obtener la letra de la columna
                            for cell in col:
                                try:
                                    if len(str(cell.value)) > max_length:
                                        max_length = len(cell.value)
                                except:
                                    pass
                            adjusted_width = (max_length + 2)
                            worksheet_hoja2.column_dimensions[column].width = adjusted_width

                else:
                    F_Cuant_For_Many_Values = pd.DataFrame(Data["Frecuences_Cuant_For_Many_Values"])

                    with pd.ExcelWriter(full_path) as writer:
                        F_Cuant_For_Many_Values.to_excel(writer , sheet_name='Hoja1' , index=False , startcol=3 , startrow=3)

                        workbook = writer.book  #Acceder al excel
                        worksheet_hoja1 = workbook['Hoja1']
                        
                        for col in ["D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L"]:
                            for row in worksheet_hoja1[col]:
                                row.alignment = Alignment(horizontal="center", vertical="center")
                            
                            cell = worksheet_hoja1[f"{col}4"] # Accedo a por ejemplo A4 o D4
                            cell.font = Font(bold=True , color="FF0000")

                            if(col == "D"):
                                for row in range(5 , 9):
                                    cell = worksheet_hoja1[f"{col}{row}"]
                                    cell.font = Font(bold=True)

                        for col in worksheet_hoja1.columns:
                            max_length = 0
                            column = col[0].column_letter  # Obtener la letra de la columna
                            for cell in col:
                                try:
                                    if len(str(cell.value)) > max_length:
                                        max_length = len(cell.value)
                                except:
                                    pass
                            adjusted_width = (max_length + 2)
                            worksheet_hoja1.column_dimensions[column].width = adjusted_width
                
            case "Cualitative":
                F_Cuali_Norm_Extend = pd.DataFrame(Data["Frecuences_Cuali_Normal_Extended"])

                with pd.ExcelWriter(full_path) as writer:

                    F_Cuali_Norm_Extend.to_excel(writer , sheet_name='Hoja1' , index=False , startcol=3 , startrow=3)

                    workbook = writer.book  #Acceder al excel
                    worksheet_hoja1 = workbook['Hoja1']
                    
                    for col in ["D" , "E" , "F" , "G" , "H" , "I" , "J"]:
                        for row in worksheet_hoja1[col]:
                            row.alignment = Alignment(horizontal="center", vertical="center")
                        
                        cell = worksheet_hoja1[f"{col}4"] # Accedo a por ejemplo A4 o D4
                        cell.font = Font(bold=True , color="FF0000")

                        if(col == "D"):
                            for row in range(5 , worksheet_hoja1.max_row + 1):
                                cell = worksheet_hoja1[f"{col}{row}"]
                                cell.font = Font(bold=True)

                    for col in worksheet_hoja1.columns:
                        max_length = 0
                        column = col[0].column_letter  # Obtener la letra de la columna
                        for cell in col:
                            try:
                                if len(str(cell.value)) > max_length:
                                    max_length = len(cell.value)
                            except:
                                pass
                        adjusted_width = (max_length + 2)
                        worksheet_hoja1.column_dimensions[column].width = adjusted_width

            case _:
                raise Exception("Error al identificar el tipo de variable")
            
    except Exception as e:
        messagebox.showerror("Error" , f"Los datos no fueron procesados correctamente. \n {e}")
    else:
        messagebox.showinfo("Sucess" , f"Los datos fueron exportados correctamente a {route}")
        Main_Window.destroy()
