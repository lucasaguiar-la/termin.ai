FROM python:3.11-slim

RUN apt-get update && apt-get install -y build-essential git curl

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app /app/app
COPY llama.cpp /app/llama
COPY model /app/models

WORKDIR /app/llama
RUN make

WORKDIR /app
CMD ['uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '8000']
