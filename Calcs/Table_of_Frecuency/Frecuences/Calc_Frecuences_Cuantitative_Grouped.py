from math import *
import numpy as np
from decimal import Decimal , getcontext
import decimal

def Rounding_Up(Number , N_Decimals):
    """
        ==============================================================================================
        Esta funcion se encarga de redondear la amplitud, recibe un valor y le añade una decima de mas 
        para que el ultimo intervalo se pase un poco del valor maximo del dataset.
        Ejemplos de uso:
            Input: 1.3456 , N_Decimals = 2
            Output: 1.346

            Input: 0.02 , N_Decimals = 2
            Output: 0.021
        ==============================================================================================
    """
    """ 
        antes de redondear revisar si el ultimo decimal es >=5 o <5
    """
    if(Number - round(Number) != 0):
        print(f"{Number=}")
        Integer_Part = str(Number).split(".")[0]
        Decimal_Part = str(Number).split(".")[1]

        N_Decimals = N_Decimals if N_Decimals < len(Decimal_Part) else len(Decimal_Part)
        if(N_Decimals > len(Decimal_Part) - 1):
            Decimal_Part += "0"
    
        if(int(Decimal_Part[N_Decimals]) >= 5):
            Decimal_Part = "".join([val for i , val in enumerate(Decimal_Part , start=1) if i <= N_Decimals])
            Value_To_Add = float("0." + "0"*(N_Decimals - 1) + "1")
        else:
            Decimal_Part = "".join([val for i , val in enumerate(Decimal_Part , start=1) if i <= N_Decimals + 1])
            Value_To_Add = "0." + "0"*N_Decimals + "1"
            N_Decimals += 1

        Number = float(Integer_Part + "." + Decimal_Part)
        
        print("Numero cortado: " , Number)

        Decimals_To_Round = "1." + "0"*(N_Decimals) if N_Decimals > 0 else "1"

        Number + float(Value_To_Add)

        Number = float(Decimal(str(Number)).quantize(Decimal(Decimals_To_Round)))
        
        """ 
        Number = Decimal(str(Number))
        Decimals_To_Round = "1." + "0"*N_Decimals if N_Decimals > 0 else "1"
        return float(Number.quantize(Decimal(Decimals_To_Round) , rounding=ROUND_UP)) """
        Number += float(Value_To_Add)
        print(f"{Number=}")

        return round(Number , N_Decimals)
    else:
        return Number + 0.1

def Calc_Max_Decimal_Number(Numbers):
    N_Decimals = []
    for Number in Numbers:

        Temp = str(Number)
        if "." in Temp:
            N_Decimals.append(len(Temp.split(".")[1]))
        else:
            N_Decimals.append(0)

    return max(N_Decimals)

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

            """ if((Acumulate != Max) and (a == m-1 and b == 1)):
                Arr_Intervals[a][b] = Max
            else:
                Arr_Intervals[a][b] = round(Acumulate , Precision) """
            
            Arr_Intervals[a][b] = round(Acumulate , Precision)

    return Arr_Intervals

def Calc_Groups_For_Integer_Numbers(Intervals , m , Precision):
    Arr_Groups = []
    for a in range (0 , m):
        Ls = Intervals[a][1]

        if(a==m-1):
            Arr_Groups.append(Intervals[a][1])
        else:
            if(Precision==0):
                Arr_Groups.append(Ls - Decimal(1))
            else:
                Subs = 10 ** (-Precision)
                Group = Ls - Subs
                Arr_Groups.append(round(Group , Precision))
    return Arr_Groups

def Calc_Groups_For_Decimal_Numbers(Intervals , m , Precision):
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

if(__name__ == "__main__"):
    Number = float(input("Ingrese la amplitud: "))
    Precision = int(input("Ingrese la precision: "))
    print("El valor redondeado de la amplitud es: " , Rounding_Up(Number , Precision))