from litestar import Router

from litestar_example.api.routes.root.router import router as root_router

router = Router(
    path="/",
    route_handlers=[
        root_router,
    ],
)
