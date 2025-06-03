from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib


app = Flask(__name__)
CORS(app)

# Load model + vectorizer
try:
    model = joblib.load("model/model.pkl")
    vectorizer = joblib.load("model/vectorizer.pkl")
    print("Model and vectorizer loaded.")
except Exception as e:
    print("ERROR loading model:", e)
    model = None
    vectorizer = None

@app.route("/ping")
def ping():
    return "pong"

@app.route("/test")
def test():
    return jsonify({"msg": "CORS is working!"})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print("Received:", data)

        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        user_input = data["text"]
        transformed = vectorizer.transform([user_input])
        prediction = model.predict(transformed)[0]

        return jsonify({"category": prediction})
    except Exception as e:
        print("!ERROR:", e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
