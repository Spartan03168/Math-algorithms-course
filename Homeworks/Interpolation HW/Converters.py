import numpy as np

def numpy_conversion(variable: [list, np.ndarray]):
    assert(isinstance(variable, (list, np.ndarray)))
    if type(variable) == list:
        return np.array(variable)
    elif type(variable) == np.ndarray:
        return variable

def list_conversion(variable: [list, np.ndarray]):
    assert (isinstance(variable, (list, np.ndarray)))
    if type(variable) == list:
        return variable
    elif type(variable) == np.ndarray:
        list_convert = []
        for elements in variable:
            list_convert.append(elements)
        return list_convert