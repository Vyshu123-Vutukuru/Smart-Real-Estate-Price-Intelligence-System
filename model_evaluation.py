from sklearn.metrics import r2_score, mean_squared_error
import joblib

def evaluate_model(model_path, X_test, y_test):
    model = joblib.load(model_path)
    predictions = model.predict(X_test)
    return {
        "r2_score": r2_score(y_test, predictions),
        "mse": mean_squared_error(y_test, predictions)
    }
