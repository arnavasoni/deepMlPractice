# # Matrix times Vector

def matrixDotVector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[1]) != len(b):
		return -1
	else:
		result = []
		for row in a:
			temp = 0
			for i in range(len(row)):
				temp += row[i]*b[i]
			result.append(temp)
		return result

# sample
print(matrixDotVector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))