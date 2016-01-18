Title: API всему голова: Feedly API - разбираемся с RSS сервисом
Date: 2016-01-01 18:00
Tags: feedly, api, rss, фильтр
Category: API всему голова

Сегодня хочу описать как работать с `Feedly` через их API в языке Python.

Для начала ссылки, которые точно понадобятся:

- Документация: [https://developer.feedly.com/](https://developer.feedly.com/)
- Рассылка: [https://groups.google.com/forum/#!forum/feedly-cloud](https://groups.google.com/forum/#!forum/feedly-cloud)


Разработчики из Feedly довольно активно желают, чтобы сторонние разработчики участвовали в совершенствовании сервиса. 
Поэтому если вам необходимы какие-то хитрые условия для работы вашего приложения - изменить ограничение по запросам, как пример, то Feedly могут пойти на встречу.

В Feedly есть 3 варианта API:

- Работа в “`песочнице`” - [https://sandbox.feedly.com/](https://sandbox.feedly.com/)
    - Ссылка по которой можно получить ключ (`token`): [https://sandbox.feedly.com/v3/auth/dev](https://sandbox.feedly.com/v3/auth/dev)
- Работа с облаком - это [https://cloud.feedly.com](cloud.feedly.com), который является главным сервисом, все пользователи его видят
    - Ссылка по которой можно получить ключ (`token`): [https://feedly.com/v3/auth/dev](https://feedly.com/v3/auth/dev)
- И `development sandbox`. Отличие от первого варианта, что работаешь не через свой аккаунт. А через общий сервис
    - Раз в месяц в группе (рыссылке) размещают токен.

Интересен мне второй вариант, про него и будет рассказ.

Стоит обратить внимание что в документации можно найти готовые запросы с помощью `curl`. Т.е. даже не трогая никакого языка программирования можно работать с API Feedly.

Я же буду работать в Python.

И буду использовать `python-feedly`

Устанавливаем спомощью pip:

```pip install python-feedly```

В [`README.md`](https://github.com/WarmongeR1/python-feedly/blob/master/README.rst) есть готовые примеры для использования. Их и заиспользуем:

```python
feedly = FeedlyClient(token=token, sandbox=False)
```

Где `token`, это длинная строчка типа `AhQjf…...Q:feedlydev`
Объект есть, теперь можно возиться с ним.

Не стану разводить тут мысли и раздумья и покажу как получить список непрочитанных новостей. 

> В документации используется понятие `stream_id`. Это `id` почти любого объекта, например, категория, feed и др.


Получим все категории:

```python
categories = feedly.get_info_type(token, 'categories')
```

А теперь получим все непрочитанные новости из этих категорий.

```python
articles = []
for i, category in enumerate(categories):
   if type(category) != str:
       print("{} of {} category ({})".format(i + 1, len(categories), category.get('label')))
       result = feedly.get_feed_content(token, category.get('id'), True, previous_time)
       items = result.get('items', [])
       articles.extend(items)
```

,где `token` уже знаем что такое, 
`previous_time` это время начиная с которого хочется получить статьи, целое число, время в unix time.

Оп, теперь в `acticles` есть список статей, которые не прочтены.


Заголовок, ссылку на новость и описание можно получить так:

```python
for item in articles:
   url = item.get('alternate')[0].get('href')
   title = item.get('title', '')
   description = item.get('summary', {}).get('content')
```

Теперь умеем получать категории, статьи, а у статей доставать описание, название, ссылку. 
Этого уже достаточно, чтобы написать свой фильтр RSS. 

В API Feedly есть еще много всяких возможностей. Пользуйтесь.