from litestar import Router

from litestar_example.api.routes.sse.controller import Controller

router = Router(
    path="/sse",
    tags=["SSE"],
    route_handlers=[
        Controller,
    ],
)
