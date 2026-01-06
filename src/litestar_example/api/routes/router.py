from litestar import Router

from litestar_example.api.routes.ping.router import router as ping_router
from litestar_example.api.routes.sse.router import router as sse_router

router = Router(
    path="/",
    route_handlers=[
        ping_router,
        sse_router,
    ],
)
