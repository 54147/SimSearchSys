FROM python:3.10-slim

RUN mkdir -p /usr/src/server/
WORKDIR /usr/src/server

COPY requirements_docker.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "9000"]
