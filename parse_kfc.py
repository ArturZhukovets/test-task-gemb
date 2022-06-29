from bs4 import BeautifulSoup
import lxml
import requests
import json
import time



def get_data_from_kfc():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    content = []

    url = 'https://api.kfc.com/api/store/v2/store.get_restaurants?showClosed=true'

    req = requests.get(url, headers=headers)
    json_data = json.loads(req.text)
    number_of_restaurant = len(json_data['searchResults'])
    print(number_of_restaurant)

    for restaurant_num in range(number_of_restaurant):
        try:
            road_to_inf = json_data['searchResults'][restaurant_num]['storePublic']['contacts']
            working_hours = json_data['searchResults'][restaurant_num]['storePublic']['openingHours']['regular']

            status = json_data['searchResults'][restaurant_num]['storePublic']['status']

            dict_data = {
                'address': [road_to_inf['streetAddress']['ru']],
                'latlon': road_to_inf['coordinates']['geometry']['coordinates'],
                "name": road_to_inf['coordinates']['properties']['name']['ru'],
                'phones': [road_to_inf['phone']['number']],
                "working_hours": [
                    f"пн-пт {working_hours['startTimeLocal']} до {working_hours['endTimeLocal']}"
                    f" сб-вс {working_hours['startTimeLocal']} до {working_hours['endTimeLocal']}",
                    status

                ],

            }
            content.append(dict_data)

            iterations_left = number_of_restaurant - restaurant_num
            print(f'Iteration number {restaurant_num} is gone. Iterations left {iterations_left} ')
        except TypeError:
            print(f'Object {restaurant_num} has some problems')
        except KeyError:
            print(f'Object {restaurant_num} has some with json keys')

    with open('kfc.json', 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=4, ensure_ascii=False)