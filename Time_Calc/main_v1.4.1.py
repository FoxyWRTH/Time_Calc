"""
Калькулятор времени.
"""
from datetime import timedelta
from Resources import city_database as data_base
from Resources import decorators


@decorators.decorator_debug
def time_calc_all_in_one(time: str, city='SVO', svo=3):
    """
    Функция считает разницу по UTC между городом который передаётся в функцию и Москвой,
    тем самым получаем время Москвы относительно времени переданного города.
    Так же функция рассчитывает время которое нужно установить при пересадке пассажира. (TL)
    Так же функция рассчитывает локальное время вылета согласно информации из телеграммы. (TG)
    Так же функция рассчитывает крайнее время для подачи заявки на провоз спец оборудования. (36)
    :param time: Местное время вылета.
    :param city: Город вылета.
    :param svo: UTC москвы (Константа)
    :return: Время в москве с учётом разницы UTC
    """
    city = city.upper()
    if len(str(time)) > 4 or len(str(time)) < 3:
        return 'Некорректно указанно время. Пример: HHMM'
    if not time.isdigit():
        return 'Время должно быть указанно в цифровом виде'
    if city not in data_base.city_database:
        raise TypeError(f'Города: ---> {city} <--- Нет в базе с UTC.')
    hours = int(time[:2])
    minutes = int(time[2:])

    local_time = timedelta(hours=hours, minutes=minutes)
    local_city_utc = timedelta(hours=data_base.city_database.get(city)[1],
                               minutes=data_base.city_database.get(city)[2])
    svo_utc = timedelta(hours=svo)

    moscow_time = local_time - (local_city_utc - svo_utc)
    minus_36_hours = moscow_time - timedelta(hours=36)
    minus_40_minutes = moscow_time - timedelta(minutes=40)
    telegram_time = local_time + local_city_utc

    result = (f'TL = {minus_40_minutes}\n'
              f'TG = {telegram_time}\n'
              f'36 = {minus_36_hours}\n')

    return result


if __name__ == '__main__':
    try:
        print(time_calc_all_in_one('1000', 'del'))
    except TypeError as error:
        print(error)
