import pandas as pd
import csv



class Model:
    def __init__(self, name, dist_border, dens_factor, modify_down_scope, modify_up_scope, x_var, y_var, x_math_form, y_math_form, polynominal_degree,limit_up_scope,limit_down_scope,step,
                 time_var_tab1,y1_var_tab1,y2_var_tab1,down_scope_var_tab_1,up_scope_var_tab_1,
                 name_of_chart_var,
                 name_of_X_axis_var, unit_of_X_axis_var,scope_min_of_X_axis_var,scope_max_of_X_axis_var,
                 name_of_Y_axis_var,unit_of_Y_axis_var,scope_min_of_Y_axis_var,scope_max_of_Y_axis_var,
                 name_serial_var,
                 scale_time_chart,
                 scope_down_back_entry_x_var,
                 scope_up_back_entry_x_var,
                 scope_up_back_entry_y_var,
                 scope_down_back_entry_y_var,
                 switch_background,
                 name_picture,
                 trans_picture
                  ):

        self.name = name

        self.dist_border = dist_border
        self.dens_factor = dens_factor
        self.modify_down_scope = modify_down_scope
        self.modify_up_scope = modify_up_scope
        self.limit_down_scope = limit_down_scope
        self.limit_up_scope = limit_up_scope
        self.x_var = x_var
        self.y_var = y_var
        self.x_math_form = x_math_form
        self.y_math_form = y_math_form
        self.polynominal_degree = polynominal_degree
        self.step = step

        self.time_var_tab1 = time_var_tab1
        self.y1_var_tab1 = y1_var_tab1
        self.y2_var_tab1 = y2_var_tab1

        self.down_scope_var_tab_1 = down_scope_var_tab_1
        self.up_scope_var_tab_1 = up_scope_var_tab_1

        self.name_of_chart_var = name_of_chart_var

        self.name_of_X_axis_var  = name_of_X_axis_var
        self.unit_of_X_axis_var = unit_of_X_axis_var
        self.scope_min_of_X_axis_var = scope_min_of_X_axis_var
        self.scope_max_of_X_axis_var = scope_max_of_X_axis_var

        self.name_of_Y_axis_var  = name_of_Y_axis_var
        self.unit_of_Y_axis_var = unit_of_Y_axis_var
        self.scope_min_of_Y_axis_var = scope_min_of_Y_axis_var
        self.scope_max_of_Y_axis_var = scope_max_of_Y_axis_var

        self.name_serial_var = name_serial_var
        self.scale_time_chart = scale_time_chart

        self.scope_down_back_entry_x_var = scope_down_back_entry_x_var
        self.scope_up_back_entry_x_var = scope_up_back_entry_x_var
        self.scope_down_back_entry_y_var = scope_down_back_entry_y_var
        self.scope_up_back_entry_y_var = scope_up_back_entry_y_var
        self.switch_background = switch_background

        self.name_picture = name_picture
        self.trans_picture = trans_picture









    def open_data(self):
        """
        Save the email into a file
        :return:
        """
        # with open('emails.txt', 'a') as f:


        print(f'asdsa{self.name}')
        data_list = []
        with open(self.name, 'r') as f:
            data = csv.reader(f)
            for i in data:
                data_list.append(i)

        result_row_number = []
        for row_number, row in enumerate(data_list):
            if str(self.x_var) in str(row):
                result_row_number.append(row_number)

        print(int(result_row_number[0]))
        df1 = pd.read_csv(self.name, sep=';', decimal=',', header=int(result_row_number[0]))

        df1.sort_values(by=self.x_var, ascending=True)

        return df1

    def open_data_tab_1(self):

        data_list = []
        with open(self.name, 'r') as f:
            data = csv.reader(f)
            for i in data:
                data_list.append(i)

        result_row_number = []
        for row_number, row in enumerate(data_list):
            if str(self.time_var_tab1) in str(row):
                result_row_number.append(row_number)


        df1 = pd.read_csv(self.name, sep=';', decimal=',', header=int(result_row_number[0]))
        df1.sort_values(by=self.time_var_tab1, ascending=True)
        return df1