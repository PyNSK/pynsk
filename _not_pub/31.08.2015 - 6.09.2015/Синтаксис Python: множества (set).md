Title: Синтаксис Python: множества (set)
Date: 2015-08-31 17:00
Tags: set
Category: Синтаксис Python

Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.


```python
>>> a = set()
>>> a
set()
>>> a = set('hello')
>>> a
{'h', 'o', 'l', 'e'}
>>> a = {'a', 'b', 'c', 'd'}
>>> a
{'b', 'c', 'a', 'd'}
>>> a = {i ** 2 for i in range(10)} # генератор множеств
>>> a
{0, 1, 4, 81, 64, 9, 16, 49, 25, 36}
>>> a = {}  # А так нельзя!
>>> type(a)
<class 'dict'>
```

Ссылки по теме:

- [http://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html](http://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html)
- [http://server.179.ru/tasks/python/2014b1/17-sets.html](http://server.179.ru/tasks/python/2014b1/17-sets.html)
- [http://informatics.mccme.ru/mod/book/view.php?id=6693](http://informatics.mccme.ru/mod/book/view.php?id=6693)