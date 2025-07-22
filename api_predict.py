from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("linear_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['features']]
    prediction = model.predict(features)
    return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
