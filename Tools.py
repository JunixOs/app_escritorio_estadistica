from Exceptions.Exception_Warning import Raise_JSON_Settings_Error

import os
import sys
import json
import psutil
from datetime import datetime
import time
import traceback
from typing import Literal

# ==================================================================== Miscelaneous Tools ====================================================================
def Get_Project_Root(Ignore_Compiler_Path_System):
    Script_Dir = os.path.dirname(os.path.realpath(__file__))
    Project_Root = os.path.abspath(os.path.join(Script_Dir))

    if(Ignore_Compiler_Path_System):
        return Project_Root
    
    if(getattr(sys , 'frozen' , False)):
        return sys._MEIPASS
    else:
        return Project_Root

def Get_Resource_Path(Resource_Name , Ignore_Compiler_Path_System=False):
    Project_Root = Get_Project_Root(Ignore_Compiler_Path_System)

    Resource_Name = Resource_Name.strip("/\\")

    if("/" in Resource_Name):
        Resource_Name = Resource_Name.split("/")
        Resource_Path = os.path.join(Project_Root , *Resource_Name)
    else:
        Resource_Path = os.path.join(Project_Root , Resource_Name)

    return Resource_Path

def Get_RAM_Memory_In_Device():
    Memory_RAM = psutil.virtual_memory()

    return {
        "Total": Memory_RAM.total / (1024 ** 3),
        "In Use": Memory_RAM.used / (1024 ** 3),
        "Available": Memory_RAM.available / (1024 ** 3),
        "Pecentaje_Use": Memory_RAM.percent,
    }

def Get_Version():
    Version = "v3.0.0"

    return Version

def Get_Detailed_Info_About_Error():
    Exception_Type , Value , tb = sys.exc_info()
    File_Name = tb.tb_frame.f_code.co_filename
    Line_Error = tb.tb_lineno
    Function_Error = tb.tb_frame.f_code.co_name

    Extended_Massage_Error = f"""
        Tipo de Excepcion: {Exception_Type.__name__}
        Mensaje: {Value}
        Archivo: {File_Name}
        Funcion: {Function_Error}
        Linea de error: {Line_Error}
    """
    return Extended_Massage_Error

# ==================================================================== Tkinter Tools ====================================================================
def Get_Window_Level(Window):
    Level = 0
    Actual = Window
    while hasattr(Actual, 'master') and Actual.master is not None:
        Actual = Actual.master
        Level += 1

    return Level

def Delete_Actual_Window(Father_Window=None , Children_Window=None , Display_Father_Window=False , Function=None):
    if(Father_Window and Children_Window):
        for widget in Children_Window.winfo_children():
            widget.destroy()
        
        try:
            Children_Window.grab_release()
        except:
            pass

        Children_Window.destroy()
        if(Display_Father_Window):
            Father_Window.state(newstate="normal")
        
        Level_Father_Window = Get_Window_Level(Father_Window)
        if(Level_Father_Window > 1):
            try:
                Father_Window.grab_set()
            except:
                pass
        
        if(Function and callable(Function)):
            Function()

        Father_Window.lift()

def Center_Window(Window_To_Center , Window_Width , Window_Height):
    try:
        Screen_Width = Window_To_Center.winfo_screenwidth()
        Screen_Height = Window_To_Center.winfo_screenheight()

        x = (Screen_Width - Window_Width) // 2
        y = (Screen_Height - Window_Height) // 2

        Window_To_Center.geometry(f"{Window_Width}x{Window_Height}+{x}+{y}")
    except Exception:
        Window_To_Center.geometry(f"{Window_Width}x{Window_Height}")

