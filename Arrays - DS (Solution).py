

def reverseArray(a,l):
	#inicializacion de apuntadores
	left = 0
	right = l -1
	print("riight "+ str(right))

	while left<right:
		#se hace el swapping
		temp = a[left]
		a[left] = a[right]
		a[right] = temp

		#Se actualizan los apuntadores
		left += 1
		right += 1

	return a
#se lee la longitud del array
l = int(input()) 
array = []
#Se recibe el array
for i in range(0,l):
	x = int(input())
	array.append(x)


print(reverseArray(array,l))
	