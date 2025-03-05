import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from math import *
import Calc_Frecuences_Cuantitative_Many_Values as Cuant_Many_Values
import Calc_Frecuences_Cualitative_Normal_Extended as Cuali_Normal_Extended
import Calc_Frecuences_Cuantitative_Normal_Extended as Cuant_Normal_Extended
import Summary_Measures.Calc_For_Not_Agrupped_Data as SM_For_Not_Grouped_Data
import Summary_Measures.Calc_For_Agrupped_Data as SM_For_Grouped_Data
import Quantiles.Quantil as Quantile

def Check_Contains_Only_Numbers(Data):
    return not any(caracter.isalpha() for caracter in Data)

def Convert_Input_Str_To_List(a):
    """
        ==============================================================================================
        Esta funcion sirve para separar los datos si es que se da el caso de que el usuario introduce
        los datos manualmente. Aqui se recibe una cadena de texto, que luego se transformara en una
        lista con cada uno de los valores.
        Esta pensado para trabajar con datos separados por espacios en blanco o saltos de linea.
        ==============================================================================================
    """
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
    """
        ==============================================================================================
        Esta funcion tiene el proposito de convertir los datos cuantitativos de valores str a int
        o float. Permite convertir los datos de la lista de strings resultante de la funcion 
        "Convert_Input_Str_To_List" a numeros, con los cuales se pueden realizar operaciones matematicas.
        Ademas, esta funcion comprueba si existen valores decimales dentro de los datos ingresados.
        ==============================================================================================
    """
    Data_Converted = Data

    if(len(Data_Converted)<2):
        raise ValueError("Se ingresaron muy pocos datos")
    
    Is_Float = False
    for n in range(0,len(Data_Converted)):
        Bool = "." in Data_Converted[n]        
        match Bool:
            case True:
                Is_Float = True
                Data_Converted[n] = float(Data_Converted[n])
            case False:
                Data_Converted[n] = int(Data_Converted[n])
    return Data_Converted , Is_Float

