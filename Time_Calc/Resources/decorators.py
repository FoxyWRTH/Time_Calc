"""
Декораторы. Относятся к версии 1.4
"""
from datetime import timedelta as td
from time import perf_counter_ns


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


def decorator_debug(func):
    def wrapper(*args, **kwargs):
        func_start_time = perf_counter_ns()
        func_result = func(*args, **kwargs)
        func_stop_time = perf_counter_ns()
        func_worktime = func_stop_time - func_start_time
        print(f'{'-' * 14} Debug Result {'-' * 14}\n'
              f'func name is: {func.__name__}\n'
              f'func_args: {args}\n'
              f'func_kwargs {kwargs}\n'
              f'func_result is: {func_result}\n'
              f'func_result_type_is: {type(func_result)}\n'
              f'func time is: {func_worktime} nanoseconds\n'
              f'func time is: {func_worktime / 10 ** 9} seconds\n'
              f'{'-' * 14} End of Debug {'-' * 14}')
        return func_result

    return wrapper


if __name__ == '__main__':
    pass
