import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import warnings
from sklearn.metrics import r2_score
from sklearn import metrics
warnings.filterwarnings('ignore')

df = pd.read_excel("FuelConsumptionCo2.xlsx")

df.drop(['MAKE', 'MODEL','VEHICLECLASS', 'TRANSMISSION','FUELTYPE'], axis=1, inplace= True)


# Remover renglones faltantes
df.dropna(inplace=True)

# Comprobación de valores no faltantes
plt.figure(figsize=(20,6))
sns.heatmap(df.isnull(),yticklabels= False, cbar=False, cmap='viridis')

X = df.drop('CO2EMISSIONS',axis=1)
y= df['CO2EMISSIONS']

# División de grupos de entrenamiento y de prueba 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)

# Ejecución de modelo de regresión lineal múltiple 
from sklearn.linear_model import LinearRegression 
linreg= LinearRegression()
linreg.fit(X_train, y_train)

# Impresión de coeficientes de regresión 
print("Intercepto:", linreg.intercept_)
print("Coeficientes:", linreg.coef_)

# Predicciones 
y_pred= linreg.predict(X_test)
y_pred

# Regresión de Ridge alpha = 0.1
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
# Crear un pipeline para escalar los datos y aplicar Ridge
pipeline = make_pipeline(StandardScaler(), Ridge(alpha=0.1))
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)


# Impresión de indicadores de bondad de ajuste 
print("Valor de R cuadrada:", r2_score(y_test, y_pred))
print("Error absoluto medio:", metrics.mean_absolute_error(y_test, y_pred))
print("Error cuadrático medio:", metrics.mean_squared_error(y_test, y_pred))
print("Raíz del Error cuadrático medio:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# Examinar coeficientes de la regresión Ridge 
ridgereg = pipeline.named_steps['ridge'] # Acceder al modelo Ridge dentro del pipeline
print("Intercepto:", ridgereg.intercept_)
print("Coeficientes:", ridgereg.coef_)

# Optimización de alpha Ridge 
alpha_range= 10.**np.arange(-2,3)
alpha_range

# Regresión de Lasso alpha = 0.001
from sklearn.linear_model import Lasso 
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

pipeline = make_pipeline(StandardScaler(), Lasso(alpha=0.001))
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Examinar coeficientes 
lassoreg = pipeline.named_steps['lasso']  # Acceso al modelo Lasso dentro del pipeline
print("Intercepto:", lassoreg.intercept_)
print("Coeficientes:", lassoreg.coef_)


from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Definir el rango de valores de alpha
alpha_range = [1, 0.01, 0.001, 0.0001]
# Crear un pipeline para escalar los datos y aplicar RidgeCV
ridge_pipeline = make_pipeline(StandardScaler(), RidgeCV(alphas=alpha_range, scoring='neg_mean_squared_error'))
ridge_pipeline.fit(X_train, y_train)
# Obtener el modelo ajustado y el valor óptimo de alpha
ridgeregcv = ridge_pipeline.named_steps['ridgecv']
print("Alpha óptimo:", ridgeregcv.alpha_)


# Predicción mediante alpha óptimo Ridge 
y_pred= ridgeregcv.predict(X_test)

# Impresión de indicadores de bondad de ajuste
print("Valor de R cuadrada:", r2_score(y_test, y_pred))
print("Error absoluto medio:", metrics.mean_absolute_error(y_test, y_pred))
print("Error cuadrático medio:", metrics.mean_squared_error(y_test, y_pred))
print("Raíz del Error cuadrático medio:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# Impresión de indicadores de bondad de ajuste Lasso
print("Valor de R cuadrada:", r2_score(y_test, y_pred))
print("Error absoluto medio:", metrics.mean_absolute_error(y_test, y_pred))
print("Error cuadrático medio:", metrics.mean_squared_error(y_test, y_pred))
print("Raíz del Error cuadrático medio:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# Selección de valor óptimo de Alpha para Lasso 
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

lasso_pipeline = make_pipeline(StandardScaler(), LassoCV(n_alphas=100, random_state=1))
lasso_pipeline.fit(X_train, y_train)
lassoregcv = lasso_pipeline.named_steps['lassocv']
print("Alpha óptimo:", lassoregcv.alpha_)

print("Intercepto:", lassoregcv.intercept_)
print("Coeficientes:", lassoregcv.coef_)


# Predicción mediante alpha óptimo Lasso
y_pred= lassoregcv.predict(X_test)

# Impresión de indicadores de bondad de ajuste
print("Valor de R cuadrada:", r2_score(y_test, y_pred))
print("Error absoluto medio:", metrics.mean_absolute_error(y_test, y_pred))
print("Error cuadrático medio:", metrics.mean_squared_error(y_test, y_pred))
print("Raíz del Error cuadrático medio:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
