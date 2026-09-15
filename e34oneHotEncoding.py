import numpy as np

def to_categorical(x, n_col=None):
	labels = np.unique(x).tolist() # gives the number of unique labels available.
	if n_col:
		labels = [i for i in range(n_col)]
	res = np.zeros((x.shape[0], len(labels))) # no. of rows = no. of observations; no. of cols = no. of unique labels
	for i in range(x.shape[0]):
		res[i][x[i]] = 1
	return res
