def Find_Stadistic_Variable_xi(Data):
    Arr_xi = []
    Arr_xi.append(Data[0])
    stop = False
    while(not stop):
        for a in Arr_xi:
            if (Data.count(a) > 0):
                for n in range (0 , Data.count(a)):
                    Data.remove(a)
        if(len(Data) != 0):
            Arr_xi.append(Data[0])
        else:
            stop = True
    return Arr_xi

def calc_fi():
    pass
def calc_Fi():
    pass
def Cals_hi():
    pass
def Calc_Hi():
    pass
def Calc_hi_percent():
    pass
def Calc_Hi_percent():
    pass