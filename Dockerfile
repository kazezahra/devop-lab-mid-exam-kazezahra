# Use the correct base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the correct port
EXPOSE 5000

# Set the entry point
CMD ["python", "app.py"]
