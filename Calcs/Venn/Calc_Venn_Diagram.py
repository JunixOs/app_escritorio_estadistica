import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from matplotlib_venn import venn3
import numpy as np

def Convert_Input_Str_To_Set(a):
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
    def __init__(self , Data_From_Widgets_Sets , Imported_Data):
        self.Data_From_Sets = Data_From_Widgets_Sets
        self.Imported_Data = Imported_Data
        self.Sets_Names = []
        self.Sets_Values = []

        if(self.Imported_Data):
            for key , s in self.Imported_Data.items():
                self.Sets_Names.append(key)
                self.Sets_Values.append(s)
        elif(self.Data_From_Sets):
            for key , s in self.Data_From_Sets.items():
                self.Sets_Names.append(key)
                Data_In_Sets = Convert_Input_Str_To_Set(s[2].get())
                self.Sets_Values.append(Data_In_Sets)
        else:
            raise Exception("No se ingresaron datos.")
        self.N_Sets = len(self.Sets_Names)

    def Calc_ID_For_Sets(self):
        ID = [str(bin(a)).replace("0b" , "") for a in range(2 ** len(self.Sets_Values)) if a != 0]
        for i in range(len(ID)):
            if(len(ID[i]) < self.N_Sets):
                ID[i] = "0"*(self.N_Sets - len(ID[i])) + ID[i]
        return ID

    def Generate_Diagrams(self):
        match(len(self.Sets_Values)):
            case 2:
                fiugre_venn = venn2(self.Sets_Values , set_labels=tuple(self.Sets_Names))
            case 3:
                fiugre_venn = venn3(self.Sets_Values , set_labels=tuple(self.Sets_Names))
            case _:
                raise Exception("Se deben ingresar un minimo de 2 cojuntos de datos")
        ID = self.Calc_ID_For_Sets()
        Total_Elements = np.sum(int(fiugre_venn.get_label_by_id(f"{identifier}").get_text()) for identifier in ID)
        for identifier in ID:
            old_text = fiugre_venn.get_label_by_id(f"{identifier}").get_text()
            Percentage = round((int(old_text) / Total_Elements) * 100 , 4)
            fiugre_venn.get_label_by_id(f"{identifier}").set_text(f"{old_text}\n{Percentage}")
        
        return fiugre_venn


# Definir los elementos en cada conjunto
if(__name__ == "__main__"):
    set_A = {1, 2, 3, 4}
    set_B = {3, 4, 5, 6}
    total_elements = len(set_A.union(set_B))

    Only_A = (len(set_A - set_B) / total_elements) * 100
    Only_B = (len(set_B - set_A) / total_elements) * 100
    Intersection = (len(set_A & set_B) / total_elements) * 100

    # Crear el diagrama de Venn
    g_ven = venn2([set_A, set_B], set_labels=('A', 'B'))


    old_text = g_ven.get_label_by_id("10").get_text()
    percent = round((int(old_text) / total_elements) * 100 , 4)
    g_ven.get_label_by_id("10").set_text(f"{old_text}\n{percent:.4f}%")
    g_ven.get_label_by_id("10").set_backgroundcolor(color="#ffffff")
    g_ven.get_label_by_id("01").set_text(f"{Only_B:.3f}%")
    g_ven.get_label_by_id("11").set_text(f"{Intersection:.3f}%")

    # Mostrar el gráfico
    plt.title("Diagrama de Venn - 2 Conjuntos")
    plt.show()