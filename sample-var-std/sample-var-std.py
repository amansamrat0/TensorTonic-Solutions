import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    varience =float (np.var(x , ddof=1))
    sd = float(np.sqrt(varience))

    return {
        "variance" : varience,
        "standard_deviation":sd
    }