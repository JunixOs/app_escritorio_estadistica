""" Codgio extraido y adaptado de ejemplo1.py de Paul Tarazona Benancio """

from scipy.stats import norm # type: ignore
from tkinter import messagebox

def qnorm(probability , average = 0 , deviation = 1):
    return norm.ppf(probability , loc=average , scale = deviation)

def Calc_Probability(Confidence_Level , Precision=2):
    alpha = 1 - Confidence_Level
    probability = 1 - (alpha/2)
    return round(qnorm(probability) , Precision)

def Calc_Samplings(e , Confidence_Level , N , n_o=0 , n_f=0 , Finite_Population=True , Precision=2 , p=50):
    try:
        e /= 100
        Confidence_Level /= 100
        p /= 100
        q = 1 - p
        if(e < 0):
            raise Exception("El error no puede tener un valor negativo.")
        elif(p < 0):
            raise Exception("La probabilidad de exito no puede tener un valor negativo.")
        elif(Confidence_Level < 0):
            raise Exception("El nivel de confianza no puede tener un valor negativo.")

        Z = Calc_Probability(Confidence_Level , Precision)
        if(Finite_Population):
            initial = round(((Z**2)*p*q*N)/(((e**2)*(N-1))+((Z**2)*p*q)))
            final = round(initial/(1+(initial/N)))
        else:
            initial = round(((Z**2)*p*q)/e**2)
            final = 0
        n_o.set(initial)
        n_f.set(final)
    except Exception as e:
        messagebox.showerror("Error" , f"{e}")