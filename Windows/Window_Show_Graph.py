import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox

from Calcs.Calc_Graphs import Draw_Graph_for_Each_Variable
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def Change_Key(dictionary, old_key, new_key):
    """ No modifica el diccionarrio, sino que genera uno nuevo , pero con las claves moficiadas """
    return {clave if clave != old_key else new_key: valor for clave, valor in dictionary.items()}

def Window_Download_Graph():
    pass

def Create_Window_Show_Graph(Father_Window , Data , Precision):
    if __name__ == "__main__":
        W_Show_Graph = Tk()
    else:
        W_Show_Graph = Toplevel(Father_Window)
        W_Show_Graph.grab_set()

    def Display_Graphs():
        if(Checked_According_fi.get()):
            Widgets["bar_hi"][0].get_tk_widget().place_forget()
            Widgets["pie_hi"][0].get_tk_widget().place_forget()
            Widgets["bar_hi_percent"][0].get_tk_widget().place_forget()
            Widgets["pie_hi_percent"][0].get_tk_widget().place_forget()
            if(Checked_Bar_Graph.get()):
                Widgets["bar_fi"][0].get_tk_widget().place(x=320 , y=0)
                Widgets["pie_fi"][0].get_tk_widget().place_forget()
            elif(Checked_Pie_Graph.get()):
                Widgets["pie_fi"][0].get_tk_widget().place(x=320 , y=0)
                Widgets["bar_fi"][0].get_tk_widget().place_forget()
            else:
                Widgets["bar_fi"][0].get_tk_widget().place_forget()
                Widgets["pie_fi"][0].get_tk_widget().place_forget()
        elif(Checked_According_hi.get()):
            Widgets["bar_fi"][0].get_tk_widget().place_forget()
            Widgets["pie_fi"][0].get_tk_widget().place_forget()
            Widgets["bar_hi_percent"][0].get_tk_widget().place_forget()
            Widgets["pie_hi_percent"][0].get_tk_widget().place_forget()
            if(Checked_Bar_Graph.get()):
                Widgets["bar_hi"][0].get_tk_widget().place(x=320 , y=0)
                Widgets["pie_hi"][0].get_tk_widget().place_forget()
            elif(Checked_Pie_Graph.get()):
                Widgets["pie_hi"][0].get_tk_widget().place(x=320 , y=0)
                Widgets["bar_hi"][0].get_tk_widget().place_forget()
            else:
                Widgets["bar_hi"][0].get_tk_widget().place_forget()
                Widgets["pie_hi"][0].get_tk_widget().place_forget()
        elif(Checked_According_hi_percent.get()):
            Widgets["bar_hi"][0].get_tk_widget().place_forget()
            Widgets["pie_hi"][0].get_tk_widget().place_forget()
            Widgets["bar_fi"][0].get_tk_widget().place_forget()
            Widgets["pie_fi"][0].get_tk_widget().place_forget()
            if(Checked_Bar_Graph.get()):
                Widgets["bar_hi_percent"][0].get_tk_widget().place(x=320 , y=0)
                Widgets["pie_hi_percent"][0].get_tk_widget().place_forget()
            elif(Checked_Pie_Graph.get()):
                Widgets["pie_hi_percent"][0].get_tk_widget().place(x=320 , y=0)
                Widgets["bar_hi_percent"][0].get_tk_widget().place_forget()
            else:
                Widgets["bar_hi_percent"][0].get_tk_widget().place_forget()
                Widgets["pie_hi_percent"][0].get_tk_widget().place_forget()
        else:
            for value in Widgets.values():
                value[0].get_tk_widget().place_forget()

    def Only_Check_Bar_Graph():
        if(Checked_Bar_Graph.get() and Checked_Pie_Graph.get()):
            Checked_Pie_Graph.set(False)
        Display_Graphs()

    def Only_Check_Pie_Graph():
        if(Checked_Pie_Graph.get() and Checked_Bar_Graph.get()):
            Checked_Bar_Graph.set(False)
        Display_Graphs()

    def Activate_Disable_Bar_Pie_Checkbox():
        if(Checked_According_fi.get() or Checked_According_hi.get() or Checked_According_hi_percent.get()):
            Checkbox_Bar_Graph.config(state="normal")
            Checkbox_Pie_Graph.config(state="normal")
        else:
            Checkbox_Bar_Graph.config(state="disabled")
            Checked_Bar_Graph.set(False)
            Checkbox_Pie_Graph.config(state="disabled")
            Checked_Pie_Graph.set(False)

    def Only_Check_According_fi():
        if((Checked_According_fi.get() and Checked_According_hi.get()) or (Checked_According_fi.get() and Checked_According_hi_percent.get())):
            Checked_According_hi.set(False)
            Checked_According_hi_percent.set(False)
        Activate_Disable_Bar_Pie_Checkbox()
        Display_Graphs()

    def Only_Check_According_hi():
        if((Checked_According_hi.get() and Checked_According_fi.get()) or (Checked_According_hi.get() and Checked_According_hi_percent.get())):
            Checked_According_fi.set(False)
            Checked_According_hi_percent.set(False)
        Activate_Disable_Bar_Pie_Checkbox()
        Display_Graphs()

    def Only_Check_According_hi_percent():
        if((Checked_According_hi_percent.get() and Checked_According_fi.get()) or (Checked_According_hi_percent.get() and Checked_According_hi.get())):
            Checked_According_fi.set(False)
            Checked_According_hi.set(False)
        Activate_Disable_Bar_Pie_Checkbox()
        Display_Graphs()

    def Generate_Graph(Root_Window , Data):
        New_Data = {}

        for key,value in Data.items():
            if value != None:
                New_Data[key] = value

        if("Frecuences_Cuant_For_Many_Values" in New_Data):
            for a in range(0 , len(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"])):
                if(a != len(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"]) - 1):
                    New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" >"
                else:
                    New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" ]"
        try:
            Graph = Draw_Graph_for_Each_Variable(New_Data , Precision)
            
            bar_fi , pie_fi = Graph.Draw_Graph("fi")
            bar_hi , pie_hi = Graph.Draw_Graph("hi")
            bar_hi_percent , pie_hi_percent = Graph.Draw_Graph("hi_percent")
            
            Widget_bar_fi = FigureCanvasTkAgg(bar_fi , master=Root_Window)
            Widget_bar_fi.draw()
            Widget_bar_hi = FigureCanvasTkAgg(bar_hi , master=Root_Window)
            Widget_bar_hi.draw()
            Widget_bar_hi_percent = FigureCanvasTkAgg(bar_hi_percent , master=Root_Window)
            Widget_bar_hi_percent.draw()
            Widget_pie_fi = FigureCanvasTkAgg(pie_fi , master=Root_Window)
            Widget_pie_fi.draw()
            Widget_pie_hi = FigureCanvasTkAgg(pie_hi , master=Root_Window)
            Widget_pie_hi.draw()
            Widget_pie_hi_percent = FigureCanvasTkAgg(pie_hi_percent , master=Root_Window)
            Widget_pie_hi_percent.draw()

            Dictionary_Widgets = dict([
                ("bar_fi" , [Widget_bar_fi , bar_fi]),
                ("bar_hi" , [Widget_bar_hi , bar_hi]),
                ("bar_hi_percent" , [Widget_bar_hi_percent , bar_hi]),
                ("pie_fi" , [Widget_pie_fi , pie_fi]),
                ("pie_hi" , [Widget_pie_hi , pie_hi]),
                ("pie_hi_percent" , [Widget_pie_hi_percent , pie_hi_percent]),
            ])
            return Dictionary_Widgets
        except Exception as e:
            messagebox.showerror("Error" , f"{e}")

    def Change_Title(Bar_Title , Pie_Title):
        if(Bar_Title):
            Widgets["bar_fi"][1].suptitle(f"{Bar_Title}")
            Widgets["bar_fi"][0].draw()
            Widgets["bar_hi"][1].suptitle(f"{Bar_Title}")
            Widgets["bar_hi"][0].draw()
            Widgets["bar_hi_percent"][1].suptitle(f"{Bar_Title}")
            Widgets["bar_hi_percent"][0].draw()

            Input_Name_Bar_Graph.delete(0 , END)
        if(Pie_Title):
            Widgets["pie_fi"][1].suptitle(f"{Pie_Title}")
            Widgets["pie_fi"][0].draw()
            Widgets["pie_hi"][1].suptitle(f"{Pie_Title}")
            Widgets["pie_hi"][0].draw()
            Widgets["pie_hi_percent"][1].suptitle(f"{Pie_Title}")
            Widgets["pie_hi_percent"][0].draw()
            Input_Name_Píe_Graph.delete(0 , END)
        else:
            messagebox.showwarning("Alerta" , "Ningun valor introducido")

    Icon = PhotoImage(file="Images/icon.png")
    W_Show_Graph.title("Ver Grafico")
    W_Show_Graph.geometry("1000x700+280+90")
    W_Show_Graph.iconphoto(False , Icon)


    Checked_According_fi = BooleanVar(W_Show_Graph)
    Checked_According_hi = BooleanVar(W_Show_Graph)
    Checked_According_hi_percent = BooleanVar(W_Show_Graph)

    Checked_Bar_Graph = BooleanVar(W_Show_Graph)
    Checked_Pie_Graph = BooleanVar(W_Show_Graph)

    Name_Bar_Graph = StringVar(W_Show_Graph)
    Name_Pie_Graph = StringVar(W_Show_Graph)

    Checkbox_Calc_According_fi = Checkbutton(W_Show_Graph , text="Segun fi" , font=("Times New Roman" , 13) , variable=Checked_According_fi ,  command=Only_Check_According_fi)
    Checkbox_Calc_According_fi.place(x=20 , y=20)

    Checkbox_Calc_According_hi = Checkbutton(W_Show_Graph , text="Segun hi" , font=("Times New Roman" , 13) , variable=Checked_According_hi , command=Only_Check_According_hi)
    Checkbox_Calc_According_hi.place(x=20 , y=60)

    Checkbox_Calc_According_hi_percent = Checkbutton(W_Show_Graph , text="Segun hi%" , font=("Times New Roman" , 13) , variable=Checked_According_hi_percent , command=Only_Check_According_hi_percent)
    Checkbox_Calc_According_hi_percent.place(x=20 , y=100)

    Checkbox_Bar_Graph = Checkbutton(W_Show_Graph , text="Grafico de barras" , font=("Times New Roman" , 13) , variable=Checked_Bar_Graph , command=Only_Check_Bar_Graph)
    Checkbox_Bar_Graph.place(x=20 , y=180)
    Checkbox_Bar_Graph.config(state="disabled")

    Checkbox_Pie_Graph = Checkbutton(W_Show_Graph , text="Grafico de pastel" , font=("Times New Roman" , 13) , variable=Checked_Pie_Graph , command=Only_Check_Pie_Graph)
    Checkbox_Pie_Graph.place(x=20 , y=220)
    Checkbox_Pie_Graph.config(state="disabled")

    Text_Change_Name_Bar_Graph = Label(W_Show_Graph , text="Ingrese un nombre para el grafico de barras: " , font=("Times New Roman" , 13))
    Text_Change_Name_Bar_Graph.place(x=20 , y=300)
    Input_Name_Bar_Graph = Entry(W_Show_Graph , font=("Courier New" , 13) , textvariable=Name_Bar_Graph , width=30)
    Input_Name_Bar_Graph.place(x=20 , y=330)
    Input_Name_Bar_Graph.focus()

    Text_Change_Name_Pie_Graph = Label(W_Show_Graph , text="Ingrese un nombre para el grafico de pastel: " , font=("Times New Roman" , 13))
    Text_Change_Name_Pie_Graph.place(x=20 , y=370)
    Input_Name_Píe_Graph = Entry(W_Show_Graph , font=("Courier New" , 13) , textvariable=Name_Pie_Graph , width=30)
    Input_Name_Píe_Graph.place(x=20 , y=400)

    Widgets = Generate_Graph(W_Show_Graph , Data)

    Btn_Change_Name = Button(W_Show_Graph , text="Cambiar" , font=("Times New Roman" , 13) , width=10 , command= lambda: Change_Title(Name_Bar_Graph.get() , Name_Pie_Graph.get()))
    Btn_Change_Name.place(x=80 , y=440)

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar_Grafico" , font=("Times New Roman" , 13) , width=15)
    Btn_Export_Graph.place(x=65 , y=480)

    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()

if __name__ == "__main__":
    Create_Window_Show_Graph(None)