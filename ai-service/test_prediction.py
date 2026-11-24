
import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent

# Load dataset
df = pd.read_csv(BASE_DIR / "irrigation_prediction.csv")

# Separate input and target
X = df.drop(columns=["Irrigation_Need"])
y = df["Irrigation_Need"]

# Recreate the same test split used during training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Load saved ANN model
model = joblib.load(BASE_DIR / "hybrid_ann_model.pkl")

print("ANN model loaded successfully!")

# Predict first 10 test records
predictions = model.predict(X_test.iloc[:10])

print("\nIrrigation Prediction Results")
print("-" * 45)

for i in range(10):
    print("Actual:", y_test.iloc[i])
    print("Predicted:", predictions[i])
    print("-" * 45)
