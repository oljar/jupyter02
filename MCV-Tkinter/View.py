import re
import tkinter as tk
from tkinter import ttk
import source
from Controller import Controller
from Model import Model
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile



window = tk.Tk()
window.title("Data modificator")
window.geometry('790x700')

tab_parent = ttk.Notebook(window)
tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)





class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


        self.open_name_var = StringVar()
        self.save_name_var = StringVar()
        self.dist_border_var = StringVar()
        self.total_up_scope_var = StringVar()
        self.total_down_scope_var = StringVar()

        self.up_scope_var = tk.StringVar()
        self.down_scope_var = tk.StringVar()

        self.density_var = tk.StringVar()
        self.x_var = tk.StringVar()
        self.y_var = tk.StringVar()

        self.x_math_form = tk.StringVar()
        self.y_math_form  = tk.StringVar()

        self.polynominal_degree = tk.StringVar()

        self.step = tk.StringVar()
        #################################

        self.time_var_tab1 = tk.StringVar()
        self.y1_var_tab1 = tk.StringVar()
        self.y2_var_tab1 = tk.StringVar()

        self.up_scope_var_tab_1 = tk.StringVar()
        self.down_scope_var_tab_1 = tk.StringVar()

        self.switch_modyfied_export = False

        self.name_of_chart_var = tk.StringVar()

        self.name_of_X_axis_var  = tk.StringVar()
        self.unit_of_X_axis_var = tk.StringVar()
        self.scope_min_of_X_axis_var = tk.StringVar()
        self.scope_max_of_X_axis_var = tk.StringVar()



        self.name_of_Y_axis_var  = tk.StringVar()
        self.unit_of_Y_axis_var = tk.StringVar()
        self.scope_min_of_Y_axis_var = tk.StringVar()
        self.scope_max_of_Y_axis_var = tk.StringVar()

        self.name_serial_var = tk.StringVar()














        # create widgets
        ####################
        #tab0
        #####################
        lf1 = ttk.LabelFrame(tab0, width=500, height=180, text = "Dane", )
        lf1.grid(column = 1, row = 0, padx=15 , pady=15)

        lf2 = ttk.LabelFrame(tab0, width=500, height=180, text= "Obróbka podstawowa")
        lf2.grid(column=1, row=2, padx=15, pady=15)

        lf3 = ttk.LabelFrame(tab0, width=500, height=180, text="Modyfikacje")
        lf3.grid(column=1, row=3, padx=15, pady=15)








        ####################
        self.label = ttk.Label(lf1)
        self.label.grid(row=5,column = 0)


        self.show_file = ttk.Button(lf1, text='Wskaż plik csv', command=self.show_open_file_clicked_tab_0)

        self.show_file.grid(row=10, column=0, padx=10)


        ######################

        self.label = ttk.Label(lf1)
        self.label.grid(row=15, column=0)

        self.distance_label = ttk.Label(lf1, text='nazwa kolumny - x')
        self.distance_label.grid(row=20, column=0)

        self.name_col_x_entry = ttk.Entry(lf1, textvariable=self.x_var, width=10)
        self.name_col_x_entry.grid(row=20, column=1, sticky=tk.NSEW)



        self.distance_label = ttk.Label(lf1, text='nazwa kolumny - y')
        self.distance_label.grid(row=20, column=2)

        self.name_col_y_entry = ttk.Entry(lf1, textvariable=self.y_var, width=10)
        self.name_col_y_entry.grid(row=20, column=3, sticky=tk.NSEW)

        self.distance_label = ttk.Label(lf1, text='nazwa serii')
        self.distance_label.grid(row=20, column=4)

        self.name_serial_entry = ttk.Entry(lf1, textvariable=self.name_serial_var, width=35)
        self.name_serial_entry.grid(row=20, column=5, sticky=tk.NSEW)





        #############################################################

        self.label = ttk.Label(lf1)
        self.label.grid(row=22, column=0)

        self.open_button = ttk.Button(lf1, text='Pobierz dane', command=self.open_button_clicked)
        self.open_button.grid(row=23, column=0, padx=10)



        ###########################################################

        self.label = ttk.Label(lf2 )
        self.label.grid(row=24, column=0)

        self.distance_label = ttk.Label(lf2, text='st. wielomianu lini trendu')
        self.distance_label.grid(row=26, column=0)

        self.name_col_x_entry = ttk.Entry(lf2, textvariable=self.polynominal_degree, width=10)
        self.name_col_x_entry.grid(row=26, column=1, sticky=tk.NSEW)

        ################################################################


        self.distance_label = ttk.Label(lf2, text='krok')
        self.distance_label.grid(row=26, column=2)

        self.name_col_x_entry = ttk.Entry(lf2, textvariable=self.step , width=10)
        self.name_col_x_entry.grid(row=26, column=3, sticky=tk.NSEW)




        self.label = ttk.Label(lf2)
        self.label.grid(row=27, column=0)

        self.total_scope_label = ttk.Label(lf2, text='dolny zakres:')
        self.total_scope_label.grid(row=28, column=0)

        self.total_scope_entry = ttk.Entry(lf2, textvariable=self.total_down_scope_var, width=30)
        self.total_scope_entry.grid(row=28, column=1, sticky=tk.NSEW)

        self.total_scope_label = ttk.Label(lf2, text='górny zakres:')
        self.total_scope_label.grid(row=28, column=2)
        self.total_scope_entry = ttk.Entry(lf2, textvariable=self.total_up_scope_var, width=30)
        self.total_scope_entry.grid(row=28, column=3, sticky=tk.NSEW)

        ############################################

        self.label = ttk.Label(lf2)
        self.label.grid(row=29, column=0)


        self.label = ttk.Label(lf2, text='wzór korekcyjny - x')
        self.label.grid(row=30, column=0)

        self.name_col_x_entry = ttk.Entry(lf2, textvariable = self.x_math_form , width=10)
        self.name_col_x_entry.grid(row=30, column=1, sticky=tk.NSEW)

        self.label = ttk.Label(lf2, text='wzór korekcyjny - y')
        self.label.grid(row=30, column=2)

        self.name_col_y_entry = ttk.Entry(lf2, textvariable = self.y_math_form , width=10)
        self.name_col_y_entry.grid(row=30, column=3, sticky=tk.NSEW)

        self.distance_label = ttk.Label(lf2)
        self.distance_label.grid(row=31, column=0)

        self.label = ttk.Label(lf3)
        self.label.grid(row=32, column=0)


        self.count_button_count = ttk.Button(lf2, text='Przelicz', command=self.count_button_clicked_tab_0)
        self.count_button_count.grid(row=35, column=0, padx=10)


        self.open_button_draw_natural = ttk.Button(lf2, text='Rysuj wykres naturalny',
                                                   command=self.draw_natural_chart_clicked_tab_0)

        self.open_button_draw_natural.grid(row=35, column=1, padx=10)



        self.open_button = ttk.Button(lf2, text='Zapisz', command=self.save_natural_button_clicked_tab_0)
        self.open_button.grid(row=35, column=2, padx=10)


        self.export_button_natural_data_tab_0 = ttk.Button(lf2, text='Dalej', command=self.export_nature_data_button_clicked_tab_0)
        self.export_button_natural_data_tab_0.grid(row=35, column=3, padx=10)


        #######################



        self.label = ttk.Label(lf3)
        self.label.grid(row=35, column=0)




        self.distance_label = ttk.Label(lf3, text='odleglość:')
        self.distance_label.grid(row=40, column=0)


        self.distance_entry = ttk.Entry(lf3, textvariable=self.dist_border_var, width=30)
        self.distance_entry.grid(row=40, column=1, sticky=tk.NSEW)




        ######################

        self.label = ttk.Label(lf3)
        self.label.grid(row=50, column=0)


        self.density_label = ttk.Label(lf3, text='gęstość:')
        self.density_label.grid(row = 60, column=0)


        self.density_entry = ttk.Entry(lf3, textvariable=self.density_var, width=30)
        self.density_entry.grid(row = 60, column=1, sticky=tk.NSEW)


        #######################
        #
        self.label = ttk.Label(lf3)
        self.label.grid(row=70, column=0)


        self.down_scope_label = ttk.Label(lf3, text='dolny zakres:')
        self.down_scope_label.grid(row = 80, column=0)


        self.down_scope_entry = ttk.Entry(lf3, textvariable=self.down_scope_var, width=30)
        self.down_scope_entry.grid(row = 80, column=1, sticky=tk.NSEW)

        #######################



        self.up_scope_label = ttk.Label(lf3, text='górny zakres:')
        self.up_scope_label.grid(row = 80, column=2)


        self.up_scope_entry = ttk.Entry(lf3, textvariable=self.up_scope_var, width=30)
        self.up_scope_entry.grid(row = 80, column=3, sticky=tk.NSEW)



        self.label = ttk.Label(lf3)
        self.label.grid(row=90, column=0)






        ##########################
        #
        self.label = ttk.Label(lf3)
        self.label.grid(row=110, column=0)


        self.count_button_count = ttk.Button(lf3, text='Przelicz', command=self.count_button_clicked_tab_0)
        self.count_button_count.grid(row=100, column=0, padx=10)

        #############################



        self.open_button_draw_modified = ttk.Button(lf3, text='Rysuj wykres obrobiony', command=self.draw_modyfied_chart_clicked_tab_0)
        self.open_button_draw_modified.grid(row=100, column=1, padx=10)



        ############################


        #
        self.open_button_save_data= ttk.Button(lf3, text='Zapisz', command=self.save_modify_button_clicked_tab_0)
        self.open_button_save_data.grid(row=100, column=2, padx=10)



        ##########################



        self.open_button = ttk.Button(lf3, text='Dalej', command=self.export_modyfied_button_clicked_tab_0)
        self.open_button.grid(row=100, column=3, padx=10)

        ######################################################################################################################################################
       #tab1
       ######################################################################################################################################################

        lf101 = ttk.LabelFrame(tab1, width=500, height=180, text="Dane" )
        lf101.grid(column=0, row=0, padx=15, pady=15)

        lf102 = ttk.LabelFrame(tab1, width=500, height=180, text="Zmiana zakresu")
        lf102.grid(column=0, row=1, padx=15, pady=15)


        #########################################

        self.open_button_data_tab_1 = ttk.Button(lf101, text='Wskaż plik csv', command=self.show_open_file_clicked_tab_1)
        self.open_button_data_tab_1.grid(row=1, column=0, padx=10)


        #######################################


        self.label = ttk.Label(lf101)
        self.label.grid(row=15, column=0)

        self.label = ttk.Label(lf101, text='nazwa kolumny - czas')
        self.label.grid(row=20, column=0)

        self.name_col_x_entry_tab_1 = ttk.Entry(lf101, textvariable=self.time_var_tab1, width=10)
        self.name_col_x_entry_tab_1.grid(row=20, column=1, sticky=tk.NSEW)



        self.label = ttk.Label(lf101, text='nazwa kolumny - x')
        self.label.grid(row=20, column=2)

        self.name_col_y1_entry_tab_1 = ttk.Entry(lf101, textvariable=self.y1_var_tab1, width=10)
        self.name_col_y1_entry_tab_1.grid(row=20, column=3, sticky=tk.NSEW)


        self.label = ttk.Label(lf101, text='nazwa kolumny - y')
        self.label.grid(row=20, column=4)

        self.name_col_y2_entry_tab_1 = ttk.Entry(lf101, textvariable=self.y2_var_tab1, width=10)
        self.name_col_y2_entry_tab_1.grid(row=20, column=5, sticky=tk.NSEW)


        #############################################################

        self.label = ttk.Label(lf101)
        self.label.grid(row=22, column=0)

        self.open_button_tab_1 = ttk.Button(lf101, text='Pobierz dane', command=self.get_data_button_clicked_tab_1)
        self.open_button_tab_1.grid(row=23, column=0, padx=10)

        #############################################################

        self.draw_natural_tab1 = ttk.Button(lf101, text='Rysuj wykres ', command=self.natural_chart_clicked_tab_1)

        self.draw_natural_tab1.grid(row=23, column=4, padx=10)


        #############################################################

        #
        self.label = ttk.Label(lf102)
        self.label.grid(row=1, column=0)


        self.down_scope_label = ttk.Label(lf102, text='dolny zakres:')
        self.down_scope_label.grid(row = 10, column=0)


        self.down_scope_entry_tab_1 = ttk.Entry(lf102, textvariable=self.down_scope_var_tab_1, width=30)
        self.down_scope_entry_tab_1.grid(row = 10, column=1, sticky=tk.NSEW)

        #######################



        self.up_scope_label = ttk.Label(lf102, text='górny zakres:')
        self.up_scope_label.grid(row = 10, column=2)


        self.up_scope_entry_tab_1 = ttk.Entry(lf102, textvariable=self.up_scope_var_tab_1, width=30)
        self.up_scope_entry_tab_1.grid(row = 10, column=3, sticky=tk.NSEW)



        self.label = ttk.Label(lf102)
        self.label.grid(row=15, column=0)

        #########################



        self.set_button_count_tab_1 = ttk.Button(lf102, text='Ustaw', command=self.set_button_clicked_tab_1)
        self.set_button_count_tab_1.grid(row=20, column=0, padx=10)

        self.draw_slice_button_count_tab_1 = ttk.Button(lf102, text='Rysuj wykres', command=self.draw_slice_button_clicked_tab_1)
        self.draw_slice_button_count_tab_1.grid(row=20, column=1, padx=10)



        self.save_button_tab_1 = ttk.Button(lf102, text='Zapisz', command=self.save_modyfied_data_clicked_tab_1)
        self.save_button_tab_1.grid(row=20, column=3, padx=10)

        self.draw_slice_button_count_tab_1 = ttk.Button(lf102, text='Dalej', command=self.export_clicked_tab_1)
        self.draw_slice_button_count_tab_1.grid(row=20, column=4, padx=10)


        ###############################################################################################################################


        # tab 2
        ###############################################################################################################################

        lf301 = ttk.LabelFrame(tab2, width=500, height=180, text="Pobierz")
        lf301.grid(column=0, row=0, padx=15, pady=15)

        lf302 = ttk.LabelFrame(tab2, width=500, height=180, text="Łącz")
        lf302.grid(column=0, row=1, padx=15, pady=15)

        lf303 = ttk.LabelFrame(tab2, width=500, height=180, text="Wynik")
        lf303.grid(column=0, row=2, padx=15, pady=15)

        ###############################################################################################################################
        self.label = ttk.Label(lf301)
        self.label.grid(row=0, column=0)

        self.open_button_chart_01_tab_2 = ttk.Button(lf301, text='Wykres 1', command=self.data_trans_chart_01_tab_2)
        self.open_button_chart_01_tab_2.grid(row=0, column=0, padx=10)


        self.open_button_chart_02_tab_2 = ttk.Button(lf301, text='Wykres 2', command=self.data_trans_chart_02_tab_2)
        self.open_button_chart_02_tab_2.grid(row=0, column=1, padx=10)

        self.open_button_chart_03_tab_2 = ttk.Button(lf301, text='Wykres 3', command=self.data_trans_chart_03_tab_2)
        self.open_button_chart_03_tab_2.grid(row=0, column=3, padx=10)

        self.open_button_chart_04_tab_2 = ttk.Button(lf301, text='Wykres 4', command=self.data_trans_chart_04_tab_2)
        self.open_button_chart_04_tab_2.grid(row=0, column=4, padx=10)

        self.open_button_chart_05_tab_2 = ttk.Button(lf301, text='Wykres 5', command=self.data_trans_chart_05_tab_2)
        self.open_button_chart_05_tab_2.grid(row=0, column=5, padx=10)

        self.open_button_chart_06_tab_2 = ttk.Button(lf301, text='Wykres 6', command=self.data_trans_chart_06_tab_2)
        self.open_button_chart_06_tab_2.grid(row=0, column=6, padx=10)


        #########################################################################################################################

        self.aggregation_button_tab_2 = ttk.Button(lf302, text='Agreguj', command=self.aggregation_united_data_clicked_tab_2)
        self.aggregation_button_tab_2.grid(row=0, column=0, padx=10)

        #########################################################################################################################



        self.united_chart_button_tab_2 = ttk.Button(lf303, text='Wykres zespolony', command=self.draw_united_data_clicked_tab_2)
        self.united_chart_button_tab_2.grid(row=2, column=0, padx=10)

        self.label = ttk.Label(lf303)
        self.label.grid(row=3, column=0)


        self.open_button_tab_2 = ttk.Button(lf303, text='Zapisz', command=self.data_save_clicked_tab_2)
        self.open_button_tab_2.grid(row=4, column=0, padx=10)



        #######################################################################################################################################
        # units - tab3

        #######################################################################################################################################

        lf301 = ttk.LabelFrame(tab3, width=500, height=180, text="Nazwa wykresu")
        lf301.grid(column=0, row=0)

        lf302 = ttk.LabelFrame(tab3, width=500, height=180, text="Nazwy i jednostki - oś X")
        lf302.grid(column=0, row=1, padx=15, pady=15)

        lf303 = ttk.LabelFrame(tab3, width=500, height=180, text="Nazwy i jednostki - oś Y")
        lf303.grid(column=0, row=2, padx=15, pady=15)


        ####################################################################################################################

        self.label = ttk.Label(lf301)
        self.label.grid(row=1, column=0)



        self.name_of_chart = ttk.Entry(lf301, textvariable=self.name_of_chart_var, width=10)
        self.name_of_chart.grid(row=1, column=1, sticky=tk.NSEW, ipadx=200)

        #####################################################################################################################
        self.distance_label = ttk.Label(lf302).grid(row=0, column=0)

        self.label = ttk.Label(lf302, text='nazwa osi X')
        self.label.grid(row=10, column=1)


        self.name_of_X_axis = ttk.Entry(lf302, textvariable=self.name_of_X_axis_var, width=10)
        self.name_of_X_axis.grid(row=10, column=2,ipadx=90)

        ##################

        self.distance_label = ttk.Label(lf302).grid(row=20, column=0)

        self.label = ttk.Label(lf302, text='jednostka')
        self.label.grid(row=30, column=1)

        self.unit_of_X_axis = ttk.Entry(lf302, textvariable=self.unit_of_X_axis_var, width=10)
        self.unit_of_X_axis.grid(row=30, column=2, sticky=tk.W)
        ####################


        self.distance_label = ttk.Label(lf302).grid(row=40, column=0)

        self.label = ttk.Label(lf302, text='zakres - min')
        self.label.grid(row=50, column=1)
        self.scope_min_of_X_axis = ttk.Entry(lf302, textvariable=self.scope_min_of_X_axis_var, width=10)
        self.scope_min_of_X_axis.grid(row=50, column=2, sticky=tk.W)

        ###################

        self.distance_label = ttk.Label(lf302).grid(row=60, column=0)

        self.label = ttk.Label(lf302, text='zakres - max')
        self.label.grid(row=70, column=1)

        self.scope_max_of_X_axis = ttk.Entry(lf302, textvariable=self.scope_max_of_X_axis_var, width=10)
        self.scope_max_of_X_axis.grid(row=70, column=2, sticky=tk.W)

        ##########################################################################################################################################
        self.distance_label = ttk.Label(lf303).grid(row=0, column=0)

        self.label = ttk.Label(lf303, text='nazwa osi Y')
        self.label.grid(row=10, column=1)

        self.name_of_Y_axis = ttk.Entry(lf303, textvariable=self.name_of_Y_axis_var, width=10)
        self.name_of_Y_axis.grid(row=10, column=2, ipadx=90)

        ##################

        self.distance_label = ttk.Label(lf303).grid(row=20, column=0)

        self.label = ttk.Label(lf303, text='jednostka')
        self.label.grid(row=30, column=1)

        self.unit_of_Y_axis = ttk.Entry(lf303, textvariable=self.unit_of_Y_axis_var, width=10)
        self.unit_of_Y_axis.grid(row=30, column=2, sticky=tk.W)
        ####################

        self.distance_label = ttk.Label(lf303).grid(row=40, column=0)

        self.label = ttk.Label(lf303, text='zakres - min')
        self.label.grid(row=50, column=1)
        self.scope_min_of_Y_axis = ttk.Entry(lf303, textvariable=self.scope_min_of_Y_axis_var, width=10)
        self.scope_min_of_Y_axis.grid(row=50, column=2, sticky=tk.W)

        ###################

        self.distance_label = ttk.Label(lf303).grid(row=60, column=0)

        self.label = ttk.Label(lf303, text='zakres - max')
        self.label.grid(row=70, column=1)

        self.scope_max_of_Y_axis = ttk.Entry(lf303, textvariable=self.scope_max_of_Y_axis_var, width=10)
        self.scope_max_of_Y_axis.grid(row=70, column=2, sticky=tk.W)



    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller


    def show_open_file_clicked_tab_0(self):

        file1 = askopenfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='r', filetypes=[('CSV Files', '*.csv')])

        self.open_name_var.set(str(file1.name))


    def show_save_file_clicked(self):


        file2 = asksaveasfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='w',defaultextension = '*.csv', filetypes=[('CSV Files', '*.csv')])

        if file2 is not None:
            self.save_name_var.set(str(file2.name))



    def open_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.open_data()









