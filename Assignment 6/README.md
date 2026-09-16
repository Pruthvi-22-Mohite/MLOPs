# Assignment 6: Model Deployment with Flask and Docker

This assignment focuses on deploying a machine learning model as a REST API using Flask and packaging the application in a Docker container.

## Objective

- Train an Iris flower classification model
- Save the trained model as a serialized artifact
- Serve predictions through a Flask API
- Containerize the application for deployment

## Project Structure

- `app.py` — Flask application that loads the trained model and exposes `/predict`
- `model/train_model.py` — script to train the Random Forest model on the Iris dataset
- `requirements.txt` — Python dependencies required for the project
- `Dockerfile` — Docker image definition for the API service
- `iris_model.pkl` — trained model artifact used by the API

## Model Training

The model is trained using the Iris dataset from `scikit-learn` and saved as `iris_model.pkl`.

Run the training script:

```bash
cd "Assignment 6"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python model/train_model.py
```

This will:

- load the Iris dataset
- split data into train and test sets
- train a `RandomForestClassifier`
- evaluate the model accuracy and classification report
- save the trained model to `iris_model.pkl`

## Running the API

Start the Flask API:

```bash
cd "Assignment 6"
source .venv/bin/activate
python app.py
```

The application will run on:

- `http://localhost:5000`

### API Endpoints

#### GET `/`
Returns a simple health message.

Example response:

```json
{
  "message": "Iris Model API is running"
}
```

#### POST `/predict`
Accepts a JSON body containing a list of 4 flower features.

Example request:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

Example response:

```json
{
  "prediction": 0
}
```

## Docker Deployment

Build the Docker image:

```bash
docker build -t iris-flask-api .
```

Run the container:

```bash
docker run -p 5000:5000 iris-flask-api
```

This exposes the model API on port `5000`.

## Notes

- The app expects the model file `iris_model.pkl` to exist in the same directory as `app.py`.
- This project demonstrates a simple deployment workflow for an ML model in a production-like environment.
- It can be extended by adding versioning, monitoring, and CI/CD automation.
