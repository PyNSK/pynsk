Title: Hardcore Python: запускаем С код с помощью cffi
Date: 2015-08-23 18:00
Tags: cffi
Category: Hardcore Python


Самый популярный Python это CPython. Он настолько популярен, что когда говорят Python имеют ввиду именно каноническую реализацию - CPython.

CPython, как можно понять из названия, имеет какое-то отношение к языку C.
Из Python вы можете с помощью ctypes дергать С-шные функции.  
Однако, этот механизм несколько медленный и не всегда удобный - бывает надо просто дернуть один кусок C-кода. Или надо только часть от h-файла, или только кусок структуры.
Вот в этом случае помогает - cffi.

Пример кода с использованием этой библиотеки:

```python
>>> from cffi import FFI
>>> ffi = FFI()
>>> ffi.cdef("""
.......int printf(const char *format, ...);   // copy-pasted from the man page
.......""")
>>> C = ffi.dlopen(None)                     # loads the entire C namespace
>>> arg = ffi.new("char[]", "world")         # equivalent to C code: char arg[] = "world";
>>> C.printf("hi there, %s.\n", arg)         # call printf
hi there, world.
17                                           # this is the return value
>>>
```

Эти многоточия в cdef это _реальный_ код, который надо писать.

- [https://cffi.readthedocs.org/en/latest/](https://cffi.readthedocs.org/en/latest/)
- [https://pypi.python.org/pypi/cffi](https://pypi.python.org/pypi/cffi)