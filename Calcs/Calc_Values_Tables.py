import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from math import *
import Calc_Frecuences_Cuantitative_Many_Values as Cuant_Many_Values
import Calc_Frecuences_Cualitative_Normal_Extended as Cuali_Normal_Extended
import Calc_Frecuences_Cuantitative_Normal_Extended as Cuant_Normal_Extended
import Summary_Measures.Calc_For_Not_Agrupped_Data as SM_For_Not_Grouped_Data
import Summary_Measures.Calc_For_Agrupped_Data as SM_For_Grouped_Data

def Contains_Letters(Data):
    return not any(caracter.isalpha() for caracter in Data)

def Separate_Data(a):
    Value = ""
    Data = []
    for n in range(0,len(a)):
        char = a[n]
        if(char == " " or n==len(a)-1 or char=="\n"):
            """ Primero se comprueba que no haya un salto en blanco o un salto de linea o si la cadena esta a punto de terminar"""
            if(n==len(a)-1 and char!=" "):
                """ Si la cadena esta por terminar, se añade el ultimo caracter para no quedar incompleta"""
                Value+=char

            if(Value==""):
                """ Si el valor que estamos armando no tiene nada, pasa a la siguiente iteracion """
                continue

            else:
                """ Si hay algo entonces se añade a todos los datos y se devuelve a su valor inicial """
                Data.append(Value)
                Value = ""

        else:
            Value += char

    return Data

def Conv_Data_To_Numbers(Data):
    Data_Converted = Data

    if(len(Data_Converted)<2):
        raise ValueError("Se ingresaron muy pocos datos")

    for n in range(0,len(Data_Converted)):
        Bool = "." in Data_Converted[n]        
        match Bool:
            case True:
                Data_Converted[n] = float(Data_Converted[n])
            case False:
                Data_Converted[n] = int(Data_Converted[n])
    return Data_Converted

