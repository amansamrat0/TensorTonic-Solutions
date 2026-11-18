import numpy as np

def magnitude(a: list) -> float:
    n = len(a)
    sum = 0
    for i in range(n):
        sum += a[i]**2

    return (np.sqrt(sum))
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dot_product = np.dot(a , b)

    mag_a = magnitude(a);
    mag_b = magnitude(b);

    if(mag_a == 0 or mag_b==0):
        return float(0)
    
    
    return float(dot_product/ (mag_a * mag_b))