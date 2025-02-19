import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

