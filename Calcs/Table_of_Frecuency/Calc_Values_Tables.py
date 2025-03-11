import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from math import *
import Calcs.Table_of_Frecuency.Frecuences.Calc_Frecuences_Cuantitative_Grouped as Cuant_Grouped
import Calcs.Table_of_Frecuency.Frecuences.Calc_Frecuences_Cualitative as Cuali
import Calcs.Table_of_Frecuency.Frecuences.Calc_Frecuences_Cuantitative_Not_Grouped as Cuant_Not_Grouped
import Calcs.Table_of_Frecuency.Summary_Measures.Calc_For_Not_Grouped_Data as SM_For_Not_Grouped_Data
import Calcs.Table_of_Frecuency.Summary_Measures.Calc_For_Grouped_Data as SM_For_Grouped_Data
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
    V_Min = Cuant_Grouped.Calc_Min(Data)
    V_Max = Cuant_Grouped.Calc_Max(Data)

    n = len(Data)
    R = Cuant_Grouped.Calc_Range(V_Min,V_Max)

    if(not There_Are_Floats):
        """ 
            **********************************************************************************
            Si no existe ningun valor decimal entre todos los datos, entonces la amplitud se
            redondea con un maximo de 1 decimal.
            **********************************************************************************
        """
        C = round(R/m , 1)
        C_N_Decimals = 1
        Arr_Intervals = Cuant_Grouped.Calc_Intervals(V_Min , C , V_Max , m , C_N_Decimals)
        Arr_Groups = Cuant_Grouped.Calc_Groups_For_Integer_Numbers(Arr_Intervals , m , C_N_Decimals)
    else:
        """ 
            **********************************************************************************
            Si por el contrario, existe algun valor decimal entre todos los datos, entonces 
            la amplitud se redondea a la cantidad de decimales mas comun entre todos los 
            datos.
            **********************************************************************************
        """
        N_Decimals_Most_Common = Cuant_Grouped.Calc_Max_Decimal_Number(Data)
        C_N_Decimals = int(N_Decimals_Most_Common[0][0]) + 1
        C = round(R/m , C_N_Decimals)

        Arr_Intervals = Cuant_Grouped.Calc_Intervals(V_Min , C , V_Max , m , C_N_Decimals)
        Arr_Groups = Cuant_Grouped.Calc_Groups_For_Decimal_Numbers(Arr_Intervals , m , C_N_Decimals)

    Arr_xi = Cuant_Grouped.Calc_xi(Arr_Intervals , m)

    Arr_fi = Cuant_Grouped.Calc_fi(Data , Arr_Intervals , m)
    Arr_Fi = Cuant_Grouped.Calc_Fi(Arr_fi)

    Arr_hi = Cuant_Grouped.Calc_hi(Data , Arr_fi)
    Arr_Hi = Cuant_Grouped.Calc_Hi(Arr_hi)

    Arr_hi_percent = Cuant_Grouped.Calc_hi_percent(Arr_hi)
    Arr_Hi_percent = Cuant_Grouped.Calc_Hi_percent(Arr_Hi)
    
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

    Coef_Pearson = SM_For_Grouped_Data.Calc_Pearson_Coefficient(X_ , Me , S)
    Coef_Fisher = SM_For_Grouped_Data.Calc_Fisher_Coefficient(Arr_xi , X_ , Arr_fi , n , S)
    Coef_Kurtosis = SM_For_Grouped_Data.Calc_Kurtosis_Coefficient(Arr_Percentile , Arr_xi , X_ , Arr_fi , n , S)

    Summary_Measures = {
        "Measures_Of_Central_Tendency_And_Dispersion" : dict([
            ("Media Aritmetica (X)" , X_),
            ("Media Geometrica (X_g)" , X_g),
            ("Media Armonica (X_h)" , X_h),
            ("Moda (Mo)" , Mo),
            ("Mediana (Me)" , Me),
            ("Varianza (S^2)" , S_2),
            ("Desviacion Estandar (S)" , S),
            ("CV%" , CV_Percent),
        ]),
        "Quantiles" : dict([
            ("Cuartil" , Arr_Quartile),
            ("Decil" , Arr_Decile),
            ("Percentil" , Arr_Percentile),
        ]),
        "Coefficient_Asymmetry" : dict([
            ("Pearson" , Coef_Pearson),
            ("Fisher" , Coef_Fisher),
            ("Kurtosis" , Coef_Kurtosis),
        ]),
    }

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

    return Variables_Value , Frecuences_Value , Summary_Measures

