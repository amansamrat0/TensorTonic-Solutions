import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    n = len(x)

    prosum =0

    for i in range(n):
        prosum += x[i]*p[i]

    return float(prosum)
    pass