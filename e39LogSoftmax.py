import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    # Your code here
    A = [(x - max(scores)) for x in scores]
    B = map(lambda x: np.exp(x), A)
    sumB = sum(B)
    return [ele - np.log(sumB) for ele in A]