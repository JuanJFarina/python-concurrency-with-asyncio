import asyncio
from asyncio import AbstractEventLoop
import socket
import logging
import signal


async def echo(connection: socket.socket, loop: AbstractEventLoop) -> None:
    buffer = b""
    try:
        while data := await loop.sock_recv(connection, 1024):
            print(f"Got data: {data}")
            if buffer == b"boom":
                print("Unexpected network error")
                break
            if data == b"\r\n":
                print("Sending data")
                await loop.sock_sendall(connection, data+buffer+data)
                buffer = b""
                continue
            buffer += data
    except Exception as e:
        logging.exception(e)
    finally:
        connection.close()


echo_tasks = []


async def connection_listener(server_socket, loop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"New connection from {address}")
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)


class GracefulExit(SystemExit):
    pass


def shutdown():
    raise GracefulExit()


async def close_echo_tasks(echo_tasks: list[asyncio.Task]) -> None:
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    print(f"Waiting for {len(waiters)} echo tasks to finish")
    for task in waiters:
        try:
            await task
        except asyncio.TimeoutError:
            pass


async def main():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    # for signame in {"SIGINT", "SIGTERM"}:
    #     loop.add_signal_handler(
    #         getattr(signal, signame), shutdown
    #     )  # this only works in Unix-based systems
    await connection_listener(server_socket, loop)


loop = asyncio.new_event_loop()

### Ootional work to make a similar behavior in Windows


def raise_graceful_exit(*args):
    loop = asyncio.get_event_loop()
    print("Got a SIGINT or SIGTERM")
    loop.stop()
    raise GracefulExit("Exiting gracefully")


signal.signal(signal.SIGINT, raise_graceful_exit)  # this works in Windows
signal.signal(signal.SIGTERM, raise_graceful_exit)  # this works in Windows

###

try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()
