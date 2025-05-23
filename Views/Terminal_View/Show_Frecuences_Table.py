import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..')))

import numpy as np
from Functions_For_Terminal import Get_Terminal_Dimensions

def Adjust_Width_Frecuences_Table(Terminal_Width , **Values):
    Space_Intervals_or_xi = None

    keywords = list(Values.keys())
    if("Space_Intervals" in keywords and "Space_fi_Fi" in keywords and "Space_For_Others" in keywords):
        Space_Intervals_or_xi = round(Values["Space_Intervals"] * Terminal_Width)
    elif("Space_xi" in keywords and "Space_fi_Fi" in keywords and "Space_For_Others" in keywords):
        Space_Intervals_or_xi = round(Values["Space_xi"] * Terminal_Width)
    else:
        raise Exception("No se pasaron los arguementos validos a la funcion.")

    Space_fi_Fi = round(Values["Space_fi_Fi"] * Terminal_Width)
    Space_For_Others = round(Values["Space_For_Others"] * Terminal_Width)

    Total_Width_For_Table = Space_Intervals_or_xi + Space_fi_Fi + Space_For_Others
    Width_Difference = Terminal_Width - Total_Width_For_Table
    Space_Intervals_or_xi += Width_Difference

    return Space_Intervals_or_xi , Space_fi_Fi , Space_For_Others

def Print_Frecuences_Table():
    pass

def Print_Central_Tendency_Measures():
    pass

def Print_Dispersion_Measures():
    pass

def Print_Position_Measures():
    pass

