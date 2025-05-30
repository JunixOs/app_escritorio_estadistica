import os
import json
from Exceptions.Exception_Warning import Raise_JSON_Settings_Error

# ==================================================================== Miscelaneous Tools ====================================================================
def Get_Project_Root():
    Script_Dir = os.path.dirname(os.path.realpath(__file__))
    Project_Root = os.path.abspath(os.path.join(Script_Dir))

    return Project_Root

def Get_Resource_Path(Resource_Name):
    Project_Root = Get_Project_Root()

    Resource_Path = os.path.join(Project_Root , Resource_Name)

    return Resource_Path

def Get_Version():
    Version = "v1.0.1"

    return Version


# ==================================================================== Tkinter Tools ====================================================================
def Get_Window_Level(Window):
    Level = 0
    Actual = Window
    while hasattr(Actual, 'master') and Actual.master is not None:
        Actual = Actual.master
        Level += 1

    return Level

def Delete_Actual_Window(Father_Window=None , Children_Window=None , Display_Father_Window=False):
    if(Father_Window and Children_Window):
        for widget in Children_Window.winfo_children():
            widget.destroy()
        Children_Window.grab_release()
        Children_Window.quit()
        Children_Window.destroy()
        Level_Father_Window = Get_Window_Level(Father_Window)
        if(Display_Father_Window):
            Father_Window.state(newstate="Normal")
        
        if(Level_Father_Window > 1):
            Father_Window.grab_set()
        
        Father_Window.lift()


# ==================================================================== JSON Settings Tools ====================================================================
def Get_Default_Settings_Param_In_JSON():
    Import_Excel_Settings = {
        "void_tolerance": 2,
        "maximun_rows_to_display_in_preview": 100,
        "import_matrix_data": False,
    }

    Calc_Frecuences_Table_Settings = {
        "round_up_amplitude": True,
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
    }

def Verify_JSON_Files():
    Default_Settings_Data = Get_Default_Settings_Param_In_JSON()

    for default_settings_data in Default_Settings_Data.values():
        if(not os.path.exists(default_settings_data[0])):
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
    print(Get_Project_Root())
    print(Get_Version())