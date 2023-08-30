import re
import tkinter as tk
from tkinter import ttk
import source

import csv
import pandas as pd
from scipy.spatial import distance
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import numpy as np
import math
from datetime import datetime




class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.temporary_chart_1_data = 0
        self.temporary_chart_2_data = 0
        self.temporary_chart_3_data = 0
        self.temporary_chart_4_data = 0
        self.temporary_chart_5_data = 0
        self.temporary_chart_6_data = 0


    def open_data(self):





            #     self.view.x_var.set(self.view.y1_var_tab1.get())
            #     self.view.y_var.set(self.view.y2_var_tab1.get())
            #
            #     self.model.x_var = (self.view.x_var.get())
            #     self.model.y_var = (self.view.y_var.get())
            #     self.df1 = pd.DataFrame()
            #     self.df1[self.model.time_var_tab1] = pd.DataFrame(self.time_modyfied_tab1_exam_pts)
            #     self.df1[self.model.y1_var_tab1] = pd.DataFrame(self.y1_modyfied_tab1_exam_pts)
            #     self.df1[self.model.y2_var_tab1] = pd.DataFrame(self.y2_modyfied_tab1_exam_pts)
            #
            #     print(self.df1)
            #






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


        self.y_exam_pts = [ eval(cor_factor_y) for y in self.y_exam_pts]





        print (self.y_exam_pts)

        # c = 41.1  # reducer constns
        #
        # self.x_exam_pts = [(c * math.sqrt(x)) for x in x_points]




        def scope_limit(self):

            self.model.limit_down_scope.set(self.view.total_down_scope_var.get())
            self.model.limit_up_scope.set(self.view.total_up_scope_var.get())

            lim_a = float(self.model.limit_down_scope.get())
            lim_b = float(self.model.limit_up_scope.get())


            lim_down = int(len(self.x_exam_pts ) * (lim_a / 100))
            lim_up = int(len(self.x_exam_pts ) * (lim_b / 100))


            x_slice, y_slice = self.x_exam_pts[lim_down:lim_up], self.y_exam_pts[lim_down:lim_up]

            #
            # print (f'gora {x_slice}')
            # print(f'dol {y_slice}')



            return x_slice,y_slice








        def main_proces(ex, ey, dist_border = 10000):



            # input filters


            self.model.polynominal_degree.set(self.view.polynominal_degree.get())

            self.model.step.set(self.view.step.get())

            deg = int(self.model.polynominal_degree.get())               # stopień wielomianu

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
            coefs = poly.polyfit(x_exam_points, y_exam_points, deg)

            y_trend_points = poly.polyval(x_trend_points, coefs)

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
            print(f'współcznimmiki lini trendu {coefs}')

            # distance border
            filtred = sol_exam[sol_exam['dist'] < dist_border]

            density = len(x_exam_points) / (x_exam_points[(len(x_exam_points) - 1)] - x_exam_points[0])

            x_output = filtred['X_Exam'].tolist()
            y_output = filtred['Y_Exam'].tolist()
            return x_output, y_output, x_trend_points, y_trend_points

        def density_control(x, y, density=1):

            n = int(1 / density)

            x_set = (x[::n])
            y_set = (y[::n])

            return x_set, y_set






        print(f'SCOPE x {scope_limit(self)[0]}')
        print(f'SCOPE y {scope_limit(self)[1]}')





        self.x_exam_pts_basic= scope_limit(self)[0]
        self.y_exam_pts_basic = scope_limit(self)[1]




        try:
            self.model.dist_border = int(self.view.dist_border_var.get())
            dist_fact = self.model.dist_border
        except:
            dist_fact = 10000



        x_exam_pts_2, y_exam_pts_2, self.x_trend_pts_1, self.y_trend_pts_1 = main_proces(self.x_exam_pts_basic, self.y_exam_pts_basic,dist_fact)

        #

        x_exam_pts_3, y_exam_pts_3, self.x_trend_pts_1, self.y_trend_pts_1 = main_proces(x_exam_pts_2, y_exam_pts_2)

        #chart(x_exam_pts_3, y_exam_pts_3, x_trend_pts_1, y_trend_pts_1, x_exam_pts_2)

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

        self.x_exam_pts_4, self.y_exam_pts_4, self.x_trend_pts_4, self.y_trend_pts_4 = main_proces(x_exam_pts_3, y_exam_pts_3)




    def natural_chart_execution_tab_0(self):
        def chart(x, y, x_trend, y_trend):
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twiny()

            ax1.plot(x, y, "-o")
            ax1.plot(x_trend, y_trend, "-s")

            ax2.set_xlim(0, 100)

            plt.show()

        chart(self.x_exam_pts_basic, self.y_exam_pts_basic, self.x_trend_pts_1, self.y_trend_pts_1)

    def modyfied_chart_execution_tab_0(self):
        def chart(x, y, x_trend, y_trend):
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twiny()

            ax1.plot(x, y, "-o")
            ax1.plot(x_trend, y_trend, "-s")

            ax2.set_xlim(0, 100)

            plt.show()

        chart(self.x_exam_pts_4, self.y_exam_pts_4, self.x_trend_pts_4, self.y_trend_pts_4)




    def export_nature_data_tab_0(self):

        self.model.name_of_chart_var = self.view.name_of_chart_var.get()

        self.model.name_of_X_axis_var = self.view.name_of_X_axis_var.get()
        self.model.unit_of_X_axis_var = self.view.unit_of_X_axis_var.get()
        self.model.scope_min_of_X_axis_var = self.view.scope_min_of_X_axis_var.get()
        self.model.scope_max_of_X_axis_var = self.view.scope_max_of_X_axis_var.get

        self.model.name_of_Y_axis_var = self.view.name_of_Y_axis_var.get()
        self.model.unit_of_Y_axis_var = self.view.unit_of_Y_axis_var.get()
        self.model.scope_min_of_Y_axis_var = self.view.scope_min_of_Y_axis_var.get()
        self.model.scope_max_of_Y_axis_var = self.view.scope_max_of_Y_axis_var.get()
        self.model.name_serial_var = self.view.name_serial_var.get()

        return(self.x_exam_pts_basic, self.y_exam_pts_basic, self.x_trend_pts_1, self.y_trend_pts_1,
               self.model.name_of_chart_var,
               self.model.name_of_X_axis_var,self.model.unit_of_X_axis_var,
               self.model.scope_min_of_X_axis_var,self.model.scope_max_of_X_axis_var,
               self.model.name_of_Y_axis_var, self.model.unit_of_Y_axis_var,
               self.model.scope_min_of_Y_axis_var, self.model.scope_max_of_Y_axis_var,
               self.model.name_serial_var)





    def save_nature_data_tab_0(self):
        solution = pd.DataFrame()
        solution[self.view.x_var.get()] = pd.DataFrame(self.x_exam_pts_basic)
        solution[self.view.y_var.get()] = pd.DataFrame(self.y_exam_pts_basic)
        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False)


    def save_modify_data_tab_0(self):
        solution = pd.DataFrame()
        solution[self.view.x_var.get()] = pd.DataFrame(self.x_exam_pts_4)
        solution[self.view.y_var.get()] = pd.DataFrame(self.y_exam_pts_4)
        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False)



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

        return(self.x_exam_pts_4, self.y_exam_pts_4, self.x_trend_pts_4, self.y_trend_pts_4,
                self.model.name_of_chart_var,
                self.model.name_of_X_axis_var, self.model.unit_of_X_axis_var,
                self.model.scope_min_of_X_axis_var, self.model.scope_max_of_X_axis_var,
                self.model.name_of_Y_axis_var, self.model.unit_of_Y_axis_var,
                self.model.scope_min_of_Y_axis_var, self.model.scope_max_of_Y_axis_var,
                self.model.name_serial_var)



        ######################################################################################################################
