def Find_Character_Modalities(Data):
    Arr_ai = []
    Ref_Data = Data.copy()
    Arr_ai.append(Ref_Data[0])
    stop = False
    while(not stop):
        for a in Arr_ai:
            if (Ref_Data.count(a) > 0):
                for n in range (0 , Ref_Data.count(a)):
                    Ref_Data.remove(a)
        if(len(Ref_Data) != 0):
            Arr_ai.append(Ref_Data[0])
        else:
            stop = True
    return Arr_ai

def Calc_fi(Data , Arr_Char_Mod):
    Arr_fi = []
    count = 0
    for a in Arr_Char_Mod:
        for b in Data:
            if(a == b):
                count += 1
        Arr_fi.append(count)
        count = 0

    return Arr_fi

def Calc_Fi(Arr_fi):
    Arr_Fi = []
    Acumulate = 0
    for a in Arr_fi:
        Acumulate += a
        Arr_Fi.append(Acumulate)
    return Arr_Fi

def Calc_hi(Data , Arr_fi, Precision):
    Arr_hi = []
    n = len(Data)
    for a in Arr_fi:
        if(Precision != 0):
            Arr_hi.append(round(a/n , Precision))
        else:
            Arr_hi.append(round(a/n))
    return Arr_hi

def Calc_Hi(Arr_hi , Precision):
    Arr_Hi = []
    Acumulate = 0
    for a in Arr_hi:
        Acumulate += a
        if(Acumulate+0.1>=1):
            Acumulate=1
        if(Precision != 0):
            Arr_Hi.append(round(Acumulate , Precision))
        else:
            Arr_Hi.append(round(Acumulate))
    return Arr_Hi

def Calc_hi_percent(Arr_hi , Precision):
    Arr_hi_percent = []
    for a in Arr_hi:
        if(Precision != 0):
            Arr_hi_percent.append(round(a*100 , Precision))
        else:
            Arr_hi_percent.append(round(a*100))
    return Arr_hi_percent

def Calc_Hi_percent(Arr_Hi , Precision):
    Arr_Hi_percent = []
    for a in Arr_Hi:
        if(Precision != 0):
            Arr_Hi_percent.append(round(a*100 , Precision))
        else:
            Arr_Hi_percent.append(round(a*100))
    return Arr_Hi_percent
