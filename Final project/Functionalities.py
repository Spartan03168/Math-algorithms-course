import numpy as np
import datetime
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression

def linear_regression_projector(data_injection: [list, np.ndarray], source_DF, features: str, target: str, developer_mode: int):
    assert(isinstance(data_injection, (list, np.ndarray)))
    assert(type(developer_mode) == int)
    start = datetime.datetime.now()
    # - Model initialization -
    model_applied = LinearRegression()
    # - x train, x test, y train, y test splitting -
    X = source_DF[features]
    y = source_DF[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # - Deploy forecast -
    model_applied.fit(X_train, y_train)
    projection = model_applied.predict(X_test)
    # - End processing time -
    end = datetime.datetime.now() - start
    # - Accuracy calculations -
    mse_tracked = mean_squared_error(y_test, projection)
    mae_tracked = mean_absolute_error(y_test, projection)
    r2_tracked = r2_score(y_test, projection)
    # - Return statements -
    return projection, mae_tracked, mse_tracked, r2_tracked, end

