from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import make_scorer, mean_squared_error

# Gerar dados de regressão
X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)

# Modelo
model = LinearRegression()

# Validação cruzada (5-fold)
mse_scores = cross_val_score(model, X, y, cv=5, scoring=make_scorer(mean_squared_error))

# Resultados
print("MSE por fold:", mse_scores)
print("MSE médio:", mse_scores.mean())
