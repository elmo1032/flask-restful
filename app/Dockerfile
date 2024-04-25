# Use the official Python 3.9 as the base image for the builder stage
FROM python:3.9-slim-buster AS builder-image

# Set the environment variable to noninteractive to avoid user prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package lists and install necessary packages, then clean up the apt cache
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment using python3.9 and the final folder name to avoid path issues with packages
WORKDIR /app
RUN python3.9 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Install the required packages from the requirements.txt file
COPY --chown=myuser:myuser requirements.txt .
RUN pip install --no-cache-dir wheel  # Install wheel package for efficient package installation
RUN pip install --no-cache-dir -r requirements.txt  # Install required packages

# Use the official Python 3.9 as the base image for the runner stage
FROM python:3.9-slim-buster AS runner-image

# Create a new user named myuser and set up the virtual environment
RUN useradd --create-home myuser
COPY --from=builder-image /app/venv /app/venv  # Copy the virtual environment from the builder stage

# Set the user to myuser and switch to the working directory
USER myuser
WORKDIR /app/code

# Copy the current directory (containing the application code) to the working directory
COPY --chown=myuser:myuser . .

# Expose port 5000 for the application
EXPOSE 5000

# Set the command to run the application
CMD ["python", "app.py"]
