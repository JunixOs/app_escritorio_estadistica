from Exceptions.Exception_Warning import Raise_Warning
from Tools import Insert_Data_In_Log_File , Get_Detailed_Info_About_Error

from tkinter import *
from tkinter import ttk , messagebox
from typing import Literal


# ==================================================================== Tabla ====================================================================
class Table_Widget:
    def __init__(self , Father_Window , Number_Of_Table_Columns: int , Titles_For_Heading_Table_Columns: list[str]):
        self.Number_Of_Table_Columns = Number_Of_Table_Columns
        self.Titles_For_Heading_Table_Columns = Titles_For_Heading_Table_Columns

        self.Father_Frame_Of_Table = ttk.Frame(Father_Window)
        self.Father_Frame_Of_Table.rowconfigure(0 , weight=1)
        self.Father_Frame_Of_Table.columnconfigure(0 , weight=1)

        Columns_IDs = [str(idx) for idx in range(1 , Number_Of_Table_Columns + 1)]
        self.Treeview_Widget = ttk.Treeview(self.Father_Frame_Of_Table , columns=tuple(Columns_IDs) , show="headings")
        for col_idx , title_column in zip(Columns_IDs , Titles_For_Heading_Table_Columns):
            self.Treeview_Widget.heading(col_idx , text=title_column)
            self.Treeview_Widget.column(col_idx , anchor="center" , stretch=True)
        
        self.Treeview_Widget.delete(*self.Treeview_Widget.get_children())

        self.y_Scrollbar = ttk.Scrollbar(self.Father_Frame_Of_Table , orient="vertical" , command=self.Treeview_Widget.yview)
        self.x_Scrollbar = ttk.Scrollbar(self.Father_Frame_Of_Table , orient="horizontal" , command=self.Treeview_Widget.xview)

        self.Treeview_Widget.configure(yscrollcommand=self.y_Scrollbar.set)
        self.Treeview_Widget.configure(xscrollcommand=self.x_Scrollbar.set)

        self.Treeview_Widget.grid(row=0 , column=0 , sticky="nsew")
        self.y_Scrollbar.grid(row=0 , column=1 , sticky="ns")
        self.x_Scrollbar.grid(row=1 , column=0 , sticky="ew")

        self.Extra_Data_For_Been_Saved = {}

    def Delete_Items_In_Table(self):
        self.Treeview_Widget.delete(*self.Treeview_Widget.get_children())

    def Display_Table(self , Type_Of_Display: Literal["place" , "grid"] , **Position_Parameters):
        try:
            match(Type_Of_Display):
                case "place":
                    self.Father_Frame_Of_Table.place(**Position_Parameters)
                case "grid":
                    self.Father_Frame_Of_Table.grid(**Position_Parameters)
        except Exception:
            Insert_Data_In_Log_File("Ocurrio un error al posicionar una tabla" , "Error" , "Creacion del Widget de Tabla" , Get_Detailed_Info_About_Error())
            messagebox.showerror("Error" , "Ocurrio un error al posicionar una tabla")

    def Hidden_Table(self):
        self.Father_Frame_Of_Table.grid_forget()

    def Modify_Number_Of_Columns(self , New_Number_Of_Table_Columns: int , New_Titles_For_Heading_Table_Columns: list[str] , Columns_Width: int):
        self.Number_Of_Table_Columns = New_Number_Of_Table_Columns
        self.Titles_For_Heading_Table_Columns = New_Titles_For_Heading_Table_Columns

        self.Treeview_Widget["columns"] = []
        self.Treeview_Widget["columns"] = [f"{col_idx}" for col_idx in range(1 , self.Number_Of_Table_Columns + 1)]
        
        for col_idx , title_column in enumerate(self.Titles_For_Heading_Table_Columns , start=1):
            self.Treeview_Widget.heading(f"{col_idx}" , text=title_column)
            self.Treeview_Widget.column(f"{col_idx}" , anchor="center" , width=Columns_Width , stretch=False)

    def Insert_Data(self , Data_To_Display , Extra_Data_In_Bottom_Of_Table=None):
        self.Delete_Items_In_Table()

        try:
            for row_data in Data_To_Display:
                self.Treeview_Widget.insert(
                    "" , "end" , values=row_data if isinstance(row_data , tuple) else tuple(row_data)
                )
            
            if(Extra_Data_In_Bottom_Of_Table):
                self.Treeview_Widget.insert(
                    "" , "end" , values=Extra_Data_In_Bottom_Of_Table if isinstance(Extra_Data_In_Bottom_Of_Table , tuple) else tuple(Extra_Data_In_Bottom_Of_Table)
                )
            
        except Exception:
            Insert_Data_In_Log_File("Ocurrio un error al mostrar una tabla" , "Error" , "Creacion del Widget de Tabla" , Get_Detailed_Info_About_Error())
            messagebox.showerror("Error" , "Ocurrio un error al mostrar una tabla")

