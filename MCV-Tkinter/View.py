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
window.geometry('750x700')

tab_parent = ttk.Notebook(window)
tab0 = ttk.Frame(tab_parent)





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


        # create widgets

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


        self.show_file = ttk.Button(lf1, text='Wskaż plik csv', command=self.show_open_file_clicked)
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


        self.count_button_count = ttk.Button(lf2, text='Przelicz', command=self.count_button_clicked)
        self.count_button_count.grid(row=35, column=0, padx=10)


        self.open_button_draw_natural = ttk.Button(lf2, text='Rysuj wykres naturalny',
                                                   command=self.natural_chart_clicked)

        self.open_button_draw_natural.grid(row=35, column=1, padx=10)


        self.open_button = ttk.Button(lf2, text='Zapisz', command=self.nature_data_button_clicked)
        self.open_button.grid(row=35, column=3, padx=10)


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


        self.count_button_count = ttk.Button(lf3, text='Przelicz', command=self.count_button_clicked)
        self.count_button_count.grid(row=100, column=0, padx=10)

        #############################






        self.open_button_draw_modified = ttk.Button(lf3, text='Rysuj wykres obrobiony', command=self.modified_chart_clicked)
        self.open_button_draw_modified.grid(row=100, column=1, padx=10)

        ############################


        #
        self.open_button_save_data= ttk.Button(lf3, text='Zapisz dane', command=self.save_modify_button_clicked)
        self.open_button_save_data.grid(row=100, column=3, padx=10)

        #########################


    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def show_open_file_clicked(self):

        file1 = askopenfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='r', filetypes=[('CSV Files', '*.csv')])
        if file1 is not None:
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


    def nature_data_button_clicked(self):

        if self.controller:
            self.controller.save_nature_data()


    def save_modify_button_clicked(self):
        if self.controller:
            self.controller.save_modify_data()



    def count_button_clicked(self):

        self.controller.counter()

    def natural_chart_clicked(self):
        self.controller.natural_chart_execution()


    def modified_chart_clicked(self):
        self.controller.modified_chart_execution()


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

