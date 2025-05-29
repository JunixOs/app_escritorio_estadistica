import os

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

def Get_Window_Level(Window):
    Level = 0
    Actual = Window
    while hasattr(Actual, 'master') and Actual.master is not None:
        Actual = Actual.master
        Level += 1

    print(Level)
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

if(__name__ == "__main__"):
    print(Get_Project_Root())
    print(Get_Version())