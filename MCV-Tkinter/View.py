import re
import tkinter as tk
from tkinter import ttk

import error_list
import source
from Controller import Controller
from Model import Model
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from data_source import *
from tkinter import messagebox
import datetime
from error_list import *
import time


window = tk.Tk()
window.title("Chart plotter")
window.geometry('790x850')

tab_parent = ttk.Notebook(window)
tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)

get_data = GetData()

errors = Errors()

class View(ttk.Frame):


    def __init__(self, parent):
        super().__init__(parent)

        self.open_name_var = StringVar()
        self.open_name_cfg_var = StringVar()
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
        self.switch_background = False
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

        self.scale_time_chart = tk.StringVar()

        self.is_on_canal_01 = True
        self.is_on_canal_02 = True
        self.is_on_canal_03 = True
        self.is_on_canal_04 = True
        self.is_on_canal_05 = True
        self.is_on_canal_06 = True

        self.total_down_scope_background_var = tk.StringVar()
        self.total_up_scope_background_var = tk.StringVar()

        self.scope_up_back_entry_x_var = tk.StringVar()
        self.scope_down_back_entry_x_var = tk.StringVar()

        self.scope_up_back_entry_y_var = tk.StringVar()
        self.scope_down_back_entry_y_var = tk.StringVar()

        self.name_picture = tk.StringVar()
        self.trans_picture = tk.StringVar()

        self.save_name_cfg_var = tk.StringVar()

        self.delay_time = 500


#########################################################################################################################
# validation
#########################################################################################################################



        def validate_number(input):

            if input.isdigit():
                print(input)
                return True

            elif input is "":
                print(input)
                return True

            else:
                print(input)

                return False

        def on_invalid_number():

            messagebox.showerror('ERROR', 'Wpisano literę')

        self.vcmd_number = (window.register(validate_number), '%P')
        self.ivcmd_number = (window.register(on_invalid_number),)

#####################################################################################################################

        def validate_time(value):

            if value =='':
                return True

            else:
                try:
                    datetime.datetime.strptime(value, '%H:%M:%S')
                    print('sukces')
                    return True
                except:
                    return False


        def on_invalid_time():

            messagebox.showerror('ERROR', 'Wpisano niewłaściwy format')

        self.vcmd_time = (window.register(validate_time), '%P')
        self.ivcmd_time = (window.register(on_invalid_time),)



####################################################################################################################
#errors
####################################################################################################################



