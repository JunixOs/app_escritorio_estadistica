from math import *
def Calc_Decimals_Number(Number):
    Temp = str(Number)
    Count = 0
    for a in range(len(Temp)-1,0,-1):
        if(Temp[a] == "."):
            return Count
        else:
            Count = Count + 1

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
    Arr_Groups = []
    for a in range (0 , m):
        if(a==m-1):
            Arr_Groups.append(Intervals[a][1])
        else:
            if(Precision==0):
                Arr_Groups.append(Intervals[a][1] - 1)
            else:
                Arr_Groups.append(round(Intervals[a][1] - 1*pow(10,-1*Precision) , Precision))

    return Arr_Groups

def Calc_xi(Intervals , m , Precision):
    Arr_xi = []
    for a in range (0 , m):
        if(Precision == 0):
            Arr_xi.append(round((Intervals[a][1]+Intervals[a][0])/2))
        else:
            Arr_xi.append(round((Intervals[a][1]+Intervals[a][0])/2 , Precision))

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
    Arr_Fi = []
    Acumulate = 0
    for a in fi:
        Acumulate += a
        Arr_Fi.append(Acumulate)
    return Arr_Fi

def Calc_hi(Data , fi , Precision):
    Arr_hi = []
    N = len(Data)
    for a in fi:
        if(Precision != 0):
            Arr_hi.append(round(a/N , Precision))
        else:
            Arr_hi.append(round(a/N))
    return Arr_hi

def Calc_Hi(hi , Precision):
    Arr_Hi = []
    Acumulate = 0
    for a in hi:
        Acumulate += a
        if(Acumulate+0.0001>=1):
            Acumulate=1
        if(Precision != 0):
            Arr_Hi.append(round(Acumulate , Precision))
        else:
            Arr_Hi.append(round(Acumulate))
    return Arr_Hi

def Calc_hi_percent(hi , Precision):
    Arr_hi_percent = []
    for a in hi:
        if(Precision !=0):
            Arr_hi_percent.append(round(a*100 , Precision))
        else:
            Arr_hi_percent.append(round(a*100))
            
    return Arr_hi_percent

def Calc_Hi_percent(Hi , Precision):
    Arr_Hi_percent = []
    for a in Hi:
        if(Precision != 0 ):
            Arr_Hi_percent.append(round(a*100 , Precision))
        else:
            Arr_Hi_percent.append(round(a*100))
    return Arr_Hi_percent