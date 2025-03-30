# syntax=docker/dockerfile:1
FROM ubuntu:22.04
WORKDIR /usr/src/portfolio-app

COPY /app.py ./
COPY /static ./static
COPY /templates ./templates
COPY /requirements.txt ./

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt

ENV LANG C.UTF-8
ENV FLASK_APP=app
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]