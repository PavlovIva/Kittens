# Импорт всего необходимого
import requests
import random
from Data.lexica import PHOTO
from Data.config import TOKEN, admin


# Получает id фото
def get_a_cat1():
    url = 'https://cataas.com/cat?json=true'
    response = requests.get(url)
    response.raise_for_status()
    file = response.json()['file']
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={admin}&photo=http://random.cat/view/{file}')


# Класс, отвечающий за отправку фото, получения айди сообщения.
class GetCat:

    def __init__(self):
        self.message_id = 0
        self.count_like = 0

    # Отправка фото через Telegram API
    def get_a_cat(self, message_from_user_id):
        caption = PHOTO[random.randint(0, (len(PHOTO) - 1))]
        response = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={message_from_user_id}&caption={caption}&photo=http://random.cat/view/{str(random.randint(0, 1677))}')
        response.raise_for_status()
        self.message_id = (response.json()['result']['message_id'])

    # Возвращение айди сообщения
    def photo_id(self):
        return self.message_id

    def count_likes(self):
        self.count_like += 1
        return self.count_like




