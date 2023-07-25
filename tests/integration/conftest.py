import pytest
from litestar.testing import AsyncTestClient

from litestar_example.api import AppBuilder
from litestar_example.config import ConfigBuilder


@pytest.fixture(scope="session")
def client() -> AsyncTestClient:
    """Reusable test client."""

    config = ConfigBuilder().build()
    app = AppBuilder(config).build()
    return AsyncTestClient(app=app)
