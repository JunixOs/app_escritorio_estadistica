import sys
import os
import copy
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from Calcs.Graphs.Calc_Bar_Pie_Graphs import Draw_Graph_for_Each_Variable
from Calcs.Graphs.Calc_Boxplot import Draw_Boxplot_For_Single_Column_Data
from Window_Export_Graph import Create_Windows_Export_Graphs
from Window_Create_Multiple_Graphs import Create_Window_Multiple_Graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def Change_Key(dictionary, old_key, new_key):
    """ No modifica el diccionarrio, sino que genera uno nuevo , pero con las claves moficiadas """
    return {clave if clave != old_key else new_key: valor for clave, valor in dictionary.items()}

def Create_Windows_Show_Graphs(Father_Window , Results_From_Single_Column , Results_From_Multiple_Columns , Precision , Graphs):
    """ Esta es la funcion principal del modulo """
    if(Precision > 3):
        Precision = 3

    if(Results_From_Single_Column):
        W_For_Single_Colum_Data(Father_Window , Results_From_Single_Column , Precision , Graphs)
    elif(Results_From_Multiple_Columns):
        W_For_Multiple_Column_Data(Father_Window , Results_From_Multiple_Columns , Precision , Graphs)
    else:
        raise Exception("No se encontraron los datos para generar los graficos.")

