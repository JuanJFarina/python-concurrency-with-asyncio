import socket

server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # creates the socket object
# we pass the socket domain (address family), and also the socket type:
# A pair (host, port) is used for the AF_INET address family, where host is a string
# representing either a hostname in internet domain notation like 'daring.cwi.nl' or an
# IPv4 address like '100.50.200.5', and port is an integer.
# Socket type SOCK_STREAM indicates we will use the TCP protocol for communication
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# the setsockopt() method allows you to set different configurations as constant integers
# SO_REUSEADDR allows us to reuse the same port when restarting the server, otherwise
# the system could not unbind the socket and we may get an error

# for more information on sockets, go to the official documentation at:
# https://docs.python.org/3/library/socket.html

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)  # we bind the socket to the address
server_socket.listen()  # we enable listening to incoming requests
connection, client_address = server_socket.accept()  # wait for a connection with a client

print(f"Incoming connection from address {client_address}:\n{connection}")

# running this code will establish a local server which you can attempt to connect to 
# using your web browser. The server won't respond with any data, but you will see the 
# print message in the terminal.