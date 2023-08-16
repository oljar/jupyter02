import pandas as pd
import csv



class Model:
    def __init__(self, name, dist_border, dens_factor, modify_down_scope, modify_up_scope, x_var, y_var, x_math_form, y_math_form, polynominal_degree,limit_up_scope,limit_down_scope,step):
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






    def open_data(self):
        """
        Save the email into a file
        :return:
        """
        # with open('emails.txt', 'a') as f:








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





