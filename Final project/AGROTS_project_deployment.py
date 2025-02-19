import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from Functionalities import linear_regression_projector

# - Behaviour modifiers -
developer_mode = 1
# -----------------------
project_start = datetime.datetime.now()

file_path = "AGROTSDatasetFinal.csv"
if file_path == 0:
    raise LookupError("File path cannot be found as the field is empty")
source_dataframe = pd.read_csv(fr"{file_path}")
if developer_mode == 1:
    print("Dataframe info:")
    print(source_dataframe.info())
    print()

# - Prep work -
time_stamps = source_dataframe["Timestamp"].to_numpy()
air_pressure_data = source_dataframe["AirPressure"].to_numpy()
air_temperature_A = source_dataframe["AirTemperatureA"].to_numpy()
air_temperature_B = source_dataframe["AirTemperatureB"].to_numpy()
air_humidity = source_dataframe["AirHumidity"].to_numpy()

air_temp_A_processing_df = pd.DataFrame({
    "Time stamps": time_stamps,
    "Air pressure": air_pressure_data,
    "Air temperature A": air_temperature_A
    })

air_temp_B_processing_df = pd.DataFrame({
    "Time stamps": time_stamps,
    "Air pressure": air_pressure_data,
    "Air temperature B": air_temperature_B
    })

air_humidity_processing_df = pd.DataFrame({
    "Time stamps": time_stamps,
    "Air pressure": air_pressure_data,
    "Air humidity": air_humidity
    })

# ----> Deployment <----
# - Air temperature A -
air_temp_A_forecast, air_temp_A_mae, air_temp_A_mse, air_temp_A_r2, air_temp_A_exec_time = linear_regression_projector(air_temp_A_processing_df["Air temperature A"].to_numpy(),air_temp_A_processing_df,
                                                                                                                       "Air temperature A","Air pressure",developer_mode)
air_temp_A_metrics = pd.DataFrame({
    "MAE": [air_temp_A_mae],
    "MSE": [air_temp_A_mse],
    "R squared": [air_temp_A_r2],
    "Execution time": [air_temp_A_exec_time]
    })
if developer_mode == 1:
    print()
    print(air_temp_A_metrics)
    print()

# - Air temperature B -
air_temp_B_forecast, air_temp_B_mae, air_temp_B_mse, air_temp_B_r2, air_temp_B_exec_time = linear_regression_projector(air_temp_B_processing_df["Air temperature B"].to_numpy(),air_temp_B_processing_df,
                                                                                                                       "Air temperature B","Air pressure", developer_mode)
air_temp_B_metrics = pd.DataFrame({
    "Column used:": "Air temperature B",
    "MAE": [air_temp_B_mae],
    "MSE": [air_temp_B_mse],
    "R squared": [air_temp_B_r2],
    "Execution time": [air_temp_B_exec_time]
    })
if developer_mode == 1:
    print()
    print(air_temp_B_metrics)
    print()

# - Air humidity -
air_humidity_forecast, air_humidity_mae, air_humidity_mse, air_humidity_r2, air_humidity_exec_time = linear_regression_projector(air_humidity_processing_df["Air humidity"].to_numpy(), air_humidity_processing_df,
                                                                                                                                 "Air humidity", "Air pressure", developer_mode)
air_humidity_metrics = pd.DataFrame({
    "Column used:": "Air humidity",
    "MAE": [air_humidity_mae],
    "MSE": [air_humidity_mse],
    "R squared": [air_humidity_r2],
    "Execution time": [air_humidity_exec_time]
    })
if developer_mode == 1:
    print()
    print(air_humidity_metrics)
    print()

project_end = datetime.datetime.now() - project_start
if developer_mode == 1:
    print(f"Total processing time: {project_end}")