from datetime import datetime
import os
from tkinter import messagebox

class Validations:
    def Validate_Route(self , File_Name , File_Path):
        if(File_Name == ""):
            File_Name = "grafico"
        
        if(File_Path == ""):
            raise Exception("No se ha ingresado ninguna ruta de exportacion")
        elif not File_Path.endswith("/"):
            File_Path += "/"

        if(not os.path.exists(File_Path) or not os.path.isdir(File_Path)):
            raise Exception("Ruta de exportacion no valida")
        return File_Path + File_Name
    
class Exports(Validations):
    def __init__(self , Graphs , File_Name , File_Path , Format , Resolution , Variable_Name , Bar_Title , Pie_Title , Boxplot_Title):
        self.Graphs = Graphs
        self.Full_Route = self.Validate_Route(File_Name , File_Path)
        self.Format = Format
        self.Resolution = Resolution
        self.Variable_Name = Variable_Name
        self.Extra_Info_Graph = ["fi" , "hi" , "hi%" , "pie"]
        self.Actual_Time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        self.Graphs_Title = [Bar_Title , Bar_Title , Bar_Title , Pie_Title]

        if("boxplot_graph" in Graphs):
            self.Extra_Info_Graph.append("boxplot")
            self.Graphs_Title.append(Boxplot_Title)

    def Export_All(self):
        for i , graphs in enumerate(self.Graphs.values()):
            if(self.Variable_Name):
                Route_To_Export = self.Full_Route + "_" + self.Extra_Info_Graph[i] + "_para_" + self.Variable_Name + self.Actual_Time + self.Format
            else:
                Route_To_Export = self.Full_Route + "_" + self.Extra_Info_Graph[i] + "_" + self.Actual_Time + self.Format
            graphs.suptitle(f"{self.Graphs_Title[i]}")
            graphs.savefig(Route_To_Export , dpi=self.Resolution)

    def Export_Only_Bars(self):
        for i , bar in enumerate(self.Graphs.values()):
            if(i <= 2):
                if(self.Variable_Name):
                    Route_To_Export = self.Full_Route + "_" + self.Extra_Info_Graph[i] + "_para_" + self.Variable_Name + "_" + self.Actual_Time + self.Format
                else:
                    Route_To_Export = self.Full_Route + "_" + self.Extra_Info_Graph[i] + "_" + self.Actual_Time + self.Format
                bar.suptitle(f"{self.Graphs_Title[i]}")
                bar.savefig(Route_To_Export , dpi=self.Resolution)

    def Export_One_Graph(self , Graph_Name , E_Info_Graph):
        Graph = self.Graphs[f"{Graph_Name}"]

        if("fi" in Graph_Name or "hi" in Graph_Name):
            G_Name = self.Graphs_Title[0]
        elif("pie" in Graph_Name):
            G_Name = self.Graphs_Title[3]
        elif("boxplot" in Graph_Name):
            G_Name = self.Graphs_Title[4]

        if(self.Variable_Name):
            Route_To_Export = self.Full_Route + "_" + E_Info_Graph + "_para_" + self.Variable_Name + self.Actual_Time + self.Format
        else:
            Route_To_Export = self.Full_Route + "_" + E_Info_Graph + "_" + self.Actual_Time + self.Format
        Graph.suptitle(f"{G_Name}")
        Graph.savefig(Route_To_Export , dpi=self.Resolution)

