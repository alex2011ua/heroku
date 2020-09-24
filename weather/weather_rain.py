'''
https://openweathermap.org/
'''

import requests
import datetime
from heroku.settings import APPID_Weather
def weather_rain_summ(lat=50.40, lon= 30.31):
    '''
    :param lat: lattitude(широта)
    :param lon: longtitude (долгота)
    :return: summ of rain (Сумма воды которая выпадет за 5 дней)
    '''
    payload = {'lat': lat,
               'lon': lon,
               'appid': APPID_Weather}
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    r = requests.get(url, params = payload)
    d = r.json()
    summ = 0
    for i in d["list"]:
        if i.get('rain'):
            summ += float(i['rain']['3h'])
    print(d['city']['name'])
    timestamp = d['list'][0]['dt']
    value = datetime.datetime.fromtimestamp(timestamp)
    value = value - datetime.timedelta(hours = 2)
    print(value.strftime('%Y-%m-%d %H:%M:%S'))
    if summ == 0:
        summ = 'Дождя не будет'
    context = {'rain': round(summ), 'date': value.strftime('%Y-%m-%d %H:%M:%S')}
    return context


if __name__ == "__main__":
    print(weather_rain_summ())
