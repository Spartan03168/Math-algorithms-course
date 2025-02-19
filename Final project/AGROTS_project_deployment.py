import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import datetime

# - Behaviour modifiers -
developer_mode = 1
# -----------------------
file_path = "AGROTSDatasetFinal.csv"
if file_path == 0:
    raise LookupError("File path cannot be found as the field is empty")
source_dataframe = pd.read_csv(fr"{file_path}")
if developer_mode == 1:
    print("Dataframe info:")
    print(source_dataframe.info())