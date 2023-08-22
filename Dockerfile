# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port for the application
EXPOSE 8000

# Run the command to start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]