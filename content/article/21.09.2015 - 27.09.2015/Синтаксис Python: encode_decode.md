Title: Синтаксис Python: encode/decode
Date: 2015-09-21 10:00
Tags: encode, decode, синтаксис
Category: Синтаксис Python

Вероятно, самым заметным отличием Python 2 от Python 3 является юникод.  Это нововведение упростило работу со строками. Однако, так как Python 2 еще в строю, то кодировки еще в силе и не мало разработчиков путается между encode и decode.

Стоит привести картинку, которая прояснит все:

![Image](http://eli.thegreenplace.net/images/2012/01/py3_string_bytes.png)

Таким образом, если у нас есть строка:

```python
a = 'Cool page'
```

То существует множество способов (кодировок) представить ее в байтовом виде

Поэтому мы и пишем:
```python
a.encode('<название кодировки>') # переводим строку байтовый вид
```

И обратно. Если у нас есть набор байт, то чтобы получить строку пишем:

```python
b'<байт-строка>'.decode('<название кодировки>') # получаем из байтовой строки настоящую строку
```

Подробнее:

- [http://habrahabr.ru/post/135913/](http://habrahabr.ru/post/135913/)
- [http://eli.thegreenplace.net/2012/01/30/the-bytesstr-dichotomy-in-python-3/](http://eli.thegreenplace.net/2012/01/30/the-bytesstr-dichotomy-in-python-3/)