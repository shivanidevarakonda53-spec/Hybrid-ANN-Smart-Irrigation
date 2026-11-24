
import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "hybrid_ann_model.pkl"

model = joblib.load(MODEL_PATH)

FEATURE_COLUMNS = [
    "Temperature_C",
    "Humidity",
    "Rainfall_mm",
    "Wind_Speed_kmh",
    "Crop_Type",
    "Crop_Growth_Stage",
    "Field_Area_hectare",
    "Previous_Irrigation_mm"
]

def predict_irrigation(features):

    missing_columns = [
        column for column in FEATURE_COLUMNS
        if column not in features
    ]

    if missing_columns:
        raise ValueError(
            f"Missing input columns: {missing_columns}"
        )

    input_data = pd.DataFrame(
        [[features[column] for column in FEATURE_COLUMNS]],
        columns=FEATURE_COLUMNS
    )

    prediction = model.predict(input_data)[0]

    return {
        "irrigation_need": str(prediction)
    }

if __name__ == "__main__":
    print("ANN model loaded successfully!")
    print("Prediction service is ready!")
