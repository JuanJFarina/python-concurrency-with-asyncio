import asyncio
from asyncio import AbstractEventLoop
import socket


async def echo(client_socket: socket.socket, loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(client_socket, 1024):
            if data == b"boom":
                raise Exception("Simulated error for testing")
            await loop.sock_sendall(client_socket, data)
    except Exception as e:
        print(f"Error during communication with client: {e}")
    finally:
        client_socket.close()


async def listen_for_connections(
    server_socket: socket.socket, loop: AbstractEventLoop
) -> None:
    while True:
        client_socket, client_address = await loop.sock_accept(server_socket)
        client_socket.setblocking(False)
        print(f"Incoming connection from address {client_address}:\n{client_socket}")
        loop.create_task(echo(client_socket, loop))


async def main() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connections(server_socket, asyncio.get_event_loop())


asyncio.run(main())
