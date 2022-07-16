import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class LinearRegression:
    def __init__(self,X ,Y):
        self.X = X
        self.Y = Y
        pass
    def m(self):
        FinalData = pd.DataFrame()
        FinalData['X'] = self.X
        FinalData['Y'] = self.Y
        sum_x = FinalData['X'].sum()
        sum_y = FinalData['Y'].sum()
        sum_xy = (FinalData['X']*FinalData['Y']).sum()
        sum_xsqr = (FinalData['X']**2).sum()
        sum_x_sqr = sum_x**2
        n = len(FinalData)
        m = ((n*(sum_xy))-(sum_x*sum_y)) / ((n*sum_xsqr)-(sum_x_sqr))
        print(m)
        pass
    def c(self):
        c = (sum_y - (m*sum_x))/ n
        print(c)
    def y(self):
        y = [(m*X)+c for X in FinalData['X']]
        print(y)
    def visualize(self):
        plt.plot(FinalData['X'],FinalData['Y'])
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.title("LinearRegression Plot")
        plt.show()
        
obj = LinearRegression([1,2,3,4,5,6,7],[1.5,3.8,6.7,9.0,11.2,13.6,16])
obj.m()
obj.c()
obj.y()
obj.visualize()