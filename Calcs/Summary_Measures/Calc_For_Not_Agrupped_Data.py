import math
import numpy as np

def Calc_Arithmetic_Average(Data):
    return np.sum(Data)/len(Data)

def Calc_Geometric_Average(Data):
    return pow(np.prod(Data) , 1/len(Data))

def Calc_Armonic_Average(Data):
    return len(Data)/sum(1/value for value in Data)

def Calc_Median_Me(Data):
    Copy_Data = Data.copy()
    Copy_Data.sort()
    n = len(Copy_Data)
    if (n % 2 == 1):
        Me = Copy_Data[(n-1)//2]
    else:
        Me = (Copy_Data[(n//2)-1]+Copy_Data[n//2])/2
    return Me

def Calc_Mode_Mo(Arr_xi , Arr_fi):
    Max_Rep = max(Arr_fi)
    Mo = [Arr_xi[a] for a in range(0 , len(Arr_fi)) if Arr_fi[a] == Max_Rep]
    return Mo


####### Medidas de variabilidad o de dispercion muestral
def Calc_Variance(Arith_Average , Data):
    return sum(pow(value - Arith_Average , 2) for value in Data)/(len(Data) - 1)

def Calc_Standard_Deviation(Variance):
    return math.pow(Variance , 1/2)

def Calc_Percentage_Coefficient_Variation(Standart_Variation , Arith_Average):
    return (Standart_Variation/Arith_Average)*100

def Calc_Symmetry_Coefficient(Arith_Average , Me , S):
    return 3*(Arith_Average - Me)/S