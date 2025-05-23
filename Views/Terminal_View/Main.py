import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..')))

from tkinter import filedialog
import pandas as pd
from Calcs.Table_of_Frecuency.Calc_Values_Tables import Main_Function

from Views.Terminal_View.Functions_For_Terminal import Clear_Terminal
from Views.Terminal_View.Show_Frecuences_Table import Print_Results_Cuantitative_Grouped_Data_In_Terminal , Print_Results_Cuantitative_No_Grouped_Data_In_Terminal

def Create_Main_View_In_Terminal():
    """
        ==================================================================
        Este bloque de codigo solo se usa para pruebas y Debugging.
        ==================================================================
    """
    Stop = False
    while(not Stop):
        Excel_Path = filedialog.askopenfilenames(filetypes=[("Archivos Excel" , "*.xlsx")])
        if(Excel_Path):
            Excel = pd.read_excel(Excel_Path[0] , engine="openpyxl" , nrows=3)
            columns_list = [coln for coln in Excel.columns.tolist()]
            for i , col_name in enumerate(columns_list):
                print(f"{i + 1}. {col_name}")
            
            column_index = int(input("Ingrese el numero de la columna a importar: "))
            while(column_index < 0 or column_index > len(columns_list)):
                Clear_Terminal()
                for i , col_name in enumerate(columns_list):
                    print(f"{i + 1}. {col_name}")
                print("Valor invalido, intente nuevamente")
                column_index = int(input("Ingrese el nombre de la columna: "))
            Clear_Terminal()

            variable = ["Discreta" , "Continua"]
            variable_type = int(input("Ingrese el tipo de variable (1 = Discreta ; 2 = Continua): "))
            while(variable_type > 2 or variable_type < 1):
                Clear_Terminal()

                print("Valor invalido, intente nuevamente")
                variable_type = int(input("Ingrese el tipo de variable (1 = Discreta ; 2 = Continua): "))
            Clear_Terminal()

            precision = int(input("Ingrese la precsion de los resultados (1 - 10): "))
            while(precision < 1 or precision > 11):
                Clear_Terminal()

                print("Valor invalido, intente nuevamente")
                precision = int(input("Ingrese la precsion de los resultados (1 - 10): "))
            Clear_Terminal()

            results = Main_Function(Excel_Path[0] , columns_list[column_index - 1] , variable[variable_type - 1])
            if(variable_type == 1):
                Print_Results_Cuantitative_No_Grouped_Data_In_Terminal(results , precision)
            elif(variable_type == 2):
                Print_Results_Cuantitative_Grouped_Data_In_Terminal(results , precision)

            print("\n")

            # Descargar graficos
            """ Download_Graphs = input("Deseea descargar los graficos (s/n): ")
            while(Download_Graphs.lower() != "s" and Download_Graphs.lower() != "n"):
                Clear_Terminal()

                print("Opcion Invalida, intente nuevamente")
                Download_Graphs = input("Deseea descargar los graficos (s/n): ")

            match(Download_Graphs.lower()):
                case "s":
                    pass
                case "n":
                    pass """

            Continue = input("Deseea realizar otro calculo (s/n): ")
            while(Continue.lower() != "s" and Continue.lower() != "n"):
                Clear_Terminal()

                print("Opcion Invalida, intente nuevamente")
                Continue = input("Desea realizar otro calculo (s/n): ")
            
            match(Continue.lower()):
                case "s":
                    pass
                case "n":
                    Stop = True