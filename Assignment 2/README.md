# Assignment 2: MLflow Experiment Tracking

This assignment trains three Iris classifiers and records their experiments with
MLflow: Logistic Regression, Decision Tree, and Random Forest.

## Contents

- `src/train.py`: trains, evaluates, and logs all three models.
- `requirements.txt`: Python dependencies.
- `*_report.txt`: classification reports from the recorded runs.
- `*_cm.png`: confusion-matrix images.
- `data/mlruns/`: local MLflow tracking data and logged model artifacts.
- `models/`: reserved location for exported models.
- `notebooks/` and `screenshots/`: workspace locations for exploration and evidence.

## Run

```bash
pip install -r requirements.txt
python src/train.py
```

The script uses a local SQLite-backed MLflow tracking URI and creates the
experiment named `Iris Classification`.