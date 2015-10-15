Title: Hardcore Python: Cython
Date: 2015-08-16 18:00
Tags: cython, оптимизация
Category: Hardcore Python 

Cython — язык программирования, упрощающий написание модулей С/С++ кода для Python. Кроме стандартного синтаксиса Python, поддерживаются:

Прямой вызов функций и методов С/С++ из кода на Cython;
Строгая типизация переменных, классов, атрибутов классов.

Код Cython преобразуется в С/С++ код для последующей компиляции и впоследствии может использоваться как расширение стандартного Python или как независимое приложение со встроенной библиотекой выполнения Cython.

Программирование на Cyhton не очень отличается от Python:

```python
cdef ackermann(int m, int n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

print("Ackermann:")
print(ackermann(0, 3))
print(ackermann(1, 4))
```

В этом коде указаны типы, что делать не обязательно (тогда и прироста не будет толком)
Типы в Cython - Си-шные, т.е. каких-то сложных Python-типов вы не найдете.

Хорошее применение языка - связка с C/C++ кодом - оно происходит в разы быстрее, чем в CPython и PyPi. Скорость исполнения программы также выше (может достигать сотен раз).  

- [http://cython.org/](http://cython.org/)
- [https://www.wikiwand.com/ru/Cython](https://www.wikiwand.com/ru/Cython)
