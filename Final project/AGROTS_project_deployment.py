import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime, os
import seaborn as sns
from Functionalities import linear_regression_projector, polynomial_regression_projector

# - Autodownload folder path -
dl_path = "C:\Users\Tomy\PycharmProjects\Math_algorithm_work\Final project\Saved_downloads\Recent"
os.chdir(dl_path)
# - Behaviour modifiers -
developer_mode = 1
deploy_switch = 0
# -----------------------
project_start = datetime.datetime.now()

file_path = "AGROTSDatasetFinal.csv"
if file_path == 0:
    raise LookupError("File path cannot be found as the field is empty")
source_dataframe = pd.read_csv(fr"{file_path}")
source_df_corr = source_dataframe.corr()
# - Correlation matrix
plt.figure(figsize=(10,8))
sns.heatmap(source_df_corr,annot=True,cmap='coolwarm',fmt='.4f',linewidths=0.5)
plt.title("Source data correlation matrix heat map")
plt.savefig("Source_data_heatmap.png")

print(f"NANs detected: {source_dataframe.isnull().sum()}\n")
if developer_mode == 1:
    print("Dataframe info:")
    print(source_dataframe.info())
    print(source_dataframe.head(15))
    print(f"\nDataframe shape: {source_dataframe.shape}")
    print(f"Number of rows: {source_dataframe.shape[0]}, number of columns: {source_dataframe.shape[1]}")

# - Prep work -
features = ["AirTemperatureA", "AirTemperatureB", "AirHumidity"]
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
plt.savefig("Air_pressure_VS_air_temp_A.png")
plt.close()
# - Air temperature B VS air pressure
plt.scatter(air_temperature_B, air_pressure_data)
plt.xlabel("Air temperature B")
plt.ylabel("Air pressure")
plt.title("Air pressure VS Air temperature B")
plt.savefig("Air_pressure_VS_air_temp_B.png")
plt.close()
# - Air humidity VS air pressure
plt.scatter(air_humidity, air_pressure_data)
plt.xlabel("Air humidity")
plt.ylabel("Air pressure")
plt.title("Air pressure VS Air humidity")
plt.savefig("Air_pressure_VS_air_humidity.png")
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
plt.savefig("Processing_corr_matrix_heat_map.png")
plt.close()
# --------------------------
# ----> Deployment <----
if deploy_switch == 1:
    # - Air temperature A -
    air_temp_A_forecast, air_temp_A_test_data, air_temp_A_mae, air_temp_A_mse, air_temp_A_r2, air_temp_A_exec_time, air_temp_A_model = linear_regression_projector(source_DF=source_dataframe, features=features,target="AirTemperatureA",developer_mode=developer_mode)

    air_temp_A_metrics = pd.DataFrame({
        "MAE": [air_temp_A_mae],
        "MSE": [air_temp_A_mse],
        "R squared": [air_temp_A_r2],
        "Execution time": [air_temp_A_exec_time],
        "Model": [air_temp_A_model]
        })
    if developer_mode == 1:
        print()
        for x_11, y_11 in air_temp_A_metrics.items():
            print(f"{x_11}: {y_11}")
        print()

    # - Air temperature B -
    air_temp_B_forecast, air_temp_B_test_data, air_temp_B_mae, air_temp_B_mse, air_temp_B_r2, air_temp_B_exec_time, air_temp_B_model = linear_regression_projector(source_DF=source_dataframe, features=features,target="AirTemperatureB", developer_mode=developer_mode)

    air_temp_B_metrics = pd.DataFrame({
        "Column used:": "Air temperature B",
        "MAE": [air_temp_B_mae],
        "MSE": [air_temp_B_mse],
        "R squared": [air_temp_B_r2],
        "Execution time": [air_temp_B_exec_time],
        "Model": [air_temp_A_model]
        })
    if developer_mode == 1:
        print()
        for x_12, y_12 in air_temp_B_metrics.items():
            print(f"{x_12}: {y_12}")
        print()

    # - Air humidity -
    air_humidity_forecast, air_humidity_test_data, air_humidity_mae, air_humidity_mse, air_humidity_r2, air_humidity_exec_time, air_humidity_model = linear_regression_projector(source_DF=source_dataframe, features=features, target="AirHumidity", developer_mode=developer_mode)

    air_humidity_metrics = pd.DataFrame({
        "Column used:": "Air humidity",
        "MAE": [air_humidity_mae],
        "MSE": [air_humidity_mse],
        "R squared": [air_humidity_r2],
        "Execution time": [air_humidity_exec_time],
        "Model": [air_humidity_model]
        })
    if developer_mode == 1:
        print()
        for x_10, y_10 in air_humidity_metrics.items():
            print(f"{x_10}: {y_10}")
        print()

project_end = datetime.datetime.now() - project_start
# ---> Document the processing time <---
if developer_mode == 1:
    print(f"Total processing time: {project_end}")