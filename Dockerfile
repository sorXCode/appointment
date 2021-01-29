FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE $PORT
CMD python3 manage.py migrate && gunicorn hospice.wsgi -b :$PORT --log-level debug