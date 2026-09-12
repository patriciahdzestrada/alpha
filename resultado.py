import pandas as pd
from alpha import entrenar_modelo


def resultado():

    model, r2, mae, rmse = entrenar_modelo()

    resultado_modelo = pd.DataFrame({
        "metrica": ["R2", "MAE", "RMSE"],
        "valor": [r2, mae, rmse]
    })

    return resultado_modelo


df_resultado = resultado()

print(df_resultado)

df_resultado.to_csv("resultado_modelo.csv", index=False)