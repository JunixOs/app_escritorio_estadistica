import numpy as np
import collections

def Order_Variable_Cuantitative_Ordinal(Data):
    Dictionary_Possible_Orders = {
        "Likert_Scale" : ["muy malo" , "malo" , "regular" , "bueno" , "excelente"],
        "Likert_Scale_Initials" : ["m" , "r" , "b" , "e"],
        "Grade" : ["inicial" , "primaria" , "secundaria" , "superior" , "maestria" , "doctorado"],
    }

    Ordered_Data = [value for value_list in Dictionary_Possible_Orders.values() for value in value_list if value in Data]

    return Ordered_Data

def Calc_fi_And_ai(Data):
    Counts = collections.Counter(Data)
    return [ai for ai in Counts.keys()] , [fi for fi in Counts.values()]

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
