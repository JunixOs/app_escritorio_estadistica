import matplotlib.pyplot as plt
from datetime import datetime
import os
from tkinter import messagebox

def Export_Graph_As_Image(W_S_Graph , Root_Window , Graphs , File_Name , File_Path , dpi , Format , Bar_Title , Pie_Title , **kwargs):
    time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    Is_Checked = False
    if(Bar_Title == ""):
        Bar_Title = "Grafico de barras sobre la distribucion de los valores"
    if(Pie_Title == ""):
        Pie_Title = "Grafico de pastel sobre la distribucion de los valores"

    for a in kwargs.values():
        if(a):
            Is_Checked = True

    try:
        if(not Is_Checked):
            raise Exception("No se ha seleccionado un grafico para exportar")

        if(File_Name == ""):
            File_Name = "grafico"
        
        if not File_Path.endswith("/"):
            File_Path += "/"

        if(not os.path.exists(File_Path) or not os.path.isdir(File_Path)):
            raise Exception("Ruta de exportacion no valida")

        if(kwargs["Export_All"]):
            Full_Path = File_Path + File_Name + "_" + "fi" + "_" + time + Format
            Graphs["bar_fi"][1].suptitle(f"{Bar_Title} fi")
            Graphs["bar_fi"][1].savefig(Full_Path , dpi=dpi)

            Full_Path = File_Path + File_Name + "_" + "hi" + "_" + time + Format
            Graphs["bar_hi"][1].suptitle(f"{Bar_Title} hi")
            Graphs["bar_hi"][1].savefig(Full_Path , dpi=dpi)
            Full_Path = File_Path + File_Name + "_" + "hi%" + "_" + time + Format
            Graphs["bar_hi_percent"][1].suptitle(f"{Bar_Title} hi%")
            Graphs["bar_hi_percent"][1].savefig(Full_Path , dpi=dpi)

            Full_Path = File_Path + File_Name + "_" + "pie" + "_" + time + Format
            Graphs["pie_graph"][1].suptitle(f"{Pie_Title}")
            Graphs["pie_graph"][1].savefig(Full_Path , dpi=dpi)

        elif(kwargs["Export_All_Bars"]):
            Full_Path = File_Path + File_Name + "_" + "fi" + "_" + time + Format
            Graphs["bar_fi"][1].suptitle(f"{Bar_Title} fi")
            Graphs["bar_fi"][1].savefig(Full_Path , dpi=dpi)

            Full_Path = File_Path + File_Name + "_" + "hi" + "_" + time + Format
            Graphs["bar_hi"][1].suptitle(f"{Bar_Title} hi")
            Graphs["bar_hi"][1].savefig(Full_Path , dpi=dpi)

            Full_Path = File_Path + File_Name + "_" + "hi%" + "_" + time + Format
            Graphs["bar_hi_percent"][1].suptitle(f"{Bar_Title} hi%")
            Graphs["bar_hi_percent"][1].savefig(Full_Path , dpi=dpi)
        else:
            if(kwargs["Export_Bar_fi"]):
                Full_Path = File_Path + File_Name + "_" + "fi" + "_" + time + Format
                Graphs["bar_fi"][1].suptitle(f"{Bar_Title} fi")
                Graphs["bar_fi"][1].savefig(Full_Path , dpi=dpi)
            elif(kwargs["Export_Bar_hi"]):
                Full_Path = File_Path + File_Name + "_" + "hi" + "_" + time + Format
                Graphs["bar_hi"][1].suptitle(f"{Bar_Title} hi")
                Graphs["bar_hi"][1].savefig(Full_Path , dpi=dpi)
            elif(kwargs["Export_Bar_hi_percent"]):
                Full_Path = File_Path + File_Name + "_" + "hi%" + "_" + time + Format
                Graphs["bar_hi_percent"][1].suptitle(f"{Bar_Title} hi%")
                Graphs["bar_hi_percent"][1].savefig(Full_Path , dpi=dpi)
        
        if(kwargs["Export_Pie"]):
            Full_Path = File_Path + File_Name + "_" + "pie" + "_" + time + Format
            Graphs["pie_graph"][1].suptitle(f"{Pie_Title}")
            Graphs["pie_graph"][1].savefig(Full_Path , dpi=dpi)
    except Exception as e:
        messagebox.showerror("Error" , f"{e}")
    else:
        messagebox.showinfo("Success" , f"Las imagenes fueron exportadas con exito a\n{File_Path}")
        Root_Window.destroy()
        
        W_S_Graph.state(newstate="normal")
        W_S_Graph.lift()