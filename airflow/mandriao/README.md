# README
# Apache Airflow Tutorial

# How to install 


Create, and start a virtual environment, then:

```{python}
pip install apache-airflow
```


# How to configure

In your terminal emulator, run:

```
airflow db init
airflow users create --username admin --password admin --firstname YourName --lastname Admin --role Admin --email admin@example.org
```

# DAG writing

Stop here, time to write our first DAG.

We need to point a folder where we placed our DAGs.

To validate our DAG, run ```airflow init db```


# Run webserver and scheduler

```
airflow webserver 
airflow scheduler
```
