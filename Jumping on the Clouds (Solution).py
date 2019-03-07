import re
import sys

#Solucion
def check(x):
	global intClouds
	global l

	if (x+1 < len(intClouds) and x+2 < len(intClouds)):
		if(intClouds[x] == 0):
			if(intClouds[x+1] == 0 and intClouds[x+2] == 0): 
				intClouds.pop(x+1)

#Vars
n = int(input())
clouds = input()
i=0

#Convierto el string que contiene los 0 y 1 a un array para poder manipuralos como ints
intClouds = [int(d) for d in re.findall(r'-?\d+', clouds)]

l = len(intClouds)

while(i < l):
	check(i)
	l = len(intClouds)
	i = i+1

check1 = [x for x in intClouds if x != 1]

#if para revisar que que se cumplen las restricciones
if (n < 2 or n > 100) :
	sys.exit()
else:
	result = len(check1) - 1
	print(str(result))