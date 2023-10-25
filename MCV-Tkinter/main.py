import tkinter as tk
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
name_cfg = tk.StringVar()
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
name_of_chart_var = tk.StringVar()

name_of_X_axis_var = tk.StringVar()
unit_of_X_axis_var = tk.StringVar()
scope_min_of_X_axis_var = tk.StringVar()
scope_max_of_X_axis_var = tk.StringVar()

name_of_Y_axis_var = tk.StringVar()
unit_of_Y_axis_var = tk.StringVar()
scope_min_of_Y_axis_var = tk.StringVar()
scope_max_of_Y_axis_var = tk.StringVar()

name_serial_var = tk.StringVar()

scale_time_chart = tk.StringVar()

scope_up_back_entry_x_var = tk.StringVar()
scope_down_back_entry_x_var = tk.StringVar()

scope_up_back_entry_y_var = tk.StringVar()
scope_down_back_entry_y_var = tk.StringVar()
switch_background = tk.BooleanVar()

name_picture = tk.StringVar()
trans_picture = tk.StringVar()





model = Model(name,name_cfg,dist_border,dens_factor,modify_down_scope,modify_up_scope,x_var,y_var,x_math_form,y_math_form,polynominal_degree, limit_down_scope, limit_up_scope
              ,step, time_var_tab1, y1_var_tab1, y2_var_tab1, down_scope_var_tab_1, up_scope_var_tab_1,
              name_of_chart_var,
              name_of_X_axis_var,unit_of_X_axis_var,scope_min_of_X_axis_var,scope_max_of_X_axis_var,
              name_of_Y_axis_var,unit_of_Y_axis_var,scope_min_of_Y_axis_var,scope_max_of_Y_axis_var,
              name_serial_var,
              scale_time_chart,
              scope_up_back_entry_x_var,
              scope_down_back_entry_x_var,
              scope_up_back_entry_y_var,
              scope_down_back_entry_y_var,
              switch_background,
              name_picture,
              trans_picture
              )

controller = Controller(model, view)

# set the controller to view
view.set_controller(controller)


V.tab_parent.add(V.tab3,text = 'jednostki')
V.tab_parent.add(V.tab1,text = 'zakres')
V.tab_parent.add(V.tab0,text = 'ustawienia')
V.tab_parent.add(V.tab2,text = 'agregacja')




V.tab_parent.pack(expand = 1, fill = 'both')

app =Application(V.window)



#check

V.window.mainloop()