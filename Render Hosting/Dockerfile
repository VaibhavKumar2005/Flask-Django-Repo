# Use a slim Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install ONLY curl for health checks (skipping build-essential)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8000

# Start the app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]