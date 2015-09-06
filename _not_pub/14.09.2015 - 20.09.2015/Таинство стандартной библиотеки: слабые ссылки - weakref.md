Title: Таинство стандартной библиотеки: слабые ссылки - weakref
Date: 2015-09-19 15:00
Tags: weakref, стандартная библиотека, слабая ссылка
Category: Таинство стандартной библиотеки


Python имеет автоматическое управление памятью: подсчёт ссылок для большинства объектов и сборка мусора для удаления циклов. Память освобождается сразу после того, как была удалена последняя ссылка на объект.

Этот подход отлично работает для большинства приложений, но иногда возникает необходимость вести учёт объектов только когда они используются где-нибудь ещё. К сожалению, само слежение за объектами уже создает ссылку и тем самым объекты остаются в памяти. Модуль weakref (от англ. weak reference - слабая ссылка) даёт средство для учёта объектов без создания ссылок на них. Когда объект больше не нужен, он автоматически удаляется из таблицы слабых ссылок и производится обратный вызов weakref-объектов. Типичное применение модуля - кэширование объектов, которые затратно воспроизвести снова.

```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...             self.value = value
...     def __repr__(self):
...             return str(self.value)
...
>>> a = A(10)                   # создаёт ссылку
>>> d = weakref.WeakValueDictionary()  # словарь, использующий слабые ссылки
>>> d['primary'] = a            # не создаёт ссылки
>>> d['primary']                # достать объект, если он все ещё "жив"
10
>>> del a                       # удалить одну ссылку
>>> gc.collect()                # произвести сборку мусора
0
>>> d['primary']                # запись была автоматически удалена
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']
  File "C:/python31/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

Ссылки на тему:

- [https://docs.python.org/3/library/weakref.html](https://docs.python.org/3/library/weakref.html)
- [http://pep8.ru/doc/tutorial-3.1/11.html](http://pep8.ru/doc/tutorial-3.1/11.html)
- [http://www.ilnurgi1.ru/docs/python/modules/weakref.html](http://www.ilnurgi1.ru/docs/python/modules/weakref.html)