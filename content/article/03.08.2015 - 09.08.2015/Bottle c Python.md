Title: Bottle с Python
Date: 2015-08-05 8:00
Tags: bottle, web
Category: Пишем web-проекты


bottle - это веб-фреймворк для Python. Отличительной особенностью этого фреймворка является простота - исходный код занимает один файл. Несмотря на свою минималистичность, Bottle предоставляет довольно широкие возможности, которых на 100% хватает для мелких и средних проектов.
Чтобы стартануть изучение достаточно написать:

```python
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
```

Это запустит web-приложение на 8080 порту, а по ссылке ```http://127.0.0.1/hello/Alexander``` вы увидите Hello Alexander.
Очень просто.

Дальнейшее изучение можно продолжить по ссылкам:

- [http://bottlepy.org/docs/dev/index.html](http://bottlepy.org/docs/dev/index.html)
- [http://habrahabr.ru/post/221659/](http://habrahabr.ru/post/221659/)
- [http://habrahabr.ru/post/250831/](http://habrahabr.ru/post/250831/)