#####################################################################################################################



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

        lf4 = ttk.LabelFrame(tab0, width=600, height=100, text="Wstaw tło")
        lf4.grid(column=1, row=4, padx=15, pady=15)

        lf5 = ttk.LabelFrame(tab0, text="Zapis")
        lf5.grid(column=2, row=3)




        ####################
        self.label = ttk.Label(lf1)
        self.label.grid(row=5,column = 0)

        self.show_file_tab0 = ttk.Button(lf1, text='Wskaż plik csv', command=self.show_open_file_clicked_tab_0)
        self.show_file_tab0.grid(row=10, column=0, padx=10)


        ######################

        self.label = ttk.Label(lf1)
        self.label.grid(row=15, column=0)

        self.distance_label = ttk.Label(lf1, text='nazwa kolumny - x')
        self.distance_label.grid(row=20, column=0)
        self.name_col_x_entry = ttk.Entry(lf1, textvariable=self.x_var, width=10)
        self.name_col_x_entry.insert(0, get_data.name_col_x_tab0.get())
        self.name_col_x_entry.grid(row=20, column=1, sticky=tk.NSEW)



        self.distance_label = ttk.Label(lf1, text='nazwa kolumny - y')
        self.distance_label.grid(row=20, column=2)
        self.name_col_y_entry = ttk.Entry(lf1, textvariable=self.y_var, width=10)
        self.name_col_y_entry.insert(0, get_data.name_col_y_tab_0.get())
        self.name_col_y_entry.grid(row=20, column=3, sticky=tk.NSEW)
        self.distance_label = ttk.Label(lf1, text='nazwa serii')
        self.distance_label.grid(row=20, column=4)

        self.name_serial_entry = ttk.Entry(lf1, textvariable=self.name_serial_var, width=35)
        self.name_serial_entry.insert(0, get_data.name_serial_var.get())
        self.name_serial_entry.grid(row=20, column=5, sticky=tk.NSEW)



        #############################################################

        self.label = ttk.Label(lf1)
        self.label.grid(row=22, column=0)

        self.open_button_tab0 = ttk.Button(lf1, text='Pobierz dane', command=self.open_button_clicked)
        self.open_button_tab0.grid(row=23, column=0, padx=10)



        ###########################################################


        self.label = ttk.Label(lf2 )
        self.label.grid(row=24, column=0)

        self.distance_label = ttk.Label(lf2, text='st. wielomianu lini trendu')
        self.distance_label.grid(row=26, column=0)
        self.polynom_degree_entry = ttk.Entry(lf2, textvariable=self.polynominal_degree, width=10)
        self.polynom_degree_entry.insert(0, get_data.polynom_degree.get())
        self.polynom_degree_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.polynom_degree_entry.grid(row=26, column=1, sticky=tk.NSEW)
        ################################################################


        self.distance_label = ttk.Label(lf2, text='krok')
        self.distance_label.grid(row=26, column=2)
        self.step_value_entry = ttk.Entry(lf2, textvariable=self.step , width=10)
        self.step_value_entry.insert(0, get_data.step_value.get())
        self.step_value_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.step_value_entry.grid(row=26, column=3, sticky=tk.NSEW)




        self.label = ttk.Label(lf2)
        self.label.grid(row=27, column=0)

        self.label = ttk.Label(lf2, text='dolny zakres:')
        self.label.grid(row=28, column=0)

        self.scope_down_entry = ttk.Entry(lf2, textvariable=self.total_down_scope_var, width=30)
        self.scope_down_entry.insert(0, get_data.scope_down_entry_tab0.get())
        self.scope_down_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.scope_down_entry.grid(row=28, column=1, sticky=tk.NSEW)

        self.total_scope_label = ttk.Label(lf2, text='górny zakres:')
        self.total_scope_label.grid(row=28, column=2)
        self.scope_up_entry = ttk.Entry(lf2, textvariable=self.total_up_scope_var, width=30)
        self.scope_up_entry.insert(0, get_data.scope_up_entry_tab0.get())
        self.scope_up_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.scope_up_entry.grid(row=28, column=3, sticky=tk.NSEW)

        ############################################

        self.label = ttk.Label(lf2)
        self.label.grid(row=29, column=0)


        self.label = ttk.Label(lf2, text='wzór korekcyjny - x')
        self.label.grid(row=30, column=0)

        self.formula_x_entry = ttk.Entry(lf2, textvariable = self.x_math_form , width=10)
        self.formula_x_entry.insert(0,get_data.formula_x.get())
        self.formula_x_entry .grid(row=30, column=1, sticky=tk.NSEW)

        self.label = ttk.Label(lf2, text='wzór korekcyjny - y')
        self.label.grid(row=30, column=2)

        self.formula_y_entry = ttk.Entry(lf2, textvariable = self.y_math_form , width=10)
        self.formula_y_entry.insert(0, get_data.formula_y.get())
        self.formula_y_entry.grid(row=30, column=3, sticky=tk.NSEW)

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
        self.distance_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.distance_entry.grid(row=40, column=1, sticky=tk.NSEW)




        ######################

        self.label = ttk.Label(lf3)
        self.label.grid(row=50, column=0)


        self.density_label = ttk.Label(lf3, text='gęstość:')
        self.density_label.grid(row = 60, column=0)


        self.density_entry = ttk.Entry(lf3, textvariable=self.density_var, width=30)
        self.density_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.density_entry.grid(row = 60, column=1, sticky=tk.NSEW)


        #######################
        #
        self.label = ttk.Label(lf3)
        self.label.grid(row=70, column=0)


        self.down_scope_label = ttk.Label(lf3, text='dolny zakres:')
        self.down_scope_label.grid(row = 80, column=0)
        self.down_scope_entry = ttk.Entry(lf3, textvariable=self.down_scope_var, width=30)
        self.down_scope_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.down_scope_entry.grid(row = 80, column=1, sticky=tk.NSEW)

        #######################



        self.up_scope_label = ttk.Label(lf3, text='górny zakres:')
        self.up_scope_label.grid(row = 80, column=2)
        self.up_scope_entry = ttk.Entry(lf3, textvariable=self.up_scope_var, width=30)
        self.up_scope_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.up_scope_entry.grid(row = 80, column=3, sticky=tk.NSEW)



        self.label = ttk.Label(lf3)
        self.label.grid(row=90, column=0)






        ##########################
        #
        self.label = ttk.Label(lf3)
        self.label.grid(row=110, column=0)


        self.count_button_count_basic_tab0 = ttk.Button(lf3, text='Przelicz', command=self.count_button_clicked_tab_0)
        self.count_button_count_basic_tab0.grid(row=100, column=0, padx=10)

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


        ############################

        self.distance_label = ttk.Label(lf4)
        self.distance_label.grid(row=0, column=0)

        self.label_down_background_x_entry = ttk.Label(lf4, text='dolny zakres x:')
        self.label_down_background_x_entry.grid(row=10, column=0)
        self.scope_down_background_x_entry = ttk.Entry(lf4, textvariable = self.scope_down_back_entry_x_var, width=30)
        self.scope_down_background_x_entry.insert(0, get_data.scope_down_x_background_entry_tab0.get())
        self.scope_down_background_x_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.scope_down_background_x_entry.grid(row=10, column=3, sticky=tk.NSEW)



        self.label_up_background_x_entry = ttk.Label(lf4, text='górny zakres x:')
        self.label_up_background_x_entry.grid(row=10, column=4)

        self.scope_up_background_x_entry = ttk.Entry(lf4, textvariable = self.scope_up_back_entry_x_var, width=30)
        self.scope_up_background_x_entry.insert(0, get_data.scope_up_x_background_entry_tab0.get())
        self.scope_up_background_x_entry.config(validate="key", validatecommand=self.vcmd_number, invalidcommand=self.ivcmd_number)
        self.scope_up_background_x_entry.grid(row=10, column=5, sticky=tk.NSEW)

        self.distance_label = ttk.Label(lf4)
        self.distance_label.grid(row=15, column=0)

        self.scope_down_background_y_label = ttk.Label(lf4, text='dolny zakres y:')
        self.scope_down_background_y_label.grid(row=20, column=0)
        self.scope_down_background_y_entry = ttk.Entry(lf4, textvariable=self.scope_down_back_entry_y_var, width=30)
        self.scope_down_background_y_entry.insert(0, get_data.scope_down_y_background_entry_tab0.get())
        self.scope_down_background_y_entry.config(validate="key", validatecommand=self.vcmd_number,invalidcommand=self.ivcmd_number)
        self.scope_down_background_y_entry.grid(row=20, column=3, sticky=tk.NSEW)

        self.scope_up_background_y_label = ttk.Label(lf4, text='górny zakres y:')
        self.scope_up_background_y_label.grid(row=20, column=4)

        self.scope_up_background_y_entry = ttk.Entry(lf4, textvariable=self.scope_up_back_entry_y_var, width=30)
        self.scope_up_background_y_entry.insert(0, get_data.scope_up_y_background_entry_tab0.get())
        self.scope_up_background_y_entry.config(validate="key", validatecommand=self.vcmd_number,invalidcommand=self.ivcmd_number)
        self.scope_up_background_y_entry.grid(row=20, column=5, sticky=tk.NSEW)

        self.distance_label = ttk.Label(lf4)
        self.distance_label.grid(row=25, column=0)

        self.choice_button_foto_background = ttk.Button(lf4, text='Wybierz tło', command=self.show_open_picture_clicked_tab_0)
        self.choice_button_foto_background.grid(row=30, column=2, padx=10)

        self.label_trans_picture = ttk.Label(lf4, text='przezroczystość - ')
        self.label_trans_picture.grid(row=30, column=3, sticky=tk.E)

        self.trans_picture_entry = ttk.Entry(lf4, textvariable=self.trans_picture, width=5)
        self.trans_picture_entry.insert(0, get_data.trasparency_picture.get())
        self.trans_picture_entry.grid(row=30, column=4, sticky=tk.W)



        self.draw_chart_button_background = ttk.Button(lf4, text='wykres bez tła', command=self.draw_btn_foto_back_clicked_tab_0)
        self.draw_chart_button_background.grid(row=30, column=5, padx=10)

        self.button_save_config = ttk.Button(lf5, text='cfg', command=self.show_save_file_cfg_clicked_tab_0,width=6)
        self.button_save_config.grid(row=0, column=0,ipady=90 )





        ######################################################################################################################################################
       #tab1
       ######################################################################################################################################################

        lf101 = ttk.LabelFrame(tab1, width=500, height=180, text="Dane" )
        lf101.grid(column=0, row=1, padx=15, pady=15,sticky=W)

        lf102 = ttk.LabelFrame(tab1, width=500, height=180, text="Zmiana zakresu")
        lf102.grid(column=0, row=3, padx=15, pady=15,sticky=W)

        lf103 = ttk.LabelFrame(tab1, width=100, height=50, text="Podziałka czasu")
        lf103.grid(column=0, row=2, padx=15, pady=15, sticky=W)

        lf104 = ttk.LabelFrame(tab1, width=100, height=50, text="Wczytaj ")
        lf104.grid(column=0, row=0, padx=15, pady=15, sticky=W)


        ########################################

        self.open_button_cfg_data_tab_1 = ttk.Button(lf104, text='*.cfg',command=self.show_open_file_cfg_clicked_tab_0)
        self.open_button_cfg_data_tab_1.grid(row=1, column=0, padx=10)





        #########################################

        self.open_button_data_tab_1 = ttk.Button(lf101, text='Wskaż plik csv', command=self.show_open_file_clicked_tab_1)
        self.open_button_data_tab_1.grid(row=1, column=0, padx=10)


        #######################################





        self.label = ttk.Label(lf101)
        self.label.grid(row=15, column=0)

        self.label = ttk.Label(lf101, text='nazwa kolumny - czas')
        self.label.grid(row=20, column=0)

        self.time_tag_entry = ttk.Entry(lf101, textvariable=self.time_var_tab1, width=10)
        self.time_tag_entry.insert(0, get_data.time_tag.get())
        self.time_tag_entry.grid(row=20, column=1, sticky=tk.NSEW)



        self.label = ttk.Label(lf101, text='nazwa kolumny - x')
        self.label.grid(row=20, column=2)
        self.column_x_tag_tab1_entry = ttk.Entry(lf101, textvariable=self.y1_var_tab1, width=10)
        self.column_x_tag_tab1_entry.insert(0, get_data.column_x_tag_tab1.get())
        self.column_x_tag_tab1_entry .grid(row=20, column=3, sticky=tk.NSEW)


        self.label = ttk.Label(lf101, text='nazwa kolumny - y')
        self.label.grid(row=20, column=4)

        self.column_y_tag_tab1_entry= ttk.Entry(lf101, textvariable=self.y2_var_tab1, width=10)
        self.column_y_tag_tab1_entry.insert(0, get_data.column_y_tag_tab1.get())
        self.column_y_tag_tab1_entry.grid(row=20, column=5, sticky=tk.NSEW)



        #############################################################

        self.label = ttk.Label(lf101)
        self.label.grid(row=22, column=0)

        self.open_button_tab_1 = ttk.Button(lf101, text='Pobierz dane', command=self.get_data_button_clicked_tab_1)
        self.open_button_tab_1.grid(row=23, column=0, padx=10)

        #############################################################

        self.draw_natural_tab1 = ttk.Button(lf101, text='Rysuj wykres ', command=self.natural_chart_clicked_tab_1)

        self.draw_natural_tab1.grid(row=23, column=4, padx=10)


        #############################################################





        #############################################################
        #
        self.label = ttk.Label(lf102)
        self.label.grid(row=1, column=0)


        self.down_scope_label = ttk.Label(lf102, text='zakres dolny:[hh:mm:ss]')

        self.down_scope_label.grid(row = 10, column=0)


        self.down_scope_entry_tab_1 = ttk.Entry(lf102, textvariable=self.down_scope_var_tab_1, width=30)
        self.down_scope_entry_tab_1.insert(0, get_data.down_scope_tab1.get())
        self.down_scope_entry_tab_1.config(validate="focusout", validatecommand=self.vcmd_time, invalidcommand=self.ivcmd_time)
        self.down_scope_entry_tab_1.grid(row = 10, column=1, sticky=tk.NSEW)

        #######################



        self.up_scope_label = ttk.Label(lf102, text='zakres górny:[hh:ss:mm]')

        self.up_scope_label.grid(row = 10, column=2)


        self.up_scope_entry_tab_1 = ttk.Entry(lf102, textvariable=self.up_scope_var_tab_1, width=30)
        self.up_scope_entry_tab_1.insert(0, get_data.up_scope_tab_1.get())
        self.up_scope_entry_tab_1.config(validate="focusout", validatecommand=self.vcmd_time, invalidcommand=self.ivcmd_time)
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

        self.export_button_count_tab_1 = ttk.Button(lf102, text='Dalej', command=self.export_clicked_tab_1)
        self.export_button_count_tab_1.grid(row=20, column=4, padx=10)

        self.scale_time_chart_entry_tab_1 = ttk.Entry(lf103, textvariable=self.scale_time_chart, width=15)
        self.scale_time_chart_entry_tab_1.config(validate="key", validatecommand=self.vcmd_number,invalidcommand=self.ivcmd_number)
        self.scale_time_chart_entry_tab_1.insert(0,get_data.scale_time_chart.get())

        self.scale_time_chart_entry_tab_1.grid(row=1, column=1, sticky=tk.NSEW)




        ###############################################################################################################################



        ###############################################################################################################################
        # tab 2
        ###############################################################################################################################

        lf301 = ttk.LabelFrame(tab2, width=500, height=180, text="Seria")
        lf301.grid(column=0, row=0, padx=15, pady=15)

        # lf302 = ttk.LabelFrame(tab2, width=50, height=18, text="Wygaś")
        # lf302.grid(column=0, row=1, padx=15, pady=15)

        lf303 = ttk.LabelFrame(tab2, width=500, height=180, text="Wynik")
        lf303.grid(column=0, row=2, padx=15, pady=15)

        ###############################################################################################################################
        self.label = ttk.Label(lf301)
        self.label.grid(row=0, column=0)

        self.open_button_chart_01_tab_2 = ttk.Button(lf301, text='01 Otwarta', command=self.canal_01)
        self.open_button_chart_01_tab_2.grid(row=0, column=0, padx=10)


        self.open_button_chart_02_tab_2 = ttk.Button(lf301, text='02 Otwarta', command=self.canal_02)
        self.open_button_chart_02_tab_2.grid(row=0, column=1, padx=10)

        self.open_button_chart_03_tab_2 = ttk.Button(lf301, text='03 Otwarta', command=self.canal_03)
        self.open_button_chart_03_tab_2.grid(row=0, column=3, padx=10)

        self.open_button_chart_04_tab_2 = ttk.Button(lf301, text='04 Otwarta', command=self.canal_04)
        self.open_button_chart_04_tab_2.grid(row=0, column=4, padx=10)

        self.open_button_chart_05_tab_2 = ttk.Button(lf301, text='05 Otwarta', command=self.canal_05)
        self.open_button_chart_05_tab_2.grid(row=0, column=5, padx=10)

        self.open_button_chart_06_tab_2 = ttk.Button(lf301, text='06 Otwarta', command=self.canal_06)
        self.open_button_chart_06_tab_2.grid(row=0, column=6, padx=10)


        #########################################################################################################################




        #########################################################################################################################



        self.united_chart_button_tab_2 = ttk.Button(lf303, text='Wykres zespolony', command=self.draw_united_data_clicked_tab_2)
        self.united_chart_button_tab_2.grid(row=2, column=0, padx=10)

        self.label = ttk.Label(lf303)
        self.label.grid(row=3, column=0)


        self.save_data_button_tab_2 = ttk.Button(lf303, text='Zapisz dane', command=self.data_save_clicked_tab_2)
        self.save_data_button_tab_2.grid(row=4, column=0, padx=10)

        self.label = ttk.Label(lf303)
        self.label.grid(row=5, column=0)

        self.save_trend_button_tab_2 = ttk.Button(lf303, text='Zapisz trend', command=self.trend_save_clicked_tab_2)
        self.save_trend_button_tab_2.grid(row=6, column=0, padx=10)

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
        self.name_of_chart_entry_tab3 = ttk.Entry(lf301, textvariable=self.name_of_chart_var, width=10)
        self.name_of_chart_entry_tab3.insert(0,get_data.name_of_chart.get())
        self.name_of_chart_entry_tab3.grid(row=1, column=1, sticky=tk.NSEW, ipadx=200)
        #####################################################################################################################

        self.distance_label = ttk.Label(lf302)
        self.distance_label.grid(row=0, column=0)
        self.label = ttk.Label(lf302, text='nazwa osi X')
        self.label.grid(row=10, column=1)


        self.name_of_X_axis_entry = ttk.Entry(lf302, textvariable=self.name_of_X_axis_var, width=10)
        self.name_of_X_axis_entry.insert(0, get_data.name_of_X_axis_tab3.get())
        self.name_of_X_axis_entry.grid(row=10, column=2,ipadx=90)

        ##################

        self.distance_label = ttk.Label(lf302).grid(row=20, column=0)

        self.label = ttk.Label(lf302, text='jednostka')
        self.label.grid(row=30, column=1)

        self.unit_of_X_axis_entry = ttk.Entry(lf302, textvariable=self.unit_of_X_axis_var, width=10)
        self.unit_of_X_axis_entry.insert(0, get_data.unit_of_X_axis_tab3.get())
        self.unit_of_X_axis_entry.grid(row=30, column=2, sticky=tk.W)
        ####################

        self.distance_label = ttk.Label(lf302)
        self.distance_label.grid(row=40, column=0)
        self.label = ttk.Label(lf302, text='zakres - min')
        self.label.grid(row=50, column=1)
        self.scope_min_of_X_axis = ttk.Entry(lf302, textvariable=self.scope_min_of_X_axis_var, width=10)
        self.scope_min_of_X_axis.config(state= "disabled")
        self.scope_min_of_X_axis.grid(row=50, column=2, sticky=tk.W)

        ###################

        self.distance_label = ttk.Label(lf302).grid(row=60, column=0)

        self.label = ttk.Label(lf302, text='zakres - max')
        self.label.grid(row=70, column=1)

        self.scope_max_of_X_axis = ttk.Entry(lf302, textvariable=self.scope_max_of_X_axis_var, width=10)
        self.scope_max_of_X_axis.config(state="disabled")
        self.scope_max_of_X_axis.grid(row=70, column=2, sticky=tk.W)

        ##########################################################################################################################################
        self.distance_label = ttk.Label(lf303)
        self.distance_label.grid(row=0, column=0)
        self.label = ttk.Label(lf303, text='nazwa osi Y')
        self.label.grid(row=10, column=1)

        self.name_of_Y_axis_entry_tab3 = ttk.Entry(lf303, textvariable=self.name_of_Y_axis_var, width=10)
        self.name_of_Y_axis_entry_tab3.insert(0, get_data.name_of_Y_axis_tab3.get())
        self.name_of_Y_axis_entry_tab3.grid(row=10, column=2, ipadx=90)

        ##################

        self.distance_label = ttk.Label(lf303).grid(row=20, column=0)

        self.label = ttk.Label(lf303, text='jednostka')
        self.label.grid(row=30, column=1)

        self.unit_of_Y_axis_entry_tab3 = ttk.Entry(lf303, textvariable=self.unit_of_Y_axis_var, width=10)
        self.unit_of_Y_axis_entry_tab3.insert(0,get_data.unit_of_Y_axis_tab3.get())
        self.unit_of_Y_axis_entry_tab3.grid(row=30, column=2, sticky=tk.W)
        ####################

        self.distance_label = ttk.Label(lf303).grid(row=40, column=0)

        self.label = ttk.Label(lf303, text='zakres - min')
        self.label.grid(row=50, column=1)
        self.scope_min_of_Y_axis = ttk.Entry(lf303, textvariable=self.scope_min_of_Y_axis_var, width=10)
        self.scope_min_of_Y_axis.config(state = 'disabled')
        self.scope_min_of_Y_axis.grid(row=50, column=2, sticky=tk.W)

        ###################

        self.distance_label = ttk.Label(lf303).grid(row=60, column=0)

        self.label = ttk.Label(lf303, text='zakres - max')
        self.label.grid(row=70, column=1)

        self.scope_max_of_Y_axis = ttk.Entry(lf303, textvariable=self.scope_max_of_Y_axis_var, width=10)
        self.scope_max_of_Y_axis.config(state='disabled')
        self.scope_max_of_Y_axis.grid(row=70, column=2, sticky=tk.W)



    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def show_open_file_cfg_clicked_tab_0(self):
        try:
            get_data.dicto_paresr()
            self.open_button_cfg_data_tab_1.config(text='ok')
            self.open_button_cfg_data_tab_1.after(self.delay_time, lambda: self.open_button_cfg_data_tab_1.config(text='Pobierz dane' ))
        except:
            errors.err_lack_of_file_or_bad_data()

        self.name_col_x_entry.delete(0, END)
        self.name_col_y_entry.delete(0, END)
        self.name_serial_entry.delete(0, END)
        self.polynom_degree_entry.delete(0,END)
        self.step_value_entry.delete(0, END)
        self.scope_down_entry.delete(0, END)
        self.scope_up_entry.delete(0, END)
        self.formula_x_entry.delete(0, END)
        self.formula_y_entry.delete(0, END)
        self.scope_down_background_x_entry.delete(0, END)
        self.scope_up_background_x_entry.delete(0, END)
        self.scope_down_background_y_entry.delete(0, END)
        self.scope_up_background_y_entry.delete(0, END)
        self.trans_picture_entry.delete(0, END)
        self.time_tag_entry.delete(0, END)
        self.column_x_tag_tab1_entry.delete(0, END)
        self.column_y_tag_tab1_entry.delete(0, END)
        self.down_scope_entry_tab_1.delete(0, END)
        self.up_scope_entry_tab_1.delete(0, END)
        self.scale_time_chart_entry_tab_1.delete(0, END)
        self.name_of_chart_entry_tab3.delete(0, END)
        self.name_of_X_axis_entry.delete(0, END)
        self.unit_of_X_axis_entry.delete(0, END)
        self.name_of_Y_axis_entry_tab3.delete(0, END)
        self.unit_of_Y_axis_entry_tab3.delete(0, END)


        self.name_col_x_entry.insert(0, get_data.name_col_x_tab0.get())
        self.name_col_y_entry.insert(0, get_data.name_col_y_tab_0.get())
        self.name_serial_entry.insert(0, get_data.name_serial_var.get())
        self.polynom_degree_entry.insert(0, get_data.polynom_degree.get())
        self.step_value_entry.insert(0, get_data.step_value.get())
        self.scope_down_entry.insert(0, get_data.scope_down_entry_tab0.get())
        self.scope_up_entry.insert(0, get_data.scope_up_entry_tab0.get())
        self.formula_x_entry.insert(0, get_data.formula_x.get())
        self.formula_y_entry.insert(0, get_data.formula_y.get())
        self.scope_down_background_x_entry.insert(0, get_data.scope_down_x_background_entry_tab0.get())
        self.scope_up_background_x_entry.insert(0, get_data.scope_up_x_background_entry_tab0.get())
        self.scope_down_background_y_entry.insert(0, get_data.scope_down_y_background_entry_tab0.get())
        self.scope_up_background_y_entry.insert(0, get_data.scope_up_y_background_entry_tab0.get())
        self.trans_picture_entry.insert(0, get_data.trasparency_picture.get())
        self.time_tag_entry.insert(0, get_data.time_tag.get())
        self.column_x_tag_tab1_entry.insert(0, get_data.column_x_tag_tab1.get())
        self.column_y_tag_tab1_entry.insert(0, get_data.column_y_tag_tab1.get())
        self.down_scope_entry_tab_1.insert(0, get_data.down_scope_tab1.get())
        self.up_scope_entry_tab_1.insert(0, get_data.up_scope_tab_1.get())
        self.scale_time_chart_entry_tab_1.insert(0, get_data.scale_time_chart.get())
        self.name_of_chart_entry_tab3.insert(0, get_data.name_of_chart.get())
        self.name_of_X_axis_entry.insert(0, get_data.name_of_X_axis_tab3.get())
        self.unit_of_X_axis_entry.insert(0, get_data.unit_of_X_axis_tab3.get())
        self.name_of_Y_axis_entry_tab3.insert(0, get_data.name_of_Y_axis_tab3.get())
        self.unit_of_Y_axis_entry_tab3.insert(0, get_data.unit_of_Y_axis_tab3.get())



    def show_save_file_cfg_clicked_tab_0(self):

        file44 = asksaveasfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02',defaultextension = '*.txt', mode='w',filetypes=[('TXT Files', '*.txt')])
        self.save_name_cfg_var.set(str(file44.name))
        self.controller.save_cfg_data_tab0()




    def show_open_file_clicked_tab_0(self):


        try:
            file1 = askopenfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='r', filetypes=[('CSV Files', '*.csv')])
            self.open_name_var.set(str(file1.name))
            self.show_file_tab0.config(text='ok')
            self.show_file_tab0.after(self.delay_time,lambda: self.show_file_tab0.config(text='Pobierz dane'))



        except:
            errors.err_lack_of_file()




    def show_save_file_clicked(self):


        file2 = asksaveasfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='w',defaultextension = '*.csv', filetypes=[('CSV Files', '*.csv')])

        if file2 is not None:
            self.save_name_var.set(str(file2.name))



    def show_open_picture_clicked_tab_0(self):

        picture1 = askopenfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='r', filetypes=[
                    ("image", ".jpeg"),
                    ("image", ".png"),
                    ("image", ".jpg"),
                    ("image", ".bmp")
                ])

        self.name_picture.set(str(picture1.name))


    def open_button_clicked(self):

        try:
            self.controller.open_data()

        except:
            errors.err_bad_data()








