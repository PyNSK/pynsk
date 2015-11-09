Title: Таинство стандартной библиотеки: zipimport - импортируем код из zip файлов
Date: 2015-10-24 15:00
Tags: zip, import
Category: Таинство стандартной библиотеки

Еще в далеком Python 2.3 был добавлен модуль ```zipimport```. 
Этот модуль упростил возможность импорта из ```zip``` файлов: 

```python
$ python
Python 2.3 (#1, Aug 1 2003, 19:54:32) 
>>> import sys
>>> sys.path.insert(0, '/tmp/example.zip')  # Add .zip file to front of path
>>> import jwzthreading
>>> jwzthreading.__file__
'/tmp/example.zip/jwzthreading.py'
```

(больше примеров по см. по первой ссылке)

Конечно, такой функционал мало кому нужен, но давайте придумаем какой-то use-case - пофантазируем. Пишите свои мысли в комментариях

Предположим что есть динамическая система, какая-то жутко настраиваемая система - в зависимости от дня недели выполняется код. Тогда можно реализовать в коде выкачивание нужного архива с вашего сервера в виде zip файла и затем с помощью zipimport исполнять код.

Ссылки: 

- [https://pymotw.com/2/zipimport/](https://pymotw.com/2/zipimport/)
- [https://docs.python.org/2/library/zipimport.html](https://docs.python.org/2/library/zipimport.html)
- [https://docs.python.org/2.3/whatsnew/node5.html](https://docs.python.org/2.3/whatsnew/node5.html)
- [http://habrahabr.ru/company/acronis/blog/208378/](http://habrahabr.ru/company/acronis/blog/208378/)
