import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..')))

from Exceptions.Exception_Warning import Raise_Warning

import matplotlib.pyplot as plt
import venn
import numpy as np

def Convert_Input_Data_To_Set(a):
    """
        ==============================================================================================
        Esta funcion sirve para separar los datos si es que se da el caso de que el usuario introduce
        los datos manualmente. Aqui se recibe una cadena de texto, que luego se transformara en un
        set con cada uno de los valores.
        Esta pensado para trabajar con datos separados por espacios en blanco o saltos de linea.
        ==============================================================================================
    """
    Value = ""
    Data = set()
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
                Data.add(Value)
                Value = ""

        else:
            Value += char

    return Data

class Venn_Diagram:
    def __init__(self , Data_From_Sets , Imported_From_Excel = False):
        self.Data_From_Sets = Data_From_Sets
        self.Imported_From_Excel = Imported_From_Excel

        if(not(self.Data_From_Sets)):
            raise Raise_Warning("No se ingresaron datos.")
            
        if(self.Imported_From_Excel):
            for key , value in self.Data_From_Sets.items():
                self.Data_From_Sets[f"{key}"] = set(value)
        else:
            for key , value in self.Data_From_Sets.items():
                self.Data_From_Sets[f"{key}"] = Convert_Input_Data_To_Set(value)

        self.N_Sets = len(self.Data_From_Sets)

    def Generate_Diagram(self):
        if(self.N_Sets < 2):
            raise Raise_Warning("No se puede calcular el diagrama para un solo conjunto.")
        elif(self.N_Sets > 6):
            raise Raise_Warning("No se puede calcular el diagrama para mas de 6 conjuntos")
        
        Values_Labels = venn.generate_petal_labels(self.Data_From_Sets.values())
        total_elements = np.sum(int(v) for v in Values_Labels.values())
        New_Labels = {}
        for key , value in Values_Labels.items():
            value = int(value)
            New_Labels[f"{key}"] = f"{value}\n({(value * 100 / total_elements):.1f}%)"

        figure_venn = plt.Figure(figsize=(900/72 , 510/72) , dpi=72)

        ax = figure_venn.add_subplot(111)
        venn.draw_venn(petal_labels=New_Labels , dataset_labels=self.Data_From_Sets.keys() , hint_hidden=False , colors=venn.generate_colors(n_colors=3) , figsize=(900/72 , 510/72) , fontsize=10, legend_loc="best", ax=ax)
            
        return figure_venn


# Definir los elementos en cada conjunto
if(__name__ == "__main__"):
    """
        1 2 3 4
        3 4 5 6
    """
    set_A = {1, 2, 3, 4}
    set_B = {3, 4, 5, 6}
    Sets ={
        "A" : set_A,
        "B" : set_B,
    }
    total_elements = len(set_A.union(set_B))

    Only_A = (len(set_A - set_B) / total_elements) * 100
    Only_B = (len(set_B - set_A) / total_elements) * 100
    Intersection = (len(set_A & set_B) / total_elements) * 100
    # Crear el diagrama de Venn
    labels = venn.generate_petal_labels(Sets.values())
    total_elements = np.sum(int(a) for a in labels.values())
    new_labels = {}
    for key , value in labels.items():
        value = int(value)
        new_labels[f"{key}"] = f"{value}\n{round(value*100/total_elements , 4)}"

    g_ven = venn.draw_venn(petal_labels = new_labels , dataset_labels=Sets.keys() , hint_hidden=False, colors=venn.generate_colors(n_colors=3),
    figsize=(8, 8), fontsize=14, legend_loc="best", ax=None)

    """ g_ven[0].suptitle("Diagrama de Venn - 2 Conjuntos")
    g_ven[0].savefig("C:/Users/yonel/Downloads/grafico2" , dpi=72 , bbox_inches='tight') """
    # Mostrar el gráfico
    plt.title("Diagrama de Venn - 2 Conjuntos")
    plt.show()