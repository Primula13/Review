"""Создать массив из 1000 элементов и рандомно заполнить его числами от -1000 до 1000.
Найти среднее арифметическое всех элементов. Создать другой массив и записать в него все элементы,
которые на +- 20 % отличаются от среднего."""
from random import randint


def find_average_from_random_create_new_list():
    random_list = [randint(-1000, 1000) for _ in range(1000)]
    average = sum(random_list)/len(random_list)
    print(average)
    if average > 0:
        new_list = [x for x in range(int(average * 0.8), int(average * 1.2 + 1))]
        print(new_list)
    elif average <= 0:
        new_list = [x for x in range(int(average * 1.2), int(average * 0.8 + 1))]
        print(new_list)