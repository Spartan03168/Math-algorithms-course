import numpy as np
import pandas as pd


def numpy_conversion(variable: [list, np.ndarray, pd.Series]):
    assert(isinstance(variable, (list, np.ndarray, pd.Series))), f"Type: {type(variable)}"
    if type(variable) == list:
        return np.array(variable)
    elif type(variable) == pd.Series:
        return np.array(variable.tolist())
    elif type(variable) == np.ndarray:
        return variable

def list_conversion(variable: [list, np.ndarray, pd.Series]):
    assert (isinstance(variable, (list, np.ndarray, pd.Series)))
    if type(variable) == list:
        return variable
    elif type(variable) == pd.Series:
        return variable.tolist()
    elif type(variable) == np.ndarray:
        list_overwrite = []
        for elements in variable:
            list_overwrite.append(elements)
        del variable
        return list_overwrite