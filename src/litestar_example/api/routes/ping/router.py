from litestar import Router

from litestar_example.api.routes.ping.controller import Controller

router = Router(
    path="/ping",
    tags=["Ping"],
    route_handlers=[
        Controller,
    ],
)
