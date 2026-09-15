# Iris Classification REST API

## Objective

# Assignment 5: Iris Classification REST API
This project implements a REST API using FastAPI to serve predictions
from a trained Iris flower classification model.

## Run locally

```bash
pip install -r requirements.txt
python train_model.py
uvicorn main:app --reload
```

Open `/docs` for the interactive API documentation. The API provides health,
model-info, and prediction endpoints.

The model artifact is created in `artifacts/` by `train_model.py`, and the API
tests in `tests/` exercise validation, health, and prediction behavior.

## Technologies

- Python
- FastAPI
- Scikit-learn
- NumPy
- Joblib
- Pydantic
- Pytest

## Project Structure

```text
fastapi-ml-assignment/
├── artifacts/
│   └── iris_model.joblib
├── tests/
│   └── test_api.py
├── main.py
├── train_model.py
├── requirements.txt
└── README.md