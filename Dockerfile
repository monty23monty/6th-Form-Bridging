FROM ubuntu:latest
LABEL authors="leohe"

ENTRYPOINT ["top", "-b"]

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to prevent Python from buffering outputs
ENV PYTHONUNBUFFERED=1

# Run the Flask app
CMD ["python", "app.py"]
