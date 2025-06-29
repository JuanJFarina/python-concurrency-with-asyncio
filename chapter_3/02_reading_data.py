import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f"Incoming connection from address {client_address}:\n{connection}")

    buffer = b""

    while buffer[-2:] != b"\r\n":
        data = connection.recv(2)  # read data using a buffsize of 2 bytes
        if not data:
            break
        else:
            print(f"Received piece of data: {data}")
            buffer += data
            print(f"This is the buffer so far: {buffer}")
    print(f"Data received: {buffer}")
    connection.sendall(buffer)  # send data to the client's socket
finally:
    server_socket.close()

# you can try connecting to this socket via telnet or similar applications