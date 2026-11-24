
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.utils import resample
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# File paths
BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "irrigation_prediction.csv"
MODEL_PATH = BASE_DIR / "hybrid_ann_model.pkl"

# Graph output paths
CONFUSION_GRAPH = BASE_DIR / "confusion_matrix.png"
METRICS_GRAPH = BASE_DIR / "classification_metrics.png"
ACCURACY_GRAPH = BASE_DIR / "model_accuracy.png"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# Features available from the website
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

TARGET_COLUMN = "Irrigation_Need"

# Check required columns
required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing dataset columns: {missing_columns}")

# Select input and output
X = df[FEATURE_COLUMNS]
y = df[TARGET_COLUMN]

print("\nFeatures used:")
print(FEATURE_COLUMNS)

print("\nTarget classes:")
print(y.value_counts())

# Numerical and categorical features
numerical_columns = [
    "Temperature_C",
    "Humidity",
    "Rainfall_mm",
    "Wind_Speed_kmh",
    "Field_Area_hectare",
    "Previous_Irrigation_mm"
]

categorical_columns = [
    "Crop_Type",
    "Crop_Growth_Stage"
]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Balance only the training dataset
training_data = X_train.copy()
training_data[TARGET_COLUMN] = y_train.values

maximum_count = training_data[TARGET_COLUMN].value_counts().max()

balanced_parts = []

for class_name in training_data[TARGET_COLUMN].unique():

    class_data = training_data[
        training_data[TARGET_COLUMN] == class_name
    ]

    balanced_class = resample(
        class_data,
        replace=True,
        n_samples=maximum_count,
        random_state=42
    )

    balanced_parts.append(balanced_class)

balanced_data = pd.concat(
    balanced_parts
).sample(frac=1, random_state=42)

X_train_balanced = balanced_data[FEATURE_COLUMNS]
y_train_balanced = balanced_data[TARGET_COLUMN]

print("\nBalanced training data:")
print(y_train_balanced.value_counts())

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_columns
        ),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ]
)

# Artificial Neural Network
ann = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    activation="relu",
    solver="adam",
    learning_rate_init=0.001,
    max_iter=300,
    early_stopping=True,
    random_state=42
)

# Complete ML pipeline
model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("ann", ann)
    ]
)

# Train model
print("\nTraining ANN model...")

model.fit(
    X_train_balanced,
    y_train_balanced
)

print("Training completed!")

# Evaluate model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Confusion matrix
cm = confusion_matrix(
    y_test,
    y_pred,
    labels=model.classes_
)

print("\nConfusion Matrix:")
print(cm)

# Save trained model
joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully!")
print("Saved at:", MODEL_PATH)

# --------------------------------
# GRAPH 1: CONFUSION MATRIX
# --------------------------------

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

display.plot(values_format="d")
plt.title("ANN Model - Confusion Matrix")
plt.tight_layout()
plt.savefig(CONFUSION_GRAPH, dpi=300)
plt.close()

print("\nConfusion matrix graph saved:", CONFUSION_GRAPH)

# --------------------------------
# GRAPH 2: PRECISION, RECALL, F1
# --------------------------------

report = classification_report(
    y_test,
    y_pred,
    output_dict=True,
    zero_division=0
)

classes = list(model.classes_)

precision = [report[c]["precision"] for c in classes]
recall = [report[c]["recall"] for c in classes]
f1 = [report[c]["f1-score"] for c in classes]

x = range(len(classes))
width = 0.25

plt.figure(figsize=(9, 5))

plt.bar(
    [i - width for i in x],
    precision,
    width,
    label="Precision"
)

plt.bar(
    x,
    recall,
    width,
    label="Recall"
)

plt.bar(
    [i + width for i in x],
    f1,
    width,
    label="F1-score"
)

plt.xlabel("Irrigation Classes")
plt.ylabel("Score")
plt.title("ANN Classification Performance")
plt.xticks(list(x), classes)
plt.ylim(0, 1)
plt.legend()
plt.tight_layout()
plt.savefig(METRICS_GRAPH, dpi=300)
plt.close()

print("Classification metrics graph saved:", METRICS_GRAPH)

# --------------------------------
# GRAPH 3: MODEL ACCURACY
# --------------------------------

plt.figure(figsize=(6, 5))

plt.bar(
    ["ANN Model"],
    [accuracy]
)

plt.ylabel("Accuracy")
plt.title("ANN Model Accuracy")
plt.ylim(0, 1)

plt.text(
    0,
    accuracy + 0.02,
    f"{accuracy * 100:.2f}%",
    ha="center"
)

plt.tight_layout()
plt.savefig(ACCURACY_GRAPH, dpi=300)
plt.close()

print("Accuracy graph saved:", ACCURACY_GRAPH)

print("\nAll performance graphs generated successfully!")
