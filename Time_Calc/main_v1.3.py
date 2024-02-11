"""
Калькулятор времени.
"""
from datetime import timedelta as td
import city_database as cd


def time_calc(hours, minutes, city='SVO', svo=3):
    """
    :param hours: Местное время вылета - Часы.
    :param minutes: Местное время вылета - Минуты.
    :param city: Город вылета.
    :param svo: UTC по Москве (Константа)
    :return: Сколько ставить TimeLimit
    """
    if city not in cd.city_database:
        raise ValueError(f'Города: ---> {city} <--- Нет в базе с UTC.')
    local_departure_time = td(hours=hours, minutes=minutes)
    difference_between_utc = td(hours=cd.city_database.get(city)[1],
                                minutes=cd.city_database.get(city)[2]) - td(hours=svo)
    minus_forty_minutes = td(minutes=40)

    result = local_departure_time - difference_between_utc - minus_forty_minutes
    return result


def telegram_time_calc(hours, minutes, city='SVO'):
    if city not in cd.city_database:
        raise ValueError(f'Города: ---> {city} <--- Нет в базе с UTC.')
    telegram_time = td(hours=hours, minutes=minutes)
    result = telegram_time + td(hours=cd.city_database.get(city)[1],
                                minutes=cd.city_database.get(city)[2])
    return result


if __name__ == '__main__':
    try:
        print(f'Cтавь TL: {time_calc(0, 0, "KGD")}')
        print('-' * 15)
        print(f'Локальное время вылета: {telegram_time_calc(0, 0, 'KGD')}')
    except ValueError as error:
        print(error)