def Load_Global_Styles(Global_ttk_Style):
    """ Sirve para cargar los estilos de todos los widgets ttk """
    """ ****************************************** Widget Label ****************************************** """
    Global_ttk_Style.configure("TLabel",
                    font=("Times New Roman", 13),
                    background="#d0d0d0",
                    foreground="#333")

    """ ****************************************** Widget Entry ****************************************** """
    Global_ttk_Style.configure("TEntry",
                    font=("Times New Roman", 10),
                    padding=5,
                    relief="flat")

    """ ****************************************** Widget Button ****************************************** """
    Global_ttk_Style.configure("TButton",
                    font=("Times New Roman", 10, "bold"),
                    padding=6,
                    foreground="#fff",
                    background="#0078D7")
    Global_ttk_Style.map("TButton",
            background=[("active", "#005A9E")],
            relief=[("pressed", "sunken")])

    """ ****************************************** Widget Checkbutton ****************************************** """
    Global_ttk_Style.configure("TCheckbutton",
                    font=("Times New Roman", 10),
                    padding=5)

    """ ****************************************** Widget Combobox ****************************************** """
    Global_ttk_Style.configure("TCombobox",
                    font=("Times New Roman", 10),
                    padding=1)

    """ ****************************************** Widget Notebook ****************************************** """
    Global_ttk_Style.configure("TNotebook",
                    tabposition='n')

    Global_ttk_Style.configure("TNotebook.Tab",
                    font=("Times New Roman", 10),
                    padding=[10, 5],
                    background="#f0f0f0")

    Global_ttk_Style.map("TNotebook.Tab",
            background=[("selected", "#dcdcdc")],
            expand=[("selected", [1, 1, 1, 0])])

    """ ****************************************** Widget Treeview ****************************************** """
    Global_ttk_Style.configure("Treeview",
                    font=("Times New Roman", 10),
                    rowheight=28,
                    padding=5,
                    relief="flat",
                    background="#ffffff",
                    fieldbackground="#ffffff",
                    foreground="#333")

    Global_ttk_Style.map("Treeview",
            background=[("selected", "#0078D7")],
            foreground=[("selected", "#ffffff")])

    Global_ttk_Style.configure("Treeview.Heading",
                    font=("Times New Roman", 10, "bold"),
                    background="#f0f0f0",
                    foreground="#333",
                    relief="flat")

    Global_ttk_Style.map("Treeview.Heading",
            background=[("active", "#e0e0e0")])

    """ ****************************************** Widget Scrollbar ****************************************** """
    Global_ttk_Style.configure("Vertical.TScrollbar",
        gripcount=0,
        borderwidth=0,
        relief="flat",
        background="#d0d0d0",
        darkcolor="#d0d0d0",
        lightcolor="#d0d0d0",
        troughcolor="#f0f0f0",
        arrowcolor="#666",
        arrowsize=12
    )

    Global_ttk_Style.configure("Horizontal.TScrollbar",
        gripcount=0,
        borderwidth=0,
        relief="flat",
        background="#d0d0d0",
        darkcolor="#d0d0d0",
        lightcolor="#d0d0d0",
        troughcolor="#f0f0f0",
        arrowcolor="#666",
        arrowsize=12
    )

    # Opcional: efecto de hover y presionado
    Global_ttk_Style.map("Vertical.TScrollbar",
        background=[("active", "#c0c0c0"), ("pressed", "#a0a0a0")],
        arrowcolor=[("active", "#333"), ("pressed", "#222")]
    )

    Global_ttk_Style.map("Horizontal.TScrollbar",
        background=[("active", "#c0c0c0"), ("pressed", "#a0a0a0")],
        arrowcolor=[("active", "#333"), ("pressed", "#222")]
    )

    """ ****************************************** Widget Progressbar ****************************************** """
    Global_ttk_Style.configure("TProgressbar",
                    troughcolor="#f0f0f0",
                    background="#0078D7", 
                    thickness=20,   
                    bordercolor="#f0f0f0",
                    lightcolor="#0078D7",
                    darkcolor="#0078D7")

# ==================================================================== Threads Tools ====================================================================
def Check_Threads_Alive(Threads_List , Root_Window , Class_Progress_Bar , On_Finish=None):
    # Verifica si todos los hilos terminaron
    if all(not t.is_alive() for t in Threads_List):
        Class_Progress_Bar.Close_Progress_Bar()
        if(On_Finish):
            Root_Window.after(0 , On_Finish)
    else:
        Root_Window.after(500, Check_Threads_Alive, Threads_List, Root_Window , Class_Progress_Bar , On_Finish)

