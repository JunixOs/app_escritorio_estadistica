import numpy as np
from collections import Counter

def Calc_fi_And_xi(Data):
    Counts = Counter(Data)
    Arr_xi = sorted(Counts.keys())

    Arr_fi = [Counts[xi] for xi in Arr_xi]
    
    # Evitar usar metodo count() aqui debido a que la complejidad aumenta O(n * m)
    # n = numero de elementos unicos
    # m = numero de elementos totales
    # Mantener el uso de Counter()

    return Arr_xi , Arr_fi

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