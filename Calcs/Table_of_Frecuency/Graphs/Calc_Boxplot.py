import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
def Draw_Boxplot_For_Single_Column_Data(Data_List , Column_Name = None):
    if(Column_Name):
        Key = Column_Name
    else:
        Key = "Variable"

    Figure_Boxplot , ax = plt.subplots(figsize=(980/96 , 700/96) , dpi=96)


    sns.boxplot(data=Data_List , flierprops=dict(markerfacecolor='red', marker='o', markersize=8) , ax=ax)

    ax.set_ylabel("Valores")
    plt.xticks([0] , [f"{Key}"])

    return Figure_Boxplot

class Draw_Boxplot_For_Multiple_Columns_Data:
    def __init__(self , Results , Type_Of_Variable):
        self.Results = Results
        self.Type_Of_Variable = Type_Of_Variable

    def Draw_For_One_Column(self , Column_Name):
        if(self.Type_Of_Variable[f"{Column_Name}"] == "Cualitative_Grouped"):
            Draw_Boxplot_For_Single_Column_Data(self.Results[f"{Column_Name}"]["Variables_Cuant_For_Many_Values"]["Data_List"] , Column_Name)
        elif(self.Type_Of_Variable[f"{Column_Name}"] == "Cualitative_Not_Grouped"):
            Draw_Boxplot_For_Single_Column_Data(self.Results[f"{Column_Name}"]["Variables_Cuant_Normal_Extended"]["Data_List"] , Column_Name)

    def Draw_For_Many_Columns(self , Column_Names):
        Arr_Data_List = [value for key , value in self.Results.items() if key in Column_Names]

        Figure_Boxplot , ax = plt.subplots(figsize=(680/96 , 700/96) , dpi=96)

        sns.boxplot(data=Arr_Data_List , flierprops=dict(markerfacecolor='red', marker='o', markersize=8) , ax=ax)

        ax.set_ylabel("Valores")

        N_Columns = [n for n in range(0 , len(Arr_Data_List))]
        plt.xticks(N_Columns , Column_Names)

        return Figure_Boxplot

if __name__ == "__main__":
    data_List1 = np.random.normal(0, 1, 100)
    data_List2 = np.random.normal(1, 2, 100)
    data_List3 = np.random.normal(2, 1, 100)
    Data_List = dict([
        ("Circunferencias" ,data_List1) , 
        ("Radio" , data_List2) , 
        ("Longitud" , data_List3),
        ])
    Draw_Boxplot_For_Single_Column_Data(data_List1)
    """ Draw = Draw_Boxplot_For_Multiple_Columns_Data(Data_List , "")
    Draw.Draw_For_Many_Columns(["Circunferencias" , "Radio" , "Longitud"]) """

