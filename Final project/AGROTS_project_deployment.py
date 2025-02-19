import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
from Functionalities import linear_regression_projector

# - Behaviour modifiers -
developer_mode = 1
# -----------------------
project_start = datetime.datetime.now()

file_path = "AGROTSDatasetFinal.csv"
if file_path == 0:
    raise LookupError("File path cannot be found as the field is empty")
source_dataframe = pd.read_csv(fr"{file_path}")
print(f"NANs detected: {source_dataframe.isnull().sum()}\n")
if developer_mode == 1:
    print("Dataframe info:")
    print(source_dataframe.info())
    print(source_dataframe.head(15))
    print(f"\nDataframe shape: {source_dataframe.shape}")
    print(f"Number of rows: {source_dataframe.shape[0]}, number of columns: {source_dataframe.shape[1]}")

# - Prep work -
air_pressure_data = source_dataframe["AirPressure"].to_numpy()
air_temperature_A = source_dataframe["AirTemperatureA"].to_numpy()
air_temperature_B = source_dataframe["AirTemperatureB"].to_numpy()
air_humidity = source_dataframe["AirHumidity"].to_numpy()

# ---> Charting process <---
# - Air temperature A VS air pressure
plt.scatter(air_temperature_A, air_pressure_data)
plt.xlabel("Air temperature A")
plt.ylabel("Air pressure")
plt.title("Air pressure VS Air temperature A")
plt.show()
plt.close()
# - Air temperature B VS air pressure
plt.scatter(air_temperature_B, air_pressure_data)
plt.xlabel("Air temperature B")
plt.ylabel("Air pressure")
plt.title("Air pressure VS Air temperature B")
plt.show()
plt.close()
# - Air humidity VS air pressure
plt.scatter(air_humidity, air_pressure_data)
plt.xlabel("Air humidity")
plt.ylabel("Air pressure")
plt.title("Air pressure VS Air humidity")
plt.show()
plt.close()
# ---> Correleation coeficients <---
process_data = pd.DataFrame({
    "Air pressure": air_pressure_data,
    "Air temperature A": air_temperature_A,
    "Air temperature B": air_temperature_B,
    "Air humidity": air_humidity
})
corr_matrix = process_data.corr()
print("\nCorrelation matrix:\n")
print(corr_matrix)
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',fmt='.4f',linewidths=0.5)
plt.title("Correlation matrix heat map")
plt.show()
# --------------------------

air_temp_A_processing_df = pd.DataFrame({
    "Air pressure": air_pressure_data,
    "Air temperature A": air_temperature_A
    })

air_temp_B_processing_df = pd.DataFrame({
    "Air pressure": air_pressure_data,
    "Air temperature B": air_temperature_B
    })

air_humidity_processing_df = pd.DataFrame({
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
# ---> Charting process <---

# ---> Document the processing time <---
if developer_mode == 1:
    print(f"Total processing time: {project_end}")