import sys

#El string del cual se obtendran el numero de 'a's repetidas
s = input() 
# el tamaño del string infinito
n = int(input())


#if para revisar que que se cumplen las restricciones
if (n < 1 or n > n**12 or len(s) < 1  or len(s) > 100):
	sys.exit()
else:
	ocurrences = s.count('a')
	fullS = n // len(s)
	module = n % len(s)

	#simplemente se regresa el num de ocurrencias de "a" del string original
	#por las N veces que cupo dentro de s, a esto se le suma las
	#ocurrencias del substring que completa el tamaño "n" del input
	result = (ocurrences * fullS) + (s[:module].count('a'))


print(result)