import selectors
import socket
from selectors import SelectorKey

selector = selectors.DefaultSelector()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: list[tuple[SelectorKey, int]] = selector.select(timeout=1)

    if len(events) == 0:
        print("No events, waiting for connections...")

    for event, _ in events:
        event_socket = event.fileobj

        if event_socket is server_socket:
            conn, client_address = server_socket.accept()
            conn.setblocking(False)
            print(f"Incoming connection from address {client_address}:\n{conn}")
            selector.register(conn, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f"Received data: {data} from {client_address}")
            event_socket.send(data)

# the selectors module gives us an abstraction over the operating system's
# APIs for monitoring I/O events, allowing us to write non-blocking
# network applications that can handle multiple connections efficiently.
