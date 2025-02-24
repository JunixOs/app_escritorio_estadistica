from tkinter import *
import Window_Calc_Table_of_Frecuency as W_Calc_Table
import Window_MAS as W_MAS

def On_Closing():
    Main_Window.quit()
    Main_Window.destroy()

Main_Window = Tk()

Image_Right_Section = PhotoImage(file="Images/normal_distribution.png")
Image_Right_Section.subsample(10)
Icon = PhotoImage(file="Images/icon.png")

Main_Window.geometry("1240x700+135+100")
Main_Window.title("StatPhi beta v1.7")
Main_Window.config(bg="#9DAEC6")
Main_Window.iconphoto(False , Icon)

Right_Section = Label(Main_Window , width=531 , height=691 , bg="#F7EDCB" , image=Image_Right_Section , highlightthickness=2 , highlightbackground="#000000")
Right_Section.place(x=700 , y=0)

BtnFrecuencyTable = Button(Main_Window , text="Crear tabla de frecuencias" , font=("Times New Roman", 14) , command= lambda: W_Calc_Table.Create_Window_Frecuences_Table(Main_Window) , width=30 , bg="#FBCFC6")
BtnFrecuencyTable.place(x=190,y=260)

BtnMAS = Button(Main_Window , text="Calcular tamaño de muestra" , font=("Times New Roman", 14) , command= lambda: W_MAS.Create_Window_MAS(Main_Window) , width=30 , bg="#FBCFC6")
BtnMAS.place(x=190 , y=330)

Main_Window.protocol("WM_DELETE_WINDOW", On_Closing)
Main_Window.resizable(False,False)
Main_Window.mainloop()