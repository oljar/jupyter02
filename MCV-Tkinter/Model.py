import pandas as pd




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

        df1 = pd.read_csv(self.name,sep=';', decimal=',')
        df1.sort_values(by=x_tag, ascending=True)

        return df1







