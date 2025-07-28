import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Tools import Insert_Data_In_Log_File , Get_Detailed_Info_About_Error
from Exceptions.Exception_Warning import Raise_Warning
from datetime import datetime
from tkinter import messagebox

class Validations:
    def Validate_Route(self , File_Name , File_Path):
        if(File_Name == ""):
            File_Name = "venn"
        
        if(File_Path == ""):
            raise Raise_Warning("No se ha ingresado ninguna ruta de exportacion")
        elif not File_Path.endswith("/"):
            File_Path += "/"

        if(not os.path.exists(File_Path) or not os.path.isdir(File_Path)):
            raise Raise_Warning("Ruta de exportacion no valida")
        return File_Path + File_Name
    

class Export_Diagram:
    def __init__(self , Graph , File_Name , File_Path , Format , Resolution , Venn_Diagram_Title):
        self.Full_Route = Validations.Validate_Route(self , File_Name , File_Path)
        self.Graph = Graph
        self.Format = Format
        self.Resolution = Resolution
        self.Venn_Diagram_Title = Venn_Diagram_Title
        self.Actual_Time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    def Export(self):
        Route_To_Export = self.Full_Route + "_" + self.Actual_Time + self.Format
        if(self.Venn_Diagram_Title):
            self.Graph.suptitle(f"{self.Venn_Diagram_Title}")

        self.Graph.savefig(Route_To_Export , dpi=self.Resolution , bbox_inches='tight')
        self.Graph.suptitle("")

def Export_Venn_Diagram_As_Image(W_Export_Venn_Diagram , Graph , File_Name , File_Path , Format , Resolution , Venn_Diagram_Title):
    try:

        Export = Export_Diagram(Graph , File_Name , File_Path , Format , Resolution , Venn_Diagram_Title)

        Export.Export()

    except Raise_Warning as e:
        Insert_Data_In_Log_File(e , "Advertencia" , "Exportacion de graficos de Venn")
        messagebox.showwarning("Advertencia" , f"{e}")
    except Exception as e:
        Insert_Data_In_Log_File("Ocurrio un error al exportar los diagramas de Venn" , "Error" , "Exportacion de graficos de Venn" , Get_Detailed_Info_About_Error())
        messagebox.showerror("Error" , "Ocurrio un error al exportar los diagramas de Venn")
    else:
        Insert_Data_In_Log_File(f"Se exporto el grafico de Venn correctamente a {File_Path}" , "Operacion exitosa" , "Exportacion de graficos de Venn")

        messagebox.showinfo("Sucess" , f"Grafico exportado con exito a {File_Path}")

        W_Export_Venn_Diagram.destroy()