# Step 1: Base image
FROM python:3.10

# Step 2: Set working directory
WORKDIR /app

# Step 3: Install required ML libraries
RUN pip install numpy pandas scikit-learn matplotlib

# Step 4: Copy application code into container
COPY ml_demo.py .

# Step 5: Command to execute ML program
CMD ["python", "ml_demo.py"]
