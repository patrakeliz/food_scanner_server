from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "AI Nutrition Server is running."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    return jsonify({
        "message": "Received data successfully.",
        "data": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)