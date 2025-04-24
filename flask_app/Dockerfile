# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN apt-get update && apt-get install -y curl \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=development

# Expose port and run app
EXPOSE 5000
CMD ["python", "app.py"]

