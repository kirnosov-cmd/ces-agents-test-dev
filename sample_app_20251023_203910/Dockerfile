# Use an official Python runtime as a parent image
FROM python:3.11-slim


# Set the working directory to /app
WORKDIR /app

# Install git and wget (required for pip install git+... and downloading CES lib)
RUN apt-get update && apt-get install -y git wget && rm -rf /var/lib/apt/lists/*

# Install CES Client Library (Pre-requisite) - Cached Layer
RUN wget https://storage.googleapis.com/gassets-api-ai/ces-client-libraries/v1beta/ces-v1beta-py.tar && \
    pip install ces-v1beta-py.tar --quiet && \
    rm ces-v1beta-py.tar

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies - Cached Layer
RUN pip install --no-cache-dir -r requirements.txt

# Copy the agent code into the container
COPY . .

# Set the entrypoint to cxas-scrapi
ENTRYPOINT ["cxas-eval"]
