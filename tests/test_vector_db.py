# Import the standard socket module to test direct TCP network connectivity
import socket
# Import pytest to define automated tetst cases
import pytest

# Define a test case to verify that the PostgreSQl port is open and accepting connections
def test_pgvector_port_open():
    # Create an IPv4 TCP socket connection object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set a 2-second timeout so the test fails fast if the container is down
    client_socket.settimeout(2.0)
    # Attempt to connect to localhost on port 5432
    result = client_socket.connect_ex(("127.0.0.1", 5432))
    # Close the socket connection after the attempt
    client_socket.close()
    # Assert that the return code is 0 (0 indicates a succesful connection)
    assert result == 0, "PostgreSQl/pgvector container is not reachable on port 5432"