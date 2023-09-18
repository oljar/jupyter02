from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter import *


from Model import *
class GetData:

    def __init__(self):
        self.name_col_x_tab0 = StringVar()
        self.name_col_y_tab_0 = StringVar()
        self.name_serial_var = StringVar()
        self.polynom_degree = StringVar()
        self.step_value = StringVar()
        self.scope_down_entry_tab0 = StringVar()
        self.scope_up_entry_tab0 = StringVar()
        self.formula_x = StringVar()
        self.formula_y = StringVar()
        self.time_tag = StringVar()
        self.column_x_tag_tab1 = StringVar()
        self.column_y_tag_tab1 = StringVar()
        self.down_scope_tab1 = StringVar()
        self.up_scope_tab_1 = StringVar()
        self.scale_time_chart = StringVar()
        self.name_of_chart = StringVar()
        self.name_of_X_axis_tab3 = StringVar()
        self.unit_of_X_axis_tab3 = StringVar()
        self.name_of_Y_axis_tab3 = StringVar()
        self.unit_of_Y_axis_tab3 = StringVar()
        self.scope_down_x_background_entry_tab0 = StringVar()
        self.scope_up_x_background_entry_tab0 = StringVar()
        self.scope_down_y_background_entry_tab0 = StringVar()
        self.scope_up_y_background_entry_tab0 = StringVar()
        self.trasparency_picture = StringVar()





        def start_parser():

            diction = {}
            keys = []
            values = []

            with open('default_config.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for ln in lines:
                key, value = ln.strip('\n').split('=')
                diction[key] = value

            return diction
        self.name_col_x_tab0.set(start_parser()['name_col_x_tab0'])
        self.name_col_y_tab_0.set(start_parser()['name_col_y_tab_0'])
        self.name_serial_var.set(start_parser()['name_serial_var'])
        self.polynom_degree.set(start_parser()['polynom_degree'])
        self.step_value.set(start_parser()['step_value'])
        self.scope_down_entry_tab0.set(start_parser()['scope_down_entry_tab0'])
        self.scope_up_entry_tab0.set(start_parser()['scope_up_entry_tab0'])
        self.formula_x.set(start_parser()['formula_x'])
        self.formula_y.set(start_parser()['formula_y'])
        self.time_tag.set(start_parser()['time_tag'])
        self.column_x_tag_tab1.set(start_parser()['column_x_tag_tab1'])
        self.column_y_tag_tab1.set(start_parser()['column_y_tag_tab1'])
        self.down_scope_tab1.set(start_parser()['down_scope_tab1'])
        self.up_scope_tab_1.set(start_parser()['up_scope_tab_1'])
        self.scale_time_chart.set(start_parser()['scale_time_chart'])
        self.name_of_chart.set(start_parser()['name_of_chart'])
        self.name_of_X_axis_tab3.set(start_parser()['name_of_X_axis_tab3'])
        self.unit_of_X_axis_tab3.set(start_parser()['unit_of_X_axis_tab3'])
        self.name_of_Y_axis_tab3.set(start_parser()['name_of_Y_axis_tab3'])
        self.unit_of_Y_axis_tab3.set(start_parser()['unit_of_Y_axis_tab3'])
        self.scope_down_x_background_entry_tab0.set(start_parser()['scope_down_x_background_entry_tab0'])
        self.scope_up_x_background_entry_tab0.set(start_parser()['scope_up_x_background_entry_tab0'])
        self.scope_down_y_background_entry_tab0.set(start_parser()['scope_down_y_background_entry_tab0'])
        self.scope_up_y_background_entry_tab0.set(start_parser()['scope_up_y_background_entry_tab0'])
        self.trasparency_picture.set(start_parser()['trasparency_picture'])

    # #
    #
    def dicto_paresr(self):
        file33 = askopenfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='r',filetypes=[('TXT Files', '*.txt')])

        diction = {}
        keys = []
        values = []

        with open(str(file33.name), 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for ln in lines:
            key, value = ln.strip('\n').split('=')
            diction[key] = value


        self.name_col_x_tab0.set(diction['name_col_x_tab0'])
        self.name_col_y_tab_0.set(diction['name_col_y_tab_0'])
        self.name_serial_var.set(diction['name_serial_var'])
        self.polynom_degree.set(diction['polynom_degree'])
        self.step_value.set(diction['step_value'])
        self.scope_down_entry_tab0.set(diction['scope_down_entry_tab0'])
        self.scope_up_entry_tab0.set(diction['scope_up_entry_tab0'])
        self.formula_x.set(diction['formula_x'])
        self.formula_y.set(diction['formula_y'])
        self.time_tag.set(diction['time_tag'])
        self.column_x_tag_tab1.set(diction['column_x_tag_tab1'])
        self.column_y_tag_tab1.set(diction['column_y_tag_tab1'])
        self.down_scope_tab1.set(diction['down_scope_tab1'])
        self.up_scope_tab_1.set(diction['up_scope_tab_1'])
        self.scale_time_chart.set(diction['scale_time_chart'])
        self.name_of_chart.set(diction['name_of_chart'])
        self.name_of_X_axis_tab3.set(diction['name_of_X_axis_tab3'])
        self.unit_of_X_axis_tab3.set(diction['unit_of_X_axis_tab3'])
        self.name_of_Y_axis_tab3.set(diction['name_of_Y_axis_tab3'])
        self.unit_of_Y_axis_tab3.set(diction['unit_of_Y_axis_tab3'])