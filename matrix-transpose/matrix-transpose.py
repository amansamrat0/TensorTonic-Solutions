import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    rows = len(A)
    cols = len(A[0])

    ans =[]

    for i in range(cols):
        temp =[]
        for j in range(rows):
            temp.append(A[j][i])
        ans.append(temp)

    return np.array(ans)
