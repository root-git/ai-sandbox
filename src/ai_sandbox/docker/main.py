import sys # Import sys module to inspect runtime Python interpreter properties

def get_runtime_info() -> dict: # Define helper function to return runtime details
    # Return dictionary containing current Python path and executable location
    return {
        "executable": sys.executable, # Capture location of running Python binary
        "status": "healthy", # Set health status for container healthchecks
    }

if __name__ == "__main__": # Ensure script runs directly as entrypoint
    # Print execution confirmation message to standard output
    print(f"Container running with executable: {get_runtime_info()['executable']}")