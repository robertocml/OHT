#Marzo 15 2019
import math
import os
import random
import re
import sys



#esta funcion recibe la lista y las n rotaciones
#la funcion crea dos listas, usando "slicing" y
#regresa la concatenacion de ambas listas
def rotate(l, n):
    return l[-n:] + l[:-n]



def leftRotations(numbers,size,nRotations):
	if(size == nRotations):
		return numbers
	else:
		rotations = size % nRotations
		l = rotate(numbers,rotations)
		return l




io = input();

arraySize,dLeftRotations = io.split(" ")
arraySize = int(arraySize)
dLeftRotations = int(dLeftRotations)

array = input()
numbers = [int(d) for d in re.findall(r'-?\d+', array)]

result = leftRotations(numbers,arraySize,dLeftRotations)

strResult = ' '.join(str(e) for e in result)

print(strResult)

