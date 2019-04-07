# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:48:29 2019

@author: rober
"""

import numpy as np  
from numpy.linalg import inv 
import matplotlib.pyplot as plt  
from math import pow


def get_best_param(X, y):  
    X_transpose = X.T  
    best_params = inv(X_transpose.dot(X)).dot(X_transpose).dot(y)  
    # normal equation  
    # theta_best = (X.T * X)^(-1) * X.T * y  
      
    return best_params # returns a list 




X = [[1, 2104, 5, 1, 45],
     [1, 1416, 3, 2, 40],
     [1, 1534, 3, 2, 30],
     [1, 852, 2, 1, 36],
     [1, 3000, 4, 1, 28]]


y = [[460],
     [232],
     [15],
     [178],
     [540]]

X_b = np.c_[np.ones((100, 1)), X] # set bias term to 1 for each sample  
params = get_best_param(X_b, y)  
print(params)  

