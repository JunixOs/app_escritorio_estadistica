import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..')))

from math import *
from decimal import Decimal , getcontext
import Calcs.Table_of_Frecuency.Frecuences.Calc_Frecuences_Cuantitative_Grouped as Cuant_Grouped
import Calcs.Table_of_Frecuency.Frecuences.Calc_Frecuences_Cualitative as Cuali
import Calcs.Table_of_Frecuency.Frecuences.Calc_Frecuences_Cuantitative_Not_Grouped as Cuant_Not_Grouped
import Calcs.Table_of_Frecuency.Summary_Measures.Calc_For_Not_Grouped_Data as SM_For_Not_Grouped_Data
import Calcs.Table_of_Frecuency.Summary_Measures.Calc_For_Grouped_Data as SM_For_Grouped_Data

import time

def Check_Contains_Only_Numbers(Data):
    return not any(caracter.isalpha() for caracter in Data)

def Fix_Float_Error_For_Lists(Data):
    """
        ==============================================================================================
        Esta es una version de la funcion para arreglar el error los tipos de datos float en python,
        sirve para una lista de datos importada de un archivo externo.
        ==============================================================================================
    """
    New_Data = []
    for data in Data:
        Fixed_Number = Fix_Float_Number(data)
        New_Data.append(Fixed_Number)
    return New_Data

