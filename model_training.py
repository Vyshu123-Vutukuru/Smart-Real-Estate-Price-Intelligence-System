import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_models(df):
    X = df[['area', 'bedrooms']]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    models = {
        'linear': LinearRegression(),
        'random_forest': RandomForestRegressor()
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        joblib.dump(model, f"{name}_model.pkl")
