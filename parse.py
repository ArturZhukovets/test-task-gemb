from bs4 import BeautifulSoup
import lxml
import requests
import json
import time


domen = 'https://www.list-org.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}
correct_urls = []

def collect_url():
    for i in range(5):
        url = f'https://www.list-org.com/list?okved2=56.10&page={i}'
        req = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(req.text, 'lxml')
        cards = soup.find('div', class_='card w-100 p-1 p-lg-3 mt-1').find_all('p')

        for card in cards:
            card = card.find('label')
            if not card.find('span', class_='status_0'):
                card_url = domen + card.find('a').get('href')
                correct_urls.append(card_url)

        print(f'[INFO] CARD # {i} collected ')
        time.sleep(1)
    return correct_urls


def get_data_from_elements(list_with_urls_of_cards: list):
    get_information = []
    counter_of_operations = 0
    total_operations = len(list_with_urls_of_cards)
    for get_inf_from_card in list_with_urls_of_cards:
        req = requests.get(get_inf_from_card, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')

        name = soup.find('table', class_='table table-sm').find_all('tr')[0].find('td').next_sibling.text
        supervisor = soup.find('table', class_='table table-sm').find_all('tr')[1].find('td').next_sibling.text
        address = soup.find('h6', class_='d-flex card-title').next_sibling.find('span').text
        try:
            telephone = soup.find('a', {'class': 'clipboards nwra'}).find('span').text
        except Exception as _ex:
            telephone = None

        get_information.append({
            'name': name,
            'supervisor': supervisor,
            'address': address,
            'telephone': telephone
        })

        counter_of_operations += 1
        print(
            f'Collecting data... Wait a few minutes... Operation # {counter_of_operations}, total operations - {total_operations}')
        if counter_of_operations == 90:
            time.sleep(500)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(get_information, f, ensure_ascii=False, indent=4)
    with open('data.json', 'r', encoding='utf-8') as f:
        json.load(f)
    return get_information

    # collect_url()
    # get_data_from_elements(correct_urls)