#tab_1
######################################################################################################################

    def open_data_tab_1(self):



        self.model.name = self.view.open_name_var.get()
        self.model.time_var_tab1 =  self.view.time_var_tab1.get()
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




    def draw_data_tab_1(self):

        def chart(x, y1, y2):
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twiny()

            ax1.plot(x, y1, "-o")
            ax1.plot(x, y2, "-s")

            ax2.set_xlim(0, 100)
            plt.gcf().autofmt_xdate()
            ax1.set_xticks(np.arange(-5, 200, 10))
            plt.show()

        chart(self.time_tab1_exam_pts, self.y1_tab1_exam_pts , self.y2_tab1_exam_pts)



    def set_data_tab_1(self):
        #self.model.down_scope_var_tab_1 = datetime.strptime(str(self.view.down_scope_var_tab_1.get()),"%H:%M:%S").time()
        #self.model.up_scope_var_tab_1 = datetime.strptime(str(self.view.up_scope_var_tab_1.get()),"%H:%M:%S").time()

        self.model.down_scope_var_tab_1 = str(self.view.down_scope_var_tab_1.get())
        self.model.up_scope_var_tab_1 = str(self.view.up_scope_var_tab_1.get())


        df101 = pd.DataFrame(self.model.open_data_tab_1())
        df101 = df101.loc[:,[self.model.time_var_tab1,self.model.y1_var_tab1,self.model.y2_var_tab1]]

        df101 = df101[(df101[self.model.time_var_tab1] > (self.model.down_scope_var_tab_1)) & (df101[self.model.time_var_tab1] < self.model.up_scope_var_tab_1)]

        #df101 = df101[df101[self.model.time_var_tab1].between_time(self.model.down_scope_var_tab_1, self.model.up_scope_var_tab_1)]
        #
        self.time_modyfied_tab1_exam_pts = (df101[self.model.time_var_tab1]).tolist()
        self.y1_modyfied_tab1_exam_pts = (df101[self.model.y1_var_tab1]).tolist()
        self.y2_modyfied_tab1_exam_pts = (df101[self.model.y2_var_tab1]).tolist()
        #




    def draw_slice_data_tab_1(self):

        def chart(x, y1, y2):
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twiny()

            ax1.plot(x, y1, "-o")
            ax1.plot(x, y2, "-s")

            ax2.set_xlim(0, 100)
            plt.gcf().autofmt_xdate()
            ax1.set_xticks(np.arange(-5, 200, 10))
            plt.show()

        chart( self.time_modyfied_tab1_exam_pts ,  self.y1_modyfied_tab1_exam_pts, self.y2_modyfied_tab1_exam_pts)
        self.export_to_tab_0()

    def save_modyfied_data_clicked_tab_1(self):
        solution = pd.DataFrame()
        solution[self.model.time_var_tab1] = pd.DataFrame(self.time_modyfied_tab1_exam_pts)
        solution[self.model.y1_var_tab1] = pd.DataFrame(self.y1_modyfied_tab1_exam_pts)
        solution[self.model.y2_var_tab1] = pd.DataFrame(self.y2_modyfied_tab1_exam_pts)

        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False)




