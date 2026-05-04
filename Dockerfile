FROM python:3.13.7-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y gcc libffi-dev && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

COPY backend /app/backend
COPY db /app/db

EXPOSE 5000

WORKDIR /app/backend

# Seed initial user then start the server
CMD ["uvicorn", "main:app" , "--host", "0.0.0.0", "--port", "5000"]
