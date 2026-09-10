import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    maxz = max(scores)
    den = 0
    for j in scores:
        den += math.exp(j - maxz)
    results = []
    for i in scores:
        prob = math.exp(i - maxz) / den
        results.append(prob)
    return results