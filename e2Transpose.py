# Transpose a matrix: nxm should become mxn

def transposeMatrix(a: list[list[int|float]]) -> list[list[int|float]]:
	return [col for col in zip(*a)]