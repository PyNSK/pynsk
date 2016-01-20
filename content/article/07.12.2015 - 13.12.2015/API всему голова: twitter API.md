Title: API всему голова: twitter API - пишем твит с изображением
Date: 2015-12-10 4:00
Tags: twitter, api, автоматизация
Category: API всему голова


О Twitter нечего писать, проект уже взрослый и известный. Через Твиттер продают, покупают, разыгрывают призы, консультируют, оказывают поддержку проектов, да даже используют как сервис оповещений.
Twitter имеет открытый API, который сегодня и освоим. Мы научимся публиковать пост с изображением через Twitter API


Начинаем работу с API - получаем APP_ID
---------------------------------------

Как и с другими API, первый шаг - почитать документацию - [https://dev.twitter.com/overview/documentation](https://dev.twitter.com/overview/documentation)

А второй шаг - авторизоваться. Чтобы авторизоваться надо получить API Key, API Secret и access token. 
Для этого идем по ссылке [https://apps.twitter.com/](https://apps.twitter.com/)

Наблюдаем такую картину:

![Image](http://old.pynsk.ru/images/posts/twitter_api_1.png)

Создаем приложение - вводим название, описание и ссылку на сайт. Эти данные толком не важны, поэтому вводим любые

![Image](http://old.pynsk.ru/images/posts/twitter_api_2.png)

После того как будет создано приложение мы получим нужные данные:

![Image](http://old.pynsk.ru/images/posts/twitter_api_3.png)
![Image](http://old.pynsk.ru/images/posts/twitter_api_4.png)

Жмем на кнопку `"Create my access token"` и получаем все самое важное:

- API key (`TWITTER_CONSUMER_KEY`)
- API Secret (`TWITTER_CONSUMER_SECRET`)
- Access token (`TWITTER_TOKEN`)
- Access token secret (`TWITTER_TOKEN_SECRET`)

Теперь перейдем непосредственно к авторизации и нашей задачи

Выбираем клиенсткую библиотеку
------------------------------

Для API твиттера написано множество готовых клиентский библиотек - [https://dev.twitter.com/overview/api/twitter-libraries](https://dev.twitter.com/overview/api/twitter-libraries)

Для Python это:

- [tweepy](https://github.com/tweepy/tweepy) 
- [python-twitter](https://github.com/bear/python-twitter)
- [TweetPonyby](https://github.com/Mezgrman/TweetPony)
- [Python Twitter Tools](https://github.com/sixohsix/twitter)
- [twitter-gobject](https://github.com/tchx84/twitter-gobject)
- [TwitterSearch](https://github.com/ckoepp/TwitterSearch)
- [twythonby](https://github.com/ryanmcgrath/twython)
- [TwitterAPI](https://github.com/geduldig/TwitterAPI)
- [Birdy](https://github.com/inueni/birdy)

Т.е. очень много.

В примерах будет использоваться `tweepy` - потому что потому.


Работаем с API
----------------

Объявленная задача - написать пост через API с вложением.
Для этого:

Напишем функцию авторизации:

```python
def init_auth(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
```

После этого можно дергать методы из документации.
Для публикации поста с вложением есть метод `update_with_media` в `tweepy`, который принимает путь до файла и текст.

Практика использования показывает, что картинки используются из Интернет, поэтому удобней указывать url до картинки и текст.
Напишем функции:

```python
def download_image(url):
    try:
        file_path = os.path.abspath(os.path.split(url)[-1])
        urlretrieve(url, file_path)
    except IndexError as e:
        print(e)
        file_path = None
    except HTTPError as e:
        print(e)
        file_path = None
    return file_path


def send_tweet_with_media(api, text, image):
    if 'http://' not in image:
        assert os.path.isfile(image)
        file_path = image
    else:
        # качаем файл из сети
        file_path = download_image(image)

    assert file_path is not None, "Not found image (for twitter)"
    api.update_with_media(file_path, text) 
```

Вот и весь код. Используем его

```python
twitter_text = '#pynsk Я научился работать с twitter api"
image = 'https://pp.vk.me/c624516/v624516517/31b6b/6kViWNZI6n4.jpg'
twitter_api = init_auth(consumer_key, consumer_secret, access_token, access_token_secret)
send_tweet_with_media(twitter_api, twitter_text, image)
```