# ==================================================================== Log Files Tools ====================================================================
def Verify_Logs_Folder():
    Path_Logs_Folder = Get_Resource_Path("Logs" , True)
    if(not os.path.exists(Path_Logs_Folder)):
        os.mkdir(Path_Logs_Folder)

def Get_Log_Files_Names_And_Paths():
    Path_Logs_Folder = Get_Resource_Path("Logs" , True)
    Log_Files_Names_And_Paths = [[file_name , Get_Resource_Path(f"Logs/{file_name}")] for file_name in os.listdir(Path_Logs_Folder) if os.path.isfile(os.path.join(Path_Logs_Folder, file_name))]
    
    return Log_Files_Names_And_Paths

def Get_Log_Files_Names_Or_Paths(Resource_To_Get: Literal["names" , "paths"]):
    Path_Logs_Folder = Get_Resource_Path("Logs" , True)
    match(Resource_To_Get):
        case "names":
            Log_Files_Names = [file_name for file_name in os.listdir(Path_Logs_Folder) if os.path.isfile(os.path.join(Path_Logs_Folder, file_name))]
            return Log_Files_Names
        case "paths":
            Log_Files_Paths = [Get_Resource_Path(f"Logs/{file_name}") for file_name in os.listdir(Path_Logs_Folder) if os.path.isfile(os.path.join(Path_Logs_Folder, file_name))]
            return Log_Files_Paths

def Get_Metadata_Info_From_Log_Files(Specific_Log_File_Name="" , Get_All_Metadata_Info=False):
    Verify_Logs_Folder()

    Log_Files_Names_And_Paths = Get_Log_Files_Names_And_Paths()
    Log_Files_Netadata_Info = {}

    for (log_file_name , log_file_path) in Log_Files_Names_And_Paths:
        if(Specific_Log_File_Name and log_file_name != Specific_Log_File_Name):
            continue

        metadata_info = os.stat(log_file_path)
        if(Get_All_Metadata_Info):
            Log_Files_Netadata_Info[log_file_name] = metadata_info
        else:
            Log_Files_Netadata_Info[log_file_name] = {
                "Size": metadata_info.st_size,
                "Last_Access": time.ctime(metadata_info.st_atime),
                "Last_Modification": time.ctime(metadata_info.st_mtime),
                "Creation_Date": time.ctime(metadata_info.st_birthtime),
            }
    
    return Log_Files_Netadata_Info

def Verify_Log_File_Exists_In_Logs_Folder():
    Today_Date = datetime.now().strftime("%d-%m-%Y")
    Name_Of_Log_File = Today_Date + " - log.txt"

    Log_Files_Names = Get_Log_Files_Names_Or_Paths("names")

    return True if Name_Of_Log_File in Log_Files_Names else False

def Insert_Data_In_Log_File(Event_Message , Event_Type , Event_Section , Detailed_Message_Error=""):
    Verify_Logs_Folder()

    Today_Date = datetime.now().strftime("%d-%m-%Y")
    Full_Path_Of_Log_File = Get_Resource_Path(f"Logs/{Today_Date} - log.txt" , True)

    Actual_Time = datetime.now().strftime("%H-%M-%S")

    Log_File_Exists = Verify_Log_File_Exists_In_Logs_Folder()

    if(not Log_File_Exists):
        Log_File = open(Full_Path_Of_Log_File , "w")
    else:
        Log_File = open(Full_Path_Of_Log_File , "a")

    if(Detailed_Message_Error):
        Log_File.write(f"({Actual_Time} - [{Event_Type}] - [Seccion: {Event_Section}]) > {Event_Message}\n===>Mensaje detallado del evento{Detailed_Message_Error}")
    else:
        Log_File.write(f"({Actual_Time} - [{Event_Type}] - [Seccion: {Event_Section}]) > {Event_Message}\n")

    Log_File.close()

