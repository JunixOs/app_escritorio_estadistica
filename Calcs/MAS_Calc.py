""" Codgio extraido y adaptado de ejemplo1.py de Paul Tarazona Benancio """

from scipy.stats import norm # type: ignore

def qnorm(probability , average = 0 , deviation = 1):
    return norm.ppf(probability , loc=average , scale = deviation)

def Calc_Probability(Confidence_Level , Precision=2):
    alpha = 1 - Confidence_Level
    probability = 1 - (alpha/2)
    return round(qnorm(probability) , Precision)

def Calc_Samplings(e , Confidence_Level , N , n_o=0 , n_f=0 , Finite_Population=True , Precision=2 , p=50):
    """ Aplicar un manejo de excepciones """
    e /= 100
    Confidence_Level /= 100
    p /= 100
    q = 1 - p
    Z = Calc_Probability(Confidence_Level , Precision)
    if(Finite_Population):
        initial = round(((Z**2)*p*q*N)/(((e**2)*(N-1))+((Z**2)*p*q)))
        final = round(initial/(1+(initial/N)))
    else:
        initial = round(((Z**2)*p*q)/e**2)
        final = 0
    n_o.set(initial)
    n_f.set(final)