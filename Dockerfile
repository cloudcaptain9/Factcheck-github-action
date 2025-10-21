FROM python:3.11-slim

WORKDIR /app

# Copy and install Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY backend/app.py .

# Copy frontend files
COPY frontend /app/frontend

# Environment variables will be injected at runtime (ECS, docker run, etc.)
# No defaults set - must be provided at runtime
EXPOSE 5000

CMD ["python", "app.py"]
