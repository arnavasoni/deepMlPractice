def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	'''covariance matrix sued to understand the relationship between multiple variables in a dataset.
	quantifies the degree to which the vairables change together.
	+ve covraince means they're directly proportional
	-ve covariance means they're inversely proportional
	'''

	'''
	calculation: cov(X,Y) = sum[(xI - xMean) * (yI - yMean)]/(no. of observations - 1) 
	'''
	n = len(vectors) # number of features
	m = len(vectors[0]) # number of observations

	# list to store the feature means
	nMeans = []
	# to populate nMeans
	for feature in vectors:
		fMean = sum(feature)/len(feature)
		nMeans.append(fMean)
	
	covMat = [[0 for _ in range(n)] for _ in range(n)]

	for i in range(n): # for each feature
		for j in range(i, n):
			cov = sum((vectors[i][k] - nMeans[i]) * (vectors[j][k] - nMeans[j]) for k in range(m)) / (m-1)
            # remember, that k comes in handy because one column contains values of the respective feature for that particular observation

			covMat[i][j] = covMat[j][i] = cov

	return covMat