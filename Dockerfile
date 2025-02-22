FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies, curl, and procps (for ps command)
RUN apt-get update && apt-get install -y curl procps && \
    pip install -r requirements.txt

CMD ["python", "-u", "main.py"]
