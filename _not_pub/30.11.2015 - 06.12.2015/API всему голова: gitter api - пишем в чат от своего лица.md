Title: API всему голова: gitter api - пишем в чат от своего лица
Date: 2015-12-03 18:00
Tags: api, gitter, channel
Category: API всему голова

Gitter - это система для создания чатов для пользователей Github. 
Чаты бесплатны, есть интеграция с Github, есть API - что еще для небольшого чата надо?

Сегодня мы научимся писать в чат с помощью API. В заголовке отметил, что будем писать от своего лица, поэтому будет все просто.

Для начала стоит изучить возможность API -> [https://developer.gitter.im/docs/welcome](https://developer.gitter.im/docs/welcome)

После чего авторизуйтесь:

![Image](http://pynsk.ru/images/posts/gitter_1.png)

После авторизации вы попадете на страницу https://developer.gitter.im/apps с таким контентом

![Image](http://pynsk.ru/images/posts/gitter_2.png)


Как вы заметили - access_token, вот он, сразу готовый. Для нашей задачи его достаточно.
Сохраняем и пишем следующий код:

```python

# -*- coding: utf-8 -*-

import json
import pprint

import requests


class Gitter(object):
    """
    Gitter API wrapper
    URL: https://developer.gitter.im/docs/welcome
    """

    def __init__(self, token):
        """token: access_token
        """
        self.token = token
        self.room_id_dict = self.get_room_id_dict()

    def get_rooms(self):
        """get all room information
        """
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
        }
        r = requests.get('https://api.gitter.im/v1/rooms', headers=headers)

        return r.json()

    def get_room_id_dict(self):
        """
        """
        room_id_dict = {}
        for room in self.get_rooms():
            if room['githubType'] != 'ONETOONE':
                room_id_dict[room['uri']] = room['id']

        return room_id_dict

    def send_message(self, room, text):
        """send message to room
        """
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token),
        }
        room_id = self.room_id_dict.get(room)
        url = 'https://api.gitter.im/v1/rooms/{room_id}/chatMessages'.format(room_id=room_id)
        payload = {'text': text}
        r = requests.post(url, data=json.dumps(payload), headers=headers)

        return r


def main(token):
    gitter = Gitter(token)
    pprint.pprint(gitter.room_id_dict)
    # Пример имени канала - pythondigest/pythondigest
    # gitter.send_message('<ИМЯ КАНАЛА>', 'Тестовое сообщание с помощью API')


if __name__ == '__main__':
    token = '<ВАШ TOKEN>'

    main(token)

```

В коде видно, что при создании объекта Gitter мы получаем список доступных комнат и сохраняем себе. Внутренний словарь запоминает соответствие id'шников каналов и человеко-понятных названий. 
И с помощью метода send_message отправляем сообщение в канал.

Вот и все.
