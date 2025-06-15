# syntax=docker/dockerfile:1
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    GUNICORN_CMD_ARGS="--bind 0.0.0.0:8000 --workers 3"

# --- security: non-root user ---
RUN adduser --disabled-password --gecos "" appuser
WORKDIR /app

# --- install deps ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- copy source & fix perms ---
COPY . .
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["gunicorn", "main:app"]
