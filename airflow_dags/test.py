# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


NUMBER_DUMMY_TASKS = 5  # number of dummy task of the part 3

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}
dag = DAG(
    'test',
    default_args=default_args,
    schedule_interval='0 3 * * *'
)

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)


# create the N dummy tasks
dummy_tasks_pair = []
dummy_tasks_odd = []

for n in range(NUMBER_DUMMY_TASKS):
    task = DummyOperator(task_id=f'task_{n}', dag=dag)
    if (n % 2) == 0:
        dummy_tasks_pair.append(task)
    else:
        dummy_tasks_odd.append(task)

# create the dependencies
start >> end

for odd_task in dummy_tasks_odd:
    odd_task >> dummy_tasks_pair
