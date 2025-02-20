import numpy as np
import collections

def Calc_fi_And_xi(Data):
    Counts = collections.Counter(Data)
    return [xi for xi in Counts.keys()] , [fi for fi in Counts.values()]

def calc_Fi(Arr_fi):
    return np.cumsum(Arr_fi)

def Calc_hi(Data , Arr_fi):
    return [value/len(Data) for value in Arr_fi]

def Calc_Hi(Arr_hi):
    return np.cumsum(Arr_hi)

def Calc_hi_percent(Arr_hi):
    return [value*100 for value in Arr_hi]

def Calc_Hi_percent(Arr_Hi):
    return [value*100 for value in Arr_Hi]