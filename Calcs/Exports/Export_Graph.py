from datetime import datetime
import os
from tkinter import messagebox

def Export_Graph_As_Image(W_Show_Graph , W_Export_Graph , Graphs , File_Name , File_Path , Extra_Info , Multiple_Columns , **kwargs):
    dpi = int(dpi)
    time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    Is_Checked = False
    Checkboxes_Values = {}

    """ if(Multiple_Columns):
        for key , value in Extra_Info.items():
            Checkboxes_Values[f"{key}"] = value. """

    for a in kwargs.values():
        if(a):
            Is_Checked = True

    try:
        if(not Is_Checked):
            raise Exception("No se ha seleccionado un grafico para exportar")

        if(File_Name == ""):
            File_Name = "grafico"

        if(File_Path == ""):
            raise Exception("No se ha ingresado ninguna ruta de exportacion")
        elif not File_Path.endswith("/"):
            File_Path += "/"

        if(not os.path.exists(File_Path) or not os.path.isdir(File_Path)):
            raise Exception("Ruta de exportacion no valida")

        if(kwargs["Export_All"]):
            Full_Path = File_Path + File_Name + "_" + "fi" + "_" + time + Format
            Graphs["bar_fi"].suptitle(f"{Bar_Title} fi")
            Graphs["bar_fi"].savefig(Full_Path , dpi=dpi)

            Full_Path = File_Path + File_Name + "_" + "hi" + "_" + time + Format
            Graphs["bar_hi"].suptitle(f"{Bar_Title} hi")
            Graphs["bar_hi"].savefig(Full_Path , dpi=dpi)
            Full_Path = File_Path + File_Name + "_" + "hi%" + "_" + time + Format
            Graphs["bar_hi_percent"].suptitle(f"{Bar_Title} hi%")
            Graphs["bar_hi_percent"].savefig(Full_Path , dpi=dpi)

            Full_Path = File_Path + File_Name + "_" + "pie" + "_" + time + Format
            Graphs["pie_graph"].suptitle(f"{Pie_Title}")
            Graphs["pie_graph"].savefig(Full_Path , dpi=dpi)

            if("boxplot_graph" in Graphs):
                File_Path + File_Name + "_" + "boxplot" + "_" + time + Format
                Graphs["boxplot_graph"].suptitle(f"{Boxplot_Title}")
                Graphs["boxplot_graph"].savefig(Full_Path , dpi=dpi)

        elif(kwargs["Export_All_Bars"]):
            Full_Path = File_Path + File_Name + "_" + "fi" + "_" + time + Format
            Graphs["bar_fi"].suptitle(f"{Bar_Title} fi")
            Graphs["bar_fi"].savefig(Full_Path , dpi=dpi)

            Full_Path = File_Path + File_Name + "_" + "hi" + "_" + time + Format
            Graphs["bar_hi"].suptitle(f"{Bar_Title} hi")
            Graphs["bar_hi"].savefig(Full_Path , dpi=dpi)

            Full_Path = File_Path + File_Name + "_" + "hi%" + "_" + time + Format
            Graphs["bar_hi_percent"].suptitle(f"{Bar_Title} hi%")
            Graphs["bar_hi_percent"].savefig(Full_Path , dpi=dpi)
            
            if(kwargs["Export_Pie"]):
                Full_Path = File_Path + File_Name + "_" + "pie" + "_" + time + Format
                Graphs["pie_graph"].suptitle(f"{Pie_Title}")
                Graphs["pie_graph"].savefig(Full_Path , dpi=dpi)
            if(kwargs["Export_Boxplot"] and "boxplot_graph" in Graphs):
                Full_Path = File_Path + File_Name + "_" + "boxplot" + "_" + time + Format
                Graphs["boxplot_graph"].suptitle(f"{Boxplot_Title}")
                Graphs["boxplot_graph"].savefig(Full_Path , dpi=dpi)
        else:
            if(kwargs["Export_Bar_fi"]):
                Full_Path = File_Path + File_Name + "_" + "fi" + "_" + time + Format
                Graphs["bar_fi"].suptitle(f"{Bar_Title} fi")
                Graphs["bar_fi"].savefig(Full_Path , dpi=dpi)
            if(kwargs["Export_Bar_hi"]):
                Full_Path = File_Path + File_Name + "_" + "hi" + "_" + time + Format
                Graphs["bar_hi"].suptitle(f"{Bar_Title} hi")
                Graphs["bar_hi"].savefig(Full_Path , dpi=dpi)
            if(kwargs["Export_Bar_hi_percent"]):
                Full_Path = File_Path + File_Name + "_" + "hi%" + "_" + time + Format
                Graphs["bar_hi_percent"].suptitle(f"{Bar_Title} hi%")
                Graphs["bar_hi_percent"].savefig(Full_Path , dpi=dpi)
            if(kwargs["Export_Pie"]):
                Full_Path = File_Path + File_Name + "_" + "pie" + "_" + time + Format
                Graphs["pie_graph"].suptitle(f"{Pie_Title}")
                Graphs["pie_graph"].savefig(Full_Path , dpi=dpi)
            if(kwargs["Export_Boxplot"] and "boxplot_graph" in Graphs):
                Full_Path = File_Path + File_Name + "_" + "boxplot" + "_" + time + Format
                Graphs["boxplot_graph"].suptitle(f"{Boxplot_Title}")
                Graphs["boxplot_graph"].savefig(Full_Path , dpi=dpi)

    except Exception as e:
        messagebox.showerror("Error" , f"{e}")
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