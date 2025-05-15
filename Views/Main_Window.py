import sys
import os
# Esto añade la carpeta raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Path_Manager import Get_Resource_Path , Get_Version
from Calcs.Center_Window import Center
import Views.Table_of_Frecuency.Window_Calc_Table_of_Frecuency as W_Calc_Table
import Views.Venn_Diagram.Window_Create_Venn_Diagram as W_Venn_Diagram
import Views.MAS.Window_MAS as W_MAS
from tkinter import *

def On_Closing():
    for widget in Main_Window.winfo_children():
        widget.destroy()
    Main_Window.quit()
    Main_Window.destroy()

Main_Window = Tk()

Image_Right_Section = PhotoImage(file=Get_Resource_Path("Images/normal_distribution.png"))
Image_Right_Section.subsample(10)
Icon = PhotoImage(file=Get_Resource_Path("Images/icon.png"))

Main_Window.geometry("1240x700")
Center(Main_Window , 1240 , 700)
Main_Window.title(f"StatPhi {Get_Version()}")
Main_Window.config(bg="#9DAEC6")
Main_Window.iconphoto(False , Icon)

Right_Section = Label(Main_Window , width=531 , height=691 , bg="#F7EDCB" , image=Image_Right_Section , highlightthickness=2 , highlightbackground="#000000")
Right_Section.place(x=700 , y=0)

BtnFrecuencyTable = Button(Main_Window , text="Crear tabla de frecuencias" , font=("Times New Roman", 14) , command= lambda: W_Calc_Table.Create_Window_Frecuences_Table(Main_Window) , width=30 , bg="#FBCFC6")
BtnFrecuencyTable.place(x=190 , y=220)

BtnVennDiagram = Button(Main_Window , text="Crear Diagramas de Venn" , font=("Times New Roman", 14) , command= lambda: W_Venn_Diagram.Create_Window_Create_Venn_Diagram(Main_Window) , width=30 , bg="#FBCFC6")
BtnVennDiagram.place(x=190 , y=300)

BtnMAS = Button(Main_Window , text="Calcular tamaño de muestra" , font=("Times New Roman", 14) , command= lambda: W_MAS.Create_Window_MAS(Main_Window) , width=30 , bg="#FBCFC6")
BtnMAS.place(x=190 , y=380)

Main_Window.protocol("WM_DELETE_WINDOW", On_Closing)
Main_Window.resizable(False,False)
Main_Window.mainloop()