import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Tools import Verify_Logs_Folder , Get_Log_Files_Names , Read_Content_In_Log_Files , Get_Metadata_Info_From_Log_Files , Delete_Log_Files_After_Certain_Time , Insert_Data_In_Log_File , Center_Window , Get_Resource_Path , Delete_Actual_Window , Get_Detailed_Info_About_Error

from tkinter import *
from tkinter import ttk , messagebox

class Notebook_For_Logs:
    def __init__(self , W_View_Logs):
        self.Style_For_Notebook = ttk.Style()

        # Cambiar el color del fondo del notebook
        self.Style_For_Notebook.configure("Custom.TNotebook", background="#9DAEC6", borderwidth=0)
        self.Style_For_Notebook.configure("Custom.TNotebook.Tab", background="#9DAEC6", padding=10 , borderwidth=0)

        # Color de la pestaña seleccionada
        self.Style_For_Notebook.map("Custom.TNotebook.Tab",
            background=[("selected", "#ACB7C6")],
            foreground=[("selected", "black")],
            expand=[("selected", [1, 1, 1, 0])]
        )

        self.Style_For_Notebook.layout("Custom.TNotebook.Tab", [
            ('Notebook.tab', {'sticky': 'nswe', 'children': [
                ('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children': [
                    ('Notebook.label', {'side': 'top', 'sticky': ''})
                ]})
            ]})
        ])

        self.W_View_Logs = W_View_Logs
        self.Notebook_Logs = ttk.Notebook(self.W_View_Logs , style="Custom.TNotebook")
        self.Collection_Widgets = {}

        self.Frames_Notebook_Collection = {}
        self.Log_Files_Names = Get_Log_Files_Names()
        self.Content_In_Log_Files = Read_Content_In_Log_Files()
        self.Metadata_Info_In_Log_Files = Get_Metadata_Info_From_Log_Files()

        if(not self.Log_Files_Names):
            Frame_Widget = Frame(self.Notebook_Logs , bg="#d0d0d0")
            Frame_Widget.grid_columnconfigure(0 , weight=1)
            Frame_Widget.grid_rowconfigure(0 , weight=1)
            Label_No_Info = ttk.Label(Frame_Widget , text="No hay registros para mostrar")
            Label_No_Info.grid(row=0 , column=0 , sticky="nsew")
            self.Notebook_Logs.add(Frame_Widget , text=f"Sin Registros")
        else:
            for log_file_name in self.Log_Files_Names:
                Frame_Widget = Frame(self.Notebook_Logs , bg="#d0d0d0")
                Frame_Widget.grid_columnconfigure(0 , weight=1)
                for row_idx in range(13):
                    Frame_Widget.grid_rowconfigure(row_idx , weight=1)

                self.Notebook_Logs.add(Frame_Widget , text=f"Registros en\n{log_file_name[0]}")
                self.Frames_Notebook_Collection[log_file_name[0]] = Frame_Widget

    def Create_Widgets_For_Log_Files_Info(self):
        for log_file_name in self.Log_Files_Names:
                Label_Log_File_Path = ttk.Label(self.Frames_Notebook_Collection[log_file_name[0]] , text=f"Ruta del archivo: {log_file_name[1]}")
                Label_Log_File_Size = ttk.Label(self.Frames_Notebook_Collection[log_file_name[0]] , text=f"Tamaño del archivo: {self.Metadata_Info_In_Log_Files[log_file_name[0]]['Size']} bytes")
                Label_Log_File_Creation_Date = ttk.Label(self.Frames_Notebook_Collection[log_file_name[0]] , text=f"Fecha de creacion: {self.Metadata_Info_In_Log_Files[log_file_name[0]]['Creation_Date']}")
                Label_Log_File_Last_Access = ttk.Label(self.Frames_Notebook_Collection[log_file_name[0]]  , text=f"Ultimo acceso: {self.Metadata_Info_In_Log_Files[log_file_name[0]]['Last_Access']}")
                Label_Log_File_Last_Modification = ttk.Label(self.Frames_Notebook_Collection[log_file_name[0]] , text=f"Ultima modificacion: {self.Metadata_Info_In_Log_Files[log_file_name[0]]['Last_Modification']}")

                Treeview_Log_File_Content = ttk.Treeview(self.Frames_Notebook_Collection[log_file_name[0]] , columns=("1",) , show="headings")
                Treeview_Log_File_Content.heading("1" , text="Contenido del archivo de registro")
                Treeview_Log_File_Content.column("1" , anchor="w" , stretch=True)
                Treeview_Log_File_Content.delete(*Treeview_Log_File_Content.get_children())
                for i , text_line in enumerate(self.Content_In_Log_Files[log_file_name[0]] , start=1):
                    Treeview_Log_File_Content.insert("" , END , values=(text_line,))

                self.Collection_Widgets[log_file_name[0]] = {
                    "Widget_Path": Label_Log_File_Path,
                    "Widget_Size": Label_Log_File_Size,
                    "Widget_Creation_Date": Label_Log_File_Creation_Date,
                    "Widget_Last_Access": Label_Log_File_Last_Access,
                    "Widget_Last_Modification": Label_Log_File_Last_Modification,
                    "Widget_Log_File_Content": Treeview_Log_File_Content,
                }

    def Display_Widgets_For_Log_Files_Info(self):
        # 6 rows widgets labels and 7 rows widget treeview, total 13 rows
        for collection_widgets in self.Collection_Widgets.values():
            for idx_row , widget in enumerate(collection_widgets.values()):
                if(idx_row == len(collection_widgets) - 1):
                    widget.grid(row=idx_row*2 , column=0 , rowspan=7 , padx=(5,5) , pady=(0,0) , sticky="nsew")
                else:
                    widget.grid(row=idx_row*2 , column=0 , padx=(5,5) , pady=(5,0) , sticky="ew")

        self.Notebook_Logs.grid(row=0 , column=0 , sticky="nsew")