def Read_Content_In_Log_Files(Specific_Log_File_Name=""):
    Verify_Logs_Folder()
    Log_File_Exists = Verify_Log_File_Exists_In_Logs_Folder()

    if(not Log_File_Exists):
        return ""

    Log_Files_Names_And_Paths = Get_Log_Files_Names_And_Paths()
    Content_In_Log_Files = {}

    for (log_file_name , log_file_path) in Log_Files_Names_And_Paths:
        if(Specific_Log_File_Name and log_file_name != Specific_Log_File_Name):
            continue

        log_file = open(log_file_path , "r" , encoding="utf-8")
        Content_In_Log_Files[log_file_name] = log_file.readlines()
        log_file.close()

    return Content_In_Log_Files

def Delete_Log_Files_After_Certain_Time():
    Actual_Date = time.time()

    Logs_Settings = Read_Data_From_JSON("logs_settings")
    Metadata_Info_Log_Files = Get_Metadata_Info_From_Log_Files("" , True)
    Log_Files_Paths = Get_Log_Files_Names_Or_Paths("paths")

    Days_Until_Delete = Logs_Settings["delete_files_after_certain_time"]

    for metadata_info_log_file , log_file_path in zip(Metadata_Info_Log_Files.values() , Log_Files_Paths):
        if((Actual_Date - metadata_info_log_file.st_birthtime) / (60 * 60 * 24) >= Days_Until_Delete):
            os.remove(log_file_path)

# ==================================================================== JSON Settings Tools ====================================================================
def Get_Number_Of_Util_Threads_In_Device(Percentaje_Of_Use = 0.5):
    Max_Trheads = os.cpu_count()
    if(Percentaje_Of_Use > 1):
        Percentaje_Of_Use /= 100
    Max_Trheads = round(Max_Trheads * Percentaje_Of_Use)
    return Max_Trheads

def Get_Default_Settings_Param_In_JSON():
    Import_Excel_Settings = {
        "void_tolerance": 2,
        "maximun_rows_to_display_in_preview": 100,
        "import_matrix_data": False,
    }

    Calc_Frecuences_Table_Settings = {
        "round_up_amplitude": True,
    }

    Logs_Settings = {
        "delete_files_after_certain_time": 6,    # En dias
    }

    return {
        "import_excel_settings": [
            Get_Resource_Path("Config/import_excel_settings.json") ,
            Import_Excel_Settings ,
        ],
        "calc_frecuences_table_settings": [
            Get_Resource_Path("Config/calc_frecuences_table_settings.json") ,
            Calc_Frecuences_Table_Settings ,
        ],
        "logs_settings": [
            Get_Resource_Path("Config/logs_settings.json"),
            Logs_Settings,
        ]
    }

def Verify_JSON_Files():
    Default_Settings_Data = Get_Default_Settings_Param_In_JSON()

    for default_settings_data in Default_Settings_Data.values():
        if(not os.path.exists(default_settings_data[0])):
            with open(default_settings_data[0] , "w") as json_file:
                json.dump(default_settings_data[1] , json_file , indent=4)
        else:
            if(os.path.getsize(default_settings_data[0]) == 0):
                with open(default_settings_data[0] , "w") as json_file:
                    json.dump(default_settings_data[1] , json_file , indent=4)
            else:
                with open(default_settings_data[0] , "r") as json_file:
                    Data_From_JSON = json.load(json_file)
                Missing_Keys = set(default_settings_data[1].keys()) - Data_From_JSON.keys()
                Extra_Keys = Data_From_JSON.keys() - set(default_settings_data[1].keys())
                if(Missing_Keys or Extra_Keys):
                    with open(default_settings_data[0] , "w") as json_file:
                        json.dump(default_settings_data[1] , json_file , indent=4)

def Verify_Configurations_Folder():
    Path_File = Get_Resource_Path("Config")
    if(not os.path.exists(Path_File)):
        os.mkdir(Path_File)

    Verify_JSON_Files()

