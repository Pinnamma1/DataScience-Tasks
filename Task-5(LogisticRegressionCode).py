import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class LogisticRegression:
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
        print(f'Slope(m) = {m}')
        pass
    def b(self):
        b = (sum_y - (m*sum_x))/ n
        print(f'b = {b}')
        pass
    def y(self):
        y = [(m*X)+c for X in FinalData['X']]
        print(f'y = {y}')
        pass
    def b_s(self):
        b_s = [1/(1+np.exp(-ys)) for ys in y]
        print( f'b_s = {b_s}')
    def final_output(self):
        final_output = [1 if bs>=0.5 else 0 for bs in b_s]
        print(f'Final Output of Predicted y values = {final_output}')
    def Accuracy(self):
        correct = 0
        for pred, org in zip(final_output, FinalData['Y']):
            if pred == org:
                correct += 1
            else:
                pass
        Accuracy = correct / len(FinalData)
        print(f'Accuracy = {Accuracy}')
    def visualize(self):
        plt.plot(FinalData['X'],FinalData['Y'])
        plt.xlabel('Input Values')
        plt.ylabel('Output Values')
        plt.title("Logistic Regression Plot")
        plt.show()
        
obj = LogisticRegression([0.1,0.2,0.12,0.32,0.5,0.7,0.67],[0,0,0,0,1,1,1])
obj.m()
obj.b()
obj.y()
obj.b_s()
obj.final_output()
obj.Accuracy()
obj.visualize()