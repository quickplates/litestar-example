from litestar_example.foo import foo


def test_foo():
    """Test if foo returns bar."""

    assert foo() == "bar"
