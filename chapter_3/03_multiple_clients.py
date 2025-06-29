import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)  # this is True by default, making the socket blocking

connections: list[socket.socket] = []

try:
    conn, client_address = server_socket.accept()
    print(f"Incoming connection from address {client_address}:\n{conn}")
    conn.setblocking(False)  # the client socket must also be unblocked
    connections.append(conn)

    for connection in connections:
        try:
            buffer = b""

            while buffer[-2:] != b"\r\n":
                data = connection.recv(2)
                if not data:
                    break
                else:
                    print(f"Received piece of data: {data}")
                    buffer += data
                    print(f"This is the buffer so far: {buffer}")
            print(f"Data received: {buffer}")
            connection.send(buffer)
        except BlockingIOError:
            pass
finally:
    server_socket.close()

# this first approach works correctly for concurrent users, but is not the best practice
# code quality and raising exceptions constantly
# resource cost is higher than necessary, operating at roughly 100% CPU usage constantly