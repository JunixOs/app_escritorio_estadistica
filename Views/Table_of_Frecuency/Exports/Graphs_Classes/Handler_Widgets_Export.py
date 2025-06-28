from tkinter import BooleanVar, StringVar, Checkbutton , Frame , Canvas , Label, ttk , Entry , LEFT

class Handler_Actions:
    def __init__(self , W_Export_Graph):
        self.Dictionary_Main_Checkboxes_Values = None
        self.Dictionary_Subcheckboxes_Values = None
        self.Dictionary_Main_Checkboxes_Widgets = None
        self.Dictionary_Subcheckboxes_Widgets = None

        self.Dictionary_Entry_Titles_Widgets = None
        self.Dictionary_Entry_Titles_Values = None

        self.Checked_Export_All_Graphs = BooleanVar(W_Export_Graph)
        self.Checkbox_Export_All_Graphs = Checkbutton(W_Export_Graph , text="Exportar todos los graficos" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Export_All_Graphs , command=self.Check_All_Checkboxes)

        self.Categories_With_Single_Main_Checkbox = ["Boxplot" , "Pie"]

    def Hidden_Widgets(self):
        self.Checkbox_Export_All_Graphs.place_forget()
        
        self.Text_Entry_For_Axis_x.place_forget()
        self.Entry_For_Axis_x.place_forget()

        self.Notebook_For_Entry_Titles_Section.place_forget()

    def Display_Widgets(self):
        self.Checkbox_Export_All_Graphs.place(x=20 , y=260)

        self.Notebook_For_Entry_Titles_Section.place(x=20 , y=290 , width=840 , height=320)

        self.Text_Entry_For_Axis_x.place(x=30 , y=625)
        self.Entry_For_Axis_x.place(x=175 , y=625)

    def Check_And_Block_Single_Checkbox(self , Category_Graph , Variable_Of_Frecuency):
        Is_All_Checked = []
        for (category_graph , main_checkbox_value) , main_checkbox_widget , dict_with_subcheckboxes , dict_with_entry_titles_values , dict_with_entry_widgets in zip(self.Dictionary_Main_Checkboxes_Values.items() , self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_Subcheckboxes_Values.values() , self.Dictionary_Entry_Titles_Values.values() , self.Dictionary_Entry_Titles_Widgets.values()):
            Is_All_Checked.append(all(value.get() for value in dict_with_subcheckboxes.values()))
            if(category_graph == Category_Graph):
                Is_All_Checked_In_Single_Category = all(value.get() for value in dict_with_subcheckboxes.values())

                if(dict_with_subcheckboxes[f"{Category_Graph}_{Variable_Of_Frecuency}"].get()):
                    dict_with_entry_titles_values[f"{Category_Graph}_{Variable_Of_Frecuency}"].set("")
                    dict_with_entry_widgets[f"{Category_Graph}_{Variable_Of_Frecuency}"][1].config(state="normal")
                else:
                    dict_with_entry_titles_values[f"{Category_Graph}_{Variable_Of_Frecuency}"].set("")
                    dict_with_entry_widgets[f"{Category_Graph}_{Variable_Of_Frecuency}"][1].config(state="disabled")

                if(not category_graph in self.Categories_With_Single_Main_Checkbox):
                    if(Is_All_Checked_In_Single_Category):
                        main_checkbox_value.set(True)
                        main_checkbox_widget.config(state="disabled")
                    else:
                        main_checkbox_value.set(False)
                        main_checkbox_widget.config(state="normal")

        if(all(Is_All_Checked)):
            self.Checked_Export_All_Graphs.set(True)
            self.Checkbox_Export_All_Graphs.config(state="disabled")
        else:
            self.Checked_Export_All_Graphs.set(False)
            self.Checkbox_Export_All_Graphs.config(state="normal")
            

    def Check_And_Block_Multiple_Checkboxes(self , Category_Graph):
        Main_Checkbox = self.Dictionary_Main_Checkboxes_Values[Category_Graph]

        if(all(value.get() for value in self.Dictionary_Main_Checkboxes_Values.values())):
            self.Checked_Export_All_Graphs.set(True)
            self.Checkbox_Export_All_Graphs.config(state="disabled")
        else:
            self.Checked_Export_All_Graphs.set(False)
            self.Checkbox_Export_All_Graphs.config(state="normal")

        for subcheckbox_value , subcheckbox_widget , entry_title_value , entry_widgets in zip(self.Dictionary_Subcheckboxes_Values[f"{Category_Graph}"].values() , self.Dictionary_Subcheckboxes_Widgets[Category_Graph].values() , self.Dictionary_Entry_Titles_Values[Category_Graph].values() , self.Dictionary_Entry_Titles_Widgets[Category_Graph].values()):
                if(Main_Checkbox.get()):
                    subcheckbox_value.set(True)
                    subcheckbox_widget.config(state="disabled")

                    entry_title_value.set("")
                    entry_widgets[1].config(state="normal")
                else:
                    subcheckbox_value.set(False)
                    subcheckbox_widget.config(state="normal")

                    entry_title_value.set("")
                    entry_widgets[1].config(state="disabled")

    def Check_All_Checkboxes(self):
        for (category_graph_name , main_checkbox_value) , main_checkbox_widget , dict_with_subcheckboxes_values , dict_with_subcheckboxes_widgets , dict_with_entry_titles_values , dict_with_entry_widgets in zip(self.Dictionary_Main_Checkboxes_Values.items() , self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_Subcheckboxes_Values.values() , self.Dictionary_Subcheckboxes_Widgets.values() , self.Dictionary_Entry_Titles_Values.values() , self.Dictionary_Entry_Titles_Widgets.values()):
            if(self.Checked_Export_All_Graphs.get()):
                main_checkbox_value.set(True)
                main_checkbox_widget.config(state="disabled")

                for subcheckboxes_values , subcheckboxes_widgets , entry_title_value , entry_widgets in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values() , dict_with_entry_titles_values.values() , dict_with_entry_widgets.values()): 
                    if(not category_graph_name in self.Categories_With_Single_Main_Checkbox):
                        subcheckboxes_values.set(True)
                        subcheckboxes_widgets.config(state="disabled")
                    entry_title_value.set("")
                    entry_widgets[1].config(state="normal")
            else:
                main_checkbox_value.set(False)
                main_checkbox_widget.config(state="normal")

                for subcheckboxes_values , subcheckboxes_widgets , entry_title_value , entry_widgets in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values() , dict_with_entry_titles_values.values() , dict_with_entry_widgets.values()): 
                    if(not category_graph_name in self.Categories_With_Single_Main_Checkbox):
                        subcheckboxes_values.set(False)
                        subcheckboxes_widgets.config(state="normal")
                    entry_title_value.set("")
                    entry_widgets[1].config(state="disabled")


