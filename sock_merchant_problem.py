from collections import Counter


def searchPairs(array):
	instances = 0
	d = Counter(array)
	for key, value in d.items():
		instances = instances + d[key] // 2
		
	
	return instances

n = int(input()) 
num = input() 

numbers = [int(s) for s in num.split() if s.isdigit()]


print(searchPairs(numbers))