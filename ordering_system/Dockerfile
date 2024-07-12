FROM python:3.11

WORKDIR /code

COPY ./app /code/app
COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install Pyrebase4
RUN pip install -r /code/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9981"]
