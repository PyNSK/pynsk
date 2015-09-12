Title: Таинство стандартной библиотеки: docstring
Date: 2015-09-06 10:00
Tags: docstring, документация
Category: Таинство стандартной библиотеки

Docstring - (сокращение от documentation string, строка документации) встроенное средство документирования модулей, функций, классов и методов. Делается очень просто - сразу после определения указывается строковое значение, которое и будет docstring'ом.

```python
>>> def test():
...    "This is the test's docstring"
...    print "opa"
```

Получить доступ к docstring можно так:

```python
>>> test.__doc__
"This is the test's docstring"
```

Либо так:

```python
>>> help(test)
Help on function test in module __main__:

test()
    This is the test's docstring
```

Существуют инструменты, которые позволяют извлекать docstring не по одиночке, а для целого модуля/пакета. О них и пойдет речь.

Изучаем дальше: 

- [https://www.python.org/dev/peps/pep-0257/](https://www.python.org/dev/peps/pep-0257/)
- [http://pyobject.ru/blog/2006/09/08/document-it/](http://pyobject.ru/blog/2006/09/08/document-it/)
- [http://habrahabr.ru/post/149371/](http://habrahabr.ru/post/149371/)

