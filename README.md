# MLOPs Assignments

This repository contains the work completed for the MLOPs coursework, organized by assignment.

## Repository Structure

- Assignment 1: Dataset versioning with DVC and data storage setup
- Assignment 2: ML experiments and model training using scikit-learn and MLflow
- Assignment 3: Data preprocessing, feature selection, and model pipeline development
- Assignment 4: Airflow-based data pipeline orchestration

## Assignments

### Assignment 1

Focus areas:
- dataset versioning
- DVC configuration
- storage of versioned data artifacts

Relevant folders:
- Assignment 1/DatasetVersioning
- Assignment 1/dvc-storage

### Assignment 2

Focus areas:
- model training
- model comparison
- experiment tracking with MLflow
- evaluation reports and saved models

Relevant folders:
- Assignment 2/data
- Assignment 2/models
- Assignment 2/notebooks
- Assignment 2/src
- Assignment 2/mlruns

### Assignment 3

Focus areas:
- preprocessing pipelines
- feature selection
- transformed data generation
- model pipeline serialization

Relevant folders:
- Assignment 3/data
- Assignment 3/models
- Assignment 3/output
- Assignment 3/src

### Assignment 4

Focus areas:
- Apache Airflow DAG orchestration
- extraction and validation pipeline
- reporting and processing workflow
- dockerized workflow setup

Relevant folders:
- Assignment 4/dags
- Assignment 4/data
- Assignment 4/config
- Assignment 4/output
- Assignment 4/plugins

## Notes

- This repository intentionally ignores generated artifacts such as virtual environments, Python cache files, log files, MLflow runs, and output folders.
- Local environment folders such as .venv are not tracked in Git.

## Suggested Workflow

1. Clone the repository.
2. Open the assignment folder you want to work on.
3. Create and activate a virtual environment if needed.
4. Install dependencies from the relevant requirements file.
5. Run the training or pipeline scripts for the assignment.

## Git

To push updates:

```bash
git add .
git commit -m "Your commit message"
git push
```

## License

This project is for academic coursework and learning purposes.
