FROM python:3
WORKDIR /flight-analysis-app
COPY . /flight-analysis-app
RUN pip install -r requirements.txt
EXPOSE 5000
RUN flask run