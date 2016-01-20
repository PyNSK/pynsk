Title: Примеры кода: скрипт поздравления всех друзей с НГ в vk.com
Date: 2015-12-30 18:00
Tags: vk, api, новый год, нг
Category: Примеры кода

В посте [http://old.pynsk.ru/posts/2015/Nov/26/api-vsemu-golova-vkontakte-ot-nachala-do-otpravki-soobshcheniia-drugu/](http://old.pynsk.ru/posts/2015/Nov/26/api-vsemu-golova-vkontakte-ot-nachala-do-otpravki-soobshcheniia-drugu/) было рассказано как начать работать с VK API.

НГ совсем близко. Python хорошо подходит для автоматизации. Поэтому в этот раз рубрика "Примеры кода"пополняется скриптом поздравления друзей с Новым Годом:

Полный код доступен по ссылке: [https://gist.github.com/PyNSK/39220dabd72e54faff18](https://gist.github.com/PyNSK/39220dabd72e54faff18)

А здесь приведем только часть:

```python
def main():
    access_token, _ = get_saved_auth_params()
    if not access_token or not _:
        access_token, _ = get_auth_params()
    api = get_api(access_token)

    texts = get_texts()
    for friend in api.friends.get():
        res = send_message(api, user_id=friend, message=random.choice(texts))
```

