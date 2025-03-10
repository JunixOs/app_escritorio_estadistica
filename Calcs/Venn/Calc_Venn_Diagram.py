import matplotlib.pyplot as plt
from matplotlib_venn import venn2

class Venn_Diagram:
    def __init__(self , Data_From_Sets):
        self.Data_From_Sets = Data_From_Sets
        self.Labels = []
        self.Sets = []

        for key , s in self.Data_From_Sets.items():
            self.Labels = key
            self.Sets = s
    def Find_Elements_Only_One_Set(self):
        for i in range(len(self.Sets)):
            pass  
    def Generate_Diagrams(self):
        pass
    
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
g_ven.get_label_by_id("10").set_text(f"{old_text}\n{Only_A:.3f}%")
g_ven.get_label_by_id("10").set_backgroundcolor(color="#ffffff")
g_ven.get_label_by_id("01").set_text(f"{Only_B:.3f}%")
g_ven.get_label_by_id("11").set_text(f"{Intersection:.3f}%")

# Mostrar el gráfico
plt.title("Diagrama de Venn - 2 Conjuntos")
plt.show()