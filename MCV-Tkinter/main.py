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



name = tk.StringVar()
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
step = tk.StringVar()

time_var_tab1 = tk.StringVar()
y1_var_tab1 = tk.StringVar()
y2_var_tab1 = tk.StringVar()
down_scope_var_tab_1 = tk.StringVar()
up_scope_var_tab_1 =  tk.StringVar()



model = Model(name,dist_border,dens_factor,modify_down_scope,modify_up_scope,x_var,y_var,x_math_form,y_math_form,polynominal_degree, limit_down_scope, limit_up_scope
              ,step, time_var_tab1, y1_var_tab1, y2_var_tab1, down_scope_var_tab_1, up_scope_var_tab_1)



controller = Controller(model, view)



# set the controller to view
view.set_controller(controller)





V.tab_parent.add(V.tab1,text = 'zakres')
V.tab_parent.add(V.tab0,text = 'ustawienia')
V.tab_parent.pack(expand = 1, fill = 'both')

app =Application(V.window)



#check

V.window.mainloop()
