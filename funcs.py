import requests
import random
from Data.lexica import PHOTO
from Data.config import TOKEN


# Отправляет фото кота боту через API
def get_a_cat():
    caption = PHOTO[random.randint(0, (len(PHOTO) - 1))]
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id=867978028&caption={caption}&photo=https://cataas.com/cat')
    response.raise_for_status()


# Получает id фото
def get_a_cat1():
    url = 'https://cataas.com/cat?json=true'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['file']
