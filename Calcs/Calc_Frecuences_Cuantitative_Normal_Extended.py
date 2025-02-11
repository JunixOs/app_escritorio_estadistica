def Find_Stadistic_Variable_xi(Data):
    Arr_xi = []
    Ref_Data = Data.copy()
    
    while Ref_Data:
        element = Ref_Data[0]
        count = Ref_Data.count(element)
        
        if count > 0:
            Arr_xi.append(element)
            Ref_Data = [x for x in Ref_Data if x != element]
    Arr_xi.sort()
    return Arr_xi

def calc_fi(Data , Arr_xi):
    Arr_fi = []
    count = 0
    for a in Arr_xi:
        for b in Data:
            if (a == b):
                count += 1
        Arr_fi.append(count)
        count = 0
    return Arr_fi

def calc_Fi(Arr_fi):
    Arr_Fi = []
    Acumulate = 0
    for a in Arr_fi:
        Acumulate += a
        Arr_Fi.append(Acumulate)
    return Arr_Fi

def Calc_hi(Data , Arr_fi , Precision):
    n = len(Data)
    Arr_hi = []
    for a in Arr_fi:
        if (Precision != 0):
            Arr_hi.append(round(a/n , Precision))
        else:
            Arr_hi.append(round(a/n))
    return Arr_hi

def Calc_Hi(Arr_hi , Precision):
    Arr_Hi = []
    Acumulate = 0
    for a in Arr_hi:
        Acumulate += a
        if(Acumulate+0.0001 >=1):
            Acumulate=1
        if (Precision != 0):
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
        if(Precision !=0):
            Arr_Hi_percent.append(round(a*100 , Precision))
        else:
            Arr_Hi_percent.append(round(a*100))
    return Arr_Hi_percent