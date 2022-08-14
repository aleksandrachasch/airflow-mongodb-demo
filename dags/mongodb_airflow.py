
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from airflow.providers.mongo.hooks.mongo import MongoHook

from datetime import datetime, timedelta  

###########################################
# DEFINE AIRFLOW DAG (SETTINGS + SCHEDULE)
############################################
default_args = {
     'owner': 'airflow',
     'depends_on_past': False,
     'email': ['user@gmail.com'],
     'email_on_failure': False,
     'email_on_retry': False,
    }

dag = DAG( 'demo_mongodb_airflow_get_document',
            default_args=default_args,
            description='Get a document from students collection in MongoDB',
            catchup=False, 
            start_date= datetime(2022, 8, 13), 
            schedule_interval=timedelta(hours=3)
          )  

####################################################
# DEFINE PYTHON FUNCTIONS
####################################################


def load_data(**kwargs):

    mongohook = MongoHook(conn_id = "local_mongoDB")

    studentsCollection = mongohook.get_collection(mongo_collection = "students",
                                                 mongo_db = "myDB")
    doc = studentsCollection.find_one()
    print(doc)



##########################################
# DEFINE AIRFLOW OPERATORS
##########################################


get_document_from_mongo_task =  PythonOperator(task_id='get_document_from_mongo_task',
                                   provide_context=True,
                                   python_callable=load_data,
                                   dag=dag)

get_document_from_mongo_task
