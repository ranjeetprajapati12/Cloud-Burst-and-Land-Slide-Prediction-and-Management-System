<<<<<<< HEAD

# Cloudburst & Landslide Prediction — Local Demo

This is a self-contained demo that runs locally (Flask). It includes:
- a pretrained RandomForest model (trained on synthetic data) saved as `model.pkl`
- a simple web UI with a Leaflet map (click map to set location) and inputs for rainfall, slope, etc.
- a theory page explaining cloudbursts and landslide drivers.

## How to run (Linux / macOS / Windows with Python 3.8+)

1. Clone or unzip the project.
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\\Scripts\\activate on Windows
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

## Notes
- This demo uses synthetic training data for illustration only. Do NOT use for operational decisions.
- To improve: replace training data with historical landslide inventory and real rainfall/soil layers.
=======
# Cloud-Burst-and-Land-Slide-Prediction-and-Management-System
Build an AI-powered early-warning system that (A) identifies short-term extreme rainfall / cloudburst risk at high spatial resolution, and (B) predicts/flags landslide susceptibility and imminent landslide occurrence in vulnerable catchments —combining meteorological time-series, remote sensing and geospatial features to generate actionable alerts.
>>>>>>> b65b0ee166bc1530f4260de7436948823f5e5fed
