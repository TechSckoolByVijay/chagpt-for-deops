# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install Flask and any other dependencies
RUN pip install -r requirements.txt

# Expose the port your Flask app will run on
EXPOSE 80

# Define the command to run your Flask app
CMD ["python", "app.py"]
