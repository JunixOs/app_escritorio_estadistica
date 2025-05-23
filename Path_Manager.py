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

if(__name__ == "__main__"):
    print(Get_Project_Root())
    print(Get_Version())