def Print_Results_Cuantitative_Grouped_Data_In_Terminal(results , precision):
    for name , values in results.items():
        Terminal_Width = Get_Terminal_Dimensions()[0]
        if(name == "Frecuences_Results"):
            print(f"{name:=^{Terminal_Width}}")

            Space_Intervals , Space_fi_Fi , Space_For_Others = Adjust_Width_Frecuences_Table(Terminal_Width , Space_Intervals=1/5 , Space_fi_Fi=15/100 , Space_For_Others=1/10)
            space = round((1/10) * Terminal_Width)      # Hay 5 -> 50%
            Space_fi_Fi = round((30/100) * Terminal_Width)     # Hay 2 -> 30%
            space_intervals = round((1/5) * Terminal_Width)  # Hay 1 -> 20%
            frecuence = list(values.keys())

            if(Terminal_Width > space + Space_fi_Fi + space_intervals):
                Difference_Width = Terminal_Width - (space + Space_fi_Fi + space_intervals)
                space_intervals += Difference_Width
            else:
                Difference_Width = (space + Space_fi_Fi + space_intervals) - Terminal_Width 
                space_intervals -= Difference_Width
                
            print(f"|{frecuence[0]:^{Space_Intervals}}|{frecuence[1]:^{Space_For_Others}}|{frecuence[2]:^{Space_fi_Fi}}|{frecuence[3]:^{Space_fi_Fi}}|{frecuence[4]:^{Space_For_Others}}|{frecuence[5]:^{Space_For_Others}}|{frecuence[6]:^{Space_For_Others}}|{frecuence[7]:^{Space_For_Others}}|")
            print(f"|{'':-^{Space_Intervals}}|{'':-^{Space_For_Others}}|{'':-^{Space_fi_Fi}}|{'':-^{Space_fi_Fi}}|{'':-^{Space_For_Others}}|{'':-^{Space_For_Others}}|{'':-^{Space_For_Others}}|{'':-^{Space_For_Others}}|")
            intervals_text = [f"[ {Limit[0]} - {Limit[1]} >" for Limit in values["intervalos"]]
                
            for idx in range(0 , len(intervals_text)):
                pi_text = f"{values["pi"][idx]:.{precision}f}%"
                Pi_text = f"{values["Pi"][idx]:.{precision}f}%"
                print(f"|{intervals_text[idx]:^{Space_Intervals}}|{values['xi'][idx]:^{Space_For_Others}.{precision}f}|{values['fi'][idx]:^{Space_fi_Fi}}|{values['Fi'][idx]:^{Space_fi_Fi}}|{values['hi'][idx]:^{Space_For_Others}.{precision}f}|{values['Hi'][idx]:^{Space_For_Others}.{precision}f}|{pi_text:^{Space_For_Others}}|{Pi_text:^{Space_For_Others}}|")
            print(f"|{'':-^{Space_Intervals}}|{'':-^{Space_For_Others}}|{'':-^{Space_fi_Fi}}|{'':-^{Space_fi_Fi}}|{'':-^{Space_For_Others}}|{'':-^{Space_For_Others}}|{'':-^{Space_For_Others}}|{'':-^{Space_For_Others}}|")
            print(f"|{'Total':^{Space_Intervals}}|{'':^{Space_For_Others}}|{np.sum(values['fi']):^{Space_fi_Fi}}|{'':^{Space_fi_Fi}}|{round(np.sum(values['hi']) , 3):^{Space_For_Others}}|{'':^{Space_For_Others}}|{f'{round(np.sum(values['pi']) , 3)}%':^{Space_For_Others}}|{'':^{Space_For_Others}}|")
            
            print(f"{'':=^{Get_Terminal_Dimensions()[0]}}")
        elif(name == "Central_Tendency_Measures"):
            space = 40
            print(f"{name:=^{(space*3) + 4}}")
            name_central_tendency_measure = list(values.keys())

            print(f"|{name_central_tendency_measure[0]:^{space}}|{name_central_tendency_measure[1]:^{space}}|{name_central_tendency_measure[2]:^{space}}|")
            print(f"|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|")
            if(len(values["Mo"]) > 1):
                print(f"|{values['X_']:^{space}.{precision}f}|{values['Me']:^{space}.{precision}f}|{values['Mo'][0]:^{space}.{precision}f}|")
                for i , Mo in enumerate(values["Mo"]):
                    if(i == 0):
                        continue
                    print(f"|{'':^{space}}|{'':^{space}}|{Mo:^{space}.{precision}f}|")
            else:
                print(f"|{values['X_']:^{space}.{precision}f}|{values['Me']:^{space}.{precision}f}|{values['Mo'][0]:^{space}.{precision}f}|")
            print(f"{'':=^{(space*3) + 4}}")
        elif(name == "Dispersion_Measures"):
            space = 40
            print(f"{name:=^{(space*3) + 4}}")
            name_dispersion_measure = list(values.keys())

            print(f"|{name_dispersion_measure[0]:^{space}}|{name_dispersion_measure[1]:^{space}}|{name_dispersion_measure[2]:^{space}}|")
            print(f"|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|")
            print(f"|{values['S_2']:^{space}.{precision}f}|{values['S']:^{space}.{precision}f}|{values['CV%']:^{space}.{precision}f}|")
            print(f"{'':=^{(space*3) + 4}}")
        elif(name == "Position_Measures"):
            space = 40
            print(f"{name:=^{(space*3) + 4}}")
            name_position_measure = list(values.keys())

            print(f"|{name_position_measure[0]:^{space}}|{name_position_measure[1]:^{space}}|{name_position_measure[2]:^{space}}|")
            print(f"|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|")
            for i in range(0 , 20):
                if(i < 3):
                    Quartiles_Text = f"Q_{i + 1}: {values['Cuartiles'][i]:.{precision}f}"
                    Deciles_Text = f"D_{i + 1}: {values['Deciles'][i]:.{precision}f}"
                    Percentiles_Text = f"P_{i + 1}: {values['Percentiles'][i]:.{precision}f}"
                    print(f"|{Quartiles_Text:^{space}}|{Deciles_Text:^{space}}|{Percentiles_Text:^{space}}|")
                elif(i < 9):
                    Deciles_Text = f"D_{i + 1}: {values['Deciles'][i]:.{precision}f}"
                    Percentiles_Text = f"P_{i + 1}: {values['Percentiles'][i]:.{precision}f}"
                    print(f"|{'':^{space}}|{Deciles_Text:^{space}}|{Percentiles_Text:^{space}}|")
                else:
                    Percentiles_Text = f"P_{i + 1}: {values['Percentiles'][i]:.{precision}f}"
                    print(f"|{'':^{space}}|{'':^{space}}|{Percentiles_Text:^{space}}|")
            print(f"{'':=^{(space*3) + 4}}")
        elif(name == "Base_Results"):
            space = 50
            print(f"{name:=^{space + 2}}")
            for name_b_result , value in values.items():
                print(f"|{name_b_result:^{space}}|")
                print(f"|{'':-^{space}}|")
                print(f"|{value:^{space}}|")
                print(f"|{'':_^{space}}|")
            print(f"{'':=^{space + 2}}")
        print("\n")

