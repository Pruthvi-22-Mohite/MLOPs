from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os


BASE_DIR = "/opt/airflow"

DATA_FILE = os.path.join(
    BASE_DIR,
    "data",
    "input_data.csv"
)

EXTRACTED_FILE = os.path.join(
    BASE_DIR,
    "output",
    "extracted_data.csv"
)

PROCESSED_FILE = os.path.join(
    BASE_DIR,
    "output",
    "processed_data.csv"
)

VALIDATION_FILE = os.path.join(
    BASE_DIR,
    "output",
    "validation_report.txt"
)

REPORT_FILE = os.path.join(
    BASE_DIR,
    "output",
    "final_report.txt"
)


def extract():
    import pandas as pd

    os.makedirs(
        os.path.join(BASE_DIR, "output"),
        exist_ok=True
    )

    df = pd.read_csv(DATA_FILE)

    df.to_csv(
        EXTRACTED_FILE,
        index=False
    )

    print("Data extracted successfully.")
    print(f"Number of records: {len(df)}")


def validate():
    import pandas as pd

    df = pd.read_csv(EXTRACTED_FILE)

    missing_values = df.isnull().sum()
    total_missing = missing_values.sum()

    invalid_records = 0

    if "age" in df.columns:
        invalid_records += (
            (df["age"].notna()) &
            (df["age"] <= 0)
        ).sum()

    validation_text = f"""
DATA VALIDATION REPORT
======================

Total Records: {len(df)}

Missing Values:
{missing_values.to_string()}

Total Missing Values: {total_missing}

Invalid Records: {invalid_records}

Validation Status: Completed
"""

    with open(VALIDATION_FILE, "w") as file:
        file.write(validation_text)

    print(validation_text)


def process():
    import pandas as pd

    df = pd.read_csv(EXTRACTED_FILE)

    # Remove duplicate records
    df = df.drop_duplicates()

    # Fill missing numerical values
    if "age" in df.columns:
        df["age"] = df["age"].fillna(
            df["age"].median()
        )

    if "salary" in df.columns:
        df["salary"] = df["salary"].fillna(
            df["salary"].median()
        )

    # Clean text fields
    if "name" in df.columns:
        df["name"] = df["name"].str.strip()

    if "department" in df.columns:
        df["department"] = (
            df["department"]
            .str.strip()
            .str.title()
        )

    df.to_csv(
        PROCESSED_FILE,
        index=False
    )

    print("Data processing completed.")
    print(f"Processed records: {len(df)}")


def report():
    import pandas as pd

    df = pd.read_csv(PROCESSED_FILE)

    validation = ""

    if os.path.exists(VALIDATION_FILE):
        with open(VALIDATION_FILE, "r") as file:
            validation = file.read()

    report_text = f"""
AIRFLOW DATA PIPELINE REPORT
============================

Workflow: data_pipeline_dag

Number of Records Processed:
{len(df)}

Missing Values Identified:
{validation}

Processing Completion Status:
SUCCESS

Report Generation Status:
COMPLETED
"""

    with open(REPORT_FILE, "w") as file:
        file.write(report_text)

    print(report_text)


def notify():
    print(
        "SUCCESS: Data pipeline workflow completed successfully!"
    )


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(minutes=30),
}

with DAG(
    dag_id="data_pipeline_dag",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    dagrun_timeout=timedelta(hours=1),
    tags=["MLOps", "Assignment4"]
) as dag:

    t1 = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    t2 = PythonOperator(
        task_id="validate",
        python_callable=validate
    )

    t3 = PythonOperator(
        task_id="process",
        python_callable=process
    )

    t4 = PythonOperator(
        task_id="report",
        python_callable=report
    )

    t5 = PythonOperator(
        task_id="notify",
        python_callable=notify
    )

    t1 >> t2 >> t3 >> t4 >> t5