class Container_For_Entry_Title_Widgets:
    def __init__(self , W_Export_Graph , Axis_x_Title):
        self.Dictionary_Entry_Titles_Widgets = None
        self.Dictionary_Text_Sections = None

        self.Style_For_Notebok = ttk.Style()

        # Cambiar el color del fondo del notebook
        self.Style_For_Notebok.configure("Custom.TNotebook", background="#E7E4C1", borderwidth=0)
        self.Style_For_Notebok.configure("Custom.TNotebook.Tab", background="#E7E4C1", padding=10 , borderwidth=0)

        # Color de la pestaña seleccionada
        self.Style_For_Notebok.map("Custom.TNotebook.Tab",
            background=[("selected", "#D6D3AE")],
            foreground=[("selected", "black")],
            expand=[("selected", [1, 1, 1, 0])]
        )

        self.Style_For_Notebok.layout("Custom.TNotebook.Tab", [
            ('Notebook.tab', {'sticky': 'nswe', 'children': [
                ('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children': [
                    ('Notebook.label', {'side': 'top', 'sticky': ''})
                ]})
            ]})
        ])

        self.Notebook_For_Entry_Titles_Section = ttk.Notebook(W_Export_Graph , style="Custom.TNotebook")

        self.Title_For_Axis_x = StringVar(W_Export_Graph)
        self.Title_For_Axis_x.set(Axis_x_Title)
        self.Text_Entry_For_Axis_x = Label(W_Export_Graph , font=("Times New Roman" , 13) , bg="#E7E4C1" , text="Titulo eje x" , justify=LEFT)
        self.Entry_For_Axis_x = Entry(W_Export_Graph , font=("Courier New" , 13) , textvariable=self.Title_For_Axis_x , border=1 , width=65)

    def _bind_mousewheel(self, event):
        self.Canvas_Set.bind("<MouseWheel>", self._on_mousewheel)      # Windows/macOS
        self.Canvas_Set.bind("<Button-4>", self._on_mousewheel_linux)
        self.Canvas_Set.bind("<Button-5>", self._on_mousewheel_linux)

    def _unbind_mousewheel(self, event):
        self.Canvas_Set.unbind("<MouseWheel>")
        self.Canvas_Set.unbind("<Button-4>")
        self.Canvas_Set.unbind("<Button-5>")
    
    def _on_mousewheel(self, event):
        # Windows y macOS
        self.Canvas_Set.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_mousewheel_linux(self, event):
        # Linux (event.num 4 = scroll up, 5 = scroll down)
        if event.num == 4:
            self.Canvas_Set.yview_scroll(-1, "units")
        elif event.num == 5:
            self.Canvas_Set.yview_scroll(1, "units")

    def Insert_Widgets_In_Notebook_Container(self , Dictionary_Main_Checkboxes_Widgets , Dictionary_Subcheckboxes_Widgets , Categories_With_Single_Main_Checkbox , Collection_Of_Frames):
        for widget_frame , dict_with_subcheckboxes_widgets in zip(self.Collection_Of_Frames , self.Dictionary_Subcheckboxes_Widgets.values()):
            max_cols = len(dict_with_subcheckboxes_widgets) if len(dict_with_subcheckboxes_widgets) > 1 else 3

            for col_idx in range(0 , max_cols):
                widget_frame.grid_columnconfigure(col_idx , weight=1)

            for row_idx in range(0 , 5):
                widget_frame.rowconfigure(row_idx , weight=1)
        
        for (category_graph_name , main_checkbox_widget) , dict_with_subcheckboxes_widgets , dict_with_entry_widgets in zip(Dictionary_Main_Checkboxes_Widgets.items() , Dictionary_Subcheckboxes_Widgets.values() , self.Dictionary_Entry_Titles_Widgets.values()):
            idx_row = 0

            match(len(dict_with_subcheckboxes_widgets)):
                case 1:
                    columnspan = 2
                case 2:
                    columnspan = 1
                case _:
                    columnspan = len(dict_with_subcheckboxes_widgets) - 1

            main_checkbox_columnspan = len(dict_with_subcheckboxes_widgets) if len(dict_with_subcheckboxes_widgets) > 1 else 3
            main_checkbox_widget.grid(row=idx_row*2, column=0 , columnspan=main_checkbox_columnspan , padx=(0 , 0) , pady=0 , sticky="n")
            
            if(not category_graph_name in Categories_With_Single_Main_Checkbox):
                idx_row += 1
                for idx_col , subcheckbox_widget in enumerate(dict_with_subcheckboxes_widgets.values()):
                    subcheckbox_widget.grid(row=idx_row*2, column=idx_col , padx=(12 , 0) , pady=0 , sticky="n")
                idx_row += 1
            else:
                idx_row += 1

            for entry_titles_widget in dict_with_entry_widgets.values():
                entry_titles_widget[0].grid(row=idx_row*2 , column=0 , padx=10 , pady=10 , sticky="w")
                entry_titles_widget[1].grid(row=idx_row*2 , column=1 , columnspan=columnspan , padx=10, pady=10 , sticky="ew")
                
                idx_row += 1