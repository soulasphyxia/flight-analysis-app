FROM python:3
WORKDIR /hackaton_web
COPY . /hackaton_web
RUN pip install -r requirements.txt
EXPOSE 5000
RUN ["flask", "run"]