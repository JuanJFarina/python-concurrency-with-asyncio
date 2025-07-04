from aiohttp import web
from datetime import datetime
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncio import sleep as async_sleep
from time import sleep as sync_sleep

routes = web.RouteTableDef()


@routes.get("/time")
async def time(request: Request) -> Response:
    print(request.headers)
    print("Sleeping for 2 seconds...")
    # sync_sleep(2)  # this is blocking
    await async_sleep(2)  # this is non-blocking
    today = datetime.today()
    response: dict[str, int | str] = {
        "month": today.month,
        "day": today.day,
        "time": str(today.time()),
    }
    return web.json_response(response)


app = web.Application()
app.add_routes(routes)
web.run_app(app)

# This can be tried out by sharing the local IP to persons using the same wifi
# network, and even on concurrent requests, they should all take roughly 2
# seconds to complete.