def Calculate_Results_Cuantitative_For_Not_Grouped_Data(Data):
    """ 
        ==============================================================================================
        Aqui se calculan los valores que iran dentro de la tabla de frecuencia para datos 
        cuantitativos no agrupados, los quantiles para datos no agrupados 
        (quartiles, deciles y percentiles) y algunas variables mas.
        ==============================================================================================
    """
    n = len(Data)

    Arr_xi , Arr_fi = Cuant_Not_Grouped.Calc_fi_And_xi(Data)
    N_Stadistic_Variables = len(Arr_xi)

    Arr_Fi = Cuant_Not_Grouped.calc_Fi(Arr_fi)

    Arr_hi = Cuant_Not_Grouped.Calc_hi(Data , Arr_fi)
    Arr_Hi = Cuant_Not_Grouped.Calc_Hi(Arr_hi)

    Arr_hi_percent = Cuant_Not_Grouped.Calc_hi_percent(Arr_hi)
    Arr_Hi_percent = Cuant_Not_Grouped.Calc_Hi_percent(Arr_Hi)

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

    Coef_Pearson = SM_For_Not_Grouped_Data.Calc_Pearson_Coefficient(X_ , Me , S)
    Coef_Fisher = SM_For_Not_Grouped_Data.Calc_Fisher_Coefficient(Data , X_ , n , S)
    Coef_Kurtosis = SM_For_Not_Grouped_Data.Calc_Kurtosis_Coefficient(Data , X_ , n , S)

    Summary_Measures = {
        "Measures_Of_Central_Tendency_And_Dispersion" : dict([
            ("Media Aritmetica (X)" , X_),
            ("Media Geometrica (X_g)" , X_g),
            ("Media Armonica (X_h)" , X_h),
            ("Moda (Mo)" , Mo),
            ("Mediana (Me)" , Me),
            ("Varianza (S^2)" , S_2),
            ("Desviacion Estandar (S)" , S),
            ("CV%" , CV_Percent),
        ]),
        "Quantiles" : dict([
            ("Cuartil" , Arr_Quartile),
            ("Decil" , Arr_Decile),
            ("Percentil" , Arr_Percentile),
        ]),
        "Coefficient_Asymmetry" : dict([
            ("Pearson" , Coef_Pearson),
            ("Fisher" , Coef_Fisher),
            ("Kurtosis" , Coef_Kurtosis),
        ]),
    }

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
    return Variables_Values , Frecuences_Values , Summary_Measures

def Calculate_Results_Cualitative_Data(Data):
    """ 
        ==============================================================================================
        Aqui se calculan los valores que iran dentro de la tabla de frecuencia para datos cualitativos, 
        y algunas variables mas.
        ==============================================================================================
    """
    n = len(Data)

    Arr_Char_Mod , Arr_fi = Cuali.Calc_fi_And_ai(Data)
    Number_Char_Mod = len(Arr_Char_Mod)

    Arr_Fi = Cuali.Calc_Fi(Arr_fi)

    Arr_hi = Cuali.Calc_hi(Data , Arr_fi)
    Arr_Hi = Cuali.Calc_Hi(Arr_hi)

    Arr_hi_percent = Cuali.Calc_hi_percent(Arr_hi)
    Arr_Hi_percent = Cuali.Calc_Hi_percent(Arr_Hi)

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

