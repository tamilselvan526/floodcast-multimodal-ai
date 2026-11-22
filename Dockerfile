# Step 1: Base image (lightweight python 3.10 slim)
FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy application code into container
COPY ml_demo.py .

# Step 5: Command to execute ML program
CMD ["python", "ml_demo.py"]
