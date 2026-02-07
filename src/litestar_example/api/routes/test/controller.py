from collections.abc import Mapping
from typing import Annotated

from litestar import Controller as BaseController
from litestar import handlers
from litestar.di import Provide
from litestar.params import Parameter
from litestar.response import Response

from litestar_example.api.exceptions import BadRequestException
from litestar_example.api.routes.test import errors as e
from litestar_example.api.routes.test import models as m
from litestar_example.api.routes.test.service import Service
from litestar_example.models.base import Jsonable, Serializable
from litestar_example.services.test.service import TestService


class DependenciesBuilder:
    """Builder for the dependencies of the controller."""

    async def _build_service(self) -> Service:
        return Service(test=TestService())

    def build(self) -> Mapping[str, Provide]:
        """Build the dependencies."""
        return {
            "service": Provide(self._build_service),
        }


class Controller(BaseController):
    """Controller for the test endpoint."""

    dependencies = DependenciesBuilder().build()

    @handlers.get(
        summary="Test",
    )
    async def test(
        self,
        service: Service,
        parameters: Annotated[
            Jsonable[m.TestRequestParameters] | None,
            Parameter(
                description="Parameters for testing.",
            ),
        ] = None,
    ) -> Response[Serializable[m.TestResponseResult]]:
        """Test."""
        request = m.TestRequest(parameters=parameters.root if parameters else None)

        try:
            response = await service.test(request)
        except e.ValidationError as ex:
            raise BadRequestException(extra=[str(ex)]) from ex

        return Response(Serializable(response.result))
