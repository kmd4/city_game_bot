import requests
from bs4 import BeautifulSoup
from src.constants import *


def performing_word(word):
    if word.lower()[-1] == 'ь' or word.lower()[-1] == 'ъ':
        return word[:-1]
    return word


class GetCity():
    def __init__(self, category):
        self.category = category
        self.all_cities = {}
        self.used_cities = []
        self.get_request()

    def get_request(self):
        for i in range(1040, 1072):
            if i == 1066 or i == 1068:
                continue
            response = requests.get(f'{URL}{self.category}.php?letter={chr(i)}')
            bs = BeautifulSoup(response.text, "lxml")
            temp = bs.find('div', 'field_center')
            temp = temp.find_all('p')[4]
            print(temp.text.split())
            self.all_cities[chr(i)] = temp.text.split()
