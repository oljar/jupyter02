import csv
import pandas as pd
from scipy.spatial import distance
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import numpy as np
import math
import random


############################################################


# examinated points

x_tag = 'M51: Pa'

y_tag ='M53: Pa'


df1 = pd.read_csv("data_3.csv",sep=';', decimal=',')
df1 = df1.sort_values(by=x_tag, ascending=True)

df1 = df1[df1[x_tag]>= 0]
df1 = df1[df1[y_tag]>= 0]

df1[x_tag] = df1[x_tag].fillna(df1[x_tag].median())
df1[y_tag] = df1[y_tag].fillna(df1[y_tag].median())

x_points = (df1[x_tag]).tolist()  # definition of columns -x
c=41.1 # reducer constns

x_exam_pts = [(c * math.sqrt(x) )for x in x_points]

y_exam_pts = (df1[y_tag]).tolist() # definition of columns -y



def density_show (ex):

    density = len(ex)/(ex[(len(ex)-1)]-ex[0])

    return density




def main_proces(ex,ey,dist_border=10000000):

    # input filters

    deg = 2

    # trend line


    x_exam_points = ex
    y_exam_points = ey



    start = x_exam_points[0]
    stop = x_exam_points[(len(x_exam_points)-1)]

    #  precision of sampling
    step = 0.1
    sequence = list(np.arange (start, stop, step))
    x_trend_points = sequence


    # coefficients od polynomial 2-grade (trend)
    coefs = poly.polyfit(x_exam_points, y_exam_points, deg)


    y_trend_points = poly.polyval(x_trend_points, coefs)


    def distance_point_to_curve(x0, y0, x_curve, y_curve):
        distances = np.sqrt((x0 - x_curve)**2 + (y0 - y_curve)**2)
        #min_distance = np.min(distances)
        return distances



    def main_iteration(x1,y1,x,y):
        dist_all=[]
        for i in range(len(x)):
            dist_sum = []
            x0=x[i]
            y0=y[i]
            for j in range (len(x1)):
                a = (distance_point_to_curve(x0,y0,x1[j],y1[j]))
                dist_sum.append(a)
            min_distance = min(dist_sum)
            dist_all.append(min_distance)
        return dist_all




    sol_dist_pd = pd.DataFrame(main_iteration(x_trend_points,y_trend_points,x_exam_points,y_exam_points))

    # print(f'd {sol_dist_pd}')
    # print(f'X {x_exam_points}')
    # print(f'Y {y_exam_points}')

    sol_exam=pd.DataFrame()
    sol_exam['dist'] = sol_dist_pd
    sol_exam['X_Exam'] =  x_exam_points
    sol_exam['Y_Exam'] = y_exam_points

    #print('examinated points with distance')
  #  print(sol_exam)


    sol_trend=pd.DataFrame()
    sol_trend['X_Trend'] = pd.DataFrame(x_trend_points)
    sol_trend['Y_Trend']  = pd.DataFrame(y_trend_points)


    #print(sol_trend)

    print('y trend')
    print (f'Krzywa - y = {coefs[2]}x^2 + {coefs[1]}x + {coefs[0]}' )

    # distance border
    filtred = sol_exam[sol_exam['dist'] < dist_border]

    density = len(x_exam_points)/(x_exam_points[(len(x_exam_points)-1)]-x_exam_points[0])




    x_output = filtred['X_Exam'].tolist()
    y_output = filtred['Y_Exam'].tolist()
    return x_output,y_output,x_trend_points,y_trend_points



def density_control(x,y,density):

    n = int(1/density)

    x_set = (x[::n])
    y_set = (y[::n])

    return x_set,y_set


def chart(x,y,x_trend,y_trend,x_previous):


    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny()

    ax1.plot(x, y, "-o")
    ax1.plot(x_trend, y_trend, "-s")



    ax2.set_xlim(0, 100)


    plt.show()



# Here set distance



dist_border = 100



x_exam_pts_2, y_exam_pts_2,x_trend_pts_1,y_trend_pts_1 = main_proces(x_exam_pts,y_exam_pts,dist_border)


#
x_exam_pts_3, y_exam_pts_3,x_trend_pts_1,y_trend_pts_1 = main_proces(x_exam_pts_2,y_exam_pts_2)









chart(x_exam_pts_3,y_exam_pts_3,x_trend_pts_1,y_trend_pts_1,x_exam_pts_2)


#hier set % scope of slice

down_procent= 30
up_procent = 100




down = int(len(x_exam_pts_3)*(down_procent/100))
up = int(len(x_exam_pts_3)*(up_procent/100))



x_slice, y_slice = x_exam_pts_3[down:up],y_exam_pts_3[down:up]



#  Here set density of slice
density_factor = 0.02

x_slice_1, y_slice_1 = density_control(x_slice,y_slice,density_factor)

# change data  with corrected density in described scope - down/up






x_exam_pts_3[down:up:1],y_exam_pts_3[down:up:1]= x_slice_1[::1],y_slice_1[::1]




x_exam_pts_4, y_exam_pts_4,x_trend_pts_4,y_trend_pts_4 = main_proces(x_exam_pts_3,y_exam_pts_3)



chart(x_exam_pts_4,y_exam_pts_4,x_trend_pts_4,y_trend_pts_4,x_exam_pts)


