import re
import tkinter as tk
from tkinter import ttk
import source
from Controller import Controller
from Model import Model
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile


window = tk.Tk()
window.title("EVOT_printer")
window.geometry('660x480')

tab_parent = ttk.Notebook(window)
tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)




class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.name_var = StringVar()
        self.dist_border_var= StringVar()
        self.density_var = tk.StringVar()
        self.x_var = tk.StringVar()
        self.y_var = tk.StringVar()


        # create widgets

        #####################

        self.label = ttk.Label(tab0)
        self.label.grid(row=10,column = 0)






        self.show_file = ttk.Button(tab0, text='Wskaż plik csv', command=self.show_file_clicked)
        self.show_file.grid(row=20, column=0, padx=10)

        ######################

        self.label = ttk.Label(tab0)
        self.label.grid(row=21, column=0)

        self.distance_label = ttk.Label(tab0, text='X')
        self.distance_label.grid(row=22, column=0)

        self.distance_entry = ttk.Entry(tab0, textvariable=self.x_var, width=10)
        self.distance_entry.grid(row=22, column=1, sticky=tk.NSEW)

        self.distance_label = ttk.Label(tab0, text='Y')
        self.distance_label.grid(row=22, column=2)

        self.distance_entry = ttk.Entry(tab0, textvariable=self.y_var, width=10)
        self.distance_entry.grid(row=22, column=3, sticky=tk.NSEW)





        self.label = ttk.Label(tab0)
        self.label.grid(row=24, column=0)

        self.open_button = ttk.Button(tab0, text='Pobierz dane', command=self.open_button_clicked)
        self.open_button.grid(row=25, column=0, padx=10)






        #######################


        self.label = ttk.Label(tab0)
        self.label.grid(row=30, column=0)




        self.distance_label = ttk.Label(tab0, text='odleglość:')
        self.distance_label.grid(row=40, column=0)



        self.distance_entry = ttk.Entry(tab0, textvariable=self.dist_border_var, width=30)
        self.distance_entry.grid(row=40, column=1, sticky=tk.NSEW)


        ######################

        self.label = ttk.Label(tab0)
        self.label.grid(row=50, column=0)


        self.density_label = ttk.Label(tab0, text='gęstość:')
        self.density_label.grid(row = 60, column=0)


        self.density_entry = ttk.Entry(tab0, textvariable=self.density_var, width=30)
        self.density_entry.grid(row = 60, column=1, sticky=tk.NSEW)


        #######################
        #
        self.label = ttk.Label(tab0)
        self.label.grid(row=70, column=0)


        self.down_scope_label = ttk.Label(tab0, text='dolny zakres:')
        self.down_scope_label.grid(row = 80, column=0)

        self.down_scope_var = tk.StringVar()
        self.down_scope_entry = ttk.Entry(tab0, textvariable=self.down_scope_var, width=30)
        self.down_scope_entry.grid(row = 80, column=1, sticky=tk.NSEW)

        #######################



        self.up_scope_label = ttk.Label(tab0, text='górny zakres:')
        self.up_scope_label.grid(row = 80, column=2)

        self.up_scope_var = tk.StringVar()
        self.up_scope_entry = ttk.Entry(tab0, textvariable=self.up_scope_var, width=30)
        self.up_scope_entry.grid(row = 80, column=3, sticky=tk.NSEW)



        self.label = ttk.Label(tab0)
        self.label.grid(row=90, column=0)


        # open_data button

        self.label = ttk.Label(tab0)
        self.label.grid(row=24, column=0)

        self.open_button_get_data = ttk.Button(tab0, text='Pobierz dane', command=self.open_button_clicked)
        self.open_button_get_data.grid(row=25, column=0, padx=10)

        ##########################
        #


        self.count_button_count = ttk.Button(tab0, text='Przelicz', command=self.count_button_clicked)
        self.count_button_count.grid(row=100, column=0, padx=10)

        #############################

        self.open_button_draw_natural = ttk.Button(tab0, text='Rysuj wykres naturalny', command=self.natural_chart_clicked)
        self.open_button_draw_natural.grid(row=100, column=1, padx=10)

        ############################



        self.open_button_draw_modified = ttk.Button(tab0, text='Rysuj wykres obrobiony', command=self.modified_chart_clicked)
        self.open_button_draw_modified.grid(row=100, column=2, padx=10)

        ############################

        self.label = ttk.Label(tab0)
        self.label.grid(row=110, column=0)
        #
        self.open_button_save_data= ttk.Button(tab0, text='Zapisz dane',command=self.save_button_clicked)
        self.open_button_save_data.grid(row=120, column=0, padx=10)



        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def show_file_clicked(self):

        file = askopenfile(initialdir='C:\\Users\oljar\PycharmProjects\jupiter02', mode='r', filetypes=[('CSV Files', '*.csv')])
        if file is not None:
            self.name_var.set(str(file.name))

    def open_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.open_data()

    def save_button_clicked(self):
        if self.controller:
            self.controller.save_data()



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
        self.name_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''

