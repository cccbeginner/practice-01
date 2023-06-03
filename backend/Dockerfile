# Use the official Python base image with Python 3.8
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files to the container
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev

# Install Poetry package manager
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --only main

# Run Alembic migrations
#RUN poetry run alembic upgrade head

# Expose the port on which your backend server runs (adjust if necessary)
EXPOSE 8000

# Start the backend server
CMD poetry run alembic upgrade head && poetry run uvicorn main:app --host 0.0.0.0 --port 8000