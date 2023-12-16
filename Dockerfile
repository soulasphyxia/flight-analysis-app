FROM python:3
WORKDIR /flight-analysis-app

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

ENV FLASK_APP app.py

RUN chown -R app:app ./

EXPOSE 5000
RUN flask run