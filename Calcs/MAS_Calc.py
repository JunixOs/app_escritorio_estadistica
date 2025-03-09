""" Codgio extraido y adaptado de ejemplo1.py de Paul Tarazona Benancio """
import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Exceptions.Exception_Warning import Raise_Warning
from scipy.stats import norm # type: ignore
from tkinter import messagebox

def qnorm(probability , average = 0 , deviation = 1):
    return norm.ppf(probability , loc=average , scale = deviation)

def Calc_Probability(Confidence_Level , Precision=2):
    alpha = 1 - Confidence_Level
    probability = 1 - (alpha/2)
    return round(qnorm(probability) , Precision)

def Calc_Samplings(e , Confidence_Level , N , Finite_Population , Infinite_Population , n_o=0 , n_f=0 , Precision=2 , p=50):
    try:
        e /= 100
        Confidence_Level /= 100
        p /= 100
        q = 1 - p
        if(e < 0):
            raise Raise_Warning("El error no puede tener un valor negativo.")
        elif(p < 0):
            raise Raise_Warning("La probabilidad de exito no puede tener un valor negativo.")
        elif(Confidence_Level < 0):
            raise Raise_Warning("El nivel de confianza no puede tener un valor negativo.")

        Z = Calc_Probability(Confidence_Level , Precision)
        if(Finite_Population):
            if(N == 0):
                raise Raise_Warning("El valor de la poblacion no puede ser cero.")
            elif(N < 0):
                raise Raise_Warning("El valor de la poblacion no puede ser negativa.")
            initial = round(((Z**2)*p*q*N)/(((e**2)*(N-1))+((Z**2)*p*q)))
            final = round(initial/(1+(initial/N)))
        elif(Infinite_Population):
            if(e == 0):
                raise Exception("El error no puede ser igual a cero.")
            initial = round(((Z**2)*p*q)/e**2)
            final = 0
        else:
            raise Raise_Warning("No se ha seleccionado la naturaleza de la poblacion.")

        n_o.set(initial)
        n_f.set(final)
    except Raise_Warning as e:
        messagebox.showwarning("Advertencia" , f"{e}")
    except Exception as e:
        messagebox.showerror("Error" , f"{e}")