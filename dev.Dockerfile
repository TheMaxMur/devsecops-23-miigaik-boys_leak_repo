FROM ubuntu:22.04

COPY . /app
WORKDIR /app
RUN apt update
RUN apt install exiftool python3 python3-pip -y
RUN python3 -m pip install -r requirements.txt


ENTRYPOINT ["python3", "app.py"]

