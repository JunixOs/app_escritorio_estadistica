import math
def Calc_Arithmetic_Average(Data , Precision):
    Summa = 0
    for a in Data:
        Summa += a
    return round(Summa/len(Data) , Precision)

def Calc_Geometric_Average(Data , Precision):
    Prod = 1
    for a in Data:
        Prod *= a
    return round(math.pow(Prod, 1/len(Data)) , Precision)

def Calc_Armonic_Average(Data , Precision):
    Inv_Summa = 0
    for a in Data:
        Inv_Summa += 1/a
    return round(len(Data)/Inv_Summa , Precision)

def Calc_Median_Me(Data):
    Copy_Data = Data.copy()
    Copy_Data.sort()
    n = len(Copy_Data)
    if (n // 2 == 1):
        Me = Copy_Data[(n-1)/2]
    else:
        Me = (Copy_Data[(n/2)-1]+Copy_Data[n/2])/2
    return Me

def Calc_Mode_Mo(Arr_xi , Arr_fi):
    Max_Rep = max(Arr_fi)
    Mo = []
    for a in range(0 , len(Arr_fi)):
        if(Arr_fi[a] == Max_Rep):
            Mo.append(Arr_xi[a])
    return Mo


####### Medidas de variabilidad o de dispercion muestral
def Calc_Variance(Arith_Average , Data , Precision):
    Summa = 0
    for a in Data:
        Summa += math.pow(a - Arith_Average , 2)

    return round(Summa/(len(Data) - 1) , Precision)

def Calc_Standard_Deviation(Variance , Precision):
    return round(math.pow(Variance , 1/2) , Precision)

def Calc_Percentage_Coefficient_Variation(Standart_Variation , Arith_Average , Precision):
    return round((Standart_Variation/Arith_Average)*100 , Precision)