def Export_Graph_As_Image(W_Show_Graph , W_Export_Graph , Graphs , File_Name , File_Path , Info_For_Export , Checkboxes_Info , Variable_Name_For_Single_Column = None):
    try:
        if(isinstance(Info_For_Export , dict)):
            Check_Checked = []
            for check in Checkboxes_Info.values():
                Check_Checked.append(any([boolean[1].get() for boolean in check.values()]))

            if(not any(Check_Checked)):
                raise Exception("No se ha seleccionado un grafico para exportar")

            for i , (key , I_Export) in enumerate(Info_For_Export.items()):
                Export = None
                if(not Check_Checked[i]):
                    continue

                Export = Exports(
                    Graphs[f"{key}"] , File_Name , File_Path , I_Export.Input_Format.get() , int(I_Export.Input_dpi.get()) ,
                    key , I_Export.Name_Bar_Graph.get() , I_Export.Name_Pie_Graph.get() , I_Export.Name_Boxplot_Graph.get()
                )
                if(Checkboxes_Info[f"{key}"]["All"][1].get()):
                    Export.Export_All()
                elif(Checkboxes_Info[f"{key}"]["All_Bars"][1].get()):
                    Export.Export_Only_Bars()
                    if(Checkboxes_Info[f"{key}"]["Pie"][1].get()):
                        Export.Export_One_Graph("pie_graph" , "pie")
                    if(Checkboxes_Info[f"{key}"]["Boxplot"][1].get() and "boxplot_graph" in Graphs[f"{key}"]):
                        Export.Export_One_Graph("boxplot_graph" , "boxplot")
                else:
                    if(Checkboxes_Info[f"{key}"]["Bars_fi"][1].get()):
                        Export.Export_One_Graph("bar_fi" , "fi")
                    if(Checkboxes_Info[f"{key}"]["Bar_hi"][1].get()):
                        Export.Export_One_Graph("bar_hi" , "hi")
                    if(Checkboxes_Info[f"{key}"]["Bar_hi_percent"][1].get()):
                        Export.Export_One_Graph("bar_hi_percent" , "hi%")
                    if(Checkboxes_Info[f"{key}"]["Pie"][1].get()):
                        Export.Export_One_Graph("pie_graph" , "pie")
                    if(Checkboxes_Info[f"{key}"]["Boxplot"][1].get() and "boxplot_graph" in Graphs[f"{key}"]):
                        Export.Export_One_Graph("boxplot_graph" , "boxplot")
            
        else:
            if(not any(Checkboxes_Info)):
                raise Exception("No se ha seleccionado un grafico para exportar")
            Export = Exports(
                Graphs , File_Name , File_Path , Info_For_Export.Input_Format.get() , int(Info_For_Export.Input_dpi.get()) , 
                Variable_Name_For_Single_Column , Info_For_Export.Name_Bar_Graph.get() , Info_For_Export.Name_Pie_Graph.get() ,
                Info_For_Export.Name_Boxplot_Graph.get())

            if(Checkboxes_Info["All"][1].get()):
                Export.Export_All()
            elif(Checkboxes_Info["All_Bars"][1].get()):
                Export.Export_Only_Bars()
                if(Checkboxes_Info["Pie"][1].get()):
                    Export.Export_One_Graph("pie_graph" , "pie")
                if(Checkboxes_Info["Boxplot"][1].get()):
                    Export.Export_One_Graph("boxplot_graph" , "boxplot")
            else:
                if(Checkboxes_Info["Bars_fi"][1].get()):
                    Export.Export_One_Graph("bar_fi" , "fi")
                if(Checkboxes_Info["Bar_hi"][1].get()):
                    Export.Export_One_Graph("bar_hi" , "hi")
                if(Checkboxes_Info["Bar_hi_percent"][1].get()):
                    Export.Export_One_Graph("bar_hi_percent" , "hi%")
                if(Checkboxes_Info["Pie"][1].get()):
                    Export.Export_One_Graph("pie_graph" , "pie")
                if(Checkboxes_Info["Boxplot"][1].get()):
                    Export.Export_One_Graph("boxplot_graph" , "boxplot")

    except Exception as e:
        messagebox.showerror("Error" , f"{e}")
    else:
        if(isinstance(Info_For_Export , dict)):
            for graph in Graphs.values():
                graph["bar_fi"].suptitle("")
                graph["bar_hi"].suptitle("")
                graph["bar_hi_percent"].suptitle("")
                graph["pie_graph"].suptitle("")
                if("boxplot_graph" in graph):
                    graph["boxplot_graph"].suptitle("")
        else:
            Graphs["bar_fi"].suptitle("")
            Graphs["bar_hi"].suptitle("")
            Graphs["bar_hi_percent"].suptitle("")
            Graphs["pie_graph"].suptitle("")
            if("boxplot_graph" in Graphs):
                Graphs["boxplot_graph"].suptitle("")

        Reply = messagebox.askquestion("Success" , f"Las imagenes fueron exportadas con exito a\n{File_Path}\n¿Desea salir de la ventana de exportacion?")
        if(Reply == "yes"):
            W_Export_Graph.quit()
            W_Export_Graph.destroy()

            W_Show_Graph.state(newstate="normal")
            W_Show_Graph.lift()
            W_Show_Graph.grab_set()