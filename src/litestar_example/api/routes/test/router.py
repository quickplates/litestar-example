from litestar import Router

from litestar_example.api.routes.test.controller import Controller

router = Router(
    path="/test",
    tags=["Test"],
    route_handlers=[
        Controller,
    ],
)
