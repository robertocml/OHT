# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:54:13 2019

@author: Roberto 
"""

import math
import numpy as np


#Ejercicio 1------------------------------------------
test = "Hello World"
print ("Hello world \n" + test)

#Ejercicio 2------------------------------------------
def sigmoid(x):
    s =  1 / (1 + math.exp(-x))
    
    return s

print("Ejercicio 2 print ----------------->" + str(sigmoid(3)))


#Ejercicio 3------------------------------------------
x = [1,2,3]
print("Ejercicio 3" + str(np.exp(x)))

#print(sigmoid(x))

#-------
x = np.array([1,2,3])
x = np.array([1,2,3])
print(x + 3)
#---

#Ejercicio 4-----------------------------------------
print("\nEjercicico 4 con Numpy")

x = np.array([1,2,3])
print(np.exp(x))
x = np.array([1,2,3])
print(x + 3)

#Ejercicio 5 -----------------------------------------

print("Ejercicio 5 : Sigmoid")


#Ejercicio derivada sigmoid------------------------------------------
def sigmoid(x):
    s =  1 / (1 + math.exp(-x))
    ds = s*(1-s)
    
    return ds
x = np.array([1,2,3])
print (sigmoid(x))

## Reshape
#v = v.reshape(v.shape[0]*v.shape[1], v.shape[2])


def imageTovector(image):
    v = image.reshape(v.shape[0]*v.shape[1]*v.shape[2],1)
    
    return v

image = "aqui va la matriz" 

print(str(imageTovector(image)))

#Ejercicio 8 normalizacion
def normalizeRows():
    x_norm = np.linalg.norm(x,axis=1,keepdims = true)
    x = 
    return x


#Ejercicio 9 softmax
def softMax():
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis = 1,)
    s = "divides el exponencial entre la sumatoria de todos np.sum"
    return s

x = np.array([9,2,5,0,0],[7,5,0,0,0])
print("softMax(x)" + str(softMax(x)))
    

#Ejercicio 10 - vectorizacion

def L1(yhat,y):
    loss = ""
    return loss

    
yhat = np.array([9,2,5,0,0],[7,5,0,0,0])
    
    
