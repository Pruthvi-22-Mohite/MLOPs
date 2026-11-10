
import time
import joblib

from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import Response
from pydantic import BaseModel

# Load trained model
model = joblib.load("model/model.joblib")

CLASS_NAMES = ["setosa", "versicolor", "virginica"]

app = FastAPI(title="ML Model Monitoring API")

@app.get("/")
def root():
    return {
        "message": "ML Model Monitoring API",
        "docs": "/docs",
        "health": "/health",
        "prediction": "POST /predict",
        "metrics": "/metrics",
    }

# Request metrics
REQUESTS = Counter(
    "ml_prediction_requests_total",
    "Total prediction requests"
)

ERRORS = Counter(
    "ml_prediction_errors_total",
    "Total failed prediction requests"
)

LATENCY = Histogram(
    "ml_prediction_latency_seconds",
    "Prediction request latency"
)

PREDICTIONS = Counter(
    "ml_predictions_total",
    "Total successful predictions"
)

# Input validation
class Features(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Middleware to monitor prediction requests
@app.middleware("http")
async def monitor_requests(request: Request, call_next):

    if request.url.path != "/predict":
        return await call_next(request)

    start_time = time.perf_counter()

    REQUESTS.inc()

    try:
        response = await call_next(request)

        if response.status_code >= 400:
            ERRORS.inc()

        return response

    except Exception:
        ERRORS.inc()
        raise

    finally:
        LATENCY.observe(time.perf_counter() - start_time)


# Prediction endpoint
@app.post("/predict")
def predict(features: Features):

    try:
        data = [[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]]

        prediction = model.predict(data)[0]

        PREDICTIONS.inc()

        return {
            "prediction": CLASS_NAMES[int(prediction)]
        }

    except Exception:
        raise


# Health endpoint
@app.get("/health")
def health():
    return {"status": "API is running"}


# Prometheus metrics endpoint
@app.get("/metrics")
def metrics():

    return Response(
        content=generate_latest(),
        media_type="text/plain; version=0.0.4"
    )
