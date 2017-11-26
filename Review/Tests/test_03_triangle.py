import Tasks.Triangle_task


def test_01_fullset_for_isosceles_triangle():
    my_triangle = Tasks.Triangle_task.Triangle(7, 7, 10)
    assert my_triangle.triangle_perimeter() == 24
    assert my_triangle.triangle_square() == 24.49
    assert my_triangle.triangle_type() == "Треугольник равнобедренный"


def test_02_fullset_for_equalsided_triangle():
    my_triangle = Tasks.Triangle_task.Triangle(13.0, 13.0, 13.0)
    assert my_triangle.triangle_perimeter() == 39.0
    assert my_triangle.triangle_square() == 73.18
    assert my_triangle.triangle_type() == "Треугольник равностронний"


def test_03_fullset_for_rightangled_triangle():
    my_triangle = Tasks.Triangle_task.Triangle(3, 4, 5)
    assert my_triangle.triangle_perimeter() == 12
    assert my_triangle.triangle_square() == 6
    assert my_triangle.triangle_type() == "Треугольник прямоугольный"


def test_04_fullset_for_random_triangle():
    my_triangle = Tasks.Triangle_task.Triangle(7.5, 7, 10)
    assert my_triangle.triangle_perimeter() == 24.5
    assert my_triangle.triangle_square() == 26.22
    assert my_triangle.triangle_type() == "Треугольник разносторонний"


def test_05_unexisted_triangle_error():
    my_triangle = Tasks.Triangle_task.Triangle(3, 1, 6)
    assert my_triangle.is_exist is False


def test_06_unexisted_triangle_negative_value():
    my_triangle = Tasks.Triangle_task.Triangle(3, -3, 6)
    assert my_triangle.is_exist is False