Title: Синтаксис Python: type, isinstance - определяем тип переменной
Date: 2015-12-14 10:00
Tags: type, isinstance
Category: Синтаксис Python

С помощью функции `type()` можно проверить, принадлежит ли данное тому или иному типу:

```python
>>> a = 10
>>> b = [1,2,3]
>>> type(a) == int
True
>>> type(b) == list
True
>>> type(a) == float
False
```

То же самое можно сделать с помощью функции `isinstance()`:

```python
>>> isinstance(a,int)
True
>>> isinstance(b,list)
True
>>> isinstance(b,tuple)
False
>>> c = (4,5,6)
>>> isinstance(c,tuple)
True
```

Однако `isinstance()` по сравнению с `type()` позволяет проверить данное на принадлежность хотя бы одному типу из кортежа, переданного в качестве второго аргумента:

```python
>>> isinstance(a,(float, int, str))
True
>>> isinstance(a,(list, tuple, dict))
False
```

Отмечают другое более важное преимущество `isinstance()`. Эта функция поддерживает наследование. Для `isinstance()` экземпляр производного класса есть экземпляр его базового класса:

```python
>>> class A (list):
...     pass
...
>>> a = A()
>>> type(a) == list
False
>>> type(a) == A
True
>>> isinstance(a,A)
True
>>> isinstance(a,list)
True
```


