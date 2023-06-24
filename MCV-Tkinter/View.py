import re
import tkinter as tk
from tkinter import ttk
import source
from Controller import Controller
from Model import Model


window = tk.Tk()
window.title("EVOT_printer")
window.geometry('660x480')

tab_parent = ttk.Notebook(window)
tab0 = ttk.Frame(tab_parent)
tab1 = ttk.Frame(tab_parent)




class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets

        #####################

        self.label = ttk.Label(tab0)
        self.label.grid(row=1,column = 0)




        self.name_label = ttk.Label(tab0, text='nazwa pliku z danymi:')
        self.name_label.grid(row=2, column=0)

        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(tab0, textvariable=self.name_var, width=30)
        self.name_entry.grid(row=2, column=1, sticky=tk.NSEW)



        #######################


        self.label = ttk.Label(tab0)
        self.label.grid(row=3, column=0)




        self.distance_label = ttk.Label(tab0, text='odleglość:')
        self.distance_label.grid(row=4, column=0)



        self.distance_var = tk.StringVar()
        self.distance_entry = ttk.Entry(tab0, textvariable=self.distance_var, width=30)
        self.distance_entry.grid(row=4, column=1, sticky=tk.NSEW)

        ######################

        self.label = ttk.Label(tab0)
        self.label.grid(row=5, column=0)


        self.density_label = ttk.Label(tab0, text='gęstość:')
        self.density_label.grid(row = 6, column=0)

        self.density_var = tk.StringVar()
        self.density_entry = ttk.Entry(tab0, textvariable=self.density_var, width=30)
        self.density_entry.grid(row = 6, column=1, sticky=tk.NSEW)

        #######################

        self.label = ttk.Label(tab0)
        self.label.grid(row=7, column=0)

        self.up_scope_label = ttk.Label(tab0, text='dolny zakres:')
        self.up_scope_label.grid(row = 8, column=0)

        self.up_scope_var = tk.StringVar()
        self.up_scope_entry = ttk.Entry(tab0, textvariable=self.up_scope_var, width=30)
        self.up_scope_entry.grid(row = 8, column=1, sticky=tk.NSEW)

        #######################

        self.label = ttk.Label(tab0)
        self.label.grid(row=9, column=0)


        self.down_scope_label = ttk.Label(tab0, text='górny zakres:')
        self.down_scope_label.grid(row = 8, column=3)

        self.down_scope_var = tk.StringVar()
        self.down_scope_entry = ttk.Entry(tab0, textvariable=self.down_scope_var, width=30)
        self.down_scope_entry.grid(row = 8, column=4, sticky=tk.NSEW)










        # open_data
        self.open_button = ttk.Button(tab0, text='Open', command=self.open_button_clicked)
        self.open_button.grid(row=1, column=3, padx=10)

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

    def open_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:

            self.controller.open_data()

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

