# Import the os module to interact with the underlying operating system environment
import os 
# Import Typing's Optional to handle nullable string return types safely
from typing import Optional

# Define a function to retrieve dynamic application secrets or runtime configuration setting
def get_secret(secret_name: str, default_val: Optional[str] = None ) -> Optional[str]:
    # Fetch the environment variable using the provided key, falling back to default if absent
    secret_value = os.getenv(secret_name, default_val)
    # Return the resolved secret value or None
    return secret_value

# Define a function to generate host and port binding options for server startup
def get_server_config() -> dict[str, int |str]:
    # Read the tarfet PORT environment variable set by GCP Cloud Run / Render runtime, defaulting to 8080
    port = int(os.getenv("PORT", 8080))
    # Return a structured dictionary containing boundd server parameters
    return {"host": "0.0.0.0", "port": port}

