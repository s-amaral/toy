FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get -o Acquire::Check-Valid-Until=false \
    -o Acquire::Check-Date=false update \
    && apt-get -y --no-install-recommends install \
    gcc \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    HOST=0.0.0.0 \
    LOG_LEVEL=INFO \
    PYTHONPATH=/app

# Expose ports for HTTP and WebSocket
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Run the application
CMD ["python", "source/main.py"]