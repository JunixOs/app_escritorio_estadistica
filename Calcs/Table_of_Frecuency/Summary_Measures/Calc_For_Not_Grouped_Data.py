import math
import numpy as np

def Calc_Arithmetic_Average(Data):
    return np.sum(Data)/len(Data)

def Calc_Geometric_Average(Data):
    if(any(x < 0 for x in Data)):
        return "Indeterminado"
    elif(any(xi == 0 for xi in Data)):
        return 0

    return np.exp(np.sum(np.log(Data))/len(Data))

def Calc_Armonic_Average(Data):
    Summa = 0
    for value in Data:
        if(value == 0):
            return "Indeterminado"
        else:
            Summa += 1/value
    X_h = len(Data)/Summa
    return X_h

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

###### Coef de Asimetria
def Calc_Pearson_Coefficient(Arith_Average , Me , S):
    return 3*(Arith_Average - Me)/S

def Calc_Fisher_Coefficient(Data , Arith_Average , n , S):
    return np.sum((xi - Arith_Average) ** 3 for xi in Data)/(n * (S ** 3))

def Calc_Kurtosis_Coefficient(Data , Arith_Average , n , S):
    return (np.sum((xi - Arith_Average) ** 4 for xi in Data)/(n * (S ** 4))) - 3