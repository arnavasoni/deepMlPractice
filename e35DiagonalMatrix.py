import numpy as np

def make_diagonal(x):
	if x.ndim == 1:
		diagMat = np.zeros((len(x), len(x)))
		for idx, ele in enumerate(x):
			diagMat[idx][idx] = ele
		return diagMat
	else:
		return None