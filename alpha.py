import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


def entrenar_modelo():

    df = pd.read_csv("FuelConsumptionCo2.csv")

    df.drop(
        ['MAKE', 'MODEL', 'VEHICLECLASS', 'TRANSMISSION', 'FUELTYPE'],
        axis=1,
        inplace=True
    )

    df.dropna(inplace=True)

    X = df.drop('CO2EMISSIONS', axis=1)
    y = df['CO2EMISSIONS']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=1
    )

    alpha_range = [1, 0.01, 0.001, 0.0001]

    model = make_pipeline(
        StandardScaler(),
        RidgeCV(
            alphas=alpha_range,
            scoring='neg_mean_squared_error'
        )
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("R2:", r2)
    print("MAE:", mae)
    print("RMSE:", rmse)

    return model, r2, mae, rmse


if __name__ == "__main__":
    entrenar_modelo()