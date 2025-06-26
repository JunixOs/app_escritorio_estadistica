import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..' , '..')))

from Exceptions.Exception_Warning import Raise_Warning; from Tools import Delete_Actual_Window

from datetime import datetime
import os
from tkinter import messagebox

def Validation_For_Export(File_Name , File_Path):
    if(File_Name == ""):
        File_Name = "grafico"
    
    if(File_Path == ""):
        raise Raise_Warning("No se ha ingresado ninguna ruta de exportacion")
    elif not File_Path.endswith("/"):
        File_Path += "/"

    if(not os.path.exists(File_Path) or not os.path.isdir(File_Path)):
        raise Raise_Warning("Ruta de exportacion no valida")
    return File_Path + File_Name
    
def Get_Actual_Time():
    return datetime.now().strftime("%d_%m_%Y__%H_%M_%S")

def Build_Full_Export_Route(Route_And_File_Name , Name_Of_Graph , Variable_Name , Img_Format):
    if(Variable_Name):
        return Route_And_File_Name + "_" + Name_Of_Graph + "_para_" + Variable_Name + "_" + Get_Actual_Time() + Img_Format
    else:
        return Route_And_File_Name + "_" + Name_Of_Graph + "_" + Get_Actual_Time() + Img_Format

def Get_Values_From_Widgets_When_There_Are_Multiple_Columns_Of_Data(Collection_Formats , Collection_DPIs , Collection_Axis_x_Titles_For_Graphs):
    Value_Collection_Formats = {}
    Value_Collection_DPIs = {}
    Value_Collection_Axis_x_Titles_For_Graphs = {}

    for (key , img_format) , dpi , axis_x_title in zip(Collection_Formats.items() , Collection_DPIs.values() , Collection_Axis_x_Titles_For_Graphs.values()):
        Value_Collection_Formats[key] = img_format.get()
        Value_Collection_DPIs[key] = int(dpi.get())
        Value_Collection_Axis_x_Titles_For_Graphs[key] = axis_x_title.get()
    return Value_Collection_Formats , Value_Collection_DPIs , Value_Collection_Axis_x_Titles_For_Graphs

def Manage_Export_Of_Graphs(W_Show_Graph , W_Export_Graph , File_Name , File_Path , Collection_Formats , Collection_DPIs , Collection_Axis_x_Titles_For_Graphs , Dictionary_Of_Generated_Figures , Collection_Subcheckboxes_With_Selected_Graphs , Collection_Entry_Titles_For_Graphs , Is_Single_Row):
    try:
        Route_And_File_Name = Validation_For_Export(File_Name , File_Path)

        Value_Collection_Formats , Value_Collection_DPIs , Value_Collection_Axis_x_Titles_For_Graphs = None , None , None

        if(Is_Single_Row):
            Value_Collection_Formats = Collection_Formats.get()
            Value_Collection_DPIs = int(Collection_DPIs.get())
            Value_Collection_Axis_x_Titles_For_Graphs = Collection_Axis_x_Titles_For_Graphs.get()
        else:
            Value_Collection_Formats , Value_Collection_DPIs , Value_Collection_Axis_x_Titles_For_Graphs = Get_Values_From_Widgets_When_There_Are_Multiple_Columns_Of_Data(Collection_Formats , Collection_DPIs , Collection_Axis_x_Titles_For_Graphs)

        List_Any_Subcheckbox_Checked = []

        if(Is_Single_Row):
            for category_graph_name in Collection_Subcheckboxes_With_Selected_Graphs.keys():
                Is_Any_Subchekbox_For_Category_Graph_Checked = Export_Graphs_Acoording_To_Subcheckbox_Value(Collection_Subcheckboxes_With_Selected_Graphs[category_graph_name] , Collection_Entry_Titles_For_Graphs[category_graph_name] , "" , Dictionary_Of_Generated_Figures[f"Figure_{category_graph_name}"] , Route_And_File_Name , Value_Collection_Formats , Value_Collection_DPIs , Value_Collection_Axis_x_Titles_For_Graphs)
                List_Any_Subcheckbox_Checked.append(Is_Any_Subchekbox_For_Category_Graph_Checked)
        else:
            for (variable_name , subcheckboxes_values_dict) , entry_titles_values_dict , figures_dict , img_format , dpi_graph , axis_x_title in zip(Collection_Subcheckboxes_With_Selected_Graphs.items() , Collection_Entry_Titles_For_Graphs.values() , Dictionary_Of_Generated_Figures.values() , Value_Collection_Formats.values() , Value_Collection_DPIs.values() , Value_Collection_Axis_x_Titles_For_Graphs.values()):
                for category_graph_name in subcheckboxes_values_dict.keys():
                    Is_Any_Subchekbox_For_Category_Graph_Checked = Export_Graphs_Acoording_To_Subcheckbox_Value(subcheckboxes_values_dict[category_graph_name] , entry_titles_values_dict[category_graph_name] , variable_name , figures_dict[f"Figure_{category_graph_name}"] , Route_And_File_Name , img_format , dpi_graph , axis_x_title)
                    List_Any_Subcheckbox_Checked.append(Is_Any_Subchekbox_For_Category_Graph_Checked)
        
        if(not any(List_Any_Subcheckbox_Checked)):
            raise Raise_Warning("Debe seleccionar al menos un grafico a exportar.")
        
    except Raise_Warning as e:
        messagebox.showwarning("Advertencia" , f"{e}")
    except Exception as e:
        messagebox.showerror("Error" , f"{e}")
    else:
        Reply = messagebox.askquestion("Success" , f"Las imagenes fueron exportadas con exito a\n{File_Path}\n¿Desea salir de la ventana de exportacion?")
        if(Reply == "yes"):
            Delete_Actual_Window(W_Show_Graph , W_Export_Graph , True)

def Export_Graphs_Acoording_To_Subcheckbox_Value(Subcheckboxes_Values , Entry_Titles_Values , Variable_Name , Figures_For_Category_Graph , Route_And_File_Name , Img_Format , DPI_Graph , Axis_x_Ttile):
    for (name_of_graph , subcheckbox_value) , entry_title_value , figure in zip(Subcheckboxes_Values.items() , Entry_Titles_Values.values() , Figures_For_Category_Graph.values()):
        if(subcheckbox_value.get()):
            Complete_Route_To_Export = Build_Full_Export_Route(Route_And_File_Name , name_of_graph , Variable_Name , Img_Format)
            
            before_axis_x_title = figure.axes[0]
            before_axis_x_title = before_axis_x_title.get_xlabel()

            figure.suptitle(entry_title_value.get() , y=0.99 , fontsize=16 , fontweight='bold')

            if(not "Pie" in name_of_graph):
                figure.axes[0].set_xlabel(Axis_x_Ttile , labelpad=8 , fontweight='bold')

            figure.savefig(Complete_Route_To_Export , dpi=DPI_Graph , bbox_inches='tight')

            if(entry_title_value.get()):
                figure.suptitle("")

            if(not "Pie" in name_of_graph):
                figure.axes[0].set_xlabel(before_axis_x_title , labelpad=8 , fontweight='bold')

    return any(subcheckbox_value.get() for subcheckbox_value in Subcheckboxes_Values.values())