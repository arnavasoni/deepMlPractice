import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities = []

	features = np.array(features)
	weights= np.array(weights)
	labels = np.array(labels)
	z = 0
	for featureVector in features:
		z = (weights @ featureVector) + bias
		prob = 1 / (1 + math.exp(-z))
		probabilities.append(round(prob, 4))

	mse = sum((prob - label) ** 2 for prob, label in zip(probabilities, labels)) / len(labels)
	mse = round(mse, 4)
	return probabilities, mse

print(single_neuron_model([[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], [0, 1, 0], [0.7, -0.4], -0.1))