from alpha import entrenar_modelo
import pandas as pd


def test_modelo_entrena():

    model, r2, mae, rmse = entrenar_modelo()

    assert model is not None


def test_modelo_tiene_buen_r2():

    model, r2, mae, rmse = entrenar_modelo()

    assert r2 >= 0.90


def test_modelo_tiene_mae_aceptable():

    model, r2, mae, rmse = entrenar_modelo()

    assert mae < 10


def test_modelo_tiene_rmse_aceptable():

    model, r2, mae, rmse = entrenar_modelo()

    assert rmse < 25


 