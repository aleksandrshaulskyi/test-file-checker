FROM python:3.14

WORKDIR /checker-backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
