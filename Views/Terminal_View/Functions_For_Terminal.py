import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..' , '..')))

import platform
import subprocess
import psutil
import shutil

SCRIPT_TERMINAL_VIEW_NAME = "Main.py"
SCRIPT_TKINTER_VIEW_NAME = "Main_Window.py"

from Path_Manager import Get_Project_Root
def Clear_Terminal():
    os.system('cls' if os.name == "nt" else 'clear')

def Get_Terminal_Dimensions():
    try:
        Terminal_Size = shutil.get_terminal_size(fallback=(80 , 24))
        print(f"{'Wazaa':=^{Terminal_Size.columns}}")
        return Terminal_Size.columns , Terminal_Size.lines
    except Exception as e:
        print(f"Ocurrio un error al obtener el tamaño de la terminal {e}")
        return 80

def Check_If_Program_Running():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['cmdline'] and SCRIPT_TERMINAL_VIEW_NAME in ' '.join(proc.info['cmdline']):
                return "Running Terminal View"
            if proc.info['cmdline'] and SCRIPT_TKINTER_VIEW_NAME in ' '.join(proc.info['cmdline']):
                return "Running Tkinter View"

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return "No Running"

def Create_Terminal_With_Program():
    System_Name = platform.system()

    Program_Is_Running = Check_If_Program_Running()

    Script_Terminal_View_Root = os.path.join(Get_Project_Root() , SCRIPT_TERMINAL_VIEW_NAME)

    match(Program_Is_Running):
        case "No running":
            if System_Name == 'Windows':
                # Abrir una nueva terminal de Windows (cmd) y ejecutar el script
                subprocess.Popen(f'start cmd /k "python {Script_Terminal_View_Root}"', shell=True)

            elif System_Name == 'Linux':
                # Puedes cambiar gnome-terminal por otro si usas XFCE, KDE, etc.
                subprocess.Popen([
                    'gnome-terminal', '--', 'bash', '-c', f'python3 "{Script_Terminal_View_Root}"; exec bash'
                ])
            else:
                print(f"Sistema operativo no soportado: {System_Name}")
        case "Running Terminal View":
            pass

if(__name__ == "__main__"):
    print(Get_Terminal_Dimensions())