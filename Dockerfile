From python:3.10

COPY Pipfile.lock ./
COPY Pipfile ./

RUN pip install pipenv\
    && pipenv install --system --deploy --ignore-pipfile

COPY . .

ENTRYPOINT FLASK_APP=./app.py flask run
