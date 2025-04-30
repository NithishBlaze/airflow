from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime , timedelta


default_args = {
    'owner' : 'airflow',
    'depends_on_past' : False,
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=1)
}

with DAG(
    'sql_dag',
    default_args=default_args,
    description='A simple DAG to export data to CSV from SSMS',
    schedule=timedelta(days=1),
    start_date=datetime(2024,4,30),
    catchup = False
) as dag:
    
    run_etl_task = BashOperator(
        task_id="run_etl_task",
        bash_command='bash /home/nithishkumar/scripts/wrapper.sh '
    )