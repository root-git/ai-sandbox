from ai_sandbox.docker.main import get_runtime_info # Import runtime checker function from docker main script

def test_runtime_info_structure(): # Define unit test for container runtime info payload
    # Execute the runtime info helpfer function
    info = get_runtime_info() # Store dictionary returned by target function

    # Assert executable key is present and is a non-empty string
    assert "executable" in info # Verify required key exists in output dict
    # Assert health status key is returning healthy status
    assert info["status"] == "healthy" # Validate system status value
