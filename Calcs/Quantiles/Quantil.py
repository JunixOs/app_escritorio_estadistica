import math
def Calc_Quantile_For_Grouped_Data(N_Quantile , Data , Intervals , Arr_fi , Arr_Fi , C):
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

def Calc_Quantile_For_Not_Grouped_Data(N_Quantile , Data):
    if((N_Quantile == 4 and len(Data) < 5) or ((N_Quantile == 10 or N_Quantile == 100) and len(Data) < 10)):
        return []

    Arr_Quantile = []
    n = len(Data)
    for k in range(1 , N_Quantile):
        Q_k = k*(n+1)/N_Quantile
        if(isinstance(Q_k , float)):
            Pos_E1 = Data[math.floor(Q_k)]
            if(round(Q_k) == Pos_E1):
                Pos_E2 = round(Q_k + 1)
            else:
                Pos_E2 = round(Q_k)
            
            e = Q_k - math.floor(Q_k)
            Q_k = Data[Pos_E1] + (Data[Pos_E2] - Data[Pos_E1]) * e

        Arr_Quantile.append(Data[Q_k - 1])

    return Arr_Quantile