#########################################################################################################################




    def count_button_clicked_tab_0(self):

        self.controller.counter()

    def draw_natural_chart_clicked_tab_0(self):
        self.controller.natural_chart_execution_tab_0()


    def save_natural_button_clicked_tab_0(self):
        self.controller.save_nature_data_tab_0()



    def export_nature_data_button_clicked_tab_0(self):
        self.controller.export_nature_data_tab_0()
        self.switch_modyfied_export = False



######

    def draw_modyfied_chart_clicked_tab_0(self):
        self.controller.modyfied_chart_execution_tab_0()



    def save_modify_button_clicked_tab_0(self):
        self.controller.save_modify_data_tab_0()


    def export_modyfied_button_clicked_tab_0(self):
        self.switch_modyfied_export = True
        self.controller.export_modyfied_data_tab_0()



#####################################################################################################################




    def show_open_file_clicked_tab_1(self):

        file11 = askopenfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='r',
                            filetypes=[('CSV Files', '*.csv')])

        self.open_name_var.set(str(file11.name))


    def get_data_button_clicked_tab_1(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.open_data_tab_1()



    def natural_chart_clicked_tab_1(self):
        #self.controller.natural_chart_execution()
        self.controller.draw_data_tab_1()

    def set_button_clicked_tab_1(self):
        if self.controller:
            #self.controller.open_data()
            self.controller.set_data_tab_1()

    def draw_slice_button_clicked_tab_1(self):
        self.controller.draw_slice_data_tab_1()

    def export_clicked_tab_1(self):
        self.controller.export_to_tab_0()

    def save_modyfied_data_clicked_tab_1(self):
        self.controller.save_modyfied_data_clicked_tab_1()


###################################################################################################################################
    def data_trans_chart_01_tab_2(self):
       self.controller.trans_01_tab_2()
       self.open_button_chart_01_tab_2.config(state=DISABLED)
    def data_trans_chart_02_tab_2(self):
       self.controller.trans_02_tab_2()
       self.open_button_chart_02_tab_2.config(state=DISABLED)
    def data_trans_chart_03_tab_2(self):
       self.controller.trans_03_tab_2()
       self.open_button_chart_03_tab_2.config(state=DISABLED)
    def data_trans_chart_04_tab_2(self):
       self.controller.trans_04_tab_2()
       self.open_button_chart_04_tab_2.config(state=DISABLED)
    def data_trans_chart_05_tab_2(self):
        self.controller.trans_05_tab_2()
        self.open_button_chart_05_tab_2.config(state=DISABLED)
    def data_trans_chart_06_tab_2(self):
        self.controller.trans_06_tab_2()
        self.open_button_chart_06_tab_2.config(state=DISABLED)

    ####################################################################################################################################

    def aggregation_united_data_clicked_tab_2(self):
        self.controller.agg_tab_2()
    def draw_united_data_clicked_tab_2(self):
        self.controller.united_chart_execution_tab_2()

    def data_save_clicked_tab_2(self):
        self.controller.save_data_clicked_tab_2()


    #######################################################################################################################################




    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)


    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.name_entry['foreground'] = 'black'
        self.open_name_var.set('')



    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''

###################################################################################################################




#######################################################################################################################
#######################################################################################################################




########################################################################################################################