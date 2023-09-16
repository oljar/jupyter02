from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter import *


from Model import *
class GetData:

    def __init__(self):
        self.name_col_x_tab0 = StringVar()

        def start_parser():

            diction = {}
            keys = []
            values = []

            with open('nota.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for ln in lines:
                key, value = ln.strip('\n').split('=')
                diction[key] = value

            return diction
        self.name_col_x_tab0.set(start_parser()['name_col_x_tab0'])
        self.name_col_y_tab_0 = start_parser()['name_col_y_tab_0']
        self.name_serial_var = start_parser()['name_serial_var']
        self.polynom_degree = start_parser()['polynom_degree']
        self.step_value = start_parser()['step_value']
        self.scope_down_entry_tab0 = start_parser()['scope_down_entry_tab0']
        self.scope_up_entry_tab0 = start_parser()['scope_up_entry_tab0']
        self.formula_x = start_parser()['formula_x']
        self.formula_y = start_parser()['formula_y']
        self.time_tag = start_parser()['time_tag']
        self.column_x_tag_tab1 = start_parser()['column_x_tag_tab1']
        self.column_y_tag_tab1 = start_parser()['column_y_tag_tab1']
        self.down_scope_tab1 = start_parser()['down_scope_tab1']
        self.up_scope_tab_1 = start_parser()['up_scope_tab_1']
        self.scale_time_chart = start_parser()['scale_time_chart']
        self.name_of_chart = start_parser()['name_of_chart']
        self.name_of_X_axis_tab3 = start_parser()['name_of_X_axis_tab3']
        self.unit_of_X_axis_tab3 = start_parser()['unit_of_X_axis_tab3']
        self.name_of_Y_axis_tab3 = start_parser()['name_of_Y_axis_tab3']
        self.unit_of_Y_axis_tab3 = start_parser()['unit_of_Y_axis_tab3']
        self.scope_down_x_background_entry_tab0 = start_parser()['scope_down_x_background_entry_tab0']
        self.scope_up_x_background_entry_tab0 = start_parser()['scope_up_x_background_entry_tab0']
        self.scope_down_y_background_entry_tab0 = start_parser()['scope_down_y_background_entry_tab0']
        self.scope_up_y_background_entry_tab0 = start_parser()['scope_up_y_background_entry_tab0']
        self.trasparency_picture = start_parser()['trasparency_picture']

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

        name_col_y_tab_0 = diction['name_col_y_tab_0']

    # self.name_serial_var = dicto_parser()['name_serial_var']
    # self.polynom_degree = dicto_parser()['polynom_degree']
    # self.step_value = dicto_parser()['step_value']
    # self.scope_down_entry_tab0 = dicto_parser()['scope_down_entry_tab0']
    # self.scope_up_entry_tab0 = dicto_parser()['scope_up_entry_tab0']
    # self.formula_x = dicto_parser()['formula_x']
    # self.formula_y = dicto_parser()['formula_y']
    # self.time_tag = dicto_parser()['time_tag']
    # self.column_x_tag_tab1 = dicto_parser()['column_x_tag_tab1']
    # self.column_y_tag_tab1 = dicto_parser()['column_y_tag_tab1']
    # self.down_scope_tab1 = dicto_parser()['down_scope_tab1']
    # self.up_scope_tab_1 = dicto_parser()['up_scope_tab_1']
    # self.scale_time_chart = dicto_parser()['scale_time_chart']
    # self.name_of_chart = dicto_parser()['name_of_chart']
    # self.name_of_X_axis_tab3 = dicto_parser()['name_of_X_axis_tab3']
    # self.unit_of_X_axis_tab3 = dicto_parser()['unit_of_X_axis_tab3']
    # self.name_of_Y_axis_tab3 = dicto_parser()['name_of_Y_axis_tab3']
    # self.unit_of_Y_axis_tab3 = dicto_parser()['unit_of_Y_axis_tab3']
    # self.scope_down_x_background_entry_tab0 = dicto_parser()['scope_down_x_background_entry_tab0']
    # self.scope_up_x_background_entry_tab0 = dicto_parser()['scope_up_x_background_entry_tab0']
    # self.scope_down_y_background_entry_tab0 = dicto_parser()['scope_down_y_background_entry_tab0']
    # self.scope_up_y_background_entry_tab0 = dicto_parser()['scope_up_y_background_entry_tab0']
    # self.trasparency_picture = dicto_parser()['trasparency_picture']
