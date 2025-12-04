
from flask import Flask, render_template, request, jsonify
import joblib, numpy as np, traceback
from pathlib import Path
app = Flask(__name__)

MODEL_PATH = Path(__file__).parent / "model.pkl"
model = joblib.load(MODEL_PATH)

FEATURE_ORDER = ["rainfall_mm","soil_moisture","slope_deg","ndvi","dist_river_km"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/theory")
def theory():
    return render_template("theory.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json() or request.form.to_dict()
        # read features in order, allow strings -> float
        x = [float(data.get(f, 0)) for f in FEATURE_ORDER]
        proba = float(model.predict_proba([x])[0][1])
        label = int(proba >= 0.5)
        return jsonify({"probability": proba, "label": label, "features": dict(zip(FEATURE_ORDER, x))})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
