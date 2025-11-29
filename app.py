from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from database import init_db, insert_history, get_history

# Init Flask
app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Init DB
init_db()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data["review"]

    X = vectorizer.transform([review])
    pred = model.predict(X)[0]
    prob = float(model.predict_proba(X)[0].max())

    # simpan history
    insert_history(review, pred, prob)

    return jsonify({
        "review": review,
        "sentimen": pred,
        "confidence": prob
    })

@app.route("/history", methods=["GET"])
def history():
    rows = get_history()
    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "review": r[1],
            "sentimen": r[2],
            "confidence": r[3],
            "timestamp": r[4]
        })
    return jsonify(result)

app.run(debug=True)
