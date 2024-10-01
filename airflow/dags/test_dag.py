from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the DAG and set some default arguments
default_args = {
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
}

with DAG(
    dag_id='hello_world_dag11',
    default_args=default_args,
    schedule_interval='@daily',  # Runs daily
    catchup=False,  # Do not backfill
) as dag:

    # Define the task using BashOperator
    hello_world_task = BashOperator(
        task_id='hello_world',
        bash_command='echo "Hello, World!"'
    )

    # Set the task in the DAG
    hello_world_task
