# Assignment 7 – CI/CD Pipeline Using GitHub Actions

## Aim

To implement a CI/CD pipeline for a machine learning project using GitHub Actions, automating code validation, testing, and deployment.

## Project Description

This project demonstrates a basic Machine Learning application using the **Iris dataset** and **Logistic Regression**. A CI/CD pipeline is implemented using **GitHub Actions** to automatically install dependencies, run unit tests, and simulate deployment whenever code is pushed to the `main` branch or a Pull Request is created.

## Project Structure

```text
Assignment 7/
│
├── src/
│   └── model.py
│
├── tests/
│   └── test_model.py
│
├── requirements.txt
├── app.py
└── README.md
```

The GitHub Actions workflow is located at the repository root:

```text
.github/
└── workflows/
    └── ci-cd.yml
```

## Machine Learning Model

The project uses:

* **Dataset:** Iris Dataset
* **Algorithm:** Logistic Regression
* **Train-Test Split:** 80% training and 20% testing
* **Random State:** 42
* **Evaluation Metric:** Accuracy

The model training and prediction logic is implemented in `src/model.py`.

## Testing

`pytest` is used for unit testing.

The test verifies that the trained model achieves an accuracy of at least **80%**.

Run the test locally using:

```bash
pytest -v
```

## CI/CD Pipeline

The GitHub Actions workflow performs the following steps:

```text
Code Push / Pull Request
          ↓
   GitHub Actions
          ↓
    Checkout Code
          ↓
     Setup Python
          ↓
 Install Dependencies
          ↓
      Run Tests
          ↓
     Tests Pass?
       ↙      ↘
     No        Yes
     ↓          ↓
   Stop       Deploy
                ↓
     Deployment Simulation
```

### Continuous Integration (CI)

The CI stage:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs project dependencies.
4. Runs the unit tests using `pytest`.

If the tests fail, the pipeline stops.

### Continuous Deployment (CD)

After successful testing on the `main` branch, the deployment job is executed.

For this assignment, deployment is simulated using:

```bash
echo "Deployment started..."
echo "ML application deployed successfully."
```

## Failure Scenario

A failure scenario was tested by changing the accuracy condition from:

```python
assert accuracy >= 0.80
```

to:

```python
assert accuracy >= 0.99
```

This causes the test to fail and the deployment stage to be skipped.

The original condition was then restored:

```python
assert accuracy >= 0.80
```

## Technologies Used

* Python
* Scikit-learn
* Pytest
* Git
* GitHub
* GitHub Actions

## Conclusion

The project demonstrates a basic MLOps CI/CD pipeline in which machine learning code is automatically tested using GitHub Actions. Deployment is performed only after successful validation, demonstrating the basic principle of automated Continuous Integration and Continuous Deployment.
