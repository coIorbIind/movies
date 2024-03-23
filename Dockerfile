FROM python:3.10

RUN mkdir /app
WORKDIR /app


COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


COPY ./manage.py ./manage.py
COPY ./movies ./movies
COPY ./movies_app ./movies_app
COPY ./.env ./.env

CMD python manage.py runserver 0.0.0.0:8000
