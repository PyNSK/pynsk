Title: Таинство стандартной библиотеки: functools.lru_cache — кэшируем результат выполнения функции
Date: 2015-10-05 18:00
Tags: functools, стандартная библиотека, кэш, cache
Category: Таинство стандартной библиотеки


![Image](http://amnesia.me/images/amnesia%20humor.jpg)

Начиная с версии 3.2, в Python появилась возможность стандартными средствами организовать мемоизацию. Иными словами, кэшировать результаты вызова функции. Этот механизм представлен в виде декоратора в модуле ```functools``` и называется ```lru_cache``` (least recently used cache).

На примере изъезженных чисел Фибоначчи это выглядит так:

```python
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

>>> fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
```

Схема вычисления числа Фибоначчи для 6 без кэша:
![Image](https://upload.wikimedia.org/wikibooks/ru/d/dc/Fibtree.jpg)

Легко заметить, что есть повторяющиеся поддеревья, которые можно заново не вычислять. Однако, если у нас нет кэша, то куча времени уйдет на вычисление уже известных значений. Декоратор @lru_cache добавляет кэш необходимого размера (по умолчанию ёмкостью в 128 результатов), тем самым позволяя ускорить исполнение кода. 

Ссылка для изучения:
- [https://docs.python.org/3.4/library/functools.html](https://docs.python.org/3.4/library/functools.html)


