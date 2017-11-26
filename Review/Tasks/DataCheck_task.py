"""Написать функцию check_my_date, принимающую число месяц и год.
Вернуть True, если такая дата существует и False иначе."""
import time


def check_my_date(date_test):
    try:
        time.strptime(date_test, "%d.%m.%Y")
        return True
    except ValueError:
        return False
