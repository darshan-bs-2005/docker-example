# Use an official lightweight Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose the port your Flask app runs on (default is 5000)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
