# Stage 1: Buiild stage using python 3.11 slim base image
From python:3.11-slim As builder # Define the builder stage with an alias

# Set the working directory inside the builder container
WORKDIR /app # Create and set /app as the active working directory

# Install uv package manager to handle fast dependency installation
RUN pip install uv # Use pip to install uv in the builder stage

# Copy dependency definition files to leverage Docker layer caching
COPY pyproject.toml . # Copy the pyproject configuration file to current WORKDIR

# Install packages into the target virtual environment using the builder stage
RUN uv venv /app/.venv && uv pip install --python /app/.venv -r pyproject.toml # Target the created virtual environment explicitly

# Stage 2: Final runtime stage using a clean python 3.11 slim image
FROM python:3.11-slim AS runner # Start a fresh stage to discard build-time tools

# Set the working directory for the runtime container
WORKDIR /app # Set /app as the runtime working directory

# Copy the pre-built virtual environment from the 'builder' stage into the 'runner' stage
COPY --from=builder /app/.venv /app/.venv # Transfer only compiled dependencies from stage 1

# Copy the application source code into the runtime container
COPY src/ /app/src/ # Copy application files into the src directory inside the container

# Ensure Python utilizes the dependencies installed in the virtual environment
ENV PATH="/app.venv/bin:$PATH" # Prepend the virtual environment bin path to system PATH

# Set the default command to execute the main application 
CMD ["python", "src/ai_sandbox/docker/main.py"] # Execute main script on container start