def Calculate_Results_Cuantitative_For_Grouped_Data(Data , There_Are_Floats , m):
    """ 
        ==============================================================================================
        Aqui se calculan los valores que iran dentro de la tabla de frecuencia para datos 
        cuantitativos agrupados, los quantiles para datos agrupados (quartiles, deciles y percentiles) 
        y algunas variables mas.
        ==============================================================================================
    """
    V_Min = Cuant_Many_Values.Calc_Min(Data)
    V_Max = Cuant_Many_Values.Calc_Max(Data)

    n = len(Data)
    R = Cuant_Many_Values.Calc_Range(V_Min,V_Max)

    if(not There_Are_Floats):
        """ 
            **********************************************************************************
            Si no existe ningun valor decimal entre todos los datos, entonces la amplitud se
            redondea con un maximo de 1 decimal.
            **********************************************************************************
        """
        C = round(R/m , 1)
        C_N_Decimals = 1
        Arr_Intervals = Cuant_Many_Values.Calc_Intervals(V_Min , C , V_Max , m , C_N_Decimals)
        Arr_Groups = Cuant_Many_Values.Calc_Groups_For_Integer_Numbers(Arr_Intervals , m , C_N_Decimals)
    else:
        """ 
            **********************************************************************************
            Si por el contrario, existe algun valor decimal entre todos los datos, entonces 
            la amplitud se redondea a la cantidad de decimales mas comun entre todos los 
            datos.
            **********************************************************************************
        """
        N_Decimals_Most_Common = Cuant_Many_Values.Calc_Max_Decimal_Number(Data)
        C_N_Decimals = int(N_Decimals_Most_Common[0][0])
        C = round(R/m , C_N_Decimals)

        Arr_Intervals = Cuant_Many_Values.Calc_Intervals(V_Min , C , V_Max , m , C_N_Decimals)
        Arr_Groups = Cuant_Many_Values.Calc_Groups_For_Decimal_Numbers(Arr_Intervals , m , C_N_Decimals)

    Arr_xi = Cuant_Many_Values.Calc_xi(Arr_Intervals , m)

    Arr_fi = Cuant_Many_Values.Calc_fi(Data , Arr_Intervals , m)
    Arr_Fi = Cuant_Many_Values.Calc_Fi(Arr_fi)

    Arr_hi = Cuant_Many_Values.Calc_hi(Data , Arr_fi)
    Arr_Hi = Cuant_Many_Values.Calc_Hi(Arr_hi)

    Arr_hi_percent = Cuant_Many_Values.Calc_hi_percent(Arr_hi)
    Arr_Hi_percent = Cuant_Many_Values.Calc_Hi_percent(Arr_Hi)
    
    X_ = SM_For_Grouped_Data.Calc_Arithmetic_Average(len(Data) , Arr_xi , Arr_fi)
    Me = SM_For_Grouped_Data.Calc_Median_Me(len(Data) , Arr_fi , Arr_Fi , Arr_Intervals , C)
    Mo = SM_For_Grouped_Data.Calc_Mode_Mo(Arr_fi , Arr_Intervals , C)
    X_h = SM_For_Grouped_Data.Calc_Armonic_Average(len(Data) , Arr_xi , Arr_fi)
    X_g = SM_For_Grouped_Data.Calc_Geometric_Average(len(Data) , Arr_xi , Arr_fi)

    S_2 = SM_For_Grouped_Data.Calc_Variance(len(Data) , Arr_xi , Arr_fi , X_)
    S = SM_For_Grouped_Data.Calc_Standard_Deviation(S_2)
    CV_Percent = SM_For_Grouped_Data.Calc_Percentage_Coefficient_Variation(S , X_)

    Arr_Quartile = Quantile.Calc_Quantile_For_Grouped_Data(4 , Data , Arr_Intervals , Arr_fi , Arr_Fi , C)
    Arr_Decile = Quantile.Calc_Quantile_For_Grouped_Data(10 , Data , Arr_Intervals , Arr_fi , Arr_Fi , C)
    Arr_Percentile = Quantile.Calc_Quantile_For_Grouped_Data(100 , Data , Arr_Intervals , Arr_fi , Arr_Fi , C)

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

    Quantiles = dict([
        ("Cuartil" , Arr_Quartile),
        ("Decil" , Arr_Decile),
        ("Percentil" , Arr_Percentile),
    ])

    Variables_Value = dict([
        ("Data_List" , Data),
        ("V_Max" , V_Max),
        ("V_Min" , V_Min),
        ("n" , n),
        ("R" , R),
        ("m" , m),
        ("C" , C),
        ("Is_Float" , There_Are_Floats),
        ("C_Decimals_Number" , C_N_Decimals),
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

    return Variables_Value , Frecuences_Value , Summary_Measures , Quantiles

def Calculate_Results_Cuantitative_For_Not_Grouped_Data(Data):
    """ 
        ==============================================================================================
        Aqui se calculan los valores que iran dentro de la tabla de frecuencia para datos 
        cuantitativos no agrupados, los quantiles para datos no agrupados 
        (quartiles, deciles y percentiles) y algunas variables mas.
        ==============================================================================================
    """
    n = len(Data)

    Arr_xi , Arr_fi = Cuant_Normal_Extended.Calc_fi_And_xi(Data)
    N_Stadistic_Variables = len(Arr_xi)

    Arr_Fi = Cuant_Normal_Extended.calc_Fi(Arr_fi)

    Arr_hi = Cuant_Normal_Extended.Calc_hi(Data , Arr_fi)
    Arr_Hi = Cuant_Normal_Extended.Calc_Hi(Arr_hi)

    Arr_hi_percent = Cuant_Normal_Extended.Calc_hi_percent(Arr_hi)
    Arr_Hi_percent = Cuant_Normal_Extended.Calc_Hi_percent(Arr_Hi)

    X_ = SM_For_Not_Grouped_Data.Calc_Arithmetic_Average(Data)
    Me = SM_For_Not_Grouped_Data.Calc_Median_Me(Data)
    Mo = SM_For_Not_Grouped_Data.Calc_Mode_Mo(Arr_xi , Arr_fi)
    X_h = SM_For_Not_Grouped_Data.Calc_Armonic_Average(Data)
    X_g = SM_For_Not_Grouped_Data.Calc_Geometric_Average(Data)

    S_2 = SM_For_Not_Grouped_Data.Calc_Variance(X_ , Data)
    S = SM_For_Not_Grouped_Data.Calc_Standard_Deviation(S_2)
    CV_Percent = SM_For_Not_Grouped_Data.Calc_Percentage_Coefficient_Variation(S , X_)

    Arr_Quartile = Quantile.Calc_Quantile_For_Not_Grouped_Data(4 , Data)
    Arr_Decile = Quantile.Calc_Quantile_For_Not_Grouped_Data(10 , Data)
    Arr_Percentile = Quantile.Calc_Quantile_For_Not_Grouped_Data(100 , Data)

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

    Quantiles = dict([
        ("Cuartil" , Arr_Quartile),
        ("Decil" , Arr_Decile),
        ("Percentil" , Arr_Percentile),
    ])

    Variables_Values = dict([
        ("Data_List" , Data),
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
    return Variables_Values , Frecuences_Values , Summary_Measures , Quantiles

def Calculate_Results_Cualitative_Data(Data):
    """ 
        ==============================================================================================
        Aqui se calculan los valores que iran dentro de la tabla de frecuencia para datos cualitativos, 
        y algunas variables mas.
        ==============================================================================================
    """
    n = len(Data)

    Arr_Char_Mod , Arr_fi = Cuali_Normal_Extended.Calc_fi_And_ai(Data)
    Number_Char_Mod = len(Arr_Char_Mod)

    Arr_Fi = Cuali_Normal_Extended.Calc_Fi(Arr_fi)

    Arr_hi = Cuali_Normal_Extended.Calc_hi(Data , Arr_fi)
    Arr_Hi = Cuali_Normal_Extended.Calc_Hi(Arr_hi)

    Arr_hi_percent = Cuali_Normal_Extended.Calc_hi_percent(Arr_hi)
    Arr_Hi_percent = Cuali_Normal_Extended.Calc_Hi_percent(Arr_Hi)

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

def Main_Function(In):
    """  
        ==============================================================================================
        Aqui se determina si los datos ingresados son cualitativos o cuantitativos, y se realizan los
        calculos necesarios segun el tipo de variable.
        ==============================================================================================
    """
    Variables_Cuant_For_Many_Values = None
    Frecuences_Cuant_For_Many_Values = None
    Summary_Measures_For_Grouped_Data = None
    Quantiles_For_Grouped_Data = None

    Variables_Cuant_Normal_Extended = None
    Frecuences_Cuant_Normal_Extended = None
    Summary_Measures_For_Not_Grouped_Data = None
    Quantiles_For_Not_Grouped_Data = None

    Variables_Cuali_Normal_Extended = None
    Frecuences_Cuali_Normal_Extended = None
    if(not In):
        raise ValueError("No se ingresaron datos")
    else:
        if(not isinstance(In , list)):
            In = In.replace("\n" , " ").replace(" nan "," ").replace("nan "," ").replace(" nan"," ").replace(" NAN "," ").replace(" NAN"," ").replace("NAN "," ")
            Data = Convert_Input_Str_To_List(In)
            Is_Cuantitative = Check_Contains_Only_Numbers(In)
        else:
            Data = In
            Is_Cuantitative = True
            for value in Data:
                if(isinstance(value , str)):
                    Is_Cuantitative = False
                    break

        match(Is_Cuantitative):
            case True:
                if(not isinstance(In , list)):
                    Data , Is_Float = Conv_Data_To_Numbers(Data)
                else:
                    Is_Float = False
                    for a in Data:
                        if(int(a) != a):
                            Is_Float = True
                            break

                n = len(Data)
                m = round(1 + 3.322*log10(n))
                if(m<5):
                    Calc_For_Classes = False
                else:
                    Calc_For_Classes = True
                
                match(Calc_For_Classes):
                    case True:
                        Variables_Cuant_For_Many_Values , Frecuences_Cuant_For_Many_Values , Summary_Measures_For_Grouped_Data , Quantiles_For_Grouped_Data = Calculate_Results_Cuantitative_For_Grouped_Data(Data , Is_Float , m)
                    case False:
                        if(Is_Float):
                            Variables_Cuant_For_Many_Values , Frecuences_Cuant_For_Many_Values , Summary_Measures_For_Grouped_Data , Quantiles_For_Grouped_Data = Calculate_Results_Cuantitative_For_Grouped_Data(Data , Is_Float , m)
                        else:
                            Variables_Cuant_Normal_Extended , Frecuences_Cuant_Normal_Extended , Summary_Measures_For_Not_Grouped_Data , Quantiles_For_Not_Grouped_Data = Calculate_Results_Cuantitative_For_Not_Grouped_Data(Data)

            case False:
                Variables_Cuali_Normal_Extended , Frecuences_Cuali_Normal_Extended = Calculate_Results_Cualitative_Data(Data)
            case _:
                raise Exception("Hubo un error al identificar el tipo de variable de los datos ingresados.")

    Dictionary_Results = dict([
        ("Variables_Cuant_For_Many_Values" , Variables_Cuant_For_Many_Values),
        ("Frecuences_Cuant_For_Many_Values" , Frecuences_Cuant_For_Many_Values),
        ("Summary_Measures_For_Grouped_Data" , Summary_Measures_For_Grouped_Data),
        ("Quantiles_For_Grouped_Data" , Quantiles_For_Grouped_Data),
        ("Variables_Cuant_Normal_Extended" , Variables_Cuant_Normal_Extended),
        ("Frecuences_Cuant_Normal_Extended" , Frecuences_Cuant_Normal_Extended),
        ("Summary_Measures_For_Not_Grouped_Data" , Summary_Measures_For_Not_Grouped_Data),
        ("Quantiles_For_Not_Grouped_Data" , Quantiles_For_Not_Grouped_Data),
        ("Variables_Cuali_Normal_Extended" , Variables_Cuali_Normal_Extended),
        ("Frecuences_Cuali_Normal_Extended" , Frecuences_Cuali_Normal_Extended),
    ])
    return Dictionary_Results

if (__name__ == "__main__"):
    Data = "Casa Casa Trabajo Trabajo Trabajo Casa Casa Cibercafe Otros Cibercafe Trabajo Trabajo Otros Cibercafe Cibercafe Cibercafe Casa Cibercafe Otros Cibercafe Casa Casa Cibercafe Trabajo Otros Otros Cibercafe Cibercafe Cibercafe Cibercafe "
    Data_2 = "118 484 664 1004 1231 1372 1582 118 484 664 1004 1231 1372 1582 118 484 664 1004 1231 1372 1582 118 484 664 1004 1231 1372 1582 118 484 664 1004 1231 1372 1582  "
    Results = Main_Function(Data_2)
    for key, value in Results.items():
        print(f"{key} : {value}")
        if(value != None):
            for k , v in value.items():
                print(f"{k} : {v}")
        else:
            print(f"{key} : None")
    """ 
        Error en la funcion  Cuant_Normal_Extended.Find_Stadistic_Variable_xi, las listas de modificaban y quedaban vacias al terminar su ejecucion, perjudicando el resto de calculos
        Solucion, usar el metodo copy() para crear una copia del objeto. No usar otras variables, colo copy()
    """
    
    """ 
        Objetos mutables (como listas, diccionarios, conjuntos, etc.) se pasan por referencia. Si modificas el objeto dentro de la función, los cambios se reflejarán fuera de la función.
        Objetos inmutables (como enteros, cadenas de texto, tuplas, etc.) se pasan por valor. Esto significa que si modificas el valor dentro de la función, no afectará la variable original fuera de la función.
    """
