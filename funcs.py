import requests
import random
from Data.lexica import PHOTO
from Data.config import TOKEN, admin, users




# Получает id фото
def get_a_cat1():
    url = 'https://cataas.com/cat?json=true'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['file']


# Отправляет фото кота боту через API
def get_a_cat():
    caption = PHOTO[random.randint(0, (len(PHOTO) - 1))]
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={admin}&caption={caption}&photo=http://random.cat/view/{str(random.randint(0, 1677))}')
    response.raise_for_status()



