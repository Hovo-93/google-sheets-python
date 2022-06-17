import requests
from bs4 import BeautifulSoup as bs


def get_xml():
    # Получаем xml
    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
    response = requests.get(url=url)

    # Инициализация  переменного soup
    soup = bs(response.text, 'xml')
    # Сохранение тегов и элементов <Valute>
    parents = soup.find_all('Valute')
    # Получение курса доллара
    for p in parents:
        if p.find('CharCode').text == 'USD':
            result = p.find('Value').text
            return result
