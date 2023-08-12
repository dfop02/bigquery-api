# Block any external connection in tests
import socket
from ipaddress import ip_address
import pytest

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
        user_ip = address
    elif len(address) == 2:
        # AF_INET
        user_ip, _port = address
    else:
        # AF_INET6
        user_ip, _port, _, _ = address

    if ip_address(user_ip).is_private:
        return _original_connect(*args, **kwargs)

    pytest.fail("Public network request detected")
    return None
