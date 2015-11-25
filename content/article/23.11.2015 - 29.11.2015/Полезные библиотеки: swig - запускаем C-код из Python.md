Title: Полезные библиотеки: swig - запускаем C-код из Python
Date: 2015-11-26 10:00
Tags: видео, swig, cython, c
Category: Полезные библиотеки


Для работы с С-библиотеками есть несколько способов:
- Писать программу на С/C++ и подключать DLL (.so) файлы
- Попытаться напрямую запустить C код из нужного языка. 

Перед тем как продолжить - зачем нужно запускать C/C++ код?
Все просто - например, работаем с железом, а значит и с драйверами (а их пишут на C). Вот здесь и появляется необходимость взаимодействовать с С кодом.

В Python есть несколько вариантов запуска С/C++ кода (без модификации исходного кода) - ctypes, cliff или даже swig.

Сейчас про SWIG. SWIG (simplified wrapper and interface generator) - это инструмент создания биндингов к различным языкам. 

Работа со SWIG  проста и сложна одновременно. SWIG генерирует большинство кода за программиста. Поэтому необходимо сделать 2 основных шага:

1) Создать .i файл, в котором описать структуру C/C++-проекта (заголовочные файлы, файлы исходников, необходимые библиотеки)
2) Скомпилировать

Файл .i выглядит так (пример):

```python

%module WDMTNKv2

%typemap(in) HANDLE {
$1 = (void *)(PyInt_AsLong($input));
}

%typemap(out) HANDLE {
$result = PyInt_FromLong((int)($1));
}

%include <windows.i>
%include <carrays.i>
%array_class(unsigned short int, WordBuffer);
%include "WDMTMKv2.h"
```

А шаг компиляции может выглядеть так:

run.bat:

```
python setup.py build_ext --inplace -cmingw32
```

setup.py:
```python
import distutils
from distutils.core import setup, Extension

setup(
    name = "MIL-STD-1553B",
    version = "4.08",
    ext_modules = [Extension(
            "_WDMTMKv2",
            ["WDMTMKv2.i", "WDMTMKv2.cpp"],
            swig_opts=['-py3', '-c++', '-module','WDMTMKv2'],
    )]
)
```

В результате получится `.pyd` файл, который используется как обычный python модуль:

```from WDMTMKv2 import *```


[!embed](https://www.youtube.com/watch?v=mv0kfiepn3s )

- [http://www.swig.org/](http://www.swig.org/)