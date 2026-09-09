import math

def sigmoid(z: float) -> float:
	#Your code here
	den = 1 + math.exp(-z)

	if den != 0:
		result = 1/den
	return round(result, 4)