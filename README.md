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
export DB_NAME=${DB_NAME}
export DB_USER=${DB_USER}
export DB_PASSWORD=${DB_PASSWORD}
export DB_HOST=${DB_HOST}
export DB_PORT=${DB_PORT}
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
docker build . -t {IMAGE_NAME}
```

### To run image

```shell
docker run \
    --env DB_NAME={DB_NAME} \
    --env DB_USER={DB_USER} \
    --env DB_PASSWORD={DB_PASSWORD} \
    --env DB_HOST={DB_HOST} -p :$PORT --name {CONTAINER_NAME} {IMAGE_NAME}
```
