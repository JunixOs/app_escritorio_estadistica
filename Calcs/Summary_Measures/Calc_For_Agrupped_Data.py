import math
def Calc_Arithmetic_Average(n , arr_xi , arr_fi , Precision):
    Summa = 0
    for a in range(0 , len(arr_xi)):
        Summa += (arr_xi[a] * arr_fi[a])

    return round(Summa/n , Precision)

def Calc_Geometric_Average(n , Arr_xi , Arr_fi , Precision):
    Summa = 0
    for a in range(0 , len(Arr_xi)):
        Summa += (Arr_fi[a] * math.log10(Arr_xi[a]))

    return round(math.pow(10 , (Summa/n)) , Precision)

def Calc_Armonic_Average(n , Arr_xi , Arr_fi , Precision):
    Inv_Summa = 0
    for a in range(0 , len(Arr_xi)):
        Inv_Summa += Arr_fi[a]/Arr_xi[a]
    
    return round(n/Inv_Summa , Precision)

def Calc_Median_Me(n , Arr_fi , Arr_Fi , Arr_Intervals , C , Precision):
    Fi = n/2
    position_Fi = None
    for a in range(0 , len(Arr_Fi)):
        if(Arr_Fi[a] >= Fi):
            position_Fi = a
            break
    if(position_Fi):
        return round(Arr_Intervals[position_Fi][0] + (((n/2)-Arr_Fi[position_Fi-1])/Arr_fi[position_Fi])*C , Precision)
    else:
        raise Exception("No se pudo calcular la Mediana para los datos agrupados.")
    
def Calc_Mode_Mo(Arr_fi , Arr_Intervals , C , Precision):
    Max_fi = max(Arr_fi)
    Position_Modal_Class = []
    Mo = []
    for a in range(0 , len(Arr_fi)):
        if(Arr_fi[a] == Max_fi):
            Position_Modal_Class.append(a)
    if(len(Position_Modal_Class) > 1):
        for a in Position_Modal_Class:
            if(a == len(Arr_fi) - 1):
                d1 = Arr_fi[a] - Arr_fi[a - 1]
                d2 = Arr_fi[a]
                Mo.append(round(Arr_Intervals[a][0] + (d1/(d1 + d2))*C , Precision))
            elif(a == 0):
                d1 = Arr_fi[a]
                d2 = Arr_fi[a] - Arr_fi[a + 1]
                Mo.append(round(Arr_Intervals[a][0] + (d1/(d1 + d2))*C , Precision))
            else:
                d1 = Arr_fi[a] - Arr_fi[a - 1]
                d2 = Arr_fi[a] - Arr_fi[a + 1]
                Mo.append(round(Arr_Intervals[a][0] + (d1/(d1 + d2))*C , Precision))

        return Mo
    else:
        Pos = Position_Modal_Class[0]
        if(Pos == len(Arr_fi) - 1):
            d1 = Arr_fi[Pos] - Arr_fi[a - 1]
            d2 = Arr_fi[Pos]
            Mo.append(round(Arr_Intervals[Pos][0]+(d1/(d1 + d2))*C , Precision))
        elif(Pos == 0):
            d1 = Arr_fi[Pos]
            d2 = Arr_fi[Pos] - Arr_fi[Pos + 1]
            Mo.append(round(Arr_Intervals[Pos][0] + (d1/(d1 + d2))*C , Precision))
        else:
            d1 = Arr_fi[Pos] - Arr_fi[Pos - 1]
            d2 = Arr_fi[Pos] - Arr_fi[Pos + 1]
            Mo.append(round(Arr_Intervals[Pos][0]+(d1/(d1 + d2))*C , Precision))

        return Mo
    
##### Medidas de Variabilidad o de dispresion Muestral
def Calc_Variance(n , Arr_xi , Arr_fi , Arith_Average , Precision):
    Summa = 0
    for a in range(0 , len(Arr_xi)):
        Summa += (math.pow(Arr_xi[a] - Arith_Average , 2)*Arr_fi[a])
    return round(Summa/(n-1) , Precision)

def Calc_Standard_Deviation(Variance , Precision):
    return round(math.pow(Variance , 1/2) , Precision)

def Calc_Percentage_Coefficient_Variation(Standart_Deviation , Arith_Average , Precision):
    return round((Standart_Deviation/Arith_Average)*100 , Precision)