"""
Полигон №1
"""
from datetime import timedelta


def calculate_time(hours_1, minutes_1, hours_2, minutes_2, operator):
    first_window = timedelta(hours=hours_1, minutes=minutes_1)
    second_window = timedelta(hours=hours_2, minutes=minutes_2)
    operator = operator
    return first_window - second_window


if __name__ == '__main__':
    print(calculate_time(10, 20, 12, 00, '-'))
