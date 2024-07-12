# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables to prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Copy the requirements.txt file into the container
ADD . /app
WORKDIR /app
COPY ../requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
#CMD ["python", "app.py"]
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]