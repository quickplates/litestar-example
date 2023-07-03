from litestar import Router

from litestar_example.api.routes.controller import Controller as RootController

router = Router(
    path="/",
    route_handlers=[
        RootController,
    ],
)
