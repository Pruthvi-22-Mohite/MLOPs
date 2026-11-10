
import os
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Training Completed!")
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save model
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/model.joblib")

print("\nModel saved successfully!")
