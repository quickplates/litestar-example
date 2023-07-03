from litestar import Controller as BaseController
from litestar import Response, get

from litestar_example.api.routes.models import GetResponse
from litestar_example.foo import foo


class Controller(BaseController):
    """Root controller."""

    @get(
        summary="GET example",
        description="Example endpoint that showcases a GET request",
    )
    async def get(self) -> Response[GetResponse]:
        content = GetResponse(foo=foo())
        return Response(content)
