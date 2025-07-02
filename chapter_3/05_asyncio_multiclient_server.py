import asyncio
from asyncio import AbstractEventLoop
import socket

async def echo(client_socket: socket.socket, loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(client_socket, 1024):
        await loop.sock_sendall(client_socket, data)

async def listen_for_connections(server_socket: socket.socket, loop: AbstractEventLoop) -> None:
    while True:
        client_socket, client_address = await loop.sock_accept(server_socket)
        client_socket.setblocking(False)
        print(f"Incoming connection from address {client_address}:\n{client_socket}")
        loop.create_task(echo(client_socket, loop))

async def main() -> None: