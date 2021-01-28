# HOSPICE

## Create and Activate Virtual Environment

```shell
python3 -m venv venv
source venv/bin/activate
```

## Install dependencies

```shell
pip install -r requirements.txt
```

NOTE: To run api,set the following env variables

```shell
export SECRET_KEY={ANY-STRING-HARD-QUESS}
export DATABASE_URL="./db.sqlite3"
export DEBUG=True #optional
python3 manage.py runserver
```

### **ps: Perform databases migration**

To run application for the first time locally, perform database migration using the commands below at the root folder

```shell
python3 manage.py migrate
```

## **DOCKER**

### To build docker image

```shell
docker build --build-arg DATABASE_URL={SQLITE3_URL} . -t {IMAGE_NAME}
```

### To run image

```shell
docker run --env DATABASE_URL={SQLITE3_URL} --env SECRET_KEY={SECRET_KEY} -p :80 --name {CONTAINER_NAME} {IMAGE_NAME}
```
