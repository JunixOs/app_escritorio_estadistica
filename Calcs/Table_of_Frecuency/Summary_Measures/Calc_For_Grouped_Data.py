import math
import numpy as np

def Calc_Arithmetic_Average(n , arr_xi , arr_fi):
    return np.sum(arr_xi[pos]*arr_fi[pos] for pos in range(0 , len(arr_xi)))/n

def Calc_Geometric_Average(n , Arr_xi , Arr_fi):
    if(any(xi < 0 for xi in Arr_xi)):
        return "Indeterminado"
    elif(any(xi == 0 for xi in Arr_xi)):
        return 0

    return 10**(np.sum(Arr_fi[pos] * math.log10(Arr_xi[pos]) for pos in range(0 , len(Arr_xi)))/n)

def Calc_Armonic_Average(n , Arr_xi , Arr_fi):
    if(any(xi == 0 for xi in Arr_xi)):
        return "Indeterminado"

    return n/np.sum(Arr_fi[pos]/Arr_xi[pos] for pos in range(0 , len(Arr_xi)))

def Calc_Median_Me(n , Arr_fi , Arr_Fi , Arr_Intervals , C):
    Fi = n/2
    position_Fi = None
    for a in range(0 , len(Arr_Fi)):
        if(Arr_Fi[a] >= Fi):
            position_Fi = a
            break
    if(position_Fi == 0):
        return Arr_Intervals[position_Fi][0] + (((n/2)- 0 )/Arr_fi[position_Fi])*C
    elif(position_Fi > 0):
        return Arr_Intervals[position_Fi][0] + (((n/2)-Arr_Fi[position_Fi-1])/Arr_fi[position_Fi])*C
    else:
        raise Exception("No se pudo calcular la Mediana para los datos agrupados.")
    
def Calc_Mode_Mo(Arr_fi , Arr_Intervals , C):
    """ 
        ==============================================================================================
        La moda para datos agrupados se calcula en base al mayor fi (frecuencia relativa simple), si 
        en caso este estuviera en uno de los extremos de la tabla de frecuencias, al inicio o al
        ultimo, el valor del fi posterior o siguiente se considera como 0 (cero).
        ==============================================================================================
    """
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
                d2 = Arr_fi[a] - 0
                Mo.append(Arr_Intervals[a][0] + (d1/(d1 + d2))*C)
            elif(a == 0):
                d1 = Arr_fi[a] - 0
                d2 = Arr_fi[a] - Arr_fi[a + 1]
                Mo.append(Arr_Intervals[a][0] + (d1/(d1 + d2))*C)
            else:
                d1 = Arr_fi[a] - Arr_fi[a - 1]
                d2 = Arr_fi[a] - Arr_fi[a + 1]
                Mo.append(Arr_Intervals[a][0] + (d1/(d1 + d2))*C)

        return Mo
    else:
        Pos = Position_Modal_Class[0]
        if(Pos == len(Arr_fi) - 1):
            d1 = Arr_fi[Pos] - Arr_fi[a - 1]
            d2 = Arr_fi[Pos]
            Mo.append(Arr_Intervals[Pos][0]+(d1/(d1 + d2))*C)
        elif(Pos == 0):
            d1 = Arr_fi[Pos]
            d2 = Arr_fi[Pos] - Arr_fi[Pos + 1]
            Mo.append(Arr_Intervals[Pos][0] + (d1/(d1 + d2))*C)
        else:
            d1 = Arr_fi[Pos] - Arr_fi[Pos - 1]
            d2 = Arr_fi[Pos] - Arr_fi[Pos + 1]
            Mo.append(Arr_Intervals[Pos][0]+(d1/(d1 + d2))*C)

        return Mo


##### Medidas de Variabilidad o de dispresion Muestral
def Calc_Variance(n , Arr_xi , Arr_fi , Arith_Average):
    return np.sum(math.pow(Arr_xi[pos] - Arith_Average , 2)*Arr_fi[pos] for pos in range (0 , len(Arr_xi)))/(n-1)

def Calc_Standard_Deviation(Variance):
    return math.pow(Variance , 1/2)

def Calc_Percentage_Coefficient_Variation(Standart_Deviation , Arith_Average):
    return (Standart_Deviation/Arith_Average)*100

def Calc_Interquartile_Range(Arr_Quartile):
    return Arr_Quartile[2] - Arr_Quartile[0]


##### Coef de Asimetria
def Calc_Pearson_Coefficient(Arith_Average , Me , S):
    return 3*(Arith_Average - Me)/S

def Calc_Fisher_Coefficient(Arr_xi , Arith_Average , Arr_fi , n , S):
    return np.sum(((Arr_xi[i] - Arith_Average) ** 3 ) * Arr_fi[i] for i in range(len(Arr_xi)))/(n * (S ** 3))

def Calc_Kurtosis_Coefficient(Arr_Percentiles , Arr_xi , Arith_Average , Arr_fi , n , S):
    """ 
        ==============================================================================================
        Calculo con Percentiles:
        Elimine las comillas en el return para activar el calculo del coeficiente de kurtosis con 
        Percentiles
        ==============================================================================================
    """
    """ 
    if(Arr_Percentiles):
        return ((Arr_Percentiles[74] - Arr_Percentiles[24])/(Arr_Percentiles[89] - Arr_Percentiles[9])) - 0.5 
    else:
        return "No se pudo calcular"
    """
    return (np.sum(((Arr_xi[i] - Arith_Average) ** 4) * Arr_fi[i] for i in range(len(Arr_xi)))/(n * (S ** 4))) - 3

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


##### Cuantiles (Cuartiles , Deciles , Percentiles)
def Calc_Quantile(N_Quantile , Data , Intervals , Arr_fi , Arr_Fi , C):
    if((N_Quantile == 4 and len(Intervals) < 5) or ((N_Quantile == 10 or N_Quantile == 100) and len(Intervals) < 5)):
        return []

    Arr_Quantile = []
    n = len(Data)
    for k in range(1 , N_Quantile):
        P = (k*n)/N_Quantile

        pos = None
        for a in range(0 , len(Arr_Fi)):
            if(Arr_Fi[a] >= P):
                pos = a
                break

        if(pos == 0):
            Arr_Quantile.append(Intervals[pos][0] + ((P - 0)/Arr_fi[pos])*C)
        else:
            Arr_Quantile.append(Intervals[pos][0] + ((P - Arr_Fi[pos - 1])/Arr_fi[pos])*C)

    return Arr_Quantile