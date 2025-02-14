import sys
import os
import copy
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox

from Calcs.Calc_Graphs import Draw_Graph_for_Each_Variable
from Window_Export_Graph import Create_Window_Export_Graph
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
        if(Precision > 3):
            Precision = 3
            
    def Display_Graphs():
        if(Checked_Bar_Graph.get()):
            Widgets["pie_graph"][0].get_tk_widget().place_forget()

            if(Checked_According_fi.get()):
                Widgets["bar_fi"][0].get_tk_widget().place(x=320 , y=0)
                Widgets["bar_hi"][0].get_tk_widget().place_forget()
                Widgets["bar_hi_percent"][0].get_tk_widget().place_forget()
            elif(Checked_According_hi.get()):
                Widgets["bar_hi"][0].get_tk_widget().place(x=320 , y=0)
                Widgets["bar_fi"][0].get_tk_widget().place_forget()
                Widgets["bar_hi_percent"][0].get_tk_widget().place_forget()
            elif(Checked_According_hi_percent.get()):
                Widgets["bar_hi_percent"][0].get_tk_widget().place(x=320 , y=0)
                Widgets["bar_hi"][0].get_tk_widget().place_forget()
                Widgets["bar_fi"][0].get_tk_widget().place_forget()
            else:
                Widgets["bar_fi"][0].get_tk_widget().place_forget()
                Widgets["bar_hi"][0].get_tk_widget().place_forget()
                Widgets["bar_hi_percent"][0].get_tk_widget().place_forget()
        elif(Checked_Pie_Graph.get()):
            Widgets["bar_fi"][0].get_tk_widget().place_forget()
            Widgets["bar_hi"][0].get_tk_widget().place_forget()
            Widgets["bar_hi_percent"][0].get_tk_widget().place_forget()

            Widgets["pie_graph"][0].get_tk_widget().place(x=320 , y=0)
        else:
            for graph in Widgets.values():
                graph[0].get_tk_widget().place_forget()

    def Activate_Disable_Bars_Checkboxes():
        if(Checked_Bar_Graph.get()):
            Checkbox_Show_According_fi.config(state="normal")
            Checkbox_Show_According_hi.config(state="normal")
            Checkbox_Show_According_hi_percent.config(state="normal")
        else:
            Checkbox_Show_According_fi.config(state="disabled")
            Checked_According_fi.set(False)
            Checkbox_Show_According_hi.config(state="disabled")
            Checked_According_hi.set(False)
            Checkbox_Show_According_hi_percent.config(state="disabled")
            Checked_According_hi_percent.set(False)

    def Only_Check_Bar_Graph():
        if(Checked_Bar_Graph.get() and Checked_Pie_Graph.get()):
            Checked_Pie_Graph.set(False)
        Activate_Disable_Bars_Checkboxes()
        Display_Graphs()

    def Only_Check_Pie_Graph():
        if(Checked_Pie_Graph.get() and Checked_Bar_Graph.get()):
            Checked_Bar_Graph.set(False)
            Activate_Disable_Bars_Checkboxes()
        Display_Graphs()

    def Only_Check_According_fi():
        if((Checked_According_fi.get() and Checked_According_hi.get()) or (Checked_According_fi.get() and Checked_According_hi_percent.get())):
            Checked_According_hi.set(False)
            Checked_According_hi_percent.set(False)
        Display_Graphs()

    def Only_Check_According_hi():
        if((Checked_According_hi.get() and Checked_According_fi.get()) or (Checked_According_hi.get() and Checked_According_hi_percent.get())):
            Checked_According_fi.set(False)
            Checked_According_hi_percent.set(False)
        Display_Graphs()

    def Only_Check_According_hi_percent():
        if((Checked_According_hi_percent.get() and Checked_According_fi.get()) or (Checked_According_hi_percent.get() and Checked_According_hi.get())):
            Checked_According_fi.set(False)
            Checked_According_hi.set(False)
        Display_Graphs()

    def Generate_Graph(Root_Window , Data):
        New_Data = {}
        Copy_Data = copy.deepcopy(Data)

        for key,value in Copy_Data.items():
            if value != None:
                New_Data[key] = value

        if(("Frecuences_Cuant_For_Many_Values" in New_Data) and not isinstance(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][0][0] , str)):
            for a in range(0 , len(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"])):
                if(a != len(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"]) - 1):
                    New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" >"
                else:
                    New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" ]"
        try:
            Graph = Draw_Graph_for_Each_Variable(New_Data , Precision)
            
            bar_fi , pie_graph = Graph.Draw_Graph("fi")
            bar_hi = Graph.Draw_Graph("hi")
            bar_hi_percent = Graph.Draw_Graph("hi_percent")
            
            Widget_bar_fi = FigureCanvasTkAgg(bar_fi , master=Root_Window)
            Widget_bar_fi.draw()
            Widget_bar_hi = FigureCanvasTkAgg(bar_hi , master=Root_Window)
            Widget_bar_hi.draw()
            Widget_bar_hi_percent = FigureCanvasTkAgg(bar_hi_percent , master=Root_Window)
            Widget_bar_hi_percent.draw()
            Widget_pie_graph = FigureCanvasTkAgg(pie_graph , master=Root_Window)
            Widget_pie_graph.draw()

            Dictionary_Widgets = dict([
                ("bar_fi" , [Widget_bar_fi , bar_fi]),
                ("bar_hi" , [Widget_bar_hi , bar_hi]),
                ("bar_hi_percent" , [Widget_bar_hi_percent , bar_hi]),
                ("pie_graph" , [Widget_pie_graph , pie_graph]),
            ])
            return Dictionary_Widgets
        except Exception as e:
            messagebox.showerror("Error" , f"{e}")

    Icon = PhotoImage(file="Images/icon.png")
    W_Show_Graph.title("Ver Grafico")
    W_Show_Graph.geometry("1000x700+280+90")
    W_Show_Graph.iconphoto(False , Icon)



    Checked_According_fi = BooleanVar(W_Show_Graph)
    Checked_According_hi = BooleanVar(W_Show_Graph)
    Checked_According_hi_percent = BooleanVar(W_Show_Graph)

    Checked_Bar_Graph = BooleanVar(W_Show_Graph)
    Checked_Pie_Graph = BooleanVar(W_Show_Graph)

    Checkbox_Bar_Graph = Checkbutton(W_Show_Graph , text="Grafico de barras" , font=("Times New Roman" , 13) , variable=Checked_Bar_Graph , command=Only_Check_Bar_Graph)
    Checkbox_Bar_Graph.place(x=60 , y=180)

    Checkbox_Show_According_fi = Checkbutton(W_Show_Graph , text="Segun fi" , font=("Times New Roman" , 13) , variable=Checked_According_fi ,  command=Only_Check_According_fi)
    Checkbox_Show_According_fi.place(x=100 , y=220)
    Checkbox_Show_According_fi.config(state="disabled")

    Checkbox_Show_According_hi = Checkbutton(W_Show_Graph , text="Segun hi" , font=("Times New Roman" , 13) , variable=Checked_According_hi , command=Only_Check_According_hi)
    Checkbox_Show_According_hi.place(x=100 , y=250)
    Checkbox_Show_According_hi.config(state="disabled")

    Checkbox_Show_According_hi_percent = Checkbutton(W_Show_Graph , text="Segun hi%" , font=("Times New Roman" , 13) , variable=Checked_According_hi_percent , command=Only_Check_According_hi_percent)
    Checkbox_Show_According_hi_percent.place(x=100 , y=280)
    Checkbox_Show_According_hi_percent.config(state="disabled")

    Checkbox_Pie_Graph = Checkbutton(W_Show_Graph , text="Grafico de pastel" , font=("Times New Roman" , 13) , variable=Checked_Pie_Graph , command=Only_Check_Pie_Graph)
    Checkbox_Pie_Graph.place(x=60 , y=360)

    if __name__ != "__main__":
        Widgets = {}
        Widgets = Generate_Graph(W_Show_Graph , Data)

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar Graficos" , font=("Times New Roman" , 13) , width=15 , command= lambda: Create_Window_Export_Graph(W_Show_Graph , copy.deepcopy(Widgets)))
    Btn_Export_Graph.place(x=90 , y=440)

    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()

if __name__ == "__main__":
    Create_Window_Show_Graph(None , None , None)