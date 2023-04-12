FROM ubuntu:22.04

COPY . /app
WORKDIR /app
RUN apt update
RUN apt install exiftool python3 python3-pip -y
RUN python3 -m pip install -r requirements.txt


ENTRYPOINT ["gunicorn","--bind","0.0.0.0:5000", "app:gunicorn_app"]

