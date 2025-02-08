from tkinter import *
class Frecuences_Error(Exception):
    def __init__(self, error_id , information):
        self.error_id = error_id
        self.information = information

    def Create_Window(self, Father_Window):
        
        if __name__ == "__main__":
            Win_Err = Tk()
        else:
            Win_Err = Toplevel(Father_Window)
        Error_Icon = PhotoImage(file="Images/error_icon.png")
            
        Win_Err.geometry("700x100+400+400")
        Win_Err.title("Error")
        Win_Err.iconphoto(False,Error_Icon)

        Text = Label(Win_Err , text=f"{self.error_id} \n {self.information}" , font=("Times New Roman" , 13) , justify=CENTER)
        Text.pack(fill="both")

        Btn_Close = Button(Win_Err , text="Cerrar" , font=("Times New Roman" , 13) , command= Win_Err.destroy)
        Btn_Close.place(x=330 , y=60)

        Win_Err.protocol("WM_DELETE_WINDOW" , Win_Err.destroy)
        Win_Err.grab_set()
        Win_Err.resizable(False,False)
        Win_Err.mainloop()

if __name__ == "__main__":
    e = Frecuences_Error("MESSAGE OF ERROR SDASADASDFASD" , "ERROR ASFASFASDSADASDASDSAD")
    e.Create_Window(None)