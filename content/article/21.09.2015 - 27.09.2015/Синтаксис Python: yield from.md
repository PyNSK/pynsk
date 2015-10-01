Title: Синтаксис Python: yield from
Date: 2015-09-21 18:00
Tags: yield from, синтаксис
Category: Синтаксис Python

Рассмотрим еще одну страшную конструкцию в Python 3.3+ - yield from

Напомню, генератор это объект который можно про итерировать только однажды. Записывается как:

```python
f = (x for x in xrange(100)) 
# Или так
def gen():
    for x in range(100):
        yield x
```

Когда у нас один генератор - все хорошо. Используем его как итератор и радуемся. Но не редки ситуации когда есть два генератора:

```python
def generator2():
    for i in range(10):
        yield i

def generator3():
    for j in range(10, 20):
        yield j
```

И стоит задача - проитерировать один генератор, потом второй. Но вернуть значения не в виде списка,  в виде генератора.
Здесь на помощь приходит конструкция
```
yield from <expr>
```
где ```<expr>``` - выражение, вычисление которого даёт нам итерируемый объект, из которого и вычленяется итератор. 

Эту конструкцию можно читать так:
```yield (вернуть значение) <стоп мыслей> from (взять значение из) <expr>```

Используя ```yield form``` задача решается так:

```
def generator():
    yield from generator2()
    yield from generator3()
>>> generator()
<generator object generator at 0x7f60d8fb3480>
```

Почитать:

- [https://www.python.org/dev/peps/pep-0380/](https://www.python.org/dev/peps/pep-0380/)
- [http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html](http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html)
- [http://habrahabr.ru/post/132554/](http://habrahabr.ru/post/132554/)