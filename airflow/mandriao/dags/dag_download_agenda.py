#%%
from datetime import datetime, timedelta

# Need to instatiate a DAG 
from airflow import DAG

# Operators (Tasks)
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

#%%
from utils import download_all_agenda, process_working_hours
#%%

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}


# Create DAG
with DAG(
        'tutorial_president_agenda',
        default_args=default_args,
        description="Downloads president's agenda",
        schedule_interval=timedelta(days=1),
        start_date=days_ago(10),
        ) as dag:

    t1 = PythonOperator(
            task_id="download_all_agenda",
            python_callable=download_all_agenda,
            op_kwargs={'start_date': '2021-05-01'}
            )

    t2 = PythonOperator(
            task_id="process_working_hours",
            python_callable=process_working_hours
            )

    t1 >> t2


# %%
