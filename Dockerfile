FROM python:3.8
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app/src
CMD gunicorn app.wsgi:application --bind 0.0.0.0:8000