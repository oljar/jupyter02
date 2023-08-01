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




class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def open_data(self):



        try:
            self.model.name = self.view.open_name_var.get()
            self.model.x_var = (self.view.x_var.get())
            self.model.y_var = (self.view.y_var.get())
            self.model.x_math_form.set(self.view.x_math_form.get())
            self.model.y_math_form.set(self.view.y_math_form.get())



            self.df1 = self.model.open_data()

            print(self.df1)

        except ValueError as error:
            # show an error message
            self.view.show_error(error)




    def counter(self):


        self.x_exam_pts_basic = []
        self.y_exam_pts_basic = []



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

            deg = int(self.model.polynominal_degree.get())               # stopień wielomianu

            # trend line

            x_exam_points = ex
            y_exam_points = ey

            start = x_exam_points[0]
            stop = x_exam_points[(len(x_exam_points) - 1)]

            #  precision of sampling
            step = 0.1
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




    def natural_chart_execution(self):
        def chart(x, y, x_trend, y_trend):
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twiny()

            ax1.plot(x, y, "-o")
            ax1.plot(x_trend, y_trend, "-s")

            ax2.set_xlim(0, 100)

            plt.show()


        chart(self.x_exam_pts_basic, self.y_exam_pts_basic, self.x_trend_pts_1, self.y_trend_pts_1)






    def modified_chart_execution(self):
        def chart(x, y, x_trend, y_trend):
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twiny()

            ax1.plot(x, y, "-o")
            ax1.plot(x_trend, y_trend, "-s")

            ax2.set_xlim(0, 100)

            plt.show()

        chart(self.x_exam_pts_4, self.y_exam_pts_4, self.x_trend_pts_4, self.y_trend_pts_4)

    def save_data(self):
        solution = pd.DataFrame()
        solution[self.view.x_var.get()] = pd.DataFrame(self.x_exam_pts_4)
        solution[self.view.y_var.get()] = pd.DataFrame(self.y_exam_pts_4)
        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False)

    def save_nature_data(self):
        solution = pd.DataFrame()
        solution[self.view.x_var.get()] = pd.DataFrame(self.x_exam_pts_basic)
        solution[self.view.y_var.get()] = pd.DataFrame(self.y_exam_pts_basic)
        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False)


    def save_modify_data(self):
        solution = pd.DataFrame()
        solution[self.view.x_var.get()] = pd.DataFrame(self.x_exam_pts_4)
        solution[self.view.y_var.get()] = pd.DataFrame(self.y_exam_pts_4)
        self.view.show_save_file_clicked()

        solution.to_csv(str(self.view.save_name_var.get()), sep=';', decimal=',', index=False)









