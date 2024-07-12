# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables to prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Copy the requirements.txt file into the container
ADD . /streamlit
WORKDIR /streamlit
COPY ../requirements.txt /streamlit/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt



# Expose the port the app runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "streamlit.py"]