def Calculate_Table_Cuantitative_For_Many_Values(N_Decimals_Precision , Data):
    V_Min = Cuant_Many_Values.Calc_Min(Data)
    V_Max = Cuant_Many_Values.Calc_Max(Data)

    n = len(Data)
    R = round(Cuant_Many_Values.Calc_Range(V_Min,V_Max) , 3)
    m = round(1+(3.3*log10(n)))

    There_Are_Floats = False
    for a in Data:
        if(int(a) != a):
            There_Are_Floats = True
            break

    if(not There_Are_Floats):
        C = round(R/m , 1)
        Arr_Intervals = Cuant_Many_Values.Calc_Intervals(V_Min , C , V_Max , m , 1)
        Arr_Groups = Cuant_Many_Values.Calc_Groups(Arr_Intervals , m , 1)
    else:
        C = round(R/m , 3)
        C_N_Decimals = Cuant_Many_Values.Calc_Decimals_Number(C) # N de decimales de la amplitud (C)
        if(C - round(C)==0):
            C = round(C)
            C_N_Decimals = 0
        elif(C_N_Decimals>=1 and C_N_Decimals<=3):
            C = round(C , C_N_Decimals)
        elif(C_N_Decimals>3):
            C = round(C , 3)
            C_N_Decimals = 3
        Arr_Intervals = Cuant_Many_Values.Calc_Intervals(V_Min , C , V_Max , m , C_N_Decimals)
        Arr_Groups = Cuant_Many_Values.Calc_Groups(Arr_Intervals , m , C_N_Decimals)

    Arr_xi = Cuant_Many_Values.Calc_xi(Arr_Intervals , m , N_Decimals_Precision)

    Arr_fi = Cuant_Many_Values.Calc_fi(Data , Arr_Intervals , m)
    Arr_Fi = Cuant_Many_Values.Calc_Fi(Arr_fi)

    Arr_hi = Cuant_Many_Values.Calc_hi(Data , Arr_fi , N_Decimals_Precision)
    Arr_Hi = Cuant_Many_Values.Calc_Hi(Arr_hi , N_Decimals_Precision)

    Arr_hi_percent = Cuant_Many_Values.Calc_hi_percent(Arr_hi , N_Decimals_Precision)
    Arr_Hi_percent = Cuant_Many_Values.Calc_Hi_percent(Arr_Hi , N_Decimals_Precision)

    """ Modificar esto para mas precision en los siguientes calculos """
    if(N_Decimals_Precision>=3 and N_Decimals_Precision<5):
        Precision = 2
    elif(N_Decimals_Precision>=5 and N_Decimals_Precision<7):
        Precision = 4
    elif(N_Decimals_Precision>=7 and N_Decimals_Precision<=8):
        Precision = 6
    
    X_ = SM_For_Grouped_Data.Calc_Arithmetic_Average(len(Data) , Arr_xi , Arr_fi , Precision)
    Me = SM_For_Grouped_Data.Calc_Median_Me(len(Data) , Arr_fi , Arr_Fi , Arr_Intervals , C , Precision)
    Mo = SM_For_Grouped_Data.Calc_Mode_Mo(Arr_fi , Arr_Intervals , C , Precision)
    X_h = SM_For_Grouped_Data.Calc_Armonic_Average(len(Data) , Arr_xi , Arr_fi , Precision)
    X_g = SM_For_Grouped_Data.Calc_Geometric_Average(len(Data) , Arr_xi , Arr_fi , Precision)

    S_2 = SM_For_Grouped_Data.Calc_Variance(len(Data) , Arr_xi , Arr_fi , X_ , Precision)
    S = SM_For_Grouped_Data.Calc_Standard_Deviation(S_2 , Precision)
    CV_Percent = SM_For_Grouped_Data.Calc_Percentage_Coefficient_Variation(S , X_ , Precision)

    Summary_Measures = dict([
    ("Media Aritmetica (X)" , X_),
    ("Media Geometrica (X_g)" , X_g),
    ("Media Armonica (X_h)" , X_h),
    ("Moda (Mo)" , Mo),
    ("Mediana (Me)" , Me),
    ("Varianza (S^2)" , S_2),
    ("Desviacion Estandar (S)" , S),
    ("CV%" , CV_Percent),
    ])
    Variables_Value = dict([
        ("V_Max" , V_Max),
        ("V_Min" , V_Min),
        ("n" , n),
        ("R" , R),
        ("m" , m),
        ("C" , C),
        ("Is_Float" , False),
    ])

    Frecuences_Value = dict(
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
    return Variables_Value , Frecuences_Value , Summary_Measures

def Calculate_Table_Cuantitative_Normal_Extended(N_Decimals_Precision , Data):
    n = len(Data)

    Arr_xi = Cuant_Normal_Extended.Find_Stadistic_Variable_xi(Data)
    N_Stadistic_Variables = len(Arr_xi)

    Arr_fi = Cuant_Normal_Extended.calc_fi(Data , Arr_xi)
    Arr_Fi = Cuant_Normal_Extended.calc_Fi(Arr_fi)

    Arr_hi = Cuant_Normal_Extended.Calc_hi(Data , Arr_fi , N_Decimals_Precision)
    Arr_Hi = Cuant_Normal_Extended.Calc_Hi(Arr_hi , N_Decimals_Precision)

    Arr_hi_percent = Cuant_Normal_Extended.Calc_hi_percent(Arr_hi , N_Decimals_Precision)
    Arr_Hi_percent = Cuant_Normal_Extended.Calc_Hi_percent(Arr_Hi , N_Decimals_Precision)

    if(N_Decimals_Precision>=3 and N_Decimals_Precision<5):
        Precision = 2
    elif(N_Decimals_Precision>=5 and N_Decimals_Precision<7):
        Precision = 4
    elif(N_Decimals_Precision>=7 and N_Decimals_Precision<=8):
        Precision = 6
    X_ = SM_For_Not_Grouped_Data.Calc_Arithmetic_Average(Data , Precision)
    Me = SM_For_Not_Grouped_Data.Calc_Median_Me(Data)
    Mo = SM_For_Not_Grouped_Data.Calc_Mode_Mo(Arr_xi , Arr_fi)
    X_h = SM_For_Not_Grouped_Data.Calc_Armonic_Average(Data , Precision)
    X_g = SM_For_Not_Grouped_Data.Calc_Geometric_Average(Data , Precision)

    S_2 = SM_For_Not_Grouped_Data.Calc_Variance(X_ , Data , Precision)
    S = SM_For_Not_Grouped_Data.Calc_Standard_Deviation(S_2 , Precision)
    CV_Percent = SM_For_Not_Grouped_Data.Calc_Percentage_Coefficient_Variation(S , X_ , Precision)

    Summary_Measures = dict([
        ("Media Aritmetica (X)" , X_),
        ("Media Geometrica (X_g)" , X_g),
        ("Media Armonica (X_h)" , X_h),
        ("Moda (Mo)" , Mo),
        ("Mediana (Me)" , Me),
        ("Varianza (S^2)" , S_2),
        ("Desviacion Estandar (S)" , S),
        ("CV%" , CV_Percent),
    ])
    Variables_Values = dict([
        ("n" ,n),
        ("Number_Statistic_Variables" , N_Stadistic_Variables),
    ])

    Frecuences_Values = dict(
        xi = Arr_xi,
        fi = Arr_fi,
        Fi = Arr_Fi,
        hi = Arr_hi,
        Hi = Arr_Hi,
        hi_percent = Arr_hi_percent,
        Hi_percent = Arr_Hi_percent,
    )
    return Variables_Values , Frecuences_Values , Summary_Measures

def Calculate_Table_Cualitative_Normal_Extended(N_Decimals_Precision , Data):
    n = len(Data)

    Arr_Char_Mod = Cuali_Normal_Extended.Find_Character_Modalities(Data)
    Number_Char_Mod = len(Arr_Char_Mod)

    Arr_fi = Cuali_Normal_Extended.Calc_fi(Data , Arr_Char_Mod)
    Arr_Fi = Cuali_Normal_Extended.Calc_Fi(Arr_fi)

    Arr_hi = Cuali_Normal_Extended.Calc_hi(Data , Arr_fi , N_Decimals_Precision)
    Arr_Hi = Cuali_Normal_Extended.Calc_Hi(Arr_hi , N_Decimals_Precision)

    Arr_hi_percent = Cuali_Normal_Extended.Calc_hi_percent(Arr_hi , N_Decimals_Precision)
    Arr_Hi_percent = Cuali_Normal_Extended.Calc_Hi_percent(Arr_Hi , N_Decimals_Precision)

    Variables_Values = dict([
        ("n" , n),
        ("N_Character_Modalities" , Number_Char_Mod),
    ])

    Frecuences_Values = dict(
        ai = Arr_Char_Mod,
        fi = Arr_fi,
        Fi = Arr_Fi,
        hi = Arr_hi,
        Hi = Arr_Hi,
        hi_percent = Arr_hi_percent,
        Hi_percent = Arr_Hi_percent,
    )

    return Variables_Values , Frecuences_Values

def Main_Function(N_Decimals_Precision , In):
    Variables_Cuant_For_Many_Values = None
    Frecuences_Cuant_For_Many_Values = None
    Summary_Measures_For_Grouped_Data = None

    Variables_Cuant_Normal_Extended = None
    Frecuences_Cuant_Normal_Extended = None
    Summary_Measures_For_Not_Grouped_Data = None

    Variables_Cuali_Normal_Extended = None
    Frecuences_Cuali_Normal_Extended = None
    if(not In):
        raise ValueError("No se ingresaron datos")
    else:
        In = In.replace("\n" , "")
        Is_Cualitative = Contains_Letters(In)
        Data = Separate_Data(In)

        match(Is_Cualitative):
            case True:
                Data = Conv_Data_To_Numbers(Data)
                n = len(Data)
                m = round(1 + 3.222*log10(n))
                if(m<5):
                    Calc_For_Classes = False
                else:
                    Calc_For_Classes = True
                
                if(Calc_For_Classes):
                    Variables_Cuant_For_Many_Values , Frecuences_Cuant_For_Many_Values , Summary_Measures_For_Grouped_Data = Calculate_Table_Cuantitative_For_Many_Values(N_Decimals_Precision , Data)
                else:
                    Variables_Cuant_Normal_Extended , Frecuences_Cuant_Normal_Extended , Summary_Measures_For_Not_Grouped_Data = Calculate_Table_Cualitative_Normal_Extended(N_Decimals_Precision , Data)
            case False:
                Variables_Cuali_Normal_Extended , Frecuences_Cuali_Normal_Extended = Calculate_Table_Cualitative_Normal_Extended(N_Decimals_Precision , Data)

    Dictionary_Results = dict([
        ("Variables_Cuant_For_Many_Values" , Variables_Cuant_For_Many_Values),
        ("Frecuences_Cuant_For_Many_Values" , Frecuences_Cuant_For_Many_Values),
        ("Summary_Measures_For_Grouped_Data" , Summary_Measures_For_Grouped_Data),
        ("Variables_Cuant_Normal_Extended" , Variables_Cuant_Normal_Extended),
        ("Frecuences_Cuant_Normal_Extended" , Frecuences_Cuant_Normal_Extended),
        ("Summary_Measures_For_Not_Grouped_Data" , Summary_Measures_For_Not_Grouped_Data),
        ("Variables_Cuali_Normal_Extended" , Variables_Cuali_Normal_Extended),
        ("Frecuences_Cuali_Normal_Extended" , Frecuences_Cuali_Normal_Extended),
    ])
    return Dictionary_Results

if (__name__ == "__main__"):
    Data = "Casa Casa Trabajo Trabajo Trabajo Casa Casa Cibercafe Otros Cibercafe Trabajo Trabajo Otros Cibercafe Cibercafe Cibercafe Casa Cibercafe Otros Cibercafe Casa Casa Cibercafe Trabajo Otros Otros Cibercafe Cibercafe Cibercafe Cibercafe "
    Data_2 = "118 484 664 1004 1231 1372 1582 118 484 664 1004 1231 1372 1582 118 484 664 1004 1231 1372 1582 118 484 664 1004 1231 1372 1582 118 484 664 1004 1231 1372 1582  "
    Results = Main_Function(4 , Data_2)
    print(Results)
    """ 
        Error en la funcion  Cuant_Normal_Extended.Find_Stadistic_Variable_xi, las listas de modificaban y quedaban vacias al terminar su ejecucion, perjudicando el resto de calculos
        Solucion, usar el metodo copy() para crear una copia del objeto. No usar otras variables, colo copy()
    """
    
    """ 
        Objetos mutables (como listas, diccionarios, conjuntos, etc.) se pasan por referencia. Si modificas el objeto dentro de la función, los cambios se reflejarán fuera de la función.
        Objetos inmutables (como enteros, cadenas de texto, tuplas, etc.) se pasan por valor. Esto significa que si modificas el valor dentro de la función, no afectará la variable original fuera de la función.
    """