def Validate_Data_From_GUI(JSON_Settings_Name , New_Settings):
    Default_Settings_Data = Get_Default_Settings_Param_In_JSON()

    match(JSON_Settings_Name):
        case "import_excel_settings":
            if(not New_Settings["void_tolerance"]):
                New_Settings["void_tolerance"] = Default_Settings_Data[JSON_Settings_Name][1]["void_tolerance"]
            if(not New_Settings["maximun_rows_to_display_in_preview"]):
                New_Settings["maximun_rows_to_display_in_preview"] = Default_Settings_Data[JSON_Settings_Name][1]["maximun_rows_to_display_in_preview"]
        case "calc_frecuences_table_settings":
            pass
        case "logs_settings":
            if(not New_Settings["delete_files_after_certain_time"]):
                New_Settings["delete_files_after_certain_time"] = Default_Settings_Data[JSON_Settings_Name][1]["delete_files_after_certain_time"]
    return New_Settings

def Save_New_Configurations_In_JSON_File(JSON_Settings_Name , **New_Settings):
    Verify_Configurations_Folder()

    New_Settings = Validate_Data_From_GUI(JSON_Settings_Name , New_Settings)

    JSON_Path = Get_Resource_Path(f"Config/{JSON_Settings_Name}.json")
    with open(JSON_Path , "r") as json_file:
        JSON_Settings_Data = json.load(json_file)

    for json_key in JSON_Settings_Data.keys():
        if(json_key in New_Settings):
            JSON_Settings_Data[json_key] = New_Settings[json_key]
    
    with open(JSON_Path , "w") as json_file:
        json.dump(JSON_Settings_Data , json_file , indent=4)

def Validate_Data_From_JSON(JSON_Settings_Name , JSON_Settings_Data):
    match(JSON_Settings_Name):
        case "import_excel_settings":
            if(
                not (isinstance(JSON_Settings_Data["void_tolerance"] , int) and 
                isinstance(JSON_Settings_Data["maximun_rows_to_display_in_preview"] , int) and
                isinstance(JSON_Settings_Data["import_matrix_data"] , bool))
                ):
                raise Raise_JSON_Settings_Error("Error con los tipos de datos del JSON")
        case "calc_frecuences_table_settings":
            if(not isinstance(JSON_Settings_Data["round_up_amplitude"] , bool)):
                raise Raise_JSON_Settings_Error("Error con los tipos de datos del JSON")
            
        case "logs_settings":
            if(not isinstance(JSON_Settings_Data["delete_files_after_certain_time"] , int)):
                raise Raise_JSON_Settings_Error("Error con los tipos de datos del JSON")

def Read_Data_From_JSON(JSON_Settings_Name):
    Verify_Configurations_Folder()
    JSON_Path = Get_Resource_Path(f"Config/{JSON_Settings_Name}.json")

    try:
        with open(JSON_Path , "r") as json_file:
            JSON_Settings_Data = json.load(json_file)

        Validate_Data_From_JSON(JSON_Settings_Name, JSON_Settings_Data)
    except Raise_JSON_Settings_Error:
        Default_Settings_Data = Get_Default_Settings_Param_In_JSON()
        with open(JSON_Path , "w") as json_file:
            json.dump(Default_Settings_Data[JSON_Settings_Name][1] , json_file , indent=4)

        with open(JSON_Path , "r") as json_file:
            JSON_Settings_Data = json.load(json_file)

    return JSON_Settings_Data

if(__name__ == "__main__"):
    # strip() elimina caracteres de los lados (por defecto solo espacios pero puedes especificar)
    # version = "!!!varsion!!!"
    # print(versiion.strip("!"))  ---> version

    # lstrip() solo elimina caracteres del lado izquierdo, por defecto espacios en blanco
    # version = "v1.2.3"
    # print(version.lstrip("v"))  ---> 1.2.3
    
    # print(Get_Number_Of_Util_Threads_In_Device())
    print(Get_Version().strip().lstrip("v"))