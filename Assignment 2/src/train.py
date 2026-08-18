import os
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

# ======================================================
# MLflow Tracking Configuration
# ======================================================

mlflow.set_tracking_uri("sqlite:///mlflow.db")

mlflow.set_experiment("Iris Classification")

# ======================================================
# Load Dataset
# ======================================================

iris = load_iris()

X = iris.data
y = iris.target

# ======================================================
# Train Test Split
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ======================================================
# Feature Scaling
# ======================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ======================================================
# Models
# ======================================================

models = {
    "Logistic Regression": LogisticRegression(max_iter=200),

    "Decision Tree": DecisionTreeClassifier(
        max_depth=4,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

os.makedirs("models", exist_ok=True)

# ======================================================
# Train Models
# ======================================================

for model_name, model in models.items():

    with mlflow.start_run(run_name=model_name):

        # Train

        model.fit(X_train, y_train)

        # Prediction

        y_pred = model.predict(X_test)

        # Metrics

        accuracy = accuracy_score(y_test, y_pred)

        precision = precision_score(
            y_test,
            y_pred,
            average="weighted"
        )

        recall = recall_score(
            y_test,
            y_pred,
            average="weighted"
        )

        f1 = f1_score(
            y_test,
            y_pred,
            average="weighted"
        )

        # ==================================================
        # Log Parameters
        # ==================================================

        mlflow.log_param("Model", model_name)

        if model_name == "Decision Tree":
            mlflow.log_param("Max Depth", 4)

        if model_name == "Random Forest":
            mlflow.log_param("Estimators", 100)

        # ==================================================
        # Log Metrics
        # ==================================================

        mlflow.log_metric("Accuracy", accuracy)
        mlflow.log_metric("Precision", precision)
        mlflow.log_metric("Recall", recall)
        mlflow.log_metric("F1 Score", f1)

        # ==================================================
        # Confusion Matrix
        # ==================================================

        cm = confusion_matrix(y_test, y_pred)

        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=iris.target_names
        )

        disp.plot()

        cm_file = f"{model_name}_cm.png"

        plt.savefig(cm_file)

        plt.close()

        mlflow.log_artifact(cm_file)

        # ==================================================
        # Classification Report
        # ==================================================

        report = classification_report(y_test, y_pred)

        report_file = f"{model_name}_report.txt"

        with open(report_file, "w") as f:
            f.write(report)

        mlflow.log_artifact(report_file)

        # ==================================================
        # Save Model
        # ==================================================

        mlflow.sklearn.log_model(
            sk_model=model,
            name="model"
        )

        print("=" * 50)
        print(model_name)
        print(f"Accuracy  : {accuracy:.4f}")
        print(f"Precision : {precision:.4f}")
        print(f"Recall    : {recall:.4f}")
        print(f"F1 Score  : {f1:.4f}")
        print("=" * 50)

print("\nAll experiments completed successfully!")