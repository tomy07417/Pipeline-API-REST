FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

VOLUME ["/app/output"]

CMD ["python", "etl-API.py"]