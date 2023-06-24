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
        # create widgets

        #####################

        self.label = ttk.Label(tab0)
        self.label.grid(row=10,column = 0)






        self.show_file = ttk.Button(tab0, text='Wskaż plik csv', command=self.show_file_clicked)
        self.show_file.grid(row=20, column=0, padx=10)

        ######################


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

        self.label = ttk.Label(tab0)
        self.label.grid(row=70, column=0)

        self.up_scope_label = ttk.Label(tab0, text='dolny zakres:')
        self.up_scope_label.grid(row = 80, column=0)

        self.up_scope_var = tk.StringVar()
        self.up_scope_entry = ttk.Entry(tab0, textvariable=self.up_scope_var, width=30)
        self.up_scope_entry.grid(row = 80, column=1, sticky=tk.NSEW)

        #######################
        #
        # self.label = ttk.Label(tab0)
        # self.label.grid(row=90, column=0)


        self.down_scope_label = ttk.Label(tab0, text='górny zakres:')
        self.down_scope_label.grid(row = 80, column=3)

        self.down_scope_var = tk.StringVar()
        self.down_scope_entry = ttk.Entry(tab0, textvariable=self.down_scope_var, width=30)
        self.down_scope_entry.grid(row = 80, column=4, sticky=tk.NSEW)

        ######################


        self.label = ttk.Label(tab0)
        self.label.grid(row=90, column=0)


        # open_data button

        self.label = ttk.Label(tab0)
        self.label.grid(row=24, column=0)

        self.open_button = ttk.Button(tab0, text='Pobierz dane', command=self.open_button_clicked)
        self.open_button.grid(row=25, column=0, padx=10)

        ##########################
        #


        self.open_button = ttk.Button(tab0, text='Przelicz', command=self.open_button_clicked)
        self.open_button.grid(row=100, column=2, padx=10)

        ############################

        # self.label = ttk.Label(tab0)
        # self.label.grid(row=12, column=0)

        self.open_button = ttk.Button(tab0, text='rysuj wykres', command=self.open_button_clicked)
        self.open_button.grid(row=100, column=4, padx=10)

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
            self.controller.counter()


    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.name_entry['foreground'] = 'red'

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

