import Tasks.Triangle_task


def test_01_fullset_for_triangle(triangles):
    my_triangle = Tasks.Triangle_task.Triangle(triangles["side1"], triangles["side2"], triangles["side3"])
    assert my_triangle.triangle_perimeter() == triangles["perimeter"]
    assert my_triangle.triangle_square() == triangles["square"]
    assert my_triangle.triangle_type() == triangles["type"]


def test_03_unexisted_triangle_error():
    my_triangle = Tasks.Triangle_task.Triangle(3, 1, 6)
    assert my_triangle.is_exist is False


def test_04_unexisted_triangle_negative_value():
    my_triangle = Tasks.Triangle_task.Triangle(3, -3, 6)
    assert my_triangle.is_exist is False
