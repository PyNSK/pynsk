Title: Таинство стандартной библиотеки: shelve - база данных для объектов
Date: 2015-12-06 15:00
Tags: стандартная библиотека, pickle
Category: Таинство стандартной библиотеки

Модуль `shelve` из стандартной библиотекой можно описать одной фразой - "pickle + anydbm".

shelve позволяет сериализовать объект (прям как `pickle`), а потом сохранить его в виде похожем на БД (интерфейс `anydbm`).

```python
>>> import shelve
>>> db = shelve.open(“filename”)
>>> db[‘key’] = obj
>>> obj = db[‘key’]
>>> db.close()
```

Как видно из небольшого примера, БД предоставляет интерфейс словаря. Это позволяет нам сохранять различные сериализуемые объекты под разными именами и хранить их в одном файле.

Описание методов в модуле можно почитать:

- [https://docs.python.org/3/library/shelve.html](https://docs.python.org/3/library/shelve.html)
- [http://www.ilnurgi1.ru/docs/python/modules/shelve.html](http://www.ilnurgi1.ru/docs/python/modules/shelve.html) (на русском)