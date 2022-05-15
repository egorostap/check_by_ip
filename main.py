import requests
import json
import folium

def try_ex_dec(fn):
    def wrapped(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except Exception as e:
            print('ошибка:', e)
    # овлорлыр
    return wrapped

# сбор информации по айпи
@try_ex_dec
def check_by_ip(source='http://ip-api.com/json/', ip=''):
    response = requests.get(url=source+ip).json()

    # to json
    with open('data.json', 'w') as f:
        json.dump(response, f, indent=4, ensure_ascii=False)
    # определения местоположения на карте по широте и долготе
    area = folium.Map(location=[response['lat'], response['lon']])
    area.save(f'{response["query"]}_{response["city"]}.html')

    print(response)
    return response


if __name__ == '__main__':
    check_by_ip(ip='185.2.154.85')

