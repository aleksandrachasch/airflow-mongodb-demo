# Подключение к MongoDB из Airflow

Данный DAG выполняет поиск одного документа из коллекции `students` в MongoDB.

## Запуск MongoDB

```shell
docker pull mongo

docker run -d --name "my-mongodb-container" 
-p 27017:27017 
-e MONGO_INITDB_ROOT_USERNAME=admin 
-e MONGO_INITDB_ROOT_PASSWORD=password mongo
```

Далее необходимо создать базу данных `myDB` и коллекцию `students`. Загрузить данные в коллекцию.

## Запуск Airflow

```shell
git clone https://github.com/aleksandrachasch/airflow-mongodb-demo.git
cd airflow-mongodb-demo
docker build . -f Dockerfile --pull --tag airflow-mongo:0.0.1
docker-compose up
```
## Создание подключения (connection)

1. Открыть в браузере Airflow UI: http://localhost:8080/
2. В меню выбрать `Admin > Connections > Create`
3. Заполнить поля:
    1. Connection Id: `local_mongoDB`
    2. Connection Type: `MongoDB`
    3. Host: `host.docker.internal`
    4. Login: `admin`
    5. Password: `password`
    6. Port: `27017`
5. Нажать на `Create`

## Запустить DAG

Запустить DAG и проверить логи - в них должен быть напечатан документ из коллекции `students`