# ==================================================================== Spinbox que valida el valor ====================================================================
class Spinbox_With_Validation:
    def __init__(self , Root_Window , Max_Value , Min_Value , Increment_Value , Value_Associed , Type_Of_Display: Literal["grid","place"] , Spinbox_Width=None , **Place_Widget):
        self.Register_For_Spinbox = (Root_Window.register(self.Avoid_Unwanted_Values_In_Spinbox), '%P')
        self.Min_Value = Min_Value
        self.Max_Value = Max_Value
        
        self.Spinbox_In_App = Spinbox(Root_Window , textvariable=Value_Associed , from_=Min_Value , to=Max_Value , increment=Increment_Value , width=Spinbox_Width , font=("Courier New" , 13) , validate="all" , validatecommand=self.Register_For_Spinbox)
        self.Spinbox_In_App.config(state="readonly")
        match(Type_Of_Display):
            case "place" if "x" in Place_Widget and "y" in Place_Widget:
                self.Spinbox_In_App.place(**Place_Widget)

            case "grid" if "row" in Place_Widget and "column" in Place_Widget:
                self.Spinbox_In_App.grid(**Place_Widget)

    def Avoid_Unwanted_Values_In_Spinbox(self , Actual_Spinbox_Value):
        if(Actual_Spinbox_Value == ""):
            return True
        try:
            Number = int(Actual_Spinbox_Value)
            if("." in Actual_Spinbox_Value):
                return False
            return self.Min_Value <= Number <= self.Max_Value
        except ValueError:
            return False

# ==================================================================== Entry con validacion ====================================================================
class Entry_With_Validation:
    def __init__(self , Root_Window , Max_Characters_Number , Entry_Width , **Place):
        self.Min_Characters_Number = 0
        self.Max_Characters_Number = Max_Characters_Number

        self.Entry_Variable = StringVar(Root_Window)
        self.Entry_Variable.trace_add("write" , self.On_Text_Change)
        self.Entry_Widget = Entry(Root_Window , textvariable=self.Entry_Value , width=Entry_Width)
        self.Entry_Widget.place(x=Place["x"] , y=Place["y"])

        self.Char_Count = StringVar(Root_Window)
        self.Char_Count.set(f"0/{self.Max_Characters_Number}")
        self.Label_Char_Count = Label(Root_Window , textvariable=self.Char_Count)
        self.Label_Char_Count.place(x=Place["x"]+self.Entry_Widget.winfo_width()-self.Label_Char_Count.winfo_width()-5 , y=Place["y"]+self.Entry_Widget.winfo_height()+5)

    def On_Text_Change(self , *args):
        Text = self.Entry_Value.get()
        if(len(Text) > self.Max_Characters_Number):
            self.Entry_Variable.set(Text[:self.Max_Characters_Number])
        self.Char_Count.set(f"{len(self.Entry_Variable.get())}/{self.Max_Characters_Number} caracteres")

class Notepad_Visor:
    def __init__(self):
        pass