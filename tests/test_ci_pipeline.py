# Import built-in pathlib module for relative path inspection
from pathlib import Path
# Import PyYAML library to parse and validate YAML file syntax
import yaml

# Define test function to validate GitHub Actions YAML syntax and structure
def test_github_actions_workflow_syntax():
    # Construct relative path to the target workflow YAML file
    workflow_path = Path(".github/workflows/eval.yml")

    # Assert that the workflow configuration file actually exists in repository
    assert workflow_path.exists(), "Workflow file .github/workflows.eval.yml does not exist"

    # Open the workflow YAML file in read mode
    with open(workflow_path, "r", encoding="utf-8") as file_stream:
        # Load and parse the YAML contents safely into a Python dictionary
        workflow_config = yaml.safe_load(file_stream)

    # Assert that top-level name attribute exists in parsed configuration
    assert "name" in workflow_config, "Workflow YAML missing required 'name' field"
    # Assert that trigger 'on' key exists in parsed configuration
    assert "on" in workflow_config, "Workflow YAML missing required 'on' tirgger field"
    # Assert that 'jobs' definition exists in parsed configuration
    assert "jobs" in workflow_config, "Workflow YAML missing required 'jobs' field"