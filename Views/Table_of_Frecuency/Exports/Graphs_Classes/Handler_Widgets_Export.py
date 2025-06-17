from tkinter import BooleanVar, Checkbutton

class Handler_Actions:
    def __init__(self , W_Export_Graph):
        self.Dictionary_Main_Checkboxes_Values = None
        self.Dictionary_Subcheckboxes_Values = None
        self.Dictionary_Main_Checkboxes_Widgets = None
        self.Dictionary_Subcheckboxes_Widgets = None

        self.Main_Container = None
        self.Frame_Sets = None
        self.Canvas_Set = None
        self.ScrollBar_Frame = None
        self.Content_Frame_Sets = None

        self.Dictionary_Entry_Titles_Widgets = None
        self.Dictionary_Entry_Titles_Values = None

        self.Checked_Export_All_Graphs = BooleanVar(W_Export_Graph)
        self.Checkbox_Export_All_Graphs = Checkbutton(W_Export_Graph , text="Exportar todos los graficos" , font=("Times New Roman" , 13) , variable=self.Checked_Export_All_Graphs , command=self.Check_All_Checkboxes)

        self.Categories_With_Single_Main_Checkbox = ["Boxplot" , "Pie"]

    def Hidden_Widgets(self):
        self.Checkbox_Export_All_Graphs.place_forget()

        for main_checkbox_widget , subcheckbox_dict in zip(self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_Subcheckboxes_Widgets.values()):
            main_checkbox_widget.place_forget()
            for subcheckbox_widget in subcheckbox_dict.values():
                subcheckbox_widget.place_forget()

        self.Main_Container.place_forget()
        self.Frame_Sets.place_forget()
        self.Canvas_Set.grid_forget()
        self.ScrollBar_Frame.grid_forget()
        self.Content_Frame_Sets.place_forget()

    def Display_Widgets(self):
        self.Checkbox_Export_All_Graphs.place(x=20 , y=230)
        x_pos_checkboxes = 20

        for (category_name , main_checkbox_widget) , subcheckbox_dict in zip(self.Dictionary_Main_Checkboxes_Widgets.items() , self.Dictionary_Subcheckboxes_Widgets.values()):
            y_pos_checkboxes = 290
            main_checkbox_widget.place(x=x_pos_checkboxes , y=y_pos_checkboxes)
            if(category_name in self.Categories_With_Single_Main_Checkbox):
                x_pos_checkboxes += 220
                continue

            for subcheckbox_widget in subcheckbox_dict.values():
                y_pos_checkboxes += 30
                subcheckbox_widget.place(x=x_pos_checkboxes+30 , y=y_pos_checkboxes)
                #x=250 , y=520 , width=630
            x_pos_checkboxes += 220

        self.Main_Container.place(x=20 , y=510 , width=860 , height=150)
        self.Frame_Sets.place(x=20 , y=510 , width=860 , height=100)
        self.Canvas_Set.grid(row=0, column=0, sticky="nsew")
        self.ScrollBar_Frame.grid(row=0, column=1, sticky="ns")
        self.Content_Frame_Sets.place(x=20 , y=510)

    def Check_And_Block_Single_Checkbox(self , Category_Graph , Variable_Of_Frecuency):
        Is_All_Checked = []
        for (category_graph , main_checkbox_value) , main_checkbox_widget , dict_with_subcheckboxes , dict_with_entry_titles_values , dict_with_entry_widgets in zip(self.Dictionary_Main_Checkboxes_Values.items() , self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_Subcheckboxes_Values.values() , self.Dictionary_Entry_Titles_Values.values() , self.Dictionary_Entry_Titles_Widgets.values()):
            Is_All_Checked = all(value.get() for value in dict_with_subcheckboxes.values())
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

        if(Is_All_Checked):
            self.Checked_Export_All_Graphs.set(True)
            self.Checkbox_Export_All_Graphs.config(state="disabled")
        else:
            self.Checked_Export_All_Graphs.set(False)
            self.Checkbox_Export_All_Graphs.config(state="normal")
            

    def Check_And_Block_Multiple_Checkboxes(self , Category_Graph):
        for category_name , dict_with_subcheckboxes_values , dict_with_subcheckboxes_widgets , dict_with_entry_titles_values , dict_with_entry_widgets in zip(self.Dictionary_Main_Checkboxes_Values.keys() , self.Dictionary_Subcheckboxes_Values.values() , self.Dictionary_Subcheckboxes_Widgets.values() , self.Dictionary_Entry_Titles_Values.values() , self.Dictionary_Entry_Titles_Widgets.values()):
            for subcheckboxes_values , subcheckboxes_widgets , entry_titles_values , entry_widgets in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values() , dict_with_entry_titles_values.values() , dict_with_entry_widgets.values()):
                if(category_name == Category_Graph):
                    subcheckboxes_values.set(True)
                    subcheckboxes_widgets.config(state="disabled")

                    entry_titles_values.set("")
                    entry_widgets[1].config(state="normal")
                else:
                    subcheckboxes_values.set(False)
                    subcheckboxes_widgets.config(state="normal")

                    entry_titles_values.set("")
                    entry_widgets[1].config(state="disabled")

    def Check_All_Checkboxes(self):
        for (category_name , main_checkbox_value) , main_checkbox_widget , dict_with_subcheckboxes_values , dict_with_subcheckboxes_widgets in zip(self.Dictionary_Main_Checkboxes_Values.items() , self.Dictionary_Main_Checkboxes_Widgets.values() , self.Dictionary_Subcheckboxes_Values.values() , self.Dictionary_Subcheckboxes_Widgets.values()):
            if(self.Checked_Export_All_Graphs.get()):
                main_checkbox_value.set(True)
                main_checkbox_widget.config(state="disabled")
                if(category_name in self.Categories_With_Single_Main_Checkbox):
                    continue

                for subcheckboxes_values , subcheckboxes_widgets in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()): 
                    subcheckboxes_values.set(True)
                    subcheckboxes_widgets.config(state="disabled")
            else:
                main_checkbox_value.set(False)
                main_checkbox_widget.config(state="normal")
                if(category_name in self.Categories_With_Single_Main_Checkbox):
                    continue

                for subcheckboxes_values , subcheckboxes_widgets in zip(dict_with_subcheckboxes_values.values() , dict_with_subcheckboxes_widgets.values()): 
                    subcheckboxes_values.set(False)
                    subcheckboxes_widgets.config(state="normal")
