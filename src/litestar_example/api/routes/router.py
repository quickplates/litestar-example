from litestar import Router

from litestar_example.api.routes.ping.router import router as ping
from litestar_example.api.routes.sse.router import router as sse
from litestar_example.api.routes.test.router import router as test

router = Router(
    path="/",
    route_handlers=[
        ping,
        sse,
        test,
    ],
)
