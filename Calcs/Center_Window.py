from tkinter import messagebox
def Center(Window , Width_Window , Height_Window):
    try:
        Width_Device_Window = Window.winfo_screenwidth()
        Height_Device_Window = Window.winfo_screenheight()
        X_Pos = (Width_Device_Window - Width_Window) // 2
        Y_Pos = (Height_Device_Window - Height_Window) // 2

        Window.geometry(f"{Width_Window}x{Height_Window}+{X_Pos}+{Y_Pos}")

    except Exception:
        messagebox.showerror("Error" , "Hubo un error al centrar la ventana")