def Generate_Graphs(Root_Window , Results_From_Single_Column , Results_From_Multiple_Columns , Precision , Graphs):
    if(Results_From_Single_Column != {}):
        Copy_Data = copy.deepcopy(Results_From_Single_Column)
        Data_Column_Name = None

        if(len(Copy_Data) == 1 and isinstance(Copy_Data , dict)):
            Data_Column_Name , Copy_Data = next(iter(Copy_Data.items()))
        Dictionary_Widgets = {}

        if(("Frecuences_Cuant_For_Many_Values" in Copy_Data) and not isinstance(Copy_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][0][0] , str)):
            for a in range(0 , len(Copy_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"])):
                if(a != len(Copy_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"]) - 1):
                    Copy_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(Copy_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(Copy_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" >"
                else:
                    Copy_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(Copy_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(Copy_Data["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" ]"
        try:
            Graph = Draw_Graph_for_Each_Variable(Copy_Data , Precision , Data_Column_Name)

            if(Graphs == {}):
                bar_fi , pie_graph = Graph.Draw_Graph("fi")
                bar_hi = Graph.Draw_Graph("hi")
                bar_hi_percent = Graph.Draw_Graph("hi_percent")
                if("Frecuences_Cuant_For_Many_Values" in Copy_Data):
                    boxplot_graph = Draw_Boxplot_For_Single_Column_Data(Copy_Data["Variables_Cuant_For_Many_Values"]["Data_List"] , Data_Column_Name)
                    Graphs["boxplot_graph"] = boxplot_graph
                elif("Frecuences_Cuant_Normal_Extended" in Copy_Data):
                    boxplot_graph = Draw_Boxplot_For_Single_Column_Data(Copy_Data["Variables_Cuant_Normal_Extended"]["Data_List"] , Data_Column_Name)
                    Graphs["boxplot_graph"] = boxplot_graph

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

            if("boxplot_graph" in Graphs):
                Widget_boxplot_graph = FigureCanvasTkAgg(Graphs["boxplot_graph"] , master=Root_Window)
                Widget_boxplot_graph.draw()

                Dictionary_Widgets = dict([
                    ("bar_fi" , Widget_bar_fi),
                    ("bar_hi" , Widget_bar_hi),
                    ("bar_hi_percent" , Widget_bar_hi_percent),
                    ("pie_graph" , Widget_pie_graph),
                    ("boxplot_graph" , Widget_boxplot_graph),
                ])
            else:
                Dictionary_Widgets = dict([
                    ("bar_fi" , Widget_bar_fi),
                    ("bar_hi" , Widget_bar_hi),
                    ("bar_hi_percent" , Widget_bar_hi_percent),
                    ("pie_graph" , Widget_pie_graph),
                ])
        except Exception as e:
            messagebox.showerror("Error" , f"{e}")

    elif(Results_From_Multiple_Columns != {}):
        Copy_Data = copy.deepcopy(Results_From_Multiple_Columns)
        Dictionary_Widgets = {}
        if(Graphs == {}):
            Is_Graphs_Empty = True
        else:
            Is_Graphs_Empty = False

        for key , value in Copy_Data.items():
            if(("Frecuences_Cuant_For_Many_Values" in value) and not isinstance(value["Frecuences_Cuant_For_Many_Values"]["Intervals"][0][0] , str)):
                for a in range(0 , len(value["Frecuences_Cuant_For_Many_Values"]["Intervals"])):
                    if(a != len(value["Frecuences_Cuant_For_Many_Values"]["Intervals"]) - 1):
                        value["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(value["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(value["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" >"
                    else:
                        value["Frecuences_Cuant_For_Many_Values"]["Intervals"][a] = "[ " + str(value["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][0]) +" , " + str(value["Frecuences_Cuant_For_Many_Values"]["Intervals"][a][1]) +" ]"
            try:
                Graph = Draw_Graph_for_Each_Variable(value , Precision , key)
                if(Is_Graphs_Empty):
                    bar_fi , pie_graph = Graph.Draw_Graph("fi")
                    bar_hi = Graph.Draw_Graph("hi")
                    bar_hi_percent = Graph.Draw_Graph("hi_percent")
                    if("Frecuences_Cuant_For_Many_Values" in value):
                        boxplot_graph = Draw_Boxplot_For_Single_Column_Data(value["Variables_Cuant_For_Many_Values"]["Data_List"] , key)
                        Graphs["boxplot_graph"] = boxplot_graph
                        Graphs[f"{key}"] = {
                            "bar_fi" : bar_fi,
                            "bar_hi" : bar_hi,
                            "bar_hi_percent" : bar_hi_percent,
                            "pie_graph" : pie_graph,
                            "boxplot_graph" : boxplot_graph,
                        }
                    elif("Frecuences_Cuant_Normal_Extended" in value):
                        boxplot_graph = Draw_Boxplot_For_Single_Column_Data(value["Variables_Cuant_Normal_Extended"]["Data_List"] , key)
                        Graphs["boxplot_graph"] = boxplot_graph
                        Graphs[f"{key}"] = {
                            "bar_fi" : bar_fi,
                            "bar_hi" : bar_hi,
                            "bar_hi_percent" : bar_hi_percent,
                            "pie_graph" : pie_graph,
                            "boxplot_graph" : boxplot_graph,
                        }
                    else:
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

                if("boxplot_graph" in Graphs[f"{key}"]):
                    Widget_boxplot_graph = FigureCanvasTkAgg(Graphs[f"{key}"]["boxplot_graph"] , master=Root_Window)
                    Widget_boxplot_graph.draw()
                    Dictionary_Widgets[f"{key}"] = {
                        "bar_fi" : Widget_bar_fi,
                        "bar_hi" : Widget_bar_hi,
                        "bar_hi_percent" : Widget_bar_hi_percent,
                        "pie_graph" : Widget_pie_graph,
                        "boxplot_graph" : Widget_boxplot_graph,
                    }
                else:
                    Dictionary_Widgets[f"{key}"] = {
                        "bar_fi" : Widget_bar_fi,
                        "bar_hi" : Widget_bar_hi,
                        "bar_hi_percent" : Widget_bar_hi_percent,
                        "pie_graph" : Widget_pie_graph,
                    }
            except Exception as e:
                messagebox.showerror("Error" , f"{e}")

    return Dictionary_Widgets

def W_For_Single_Colum_Data(Father_Window , Results_From_Single_Column , Precision , Graphs):

    def Back(W_Show_Graph):
        Widgets.clear()
        W_Show_Graph.grab_release()
        W_Show_Graph.quit()
        W_Show_Graph.destroy()

    def Hidden_Graphs():
        for widget in Widgets.values():
            widget.get_tk_widget().place_forget()

    def Display_Graphs():
        Hidden_Graphs()

        if(Checked_Bar_fi.get()):
            Widgets["bar_fi"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Bar_hi.get()):
            Widgets["bar_hi"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Bar_hi_percent.get()):
            Widgets["bar_hi_percent"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Pie_Graph.get()):
            Widgets["pie_graph"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Boxplot_Graph.get()):
            Widgets["boxplot_graph"].get_tk_widget().place(x=320 , y=0)

    def Only_Check_Bar_fi():
        if((Checked_Bar_fi.get() and Checked_Bar_hi.get()) or (Checked_Bar_fi.get() and Checked_Bar_hi_percent.get()) or (Checked_Bar_fi.get() and Checked_Pie_Graph.get()) or (Checked_Bar_fi.get() and Checked_Boxplot_Graph.get())):
            Checked_Bar_hi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Pie_Graph.set(False)
            Checked_Boxplot_Graph.set(False)
        Display_Graphs()

    def Only_Check_Bar_hi():
        if((Checked_Bar_hi.get() and Checked_Bar_fi.get()) or (Checked_Bar_hi.get() and Checked_Bar_hi_percent.get()) or (Checked_Bar_hi.get() and Checked_Pie_Graph.get()) or (Checked_Bar_hi.get() and Checked_Boxplot_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Pie_Graph.set(False)
            Checked_Boxplot_Graph.set(False)
        Display_Graphs()

    def Only_Check_Bar_hi_percent():
        if((Checked_Bar_hi_percent.get() and Checked_Bar_fi.get()) or (Checked_Bar_hi_percent.get() and Checked_Bar_hi.get()) or (Checked_Bar_hi_percent.get() and Checked_Pie_Graph.get()) or (Checked_Bar_hi_percent.get() and Checked_Boxplot_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi.set(False)
            Checked_Pie_Graph.set(False)
            Checked_Boxplot_Graph.set(False)
        Display_Graphs()

    def Only_Check_Pie_Graph():
        if((Checked_Pie_Graph.get() and Checked_Bar_fi.get()) or (Checked_Pie_Graph.get() and Checked_Bar_hi.get()) or (Checked_Pie_Graph.get() and Checked_Bar_hi_percent.get()) or (Checked_Pie_Graph.get() and Checked_Boxplot_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Boxplot_Graph.set(False)
        Display_Graphs()

    def Only_Check_Boxplot_Graph():
        if((Checked_Boxplot_Graph.get() and Checked_Bar_fi.get()) or (Checked_Boxplot_Graph.get() and Checked_Bar_hi.get()) or (Checked_Boxplot_Graph.get() and Checked_Bar_hi_percent.get()) or (Checked_Boxplot_Graph.get() and Checked_Pie_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Pie_Graph.set(False)
        Display_Graphs()

    if __name__ == "__main__":
        W_Show_Graph = Tk()
    else:
        """ Hacer la ventana mas grande para que los graficos quepan mejor, modficiar el tamaño al exportar los graficos """
        """ Reducir a una sola unica funcion que administre todo. """
        W_Show_Graph = Toplevel(Father_Window)
        W_Show_Graph.title("Ver graficos")
        W_Show_Graph.geometry("1000x700+270+100")
        W_Show_Graph.grab_set()
        Icon = PhotoImage(file="Images/icon.png")
        W_Show_Graph.iconphoto(False , Icon)

        Widgets = Generate_Graphs(W_Show_Graph , Results_From_Single_Column , {} , Precision , Graphs)

    W_Show_Graph.protocol("WM_DELETE_WINDOW", lambda: Back(W_Show_Graph))

    Checked_Bar_fi = BooleanVar(W_Show_Graph)
    Checked_Bar_hi = BooleanVar(W_Show_Graph)
    Checked_Bar_hi_percent = BooleanVar(W_Show_Graph)

    Checked_Pie_Graph = BooleanVar(W_Show_Graph)
    Checked_Boxplot_Graph = BooleanVar(W_Show_Graph)
    Checked_Boxplot_Graph.set(False)

    Checkbox_Show_Bar_fi = Checkbutton(W_Show_Graph , text="Segun fi" , font=("Times New Roman" , 13) , variable=Checked_Bar_fi ,  command=Only_Check_Bar_fi)
    Checkbox_Show_Bar_fi.place(x=60 , y=220)

    Checkbox_Show_Bar_hi = Checkbutton(W_Show_Graph , text="Segun hi" , font=("Times New Roman" , 13) , variable=Checked_Bar_hi , command=Only_Check_Bar_hi)
    Checkbox_Show_Bar_hi.place(x=60 , y=260)

    Checkbox_Show_Bar_hi_percent = Checkbutton(W_Show_Graph , text="Segun hi%" , font=("Times New Roman" , 13) , variable=Checked_Bar_hi_percent , command=Only_Check_Bar_hi_percent)
    Checkbox_Show_Bar_hi_percent.place(x=60 , y=300)

    Checkbox_Pie_Graph = Checkbutton(W_Show_Graph , text="Grafico de pastel" , font=("Times New Roman" , 13) , variable=Checked_Pie_Graph , command=Only_Check_Pie_Graph)
    Checkbox_Pie_Graph.place(x=60 , y=340)

    if("boxplot_graph" in Widgets):
        Checkbox_Boxplot_Graph = Checkbutton(W_Show_Graph , text="Grafico de cajas" , font=("Times New Roman" , 13) , variable=Checked_Boxplot_Graph , command=Only_Check_Boxplot_Graph)
        Checkbox_Boxplot_Graph.place(x=60 , y=380)
        

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar Graficos" , font=("Times New Roman" , 13) , width=15 , command= lambda: Create_Windows_Export_Graphs(W_Show_Graph , Graphs , Results_From_Single_Column , {}))
    Btn_Export_Graph.place(x=90 , y=440)

    Btn_Create_And_Export_Multiple_Graphs = Button(W_Show_Graph , text="Crear y Exportar\nMultiples Graficos" , font=("Times New Roman" , 13) , width=24 , justify="center" , command= lambda: Create_Window_Multiple_Graphs(W_Show_Graph))
    Btn_Create_And_Export_Multiple_Graphs.place(x=50 , y=480)

    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()

def W_For_Multiple_Column_Data(Father_Window , Results_From_Multiple_Columns , Precision , Graphs):

    def Back(W_Show_Graph):
        Widgets.clear()
        W_Show_Graph.grab_release()
        W_Show_Graph.quit()
        W_Show_Graph.destroy()

    def Hidden_Graphs():
        for m_graph in Widgets.values():
            for graph in m_graph.values():
                graph.get_tk_widget().place_forget()

    def Display_Graphs(Event):
        Selection = Column_Select.get()
        Display_Checkbox_Boxplot(Selection)
        Hidden_Graphs()

        if(Checked_Bar_fi.get()):
            Widgets[f"{Selection}"]["bar_fi"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Bar_hi.get()):
            Widgets[f"{Selection}"]["bar_hi"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Bar_hi_percent.get()):
            Widgets[f"{Selection}"]["bar_hi_percent"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Pie_Graph.get()):
            Widgets[f"{Selection}"]["pie_graph"].get_tk_widget().place(x=320 , y=0)
        elif(Checked_Boxplot_Graph.get()):
            Widgets[f"{Selection}"]["boxplot_graph"].get_tk_widget().place(x=320 , y=0)

    def Only_Check_Bar_fi():
        if((Checked_Bar_fi.get() and Checked_Bar_hi.get()) or (Checked_Bar_fi.get() and Checked_Bar_hi_percent.get()) or (Checked_Bar_fi.get() and Checked_Pie_Graph.get()) or (Checked_Bar_fi.get() and Checked_Boxplot_Graph.get())):
            Checked_Bar_hi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Pie_Graph.set(False)
            Checked_Boxplot_Graph.set(False)
        Display_Graphs(None)

    def Only_Check_Bar_hi():
        if((Checked_Bar_hi.get() and Checked_Bar_fi.get()) or (Checked_Bar_hi.get() and Checked_Bar_hi_percent.get()) or (Checked_Bar_hi.get() and Checked_Pie_Graph.get()) or (Checked_Bar_hi.get() and Checked_Boxplot_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Pie_Graph.set(False)
            Checked_Boxplot_Graph.set(False)
        Display_Graphs(None)

    def Only_Check_Bar_hi_percent():
        if((Checked_Bar_hi_percent.get() and Checked_Bar_fi.get()) or (Checked_Bar_hi_percent.get() and Checked_Bar_hi.get()) or (Checked_Bar_hi_percent.get() and Checked_Pie_Graph.get()) or (Checked_Bar_hi_percent.get() and Checked_Boxplot_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi.set(False)
            Checked_Pie_Graph.set(False)
            Checked_Boxplot_Graph.set(False)
        Display_Graphs(None)

    def Only_Check_Pie_Graph():
        if((Checked_Pie_Graph.get() and Checked_Bar_fi.get()) or (Checked_Pie_Graph.get() and Checked_Bar_hi.get()) or (Checked_Pie_Graph.get() and Checked_Bar_hi_percent.get()) or (Checked_Pie_Graph.get() and Checked_Boxplot_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_fi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Boxplot_Graph.set(False)
        Display_Graphs(None)

    def Only_Check_Boxplot_Graph():
        if((Checked_Boxplot_Graph.get() and Checked_Bar_fi.get()) or (Checked_Boxplot_Graph.get() and Checked_Bar_hi.get()) or (Checked_Boxplot_Graph.get() and Checked_Bar_hi_percent.get()) or (Checked_Boxplot_Graph.get() and Checked_Pie_Graph.get())):
            Checked_Bar_fi.set(False)
            Checked_Bar_hi.set(False)
            Checked_Bar_hi_percent.set(False)
            Checked_Pie_Graph.set(False)
        Display_Graphs(None)

    def Display_Checkbox_Boxplot(Selection):
        if("boxplot_graph" in Widgets[f"{Selection}"]):
            Checkbox_Boxplot_Graph.place(x=60 , y=380)
        else:
            Checkbox_Boxplot_Graph.place_forget()
            Checked_Boxplot_Graph.set(False)

    if(__name__ == "__main__"):
        W_Show_Graph = Tk()
    else:
        W_Show_Graph = Toplevel(Father_Window)
        W_Show_Graph.grab_set()

    Icon = PhotoImage(file="Images/icon.png")
    W_Show_Graph.title("Ver Grafico")
    W_Show_Graph.geometry("1000x700+270+100")
    W_Show_Graph.iconphoto(False , Icon)
    W_Show_Graph.protocol("WM_DELETE_WINDOW", lambda: Back(W_Show_Graph))

    Column_Name = []
    Column_Select = ttk.Combobox(W_Show_Graph , values=Column_Name , font=("Courier New" , 13) , width=25 , state="readonly")
    for key in Results_From_Multiple_Columns.keys():
        Column_Name.append(key)

    Widgets = Generate_Graphs(W_Show_Graph , {} , Results_From_Multiple_Columns , Precision , Graphs)

    Column_Select["values"] = Column_Name
    Column_Select.set(Column_Name[0])
    Column_Select.place(x=20 , y=50)
    Column_Select.bind('<<ComboboxSelected>>' , Display_Graphs)

    Checked_Bar_fi = BooleanVar(W_Show_Graph)
    Checked_Bar_hi = BooleanVar(W_Show_Graph)
    Checked_Bar_hi_percent = BooleanVar(W_Show_Graph)

    Checked_Pie_Graph = BooleanVar(W_Show_Graph)
    Checked_Boxplot_Graph = BooleanVar(W_Show_Graph)
    Checked_Boxplot_Graph.set(False)

    Checkbox_Show_Bar_fi = Checkbutton(W_Show_Graph , text="Segun fi" , font=("Times New Roman" , 13) , variable=Checked_Bar_fi ,  command=Only_Check_Bar_fi)
    Checkbox_Show_Bar_fi.place(x=60 , y=200)

    Checkbox_Show_Bar_hi = Checkbutton(W_Show_Graph , text="Segun hi" , font=("Times New Roman" , 13) , variable=Checked_Bar_hi , command=Only_Check_Bar_hi)
    Checkbox_Show_Bar_hi.place(x=60 , y=240)

    Checkbox_Show_Bar_hi_percent = Checkbutton(W_Show_Graph , text="Segun hi%" , font=("Times New Roman" , 13) , variable=Checked_Bar_hi_percent , command=Only_Check_Bar_hi_percent)
    Checkbox_Show_Bar_hi_percent.place(x=60 , y=280)

    Checkbox_Pie_Graph = Checkbutton(W_Show_Graph , text="Grafico de pastel" , font=("Times New Roman" , 13) , variable=Checked_Pie_Graph , command=Only_Check_Pie_Graph)
    Checkbox_Pie_Graph.place(x=60 , y=320)

    Checkbox_Boxplot_Graph = Checkbutton(W_Show_Graph , text="Grafico de cajas" , font=("Times New Roman" , 13) , variable=Checked_Boxplot_Graph , command=Only_Check_Boxplot_Graph)
    Display_Checkbox_Boxplot(Column_Name[0])

    Btn_Export_Graph = Button(W_Show_Graph , text="Exportar Graficos" , font=("Times New Roman" , 13) , width=15 , command= lambda: Create_Windows_Export_Graphs(W_Show_Graph , Graphs , {} , Results_From_Multiple_Columns))
    Btn_Export_Graph.place(x=90 , y=440)

    Btn_Create_And_Export_Multiple_Graphs = Button(W_Show_Graph , text="Crear y Exportar\nMultiples Graficos" , font=("Times New Roman" , 13) , width=24 , justify="center" , command= lambda: Create_Window_Multiple_Graphs(W_Show_Graph))
    Btn_Create_And_Export_Multiple_Graphs.place(x=50 , y=500)

    W_Show_Graph.resizable(False , False)
    W_Show_Graph.mainloop()
    W_Show_Graph.quit()

if __name__ == "__main__":
    Create_Windows_Show_Graphs(None , {} , {"one": [1 , 2] , "two": [1 , 3]} , 1 , {})