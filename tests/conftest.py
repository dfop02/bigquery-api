# Block any external connection in tests
import socket, pytest
from ipaddress import ip_address

_original_connect = socket.socket.connect

@pytest.fixture(autouse=True)
def disable_network():
    socket.socket.connect = patched_connect
    yield
    socket.socket.connect = _original_connect

def patched_connect(*args, **kwargs):
    address = args[1]

    if isinstance(address, str):
        # AF_UNIX
        ip = address
    elif len(address) == 2:
        # AF_INET
        ip, port = address
    else:
        # AF_INET6
        ip, port, _, _ = address

    if ip_address(ip).is_private:
        return _original_connect(*args, **kwargs)

    pytest.fail("Public network request detected")
