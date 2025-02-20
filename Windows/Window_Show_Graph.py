import sys
import os
import copy
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Calcs.Calc_Graphs import Draw_Graph_for_Each_Variable
from Window_Export_Graph import Create_Windows_Export_Graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def Change_Key(dictionary, old_key, new_key):
    """ No modifica el diccionarrio, sino que genera uno nuevo , pero con las claves moficiadas """
    return {clave if clave != old_key else new_key: valor for clave, valor in dictionary.items()}

def Create_Windows_Show_Graphs(Father_Window , Data_From_Single_Column , Data_From_Multiple_Columns , Precision , Graphs):
    """ Esta es la funcion principal del modulo """

    if(Precision > 3):
        Precision = 3

    if(Data_From_Single_Column != {}):
        W_For_Single_Colum_Data(Father_Window , Data_From_Single_Column , Precision , Graphs)
    elif(Data_From_Multiple_Columns != {}):
        """ raise Exception("Error, la funcion todavia esta en desarrollo.") """
        W_For_Multiple_Column_Data(Father_Window , Data_From_Multiple_Columns , Precision , Graphs)
    else:
        raise Exception("No se encontraron los datos para generar los graficos.")

def Generate_Graphs(Root_Window , Data_From_Single_Column , Data_From_Multiple_Column , Precision , Graphs):
    New_Data = {}
    if(Data_From_Single_Column != {}):
        Copy_Data = copy.deepcopy(Data_From_Single_Column)
        Dictionary_Widgets = {}
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

            if(Graphs == {}):
                bar_fi , pie_graph = Graph.Draw_Graph("fi")
                bar_hi = Graph.Draw_Graph("hi")
                bar_hi_percent = Graph.Draw_Graph("hi_percent")

                Graphs["bar_fi"] = bar_fi
                Graphs["bar_hi"] = bar_hi
                Graphs["bar_hi_percent"] = bar_hi_percent
                Graphs["pie_graph"] = pie_graph
            
            Widget_bar_fi = FigureCanvasTkAgg(Graphs["bar_fi"] , master=Root_Window)
            Widget_bar_fi.draw()
            Widget_bar_hi = FigureCanvasTkAgg(Graphs["bar_hi"] , master=Root_Window)
            Widget_bar_hi.draw()
            Widget_bar_hi_percent = FigureCanvasTkAgg(Graphs["bar_hi_percent"] , master=Root_Window)
            Widget_bar_hi_percent.draw()
            Widget_pie_graph = FigureCanvasTkAgg(Graphs["pie_graph"] , master=Root_Window)
            Widget_pie_graph.draw()


            Dictionary_Widgets = dict([
                ("bar_fi" , Widget_bar_fi),
                ("bar_hi" , Widget_bar_hi),
                ("bar_hi_percent" , Widget_bar_hi_percent),
                ("pie_graph" , Widget_pie_graph),
            ])
        except Exception as e:
            messagebox.showerror("Error" , f"{e}")

    elif(Data_From_Multiple_Column != {}):
        Copy_Data = copy.deepcopy(Data_From_Multiple_Column)
        Dictionary_Widgets = {}
        if(Graphs == {}):
            Is_Graphs_Empty = True
        else:
            Is_Graphs_Empty = False

        for key , value in Copy_Data.items():
            for k,v in value.items():
                if v != None:
                    New_Data[k] = v

            if(("Frecuences_Cuant_For_Many_Values" in New_Data) and not isinstance(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][0][0] , str)):
                for a in range(0 , len(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"])):
                    if(a != len(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"]) - 1):
                        New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" >"
                    else:
                        New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(New_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" ]"
            try:
                Graph = Draw_Graph_for_Each_Variable(New_Data , Precision)
                if(Is_Graphs_Empty):
                    bar_fi , pie_graph = Graph.Draw_Graph("fi")
                    bar_hi = Graph.Draw_Graph("hi")
                    bar_hi_percent = Graph.Draw_Graph("hi_percent")

                    Graphs[f"{key}"] = {
                        "bar_fi" : bar_fi,
                        "bar_hi" : bar_hi,
                        "bar_hi_percent" : bar_hi_percent,
                        "pie_graph" : pie_graph,
                    }
                
                Widget_bar_fi = FigureCanvasTkAgg(Graphs[f"{key}"]["bar_fi"] , master=Root_Window)
                Widget_bar_fi.draw()
                Widget_bar_hi = FigureCanvasTkAgg(Graphs[f"{key}"]["bar_hi"] , master=Root_Window)
                Widget_bar_hi.draw()
                Widget_bar_hi_percent = FigureCanvasTkAgg(Graphs[f"{key}"]["bar_hi_percent"] , master=Root_Window)
                Widget_bar_hi_percent.draw()
                Widget_pie_graph = FigureCanvasTkAgg(Graphs[f"{key}"]["pie_graph"] , master=Root_Window)
                Widget_pie_graph.draw()

                Dictionary_Widgets[f"{key}"] = {
                    "bar_fi" : Widget_bar_fi,
                    "bar_hi" : Widget_bar_hi,
                    "bar_hi_percent" : Widget_bar_hi_percent,
                    "pie_graph" : Widget_pie_graph,
                }
            except Exception as e:
                messagebox.showerror("Error" , f"{e}")

    return Dictionary_Widgets

def W_For_Single_Colum_Data(Father_Window , Data_From_Single_Column , Precision , Graphs):

    def Display_Graphs():
        if(Checked_Bar_Graph.get()):
            Widgets["pie_graph"].get_tk_widget().place_forget()

            if(Checked_Bar_fi.get()):
                Widgets["bar_fi"].get_tk_widget().place(x=320 , y=0)
                Widgets["bar_hi"].get_tk_widget().place_forget()
                Widgets["bar_hi_percent"].get_tk_widget().place_forget()
            elif(Checked_Bar_hi.get()):
                Widgets["bar_hi"].get_tk_widget().place(x=320 , y=0)
                Widgets["bar_fi"].get_tk_widget().place_forget()
                Widgets["bar_hi_percent"].get_tk_widget().place_forget()
            elif(Checked_Bar_hi_percent.get()):
                Widgets["bar_hi_percent"].get_tk_widget().place(x=320 , y=0)
                Widgets["bar_hi"].get_tk_widget().place_forget()
                Widgets["bar_fi"].get_tk_widget().place_forget()
            else:
                Widgets["bar_fi"].get_tk_widget().place_forget()
                Widgets["bar_hi"].get_tk_widget().place_forget()
                Widgets["bar_hi_percent"].get_tk_widget().place_forget()
        elif(Checked_Pie_Graph.get()):
            Widgets["bar_fi"].get_tk_widget().place_forget()
            Widgets["bar_hi"].get_tk_widget().place_forget()
            Widgets["bar_hi_percent"].get_tk_widget().place_forget()

            Widgets["pie_graph"].get_tk_widget().place(x=320 , y=0)
        else:
            for graph in Widgets.values():
                graph.get_tk_widget().place_forget()

    def Activate_Disable_Bars_Checkboxes():
        if(Checked_Bar_Graph.get()):
            Checkbox_Show_Bar_fi.config(state="normal")
            Checkbox_Show_Bar_hi.config(state="normal")
            Checkbox_Show_Bar_hi_percent.config(state="normal")
        else:
            Checkbox_Show_Bar_fi.config(state="disabled")
            Checked_Bar_fi.set(False)
            Checkbox_Show_Bar_hi.config(state="disabled")
            Checked_Bar_hi.set(False)
            Checkbox_Show_Bar_hi_percent.config(state="disabled")
            Checked_Bar_hi_percent.set(False)

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

    def Only_Check_Bar_fi():
        if((Checked_Bar_fi.get() and Checked_Bar_hi.get()) or (Checked_Bar_fi.get() and Checked_Bar_hi_percent.get())):
            Checked_Bar_hi.set(False)
            Checked_Bar_hi_percent.set(False)
        Display_Graphs()

    def Only_Check_Bar_hi():
        if((Checked_Bar_hi.get() and Checked_Bar_fi.get()) or (Checked_Bar_hi.get() and Checked_Bar_hi_percent.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi_percent.set(False)
        Display_Graphs()

    def Only_Check_Bar_hi_percent():
        if((Checked_Bar_hi_percent.get() and Checked_Bar_fi.get()) or (Checked_Bar_hi_percent.get() and Checked_Bar_hi.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi.set(False)
        Display_Graphs()

    if __name__ == "__main__":
        W_Show_Graph = Tk()
    else:
        W_Show_Graph = Toplevel(Father_Window)
        W_Show_Graph.title("Ver graficos")
        W_Show_Graph.geometry("1000x700+280+90")
        W_Show_Graph.grab_set()
        Icon = PhotoImage(file="Images/icon.png")
        W_Show_Graph.iconphoto(False , Icon)

        Widgets = Generate_Graphs(W_Show_Graph , Data_From_Single_Column , {} , Precision , Graphs)

    Checked_Bar_fi = BooleanVar(W_Show_Graph)
    Checked_Bar_hi = BooleanVar(W_Show_Graph)
    Checked_Bar_hi_percent = BooleanVar(W_Show_Graph)

    Checked_Bar_Graph = BooleanVar(W_Show_Graph)
    Checked_Pie_Graph = BooleanVar(W_Show_Graph)

    Checkbox_Bar_Graph = Checkbutton(W_Show_Graph , text="Grafico de barras" , font=("Times New Roman" , 13) , variable=Checked_Bar_Graph , command=Only_Check_Bar_Graph)
    Checkbox_Bar_Graph.place(x=60 , y=180)

    Checkbox_Show_Bar_fi = Checkbutton(W_Show_Graph , text="Segun fi" , font=("Times New Roman" , 13) , variable=Checked_Bar_fi ,  command=Only_Check_Bar_fi)
    Checkbox_Show_Bar_fi.place(x=100 , y=220)
    Checkbox_Show_Bar_fi.config(state="disabled")

    Checkbox_Show_Bar_hi = Checkbutton(W_Show_Graph , text="Segun hi" , font=("Times New Roman" , 13) , variable=Checked_Bar_hi , command=Only_Check_Bar_hi)
    Checkbox_Show_Bar_hi.place(x=100 , y=250)
    Checkbox_Show_Bar_hi.config(state="disabled")

    Checkbox_Show_Bar_hi_percent = Checkbutton(W_Show_Graph , text="Segun hi%" , font=("Times New Roman" , 13) , variable=Checked_Bar_hi_percent , command=Only_Check_Bar_hi_percent)
    Checkbox_Show_Bar_hi_percent.place(x=100 , y=280)
    Checkbox_Show_Bar_hi_percent.config(state="disabled")

    Checkbox_Pie_Graph = Checkbutton(W_Show_Graph , text="Grafico de pastel" , font=("Times New Roman" , 13) , variable=Checked_Pie_Graph , command=Only_Check_Pie_Graph)
    Checkbox_Pie_Graph.place(x=60 , y=360)

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar Graficos" , font=("Times New Roman" , 13) , width=15 , command= lambda: Create_Windows_Export_Graphs(W_Show_Graph , Graphs , Data_From_Single_Column , {}))
    Btn_Export_Graph.place(x=90 , y=440)

    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()

def W_For_Multiple_Column_Data(Father_Window , Data_From_Multiple_Columns , Precision , Graphs):
    def Hidden_Graphs():
        for m_graph in Widgets.values():
            for graph in m_graph.values():
                graph.get_tk_widget().place_forget()

    def Display_Graphs(Event):
        Selection = Column_Select.get()
        Hidden_Graphs()

        if(Checked_Bar_fi.get()):
            Widgets[f"{Selection}"]["bar_fi"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Bar_hi.get()):
            Widgets[f"{Selection}"]["bar_hi"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Bar_hi_percent.get()):
            Widgets[f"{Selection}"]["bar_hi_percent"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Pie_Graph.get()):
            Widgets[f"{Selection}"]["pie_graph"].get_tk_widget().place(x=320 , y=0)

    def Only_Check_Bar_fi():
        if((Checked_Bar_fi.get() and Checked_Bar_hi.get()) or (Checked_Bar_fi.get() and Checked_Bar_hi_percent.get()) or (Checked_Bar_fi.get() and Checked_Pie_Graph.get())):
            Checked_Bar_hi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Pie_Graph.set(False)
        Display_Graphs(None)

    def Only_Check_Bar_hi():
        if((Checked_Bar_hi.get() and Checked_Bar_fi.get()) or (Checked_Bar_hi.get() and Checked_Bar_hi_percent.get()) or (Checked_Bar_hi.get() and Checked_Pie_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Pie_Graph.set(False)
        Display_Graphs(None)

    def Only_Check_Bar_hi_percent():
        if((Checked_Bar_hi_percent.get() and Checked_Bar_fi.get()) or (Checked_Bar_hi_percent.get() and Checked_Bar_hi.get()) or (Checked_Bar_hi_percent.get() and Checked_Pie_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi.set(False)
            Checked_Pie_Graph.set(False)
        Display_Graphs(None)

    def Only_Check_Pie_Graph():
        if((Checked_Pie_Graph.get() and Checked_Bar_fi.get()) or (Checked_Pie_Graph.get() and Checked_Bar_hi.get()) or (Checked_Pie_Graph.get() and Checked_Bar_hi_percent.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_fi.set(False)
            Checked_Bar_hi_percent.set(False)
        Display_Graphs(None)

    if(__name__ == "__main__"):
        W_Show_Graph = Tk()
    else:
        W_Show_Graph = Toplevel(Father_Window)
        W_Show_Graph.grab_set()

    Icon = PhotoImage(file="Images/icon.png")
    W_Show_Graph.title("Ver Grafico")
    W_Show_Graph.geometry("1000x700+280+90")
    W_Show_Graph.iconphoto(False , Icon)

    Column_Name = []
    Column_Select = ttk.Combobox(W_Show_Graph , values=Column_Name , font=("Courier New" , 13) , width=25 , state="readonly")
    for key in Data_From_Multiple_Columns.keys():
        Column_Name.append(key)

    Widgets = Generate_Graphs(W_Show_Graph , {} , Data_From_Multiple_Columns , Precision , Graphs)

    Column_Select["values"] = Column_Name
    Column_Select.set(Column_Name[0])
    Column_Select.place(x=20 , y=50)
    Column_Select.bind('<<ComboboxSelected>>' , Display_Graphs)

    Checked_Bar_fi = BooleanVar(W_Show_Graph)
    Checked_Bar_hi = BooleanVar(W_Show_Graph)
    Checked_Bar_hi_percent = BooleanVar(W_Show_Graph)

    Checked_Pie_Graph = BooleanVar(W_Show_Graph)

    Checkbox_Show_Bar_fi = Checkbutton(W_Show_Graph , text="Segun fi" , font=("Times New Roman" , 13) , variable=Checked_Bar_fi ,  command=Only_Check_Bar_fi)
    Checkbox_Show_Bar_fi.place(x=60 , y=200)

    Checkbox_Show_Bar_hi = Checkbutton(W_Show_Graph , text="Segun hi" , font=("Times New Roman" , 13) , variable=Checked_Bar_hi , command=Only_Check_Bar_hi)
    Checkbox_Show_Bar_hi.place(x=60 , y=240)

    Checkbox_Show_Bar_hi_percent = Checkbutton(W_Show_Graph , text="Segun hi%" , font=("Times New Roman" , 13) , variable=Checked_Bar_hi_percent , command=Only_Check_Bar_hi_percent)
    Checkbox_Show_Bar_hi_percent.place(x=60 , y=280)

    Checkbox_Pie_Graph = Checkbutton(W_Show_Graph , text="Grafico de pastel" , font=("Times New Roman" , 13) , variable=Checked_Pie_Graph , command=Only_Check_Pie_Graph)
    Checkbox_Pie_Graph.place(x=60 , y=320)

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar Graficos" , font=("Times New Roman" , 13) , width=15 , command= lambda: Create_Windows_Export_Graphs(W_Show_Graph , Graphs , {} , Data_From_Multiple_Columns))
    Btn_Export_Graph.place(x=90 , y=440)

    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()
if __name__ == "__main__":
    Create_Windows_Show_Graphs(None , {} , {"one": [1 , 2] , "two": [1 , 3]} , 1 , {})