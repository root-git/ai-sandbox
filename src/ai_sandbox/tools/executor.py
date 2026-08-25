# Import json module to parse incoming string arguments from the tool call
import json
# Import Any and Callable from typing to type-hint parameters and returns
from typing import Any, Callable
# Import BaseModel from pydantic for schema validation
from pydantic import BaseModel

# Define the function execution loop function signature
def execute_tool_call(tool_call: Any, tools_map: dic[str, Callable]) -> str:
    # Extract the tool name requested by the model
    func_name = tool_call.function.name
    # Extract the raw JSON string arguments provided by the model
    raw_args = tool_call.function.arguments 

    # Retrieve the target tool function from the execution map
    target_func = tools_map[func_name]

    # Parse the raw JSON arguments string into a Python dictionary
    parsed_args = json.loads(raw_args)

    # Execute the target function using unpacked kayword arguments and return the result
    return str(target_func(**parsed_args))



