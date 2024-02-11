"""
Калькулятор времени.
"""
from datetime import timedelta as td
import EDUCATION.Time_Calc.city_database as cd
import EDUCATION.Time_Calc.decorators as decor


def calc_difference_between_utc_and_telegram_time(time, city='SVO', svo=3):
    """
    Функция считает разницу по UTC между городом который передаётся в функцию и Москвой,
    тем самым получаем время Москвы относительно времени переданного города.
    :param time: Местное время вылета.
    :param city: Город вылета.
    :param svo: UTC москвы (Константа)
    :return: Кортеж(Время в москве с учётом разницы UTC | Локальное время из телеграммы)
    """
    hours = int(time[:2])
    minutes = int(time[2:])
    input_time = td(hours=hours, minutes=minutes)

    difference_between_utc = (input_time
                              - (td(hours=cd.city_database.get(city)[1],
                                    minutes=cd.city_database.get(city)[2])
                                 - td(hours=svo)))
    telegram_time = input_time + td(hours=cd.city_database.get(city)[1],
                                    minutes=cd.city_database.get(city)[2])

    result_1 = difference_between_utc
    result_2 = telegram_time
    return result_1, result_2


def func_filter(time, city):
    """
    Функция подводит общий итог:
    Время которое нужно установить в TL при пересадке. |
    Крайнее время для заявки на провоз спецоборудования. |
    Локальное время вылета, относительно времени в телеграмме. |
    Так же в этой функции внедрены проверки на корректность ввода данных в функцию. |
    :param time: Местное время вылета.
    :param city: Город вылета.
    :return:
    """
    time = str(time)
    city = city.upper()
    if len(str(time)) > 4 or len(str(time)) < 3:
        return 'Некорректно указанно время. Пример: HHMM'
    if not time.isdigit():
        return 'Время должно быть указанно в цифровом виде'
    if city not in cd.city_database:
        raise TypeError(f'Города: ---> {city} <--- Нет в базе с UTC.')

    result_01 = decor.decorator_minus_40_minutes(  # ------------------------------> TL.
        calc_difference_between_utc_and_telegram_time(time, city))
    result_02 = decor.decorator_minus_36_hours(  # --------------------------------> 36 Часов.
        calc_difference_between_utc_and_telegram_time(time, city))
    result_03 = calc_difference_between_utc_and_telegram_time(time, city)[1]  # ---> Телеграмма.
    return f'TL ---> {result_01} | 36 ---> {result_02} | TLG ---> {result_03}'


if __name__ == '__main__':
    try:
        print(func_filter('1200', 'svo'))
    except TypeError as error:
        print(error)
