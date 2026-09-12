FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY alpha.py .
COPY FuelConsumptionCo2.csv .

CMD ["python", "alpha.py"]