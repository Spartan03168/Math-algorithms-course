import numpy as np
import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from Specialist_code import numpy_conversion

def linear_regression_projector(source_DF, features: [list, np.ndarray], target: str, developer_mode: int):
    assert(isinstance(features, (list, np.ndarray)))
    assert(len(features) > 0)
    assert(type(target) == str)
    assert(len(target) > 0)
    assert(type(developer_mode) == int)

    if developer_mode == 1:
        print("---------\nLinear regression deployed")
        print(f"Features: {features}\nTarget: {target}\n---------")
    start = datetime.datetime.now()
    # - Model initialization -
    model_applied = LinearRegression()
    if developer_mode == 1:
        print("Model initiated")
        print(f"Model details:\n{model_applied}")
    # - x train, x test, y train, y test splitting -
    X = source_DF[features]
    y = source_DF[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    if developer_mode == 1:
        print("Data splitting completed")
    # - Deploy forecast -
    model_applied.fit(X_train, y_train)
    projection = model_applied.predict(X_test)
    r_squared = model_applied.score(X_train, y_train)
    coeff = model_applied.coef_
    # - Document coefficients -
    coef_file = pd.DataFrame({
        "Feature": features,
        "Coefficients": coeff
        })
    coef_file.to_csv("Linear_reg_coefficients.csv")
    # -------------------------
    if developer_mode == 1:
        print(f"Coefficients: {coeff}")
        print(f"R squared of forecast\n{r_squared}")
        print("Forecast completed")
    # - End processing time -
    end = datetime.datetime.now() - start
    # - Accuracy calculations -
    mse_tracked = mean_squared_error(y_test, projection)
    mae_tracked = mean_absolute_error(y_test, projection)
    r2_tracked = r_squared
    # - Accuracy documentation -
    accuracy_tracking = pd.DataFrame({
        "MAE": [mae_tracked],
        "MSE": [mse_tracked],
        "R squared": [r2_tracked]
        })
    accuracy_tracking.to_csv("Linear_reg_accuracy_documented.csv")
    # --------------------------
    if developer_mode == 1:
        print("Accuracy diagnostics calculated\n")
    # - Return statements -
    return numpy_conversion(projection), numpy_conversion(y_test), mae_tracked, mse_tracked, r2_tracked, end, model_applied

def polynomial_regression_projector(source_DF, features: [list, np.ndarray],
                                    target: str, developer_mode: int, forecast_steps: int, poly_degrees: int):
    assert(isinstance(features, (list, np.ndarray)))
    assert(type(target) == str)
    assert(len(target) > 0)
    assert(type(developer_mode) == int)
    assert(type(forecast_steps) == int)
    assert(forecast_steps > 0)
    assert(type(poly_degrees) == int)
    assert(poly_degrees > 0)

    if developer_mode == 1:
        print("---------\nPolynomial linear regression deployed")
        print(f"Features: {features}\nTarget: {target}\n---------")
    start = datetime.datetime.now()
    # ---------
    # - X and y splitting -
    X = source_DF[features]
    y = source_DF[target]
    if developer_mode == 1:
        print("Data splitting completed")
    # - Model declaration -
    degrees = 2
    model = make_pipeline(PolynomialFeatures(degrees), LinearRegression())
    model.fit(X,y)
    # - Model diagnostics -
    # Extract the trained linear regression model
    linear_model = model.named_steps['linearregression']
    # Extract coefficients and intercept
    coefficients = linear_model.coef_
    """
    model_diagnostics = pd.DataFrame({
        "Feature": features,
        "Coefficients": coefficients
        })
    model_diagnostics.to_csv("Poly_reg_coeffs.csv")
    """
    # - Forecast mechanism -
    forecast_data = numpy_conversion(model.predict(X))
    # ---------
    end = datetime.datetime.now() - start
    # - Accuracy tracking diagnostics -
    mse_tracked = mean_squared_error(y, forecast_data)
    mae_tracked = mean_absolute_error(y, forecast_data)
    r2_tracked = r2_score(y, forecast_data)
    accuracy_tracking = pd.DataFrame({
        "MAE": [mae_tracked],
        "MSE": [mse_tracked],
        "R squared": [r2_tracked]
        })
    accuracy_tracking.to_csv("Poly_reg_accuracy_documented.csv")
    # - Return statements -
    return numpy_conversion(forecast_data), mae_tracked, mse_tracked, r2_tracked, end, model
