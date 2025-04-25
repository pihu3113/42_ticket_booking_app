# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app/ticket_booking_system

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/ticket_booking_system/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/ticket_booking_system/

# Collect static files (optional, for production)
RUN python manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "ticket_booking_system.wsgi:application", "--bind", "0.0.0.0:8000"] 