#########################################################################################################################
#tab2
########################################################################################################################
    def trans_01_tab_2(self):
        self.temporary_chart_1_data = self.export_nature_data_tab_0()
        if self.view.switch_modyfied_export == True:
            self.temporary_chart_1_data = self.export_modyfied_data_tab_0()
            # print(len(self.temporary_chart_1_data[0]))
            # print(len(self.temporary_chart_1_data[1]))
            # print(len(self.temporary_chart_1_data[2]))
            # print(len(self.temporary_chart_1_data[3]))



    def trans_02_tab_2(self):
        self.temporary_chart_2_data = self.export_nature_data_tab_0()
        if self.view.switch_modyfied_export == True:
            self.temporary_chart_2_data = self.export_modyfied_data_tab_0()
            # print(len(self.temporary_chart_2_data[0]))
            # print(len(self.temporary_chart_2_data[1]))
            # print(len(self.temporary_chart_2_data[2]))
            # print(len(self.temporary_chart_2_data[3]))




    def agg_tab_2(self):
        agg = []
        if self.temporary_chart_1_data != 0 :
            agg.append(self.temporary_chart_1_data)
        if self.temporary_chart_2_data != 0:
            agg.append(self.temporary_chart_2_data)


        return agg




    def united_chart_execution_tab_2(self):
        print(f'długość{len(self.agg_tab_2())}')
        print((self.agg_tab_2()[0])[13])

        print((self.agg_tab_2()[1])[13])

        def chart(x, y, x_trend, y_trend,x1,y1,x1_trend,y1_trend):
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            #ax2 = ax1.twiny()

            ax1.plot(x, y, "-o")
            ax1.plot(x_trend, y_trend, "-s")

            ax1.plot(x1, y1, "-o")
            ax1.plot(x1_trend, y1_trend, "-s")

            #ax2.set_xlim(0, 100)

            plt.show()

        chart((self.agg_tab_2()[0])[0],(self.agg_tab_2()[0])[1],(self.agg_tab_2()[0])[2],(self.agg_tab_2()[0])[3],
              (self.agg_tab_2()[1])[0],(self.agg_tab_2()[1])[1],(self.agg_tab_2()[1])[2],(self.agg_tab_2()[1])[3])




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
        solution = pd.DataFrame()

        # solution[str((self.agg_tab_2()[0])[5])] = pd.DataFrame(((self.agg_tab_2()[0])[0]))
        solution['x1'] = pd.DataFrame(((self.agg_tab_2()[0])[0]))
        # solution[str((self.agg_tab_2()[0])[9])] = pd.DataFrame(((self.agg_tab_2()[0])[1]))
        solution['y1'] = pd.DataFrame(((self.agg_tab_2()[0])[1]))
        # solution[str((self.agg_tab_2()[1])[5])] = pd.DataFrame((self.agg_tab_2()[1])[0])
        solution['x2'] = pd.DataFrame((self.agg_tab_2()[1])[0])
        #solution[str((self.agg_tab_2()[1])[9])] = pd.DataFrame((self.agg_tab_2()[1])[1])
        solution['y2'] = pd.DataFrame((self.agg_tab_2()[1])[1])

        print(solution)





        #
        # solution[self.model.y1_var_tab1] = (self.agg_tab_2()[0])[0]
        #
        # solution[self.model.y2_var_tab1] = (self.agg_tab_2()[0])[1]


        # solution = pd.DataFrame(list(self.agg_tab_2()))

        # print((self.agg_tab_2()[0])[0])
        # print((self.agg_tab_2()[0])[1])



        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False)