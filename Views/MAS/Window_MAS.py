import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Calcs.MAS.MAS_Calc as MAS
from Calcs.Center_Window import Center
from tkinter import *

def Create_Window_MAS(Main_Window=None):
    def Back():
        for widget in Window_MAS.winfo_children():
            widget.destroy()
        Window_MAS.grab_release()
        Window_MAS.quit()
        Window_MAS.destroy()

        Main_Window.state(newstate="normal")
        Main_Window.lift()
        
    if __name__ == "__main__":
        Window_MAS = Tk()
    else:
        Window_MAS = Toplevel(Main_Window)
        Main_Window.state(newstate="withdraw")

    Icon = PhotoImage(file="Images/icon.png")
    Window_MAS.title("Calcular tamaño de muestra")
    Window_MAS.geometry("550x450")
    Center(Window_MAS , 550 , 450)

    Window_MAS.iconphoto(False , Icon)
    Window_MAS.lift()
    Window_MAS.protocol("WM_DELETE_WINDOW" , Back)
    Window_MAS.config(bg="#CBEFE3")

    Checked_Finite_Population = BooleanVar(Window_MAS)
    Checked_Infinite_Population = BooleanVar(Window_MAS)

    Confidence_Level = DoubleVar(Window_MAS)
    N = IntVar(Window_MAS)
    p = DoubleVar(Window_MAS)
    e = DoubleVar(Window_MAS)
    Precision = IntVar(Window_MAS)
    n_o = IntVar(Window_MAS)
    n_f = IntVar(Window_MAS)

    Confidence_Level.set(0)
    N.set(0)
    p.set(0)
    e.set(0)
    n_o.set(0)
    n_f.set(0)

    def Only_Check_Finite_Population():
        if(Checked_Finite_Population.get() and Checked_Infinite_Population.get()):
            Checked_Infinite_Population.set(False)
        else:
            Input_N.config(state="disabled")
            N.set(0)
            Input_Confidence_Level.config(state="disabled")
            Confidence_Level.set(0)
            Input_p.config(state="disabled")
            p.set(0)
            Input_e.config(state="disabled")
            e.set(0)
            Input_Precision.config(state="disabled")
            n_o.set(0)
            n_f.set(0)
        
        if(Checked_Finite_Population.get()):
            Input_N.config(state="normal")
            Input_Confidence_Level.config(state="normal")
            Input_p.config(state="normal")
            Input_e.config(state="normal")
            Input_Precision.config(state="normal")
            n_o.set(0)
            n_f.set(0)
        
    def Only_Check_Infinite_Population():
        if(Checked_Infinite_Population.get() and Checked_Finite_Population.get()):
            Checked_Finite_Population.set(False)
        else:
            Input_N.config(state="disabled")
            N.set(0)
            Input_Confidence_Level.config(state="disabled")
            Confidence_Level.set(0)
            Input_p.config(state="disabled")
            p.set(0)
            Input_e.config(state="disabled")
            e.set(0)
            Input_Precision.config(state="disabled")
            n_o.set(0)
            n_f.set(0)
        
        if(Checked_Infinite_Population.get()):
            Input_N.config(state="disabled")
            N.set(0)
            Input_Confidence_Level.config(state="normal")
            Input_p.config(state="normal")
            Input_e.config(state="normal")
            Input_Precision.config(state="normal")
            n_o.set(0)
            n_f.set(0)

    Main_Text = Label(Window_MAS , text="Ingrese los valores en porcentaje. ej: 20% => 20 \n usar punto \".\" en lugar de coma \",\" para los decimales", font=("Times New Roman" , 13) , justify=CENTER , bg="#F8E6CE")
    Main_Text.pack(side=TOP , fill=BOTH)

    Checkbox_Finite_Population = Checkbutton(Window_MAS , text="Poblacion finita" , font=("Times New Roman" , 13) , variable=Checked_Finite_Population , command=Only_Check_Finite_Population , bg="#CBEFE3")
    Checkbox_Finite_Population.place(x=50 , y=50)
    Checkbox_Infinite_Population = Checkbutton(Window_MAS , text="Poblacion infinita" , font=("Times New Roman" , 13) , variable=Checked_Infinite_Population , command=Only_Check_Infinite_Population , bg="#CBEFE3")
    Checkbox_Infinite_Population.place(x=340 , y=50)

    Text_Input_N = Label(Window_MAS , text="Poblacion (N): ", font=("Times New Roman" , 13) , bg="#CBEFE3")
    Text_Input_N.place(x=40 , y=100)
    Input_N = Entry(Window_MAS , font=("Courier New" , 13), width=26 , textvariable=N)
    Input_N.place(x=230 , y=100)
    Input_N.config(state="disabled")

    Text_Input_Confidence_Level = Label(Window_MAS , text="Nivel de confianza (1 - α): ", font=("Times New Roman" , 13) , bg="#CBEFE3")
    Text_Input_Confidence_Level.place(x=40 , y=140)
    Input_Confidence_Level = Entry(Window_MAS , font=("Courier New" , 13), width=26 , textvariable=Confidence_Level)
    Input_Confidence_Level.place(x=230 , y=140)
    Input_Confidence_Level.config(state="disabled")

    Text_Input_p = Label(Window_MAS , text="Probabilidad de exito (p): ", font=("Times New Roman" , 13) , bg="#CBEFE3")
    Text_Input_p.place(x=40 , y=180)
    Input_p = Entry(Window_MAS, font=("Courier New" , 13), width=26 , textvariable=p)
    Input_p.place(x=230 , y=180)
    Input_p.config(state="disabled")

    Text_Input_e = Label(Window_MAS , text="Error (e): ", font=("Times New Roman" , 13) , bg="#CBEFE3")
    Text_Input_e.place(x=40 , y=220)
    Input_e = Entry(Window_MAS, font=("Courier New" , 13), width=26 , textvariable=e)
    Input_e.place(x=230 , y=220)
    Input_e.config(state="disabled")

    Text_Input_Precision = Label(Window_MAS , text="Precision que se usara: ", font=("Times New Roman" , 13) , bg="#CBEFE3")
    Text_Input_Precision.place(x=40 , y=260)
    Input_Precision = Spinbox(Window_MAS , font=("Courier New" , 13) , from_=2 , to=4 , textvariable=Precision , width=2)
    Input_Precision.place(x=230 , y=260)
    Input_Precision.config(state="disabled")

    Btn_Calculate = Button(Window_MAS , text="Cacular tamaño de muestra" , font=("Times New Roman" , 13) , bg="#FBCFC6" ,  command= lambda: MAS.Calc_Samplings(e.get() , Confidence_Level.get() , N.get() , Checked_Finite_Population.get() , Checked_Infinite_Population.get() , n_o , n_f , Precision.get() , p.get()))
    Btn_Calculate.place(x=170 , y=300 , width=210)

    Text_Output_n_o = Label(Window_MAS , text="Muestra Inicial (n_o): ", font=("Times New Roman" , 13) , bg="#CBEFE3")
    Text_Output_n_o.place(x=150 , y=380)
    Output_n_o = Entry(Window_MAS , font=("Courier New" , 13), width=6 , textvariable=n_o)
    Output_n_o.place(x=310 , y=380)
    Output_n_o.config(state="disabled")

    Text_Output_n_f = Label(Window_MAS , text="Muestra Final Corregida (n_f): ", font=("Times New Roman" , 13) , bg="#CBEFE3")
    Text_Output_n_f.place(x=90 , y=420)
    Output_n_f = Entry(Window_MAS , font=("Courier New" , 13), width=6 , textvariable=n_f)
    Output_n_f.place(x=310 , y=420)
    Output_n_f.config(state="disabled")

    Window_MAS.resizable(False , False)
    Window_MAS.mainloop()

if __name__ == "__main__":
    Create_Window_MAS()