def Main_Function(In , Is_Continue , Repeated_Calc):
    """  
        ==============================================================================================
        Aqui se determina si los datos ingresados son cualitativos o cuantitativos, y se realizan los
        calculos necesarios segun el tipo de variable.
        ==============================================================================================
    """
    Variables_Cuant_Grouped = None
    Frecuences_Cuant_Grouped = None
    Summary_Measures_For_Grouped_Data = None

    Variables_Cuant_Not_Grouped = None
    Frecuences_Cuant_Not_Grouped = None
    Summary_Measures_For_Not_Grouped_Data = None

    Variables_Cuali = None
    Frecuences_Cuali = None
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
        
        if(len(Data) < 2):
            raise Exception("Se ingresaron muy pocos datos.")

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
                Data.sort()
                m = round(1 + (3.322*log10(len(Data))))
                
                if(not Repeated_Calc):
                    Arr_xi , Arr_fi = Cuant_Not_Grouped.Calc_fi_And_xi(Data)

                    if(len(Arr_xi) > (1/5)*(len(Data))):
                        Is_Continue[0].set(True)
                        Is_Continue[1].config(state="disabled")
                    elif(Is_Float and m > 5):
                        Is_Continue[0].set(True)
                        Is_Continue[1].config(state="disabled")
                    else:
                        Is_Continue[0].set(Is_Float)

                match(Is_Continue[0].get()):
                    case True:
                        if(m < 5):
                            Variables_Cuant_Not_Grouped , Frecuences_Cuant_Not_Grouped , Summary_Measures_For_Not_Grouped_Data = Calculate_Results_Cuantitative_For_Not_Grouped_Data(Data)
                        else:
                            Variables_Cuant_Grouped , Frecuences_Cuant_Grouped , Summary_Measures_For_Grouped_Data = Calculate_Results_Cuantitative_For_Grouped_Data(Data , Is_Float , m)
                    case False:
                        Variables_Cuant_Not_Grouped , Frecuences_Cuant_Not_Grouped , Summary_Measures_For_Not_Grouped_Data = Calculate_Results_Cuantitative_For_Not_Grouped_Data(Data)
            case False:
                Variables_Cuali , Frecuences_Cuali = Calculate_Results_Cualitative_Data(Data)
            case _:
                raise Exception("Hubo un error al identificar el tipo de variable de los datos ingresados.")

    Dictionary_Results = dict([
        ("Variables_Cuant_Grouped" , Variables_Cuant_Grouped),
        ("Frecuences_Cuant_Grouped" , Frecuences_Cuant_Grouped),
        ("Summary_Measures_For_Grouped_Data" , Summary_Measures_For_Grouped_Data),
        ("Variables_Cuant_Not_Grouped" , Variables_Cuant_Not_Grouped),
        ("Frecuences_Cuant_Not_Grouped" , Frecuences_Cuant_Not_Grouped),
        ("Summary_Measures_For_Not_Grouped_Data" , Summary_Measures_For_Not_Grouped_Data),
        ("Variables_Cuali" , Variables_Cuali),
        ("Frecuences_Cuali" , Frecuences_Cuali),
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
        Error en la funcion  Cuant_Not_Grouped.Find_Stadistic_Variable_xi, las listas de modificaban y quedaban vacias al terminar su ejecucion, perjudicando el resto de calculos
        Solucion, usar el metodo copy() para crear una copia del objeto. No usar otras variables, colo copy()
    """
    
    """ 
        Objetos mutables (como listas, diccionarios, conjuntos, etc.) se pasan por referencia. Si modificas el objeto dentro de la función, los cambios se reflejarán fuera de la función.
        Objetos inmutables (como enteros, cadenas de texto, tuplas, etc.) se pasan por valor. Esto significa que si modificas el valor dentro de la función, no afectará la variable original fuera de la función.
    """
