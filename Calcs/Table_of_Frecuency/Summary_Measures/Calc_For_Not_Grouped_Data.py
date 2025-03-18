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

def Calc_Interquartile_Range(Arr_Quartile):
    return Arr_Quartile[2] - Arr_Quartile[0]


###### Coef de Asimetria
def Calc_Pearson_Coefficient(Arith_Average , Me , S):
    return 3*(Arith_Average - Me)/S

def Calc_Fisher_Coefficient(Data , Arith_Average , n , S):
    return np.sum((xi - Arith_Average) ** 3 for xi in Data)/(n * (S ** 3))

def Calc_Kurtosis_Coefficient(Data , Arith_Average , n , S):
    return (np.sum((xi - Arith_Average) ** 4 for xi in Data)/(n * (S ** 4))) - 3

def Calc_Bowley_Coefficient(Arr_Quartile):
    if(Arr_Quartile):
        return (Arr_Quartile[2] + Arr_Quartile[0] - (2*Arr_Quartile[1]))/(Arr_Quartile[2] - Arr_Quartile[0])
    else:
        return "No se pudo calcular"    

def Calc_Kelly_Coefficient(Arr_Decile):
    if(Arr_Decile):
        return (Arr_Decile[8] + Arr_Decile[0] - (2 * Arr_Decile[4]))/(Arr_Decile[8] - Arr_Decile[0])
    else:
        return "No se pudo calcular"


###### Cuantiles (Cuartiles , Deciles , Percentiles)
def Calc_Quantile(N_Quantile , Data):
    if((N_Quantile == 4 and len(Data) < 5) or ((N_Quantile == 10 or N_Quantile == 100) and len(Data) < 10)):
        return []

    Arr_Quantile = []
    n = len(Data)
    for k in range(1 , N_Quantile):
        Q_k = k*(n+1)/N_Quantile
        if(isinstance(Q_k , float)):
            Pos_E1 = math.floor(Q_k) - 1
            if(round(Q_k) == Pos_E1):
                Pos_E2 = round(Q_k + 1) - 1
            else:
                Pos_E2 = round(Q_k) - 1
            
            e = Q_k - math.floor(Q_k)
            if(Pos_E2 >= n):
                Q_k = Data[Pos_E1] + (Data[-1] - Data[Pos_E1]) * e
            else:
                Q_k = Data[Pos_E1] + (Data[Pos_E2] - Data[Pos_E1]) * e
            Arr_Quantile.append(Q_k)
        else:
            if(Q_k >= n):
                Arr_Quantile.append(Data[-1])
            else:
                Arr_Quantile.append(Data[Q_k - 1])

    return Arr_Quantile