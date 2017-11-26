import pytest


@pytest.fixture(scope="session", params=["01.12.2010", "7.8.1999", "28.02.2005", "29.2.2000"])
def valid_date(request):
    return request.param


@pytest.fixture(scope="session", params=["-10.10.2000", "32.05.1997", "29.2.1999", "2.2.99"])
def invalid_date(request):
    return request.param
