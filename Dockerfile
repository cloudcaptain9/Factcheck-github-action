FROM python:3.11-slim

WORKDIR /app

# Copy and install Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY backend/app.py .
COPY backend/.env .

# Copy frontend files to the location Flask expects
COPY frontend /app/frontend

EXPOSE 5000

CMD ["python", "app.py"]
