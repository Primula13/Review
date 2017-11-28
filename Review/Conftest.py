import pytest


@pytest.fixture(scope="session", params=["01.12.2010", "7.8.1999", "28.02.2005", "29.2.2000"])
def valid_date(request):
    return request.param


@pytest.fixture(scope="session", params=["-10.10.2000", "32.05.1997", "29.2.1999", "2.2.99"])
def invalid_date(request):
    return request.param


@pytest.fixture(scope="session", params=
[
    {
        "side1": 7,
        "side2": 7,
        "side3": 10,
        "perimeter": 24,
        "square": 24.49,
        "type": "Треугольник равнобедренный"
    },
    {
        "side1": 13.0,
        "side2": 13.0,
        "side3": 13.0,
        "perimeter": 39,
        "square": 73.18,
        "type": "Треугольник равностронний"
    },
    {
        "side1": 3,
        "side2": 4,
        "side3": 5,
        "perimeter": 12,
        "square": 6,
        "type": "Треугольник прямоугольный"
    },
    {
        "side1": 7.5,
        "side2": 7,
        "side3": 10,
        "perimeter": 24.5,
        "square": 26.22,
        "type": "Треугольник разносторонний"
    }
])
def triangles(request):
    return request.param
