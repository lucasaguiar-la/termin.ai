FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    cmake \
    libopenblas-dev \
    libcurl4-openssl-dev

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app /app/app
COPY llama.cpp /app/llama

WORKDIR /app/llama
RUN mkdir -p build && \
    cd build && \
    cmake .. && \
    cmake --build . --config Release

WORKDIR /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

