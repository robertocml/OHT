# -*- coding: utf-8 -*-

import numpy as np  
from numpy.linalg import inv 
import matplotlib.pyplot as plt  
  
def generate_data():  
    X = 2 * np.random.rand(100, 1)  
    y = 4 + 3 * X + np.random.randn(100, 1)  
      
    # y = 4 + 3X + Gaussian noise  
    # theta_0 or Bias Term = 4   
    # theta_1 = 3  
      
    return X, y 

'''
Extra - Noiseless Data 
def generate_noiseless_data():  
    X = 2 * np.random.rand(100, 1)  
    y = 4 + 3 * X  
          
        # y = 4 + 3X  
        # theta_0 or Bias Term = 4   
        # theta_1 = 3  
          
    return X, y  
X, y = generate_noiseless_data()  
plt.plot(X, y, "r.") 

'''


def get_best_param(X, y):  
    X_transpose = X.T  
    best_params = inv(X_transpose.dot(X)).dot(X_transpose).dot(y)  
    # normal equation  
    # theta_best = (X.T * X)^(-1) * X.T * y  
      
    return best_params # returns a list 



X, y = generate_data()  
plt.plot(X, y, "r.") 

X_b = np.c_[np.ones((100, 1)), X] # set bias term to 1 for each sample  
params = get_best_param(X_b, y)  
print(params)  

    
# test prediction  

test_X = np.array([[0], [2]])  
test_X_b = np.c_[np.ones((2, 1)), test_X]  
      
prediction = test_X_b.dot(params)  
      
    # y = h_Theta_X(Theta) = Theta.T * X  
print(prediction)  
    
plt.plot(test_X, prediction, "r--")  
plt.plot(X, y, "b.")  
plt.axis([0, 2, 0, 15]) # x axis range 0 to 2, y axis range 0 to 15  
plt.show() 


'''
For Noiseless Data
X_b = np.c_[np.ones((100, 1)), X] # set bias term to 1 for each sample  
param = get_best_param(X_b, y)  
test_X = np.array([[0], [2]])  
test_X_b = np.c_[np.ones((2, 1)), test_X]  
      
prediction = test_X_b.dot(params)  
plt.plot(test_X, prediction, "r--")  
plt.plot(X, y, "b.")  
plt.axis([0, 2, 0, 15]) # x axis range 0 to 2, y axis range 0 to 15  
plt.show() 
'''