def Create_Window_Config_Logs_Settings(W_View_Logs):
    pass

def Create_Window_View_Logs(Father_Window=None):
    try:
        Verify_Logs_Folder()
        Delete_Log_Files_After_Certain_Time()
    except Exception:
        messagebox.showerror("Error" , "Hubo un error al verificar la carpeta de registros.")
    else:
        if(Father_Window):
            Father_Window.state(newstate="withdraw")
            W_View_Logs = Toplevel(Father_Window)
            Center_Window(W_View_Logs , 1100 , 750)
            W_View_Logs.protocol("WM_DELETE_WINDOW" , lambda: Delete_Actual_Window(Father_Window , W_View_Logs , True))
        else:
            W_View_Logs = Tk()
            Center_Window(W_View_Logs , 1100 , 750)

        W_View_Logs.lift()
        W_View_Logs.title("Ver Archivos de Registro")
        Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
        W_View_Logs.iconphoto(False , Icon)
        W_View_Logs.resizable(False , False)

        W_View_Logs.rowconfigure(0 , weight=1)
        W_View_Logs.columnconfigure(0 , weight=1)

        try:
            Notebook_W_View_Logs = Notebook_For_Logs(W_View_Logs)

            Notebook_W_View_Logs.Create_Widgets_For_Log_Files_Info()
            Notebook_W_View_Logs.Display_Widgets_For_Log_Files_Info()
        except Exception:
            messagebox.showerror("Error" , "Hubo un error al generar los widgets")
            Detailed_Info_About_Error = Get_Detailed_Info_About_Error()

            Insert_Data_In_Log_File("Hubo un error al generar los widgets" , "Error" , "Visualizar archivos de registro" , Detailed_Info_About_Error)

        W_View_Logs.mainloop()

if(__name__ == "__main__"):
    Create_Window_View_Logs()