from litestar_example.models.base import datamodel


@datamodel
class PingRequest:
    """Request to ping."""

    pass


@datamodel
class PingResponse:
    """Response for ping."""

    pass
