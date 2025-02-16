from tkinter import messagebox
from datetime import datetime
import copy
import os
from openpyxl.styles import Alignment, Font
import pandas as pd

def Change_Key(dictionary, old_key, new_key):
    """ No modifica el diccionarrio, sino que genera uno nuevo , pero con las claves moficiadas """
    return {clave if clave != old_key else new_key: valor for clave, valor in dictionary.items()}

def Export_Table_In_Excel(Main_Window , Data , Type_Of_Variable , route , file_name = ""):
    try:
        time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        if(file_name == ""):
            file_name = f"frecuences_{time}.xlsx"
        elif(not file_name.lower().endswith('.xlsx')):
            file_name += f'_{time}.xlsx'
        if (route == ""):
            raise Exception("No se ha ingresado ninguna ruta de exportacion.")
        if not route.endswith("/"):
            route += "/"

        if(not os.path.exists(route) or not os.path.isdir(route)):
            raise Exception("Ruta de exportacion no valida")
        
        full_path = route + file_name  #la ruta debe ser completa con la ubicacion y el nombre del archvo .xlsx
        
        match(Type_Of_Variable):
            case "Cuantitative":
                if(Data["Frecuences_Cuant_Normal_Extended"] != None):
                    Copy_Data = Data["Frecuences_Cuant_Normal_Extended"]

                    Copy_Data = Change_Key(Copy_Data , "hi_percent" , "hi%")
                    Copy_Data = Change_Key(Copy_Data , "Hi_percent" , "Hi%")

                    F_Cuant_Norm_Extend = pd.DataFrame(Copy_Data)

                    with pd.ExcelWriter(full_path) as writer:
                        F_Cuant_Norm_Extend.to_excel(writer , sheet_name = 'Hoja1' , index=False , startcol=3 , startrow=3)

                        workbook = writer.book  #Acceder al excel
                        worksheet_hoja1 = workbook['Hoja1'] #Acceder a Hoja 1

                        # Centrar texto de las columnas
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


                elif(Data["Frecuences_Cuant_For_Many_Values"] != None):
                    Copy_Data = copy.deepcopy(Data["Frecuences_Cuant_For_Many_Values"])

                    Copy_Data = Change_Key(Copy_Data , "Intervals" , "[ Li - Ls >")
                    Copy_Data = Change_Key(Copy_Data , "hi_percent" , "hi%")
                    Copy_Data = Change_Key(Copy_Data , "Hi_percent" , "Hi%")

                    F_Cuant_For_Many_Values = pd.DataFrame(Copy_Data)

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
                                for row in range(5 , worksheet_hoja1.max_row + 1):
                                    cell = worksheet_hoja1[f"{col}{row}"]

                                    if cell.value is not None:
                                        Old_Text = str(cell.value)
                                        Old_Text = Old_Text.replace("[","").replace("]","").replace(",","").replace(" "," - ")

                                        if(row != worksheet_hoja1.max_row):
                                            New_Text = "[ " + Old_Text + " >"
                                        else:
                                            New_Text = "[ " + Old_Text + " ]"
                                        cell.value = New_Text
                                    
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
                else:
                    raise Exception("Error al exportar el archivo, No hay datos que mostrar")
            case "Cualitative":
                Copy_Data = Data["Frecuences_Cuali_Normal_Extended"]

                Copy_Data = Change_Key(Copy_Data , "hi_percent" , "hi%")
                Copy_Data = Change_Key(Copy_Data , "Hi_percent" , "Hi%")

                F_Cuali_Norm_Extend = pd.DataFrame(Copy_Data)

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
