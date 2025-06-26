from tkinter import BooleanVar, StringVar, Checkbutton , Frame , Canvas , Label, ttk , Entry , LEFT

class Handler_Actions:
    def __init__(self , W_Export_Graph):
        self.Dictionary_Main_Checkboxes_Values = None
        self.Dictionary_Subcheckboxes_Values = None
        self.Dictionary_Main_Checkboxes_Widgets = None
        self.Dictionary_Subcheckboxes_Widgets = None

        self.Frame_Sets = None

        self.Dictionary_Entry_Titles_Widgets = None
        self.Dictionary_Entry_Titles_Values = None

        self.Checked_Export_All_Graphs = BooleanVar(W_Export_Graph)
        self.Checkbox_Export_All_Graphs = Checkbutton(W_Export_Graph , text="Exportar todos los graficos" , font=("Times New Roman" , 13) , bg="#E7E4C1" , variable=self.Checked_Export_All_Graphs , command=self.Check_All_Checkboxes)

        self.Categories_With_Single_Main_Checkbox = ["Boxplot" , "Pie"]

    def Hidden_Widgets(self):
        self.Checkbox_Export_All_Graphs.place_forget()

        for main_checkbox_widget , subcheckbox_dict in zip(self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_Subcheckboxes_Widgets.values()):
            main_checkbox_widget.place_forget()
            for subcheckbox_widget in subcheckbox_dict.values():
                subcheckbox_widget.place_forget()

        self.Frame_Sets.place_forget()

    def Display_Widgets(self):
        self.Checkbox_Export_All_Graphs.place(x=20 , y=260)
        x_pos_checkboxes = 20

        for (category_graph_name , main_checkbox_widget) , subcheckbox_dict in zip(self.Dictionary_Main_Checkboxes_Widgets.items() , self.Dictionary_Subcheckboxes_Widgets.values()):
            y_pos_checkboxes = 310
            main_checkbox_widget.place(x=x_pos_checkboxes , y=y_pos_checkboxes)
            if(category_graph_name in self.Categories_With_Single_Main_Checkbox):
                x_pos_checkboxes += 220
                continue

            for subcheckbox_widget in subcheckbox_dict.values():
                y_pos_checkboxes += 30
                subcheckbox_widget.place(x=x_pos_checkboxes+30 , y=y_pos_checkboxes)
                #x=250 , y=520 , width=630
            x_pos_checkboxes += 220

        self.Frame_Sets.place(x=20 , y=440 , width=860 , height=210)

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

        self.Frame_Sets = Frame(W_Export_Graph , bg="#F7F5DC" , highlightbackground="#000000" , highlightthickness=1)
        self.Frame_Sets.grid_rowconfigure(0, weight=1)
        self.Frame_Sets.grid_columnconfigure(0, weight=1)
        
        self.Canvas_Set = Canvas(self.Frame_Sets, bg="#F7F5DC" , width=840 , height=210)
        self.Canvas_Set.grid(row=0, column=0, sticky="nsew")
        self.Canvas_Set.bind("<Enter>", self._bind_mousewheel)
        self.Canvas_Set.bind("<Leave>", self._unbind_mousewheel)

        self.ScrollBar_Frame = ttk.Scrollbar(self.Frame_Sets, orient="vertical", command=self.Canvas_Set.yview)
        self.ScrollBar_Frame.grid(row=0, column=1, sticky="ns")

        self.Canvas_Set.configure(yscrollcommand=self.ScrollBar_Frame.set)

        self.Content_Frame_Sets = Frame(self.Canvas_Set, width=860 , bg="#F7F5DC")

        self.canvas_window_id = self.Canvas_Set.create_window((0, 0), window=self.Content_Frame_Sets, anchor="nw")
        self.Canvas_Set.bind("<Configure>", lambda e: self.Canvas_Set.itemconfig(self.canvas_window_id, width=e.width))

        self.Width_For_Entry_Titles = 65

        self.Title_For_Axis_x = StringVar(W_Export_Graph)
        self.Title_For_Axis_x.set(Axis_x_Title)
        self.Text_Entry_For_Axis_x = Label(self.Content_Frame_Sets , font=("Times New Roman" , 13) , bg="#F7F5DC" , text="Titulo eje x" , justify=LEFT)
        self.Entry_For_Axis_x = Entry(self.Content_Frame_Sets , font=("Courier New" , 13) , textvariable=self.Title_For_Axis_x , border=1 , width=self.Width_For_Entry_Titles)

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

    def Insert_Widgets_In_Container(self):
        idx = 0

        self.Content_Frame_Sets.columnconfigure(0, weight=1)
        self.Content_Frame_Sets.columnconfigure(1, weight=1)

        for dict_with_entry_widgets , title_main_section in zip(self.Dictionary_Entry_Titles_Widgets.values() , self.Dictionary_Text_Sections.values()):
            if(title_main_section):
                title_main_section.grid(row=idx*2, column=0, columnspan=2 , padx=10, pady=10, sticky="ew")
                idx += 1
            
            for i , entry_titles_widget in enumerate(dict_with_entry_widgets.values()):
                if(i == len(dict_with_entry_widgets) - 1):
                    entry_titles_widget[0].grid(row=idx*2, column=0, padx=10, pady=(10 , 25), sticky="w")
                    entry_titles_widget[1].grid(row=idx*2, column=1, padx=10, pady=(10 , 25), sticky="w")
                else:
                    entry_titles_widget[0].grid(row=idx*2, column=0, padx=10, pady=10, sticky="w")
                    entry_titles_widget[1].grid(row=idx*2, column=1, padx=10, pady=10, sticky="w")
                idx += 1
        
        self.Text_Entry_For_Axis_x.grid(row=idx*2, column=0, padx=10, pady=10, sticky="w")
        self.Entry_For_Axis_x.grid(row=idx*2, column=1, padx=10, pady=10, sticky="w")

        self.Content_Frame_Sets.update_idletasks()
        self.Canvas_Set.config(scrollregion=self.Canvas_Set.bbox("all"))