def Print_Results_Cuantitative_No_Grouped_Data_In_Terminal(results , precision):
    for name , values in results.items():
        if(name == "Frecuences_Results"):
            print(f"{name:=^{Get_Terminal_Dimensions()[0]}}")
            space = 22
            space_xi = 25
            Space_fi_Fi = 14
            frecuence = list(values.keys())
                
            print(f"|{frecuence[0]:^{space_xi}}|{frecuence[1]:^{Space_fi_Fi}}|{frecuence[2]:^{Space_fi_Fi}}|{frecuence[3]:^{space}}|{frecuence[4]:^{space}}|{frecuence[5]:^{space}}|{frecuence[6]:^{space}}|")
            print(f"|{'':-^{space_xi}}|{'':-^{Space_fi_Fi}}|{'':-^{Space_fi_Fi}}|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|")
                
            for idx in range(0 , len(values["xi"])):
                pi_text = f"{values["pi"][idx]:.{precision}f}%"
                Pi_text = f"{values["Pi"][idx]:.{precision}f}%"
                print(f"|{values["xi"][idx]:^{space_xi}}|{values["fi"][idx]:^{Space_fi_Fi}}|{values["Fi"][idx]:^{Space_fi_Fi}}|{values["hi"][idx]:^{space}.{precision}f}|{values["Hi"][idx]:^{space}.{precision}f}|{pi_text:^{space}}|{Pi_text:^{space}}|")
            print(f"|{'':-^{space_xi}}|{'':-^{Space_fi_Fi}}|{'':-^{Space_fi_Fi}}|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|")
            print(f"|{'Total':^{space_xi}}|{np.sum(values["fi"]):^{Space_fi_Fi}}|{'':^{Space_fi_Fi}}|{round(np.sum(values["hi"]) , 3):^{space}}|{'':^{space}}|{f'{round(np.sum(values["pi"]) , 3)}%':^{space}}|{'':^{space}}|")
            print(f"{'':=^{Get_Terminal_Dimensions()[0]}}")
        elif(name == "Central_Tendency_Measures"):
            space = 40
            print(f"{name:=^{(space*3) + 4}}")
            name_central_tendency_measure = list(values.keys())

            print(f"|{name_central_tendency_measure[0]:^{space}}|{name_central_tendency_measure[1]:^{space}}|{name_central_tendency_measure[2]:^{space}}|")
            print(f"|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|")
            if(len(values["Mo"]) > 1):
                print(f"|{values["X_"]:^{space}.{precision}f}|{values["Me"]:^{space}.{precision}f}|{values["Mo"][0]:^{space}.{precision}f}|")
                for i , Mo in enumerate(values["Mo"]):
                    if(i == 0):
                        continue
                    print(f"|{'':^{space}}|{'':^{space}}|{Mo:^{space}.{precision}f}|")
            else:
                print(f"|{values["X_"]:^{space}.{precision}f}|{values["Me"]:^{space}.{precision}f}|{values["Mo"][0]:^{space}.{precision}f}|")
            print(f"{'':=^{(space*3) + 4}}")
        elif(name == "Dispersion_Measures"):
            space = 40
            print(f"{name:=^{(space*3) + 4}}")
            name_dispersion_measure = list(values.keys())

            print(f"|{name_dispersion_measure[0]:^{space}}|{name_dispersion_measure[1]:^{space}}|{name_dispersion_measure[2]:^{space}}|")
            print(f"|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|")
            print(f"|{values["S_2"]:^{space}.{precision}f}|{values["S"]:^{space}.{precision}f}|{values["CV%"]:^{space}.{precision}f}|")
            print(f"{'':=^{(space*3) + 4}}")
        elif(name == "Position_Measures"):
            space = 40
            print(f"{name:=^{(space*3) + 4}}")
            name_position_measure = list(values.keys())

            print(f"|{name_position_measure[0]:^{space}}|{name_position_measure[1]:^{space}}|{name_position_measure[2]:^{space}}|")
            print(f"|{'':-^{space}}|{'':-^{space}}|{'':-^{space}}|")
            for i in range(0 , 20):
                if(i < 3):
                    Quartiles_Text = f"Q_{i + 1}: {values["Cuartiles"][i]:.{precision}f}"
                    Deciles_Text = f"D_{i + 1}: {values["Deciles"][i]:.{precision}f}"
                    Percentiles_Text = f"P_{i + 1}: {values["Percentiles"][i]:.{precision}f}"
                    print(f"|{Quartiles_Text:^{space}}|{Deciles_Text:^{space}}|{Percentiles_Text:^{space}}|")
                elif(i < 9):
                    Deciles_Text = f"D_{i + 1}: {values["Deciles"][i]:.{precision}f}"
                    Percentiles_Text = f"P_{i + 1}: {values["Percentiles"][i]:.{precision}f}"
                    print(f"|{'':^{space}}|{Deciles_Text:^{space}}|{Percentiles_Text:^{space}}|")
                else:
                    Percentiles_Text = f"P_{i + 1}: {values["Percentiles"][i]:.{precision}f}"
                    print(f"|{'':^{space}}|{'':^{space}}|{Percentiles_Text:^{space}}|")
            print(f"{'':=^{(space*3) + 4}}")
        elif(name == "Base_Results"):
            space = 50
            print(f"{name:=^{space + 2}}")
            for name_b_result , value in values.items():
                print(f"|{name_b_result:^{space}}|")
                print(f"|{'':-^{space}}|")
                print(f"|{value:^{space}}|")
                print(f"|{'':_^{space}}|")
            print(f"{'':=^{space + 2}}")
        print("\n")

