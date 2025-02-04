from math import *

def Separate_Data(a):
    number = ""
    Data = []
    for n in range(0,len(a)):
        char = a[n]
        if(char == " " or n==len(a)-1 or char=="\n"):
            if(n==len(a)-1 and char!=" "):
                number+=char

            if(number==""):
                continue

            else:
                Data.append(number)
                number = ""

        else:
            number += char

    return Data

def Conv_Data(Data):
    Data_Converted = Data

    if(len(Data_Converted)<2):
        raise ValueError

    for n in range(0,len(Data)):
        Bool = "." in Data_Converted[n]
        match Bool:
            case True:
                Data_Converted[n] = float(Data_Converted[n])
            case False:
                Data_Converted[n] = int(Data_Converted[n])
        if (Data_Converted[n]<0):
            raise ValueError("Datos no procesados correctamente")
    return Data_Converted

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
        if(Acumulate+0.1>=1):
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

def Print_Table_On_Window(m , Intervals , Arr_xi , Arr_fi , Arr_Fi , Arr_hi , Arr_Hi , Arr_hi_precent , Arr_Hi_percent):
    print("   m    |     Li     |     Ls     |     xi    |     fi     |     Fi     |     hi     |     Hi     |     hi%     |     Hi%     ")
    for a in range(m):
        print("------------------------------------------------------------------------------------------------------------------------------")
        print(f"  {a}    ")
        print("------------------------------------------------------------------------------------------------------------------------------")
    
def Main_Function(N_Decimals_Precision , In):
    if(__name__ == "__main__"):
        """ In = input("Ingrese los valores separados por espacios, si son decimales evitar usar comas \",\", usar punto \".\": \n") """
        In = """118
                484
                664
                1004
                1231
                1372
                1582
                118
                484
                664
                1004
                1231
                1372
                1582
                118
                484
                664
                1004
                1231
                1372
                1582
                118
                484
                664
                1004
                1231
                1372
                1582
                118
                484
                664
                1004
                1231
                1372
                1582"""

    Data = Separate_Data(In)
    Data = Conv_Data(Data)

    if(not Data):
        raise ValueError("Datos no procesados correctamente")
    else:

        V_Min = Calc_Min(Data)
        V_Max = Calc_Max(Data)

        n = len(Data)
        R = round(Calc_Range(V_Min,V_Max) , 3)
        m = round(1+(3.3*log10(n)))
        C = R/m

        C_N_Decimals = Calc_Decimals_Number(C) # N de decimales de la amplitud (C)
        if(C - round(C)==0):
            C = round(C)
            C_N_Decimals = 0
        elif(C_N_Decimals>=1 and C_N_Decimals<=3):
            C = round(C , C_N_Decimals)
        elif(C_N_Decimals>3):
            C = round(C , 3)
            C_N_Decimals = 3

        
        Arr_Intervals = Calc_Intervals(V_Min , C , V_Max , m , C_N_Decimals)
        Arr_Groups = Calc_Groups(Arr_Intervals , m , C_N_Decimals)

        Arr_xi = Calc_xi(Arr_Intervals , m , N_Decimals_Precision)

        Arr_fi = Calc_fi(Data , Arr_Intervals , m)
        Arr_Fi = Calc_Fi(Arr_fi)

        Arr_hi = Calc_hi(Data , Arr_fi , N_Decimals_Precision)
        Arr_Hi = Calc_Hi(Arr_hi , N_Decimals_Precision)

        Arr_hi_percent = Calc_hi_percent(Arr_hi , N_Decimals_Precision)
        Arr_Hi_percent = Calc_Hi_percent(Arr_Hi , N_Decimals_Precision)

        if(__name__ == "__main__"):
            print(f"Datos Ingresados: \n")
            for a in Data:
                print(f"{a} ")
            print(f"Intervalos: {Arr_Intervals}")
            print(f"Grupos: {Arr_Groups}")
            print(f"xi: {Arr_xi}")
            print(f"fi: {Arr_fi}")
            print(f"Fi: {Arr_Fi}")
            print(f"hi: {Arr_hi}")
            print(f"Hi: {Arr_Hi}")

            print(f"hi%: {Arr_hi_percent}")
            print(f"Hi%: {Arr_Hi_percent}")

            """ d3 = dict(Nombre='Sara',
                Edad=27,
                Documento=1003882) """
        else:
            Variables_Value = dict([
                ("V_Max" , V_Max),
                ("V_Min" , V_Min),
                ("n" , n),
                ("R" , R),
                ("m" , m),
                ("C" , C),
            ])

            Frecuences = dict(
                Data_Values = Data,
                Intervals = Arr_Intervals,
                Groups = Arr_Groups,
                xi = Arr_xi,
                fi = Arr_fi,
                Fi = Arr_Fi,
                hi = Arr_hi,
                Hi = Arr_Hi,
                hi_percent = Arr_hi_percent,
                Hi_percent = Arr_Hi_percent,
            )

            # print(Frecuences["Intervals"][0][0])    <--- Ingreso a Intervalos y busco el primer valor del primer intervalo
            return Variables_Value , Frecuences

if (__name__ == "__main__"):
    N_Decimals = int(input("Ingrese la cantidad de decimales (precision): "))
    Main_Function(N_Decimals , 0)