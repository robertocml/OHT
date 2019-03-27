def reverseArray(a,l):
	#inicializacion de apuntadores
	left = 0
	right = l -1

	while left<right:
		#se hace el swapping
		temp = a[left]
		a[left] = a[right]
		a[right] = temp

		#Se actualizan los apuntadores (Incremento para el left pointer y aumento para el right pointer)
		left += 1
		right -= 1

	return a

#se lee la longitud del array
l = int(input()) 
array = []

#Se recibe el array
for i in range(0,l):
	x = int(input())
	array.append(x)

#Se guarda la lista inversa en r 
r = reverseArray(array,l)

#El * en el print es para que imprima la lista como string separado por un espacio
# si quisieras, por ejemplo separar la lista con "," usarias el argumento sep. Ejemplo print(*L, sep=', ')
print(*r)
	
