import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# ---------------------------
# 1. Generate Synthetic Dataset
# ---------------------------

# Features (you can replace with real data later)
np.random.seed(42)
data_size = 1500

data = pd.DataFrame({
    "rainfall_mm": np.random.uniform(20, 300, data_size),
    "soil_moisture": np.random.uniform(10, 70, data_size),
    "slope_angle": np.random.uniform(5, 50, data_size),
    "vegetation_index": np.random.uniform(0.2, 0.9, data_size),
    "river_distance_km": np.random.uniform(0.1, 5, data_size),
})

# Cloudburst or Landslide label (0 = No Event, 1 = Event)
data["event"] = (
    (data["rainfall_mm"] > 180) &
    (data["soil_moisture"] > 45) &
    (data["slope_angle"] > 25)
).astype(int)

# ---------------------------
# 2. Train/Test Split
# ---------------------------
X = data.drop("event", axis=1)
y = data["event"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------------
# 3. Train Model
# ---------------------------
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    max_depth=12
)
model.fit(X_train, y_train)

# ---------------------------
# 4. Evaluate
# ---------------------------
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
print(f"Model Accuracy: {acc:.3f}")

# ---------------------------
# 5. Save Model
# ---------------------------
MODEL_PATH = "model.pkl"
joblib.dump(model, MODEL_PATH)

print(f"Model saved successfully as {MODEL_PATH}")
