Title: API всему голова: ВКонтакте - от начала до отправки сообщения другу
Date: 2015-11-26 18:00
Tags: api, vk.com, вконтакте
Category: API всему голова

Работа с API сервисов это всегда история по типу "Ожидание...реальность". Ибо даже простое API может скушать день, а то и 2 дня рабочего времени. 

API Вконтакте не исключение. Уже есть очень много материалов на тему использования этого интерфейса:

[http://habrahabr.ru/search/page2/?q=vk+api&target_type=posts&order_by=relevance](http://habrahabr.ru/search/page2/?q=vk+api&target_type=posts&order_by=relevance) 

Много практических задач решили с помощью API:

- [Скачивание музыки из VK, используя VK api и Python3](http://habrahabr.ru/post/266671/) 
- [Находим общих друзей людей с использованием VK API](http://habrahabr.ru/post/212405/) 
- [Введение в анализ социальных сетей на примере VK API](http://habrahabr.ru/company/hh/blog/263313/))
- [Сортировка треков в плейлисте VK](http://habrahabr.ru/post/183408/)

И даже уже есть несколько готовых реализаций-библиотек для работы с Вконтакте:

- модуль [vk](https://github.com/dimka665/vk)
- модуль [vk_api](https://github.com/python273/vk_api) 

И из раз в раз гугл мучается от запросов "Vk.com api". Пользователи ищут примеры авторизация, документацию, примеры использования. 
Поэтому я приведу один из вариантов старта в API Вконтакте, а именно. Мы отправим `hello world` другу.

Начнем - получим APP_ID и SECRET_KEY
---------------------------------------

Стоит отметить, что API Вконтакте неплохо описано - включив мозг можно понять что и куда тыкать. 
В этом можно убедится самостоятельно - [https://vk.com/dev/main](https://vk.com/dev/main)

Для того чтобы начать делать запросы в API необходимо получить APP_ID и SECRET_KEY - это свойственно почти всем современным сервисам.
Для этого идем на страницу [https://vk.com/apps?act=manage](https://vk.com/apps?act=manage)
Видим примерно такую картину:

![vk](http://old.pynsk.ru/images/posts/vk_api_post_1.png)

Создаем свое приложение:

![vk](http://old.pynsk.ru/images/posts/vk_api_post_2.png)

Выбираем "Standalone-приложение" - для нашего сайта это в самый раз

В итоге получаем приложение:

![vk](http://old.pynsk.ru/images/posts/vk_api_post_3.png)

На странице "настройки" видим `ID приложения` и `Защищенный ключ`:

![vk](http://old.pynsk.ru/images/posts/vk_api_post_4.png)

Запишите их, они нам понадобятся. 
А также не забудьте включить приложение.
А еще в `Права доступа` укажите необходимые доступы - можно указать все, пока не разобрались что к чему.

В результате мы получили `ID приложения` и `Защищенный ключ`, которые называются часто `APP_ID` и `SECRET_KEY`.


Получим ACCESS_TOKEN
-------------------------------

Получили какие-то `APP_ID` и `SECRET_KEY`, а везде в документации просят `ACCESS_TOKEN`. 
Давай-те научимся его получать.  

В качестве обертки над API возьмем `vk` (почему? без причины, понравилась эта обертка), установим:

```bash
pip install --upgrade vk
```

А затем возьмем готовый код (`все написано за нас`).
Для примера возьмем возьмем [готовый кусок кода](https://gist.github.com/st4lk/4708673) и немного преобразуем по Python3:

```python

# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
import pprint
from urllib.parse import parse_qs
import webbrowser
import pickle
from datetime import datetime, timedelta
import vk
import time

# id of vk.com application
APP_ID = <ВСТАВИТЬ ТВОЙ APP_ID>
# file, where auth data is saved
AUTH_FILE = '.auth_data'
# chars to exclude from filename
FORBIDDEN_CHARS = '/\\\?%*:|"<>!'

def get_saved_auth_params():
    access_token = None
    user_id = None
    try:
        with open(AUTH_FILE, 'rb') as pkl_file:
            token = pickle.load(pkl_file)
            expires = pickle.load(pkl_file)
            uid = pickle.load(pkl_file)
        if datetime.now() < expires:
            access_token = token
            user_id = uid
    except IOError:
        pass
    return access_token, user_id


def save_auth_params(access_token, expires_in, user_id):
    expires = datetime.now() + timedelta(seconds=int(expires_in))
    with open(AUTH_FILE, 'wb') as output:
        pickle.dump(access_token, output)
        pickle.dump(expires, output)
        pickle.dump(user_id, output)


def get_auth_params():
    auth_url = ("https://oauth.vk.com/authorize?client_id={app_id}"
                "&scope=wall,messages&redirect_uri=http://oauth.vk.com/blank.html"
                "&display=page&response_type=token".format(app_id=APP_ID))
    webbrowser.open_new_tab(auth_url)
    redirected_url = input("Paste here url you were redirected:\n")
    aup = parse_qs(redirected_url)
    aup['access_token'] = aup.pop(
        'https://oauth.vk.com/blank.html#access_token')
    save_auth_params(aup['access_token'][0], aup['expires_in'][0],
                     aup['user_id'][0])
    return aup['access_token'][0], aup['user_id'][0]


def get_api(access_token):
    session = vk.Session(access_token=access_token)
    return vk.API(session)

def main():
    access_token, _ = get_saved_auth_params()
    if not access_token or not _:
        access_token, _ = get_auth_params()
    api = get_api(access_token)

main()

```

Что же делает этот код? Сначала мы читаем файл `AUTH_FILE`, если такой файл есть, то выгребаем от туда токен и проверяем - протух ли он или еще нет.

Если же токена нет или протух, то скрипт генерирует ссылку для авторизации и открывает ее в браузере. 
Браузер откроется, vk api попросит доступ к вашим данным. 

После авторизации необходимо скопировать ссылку страницы в консоль и нажать Enter - скрипт сам достанет нужные параметры и сохранит в файл.

Ссылка, которая будет в браузере примерно такая:

```
https://oauth.vk.com/blank.html#access_token=147a6effsfsd342452345ea8b59e03ef0538f20e0a474887bb46299fc99aed4bfsda11c0be900&expires_in=86400&user_id=16932517
```

Теперь у нас есть `ACCESS_TOKEN`, осталось малое дело - написать другу сообщение

Пишем другу сообщение с помощью API
----------------------------------------

Модифицируем функцию main, а также добавим функцию `send_message` (угадайте что она делает):

```python
def send_message(api, user_id, message, **kwargs):
    data_dict = {
        'user_id': user_id,
        'message': message,
    }
    data_dict.update(**kwargs)
    return api.messages.send(**data_dict)

def main():
    access_token, _ = get_saved_auth_params()
    if not access_token or not _:
        access_token, _ = get_auth_params()
    api = get_api(access_token)

    users = [<СПИСОК ID'шников пользователей>]
    user_text = "Привет. Я научился с помощью API писать сообщение"
    for user_id in users:
        print("User ", user_id)
        res = send_message(api, user_id=user_id, message=user_text)
        time.sleep(1)
        print(res)
```


Объедините эти два исходника и сможете отправить другу сообщение с помощью VK API