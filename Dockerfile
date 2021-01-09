FROM python:3.7.3-slim-stretch

WORKDIR /app

COPY ./ ./
COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

ENTRYPOINT [ "python", "glvar" ]