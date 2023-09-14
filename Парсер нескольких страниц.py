import time
import requests
from bs4 import BeautifulSoup
import os
url = {
    'IXBT': 'https://ixbt.games/',
    'Stopgame': 'https://stopgame.ru/news',
}
class_novostey = {
    'IXBT': 'card-link',
    'Stopgame': '_title_1tbpr_49'
}
headers = {
    'Accept': '*/*',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def Zagryzka():
    for key, value in url.items():
        try:
            res = requests.get(value, headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'html.parser')

            with open(f'kod_str_{key}.html', 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при обращении к {key}: {e}")

def Parsing():
    for sayt, clas in class_novostey.items():
        with open(f'kod_str_{sayt}.html', 'r', encoding='utf-8') as f:
            src = f.read()

            soup = BeautifulSoup(src, 'lxml')
            zagolovki_novostey = soup.find_all(class_ = f'{clas}')
            print(f'{sayt}')
            for zag in zagolovki_novostey:
                zag_text = zag.text.strip()
                print(f'\n{zag_text}')

def Exit():
    for file, s in url.items():
        os.remove(f'kod_str_{file}.html')
        print('Файл удален.')
        time.sleep(5)
    exit()

while True:
    try:
        action = int(input('1 - Загрузить новости.\n2 - Показать список новостей.\n3 - Выход.''\n------------------>  '))
        if action == 1:
            Zagryzka()
        elif action == 2:
            Parsing()
        elif action == 3:
            Exit()
    except EOFError:
        print('\nВы ввели неверное значение')
        input('Enter для продолжения: ')