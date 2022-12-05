# syntax=docker/dockerfile:1
FROM ubuntu:20.04
RUN mkdir /output
VOLUME /output
RUN apt update && apt install -y python3 python3-pip
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "/app/xgb_prod_example.py"]