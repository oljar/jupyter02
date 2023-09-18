import re
import tkinter as tk
from tkinter import ttk

import pandas

import source

import csv
import pandas as pd
from scipy.spatial import distance
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import numpy as np
import math
from datetime import datetime
import numpy as np


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import copy


class Controller:
    def __init__(self, model, view):
        self.z = None
        self.agg_tab_2_final = None
        self.model = model
        self.view = view

        self.temporary_chart_1_data = 0
        self.temporary_chart_2_data = 0
        self.temporary_chart_3_data = 0
        self.temporary_chart_4_data = 0
        self.temporary_chart_5_data = 0
        self.temporary_chart_6_data = 0
        self.trans_perm_01 = False
        self.trans_perm_02 = False
        self.trans_perm_03 = False
        self.trans_perm_04 = False
        self.trans_perm_05 = False
        self.trans_perm_06 = False
        self.agg = []
        self.coefs = []

    def open_data(self):


        self.model.name = self.view.open_name_var.get()

        self.model.x_var = (self.view.x_var.get())
        self.model.y_var = (self.view.y_var.get())

        self.df1 = self.model.open_data()

        print(self.df1)

    def export_to_tab_0(self):

        self.view.x_var.set(self.view.y1_var_tab1.get())
        self.view.y_var.set(self.view.y2_var_tab1.get())

        self.model.x_var = (self.view.x_var.get())
        self.model.y_var = (self.view.y_var.get())
        self.df1 = pd.DataFrame()
        self.df1[self.model.time_var_tab1] = pd.DataFrame(self.time_modyfied_tab1_exam_pts)
        self.df1[self.model.y1_var_tab1] = pd.DataFrame(self.y1_modyfied_tab1_exam_pts)
        self.df1[self.model.y2_var_tab1] = pd.DataFrame(self.y2_modyfied_tab1_exam_pts)

        print(self.df1)

    #

    def counter(self):

        self.x_exam_pts_basic = []
        self.y_exam_pts_basic = []

        self.model.x_math_form.set(self.view.x_math_form.get())
        self.model.y_math_form.set(self.view.y_math_form.get())

        # examinated points

        x_tag = str(self.view.x_var.get())
        y_tag = str(self.view.y_var.get())

        df1 = self.df1
        df1 = df1.sort_values(by=x_tag, ascending=True)

        df1 = df1[df1[x_tag] >= 0]

        df1 = df1[df1[y_tag] >= 0]

        df1[x_tag] = df1[x_tag].fillna(df1[x_tag].median())
        df1[y_tag] = df1[y_tag].fillna(df1[y_tag].median())

        self.x_exam_pts = (df1[x_tag]).tolist()  # definition of columns -x

        cor_factor_x = str(self.view.x_math_form.get())

        self.x_exam_pts = [eval(cor_factor_x) for x in self.x_exam_pts]

        self.y_exam_pts = (df1[y_tag]).tolist()  # definition of columns -y

        cor_factor_y = str(self.view.y_math_form.get())

        self.y_exam_pts = [eval(cor_factor_y) for y in self.y_exam_pts]

        print(self.y_exam_pts)

        # c = 41.1  # reducer constns
        #
        # self.x_exam_pts = [(c * math.sqrt(x)) for x in x_points]

        def scope_limit(self):

            self.model.limit_down_scope.set(self.view.total_down_scope_var.get())
            self.model.limit_up_scope.set(self.view.total_up_scope_var.get())

            lim_a = float(self.model.limit_down_scope.get())
            lim_b = float(self.model.limit_up_scope.get())

            lim_down = int(len(self.x_exam_pts) * (lim_a / 100))
            lim_up = int(len(self.x_exam_pts) * (lim_b / 100))

            x_slice, y_slice = self.x_exam_pts[lim_down:lim_up], self.y_exam_pts[lim_down:lim_up]

            #
            # print (f'gora {x_slice}')
            # print(f'dol {y_slice}')

            return x_slice, y_slice

        def main_proces(ex, ey, dist_border=10000):

            # input filters

            self.model.polynominal_degree.set(self.view.polynominal_degree.get())

            self.model.step.set(self.view.step.get())

            deg = int(self.model.polynominal_degree.get())  # stopień wielomianu

            # trend line

            x_exam_points = ex
            y_exam_points = ey

            start = x_exam_points[0]
            stop = x_exam_points[(len(x_exam_points) - 1)]

            #  precision of sampling
            step = float(str(self.model.step.get()))
            sequence = list(np.arange(start, stop, step))
            x_trend_points = sequence

            # coefficients od polynomial 2-grade (trend)
            self.coefs = poly.polyfit(x_exam_points, y_exam_points, deg)
            print(f'współczynniki wielomianu {self.coefs}')
            y_trend_points = poly.polyval(x_trend_points, self.coefs)

            def distance_point_to_curve(x0, y0, x_curve, y_curve):
                distances = np.sqrt((x0 - x_curve) ** 2 + (y0 - y_curve) ** 2)
                # min_distance = np.min(distances)
                return distances

            def main_iteration(x1, y1, x, y):
                dist_all = []
                for i in range(len(x)):
                    dist_sum = []
                    x0 = x[i]
                    y0 = y[i]
                    for j in range(len(x1)):
                        a = (distance_point_to_curve(x0, y0, x1[j], y1[j]))
                        dist_sum.append(a)
                    min_distance = min(dist_sum)
                    dist_all.append(min_distance)
                return dist_all

            sol_dist_pd = pd.DataFrame(main_iteration(x_trend_points, y_trend_points, x_exam_points, y_exam_points))

            # print(f'd {sol_dist_pd}')
            # print(f'X {x_exam_points}')
            # print(f'Y {y_exam_points}')

            sol_exam = pd.DataFrame()
            sol_exam['dist'] = sol_dist_pd
            sol_exam['X_Exam'] = x_exam_points
            sol_exam['Y_Exam'] = y_exam_points

            # print('examinated points with distance')
            #  print(sol_exam)

            sol_trend = pd.DataFrame()
            sol_trend['X_Trend'] = pd.DataFrame(x_trend_points)
            sol_trend['Y_Trend'] = pd.DataFrame(y_trend_points)

            # print(sol_trend)

            print('y trend')
            print(f'współcznimmiki lini trendu {self.coefs}')

            # distance border
            filtred = sol_exam[sol_exam['dist'] < dist_border]

            density = len(x_exam_points) / (x_exam_points[(len(x_exam_points) - 1)] - x_exam_points[0])

            x_output = filtred['X_Exam'].tolist()
            y_output = filtred['Y_Exam'].tolist()

            x_trend_points = list(x_trend_points)
            y_trend_points = list(y_trend_points)

            return x_output, y_output, x_trend_points, y_trend_points

        def density_control(x, y, density=1):

            n = int(1 / density)

            x_set = (x[::n])
            y_set = (y[::n])

            return x_set, y_set

        print(f'SCOPE x {scope_limit(self)[0]}')
        print(f'SCOPE y {scope_limit(self)[1]}')

        self.x_exam_pts_basic = scope_limit(self)[0]
        self.y_exam_pts_basic = scope_limit(self)[1]

        try:
            self.model.dist_border = int(self.view.dist_border_var.get())
            dist_fact = self.model.dist_border
        except:
            dist_fact = 10000

        x_exam_pts_2, y_exam_pts_2, self.x_trend_pts_1, self.y_trend_pts_1 = main_proces(self.x_exam_pts_basic,
                                                                                         self.y_exam_pts_basic,
                                                                                         dist_fact)

        #

        x_exam_pts_3, y_exam_pts_3, self.x_trend_pts_1, self.y_trend_pts_1 = main_proces(x_exam_pts_2, y_exam_pts_2)

        # hier set % scope of slice

        self.model.modify_down_scope.set(self.view.down_scope_var.get())
        self.model.modify_up_scope.set(self.view.up_scope_var.get())

        try:
            a = float(self.model.modify_down_scope.get())
        except:
            a = 0

        try:
            b = float(self.model.modify_up_scope.get())
        except:
            b = 100

        print(f'zakres dół {a}')
        print(f'zakres góra {b}')

        down = int(len(x_exam_pts_3) * (a / 100))
        up = int(len(x_exam_pts_3) * (b / 100))

        x_slice, y_slice = x_exam_pts_3[down:up], y_exam_pts_3[down:up]

        #  Here set density of slice

        try:
            self.model.dens_factor.set(float(self.view.density_var.get()))
        except:
            self.model.dens_factor.set(1)

        x_slice_1, y_slice_1 = density_control(x_slice, y_slice, float(self.model.dens_factor.get()))

        # change data  with corrected density in described scope - down/up

        x_exam_pts_3[down:up:1], y_exam_pts_3[down:up:1] = x_slice_1[::1], y_slice_1[::1]

        self.x_exam_pts_4, self.y_exam_pts_4, self.x_trend_pts_4, self.y_trend_pts_4 = main_proces(x_exam_pts_3,
                                                                                                   y_exam_pts_3)

    def natural_chart_execution_tab_0(self):

        name_of_X_axis_var = self.view.name_of_X_axis_var.get()
        unit_of_X_axis_var = self.view.unit_of_X_axis_var.get()

        name_of_Y_axis_var = self.view.name_of_Y_axis_var.get()
        unit_of_Y_axis_var = self.view.unit_of_Y_axis_var.get()

        aux_list = [[self.x_exam_pts_basic, self.y_exam_pts_basic, self.x_trend_pts_1, self.y_trend_pts_1,
                     '', name_of_X_axis_var, unit_of_X_axis_var, '', '', name_of_Y_axis_var, unit_of_Y_axis_var, '', '',
                     '']]

        self.chart1(aux_list)

    def modyfied_chart_execution_tab_0(self):
        # def chart(x, y, x_trend, y_trend):
        #     fig = plt.figure()
        #     ax1 = fig.add_subplot(111)
        #     ax2 = ax1.twiny()
        #
        #     ax1.plot(x, y, "-o")
        #     ax1.plot(x_trend, y_trend, "-s")
        #
        #     ax2.set_xlim(0, 100)
        #
        #     plt.show()
        #
        # chart(self.x_exam_pts_4, self.y_exam_pts_4, self.x_trend_pts_4, self.y_trend_pts_4)

        name_of_X_axis_var = self.view.name_of_X_axis_var.get()
        unit_of_X_axis_var = self.view.unit_of_X_axis_var.get()

        name_of_Y_axis_var = self.view.name_of_Y_axis_var.get()
        unit_of_Y_axis_var = self.view.unit_of_Y_axis_var.get()

        aux_list = [[self.x_exam_pts_4, self.y_exam_pts_4, self.x_trend_pts_4, self.y_trend_pts_4,
                     '', name_of_X_axis_var, unit_of_X_axis_var, '', '', name_of_Y_axis_var, unit_of_Y_axis_var, '', '',
                     '']]

        self.chart1(aux_list)

    def export_nature_data_tab_0(self):

        self.model.name_of_chart_var = self.view.name_of_chart_var.get()

        self.model.name_of_X_axis_var = self.view.name_of_X_axis_var.get()
        self.model.unit_of_X_axis_var = self.view.unit_of_X_axis_var.get()
        self.model.scope_min_of_X_axis_var = self.view.scope_min_of_X_axis_var.get()
        self.model.scope_max_of_X_axis_var = self.view.scope_max_of_X_axis_var.get()

        self.model.name_of_Y_axis_var = self.view.name_of_Y_axis_var.get()
        self.model.unit_of_Y_axis_var = self.view.unit_of_Y_axis_var.get()
        self.model.scope_min_of_Y_axis_var = self.view.scope_min_of_Y_axis_var.get()
        self.model.scope_max_of_Y_axis_var = self.view.scope_max_of_Y_axis_var.get()
        self.model.name_serial_var = self.view.name_serial_var.get()
        self.model.www = 'przesłanie'

        return [self.x_exam_pts_basic, self.y_exam_pts_basic, self.x_trend_pts_1, self.y_trend_pts_1,
                self.model.name_of_chart_var,
                self.model.name_of_X_axis_var, self.model.unit_of_X_axis_var,
                self.model.scope_min_of_X_axis_var, self.model.scope_max_of_X_axis_var,
                self.model.name_of_Y_axis_var, self.model.unit_of_Y_axis_var,
                self.model.scope_min_of_Y_axis_var, self.model.scope_max_of_Y_axis_var,
                self.model.name_serial_var, self.coefs]

    def save_cfg_data_tab0(self):
        dict_to_save={}

        dict_to_save['name_col_x_tab0'] = self.view.x_var.get()
        dict_to_save['name_col_y_tab_0'] = self.view.y_var.get()
        dict_to_save['name_serial_var'] = self.view.name_serial_var.get()
        dict_to_save['polynom_degree'] = self.view.polynominal_degree.get()
        dict_to_save['step_value'] = self.view.step.get()
        dict_to_save['scope_down_entry_tab0'] = self.view.total_down_scope_var.get()
        dict_to_save['scope_up_entry_tab0'] = self.view.total_up_scope_var.get()
        dict_to_save['formula_x'] = self.view.x_math_form.get()
        dict_to_save['formula_y'] = self.view.y_math_form.get()
        dict_to_save['time_tag'] = self.view.time_var_tab1.get()
        dict_to_save['column_x_tag_tab1'] = self.view.y1_var_tab1.get()
        dict_to_save['column_y_tag_tab1'] = self.view.y2_var_tab1.get()
        dict_to_save['down_scope_tab1'] = self.view.down_scope_var_tab_1.get()
        dict_to_save['up_scope_tab_1'] = self.view.up_scope_var_tab_1.get()
        dict_to_save['scale_time_chart'] = self.view.scale_time_chart.get()
        dict_to_save['name_of_chart'] = self.view.name_of_chart_var.get()
        dict_to_save['name_of_X_axis_tab3'] = self.view.name_of_X_axis_var.get()
        dict_to_save['unit_of_X_axis_tab3'] = self.view.unit_of_X_axis_var.get()
        dict_to_save['name_of_Y_axis_tab3'] = self.view.name_of_Y_axis_var.get()
        dict_to_save['unit_of_Y_axis_tab3'] = self.view.unit_of_Y_axis_var.get()

        with open(self.view.save_name_cfg_var.get(), 'w', encoding='utf-8') as f:
            for key,value in dict_to_save.items():
                f.write(f'{key}={value}\n')


    def save_nature_data_tab_0(self):
        solution = pd.DataFrame()
        solution[self.view.x_var.get()] = pd.DataFrame(self.x_exam_pts_basic)
        solution[self.view.y_var.get()] = pd.DataFrame(self.y_exam_pts_basic)
        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False,encoding='utf-8')

    def save_modify_data_tab_0(self):
        solution = pd.DataFrame()
        solution[self.view.x_var.get()] = pd.DataFrame(self.x_exam_pts_4)
        solution[self.view.y_var.get()] = pd.DataFrame(self.y_exam_pts_4)
        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False,encoding='utf-8')

    def export_modyfied_data_tab_0(self):

        self.model.name_of_chart_var = self.view.name_of_chart_var.get()

        self.model.name_of_X_axis_var = self.view.name_of_X_axis_var.get()
        self.model.unit_of_X_axis_var = self.view.unit_of_X_axis_var.get()
        self.model.scope_min_of_X_axis_var = self.view.scope_min_of_X_axis_var.get()
        self.model.scope_max_of_X_axis_var = self.view.scope_max_of_X_axis_var.get

        self.model.name_of_Y_axis_var = self.view.name_of_Y_axis_var.get()
        self.model.unit_of_Y_axis_var = self.view.unit_of_Y_axis_var.get()
        self.model.scope_min_of_Y_axis_var = self.view.scope_min_of_Y_axis_var.get()
        self.model.scope_max_of_Y_axis_var = self.view.scope_max_of_Y_axis_var.get()

        return [self.x_exam_pts_4, self.y_exam_pts_4, self.x_trend_pts_4, self.y_trend_pts_4,
                self.model.name_of_chart_var,
                self.model.name_of_X_axis_var, self.model.unit_of_X_axis_var,
                self.model.scope_min_of_X_axis_var, self.model.scope_max_of_X_axis_var,
                self.model.name_of_Y_axis_var, self.model.unit_of_Y_axis_var,
                self.model.scope_min_of_Y_axis_var, self.model.scope_max_of_Y_axis_var,
                self.model.name_serial_var, self.coefs]

        ######################################################################################################################

    # tab_1
    ######################################################################################################################

    def open_data_tab_1(self):

        self.model.name = self.view.open_name_var.get()
        self.model.time_var_tab1 = self.view.time_var_tab1.get()
        self.model.y1_var_tab1 = self.view.y1_var_tab1.get()
        self.model.y2_var_tab1 = self.view.y2_var_tab1.get()
        self.df11 = self.model.open_data_tab_1()

        time_tag_tab1 = self.model.time_var_tab1
        y1_tag_tab1 = str(self.model.y1_var_tab1)
        y2_tag_tab1 = str(self.model.y2_var_tab1)

        df11 = self.df11
        df11 = df11.sort_values(by=time_tag_tab1, ascending=True)

        df11 = df11[df11[y1_tag_tab1] >= 0]
        df11 = df11[df11[y2_tag_tab1] >= 0]

        df11[y1_tag_tab1] = df11[y1_tag_tab1].fillna(df11[y1_tag_tab1].median())
        df11[y2_tag_tab1] = df11[y2_tag_tab1].fillna(df11[y2_tag_tab1].median())

        self.time_tab1_exam_pts = df11[time_tag_tab1].tolist()  # definition of column - time
        self.y1_tab1_exam_pts = df11[y1_tag_tab1].tolist()  # definition of column -y1
        self.y2_tab1_exam_pts = df11[y2_tag_tab1].tolist()  # definition of column -y2

    def chart(self, x, y1, y2, scale_time):
        fig = plt.figure()
        ax1 = fig.add_subplot(111)

        ax1.scatter(x, y1, s=20, c="lightblue", alpha=0.5)
        ax1.scatter(x, y2, s=20, c="orange", alpha=0.5)

        plt.gcf().autofmt_xdate()

        print(x[len(x) - 1])
        print(x[0])

        time_1 = datetime.strptime(x[0], '%H:%M:%S')
        time_1_s = time_1.hour * 3600 + time_1.minute * 60 + time_1.second

        time_2 = datetime.strptime((x[len(x) - 1]), '%H:%M:%S')
        time_2_s = time_2.hour * 3600 + time_2.minute * 60 + time_2.second
        range_time = time_2_s - time_1_s

        ax1.set_xticks(np.arange(-5, range_time, scale_time))

        # Show the major grid and style it slightly.
        ax1.grid(which='major', color='#DDDDDD', linewidth=1.2)
        # Show the minor grid as well. Style it in very light gray as a thin,
        # dotted line.
        ax1.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=1)
        # Make the minor ticks and gridlines show.
        ax1.minorticks_on()
        plt.show()

    def draw_data_tab_1(self):
        time_tab1_exam_pts = self.time_tab1_exam_pts
        y1_tab1_exam_pts = self.y1_tab1_exam_pts
        y2_tab1_exam_pts = self.y2_tab1_exam_pts
        self.model.scale_time_chart = self.view.scale_time_chart.get()
        scale_time_chart = int(self.model.scale_time_chart)

        self.chart(time_tab1_exam_pts, y1_tab1_exam_pts, y2_tab1_exam_pts, scale_time_chart)

    def set_data_tab_1(self):
        # self.model.down_scope_var_tab_1 = datetime.strptime(str(self.view.down_scope_var_tab_1.get()),"%H:%M:%S").time()
        # self.model.up_scope_var_tab_1 = datetime.strptime(str(self.view.up_scope_var_tab_1.get()),"%H:%M:%S").time()

        self.model.down_scope_var_tab_1 = str(self.view.down_scope_var_tab_1.get())
        self.model.up_scope_var_tab_1 = str(self.view.up_scope_var_tab_1.get())

        df101 = pd.DataFrame(self.model.open_data_tab_1())
        df101 = df101.loc[:, [self.model.time_var_tab1, self.model.y1_var_tab1, self.model.y2_var_tab1]]

        df101 = df101[(df101[self.model.time_var_tab1] > (self.model.down_scope_var_tab_1)) & (
                df101[self.model.time_var_tab1] < self.model.up_scope_var_tab_1)]

        # df101 = df101[df101[self.model.time_var_tab1].between_time(self.model.down_scope_var_tab_1, self.model.up_scope_var_tab_1)]
        #
        self.time_modyfied_tab1_exam_pts = (df101[self.model.time_var_tab1]).tolist()
        self.y1_modyfied_tab1_exam_pts = (df101[self.model.y1_var_tab1]).tolist()
        self.y2_modyfied_tab1_exam_pts = (df101[self.model.y2_var_tab1]).tolist()
        #

    def draw_slice_data_tab_1(self):
        time_modyfied_tab1_exam_pts = self.time_modyfied_tab1_exam_pts
        y1_modyfied_tab1_exam_pts = self.y1_modyfied_tab1_exam_pts
        y2_modyfied_tab1_exam_pts = self.y2_modyfied_tab1_exam_pts
        self.model.scale_time_chart = self.view.scale_time_chart.get()
        scale_time_chart = int(self.model.scale_time_chart)

        self.chart(time_modyfied_tab1_exam_pts, y1_modyfied_tab1_exam_pts, y2_modyfied_tab1_exam_pts, scale_time_chart)

    def save_modyfied_data_clicked_tab_1(self):
        solution = pd.DataFrame()
        solution[self.model.time_var_tab1] = pd.DataFrame(self.time_modyfied_tab1_exam_pts)
        solution[self.model.y1_var_tab1] = pd.DataFrame(self.y1_modyfied_tab1_exam_pts)
        solution[self.model.y2_var_tab1] = pd.DataFrame(self.y2_modyfied_tab1_exam_pts)

        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False)




    #########################################################################################################################
    # tab2
    ########################################################################################################################
    def trans_01_tab_2(self):
        self.temporary_chart_1_data = self.export_nature_data_tab_0()
        if self.view.switch_modyfied_export == True:
            self.temporary_chart_1_data = self.export_modyfied_data_tab_0()
        self.trans_perm_01 = True
        self.trans_perm_02 = False
        self.trans_perm_03 = False
        self.trans_perm_04 = False
        self.trans_perm_05 = False
        self.trans_perm_06 = False

    def trans_02_tab_2(self):
        self.temporary_chart_2_data = self.export_nature_data_tab_0()
        if self.view.switch_modyfied_export == True:
            self.temporary_chart_2_data = self.export_modyfied_data_tab_0()
        self.trans_perm_01 = False
        self.trans_perm_02 = True
        self.trans_perm_03 = False
        self.trans_perm_04 = False
        self.trans_perm_05 = False
        self.trans_perm_06 = False

    def trans_03_tab_2(self):
        self.temporary_chart_3_data = self.export_nature_data_tab_0()
        if self.view.switch_modyfied_export == True:
            self.temporary_chart_3_data = self.export_modyfied_data_tab_0()
        self.trans_perm_01 = False
        self.trans_perm_02 = False
        self.trans_perm_03 = True
        self.trans_perm_04 = False
        self.trans_perm_05 = False
        self.trans_perm_06 = False

    def trans_04_tab_2(self):
        self.temporary_chart_4_data = self.export_nature_data_tab_0()
        if self.view.switch_modyfied_export == True:
            self.temporary_chart_4_data = self.export_modyfied_data_tab_0()
        self.trans_perm_01 = False
        self.trans_perm_02 = False
        self.trans_perm_03 = False
        self.trans_perm_04 = True
        self.trans_perm_05 = False
        self.trans_perm_06 = False

    def trans_05_tab_2(self):
        self.temporary_chart_5_data = self.export_nature_data_tab_0()
        if self.view.switch_modyfied_export == True:
            self.temporary_chart_5_data = self.export_modyfied_data_tab_0()
        self.trans_perm_01 = False
        self.trans_perm_02 = False
        self.trans_perm_03 = False
        self.trans_perm_04 = False
        self.trans_perm_05 = True
        self.trans_perm_06 = False

    def trans_06_tab_2(self):
        self.temporary_chart_6_data = self.export_nature_data_tab_0()
        if self.view.switch_modyfied_export == True:
            self.temporary_chart_6_data = self.export_modyfied_data_tab_0()
        self.trans_perm_01 = False
        self.trans_perm_02 = False
        self.trans_perm_03 = False
        self.trans_perm_04 = False
        self.trans_perm_05 = False
        self.trans_perm_06 = True

    ############################################################################
    def data_delete_chart_01(self):
        self.agg_tab_2_final.remove(self.temporary_chart_1_data)
        print(self.agg_tab_2_final)

    def data_delete_chart_02(self):
        self.agg_tab_2_final.remove(self.temporary_chart_2_data)
        print(self.agg_tab_2_final)

    def data_delete_chart_03(self):
        self.agg_tab_2_final.remove(self.temporary_chart_3_data)
        print(self.agg_tab_2_final)

    def data_delete_chart_04(self):
        self.agg_tab_2_final.remove(self.temporary_chart_4_data)
        print(self.agg_tab_2_final)

    def data_delete_chart_05(self):
        self.agg_tab_2_final.remove(self.temporary_chart_5_data)
        print(self.agg_tab_2_final)

    def data_delete_chart_06(self):
        self.agg_tab_2_final.remove(self.temporary_chart_6_data)
        print(self.agg_tab_2_final)

    def agg_tab_2(self):

        print(f'perm01{self.trans_perm_01}')
        print(f'perm02{self.trans_perm_02}')
        print(f'perm03{self.trans_perm_03}')
        print(f'perm04{self.trans_perm_04}')
        print(f'perm05{self.trans_perm_05}')
        print(f'perm06{self.trans_perm_06}')
        if self.temporary_chart_1_data != 0 and self.trans_perm_01:
            self.agg.append(self.temporary_chart_1_data)
            print('append1')
        if self.temporary_chart_2_data != 0 and self.trans_perm_02:
            self.agg.append(self.temporary_chart_2_data)
            print('append2')
        if self.temporary_chart_3_data != 0 and self.trans_perm_03:
            self.agg.append(self.temporary_chart_3_data)
            print('append3')
        if self.temporary_chart_4_data != 0 and self.trans_perm_04:
            self.agg.append(self.temporary_chart_4_data)
            print('append4')
        if self.temporary_chart_5_data != 0 and self.trans_perm_05:
            self.agg.append(self.temporary_chart_5_data)
            print('append5')
        if self.temporary_chart_6_data != 0 and self.trans_perm_06:
            self.agg.append(self.temporary_chart_6_data)
            print('append6')

        self.agg_tab_2_final = self.agg

        return self.agg

    def chart1(self, solist):
        self.model.switch_background = self.view.switch_background
        self.model.scope_down_back_entry_x_var = self.view.scope_down_back_entry_x_var.get()
        self.model.scope_up_back_entry_x_var = self.view.scope_up_back_entry_x_var.get()
        self.model.scope_down_back_entry_y_var = self.view.scope_down_back_entry_y_var.get()
        self.model.scope_up_back_entry_y_var = self.view.scope_up_back_entry_y_var.get()
        self.model.name_picture = str(self.view.name_picture.get())
        self.model.trans_picture = float(self.view.trans_picture.get())
        print(f'prezro{self.model.trans_picture}')
        print(self.model.name_picture)

        fig, ax = plt.subplots()
        num_li = len(solist)

        if num_li == 1 or num_li == 2 or num_li == 3 or num_li == 4 or num_li == 5 or num_li == 6:
            x, y, x_trend, y_trend, name_serial_var = (solist[0])[0], (solist[0])[1], (solist[0])[2], (solist[0])[3], \
                                                      (solist[0])[13]
            sns.scatterplot(x=x, y=y, c="orange", s=40, alpha=0.3, edgecolors='none', label=name_serial_var)
            sns.lineplot(x=x_trend, y=y_trend, color="g", ax=ax, linewidth=1, label=name_serial_var)

        if num_li == 2 or num_li == 3 or num_li == 4 or num_li == 5 or num_li == 6:
            x1, y1, x1_trend, y1_trend, name_serial_var1 = (solist[1])[0], (solist[1])[1], (solist[1])[2], (solist[1])[
                3], (solist[1])[13]
            sns.scatterplot(x=x1, y=y1, c="red", s=40, alpha=0.3, edgecolors='none', label=name_serial_var1)
            sns.lineplot(x=x1_trend, y=y1_trend, color="g", ax=ax, linewidth=1, label=name_serial_var1)

        if num_li == 3 or num_li == 4 or num_li == 5 or num_li == 6:
            x2, y2, x2_trend, y2_trend, name_serial_var2 = (solist[2])[0], (solist[2])[1], (solist[2])[2], (solist[2])[
                3], (solist[2])[13]
            sns.scatterplot(x=x2, y=y2, c="brown", s=40, alpha=0.3, edgecolors='none', label=name_serial_var2)
            sns.lineplot(x=x2_trend, y=y2_trend, color="g", ax=ax, linewidth=1, label=name_serial_var2)

        if num_li == 4 or num_li == 5 or num_li == 6:
            x3, y3, x3_trend, y3_trend, name_serial_var3 = (solist[3])[0], (solist[3])[1], (solist[3])[2], (solist[3])[
                3], (solist[3])[13]
            sns.scatterplot(x=x3, y=y3, c="yellow", s=40, alpha=0.3, edgecolors='none', label=name_serial_var3)
            sns.lineplot(x=x3_trend, y=y3_trend, color="g", ax=ax, linewidth=1, label=name_serial_var3)

        if num_li == 5 or num_li == 6:
            x4, y4, x4_trend, y4_trend, name_serial_var4 = (solist[4])[0], (solist[4])[1], (solist[4])[2], (solist[4])[
                3], (solist[4])[13]
            sns.scatterplot(x=x4, y=y4, c="purple", s=40, alpha=0.3, edgecolors='none', label=name_serial_var4)
            sns.lineplot(x=x4_trend, y=y4_trend, color="g", ax=ax, linewidth=1, label=name_serial_var4)

        if num_li == 6:
            x5, y5, x5_trend, y5_trend, name_serial_var5 = (solist[5])[0], (solist[5])[1], (solist[5])[2], (solist[5])[
                3], (solist[5])[13]
            sns.scatterplot(x=x5, y=y5, c="grey", s=40, alpha=self.model.trans_picture, edgecolors='none', label=name_serial_var5)
            sns.lineplot(x=x5_trend, y=y5_trend, color="g", ax=ax, linewidth=1, label=name_serial_var5)



        ax.set_xlabel((solist[0])[5] + ' [' + (solist[0])[6] + ']')
        ax.set_ylabel((solist[0])[9] + ' [' + (solist[0])[10] + ']')

        # ax.scatter(df1.w, df1.fi,c ="blue",linewidths = 2,marker ="^", edgecolor ="red",s = 10)

        # Show the major grid and style it slightly.
        ax.grid(which='major', color='#DDDDDD', linewidth=1.2)
        # Show the minor grid as well. Style it in very light gray as a thin,
        # dotted line.
        ax.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=1)
        # Make the minor ticks and gridlines show.
        ax.minorticks_on()

        if self.model.switch_background:
            img = mpimg.imread(self.model.name_picture )
            plt.imshow(img, extent=[int(self.model.scope_down_back_entry_x_var),int(self.model.scope_up_back_entry_x_var),int(self.model.scope_down_back_entry_y_var), int(self.model.scope_up_back_entry_y_var)], aspect='auto', alpha= self.model.trans_picture)

        plt.title((solist[0])[4])
        plt.show()

    def united_chart_execution_tab_2(self):
        self.chart1(self.agg_tab_2_final)

    ################
    # print((self.agg_tab_2()[0])[0])
    # print((self.agg_tab_2()[0])[1])
    # print((self.agg_tab_2()[0])[2])`
    # print((self.agg_tab_2()[0])[3])
    #
    # print((self.agg_tab_2()[1])[0])
    # print((self.agg_tab_2()[1])[1])
    # print((self.agg_tab_2()[1])[2])
    # print((self.agg_tab_2()[1])[3])

    def save_data_clicked_tab_2(self):

        xyz = self.agg_tab_2_final
        self.z = pd.DataFrame()
        z = pd.DataFrame()
        label = None
        unit = None

        for i in (range(0, len(xyz))):
            for j in range(0, 4):
                if j == 0 :
                    label = (xyz[i])[5]
                    unit = (xyz[i])[6]
                elif j == 1:
                    label = (xyz[i])[9]
                    unit = (xyz[i])[10]
                elif j == 2:
                    label = 'linia trendu x'
                    unit = (xyz[i])[6]
                elif j == 3:
                    label = 'linia trendu y'
                    unit = (xyz[i])[10]

                w = pd.DataFrame(np.array((xyz[i])[j]).T, columns=[f'{(xyz[i])[13]}-{label}[{unit}]'])
                self.z = pd.concat([self.z, w], axis=1)
        solution = pd.DataFrame(self.z)

        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False, encoding='utf-8')

    def save_trend_clicked_tab_2(self):

        xyz = self.agg_tab_2_final
        self.z = pd.DataFrame()
        z = pd.DataFrame()

        for i in (range(0, len(xyz))):
            (xyz[i])[14] = (xyz[i])[14][::-1]
            w = pd.DataFrame(np.array((xyz[i])[14]).T, columns=[f'{(xyz[i])[13]}'])
            self.z = pd.concat([self.z, w], axis=1)
        solution = pd.DataFrame(self.z)
        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=True, encoding='utf-8')

    # def choice_btn_foto_back_tab_0(self):
    #
     # print(self.model.open_name_var.get())

    def draw_btn_foto_back_tab_0(self):
        print(self.model.name)