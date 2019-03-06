#Solucion al problema de Counting Valleys

import math
import os
import random
import re
import sys

def countValleys(array):
	#"seaLevel" es para saber cuando es un valley y "valleys" es para
	#mantener registro de cuantos valleys hay en total
	seaLevel = 0
	valleys = 0

	#El for simplemente analiza los 3 casos posibles y decrementa/incrementa
	#el sealevel y valleys
	for i in array:
		if ( i == -1 and seaLevel == 0):
			#print("a")
			valleys = valleys + 1
			seaLevel = seaLevel - 1
		elif ( i == -1 and seaLevel != 0):#
			#print("b")
			seaLevel = seaLevel - 1
		else:
			#print("c")
			seaLevel = seaLevel + 1

		#print(str(i) + ", seaLevel: " + str(seaLevel) + " valleys: " + str(valleys))

	return valleys

#Lectura de los inputs
l = int(input()) 
strHills = input()

#Convierto las U en str 1 y las D en str -1
strHills = strHills.replace("U", "1 ")
strHills = strHills.replace("D", "-1 ")

#Convierto el string que contiene los 1 y -1 a un array para poder manipuralos como ints
numbers = [int(d) for d in re.findall(r'-?\d+', strHills)]

#Resultado
print(str(countValleys(numbers)))

