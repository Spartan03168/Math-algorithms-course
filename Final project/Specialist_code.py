import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def x_y_charter(x_label: str, y_label: str, title: str, x_axis_data: [list, np.ndarray],
                y_axis_data: [list, np.ndarray], developer_mode: int):
    assert(type(x_label) == str and len(x_label) > 0)
    assert(type(y_label) == str and len(y_label) > 0)
    assert(type(title) == str and len(title) > 0)
    assert(isinstance(x_axis_data, (list, np.ndarray)))
    assert(isinstance(y_axis_data, (list, np.ndarray)))
    assert(type(developer_mode) == int)

    plt.scatter(x_axis_data, y_axis_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f"{y_label.capitalize()} VS {x_label.capitalize()}")
    plt.savefig(f"{y_label} VS {x_label}.png")
    plt.close()


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