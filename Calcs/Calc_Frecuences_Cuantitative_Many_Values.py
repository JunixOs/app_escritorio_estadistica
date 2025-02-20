from math import *
import numpy as np
import collections
from decimal import Decimal , getcontext
import decimal

def Calc_Max_Decimal_Number(Numbers):
    N_Decimals = []
    for Number in Numbers:

        Temp = str(Number)
        if "." in Temp:
            N_Decimals.append(len(Temp.split(".")[1]))

    Ocurrences = collections.Counter(N_Decimals)
    return Ocurrences.most_common(1)

def Calc_Max(Data):
    return max(Data)

def Calc_Min(Data):
    return min(Data)

def Calc_Range(Min , Max):
    return Max-Min

def Calc_Intervals(Min , C , Max , m , Precision):
    Arr_Intervals = [[0 for _ in range(2)] for _ in range(m)]
    
    Acumulate = Min
    for a in range(0 , m):
        for b in range(0 , 2):
            if(b==0):
                Arr_Intervals[a][b] = Acumulate
            else:
                Acumulate = Acumulate + C
            
            if(Acumulate>Max):
                Acumulate=Max
            if(Acumulate<Max and a==m-1 and b==1):
                Acumulate=Max
            
            if(Precision!=0):
                Arr_Intervals[a][b] = round(Acumulate , Precision)
            else:
                Arr_Intervals[a][b] = round(Acumulate)

    return Arr_Intervals

def Calc_Groups(Intervals , m , Precision):
    getcontext().prec = 50
    Arr_Groups = []
    for a in range (0 , m):
        Ls = Decimal(Intervals[a][1])

        if(a==m-1):
            Arr_Groups.append(Intervals[a][1])
        else:
            if(Precision==0):
                Arr_Groups.append(Ls - Decimal(1))
            else:
                Subs = Decimal(1) * Decimal(10) ** (-Precision)
                Group = Ls - Subs
                try:
                    Round = Group.quantize(Decimal(10) ** -Precision)
                    Arr_Groups.append(Round)
                except decimal.InvalidOperation:
                    Arr_Groups.append(f"{Group:.0f}")
    return Arr_Groups

def Calc_xi(Intervals , m):
    Arr_xi = []
    for a in range (0 , m):
        Arr_xi.append((Intervals[a][1]+Intervals[a][0])/2)

    return Arr_xi

def Calc_fi(Data , Intervals , m):
    Arr_fi = []
    Count = 0
    for n in range(0 , m):
        for a in range(0 , len(Data)):
            if(n==m-1):
                if(Intervals[n][0] <= Data[a] <= Intervals[n][1]):
                    Count += 1
            else:
                if(Intervals[n][0] <= Data[a] < Intervals[n][1]):
                        Count += 1
        Arr_fi.append(Count)
        Count = 0
    return Arr_fi

def Calc_Fi(fi):
    return np.cumsum(fi)

def Calc_hi(Data , fi):
    return [value/len(Data) for value in fi]

def Calc_Hi(hi):
    return np.cumsum(hi)

def Calc_hi_percent(hi):
    return [value*100 for value in hi]

def Calc_Hi_percent(Hi):
    return [value*100 for value in Hi]