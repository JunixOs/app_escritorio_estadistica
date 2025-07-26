import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Tools import Verify_Logs_Folder , Get_Log_Files_Names_And_Paths , Read_Content_In_Log_Files , Get_Metadata_Info_From_Log_Files , Delete_Log_Files_After_Certain_Time , Insert_Data_In_Log_File , Center_Window , Get_Resource_Path , Delete_Actual_Window , Get_Detailed_Info_About_Error , Read_Data_From_JSON , Save_New_Configurations_In_JSON_File
from Special_Tkinter_Widgets import Spinbox_With_Validation

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
        self.Log_Files_Names_And_Paths = Get_Log_Files_Names_And_Paths()

        if(not self.Log_Files_Names_And_Paths):
            Frame_Widget = Frame(self.Notebook_Logs , bg="#d0d0d0")
            Frame_Widget.grid_columnconfigure(0 , weight=1)
            Frame_Widget.grid_rowconfigure(0 , weight=1)
            Label_No_Info = ttk.Label(Frame_Widget , text="No hay registros para mostrar")
            Label_No_Info.grid(row=0 , column=0 , sticky="nsew")
            self.Notebook_Logs.add(Frame_Widget , text=f"Sin Registros")
        else:
            for log_file_name in self.Log_Files_Names_And_Paths:
                Frame_Widget = Frame(self.Notebook_Logs , bg="#d0d0d0")
                Frame_Widget.grid_columnconfigure(0 , weight=1)
                Frame_Widget.grid_columnconfigure(1 , weight=1)
                for row_idx in range(13):
                    Frame_Widget.grid_rowconfigure(row_idx , weight=1)

                self.Notebook_Logs.add(Frame_Widget , text=f"Registros en\n{log_file_name[0]}")
                self.Frames_Notebook_Collection[log_file_name[0]] = Frame_Widget

    def Update_Log_Content_In_Treeview(self , Log_File_Name):
        Metadata_Info_In_Log_File = Get_Metadata_Info_From_Log_Files(Log_File_Name)
        Content_In_Log_File = Read_Content_In_Log_Files(Log_File_Name)

        # self.Collection_Widgets[Log_File_Name]["Widget_Path"].config(text=f"Ruta del archivo: {self.Log_Files_Names_And_Paths[1]}")
        self.Collection_Widgets[Log_File_Name]["Widget_Size"].config(text=f"Tamaño del archivo: {Metadata_Info_In_Log_File[Log_File_Name]['Size']} bytes")
        self.Collection_Widgets[Log_File_Name]["Widget_Creation_Date"].config(text=f"Fecha de creacion: {Metadata_Info_In_Log_File[Log_File_Name]['Creation_Date']}")
        self.Collection_Widgets[Log_File_Name]["Widget_Last_Access"].config(text=f"Ultimo acceso: {Metadata_Info_In_Log_File[Log_File_Name]['Last_Access']}")
        self.Collection_Widgets[Log_File_Name]["Widget_Last_Modification"].config(text=f"Ultima modificacion: {Metadata_Info_In_Log_File[Log_File_Name]['Last_Modification']}")

        self.Collection_Widgets[Log_File_Name]["Widget_Log_File_Content"][1].delete(*self.Collection_Widgets[Log_File_Name]["Widget_Log_File_Content"][1].get_children())

        for text_line in Content_In_Log_File[Log_File_Name]:
            self.Collection_Widgets[Log_File_Name]["Widget_Log_File_Content"][1].insert("" , END , values=(text_line,))
        self.Collection_Widgets[Log_File_Name]["Widget_Log_File_Content"][1].yview_moveto(1.0)


    def Create_Widgets_For_Log_Files_Info(self):
        Metadata_Info_In_Log_Files = Get_Metadata_Info_From_Log_Files()
        Content_In_Log_Files = Read_Content_In_Log_Files()

        for (log_file_name , log_file_path) , content_in_log_file , metadata_info_in_log_file , frame_notebook in zip(self.Log_Files_Names_And_Paths , Content_In_Log_Files.values() , Metadata_Info_In_Log_Files.values() , self.Frames_Notebook_Collection.values()):
            Label_Log_File_Path = ttk.Label(frame_notebook , text=f"Ruta del archivo: {log_file_path}")
            Label_Log_File_Size = ttk.Label(frame_notebook , text=f"Tamaño del archivo: {metadata_info_in_log_file['Size']} bytes")
            Label_Log_File_Creation_Date = ttk.Label(frame_notebook , text=f"Fecha de creacion: {metadata_info_in_log_file['Creation_Date']}")
            Label_Log_File_Last_Access = ttk.Label(frame_notebook , text=f"Ultimo acceso: {metadata_info_in_log_file['Last_Access']}")
            Label_Log_File_Last_Modification = ttk.Label(frame_notebook , text=f"Ultima modificacion: {metadata_info_in_log_file['Last_Modification']}")

            Btn_Refresh_Log_File_Content = Button(frame_notebook , text="\u27f3" , font=("Segoe UI", 12) , bg="#d0d0d0" , command= lambda name=log_file_name: self.Update_Log_Content_In_Treeview(name))

            Frame_Treeview_Log_File_Content = ttk.Frame(frame_notebook)
            Frame_Treeview_Log_File_Content.rowconfigure(0 , weight=1)
            Frame_Treeview_Log_File_Content.columnconfigure(0 , weight=1)

            Treeview_Log_File_Content = ttk.Treeview(Frame_Treeview_Log_File_Content , columns=("1",) , show="headings")
            Treeview_Log_File_Content.heading("1" , text="Contenido del archivo de registro")
            Treeview_Log_File_Content.column("1" , anchor="w" , stretch=True)
            Treeview_Log_File_Content.delete(*Treeview_Log_File_Content.get_children())
            
            Scrollbar_y_Treeview_Log_File_Content = ttk.Scrollbar(Frame_Treeview_Log_File_Content , orient="vertical" , command=Treeview_Log_File_Content.yview)
            Treeview_Log_File_Content.configure(yscrollcommand=Scrollbar_y_Treeview_Log_File_Content.set)

            Treeview_Log_File_Content.grid(row=0 , column=0 , sticky="nsew")
            Scrollbar_y_Treeview_Log_File_Content.grid(row=0 , column=1 , sticky="ns")

            for text_line in content_in_log_file:
                Treeview_Log_File_Content.insert("" , END , values=(text_line,))

            Treeview_Log_File_Content.yview_moveto(1.0)

            self.Collection_Widgets[log_file_name] = {
                "Widget_Path": Label_Log_File_Path,
                "Widget_Button_Update": Btn_Refresh_Log_File_Content,
                "Widget_Size": Label_Log_File_Size,
                "Widget_Creation_Date": Label_Log_File_Creation_Date,
                "Widget_Last_Access": Label_Log_File_Last_Access,
                "Widget_Last_Modification": Label_Log_File_Last_Modification,
                "Widget_Log_File_Content": [Frame_Treeview_Log_File_Content , Treeview_Log_File_Content , Scrollbar_y_Treeview_Log_File_Content],
            }

    def Display_Widgets_For_Log_Files_Info(self):
        # 6 rows widgets labels and 7 rows widget treeview, total 13 rows
        for collection_widgets in self.Collection_Widgets.values():
            collection_widgets["Widget_Path"].grid(row=0 , column=0 , columnspan=2 , padx=(5,5) , pady=(5,0) , sticky="ew")

            collection_widgets["Widget_Size"].grid(row=1 , column=0 , columnspan=2 , padx=(5,5) , pady=(5,0) , sticky="ew")
            collection_widgets["Widget_Creation_Date"].grid(row=2 , column=0 , columnspan=2 , padx=(5,5) , pady=(5,0) , sticky="ew")
            collection_widgets["Widget_Last_Access"].grid(row=3 , column=0 , columnspan=2 , padx=(5,5) , pady=(5,0) , sticky="ew")
            collection_widgets["Widget_Last_Modification"].grid(row=4 , column=0 , padx=(5,5) , pady=(5,0) , sticky="ew")

            collection_widgets["Widget_Button_Update"].grid(row=4 , column=1 , padx=(5,5) , pady=(5,0) , sticky="w")
            collection_widgets["Widget_Log_File_Content"][0].grid(row=5 , column=0 , rowspan=9 , columnspan=2 , padx=(5,5) , pady=(0,0) , sticky="nsew")

        self.Notebook_Logs.grid(row=0 , column=0 , sticky="nsew")

