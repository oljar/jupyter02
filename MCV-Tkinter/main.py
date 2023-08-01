import re
import tkinter as tk
from tkinter import ttk
import source
from Controller import Controller
from Model import Model
from View import View
import View as V



class Application(tk.Frame):
        def __init__(self, master):
            super(Application, self).__init__(master)


                # create a model


view = View(V.window)


name = view.open_name_var.get()

dist_border = tk.StringVar()
dens_factor = tk.StringVar()
modify_down_scope = tk.StringVar()
modify_up_scope = tk.StringVar()
limit_down_scope = tk.StringVar()
limit_up_scope = tk.StringVar()
x_var = tk.StringVar()
y_var = tk.StringVar()
x_math_form = tk.StringVar()
y_math_form = tk.StringVar()
polynominal_degree = tk.StringVar()




model = Model(name,dist_border,dens_factor,modify_down_scope,modify_up_scope,x_var,y_var,x_math_form,y_math_form,polynominal_degree, limit_down_scope, limit_up_scope)



controller = Controller(model, view)



# set the controller to view
view.set_controller(controller)




V.tab_parent.add(V.tab0,text = 'ustaw')


V.tab_parent.pack(expand = 1, fill = 'both')

app =Application(V.window)



#check

V.window.mainloop()