#########################################################################################################################




    def count_button_clicked_tab_0(self):
        try:
            self.controller.counter()
            self.count_button_count_basic_tab0.config(text='ok')
            self.count_button_count_basic_tab0.after(self.delay_time,lambda: self.count_button_count_basic_tab0.config(text='Przelicz'))



        except:
            errors.err_export_count()

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

    def choice_btn_foto_back_clicked_tab_0(self):
        self.controller.choice_btn_foto_back_tab_0()

    def draw_btn_foto_back_clicked_tab_0(self):
        if self.switch_background :
            self.draw_chart_button_background.config(text='wykres bez tła')
            self.switch_background = False
        else :
            self.draw_chart_button_background.config(text='wykres z tłem')
            self.switch_background = True
            self.controller.draw_btn_foto_back_tab_0()





#####################################################################################################################




    def show_open_file_clicked_tab_1(self):

        try:
            file11 = askopenfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='r',
                            filetypes=[('CSV Files', '*.csv')],)

            self.open_name_var.set(str(file11.name))
            self.open_button_data_tab_1.config(text='ok')
            self.open_button_data_tab_1.after(self.delay_time,lambda: self.open_button_data_tab_1.config(text='Pobierz dane'))
        except:

            errors.err_lack_of_file()

            # messagebox.showerror('ERROR', 'Brak pliku CSV')







    def get_data_button_clicked_tab_1(self):
        """
        Handle button click event
        :return:
        """
        try:
            self.controller.open_data_tab_1()
            print ('ok')
            self.open_button_tab_1.config(text='ok')
            self.open_button_tab_1.after(self.delay_time, lambda: self.open_button_tab_1.config(text='Pobierz dane' ))


        except:
            errors.err_bad_data()



    def natural_chart_clicked_tab_1(self):
        #self.controller.natural_chart_execution()
        self.controller.draw_data_tab_1()

    def set_button_clicked_tab_1(self):

        try :
            self.controller.set_data_tab_1()
            self.set_button_count_tab_1.config(text='ok')
            self.set_button_count_tab_1.after(self.delay_time,lambda: self.set_button_count_tab_1.config(text='Ustaw'))
        except:
            errors.err_bad_process()


    def draw_slice_button_clicked_tab_1(self):
        self.controller.draw_slice_data_tab_1()

    def export_clicked_tab_1(self):

        try:
            self.controller.export_to_tab_0()


            self.export_button_count_tab_1.config(text='ok')
            self.export_button_count_tab_1.after(self.delay_time, lambda: self.export_button_count_tab_1.config(text='Zapisz'))

        except:
            errors.err_export_problem()



    def save_modyfied_data_clicked_tab_1(self):
        try:
            self.controller.save_modyfied_data_clicked_tab_1()
            self.save_button_tab_1.config(text='ok')
            self.save_button_tab_1.after(self.delay_time, lambda: self.save_button_tab_1.config(text='Zapisz'))



        except:
            errors.err_save_problem()


