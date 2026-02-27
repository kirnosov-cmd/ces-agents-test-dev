# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Install git and wget (required for pip install git+... and downloading CES lib)
RUN apt-get update && apt-get install -y git wget && rm -rf /var/lib/apt/lists/*

# Copy the agent code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install CES Client Library (Pre-requisite)
RUN wget https://storage.googleapis.com/gassets-api-ai/ces-client-libraries/v1beta/ces-v1beta-py.tar && \
    pip install ces-v1beta-py.tar --quiet

# Install cxas-scrapi (assuming standard PyPI or internal repo, adjust as needed)
# For now, we install from the public PyPI or a known location if provided in requirements.txt
# If not in requirements.txt, you might want to add it here explicitly:
# RUN pip install cxas-scrapi

# Entry point for the agent (adjustable)
ENTRYPOINT ["cxas-eval"]
