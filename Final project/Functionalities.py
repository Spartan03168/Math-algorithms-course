import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def linear_regression_projector(data_injection: [list, np.ndarray], developer_mode: int):
    assert(isinstance(data_injection, (list, np.ndarray)))
    assert(type(developer_mode) == int)