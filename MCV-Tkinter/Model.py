import pandas as pd
import csv



class Model:
    def __init__(self, name,dist_border,dens_factor, down_scope, up_scope):
        self.name = name

        self.dist_border = dist_border
        self.dens_factor = dens_factor
        self.down_scope = down_scope
        self.up_scope = up_scope




    def open_data(self):
        """
        Save the email into a file
        :return:
        """
        # with open('emails.txt', 'a') as f:

        x_tag = 'M51: Pa'
        y_tag = 'M53: Pa'
        name = 'data_3.csv'

        value = 'M51: Pa'

        data_list = []
        with open(name, 'r') as f:
            data = csv.reader(f)
            for i in data:
                data_list.append(i)

        result_row_number = []
        for row_number, row in enumerate(data_list):
            if str(x_tag) in str(row):
                result_row_number.append(row_number)

        print(int(result_row_number[0]))
        df1 = pd.read_csv(name, sep=';', decimal=',', header=int(result_row_number[0]))

        df1.sort_values(by=x_tag, ascending=True)

        return df1







