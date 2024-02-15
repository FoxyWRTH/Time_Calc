"""
Декораторы.
"""
from datetime import timedelta as td


def decorator_minus_40_minutes(time_calc_func):
    """
    Декоратор для конфигурации основной функции. |
    Результатом является время которое нужно установить в TL при пересадке.
    :param time_calc_func: Функция возвращает кортеж.
     Нулевой индекс даёт лишь разницу в UTC между городом вылета и Москвой.
    :return: Возвращает готовое значение для TL при пересадке.
    """

    def wrapper():
        minus_40_minutes = td(minutes=40)
        result = time_calc_func[0] - minus_40_minutes
        return result

    return wrapper()


def decorator_minus_36_hours(time_calc_func):
    """
    Декоратор для конфигурации основной функции. |
    Результатом является крайнее время для заявки на провоз спецоборудования.
    :param time_calc_func: Функция возвращает кортеж.
     Нулевой индекс даёт лишь разницу в UTC между городом вылета и Москвой.
    :return: Возвращает крайнее время по МСК для подачи заявки.
    """

    def wrapper():
        minus_36_hours = td(hours=36)
        result = time_calc_func[0] - minus_36_hours
        return result

    return wrapper()


def decorator_visual(result_function):
    def wrapper(*args):
        func_result = result_function(*args)
        print('-' * len(func_result))
        print(func_result)
        print('-' * len(func_result))
        return func_result

    return wrapper


if __name__ == '__main__':
    pass