def Create_Window_Config_Logs_Settings(W_View_Logs):
    JSON_Settings_Data = Read_Data_From_JSON("logs_settings")

    W_Config_Logs_Settings = Toplevel(W_View_Logs)
    Center_Window(W_Config_Logs_Settings , 500 , 300)

    W_Config_Logs_Settings.title("Configuracion de registros")
    Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))
    W_Config_Logs_Settings.iconphoto(False , Icon)
    W_Config_Logs_Settings.grab_set()
    W_Config_Logs_Settings.lift()
    W_Config_Logs_Settings.protocol("WM_DELETE_WINDOW" , lambda: Delete_Actual_Window(W_View_Logs , W_Config_Logs_Settings , False , lambda: Save_New_Configurations_In_JSON_File("logs_settings" , delete_files_after_certain_time=Days_Until_Delete_Register.get())))

    W_Config_Logs_Settings.resizable(False , False)

    for idx_row in range(6):
        W_Config_Logs_Settings.rowconfigure(idx_row , weight=1)
    for idx_col in range(2):
        W_Config_Logs_Settings.columnconfigure(idx_col , weight=1)

    Days_Until_Delete_Register = IntVar(W_Config_Logs_Settings)
    Days_Until_Delete_Register.set(JSON_Settings_Data["delete_files_after_certain_time"])

    Text_Spinbox_Config_Days_Until_Delete_Register = Label(W_Config_Logs_Settings , text="Dias de vida de un registro:" , font=("Times new Roman" , 13))
    Text_Spinbox_Config_Days_Until_Delete_Register.grid(row=0 , column=0 , sticky="w" , padx=(10 , 0) , pady=(5 , 5))
    Spinbox_Config_Days_Until_Delete_Register = Spinbox_With_Validation(
        W_Config_Logs_Settings , 
        21 , 
        1 , 
        1 , 
        Days_Until_Delete_Register , 
        "grid" , 
        None , 
        row=0 , column=1 , sticky="ew" , pady=(5 , 5)
    )

    W_Config_Logs_Settings.mainloop()


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
            Delete_Actual_Window(Father_Window , W_View_Logs , True)

        Btn_Logs_Settings = Button(W_View_Logs , text="\u2699" , font=("Segoe UI Emoji", 9) , bg="#d0d0d0" , command= lambda: Create_Window_Config_Logs_Settings(W_View_Logs))
        Btn_Logs_Settings.place(x=8 , y=293)


        W_View_Logs.mainloop()

if(__name__ == "__main__"):
    Create_Window_View_Logs()