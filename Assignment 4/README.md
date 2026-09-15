# Assignment 4: Airflow Data Pipeline

This assignment orchestrates an extract, validate, process, report, and notify
workflow with Apache Airflow. The DAG is `dags/data_pipeline_dag.py` and is
configured to run in the supplied Docker Compose environment.

## Project areas

- `dags/`: Airflow DAG definitions.
- `config/`: Airflow configuration.
- `data/`: input data consumed by the DAG.
- `output/`: extracted, processed, and reported results.
- `plugins/`: reserved for custom Airflow plugins.
- `docker-compose.yaml`, `start`, and `query`: local environment helpers.
- `logs/`: generated Airflow task and scheduler logs.

The assignment brief is stored in `32_AIDS_D_MLOps_Assignment4.pdf`.