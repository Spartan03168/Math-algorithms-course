import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime, os
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression

# - Autodownload folder path -
dl_path = r"C:\Users\Tomy\PycharmProjects\Math_algorithm_work\Final project\Saved_downloads\Recent"
os.chdir(dl_path)
# - Behaviour modifiers -
developer_mode = 1
deploy_switch = 1
# -----------------------
project_start = datetime.datetime.now()

file_path = r"C:\Users\Tomy\PycharmProjects\Math_algorithm_work\Final project\AGROTSDatasetFinal.csv"
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
features = ["AirTemperatureA", "AirTemperatureB", "AirHumidity", "B500", "V450","G550"]
air_pressure_data = source_dataframe["AirPressure"].to_numpy()
air_temperature_A = source_dataframe["AirTemperatureA"].to_numpy()
air_temperature_B = source_dataframe["AirTemperatureB"].to_numpy()
air_humidity = source_dataframe["AirHumidity"].to_numpy()
air_b500 = source_dataframe["B500"].to_numpy()
air_v450 = source_dataframe["V450"].to_numpy()
air_g550 = source_dataframe["G550"].to_numpy()

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
# - B500 VS air pressure -
plt.scatter(air_b500, air_pressure_data)
plt.xlabel("B500 data")
plt.ylabel("Air pressure")
plt.title("Air pressure VS B500 data")
plt.savefig("Air_pressure_VS_B500_data.png")
plt.close()
# - V450 VS air pressure -
plt.scatter(air_v450, air_pressure_data)
plt.xlabel("V450 data")
plt.ylabel("Air pressure")
plt.title("Air pressure VS V450 data")
plt.savefig("Air_pressure_VS_V450_data.png")
plt.close()
# - G550 VS air pressure -
plt.scatter(air_b500, air_pressure_data)
plt.xlabel("G550 data")
plt.ylabel("Air pressure")
plt.title("Air pressure VS G550 data")
plt.savefig("Air_pressure_VS_G550_data.png")
plt.close()
# ---> Correleation coeficients <---
process_data = pd.DataFrame({
    "Air pressure": air_pressure_data,
    "Air temperature A": air_temperature_A,
    "Air temperature B": air_temperature_B,
    "Air humidity": air_humidity,
    "G550": air_g550,
    "V450": air_v450,
    "B500": air_b500
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
    model = LinearRegression()
    # Features and target
    X = source_dataframe[features]
    y = source_dataframe["AirPressure"]
    # Splitting
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Model fitting and forecasting
    model.fit(X_train, y_train)
    projection = model.predict(X_test)
    r_squared = model.score(X_train, y_train)
    coeff = model.coef_
    if developer_mode == 1:
        # Dual column readout of variables in features and coefficients
        for variables in range(7):
            pass
        print(f"R squared of forecast: {r_squared}")
    # Accuracy metrics
    mse_tracked = mean_squared_error(y_test, projection)
    mae_tracked = mean_absolute_error(y_test, projection)
    r2_tracked = r_squared


project_end = datetime.datetime.now() - project_start
# ---> Document the processing time <---
"""
if developer_mode == 1:
    print(f"Total processing time: {project_end}")
"""
