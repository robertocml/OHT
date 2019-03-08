import math
import os
import random
import re
import sys

arr = []
totals = []

for _ in range(6):
	arr.append(list(map(int, input().rstrip().split())))


for r in range(0,4):
	for c in range(0,4):
		if (c+2 <= len(arr)):
			upper = arr[r][c] + arr[r][c+1] + arr[r][c+2]
			middle = arr[r+1][c+1]
			lower = arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
			total = upper + middle + lower
			totals.append(total)
			#print(str(upper) + " + " + str(middle) + " + " + str(lower) + "= " + str(total))
			#print("-----------------------")

print(max(totals))


        