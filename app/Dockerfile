# Use the LTS version of Ubuntu as the base image for the builder stage
FROM ubuntu:20.04 AS builder-image

# Set the DEBIAN_FRONTEND environment variable to noninteractive to avoid any user prompts during package installation
ARG DEBIAN_FRONTEND=noninteractive

# Update the package lists and install necessary packages, then clean up the apt cache
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment using python3.9 and the final folder name to avoid path issues with packages
RUN python3.9 -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

# Install the required packages from the requirements.txt file
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

# Use the LTS version of Ubuntu as the base image for the runner stage
FROM ubuntu:20.04 AS runner-image

# Install necessary packages, then clean up the apt cache
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3.9 python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a new user named myuser and set up the virtual environment
RUN useradd --create-home myuser
COPY --from=builder-image /home/myuser/venv /home/myuser/venv

# Set the user to myuser and switch to the working directory
USER myuser
RUN mkdir /home/myuser/code
WORKDIR /home/myuser/code/app
COPY . .

# Expose port 5000 for the application
EXPOSE 500