###################################################################################################################################
    def canal_01(self):

        if self.is_on_canal_01:
            self.data_trans_chart_01_tab_2()
            self.is_on_canal_01 = False
            self.open_button_chart_01_tab_2.config(text="01 Zajęta")

        else:
            self.is_on_canal_01 = True
            self.data_delete_chart_01_tab_2()
            self.open_button_chart_01_tab_2.config(text="01 Otwarta")

    def canal_02(self):

        if self.is_on_canal_02:
            self.data_trans_chart_02_tab_2()
            self.is_on_canal_02 = False
            self.open_button_chart_02_tab_2.config(text="02 Zajęta ")

        else:
            self.is_on_canal_02 = True
            self.data_delete_chart_02_tab_2()
            self.open_button_chart_02_tab_2.config(text="02 Otwarta")

    def canal_03(self):

        if self.is_on_canal_03:
            self.data_trans_chart_03_tab_2()
            self.is_on_canal_03 = False
            self.open_button_chart_03_tab_2.config(text="03 Zajęta")

        else:
            self.is_on_canal_03 = True
            self.data_delete_chart_03_tab_2()
            self.open_button_chart_03_tab_2.config(text="03 Otwarta")

    def canal_04(self):

        if self.is_on_canal_04:
            self.data_trans_chart_04_tab_2()
            self.is_on_canal_04 = False
            self.open_button_chart_04_tab_2.config(text="04 Zamknięta")

        else:
            self.is_on_canal_04 = True
            self.data_delete_chart_04_tab_2()
            self.open_button_chart_04_tab_2.config(text="04 Otwarta")

    def canal_05(self):

        if self.is_on_canal_05:
            self.data_trans_chart_05_tab_2()
            self.is_on_canal_05 = False
            self.open_button_chart_05_tab_2.config(text="05 Zamknięta")

        else:
            self.is_on_canal_05 = True
            self.data_delete_chart_05_tab_2()
            self.open_button_chart_05_tab_2.config(text="05 Otwarta")

    def canal_06(self):

        if self.is_on_canal_06:
            self.data_trans_chart_06_tab_2()
            self.is_on_canal_06 = False
            self.open_button_chart_06_tab_2.config(text="06 Zamknięta")

        else:
            self.is_on_canal_06 = True
            self.data_delete_chart_06_tab_2()
            self.open_button_chart_06_tab_2.config(text="06 Otwarta")

    ###################################################################################################################################
    def data_trans_chart_01_tab_2(self):
       self.controller.trans_01_tab_2()
       self.controller.agg_tab_2()

    def data_trans_chart_02_tab_2(self):
       self.controller.trans_02_tab_2()
       self.controller.agg_tab_2()

    def data_trans_chart_03_tab_2(self):
       self.controller.trans_03_tab_2()
       self.controller.agg_tab_2()

    def data_trans_chart_04_tab_2(self):
       self.controller.trans_04_tab_2()
       self.controller.agg_tab_2()

    def data_trans_chart_05_tab_2(self):
        self.controller.trans_05_tab_2()
        self.controller.agg_tab_2()

    def data_trans_chart_06_tab_2(self):
        self.controller.trans_06_tab_2()
        self.controller.agg_tab_2()


    def data_delete_chart_01_tab_2(self):
        self.controller.data_delete_chart_01()

    def data_delete_chart_02_tab_2(self):
        self.controller.data_delete_chart_02()

    def data_delete_chart_03_tab_2(self):
        self.controller.data_delete_chart_03()

    def data_delete_chart_04_tab_2(self):
        self.controller.data_delete_chart_04()

    def data_delete_chart_05_tab_2(self):
        self.controller.data_delete_chart_05()

    def data_delete_chart_06_tab_2(self):
        self.controller.data_delete_chart_06()


    ####################################################################################################################################

    def aggregation_united_data_clicked_tab_2(self):
        self.controller.agg_tab_2()
    def draw_united_data_clicked_tab_2(self):
        self.controller.united_chart_execution_tab_2()

    def data_save_clicked_tab_2(self):
        # self.controller.save_data_clicked_tab_2()
        self.controller.save_data_clicked_tab_2()

    def trend_save_clicked_tab_2(self):
        # self.controller.save_data_clicked_tab_2()
        self.controller.save_trend_clicked_tab_2()




    #######################################################################################################################################




    # def show_error(self, message):
    #     """
    #     Show an error message
    #     :param message:
    #     :return:
    #     """
    #     self.message_label['text'] = message
    #     self.message_label['foreground'] = 'red'
    #     self.message_label.after(3000, self.hide_message)
    #
    #
    # def show_success(self, message):
    #     """
    #     Show a success message
    #     :param message:
    #     :return:
    #     """
    #     self.message_label['text'] = message
    #     self.message_label['foreground'] = 'green'
    #     self.message_label.after(3000, self.hide_message)
    #
    #     # reset the form
    #     self.name_entry['foreground'] = 'black'
    #     self.open_name_var.set('')
    #
    #
    #
    # def hide_message(self):
    #     """
    #     Hide the message
    #     :return:
    #     """
    #     self.message_label['text'] = ''

###################################################################################################################




#######################################################################################################################
#######################################################################################################################




########################################################################################################################