def Fix_Float_Number(data):
    """ 
        ==============================================================================================
        Esta funcion tiene el proposito de solucionar el error de los tipos de datos float en python,
        este error puede ocurrir al importar datos de un excel o al realizar demasiados calculos con
        decimales.
        El error se presenta asi, si realizamos la operacion 137/100 podemos esperar 0.0137, pero hay
        ocasiones donde el resultado es 0.01370000000000001, esto es un problema ya que al realizar
        operaciones con el, ese valor adicional tambien afectara los resultados.

        La funcion Fix_Float_Number toma el numero 0.01370000000000001 y
        extrae la parte decimal 01370000000000001 para luego comprobar si existen muchos 0's o 9's (
        tambien hay versiones del error con 0.99999...) y si encuentra muchos de esos valores entonces
        recorre el numero de izquierda a derecha para comprobar si el error esta presente (llevando 
        una cuenta de la cantidad de decimales que se estan revisando).
        Si se cuentan 4 o mas 0's o 9's entonces se para de revisar y se hace el redondeo con Decimal
        teniendo en cuenta la cantidad de decimales a redondear extraida del bucle for.
        ==============================================================================================
    """
    getcontext().prec = 35
    Fixed_Number = None

    try:
        decimal_list = list(str(data).split(".")[1])
        if(decimal_list.count("0") > 5 or decimal_list.count("9") > 5):
            zero_nine_counter = 0
            decimals_to_round = 0
            for letter in decimal_list:
                if(letter == "0" or letter == "9"):
                    zero_nine_counter += 1
                else:
                    zero_nine_counter = 0
                
                decimals_to_round += 1
                if(zero_nine_counter >= 4):
                    break
            str_to_round = "0." + "0"*(decimals_to_round - 1) + "1"
            data = Decimal(data)
            Fixed_Number = float(data.quantize(Decimal(str_to_round)))
        else:
            Fixed_Number = data
    except Exception:
        Fixed_Number = data
    return Fixed_Number

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
    Spacers = [" " , "\n" , "," , ";" , "\t"]
    for n in range(0,len(a)):
        char = a[n]
        if(char in Spacers or n==len(a)-1):
            """ Primero se comprueba que no haya un salto en blanco o un salto de linea o si la cadena esta a punto de terminar"""
            if(n==len(a)-1 and not char in Spacers):
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
    #start_time = time.time()

    V_Min = Cuant_Grouped.Calc_Min(Data)
    V_Max = Cuant_Grouped.Calc_Max(Data)
    n = len(Data)
    R = Cuant_Grouped.Calc_Range(V_Min,V_Max)
    if(not There_Are_Floats):
        """ 
            **********************************************************************************
            Si no existe ningun valor decimal entre todos los datos, entonces la amplitud se
            redondea por exceso con un maximo de 1 decimal.
            **********************************************************************************
        """
        C = Fix_Float_Number(R/m)
        C_N_Decimals = 1
        C , C_N_Decimals = Cuant_Grouped.Round_Amplitude(C , 1 , "Redondeo por maximo")

        Arr_Intervals = Cuant_Grouped.Calc_Intervals(V_Min , C , V_Max , m , C_N_Decimals , "Metodo de Ulises")
        # Arr_Groups = Cuant_Grouped.Calc_Groups_For_Integer_Numbers(Arr_Intervals , m , C_N_Decimals)
    else:
        """ 
            **********************************************************************************
            Si por el contrario, existe algun valor decimal entre todos los datos, entonces 
            la amplitud se redondea por exceso a la cantidad maxima de decimales entre 
            todos los datos.
            **********************************************************************************
        """
        Max_N_Decimals_In_Data = Cuant_Grouped.Calc_Max_Decimal_Number(Data)

        #end_time = time.time()
        #print(f"Tiempo de determinacion de mayor numero de decimales en los datos: {end_time - start_time:.9f}\n")
        #start_time = end_time

        C_N_Decimals = Max_N_Decimals_In_Data
        C = Fix_Float_Number(R/m)
        C , C_N_Decimals = Cuant_Grouped.Round_Amplitude(C , C_N_Decimals , "Redondeo por maximo")

        Arr_Intervals = Cuant_Grouped.Calc_Intervals(V_Min , C , V_Max , m , C_N_Decimals , "Metodo de Ulises")

    Arr_xi = Cuant_Grouped.Calc_xi(Arr_Intervals , m)

    Arr_fi = Cuant_Grouped.Calc_fi(Data , Arr_Intervals , m)
    Arr_Fi = Cuant_Grouped.Calc_Fi(Arr_fi)

    Arr_hi = Cuant_Grouped.Calc_hi(Data , Arr_fi)
    Arr_Hi = Cuant_Grouped.Calc_Hi(Arr_hi)

    Arr_hi_percent = Cuant_Grouped.Calc_hi_percent(Arr_hi)
    Arr_Hi_percent = Cuant_Grouped.Calc_Hi_percent(Arr_Hi)
    
    #end_time = time.time()
    #print(f"Tiempo de calculo de frecuencias: {end_time - start_time:.9f}\n")
    #start_time = end_time


    X_ = SM_For_Grouped_Data.Calc_Arithmetic_Average(len(Data) , Arr_xi , Arr_fi)
    Me = SM_For_Grouped_Data.Calc_Median_Me(len(Data) , Arr_fi , Arr_Fi , Arr_Intervals , C)
    Mo = SM_For_Grouped_Data.Calc_Mode_Mo(Arr_fi , Arr_Intervals , C)
    X_h = SM_For_Grouped_Data.Calc_Armonic_Average(len(Data) , Arr_xi , Arr_fi)
    X_g = SM_For_Grouped_Data.Calc_Geometric_Average(len(Data) , Arr_xi , Arr_fi)

    #end_time = time.time()
    #print(f"Tiempo de calculo de medidas de tendencia central: {end_time - start_time:.9f}\n")
    #start_time = end_time

    Arr_Quartile = SM_For_Grouped_Data.Calc_Quantile(4 , Data , Arr_Intervals , Arr_fi , Arr_Fi , C)
    Arr_Decile = SM_For_Grouped_Data.Calc_Quantile(10 , Data , Arr_Intervals , Arr_fi , Arr_Fi , C)
    Arr_Percentile = SM_For_Grouped_Data.Calc_Quantile(100 , Data , Arr_Intervals , Arr_fi , Arr_Fi , C)

    #end_time = time.time()
    #print(f"Tiempo de calculo de medidas de posicion: {end_time - start_time:.9f}\n")
    #start_time = end_time

    S_2 = SM_For_Grouped_Data.Calc_Variance(len(Data) , Arr_xi , Arr_fi , X_)
    S = SM_For_Grouped_Data.Calc_Standard_Deviation(S_2)
    CV_Percent = SM_For_Grouped_Data.Calc_Percentage_Coefficient_Variation(S , X_)
    Intercuartile_Range = SM_For_Grouped_Data.Calc_Interquartile_Range(Arr_Quartile)

    #end_time = time.time()
    #print(f"Tiempo de calculo de medidas de dispercion: {end_time - start_time:.9f}\n")
    #start_time = end_time

    Coef_Pearson = SM_For_Grouped_Data.Calc_Pearson_Coefficient(X_ , Me , S)
    Coef_Fisher = SM_For_Grouped_Data.Calc_Fisher_Coefficient(Arr_xi , X_ , Arr_fi , n , S)
    Coef_Kurtosis = SM_For_Grouped_Data.Calc_Kurtosis_Coefficient(Arr_Percentile , Arr_xi , X_ , Arr_fi , n , S)
    Coef_Bowley = SM_For_Grouped_Data.Calc_Bowley_Coefficient(Arr_Quartile)
    Coef_Kelly = SM_For_Grouped_Data.Calc_Kelly_Coefficient(Arr_Decile)

    #end_time = time.time()
    #print(f"Tiempo de calculo de coeficientes de asimetria: {end_time - start_time:.9f}\n")
    #start_time = end_time

    Summary_Measures = {
        "Measures_Of_Central_Tendency_And_Dispersion" : dict([
            ("Media Aritmetica (X)" , X_),
            ("Media Geometrica (X_g)" , X_g),
            ("Media Armonica (X_h)" , X_h),
            ("Moda (Mo)" , Mo),
            ("Mediana (Me)" , Me),
            ("Varianza (S^2)" , S_2),
            ("Desviacion Estandar (S)" , S),
            ("Coeficiente de Variacion Porcentual (CV%)" , CV_Percent),
            ("Rango Intercuartilico (IQR)" , Intercuartile_Range),
        ]),
        "Quantiles" : dict([
            ("Cuartil" , Arr_Quartile),
            ("Decil" , Arr_Decile),
            ("Percentil" , Arr_Percentile),
        ]),
        "Coefficient_Asymmetry" : dict([
            ("Pearson" , Coef_Pearson),
            ("Fisher" , Coef_Fisher),
            ("Bowley" , Coef_Bowley),
            ("Kurtosis" , Coef_Kurtosis),
            ("Kelly" , Coef_Kelly),
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
        # Groups = Arr_Groups, <-- Se elimina la visualizacion de los grupos
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

    Arr_Quartile = SM_For_Not_Grouped_Data.Calc_Quantile(4 , Data)
    Arr_Decile = SM_For_Not_Grouped_Data.Calc_Quantile(10 , Data)
    Arr_Percentile = SM_For_Not_Grouped_Data.Calc_Quantile(100 , Data)

    S_2 = SM_For_Not_Grouped_Data.Calc_Variance(X_ , Data)
    S = SM_For_Not_Grouped_Data.Calc_Standard_Deviation(S_2)
    CV_Percent = SM_For_Not_Grouped_Data.Calc_Percentage_Coefficient_Variation(S , X_)
    Intercuartile_Range = SM_For_Not_Grouped_Data.Calc_Interquartile_Range(Arr_Quartile)

    Coef_Pearson = SM_For_Not_Grouped_Data.Calc_Pearson_Coefficient(X_ , Me , S)
    Coef_Fisher = SM_For_Not_Grouped_Data.Calc_Fisher_Coefficient(Data , X_ , n , S)
    Coef_Kurtosis = SM_For_Not_Grouped_Data.Calc_Kurtosis_Coefficient(Data , X_ , n , S)
    Coef_Bowley = SM_For_Not_Grouped_Data.Calc_Bowley_Coefficient(Arr_Quartile)
    Coef_Kelly = SM_For_Not_Grouped_Data.Calc_Kelly_Coefficient(Arr_Decile)

    Summary_Measures = {
        "Measures_Of_Central_Tendency_And_Dispersion" : dict([
            ("Media Aritmetica (X)" , X_),
            ("Media Geometrica (X_g)" , X_g),
            ("Media Armonica (X_h)" , X_h),
            ("Moda (Mo)" , Mo),
            ("Mediana (Me)" , Me),
            ("Varianza (S^2)" , S_2),
            ("Desviacion Estandar (S)" , S),
            ("Coeficiente de Variacion Porcentual (CV%)" , CV_Percent),
            ("Rango Intercuartilico (IQR)" , Intercuartile_Range),
        ]),
        "Quantiles" : dict([
            ("Cuartil" , Arr_Quartile),
            ("Decil" , Arr_Decile),
            ("Percentil" , Arr_Percentile),
        ]),
        "Coefficient_Asymmetry" : dict([
            ("Pearson" , Coef_Pearson),
            ("Fisher" , Coef_Fisher),
            ("Bowley" , Coef_Bowley),
            ("Kurtosis" , Coef_Kurtosis),
            ("Kelly" , Coef_Kelly),
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

    Arr_ai , Arr_fi = Cuali.Calc_fi_And_ai(Data)
    
    Number_Char_Mod = len(Arr_ai)

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
        ai = Arr_ai,
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
        #start_time = time.time()

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
        #end_time = time.time()
        #print(f"Tiempo de determinacion de Tipo de Variable: {end_time - start_time:.9f}\n")
        #start_time = end_time

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
    
                #end_time = time.time()
                #print(f"Tiempo de determinacion de Naturaleza de Variable Cuantitativa: {end_time - start_time:.9f}\n")
                #start_time = end_time

                Data.sort()
                m = round(1 + (3.322*log10(len(Data)))) # Python redondea usando el "round half to even".
                
                #end_time = time.time()
                #print(f"Tiempo de ordenamiento de datos: {end_time - start_time:.9f}\n")
                #start_time = end_time

                if(not Repeated_Calc):
                    """ 
                        *********************************************************************************
                        Cuando el calculo se realiza por primera vez, se calcula cuantas variables unicas
                        hay.

                        Luego se determina si la cantidad de estas variables es mayor o menor al 20% de
                        la cantidad total de datos ingresados.
                        Si llega a ser mayor al 30% del total, entonces los datos se agrupan en 
                        intervalos y se consideran los datos como variables Cuantitativas Continuas.
                        Este criterio es util para evitar el calculo sin agrupar de variables
                        cuantitativas continuas cuyos valores ingresados son enteros 
                        y para preservar el calculo sin agrupar de variables cuantitativas discretas 
                        cuyos valores unicos son mas reducidos.

                        Si llega a ser menor al 20% del total, entonces se determina si entre los datos 
                        ingresados hay valores decimales y si el numero de intervalos (m) es mayor a 5, 
                        si esto se  cumple, entonces se consideran los datos como 
                        variables Cuantitativas Continuas y se agrupan en intervalos.

                        Si esto ultimo tampoco se cumple, entonces segun si existen variables decimales o
                        enteros se realizara el primer calculo, si son decimales, se agrupa en intervalos
                        dependiendo del valor de m, y si es entero, entonces los datos no se agrupan en
                        intervalos.
                        *********************************************************************************
                    """
                    Arr_xi , Arr_fi = Cuant_Not_Grouped.Calc_fi_And_xi(Data)

                    #end_time = time.time()
                    #print(f"Tiempo de calculo de xi y fi para decidir agrupar datos o no: {end_time - start_time:.9f}\n")
                    #start_time = end_time

                    if(len(Arr_xi) > (3/10)*(len(Data))):
                        Is_Continue[0].set(True)
                        Is_Continue[1].config(state="disabled")
                    elif(Is_Float and m > 5):
                        Is_Continue[0].set(True)
                        Is_Continue[1].config(state="disabled")
                    else:
                        Is_Continue[0].set(Is_Float)

                    #end_time = time.time()
                    #print(f"Tiempo de determinacion para agrupar datos: {end_time - start_time:.9f}\n")
                    #start_time = end_time

                    if(Is_Continue[0].get()):
                        Data = Fix_Float_Error_For_Lists(Data)

                    #end_time = time.time()
                    #print(f"Tiempo de reparacion de error de punto flotante para los datos: {end_time - start_time:.9f}\n")
                    #start_time = end_time

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
    Data_3 = "5, 2, 4, 9, 7, 4, 5, 6, 5, 7, 7, 5, 5, 2, 10, 5, 6, 5, 4, 5, 8, 8, 4, 0, 8, 4, 8, 6, 6, 3, 6, 7, 6, 6, 7, 6, 7, 3, 5, 6,9, 6, 1, 4, 6, 3, 5, 5, 6, 7"

    Data_2 = Convert_Input_Str_To_List(Data_2)
    Data_2 , There_Are_Floats = Conv_Data_To_Numbers(Data_2)
    Results = Calculate_Results_Cuantitative_For_Grouped_Data(Data_2 , There_Are_Floats , round(1+(3.322*log10(len(Data_2)))))
    
    print(Results)
    """ 
        Error en la funcion  Cuant_Not_Grouped.Find_Stadistic_Variable_xi, las listas de modificaban y quedaban vacias al terminar su ejecucion, perjudicando el resto de calculos
        Solucion, usar el metodo copy() para crear una copia del objeto. No usar otras variables, colo copy()
    """
    
    """ 
        Objetos mutables (como listas, diccionarios, conjuntos, etc.) se pasan por referencia. Si modificas el objeto dentro de la función, los cambios se reflejarán fuera de la función.
        Objetos inmutables (como enteros, cadenas de texto, tuplas, etc.) se pasan por valor. Esto significa que si modificas el valor dentro de la función, no afectará la variable original fuera de la función.
    """
