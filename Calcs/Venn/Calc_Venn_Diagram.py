import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from matplotlib_venn import venn3

class Venn_Diagram:
    def __init__(self , Data_From_Sets):
        self.Data_From_Sets = Data_From_Sets
        self.Sets_Names = []
        self.Sets_Values = []
        self.Arr_Only_One_Set = []

        for key , s in self.Data_From_Sets.items():
            self.Sets_Names = key
            self.Sets_Values = s

        self.N_Sets = len(self.Sets)
    def Find_Elements_Only_One_Set(self):
        for i in range(len(self.Sets)):
            Collection_Only_One_Set = [len(self.Sets[i] - self.Sets[a]) for a in range(len(self.Sets)) if a != i]
            Only_One_Set = min(Collection_Only_One_Set)
    def Calc_ID_For_Sets(self):
        ID = [str(bin(a)).replace("0b" , "") for a in range(2 ** len(self.Sets)) if a != 0]
        for i in range(len(ID)):
            if(len(ID[i]) < self.N_Sets):
                ID[i] = "0"*(self.N_Sets - len(ID[i])) + ID[i]
        return ID
    def Generate_Diagrams(self):
        fiugre_venn = venn2(self.Sets , set_labels=tuple(self.Labels))


# Definir los elementos en cada conjunto
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