# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the PyWebIO app will run on
EXPOSE 8080

# Define the command to run the app
CMD ["python", "-m", "run", "your_script_name.py", "--host=0.0.0.0", "--port=8080"]
