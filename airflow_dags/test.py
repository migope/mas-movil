# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import BaseOperator
from airflow.utils.decorators import apply_defaults

NUMBER_DUMMY_TASKS = 5  # number of dummy task of the part 3


class TimeDiff(BaseOperator):
    
    @apply_defaults
    def __init__(self, diff_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.diff_date = diff_date
    
    def execute(self, context):
        date_difference = datetime.now() - self.diff_date
        print(f"The difference of dates is" +
              f" {date_difference.days} days, {date_difference.seconds} seconds" +
              f" and {date_difference.microseconds} microseconds")


# define the DAG
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

# define the tasks
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

# part 4, time diff 
diff_task = TimeDiff(
        task_id='timediff',
        dag=dag,
        diff_date=datetime(2020, 12, 1)
    )

# create the dependencies
start >> end

for odd_task in dummy_tasks_odd:
    odd_task >> dummy_tasks_pair
