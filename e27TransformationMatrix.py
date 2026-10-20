import numpy as np

'''
to get to matrix B using the matrix C, you would need to multiply C by P.
to find matrix P: P = C^(-1) * B AKA C_inverse * B
'''
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	# Convert the lists to arrays
	C = np.array(C)
	B = np.array(B)

	# Find the inverse matrix of the desired basis
	C_inv = np.linalg.inv(C)

	# Dot product of inverse matrix & converting matrix
	P = np.matmul(C_inv, B)
	return np.round(P, 5)

# example
B = [[1, 0, 0], 
	[0, 1, 0], 
	[0, 0, 1]]

C = [[1, 2.3, 3], 
	[4.4, 25, 6], 
	[7.4, 8, 9]]

print(transform_basis(B,C))