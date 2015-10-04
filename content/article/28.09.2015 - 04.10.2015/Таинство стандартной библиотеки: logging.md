Title: Таинство стандартной библиотеки: logging
Date: 2015-10-03 15:00
Tags: log, logging, print
Category: Таинство стандартной библиотеки

```Logging``` — библиотека для удобного ведения логов в Python 

В любой разработке приходится рано или поздно вести логи, ведь не отдашь же заказчику программу где отладочные сообщения выводятся с помощью print, да и в дальнейшем если у заказчика что то пойдет не так то можно просто попросит показать лог и понять в чем проблема(в большинстве случаев).

В чем же мощь logging:
Легко можно поместить указатель времени в каждое сообщение
Вы можете использовать разные уровни срочности ваших сообщений и фильтровать их по этому уровню
Когда Вы захотите позже найти / изменить лог-сообщения Вы не перепутаете их с другим выводом команды ```print```
Если Вы хотите вывести лог в файл, то очень легко будет игнорировать вывод лог-сообщений

Чтобы начать использовать logging почти ничего делать не надо:

```python
import logging

# Сообщение отладочное
logging.debug( u'This is a debug message' )
# Сообщение информационное
logging.info( u'This is an info message' )
# Сообщение предупреждение
logging.warning( u'This is a warning' )
# Сообщение ошибки
logging.error( u'This is an error message' )
# Сообщение критическое
logging.critical( u'FATAL!!!' )
```

Это только базовая возможность ```logging```, обо всех возможностях по ссылкам:

- [https://docs.python.org/3.5/library/logging.html](https://docs.python.org/3.5/library/logging.html)
- [http://python-lab.blogspot.ru/2012/08/print-logging-python.html](http://python-lab.blogspot.ru/2012/08/print-logging-python.html)
- [http://habrahabr.ru/post/144566/](http://habrahabr.ru/post/144566/)