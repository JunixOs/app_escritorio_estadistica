from tkinter import *
from tkinter import ttk
from typing import Literal

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