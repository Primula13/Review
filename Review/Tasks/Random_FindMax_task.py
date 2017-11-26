"""Сгенерировать массив из задачи b. Найти 2 максимальных элемента данного массива. Элементы не должны быть равны."""
from random import randint


def find_max_from_random():
    random_list = [randint(-1000, 1000) for _ in range(1000)]
    remove_doubles = set(random_list)
    find_max = sorted(list(remove_doubles), reverse=True)
    return random_list, find_max[0:2]
