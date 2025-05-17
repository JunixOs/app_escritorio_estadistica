import numpy as np
import collections

def Order_Variable_Cualitative_Ordinal(Arr_ai):
    """
        ==============================================================================================
        Ordena de manera ascendente las Variables Cuantitativas Ordinales, pero sin
        perder el formato original de entrada.
        ==============================================================================================
    """
    Dictionary_Possible_Orders = {
        "Likert_Scale" : ["muy malo" , "malo" , "regular" , "bueno" , "excelente"],
        "Likert_Scale_Initials" : ["m" , "r" , "b" , "e"],
        "Grade" : ["inicial" , "primaria" , "secundaria" , "superior" , "maestria" , "doctorado"],
        "Socioeconomic_Level": ["bajo" , "medio-bajo" , "medio" , "medio-alto" , "alto"],
        "Military_Rank": ["soldado" , "cabo" , "sargento"],
        "Place_In_Competition": ["5° lugar" , "4° lugar" , "3° lugar" , "2° lugar" , "1° lugar"],
        "Pain_Scale": ["leve" , "moderado" , "severo"],
        "Frecuency": ["nunca" , "rara vez" , "a veces" , "frecuentemente" , "siempre"]
    }

    Formatted_ai = [ai.lower() for ai in Arr_ai]
    Ordered_Data = []
    for value_in_dict in Dictionary_Possible_Orders.values():
        for value in value_in_dict:
            if(value in Formatted_ai):
                Ordered_Data.append(Arr_ai[Formatted_ai.index(value)])

        if(len(Ordered_Data) == len(Arr_ai)):
            break

    return Ordered_Data

def Calc_fi_And_ai(Data):
    Arr_ai = list(set(Data))
    Arr_ai = Order_Variable_Cualitative_Ordinal(Arr_ai)

    Arr_fi = [Data.count(ai) for ai in Arr_ai]

    return Arr_ai , Arr_fi

def Calc_Fi(Arr_fi):
    return np.cumsum(Arr_fi)

def Calc_hi(Data , Arr_fi):
    return [value/len(Data) for value in Arr_fi]

def Calc_Hi(Arr_hi):
    return np.cumsum(Arr_hi)

def Calc_hi_percent(Arr_hi):
    return [value*100 for value in Arr_hi]

def Calc_Hi_percent(Arr_Hi):
    return [value*100 for value in Arr_Hi]
