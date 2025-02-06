from tkinter import *
from Window_Calc_Table_of_Frecuency import Create_Window_Frecuences_Table

Main_Window = Tk()

Image_Right_Section = PhotoImage(file="Images/normal_distribution.png")
Image_Right_Section.subsample(10)
Icon = PhotoImage(file="Images/icon.png")

Main_Window.geometry("1240x700+135+100")
Main_Window.title("Seleccion")
Main_Window.config(bg="#9DAEC6")
Main_Window.iconphoto(False,Icon)

Right_Section = Label(Main_Window , width=531 , height=691 , bg="#F7EDCB" , image=Image_Right_Section , highlightthickness=2 , highlightbackground="#000000")
Right_Section.place(x=700 , y=0)

BtnFrecuencyTable = Button(Main_Window,text="Crear tabla de frecuencias", font=("Times New Roman", 14) , command=Create_Window_Frecuences_Table , width=30)
BtnFrecuencyTable.place(x=190,y=300)

Main_Window.resizable(False,False)
Main_Window.mainloop()