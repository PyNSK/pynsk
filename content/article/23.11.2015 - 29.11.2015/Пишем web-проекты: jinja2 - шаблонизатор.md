Title: Пишем web-проекты: jinja2 - шаблонизатор
Date: 2015-11-25 10:00
Tags: jinja2, web, видео
Category: Пишем web-проекты

Jinja — это шаблонизатор для языка программирования Python. Он подобен шаблонизатору Django, но предоставляет Python-ические выражения, обеспечивая исполнение шаблонов в песочнице. Это текстовый язык шаблонов и, таким образом, может быть использован для создания какой-либо разметки, а также исходного кода.

Шаблонизатор Jinja позволяет настраивать теги, фильтры, тесты и глобальные переменные. Также, в отличие от шаблонизатора Django, Jinja позволяет конструктору шаблонов вызывать функции с аргументами на объектах.


```python
# -*- coding: utf-8 -*-
from jinja2 import Template

template = Template('Hello {{ name }}!')
print(template.render(name=u'Вася'))
```


Неплохой рассказ про шаблонизаторы:

[!embed](https://www.youtube.com/watch?v=ktSo_Njy6Cc)

Ссылки для изучения:

- [http://jinja.pocoo.org/](http://jinja.pocoo.org/)
- [http://habrahabr.ru/post/164823/](http://habrahabr.ru/post/164823/)
