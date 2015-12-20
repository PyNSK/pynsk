Title: Таинство стандартной библиотеки:  functools.singledispatch
Date: 2015-08-23 10:00
Tags: functools
Category: Таинство стандартной библиотеки


Стандартная поставка Python полна возможностями. 
Хочется упомянуть обобщенные функции. Если простыми словами, то это такие функции, где мы не думаем о типах аргументов, а просто пишем логику.  Например, (натянутый пример) оператор "+" - мы не думаем о аргументах, мы просто складывает два объекта.

Для реализации обобщенных функций в Python 3 (начиная с 3.4) появился метод singledispatch в модуле functools.

```python
>>> @fun.register(int)
... def _(arg, verbose=False):
...     if verbose:
...         print("Strength in numbers, eh?", end=" ")
...     print(arg)
...

>>> @fun.register(list)
... def _(arg, verbose=False):
...     if verbose:
...         print("Enumerate this:")
...     for i, elem in enumerate(arg):
...         print(i, elem)
```

Подробней о этом механизме по ссылке - [https://www.python.org/dev/peps/pep-0443/](https://www.python.org/dev/peps/pep-0443/)
